"""Thin async client for the execution-service HTTP API.

The returned run document is authoritative for ``attempt``, ``lease_version``
and state. Every non-success outcome raises :class:`RuntimeApiError` with a
fixed reason token; none is ever mapped to success, and response text never
enters an exception.
"""

from __future__ import annotations

from typing import Any

import httpx

RUN_STATES = frozenset({"queued", "running", "retry_wait", "succeeded", "failed"})
TERMINAL_RUN_STATES = frozenset({"succeeded", "failed"})
RUNTIME_ERROR_CODES = frozenset(
    {
        "dependency_unavailable",
        "dependency_timeout",
        "worker_error",
        "unknown",
        "invalid_input",
        "invalid_result",
        "unsupported_workflow",
        "side_effect_conflict",
    }
)


class RuntimeApiError(Exception):
    def __init__(self, reason: str, *, existing_run_id: str | None = None) -> None:
        super().__init__(reason)
        self.reason = reason
        self.existing_run_id = existing_run_id


def _error(response: httpx.Response) -> RuntimeApiError:
    try:
        body = response.json()
    except ValueError:
        body = None
    code = body.get("code") if isinstance(body, dict) else None
    status = response.status_code
    if status in (401, 403):
        return RuntimeApiError("runtime_auth_rejected")
    if status == 503 and code == "runtime_draining":
        return RuntimeApiError("runtime_draining")
    if status == 409 and code == "idempotency_conflict":
        existing = body.get("existing_run_id") if isinstance(body, dict) else None
        return RuntimeApiError(
            "idempotency_conflict",
            existing_run_id=existing if isinstance(existing, str) else None,
        )
    if status == 409 and code == "lease_fenced":
        return RuntimeApiError("lease_fenced")
    if status == 404:
        return RuntimeApiError("run_not_found")
    if status == 400:
        return RuntimeApiError("runtime_invalid_request")
    return RuntimeApiError("runtime_protocol_error")


def _run(response: httpx.Response) -> dict[str, Any]:
    try:
        run = response.json()
    except ValueError:
        raise RuntimeApiError("runtime_protocol_error") from None
    if not (
        isinstance(run, dict)
        and isinstance(run.get("run_id"), str)
        and run.get("state") in RUN_STATES
        and type(run.get("attempt")) is int
        and type(run.get("max_attempts")) is int
        and type(run.get("lease_version")) is int
        and isinstance(run.get("input_ref"), dict)
    ):
        raise RuntimeApiError("runtime_protocol_error")
    return run


class RuntimeClient:
    """Client for the execution-service API over a borrowed transport.

    The transport belongs to the caller. No request enters, exits or closes it,
    so completing, failing or cancelling one request cannot close the pool that
    another request or lease maintenance is using. The caller closes it once,
    after joining all work that uses it; closing it while requests are active
    is unsupported. The client holds no event-loop state: one instance over a
    loop-free transport may serve separate event loops, while a real pooled
    transport stays within the one loop its owner uses.
    """

    def __init__(
        self,
        *,
        transport: httpx.AsyncBaseTransport,
        base_url: str = "http://127.0.0.1:8080",
        token: str | None = None,
        timeout: float = 30.0,
    ) -> None:
        self.transport = transport
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.timeout = timeout

    async def _request(
        self, method: str, path: str, body: dict[str, Any] | None = None
    ) -> httpx.Response:
        headers = {"Authorization": f"Bearer {self.token}"} if self.token else {}
        try:
            # A per-request client only builds the request, sends it, and reads
            # and closes the response, also on error or cancellation. It is
            # never entered or closed, since that would enter and close the
            # borrowed transport; with an explicit transport it owns no other.
            client = httpx.AsyncClient(
                base_url=self.base_url,
                transport=self.transport,
                timeout=self.timeout,
                headers=headers,
            )
            return await client.request(method, path, json=body)
        except httpx.TransportError:
            raise RuntimeApiError("runtime_unreachable") from None

    async def submit(
        self,
        *,
        product: str,
        workflow_name: str,
        workflow_version: str,
        idempotency_key: str,
        input_ref: dict[str, Any],
        max_attempts: int,
    ) -> tuple[dict[str, Any], bool]:
        response = await self._request(
            "POST",
            "/v1/runs",
            {
                "product": product,
                "workflow_name": workflow_name,
                "workflow_version": workflow_version,
                "idempotency_key": idempotency_key,
                "input_ref": input_ref,
                "max_attempts": max_attempts,
            },
        )
        if response.status_code not in (200, 201):
            raise _error(response)
        return _run(response), response.status_code == 201

    async def get_run(self, run_id: str) -> dict[str, Any]:
        response = await self._request("GET", f"/v1/runs/{run_id}")
        if response.status_code != 200:
            raise _error(response)
        return _run(response)

    async def list_events(self, run_id: str) -> list[dict[str, Any]]:
        response = await self._request("GET", f"/v1/runs/{run_id}/events")
        if response.status_code != 200:
            raise _error(response)
        try:
            events = response.json()
        except ValueError:
            raise RuntimeApiError("runtime_protocol_error") from None
        if not isinstance(events, list) or not all(isinstance(e, dict) for e in events):
            raise RuntimeApiError("runtime_protocol_error")
        return events

    async def claim(
        self,
        *,
        product: str,
        workflow_name: str,
        workflow_version: str,
        lease_owner: str,
        lease_duration_seconds: int,
    ) -> dict[str, Any] | None:
        response = await self._request(
            "POST",
            "/v1/worker/claims",
            {
                "product": product,
                "workflow_name": workflow_name,
                "workflow_version": workflow_version,
                "lease_owner": lease_owner,
                "lease_duration_seconds": lease_duration_seconds,
            },
        )
        if response.status_code == 204:
            return None
        if response.status_code != 200:
            raise _error(response)
        return _run(response)

    async def _mutate(self, run_id: str, action: str, body: dict[str, Any]):
        response = await self._request("POST", f"/v1/runs/{run_id}/{action}", body)
        if response.status_code != 200:
            raise _error(response)
        return _run(response)

    async def heartbeat(
        self,
        run_id: str,
        *,
        lease_owner: str,
        lease_version: int,
        lease_duration_seconds: int,
    ) -> dict[str, Any]:
        return await self._mutate(
            run_id,
            "heartbeat",
            {
                "lease_owner": lease_owner,
                "lease_version": lease_version,
                "lease_duration_seconds": lease_duration_seconds,
            },
        )

    async def complete(
        self,
        run_id: str,
        *,
        lease_owner: str,
        lease_version: int,
        output_ref: dict[str, Any],
    ) -> dict[str, Any]:
        return await self._mutate(
            run_id,
            "complete",
            {
                "lease_owner": lease_owner,
                "lease_version": lease_version,
                "output_ref": output_ref,
            },
        )

    async def fail(
        self,
        run_id: str,
        *,
        lease_owner: str,
        lease_version: int,
        error_code: str,
        error_summary: str | None = None,
    ) -> dict[str, Any]:
        body: dict[str, Any] = {
            "lease_owner": lease_owner,
            "lease_version": lease_version,
            "error_code": error_code,
        }
        if error_summary is not None:
            body["error_summary"] = error_summary
        return await self._mutate(run_id, "fail", body)

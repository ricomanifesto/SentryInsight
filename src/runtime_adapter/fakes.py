"""Synthetic test doubles for local recovery tests and the demo.

These fakes model the expected execution-service API, a provider with an independent
acceptance ledger, and a publisher. They keep durable state in small JSON files
so a restarted worker or a separate process observes the same history. They are
API test doubles, not conformance evidence for the real services.
"""

from __future__ import annotations

import asyncio
import contextlib
import fcntl
import json
import re
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Iterator, Mapping, Sequence

import httpx

from .durable import atomic_write_bytes
from .identity import canonical_json, sha256_hex
from .publication import PublisherAckLost, PublisherConflict, PublisherUnavailable
from .runtime_client import RUNTIME_ERROR_CODES

_RUN_NAMESPACE = uuid.UUID("6f1c7d36-6c35-4f55-9d0e-3a0f3a9bb1d0")
_RETRY_CODES = frozenset(
    {"dependency_unavailable", "dependency_timeout", "worker_error", "unknown"}
)


@contextlib.contextmanager
def _file_lock(path: Path) -> Iterator[None]:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path.with_name(path.name + ".lock"), "a+b") as handle:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def _read_json(path: Path, default: Any) -> Any:
    try:
        return json.loads(path.read_bytes())
    except FileNotFoundError:
        return default


class SimulatedCrash(BaseException):
    """Stands in for process death at a fault point; no handler may catch it."""


class SyntheticClock:
    """Injected wall clock in seconds, shared through a file across processes."""

    def __init__(self, path: Path, start: float = 1_800_000_000.0) -> None:
        self.path = Path(path)
        with _file_lock(self.path):
            if not self.path.exists():
                atomic_write_bytes(self.path, canonical_json({"now": start}))

    def now(self) -> float:
        return float(_read_json(self.path, {})["now"])

    def advance(self, seconds: float) -> None:
        with _file_lock(self.path):
            now = self.now() + float(seconds)
            atomic_write_bytes(self.path, canonical_json({"now": now}))


class ManualTicker:
    """Injected wait for lease maintenance; a wait ends only when ticked.

    ``tick`` advances the synthetic clock by the interval the waiter asked for
    and wakes it, so a test decides exactly when heartbeats happen and no real
    time passes. ``fail`` makes the pending wait raise instead.
    """

    def __init__(self, clock: SyntheticClock) -> None:
        self.clock = clock
        self.requested: list[float] = []
        self._waiters: list[tuple[asyncio.Future[None], float]] = []

    @property
    def waiting(self) -> int:
        return sum(1 for future, _ in self._waiters if not future.done())

    async def wait(self, seconds: float) -> None:
        self.requested.append(seconds)
        future = asyncio.get_running_loop().create_future()
        entry = (future, seconds)
        self._waiters.append(entry)
        try:
            await future
        finally:
            self._waiters.remove(entry)

    def _pending(self) -> tuple[asyncio.Future[None], float] | None:
        return next((w for w in self._waiters if not w[0].done()), None)

    def tick(self) -> bool:
        pending = self._pending()
        if pending is None:
            return False
        self.clock.advance(pending[1])
        pending[0].set_result(None)
        return True

    def fail(self, error: BaseException) -> bool:
        pending = self._pending()
        if pending is None:
            return False
        pending[0].set_exception(error)
        return True


def _timestamp(value: float | None) -> str | None:
    if value is None:
        return None
    moment = datetime.fromtimestamp(value, timezone.utc)
    return moment.isoformat(timespec="milliseconds").replace("+00:00", "Z")


def _api_error(status: int, code: str, **extra: Any) -> httpx.Response:
    return httpx.Response(status, json=dict({"code": code, "message": code}, **extra))


_SUBMIT_FIELDS = {
    "product": str,
    "workflow_name": str,
    "workflow_version": str,
    "idempotency_key": str,
    "input_ref": dict,
    "max_attempts": int,
}
_CLAIM_FIELDS = {
    "product": str,
    "workflow_name": str,
    "workflow_version": str,
    "lease_owner": str,
    "lease_duration_seconds": int,
}
_LEASE_FIELDS = {"lease_owner": str, "lease_version": int}


def _body(request: httpx.Request, required: Mapping[str, type], optional=()) -> dict:
    try:
        body = json.loads(request.content)
    except ValueError:
        return {}
    if not isinstance(body, dict) or set(body) - set(required) - set(optional):
        return {}
    for name, expected in required.items():
        value = body.get(name)
        if type(value) is not expected:
            return {}
        if expected is str and not value.strip():
            return {}
        if expected is int and value < 1:
            return {}
    return body


class FakeRuntimeService:
    """Durable in-process double of the execution-service HTTP API.

    This double uses an injected clock. Claims recover expired leases lazily,
    fencing checks owner, version and ``running``, retry delay is fixed with
    no jitter, and terminal runs are immutable.
    """

    def __init__(self, state_path: Path, clock: SyntheticClock, *, retry_delay=5.0):
        self.path = Path(state_path)
        self.clock = clock
        self.retry_delay = float(retry_delay)
        self.unavailable: str | None = None
        self._drop: list[str] = []

    def transport(self) -> httpx.MockTransport:
        return httpx.MockTransport(self.handle)

    def drop_next_response(self, operation: str) -> None:
        """Apply the next ``operation`` durably, then lose its response."""
        self._drop.append(operation)

    # Inspection for the test harness -----------------------------------

    def _state(self) -> dict[str, Any]:
        return _read_json(self.path, {"runs": {}, "events": {}})

    def runs(self) -> list[dict[str, Any]]:
        return [self._run_json(run) for run in self._state()["runs"].values()]

    def events(self, run_id: str) -> list[dict[str, Any]]:
        return list(self._state()["events"].get(run_id, []))

    def lease_grants(self, run_id: str) -> int:
        return sum(
            1 for e in self.events(run_id) if e["event_type"] == "lease_acquired"
        )

    # HTTP boundary --------------------------------------------------------

    def handle(self, request: httpx.Request) -> httpx.Response:
        if self.unavailable == "unreachable":
            raise httpx.ConnectError("synthetic runtime unreachable")
        if self.unavailable == "draining":
            return _api_error(503, "runtime_draining")
        if self.unavailable == "unauthorized":
            return _api_error(401, "unauthorized")
        if self.unavailable == "forbidden":
            return _api_error(403, "forbidden")
        with _file_lock(self.path):
            state = self._state()
            response, operation = self._route(state, request)
            if operation is not None:
                atomic_write_bytes(self.path, canonical_json(state))
        if operation is not None and operation in self._drop:
            self._drop.remove(operation)
            raise httpx.ReadTimeout("synthetic lost response")
        return response

    def _route(
        self, state: dict[str, Any], request: httpx.Request
    ) -> tuple[httpx.Response, str | None]:
        path, method = request.url.path, request.method
        if path == "/v1/runs" and method == "POST":
            return self._submit(state, request)
        if path == "/v1/worker/claims" and method == "POST":
            return self._claim(state, request)
        match = re.fullmatch(r"/v1/runs/([^/]+)(?:/([a-z]+))?", path)
        if match is None:
            return _api_error(404, "not_found"), None
        run_id, action = match.groups()
        run = state["runs"].get(run_id)
        if method == "GET" and action is None:
            if run is None:
                return _api_error(404, "run_not_found"), None
            return httpx.Response(200, json=self._run_json(run)), None
        if method == "GET" and action == "events":
            if run is None:
                return _api_error(404, "run_not_found"), None
            return httpx.Response(200, json=state["events"][run_id]), None
        if method == "POST" and action in ("heartbeat", "complete", "fail"):
            return self._mutate(state, run_id, action, request)
        return _api_error(404, "not_found"), None

    def _event(self, state, run, event_type, actor, from_state, to_state, **extra):
        events = state["events"].setdefault(run["run_id"], [])
        event = {
            "run_id": run["run_id"],
            "sequence": len(events) + 1,
            "event_type": event_type,
            "actor_type": actor[0],
            "attempt": run["attempt"],
            "lease_version": run["lease_version"],
            "metadata": {},
            "occurred_at": _timestamp(self.clock.now()),
        }
        if actor[1]:
            event["actor_id"] = actor[1]
        if from_state:
            event["from_state"] = from_state
        if to_state:
            event["to_state"] = to_state
        if extra.get("error_code"):
            event["error_code"] = extra["error_code"]
        events.append(event)

    @staticmethod
    def _run_json(run: dict[str, Any]) -> dict[str, Any]:
        document = {
            key: run[key]
            for key in (
                "run_id",
                "product",
                "workflow_name",
                "workflow_version",
                "state",
                "attempt",
                "max_attempts",
                "lease_version",
                "input_ref",
            )
        }
        for key in ("lease_owner", "output_ref", "error_code", "error_summary"):
            if run.get(key) is not None:
                document[key] = run[key]
        for key in (
            "lease_expires_at",
            "last_heartbeat_at",
            "next_available_at",
            "created_at",
            "updated_at",
        ):
            if run.get(key) is not None:
                document[key] = _timestamp(run[key])
        return document

    def _submit(self, state, request):
        body = _body(request, _SUBMIT_FIELDS)
        if not body:
            return _api_error(400, "invalid_request"), None
        request_hash = sha256_hex(
            canonical_json(
                {key: body[key] for key in _SUBMIT_FIELDS if key != "idempotency_key"}
            )
        )
        identity = (body["product"], body["workflow_name"], body["idempotency_key"])
        for run in state["runs"].values():
            if (run["product"], run["workflow_name"], run["idempotency_key"]) == (
                identity
            ):
                if run["request_hash"] != request_hash:
                    return (
                        _api_error(
                            409, "idempotency_conflict", existing_run_id=run["run_id"]
                        ),
                        None,
                    )
                return httpx.Response(200, json=self._run_json(run)), None
        now = self.clock.now()
        run_id = str(uuid.uuid5(_RUN_NAMESPACE, "\0".join(identity)))
        run = dict(
            {key: body[key] for key in _SUBMIT_FIELDS},
            run_id=run_id,
            request_hash=request_hash,
            state="queued",
            attempt=0,
            lease_version=0,
            created_at=now,
            updated_at=now,
        )
        state["runs"][run_id] = run
        self._event(state, run, "submitted", ("runtime", None), None, "queued")
        return httpx.Response(201, json=self._run_json(run)), "submit"

    def _claim(self, state, request):
        body = _body(request, _CLAIM_FIELDS)
        if not body:
            return _api_error(400, "invalid_request"), None
        now = self.clock.now()
        scope = (body["product"], body["workflow_name"], body["workflow_version"])
        recovered = False
        while True:
            eligible = [
                run
                for run in state["runs"].values()
                if (run["product"], run["workflow_name"], run["workflow_version"])
                == scope
                and (
                    run["state"] == "queued"
                    or (
                        run["state"] == "retry_wait" and run["next_available_at"] <= now
                    )
                    or (run["state"] == "running" and run["lease_expires_at"] < now)
                )
            ]
            if not eligible:
                return httpx.Response(204), ("claim" if recovered else None)

            def order(run):
                due = (
                    run["lease_expires_at"]
                    if run["state"] == "running"
                    else run.get("next_available_at")
                )
                return (due is None, due or 0.0, run["created_at"], run["run_id"])

            run = min(eligible, key=order)
            from_state = run["state"]
            if from_state != "running":
                break
            recovered = True
            run.update(
                state="retry_wait",
                lease_owner=None,
                lease_expires_at=None,
                next_available_at=now,
                updated_at=now,
            )
            self._event(
                state, run, "lease_expired", ("runtime", None), "running", "retry_wait"
            )
            if run["attempt"] >= run["max_attempts"]:
                run.update(
                    state="failed",
                    next_available_at=None,
                    error_code="worker_error",
                    error_summary="lease expired and attempt budget exhausted",
                )
                self._event(
                    state,
                    run,
                    "failed",
                    ("runtime", None),
                    "retry_wait",
                    "failed",
                    error_code="worker_error",
                )
                continue
            self._event(
                state,
                run,
                "retry_scheduled",
                ("runtime", None),
                "retry_wait",
                "retry_wait",
            )
            from_state = "retry_wait"
            break
        run.update(
            state="running",
            attempt=run["attempt"] + 1,
            lease_owner=body["lease_owner"],
            lease_version=run["lease_version"] + 1,
            lease_expires_at=now + body["lease_duration_seconds"],
            last_heartbeat_at=now,
            next_available_at=None,
            error_code=None,
            error_summary=None,
            updated_at=now,
        )
        self._event(
            state,
            run,
            "lease_acquired",
            ("worker", body["lease_owner"]),
            from_state,
            "running",
        )
        return httpx.Response(200, json=self._run_json(run)), "claim"

    def _mutate(self, state, run_id, action, request):
        if action == "heartbeat":
            body = _body(request, dict(_LEASE_FIELDS, lease_duration_seconds=int))
        elif action == "complete":
            body = _body(request, dict(_LEASE_FIELDS, output_ref=dict))
        else:
            body = _body(
                request, _LEASE_FIELDS, optional=("error_code", "error_summary")
            )
            summary = body.get("error_summary", "")
            if body and (
                body.get("error_code") not in RUNTIME_ERROR_CODES
                or not isinstance(summary, str)
                or len(summary) > 512
            ):
                body = {}
        if not body:
            return _api_error(400, "invalid_request"), None
        run = state["runs"].get(run_id)
        if run is None:
            return _api_error(404, "run_not_found"), None
        if (
            run["state"] != "running"
            or run.get("lease_owner") != body["lease_owner"]
            or run["lease_version"] != body["lease_version"]
        ):
            return _api_error(409, "lease_fenced"), None
        now = self.clock.now()
        worker = ("worker", body["lease_owner"])
        if action == "heartbeat":
            run.update(
                lease_expires_at=now + body["lease_duration_seconds"],
                last_heartbeat_at=now,
                updated_at=now,
            )
            self._event(state, run, "heartbeat_recorded", worker, "running", "running")
        elif action == "complete":
            run.update(
                state="succeeded",
                output_ref=body["output_ref"],
                lease_owner=None,
                lease_expires_at=None,
                next_available_at=None,
                error_code=None,
                error_summary=None,
                updated_at=now,
            )
            self._event(state, run, "succeeded", worker, "running", "succeeded")
        else:
            code, summary = body["error_code"], body.get("error_summary") or None
            if code in _RETRY_CODES and run["attempt"] < run["max_attempts"]:
                run.update(
                    state="retry_wait",
                    lease_owner=None,
                    lease_expires_at=None,
                    next_available_at=now + self.retry_delay,
                    error_code=code,
                    error_summary=summary,
                    updated_at=now,
                )
                self._event(
                    state,
                    run,
                    "retry_scheduled",
                    worker,
                    "running",
                    "retry_wait",
                    error_code=code,
                )
            else:
                run.update(
                    state="failed",
                    lease_owner=None,
                    lease_expires_at=None,
                    next_available_at=None,
                    error_code=code,
                    error_summary=summary,
                    updated_at=now,
                )
                self._event(
                    state, run, "failed", worker, "running", "failed", error_code=code
                )
        return httpx.Response(200, json=self._run_json(run)), action


def _encode(body: Any) -> bytes:
    if body is None:
        return b""
    if isinstance(body, bytes):
        return body
    if isinstance(body, str):
        return body.encode("utf-8")
    return canonical_json(body)


@dataclass(frozen=True)
class Respond:
    """The provider accepts the request and returns a complete response."""

    status: int
    body: Any = None
    headers: dict[str, str] | None = None
    accepts = True

    async def perform(self) -> httpx.Response:
        return httpx.Response(
            self.status, content=_encode(self.body), headers=self.headers or {}
        )


@dataclass(frozen=True)
class AcceptThenFail:
    """The provider accepts and creates an answer; the caller never receives it."""

    error: Callable[[], BaseException]
    accepts = True

    async def perform(self) -> httpx.Response:
        raise self.error()


@dataclass(frozen=True)
class RefuseConnection:
    """The connection fails before any request bytes reach the provider."""

    error: Callable[[str], BaseException] = httpx.ConnectError
    accepts = False

    async def perform(self) -> httpx.Response:
        raise self.error("synthetic connection refused")


@dataclass(frozen=True)
class AcceptThenWait:
    """The provider accepts, then responds only once ``release`` is set."""

    release: asyncio.Event
    then: Respond
    accepts = True

    async def perform(self) -> httpx.Response:
        await self.release.wait()
        return await self.then.perform()


ProviderStep = Respond | AcceptThenFail | RefuseConnection | AcceptThenWait


class FakeModelService(httpx.AsyncBaseTransport):
    """Scripted provider with an independent durable forward/acceptance ledger.

    ``forwards`` (F) counts invocations of this transport and ``accepted`` (A)
    counts requests the provider durably accepted. The adapter never reads
    either; the script position survives process restarts. Request headers and
    bodies are never stored.
    """

    def __init__(self, ledger_path: Path, script: Sequence[ProviderStep]) -> None:
        self.path = Path(ledger_path)
        self.script = list(script)

    def _ledger(self) -> dict[str, int]:
        return _read_json(self.path, {"forwards": 0, "accepted": 0})

    @property
    def forwards(self) -> int:
        return self._ledger()["forwards"]

    @property
    def accepted(self) -> int:
        return self._ledger()["accepted"]

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        with _file_lock(self.path):
            ledger = self._ledger()
            step = self.script[min(ledger["forwards"], len(self.script) - 1)]
            ledger["forwards"] += 1
            if step.accepts:
                ledger["accepted"] += 1
            atomic_write_bytes(self.path, canonical_json(ledger))
        return await step.perform()


class FakePublisher:
    """Durable publisher double with observation by operation key.

    ``effects`` counts applied publications. ``lose_next_acknowledgement``
    applies the next effect and then reports it as unavailable, and
    ``unavailable_observations`` fails that many observations.
    """

    def __init__(self, state_path: Path) -> None:
        self.path = Path(state_path)
        self.lose_next_acknowledgement = False
        self.unavailable_observations = 0

    def _state(self) -> dict[str, Any]:
        return _read_json(self.path, {"targets": {}, "receipts": {}, "effects": 0})

    @property
    def effects(self) -> int:
        return self._state()["effects"]

    def current(self, target: str) -> str | None:
        return self._state()["targets"].get(target)

    def seed(self, target: str, artifact_sha256: str) -> None:
        with _file_lock(self.path):
            state = self._state()
            state["targets"][target] = artifact_sha256
            atomic_write_bytes(self.path, canonical_json(state))

    def observe(self, operation_key: str) -> dict[str, Any] | None:
        if self.unavailable_observations:
            self.unavailable_observations -= 1
            raise PublisherUnavailable()
        return self._state()["receipts"].get(operation_key)

    def publish(
        self,
        operation_key: str,
        *,
        target: str,
        artifact_sha256: str,
        expected_remote: str | None,
    ) -> dict[str, Any]:
        with _file_lock(self.path):
            state = self._state()
            if state["targets"].get(target) != expected_remote:
                raise PublisherConflict()
            receipt = {
                "receipt_id": "receipt-" + operation_key[:16],
                "target": target,
                "artifact_sha256": artifact_sha256,
            }
            state["targets"][target] = artifact_sha256
            state["receipts"][operation_key] = receipt
            state["effects"] += 1
            atomic_write_bytes(self.path, canonical_json(state))
        if self.lose_next_acknowledgement:
            self.lose_next_acknowledgement = False
            raise PublisherAckLost()
        return receipt

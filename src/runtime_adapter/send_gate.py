"""Product-owned provider send gate at the legacy client's transport seam.

Before any forward the gate confirms the lease, then makes one crash-consistent
reservation (R += 1) that checks for an open or ambiguous intent, the budget
and any persisted not-before. It re-checks the lease immediately before the
inner transport is invoked. A complete response is captured durably before the
unchanged client parses it, and captured outcomes not yet consumed by a later
record are replayed in order instead of forwarding again.

Every reservation ends in one disposition decided from what the gate observed:
``resolved`` (complete response captured), ``failed_before_forward`` (refused
before the inner transport, or a connection/pool failure that httpx raises only
before request bytes are sent) or ``ambiguous`` (anything else once forwarding
began, including a failed capture). An ambiguous intent is never retried: the
gate raises :class:`SendGateRefusal`, which the legacy client does not retry,
and refuses every later forward for the job. Remote requests that already
started cannot be retracted; exactly-once delivery is not claimed.

The gate never sleeps, never stores request or response headers, and records
fixed tokens, never exception names or messages.
"""

from __future__ import annotations

import asyncio
import math
from datetime import datetime
from email.utils import parsedate_to_datetime
from typing import Any, Awaitable, Callable

import httpx

from src.core.openrouter_client import OpenRouterError

from .checkpoint import (
    CheckpointStateStale,
    CheckpointStore,
    CheckpointStoreError,
    ReservationRefused,
    StaleLeaseWrite,
    ledger_view,
)
from .identity import sha256_hex
from .runtime_client import RuntimeApiError, RuntimeClient

DEFAULT_BUDGET = 3
# httpx raises these only while establishing a connection or acquiring one.
PRE_SEND_ERRORS = (httpx.ConnectError, httpx.ConnectTimeout, httpx.PoolTimeout)
_STORE_REFUSALS: dict[type[Exception], str] = {
    StaleLeaseWrite: "lease_lost",
    CheckpointStoreError: "checkpoint_store_failed",
    CheckpointStateStale: "checkpoint_state_stale",
}


class SendGateRefusal(httpx.TransportError):
    """Non-retryable refusal for the legacy client; the reason is a fixed token.

    It subclasses the httpx base transport error but none of the classes the
    legacy client retries, so the client's in-call loop stops immediately.
    """

    def __init__(self, reason: str) -> None:
        super().__init__(reason)
        self.reason = reason


class Lease:
    """The worker's current Runtime lease, shared with the gate.

    While ``run_once`` owns the lease, :meth:`maintain` renews it from a task
    that only heartbeats this lease: it never claims, submits, sends to the
    provider, changes a budget or decides a retry. The first heartbeat failure,
    from maintenance or any other caller, is kept in ``problem`` so the gate and
    the worker stop instead of continuing on an unconfirmed lease.
    """

    def __init__(
        self,
        *,
        run_id: str,
        owner: str,
        version: int,
        duration: int = 600,
        runtime: RuntimeClient | None = None,
    ) -> None:
        self.run_id = run_id
        self.owner = owner
        self.version = version
        self.duration = duration
        self.runtime = runtime
        self.lost = False
        self.problem: str | None = None
        self._maintenance: asyncio.Future[None] | None = None
        self._released: asyncio.Future[None] | None = None

    async def confirm(self) -> str | None:
        """Heartbeat; return a fixed reason when the lease cannot be confirmed."""
        if self.lost:
            return "lease_lost"
        if self.problem is not None:
            return self.problem
        if self.runtime is None:
            return None
        try:
            await self.runtime.heartbeat(
                self.run_id,
                lease_owner=self.owner,
                lease_version=self.version,
                lease_duration_seconds=self.duration,
            )
        except RuntimeApiError as error:
            self._note_problem(error.reason)
            return "lease_lost" if self.lost else self.problem
        return None

    def _note_problem(self, reason: str) -> None:
        if reason == "lease_fenced":
            self.lost = True
            reason = "lease_lost"
        if self.problem is None:
            self.problem = reason

    def maintain(
        self, interval: float, wait: Callable[[float], Awaitable[None]]
    ) -> None:
        """Renew the lease every ``interval`` seconds until :meth:`release`."""
        if self.runtime is not None and self._maintenance is None:
            self._maintenance = asyncio.ensure_future(self._renew(interval, wait))

    async def _renew(
        self, interval: float, wait: Callable[[float], Awaitable[None]]
    ) -> None:
        try:
            while True:
                await wait(interval)
                if await self.confirm() is not None:
                    return
        except asyncio.CancelledError:
            # Only release() stops maintenance on purpose. Any other
            # cancellation, including one raised by the wait, is a fault.
            if self._released is not asyncio.current_task():
                self._note_problem("worker_unclassified")
            raise
        except Exception:
            # A maintenance fault is never silent; the worker reports it.
            self._note_problem("worker_unclassified")

    async def release(self) -> None:
        """Stop maintenance and wait until its task has finished."""
        task, self._maintenance = self._maintenance, None
        if task is not None:
            self._released = task
            task.cancel()
            await asyncio.wait({task})


def fault_token(error: BaseException) -> str:
    """Map an exception to a fixed token without using its name or message."""
    if isinstance(error, asyncio.CancelledError):
        return "cancelled"
    for kind, token in (
        (httpx.ConnectTimeout, "connect_timeout"),
        (httpx.PoolTimeout, "pool_timeout"),
        (httpx.ConnectError, "connect_error"),
        (httpx.WriteTimeout, "write_timeout"),
        (httpx.ReadTimeout, "read_timeout"),
        (httpx.TimeoutException, "timeout"),
        (httpx.WriteError, "write_error"),
        (httpx.ReadError, "read_error"),
        (httpx.CloseError, "close_error"),
        (httpx.RemoteProtocolError, "remote_protocol"),
        (httpx.TransportError, "transport_error"),
    ):
        if isinstance(error, kind):
            return token
    return "unexpected"


def parse_retry_after(value: str | None, received_at: float) -> int | None:
    """Return one absolute not-before instant, fixed at capture time."""
    if not value:
        return None
    try:
        seconds = float(value)
    except ValueError:
        try:
            retry_at: datetime = parsedate_to_datetime(value)
        except (TypeError, ValueError, OverflowError):
            return None
        if retry_at.tzinfo is None:
            return None
        return math.ceil(retry_at.timestamp())
    if not math.isfinite(seconds) or seconds < 0:
        return None
    return math.ceil(received_at + seconds)


class ProviderSendGate(httpx.AsyncBaseTransport):
    def __init__(
        self,
        *,
        store: CheckpointStore,
        job_id: str,
        lease: Lease,
        inner: httpx.AsyncBaseTransport,
        clock: Callable[[], float],
        budget: int = DEFAULT_BUDGET,
        fault: Callable[[str], Awaitable[None]] | None = None,
    ) -> None:
        self.store = store
        self.job_id = job_id
        self.lease = lease
        self.inner = inner
        self.clock = clock
        self.budget = budget
        self.fault = fault
        self.delivered: list[int] = []
        self.reserved: list[int] = []
        self.unresolved: list[int] = []
        self.refusal_reason: str | None = None
        self.halted: str | None = None
        self._replay_queue: list[dict[str, Any]] | None = None

    # Refusals and dispositions ------------------------------------------

    def halt(self, reason: str) -> SendGateRefusal:
        """Refuse every later replay or forward in this process.

        Used when a mandatory retry checkpoint cannot be read or written; an
        earlier refusal reason, such as an unresolved intent, is kept.
        """
        if self.halted is None:
            self.halted = reason
        if self.refusal_reason is None:
            self.refusal_reason = reason
        return SendGateRefusal(reason)

    def _refuse(self, reason: str, *, persist: bool = False) -> SendGateRefusal:
        self.refusal_reason = reason
        if persist:
            try:
                self.store.append(
                    self.job_id,
                    self.lease.version,
                    {"type": "refusal", "reason": reason, "at": self.clock()},
                )
            except (CheckpointStoreError, CheckpointStateStale, StaleLeaseWrite):
                pass
        return SendGateRefusal(reason)

    def _record(self, seq: int, outcome: dict[str, Any]) -> bool:
        try:
            self.store.record_outcome(self.job_id, self.lease.version, seq, outcome)
        except (CheckpointStoreError, CheckpointStateStale, StaleLeaseWrite):
            return False
        return True

    def _ambiguous(self, seq: int, fault: str) -> None:
        # If this write fails the reservation stays open, which recovery also
        # treats as ambiguous.
        self.unresolved.append(seq)
        self._record(seq, {"disposition": "ambiguous", "fault": fault})

    def _lease_problem(self) -> str | None:
        if self.lease.lost:
            return "lease_lost"
        if self.lease.problem is not None:
            return self.lease.problem
        try:
            record = self.store.load(self.job_id)
        except (CheckpointStoreError, CheckpointStateStale) as error:
            return error.reason
        if record is None or record["highest_lease_version"] != self.lease.version:
            return "lease_lost"
        return None

    async def _fault_point(self, name: str) -> None:
        if self.fault is not None:
            await self.fault(name)

    def _response(
        self, status: int, content: bytes, not_before: int | None
    ) -> httpx.Response:
        headers = {}
        if not_before is not None:
            # Present the fixed deadline as the time remaining now; never rebase.
            remaining = max(0, math.ceil(not_before - self.clock()))
            headers["Retry-After"] = str(remaining)
        return httpx.Response(status, content=content, headers=headers)

    # Replay ---------------------------------------------------------------

    def _next_replay(self) -> dict[str, Any] | None:
        if self._replay_queue is None:
            try:
                record = self.store.load(self.job_id)
            except (CheckpointStoreError, CheckpointStateStale):
                record = None
            self._replay_queue = (
                ledger_view(record).unconsumed_resolved if record else []
            )
        return self._replay_queue.pop(0) if self._replay_queue else None

    def _replay(self, outcome: dict[str, Any], request_sha256: str) -> httpx.Response:
        seq = outcome["reservation"]
        if self.lease.lost:
            raise self._refuse("lease_lost")
        try:
            record = self.store.load(self.job_id)
            reservation = ledger_view(record).reservation(seq) if record else None
            if reservation is None or reservation["request_sha256"] != request_sha256:
                raise CheckpointStateStale()
            content = self.store.get_blob(self.job_id, outcome["body_sha256"])
            self.store.append(
                self.job_id, self.lease.version, {"type": "replay", "reservation": seq}
            )
        except (StaleLeaseWrite, CheckpointStoreError, CheckpointStateStale) as error:
            raise self._refuse(_STORE_REFUSALS[type(error)]) from None
        self.delivered.append(seq)
        return self._response(outcome["http_status"], content, outcome["not_before"])

    # Forwarding -----------------------------------------------------------

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        if self.halted is not None:
            raise SendGateRefusal(self.halted)
        request_sha256 = sha256_hex(await request.aread())
        replay = self._next_replay()
        if replay is not None:
            return self._replay(replay, request_sha256)

        problem = await self.lease.confirm()
        if problem is not None:
            raise self._refuse(problem)
        try:
            seq = self.store.reserve(
                self.job_id,
                self.lease.version,
                request_sha256=request_sha256,
                now=self.clock(),
                budget=self.budget,
            )
        except ReservationRefused as refused:
            raise self._refuse(refused.reason, persist=True) from None
        except (StaleLeaseWrite, CheckpointStoreError, CheckpointStateStale) as error:
            raise self._refuse(_STORE_REFUSALS[type(error)]) from None
        self.reserved.append(seq)

        await self._fault_point("after_reservation")
        problem = self._lease_problem()
        if problem is not None:
            self._record(
                seq, {"disposition": "failed_before_forward", "fault": problem}
            )
            raise self._refuse(problem)

        try:
            response = await self.inner.handle_async_request(request)
        except PRE_SEND_ERRORS as error:
            outcome = {
                "disposition": "failed_before_forward",
                "fault": fault_token(error),
            }
            if not self._record(seq, outcome):
                raise self._refuse("checkpoint_store_failed") from None
            self.delivered.append(seq)
            raise
        except BaseException as error:
            self._ambiguous(seq, fault_token(error))
            if not isinstance(error, Exception):
                raise
            raise self._refuse("provider_intent_unresolved") from None

        try:
            content = await response.aread()
        except BaseException as error:
            self._ambiguous(seq, fault_token(error))
            if not isinstance(error, Exception):
                raise
            raise self._refuse("provider_intent_unresolved") from None
        finally:
            await response.aclose()

        received_at = self.clock()
        not_before = parse_retry_after(response.headers.get("Retry-After"), received_at)
        try:
            body_sha256 = self.store.put_blob(self.job_id, content)
            self.store.record_outcome(
                self.job_id,
                self.lease.version,
                seq,
                {
                    "disposition": "resolved",
                    "http_status": response.status_code,
                    "body_sha256": body_sha256,
                    "not_before": not_before,
                    "received_at": received_at,
                },
            )
        except (CheckpointStoreError, CheckpointStateStale, StaleLeaseWrite):
            self._ambiguous(seq, "capture_failed")
            raise self._refuse("provider_intent_unresolved") from None

        await self._fault_point("after_capture")
        problem = self._lease_problem()
        if problem is not None:
            # A stale process keeps its captured outcome but never promotes it.
            raise self._refuse(problem)
        self.delivered.append(seq)
        return self._response(response.status_code, content, not_before)


class JitterPolicy:
    """Adapter-owned delay policy for the legacy client's in-call retries.

    The client passes the required floor (backoff and Retry-After) and its cap
    and clamps the result to that interval. Positive jitter is drawn from the
    injected randomness over the headroom, at most the floor itself, so it can
    never move a send earlier. The sample is recorded with the outcome it
    follows and reused when that outcome is replayed after a restart.

    A sample that cannot be read or recorded durably halts the gate and stops
    the client's in-call loop, so it never waits on or sends after an
    unrecorded decision.
    """

    def __init__(
        self, gate: ProviderSendGate | None, random: Callable[[], float]
    ) -> None:
        self.gate = gate
        self.random = random

    def __call__(self, floor: float, cap: float) -> float:
        gate = self.gate
        follows = gate.delivered[-1] if gate is not None and gate.delivered else None
        if gate is not None and follows is not None:
            try:
                record = gate.store.load(gate.job_id)
            except (CheckpointStoreError, CheckpointStateStale) as error:
                raise gate.halt(_STORE_REFUSALS[type(error)]) from None
            recorded = ledger_view(record).delay_sample(follows) if record else None
            if recorded is not None:
                return float(recorded["delay"])
        headroom = max(0.0, cap - floor)
        sample = min(max(float(self.random()), 0.0), 1.0)
        delay = floor + min(headroom, floor) * sample
        if gate is not None:
            try:
                gate.store.append(
                    gate.job_id,
                    gate.lease.version,
                    {
                        "type": "delay_sample",
                        "follows": follows,
                        "floor": floor,
                        "cap": cap,
                        "delay": delay,
                        "headroom": headroom,
                    },
                )
            except (
                CheckpointStoreError,
                CheckpointStateStale,
                StaleLeaseWrite,
            ) as error:
                raise gate.halt(_STORE_REFUSALS[type(error)]) from None
        return delay


class RetryDispositionRecorder:
    """Wrapper at the ``model_client`` injection point of the analysis.

    On ``OpenRouterError`` it records the sanitized legacy retry disposition
    for the current reservation and re-raises the same exception, so the
    unchanged analysis flattens it exactly as before. If that record cannot be
    written, ``persisted`` stays false and the gate halts with the store's
    fixed reason, so no decision is taken from the in-memory copy alone.
    """

    def __init__(self, client: Any, gate: ProviderSendGate) -> None:
        self.client = client
        self.gate = gate
        self.disposition: dict[str, Any] | None = None
        self.persisted = False

    async def generate(self, **kwargs: Any) -> str:
        try:
            return await self.client.generate(**kwargs)
        except OpenRouterError as error:
            self.disposition = {
                "http_status": _bounded_int(error.http_status),
                "provider_code": _bounded_int(error.provider_code),
                "attempts": _bounded_int(error.attempts),
                "retryable": error.retryable is True,
            }
            gate = self.gate
            follows = gate.delivered[-1] if gate.delivered else None
            try:
                gate.store.append(
                    gate.job_id,
                    gate.lease.version,
                    dict(self.disposition, type="retry_disposition", follows=follows),
                )
                self.persisted = True
            except (
                CheckpointStoreError,
                CheckpointStateStale,
                StaleLeaseWrite,
            ) as fault:
                self.persisted = False
                gate.halt(_STORE_REFUSALS[type(fault)])
            raise


def _bounded_int(value: Any) -> int | None:
    return value if type(value) is int and 0 <= value < 10**6 else None

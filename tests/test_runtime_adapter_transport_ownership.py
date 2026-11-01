"""RuntimeClient borrows its injected transport.

The transport given to ``RuntimeClient`` belongs to the caller, who closes it
once after joining every task that uses it. A completed, failed or cancelled
request must therefore never enter, exit or close it: closing a real pooled
transport drops the connections of every other in-flight request on it,
including lease maintenance.

``BorrowedTransport`` records lifecycle calls and models that harm: closing it
while requests are held fails each held request with a transport error.
``TrackedStream`` shows that per-request response cleanup still happens.
``LoopbackPeer`` is a finite HTTP/1.1 peer for a real ``httpx.AsyncHTTPTransport``.
Principal request and synchronization waits are bounded; a timeout is a failure.
"""

import asyncio
import contextlib
import gc
import itertools
import json
import socket

import httpx
import pytest

from src.runtime_adapter.fakes import FakeRuntimeService, ManualTicker, SyntheticClock
from src.runtime_adapter.identity import PRODUCT, WORKFLOW_NAME, WORKFLOW_VERSION
from src.runtime_adapter.runtime_client import RuntimeApiError, RuntimeClient
from src.runtime_adapter.send_gate import Lease

BOUND = 5.0
HELD = "11111111-1111-4111-8111-111111111111"
OTHER = "22222222-2222-4222-8222-222222222222"
THIRD = "33333333-3333-4333-8333-333333333333"
INPUT_REF = {"kind": "sentryinsight.frozen_job", "manifest_sha256": "a" * 64}
NO_LIFECYCLE = {"enter": 0, "exit": 0, "close": 0}


def run_doc(run_id: str) -> dict:
    return {
        "run_id": run_id,
        "state": "queued",
        "attempt": 0,
        "max_attempts": 3,
        "lease_version": 0,
        "input_ref": INPUT_REF,
    }


async def bounded(awaitable, seconds: float = BOUND):
    return await asyncio.wait_for(awaitable, seconds)


async def until(predicate, rounds: int = 2000) -> None:
    """Let other tasks run until ``predicate`` holds; no real time passes."""
    for _ in range(rounds):
        if predicate():
            return
        await asyncio.sleep(0)
    raise AssertionError("condition not reached")


async def settle(task: asyncio.Task):
    """A request's outcome as data, so an assertion shows what happened."""
    try:
        return "returned", await bounded(task)
    except RuntimeApiError as error:
        return "runtime_error", error.reason
    except asyncio.CancelledError:
        return "cancelled", None
    except TimeoutError:
        return "timeout", None


async def cancel_others() -> None:
    """Finite teardown: stop any task a failed scenario left behind."""
    others = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
    for task in others:
        task.cancel()
    if others:
        await asyncio.wait(others, timeout=BOUND)


# A borrowed transport that counts lifecycle calls and models their harm ---------


class Hold:
    def __init__(self) -> None:
        self.armed = True
        self.entered = asyncio.Event()
        self.wake = asyncio.Event()
        self.interrupted = False

    def release(self) -> None:
        self.wake.set()


class BorrowedTransport(httpx.AsyncBaseTransport):
    """Lent to ``RuntimeClient``; records what the product does to it.

    Lifecycle calls are recorded in order. The next request whose path
    contains a held fragment waits at a barrier. Closing or exiting the
    transport while requests are held fails each of them with a transport
    error, as closing a real connection pool does. It never retries and never
    fabricates a response.
    """

    def __init__(self, handler) -> None:
        self.handler = handler
        self.lifecycle: list[str] = []
        self.requests: list[dict] = []
        self.handled: list[str] = []
        self.holds: dict[str, Hold] = {}
        self.active: set[Hold] = set()

    def counts(self) -> dict[str, int]:
        return {call: self.lifecycle.count(call) for call in NO_LIFECYCLE}

    def hold(self, fragment: str) -> Hold:
        self.holds[fragment] = hold = Hold()
        return hold

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        body = await request.aread()
        self.requests.append(
            {
                "method": request.method,
                "url": str(request.url),
                "headers": dict(request.headers),
                "body": body.decode(),
                "timeout": request.extensions.get("timeout"),
            }
        )
        path = request.url.path
        hold = next((h for f, h in self.holds.items() if h.armed and f in path), None)
        if hold is not None:
            hold.armed = False
            self.active.add(hold)
            hold.entered.set()
            try:
                await hold.wake.wait()
            finally:
                self.active.discard(hold)
            if hold.interrupted:
                raise httpx.ReadError("connection closed while the request was held")
        self.handled.append(path)
        return await self.handler(request)

    async def __aenter__(self):
        self.lifecycle.append("enter")
        return self

    async def __aexit__(self, *exc_info) -> None:
        self.lifecycle.append("exit")
        await self.aclose()

    async def aclose(self) -> None:
        self.lifecycle.append("close")
        for hold in list(self.active):
            hold.interrupted = True
            hold.wake.set()


def documents(fail: str | None = None):
    """Synthetic Runtime run documents; ``fail`` names a path that cannot connect."""

    async def handler(request: httpx.Request) -> httpx.Response:
        if fail is not None and fail in request.url.path:
            raise httpx.ConnectError("synthetic connect failure")
        return httpx.Response(200, json=run_doc(request.url.path.rsplit("/", 1)[-1]))

    return handler


# O-1 to O-6: lifecycle and overlap on a borrowed transport ----------------------


def test_requests_never_enter_exit_or_close_the_borrowed_transport():
    transport = BorrowedTransport(documents())
    client = RuntimeClient(transport=transport)

    async def scenario():
        first = await bounded(client.get_run(OTHER))
        second = await bounded(client.get_run(THIRD))
        gc.collect()  # a finalizer-driven close would show up here
        await asyncio.sleep(0)
        before_owner = transport.counts()
        await transport.aclose()  # the owner's single cleanup
        return first, second, before_owner

    first, second, before_owner = asyncio.run(scenario())

    assert (first, second) == (run_doc(OTHER), run_doc(THIRD))
    assert before_owner == NO_LIFECYCLE
    assert transport.lifecycle == ["close"]


def test_a_completed_request_does_not_close_a_peer_still_in_flight():
    transport = BorrowedTransport(documents())
    client = RuntimeClient(transport=transport)

    async def scenario():
        try:
            hold = transport.hold(HELD)
            held = asyncio.create_task(client.get_run(HELD))
            await bounded(hold.entered.wait())
            other = await bounded(client.get_run(OTHER))
            hold.release()
            return await settle(held), other, transport.counts()
        finally:
            await cancel_others()

    held, other, counts = asyncio.run(scenario())

    assert other == run_doc(OTHER)
    assert held == ("returned", run_doc(HELD))
    assert sorted(transport.handled) == [f"/v1/runs/{r}" for r in (HELD, OTHER)]
    assert counts == NO_LIFECYCLE


def test_a_cancelled_request_does_not_close_a_peer_still_in_flight():
    transport = BorrowedTransport(documents())
    client = RuntimeClient(transport=transport)

    async def scenario():
        try:
            first, second = transport.hold(HELD), transport.hold(OTHER)
            held = asyncio.create_task(client.get_run(HELD))
            await bounded(first.entered.wait())
            cancelled = asyncio.create_task(client.get_run(OTHER))
            await bounded(second.entered.wait())
            cancelled.cancel()
            outcome = await settle(cancelled)
            first.release()
            return outcome, await settle(held), transport.counts()
        finally:
            await cancel_others()

    cancelled, held, counts = asyncio.run(scenario())

    # Cancellation propagates as itself, never as a Runtime error.
    assert cancelled == ("cancelled", None)
    assert held == ("returned", run_doc(HELD))
    assert counts == NO_LIFECYCLE


def test_a_failed_request_does_not_close_a_peer_still_in_flight():
    transport = BorrowedTransport(documents(fail=OTHER))
    client = RuntimeClient(transport=transport)

    async def scenario():
        try:
            hold = transport.hold(HELD)
            held = asyncio.create_task(client.get_run(HELD))
            await bounded(hold.entered.wait())
            failed = await settle(asyncio.create_task(client.get_run(OTHER)))
            hold.release()
            return failed, await settle(held), transport.counts()
        finally:
            await cancel_others()

    failed, held, counts = asyncio.run(scenario())

    assert failed == ("runtime_error", "runtime_unreachable")
    assert transport.handled.count(f"/v1/runs/{OTHER}") == 1  # no implicit retry
    assert held == ("returned", run_doc(HELD))
    assert counts == NO_LIFECYCLE


def test_a_confirm_leaves_a_live_maintenance_heartbeat_intact(tmp_path):
    clock = SyntheticClock(tmp_path / "clock.json")
    service = FakeRuntimeService(tmp_path / "runtime.json", clock, retry_delay=5)
    transport = BorrowedTransport(service.transport().handle_async_request)
    client = RuntimeClient(transport=transport)
    ticker = ManualTicker(clock)

    async def scenario():
        try:
            await client.submit(
                product=PRODUCT,
                workflow_name=WORKFLOW_NAME,
                workflow_version=WORKFLOW_VERSION,
                idempotency_key="transport-ownership",
                input_ref=INPUT_REF,
                max_attempts=3,
            )
            run = await client.claim(
                product=PRODUCT,
                workflow_name=WORKFLOW_NAME,
                workflow_version=WORKFLOW_VERSION,
                lease_owner="transport-owner",
                lease_duration_seconds=600,
            )
            lease = Lease(
                run_id=run["run_id"],
                owner="transport-owner",
                version=run["lease_version"],
                duration=600,
                runtime=client,
            )
            hold = transport.hold("/heartbeat")
            lease.maintain(200.0, ticker.wait)
            await until(lambda: ticker.waiting == 1)
            assert ticker.tick()
            await bounded(hold.entered.wait())  # the maintenance heartbeat is held
            explicit = await bounded(lease.confirm())  # a non-terminal request
            hold.release()
            await until(lambda: ticker.waiting == 1 or lease.problem is not None)
            problem = lease.problem
            await bounded(lease.release())
            others = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
            return run["run_id"], explicit, problem, others, transport.counts()
        finally:
            await cancel_others()

    run_id, explicit, problem, others, counts = asyncio.run(scenario())

    heartbeats = [
        e for e in service.events(run_id) if e["event_type"] == "heartbeat_recorded"
    ]
    assert explicit is None
    assert problem is None
    assert len(heartbeats) == 2
    assert others == []
    assert counts == NO_LIFECYCLE


def test_one_client_serves_separate_event_loops_without_lifecycle_calls():
    transport = BorrowedTransport(documents())
    client = RuntimeClient(transport=transport)

    first = asyncio.run(client.get_run(OTHER))
    second = asyncio.run(client.get_run(THIRD))

    assert (first, second) == (run_doc(OTHER), run_doc(THIRD))
    assert transport.counts() == NO_LIFECYCLE


# O-7: the wire shape at the transport boundary is unchanged (guard) -------------


def test_requests_reach_the_transport_with_an_unchanged_wire_shape():
    transport = BorrowedTransport(documents())
    tokened = RuntimeClient(
        transport=transport,
        base_url="http://127.0.0.1:8080/",
        token="synthetic-test-token",
        timeout=12.5,
    )
    plain = RuntimeClient(transport=transport)

    asyncio.run(
        tokened.submit(
            product=PRODUCT,
            workflow_name=WORKFLOW_NAME,
            workflow_version=WORKFLOW_VERSION,
            idempotency_key="wire-shape",
            input_ref=INPUT_REF,
            max_attempts=3,
        )
    )
    asyncio.run(plain.get_run(OTHER))

    posted, fetched = transport.requests
    assert (posted["method"], posted["url"]) == (
        "POST",
        "http://127.0.0.1:8080/v1/runs",
    )
    assert posted["headers"]["authorization"] == "Bearer synthetic-test-token"
    assert posted["headers"]["content-type"] == "application/json"
    assert json.loads(posted["body"]) == {
        "product": PRODUCT,
        "workflow_name": WORKFLOW_NAME,
        "workflow_version": WORKFLOW_VERSION,
        "idempotency_key": "wire-shape",
        "input_ref": INPUT_REF,
        "max_attempts": 3,
    }
    assert posted["timeout"] == dict.fromkeys(
        ("connect", "read", "write", "pool"), 12.5
    )
    assert (fetched["method"], fetched["url"]) == (
        "GET",
        f"http://127.0.0.1:8080/v1/runs/{OTHER}",
    )
    assert "authorization" not in fetched["headers"]
    assert fetched["body"] == ""
    assert fetched["timeout"] == dict.fromkeys(
        ("connect", "read", "write", "pool"), 30.0
    )


# S-1 to S-3: per-request response cleanup still happens --------------------------


class TrackedStream(httpx.AsyncByteStream):
    """A real response body stream that records its own close."""

    def __init__(self, data: bytes, *, error=None, stall: bool = False) -> None:
        self.parts = [data[: len(data) // 2], data[len(data) // 2 :]]
        self.error = error
        self.stall = stall
        self.closes = 0
        self.reading = asyncio.Event()
        self.never = asyncio.Event()

    async def __aiter__(self):
        yield self.parts[0]
        self.reading.set()
        if self.stall:
            await self.never.wait()
        if self.error is not None:
            raise self.error
        yield self.parts[1]

    async def aclose(self) -> None:
        self.closes += 1


def streaming(**options):
    streams: list[TrackedStream] = []

    async def handler(request: httpx.Request) -> httpx.Response:
        body = json.dumps(run_doc(request.url.path.rsplit("/", 1)[-1])).encode()
        streams.append(stream := TrackedStream(body, **options))
        return httpx.Response(
            200, headers={"content-type": "application/json"}, stream=stream
        )

    return handler, streams


@pytest.mark.parametrize(
    "case",
    ["consumed", "read_error", "cancelled_while_reading"],
)
def test_the_response_stream_is_closed_on_every_path(case):
    options = {
        "consumed": {},
        "read_error": {"error": httpx.ReadError("synthetic read failure")},
        "cancelled_while_reading": {"stall": True},
    }[case]
    handler, streams = streaming(**options)
    transport = BorrowedTransport(handler)
    client = RuntimeClient(transport=transport)

    async def scenario():
        try:
            request = asyncio.create_task(client.get_run(OTHER))
            if case == "cancelled_while_reading":
                await until(lambda: bool(streams) and streams[0].reading.is_set())
                request.cancel()
            return await settle(request), transport.counts()
        finally:
            await cancel_others()

    outcome, counts = asyncio.run(scenario())

    expected = {
        "consumed": ("returned", run_doc(OTHER)),
        "read_error": ("runtime_error", "runtime_unreachable"),
        "cancelled_while_reading": ("cancelled", None),
    }[case]
    # Guards first: the unchanged httpx pipeline closes the body exactly once and
    # the error and cancellation mapping is unchanged.
    assert outcome == expected
    assert [stream.closes for stream in streams] == [1]
    assert counts == NO_LIFECYCLE


# L-1: a real pooled transport against a finite loopback HTTP/1.1 peer ------------


class LoopbackPeer:
    """HTTP/1.1 on 127.0.0.1 with Content-Length framing and keep-alive.

    It answers ``GET /v1/runs/{id}`` with a synthetic run document, can hold
    one run id until released, and keeps an ordered ledger of connection opens
    and closes and of request entry and release.
    """

    def __init__(self) -> None:
        self.ledger: list[tuple[int, str, int, str | None]] = []
        self.sequence = itertools.count(1)
        self.connections = 0
        self.open: set[int] = set()
        self.serving: set[asyncio.Task] = set()
        self.holds: dict[str, asyncio.Event] = {}
        self.entered: dict[str, asyncio.Event] = {}

    async def start(self) -> None:
        self.server = await asyncio.start_server(self.serve, "127.0.0.1", 0)
        self.port = self.server.sockets[0].getsockname()[1]
        self.url = f"http://127.0.0.1:{self.port}"

    def hold(self, run_id: str) -> None:
        self.holds[run_id] = asyncio.Event()
        self.entered[run_id] = asyncio.Event()

    def note(self, kind: str, connection: int, run_id: str | None = None) -> None:
        self.ledger.append((next(self.sequence), kind, connection, run_id))

    def first(self, kind: str, run_id: str) -> int:
        return next(s for s, k, _, r in self.ledger if k == kind and r == run_id)

    async def serve(self, reader, writer) -> None:
        task = asyncio.current_task()
        assert task is not None
        self.serving.add(task)
        self.connections += 1
        connection = self.connections
        self.open.add(connection)
        self.note("open", connection)
        try:
            while True:
                try:
                    head = await reader.readuntil(b"\r\n\r\n")
                except (asyncio.IncompleteReadError, ConnectionError):
                    break
                lines = head.decode("latin-1").split("\r\n")
                target = lines[0].split(" ")[1]
                headers = dict(
                    (k.strip().lower(), v.strip())
                    for k, v in (line.split(":", 1) for line in lines[1:] if line)
                )
                if length := int(headers.get("content-length", "0")):
                    await reader.readexactly(length)
                run_id = target.rsplit("/", 1)[-1]
                self.note("enter", connection, run_id)
                if run_id in self.holds:
                    self.entered[run_id].set()
                    await self.holds[run_id].wait()
                body = json.dumps(run_doc(run_id)).encode()
                writer.write(
                    b"HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n"
                    b"Content-Length: %d\r\n\r\n" % len(body) + body
                )
                await writer.drain()
                self.note("release", connection, run_id)
        except ConnectionError:
            pass
        finally:
            self.open.discard(connection)
            self.note("close", connection)
            writer.close()
            with contextlib.suppress(ConnectionError):
                await writer.wait_closed()
            self.serving.discard(task)

    async def stop(self) -> None:
        self.server.close()
        await bounded(self.server.wait_closed())
        for event in self.holds.values():
            event.set()
        if self.serving:
            await asyncio.wait(set(self.serving), timeout=BOUND)

    def listening(self) -> bool:
        with socket.socket() as probe:
            probe.settimeout(1.0)
            return probe.connect_ex(("127.0.0.1", self.port)) == 0


def test_a_real_pool_keeps_its_connections_until_the_owner_closes_it(capsys):
    async def scenario():
        peer = LoopbackPeer()
        await peer.start()
        transport = httpx.AsyncHTTPTransport(trust_env=False)  # owned here
        client = RuntimeClient(transport=transport, base_url=peer.url, timeout=BOUND)
        observed: dict = {}
        owner_closed = False
        try:
            peer.hold(HELD)
            held = asyncio.create_task(client.get_run(HELD))
            await bounded(peer.entered[HELD].wait())
            other = await settle(asyncio.create_task(client.get_run(OTHER)))
            peer.holds[HELD].set()
            observed["held"] = await settle(held)
            observed["other"] = other
            connections = peer.connections
            observed["third"] = await settle(asyncio.create_task(client.get_run(THIRD)))
            observed["third_new_connections"] = peer.connections - connections
            observed["closes_before_owner_close"] = sum(
                1 for _, kind, _, _ in peer.ledger if kind == "close"
            )
            await transport.aclose()  # the owner's single cleanup
            owner_closed = True
            for _ in range(int(BOUND / 0.01)):
                if not peer.open:
                    break
                await asyncio.sleep(0.01)
            observed["open_after_owner_close"] = sorted(peer.open)
            await peer.stop()
            observed["listening_after_teardown"] = peer.listening()
            observed["other_tasks"] = sum(
                1 for t in asyncio.all_tasks() if t is not asyncio.current_task()
            )
        finally:
            # Safety only, for a failed scenario; measured above before this.
            if not owner_closed:
                await transport.aclose()
            await peer.stop()
            await cancel_others()
        observed["ledger"] = peer.ledger
        observed["connections"] = peer.connections
        return peer, observed

    peer, observed = asyncio.run(scenario())
    with capsys.disabled():
        print("\nL-1 observation:", json.dumps(observed))

    assert observed["held"] == ("returned", run_doc(HELD))
    assert observed["other"] == ("returned", run_doc(OTHER))
    assert observed["third"] == ("returned", run_doc(THIRD))
    assert peer.first("enter", HELD) < peer.first("enter", OTHER)
    assert peer.first("release", OTHER) < peer.first("release", HELD)
    assert observed["closes_before_owner_close"] == 0
    assert observed["third_new_connections"] == 0  # an idle connection was reused
    assert observed["open_after_owner_close"] == []
    assert observed["listening_after_teardown"] is False
    assert observed["other_tasks"] == 0

"""Provider send gate driven through the unchanged legacy client.

R comes from the durable ledger; F and A come from the fake
provider's independent ledger, which the gate never reads."""

import asyncio
import json

import httpx
import pytest

from src.core.opencode_client import parse_model_selection
from src.core.openrouter_client import OpenRouterClient, OpenRouterError
from src.runtime_adapter.checkpoint import CheckpointStore, ledger_view
from src.runtime_adapter.fakes import (
    AcceptThenFail,
    FakeModelService,
    RefuseConnection,
    Respond,
    SimulatedCrash,
    SyntheticClock,
)
from src.runtime_adapter.identity import canonical_json, sha256_hex
from src.runtime_adapter.send_gate import Lease, ProviderSendGate, SendGateRefusal
from src.runtime_adapter.synthetic import (
    FAKE_PROVIDER_KEY,
    SYNTHETIC_MODEL,
    completion_body,
)

JOB = "a" * 64
ACTIVE_CLOCKS = []
OK = Respond(200, completion_body("Synthetic model answer"))
UNAVAILABLE = Respond(503, {"error": {"code": 503, "message": "fake overload"}})


class World:
    """Durable stores shared by every simulated process of one job."""

    def __init__(self, root, script, fault_kinds=()):
        self.root = root
        self.clock = SyntheticClock(root / "clock.json")
        ACTIVE_CLOCKS.append(self.clock)
        self.provider = FakeModelService(root / "provider.json", script)

        def store_fault(kind):
            if kind in fault_kinds:
                raise OSError("simulated store failure")

        self.store = CheckpointStore(root / "store", fault=store_fault)
        self.store.create_job(JOB, "key")
        self.store.record_run(JOB, "run-1")
        self.lease(1)

    def lease(self, version):
        self.store.record_lease(
            JOB, "run-1", version, attempt=version, now=int(self.clock.now())
        )
        return Lease(run_id="run-1", owner=f"w{version}", version=version)

    def process(self, lease_version, fault=None):
        """A fresh gate and client, sharing nothing but durable state."""
        lease = Lease(run_id="run-1", owner=f"w{lease_version}", version=lease_version)
        gate = ProviderSendGate(
            store=self.store,
            job_id=JOB,
            lease=lease,
            inner=self.provider,
            clock=self.clock.now,
            fault=fault,
        )
        client = OpenRouterClient(
            api_key=FAKE_PROVIDER_KEY,
            base_url="https://model.example.test/api/v1",
            transport=gate,
        )
        return gate, client

    def consume(self, lease_version):
        """Record what the worker records when a call sequence ends."""
        through = self.view().reservations[-1]["seq"]
        self.store.record_disposition(
            JOB,
            lease_version,
            {"reason": "provider_transient_response", "terminal": False},
            consume_through=through,
        )

    def view(self):
        return ledger_view(self.store.load(JOB))

    def counts(self):
        view = self.view()
        return {
            "R": view.reserved,
            "F": self.provider.forwards,
            "A": self.provider.accepted,
            "P": view.replays,
        }


def generate(client):
    return asyncio.run(
        client.generate(
            system_prompt="synthetic system prompt",
            user_prompt="synthetic user prompt",
            model=parse_model_selection(SYNTHETIC_MODEL),
        )
    )


def direct_forward(gate):
    request = httpx.Request(
        "POST",
        "https://model.example.test/api/v1/chat/completions",
        content=b'{"direct": true}',
    )
    return asyncio.run(gate.handle_async_request(request))


@pytest.fixture(autouse=True)
def synthetic_sleep(monkeypatch):
    """Legacy in-call delays advance synthetic time instead of sleeping."""
    delays = []
    ACTIVE_CLOCKS.clear()

    async def sleep(delay, *_args, **_kwargs):
        delays.append(delay)
        for clock in ACTIVE_CLOCKS:
            clock.advance(delay)

    monkeypatch.setattr(asyncio, "sleep", sleep)
    return delays


def crash_at(point):
    async def fault(name):
        if name == point:
            raise SimulatedCrash(point)

    return fault


def test_complete_success_is_reserved_forwarded_and_captured(tmp_path):
    world = World(tmp_path, [OK])
    gate, client = world.process(1)

    assert generate(client) == "Synthetic model answer"

    view = world.view()
    assert world.counts() == {"R": 1, "F": 1, "A": 1, "P": 0}
    [outcome] = view.outcomes(view.reservations[0]["seq"])
    assert (outcome["disposition"], outcome["http_status"]) == ("resolved", 200)
    assert world.store.get_blob(JOB, outcome["body_sha256"]) == canonical_json(
        completion_body("Synthetic model answer")
    )
    assert gate.delivered == [view.reservations[0]["seq"]]


@pytest.mark.parametrize(
    "error, token",
    [
        (lambda: httpx.ReadTimeout("private detail"), "read_timeout"),
        (lambda: httpx.WriteTimeout("private detail"), "write_timeout"),
        (lambda: httpx.ReadError("private detail"), "read_error"),
        (lambda: httpx.RemoteProtocolError("private detail"), "remote_protocol"),
        (lambda: httpx.CloseError("private detail"), "close_error"),
        (lambda: RuntimeError("private detail"), "unexpected"),
    ],
)
def test_accepted_request_with_lost_response_stops_in_process(
    tmp_path, synthetic_sleep, error, token
):
    world = World(tmp_path, [AcceptThenFail(error), OK])
    gate, client = world.process(1)

    with pytest.raises(OpenRouterError) as raised:
        generate(client)

    assert raised.value.retryable is False
    assert raised.value.attempts == 1
    assert synthetic_sleep == []
    assert world.counts() == {"R": 1, "F": 1, "A": 1, "P": 0}
    view = world.view()
    assert view.ambiguous_reservations == [view.reservations[0]["seq"]]
    assert view.outcomes(view.reservations[0]["seq"])[0]["fault"] == token
    assert gate.refusal_reason == "provider_intent_unresolved"

    with pytest.raises(SendGateRefusal) as refused:
        direct_forward(gate)
    assert refused.value.reason == "provider_intent_unresolved"
    assert world.counts()["F"] == 1
    stored = "".join(p.read_text() for p in (tmp_path / "store").rglob("*.json"))
    for marker in ("Error", "Timeout", "private detail"):
        assert marker not in stored


def test_cancellation_after_acceptance_is_ambiguous_and_propagates(tmp_path):
    world = World(tmp_path, [AcceptThenFail(asyncio.CancelledError), OK])
    _, client = world.process(1)

    with pytest.raises(asyncio.CancelledError):
        generate(client)

    view = world.view()
    assert world.counts() == {"R": 1, "F": 1, "A": 1, "P": 0}
    assert view.outcomes(view.reservations[0]["seq"])[0]["fault"] == "cancelled"
    gate, _ = world.process(1)
    with pytest.raises(SendGateRefusal):
        direct_forward(gate)
    assert world.counts()["F"] == 1


def test_unresolved_intent_blocks_a_fresh_process_on_a_later_lease(tmp_path):
    world = World(tmp_path, [AcceptThenFail(lambda: httpx.ReadTimeout("x")), OK])
    with pytest.raises(OpenRouterError):
        generate(world.process(1)[1])

    world.lease(2)
    gate, client = world.process(2)
    with pytest.raises(OpenRouterError):
        generate(client)

    assert gate.refusal_reason == "provider_intent_unresolved"
    assert world.counts() == {"R": 1, "F": 1, "A": 1, "P": 0}


def test_crash_after_reservation_before_forward_stays_unresolved(tmp_path):
    world = World(tmp_path, [OK])
    _, client = world.process(1, fault=crash_at("after_reservation"))

    with pytest.raises(SimulatedCrash):
        generate(client)

    assert world.counts() == {"R": 1, "F": 0, "A": 0, "P": 0}
    assert world.view().open_reservations == [world.view().reservations[0]["seq"]]
    world.lease(2)
    gate, _ = world.process(2)
    with pytest.raises(SendGateRefusal) as refused:
        direct_forward(gate)
    assert refused.value.reason == "provider_intent_unresolved"
    assert world.counts() == {"R": 1, "F": 0, "A": 0, "P": 0}


def test_pre_send_failure_keeps_the_charge_and_permits_a_bounded_resend(tmp_path):
    world = World(tmp_path, [RefuseConnection(httpx.ConnectError), OK])
    _, client = world.process(1)

    assert generate(client) == "Synthetic model answer"

    view = world.view()
    first, second = (entry["seq"] for entry in view.reservations)
    assert view.failed_before_forward == [first]
    assert view.disposition(second) == "resolved"
    assert world.counts() == {"R": 2, "F": 2, "A": 1, "P": 0}


@pytest.mark.parametrize("error", [httpx.ConnectTimeout, httpx.PoolTimeout])
def test_connect_and_pool_timeouts_are_pre_send(tmp_path, error):
    world = World(tmp_path, [RefuseConnection(error), OK])
    _, client = world.process(1)

    assert generate(client) == "Synthetic model answer"
    assert len(world.view().failed_before_forward) == 1


def test_general_network_error_in_the_pre_send_position_is_ambiguous(tmp_path):
    world = World(tmp_path, [RefuseConnection(httpx.NetworkError), OK])
    _, client = world.process(1)

    with pytest.raises(OpenRouterError):
        generate(client)

    assert world.view().ambiguous_reservations
    assert world.counts() == {"R": 1, "F": 1, "A": 0, "P": 0}


def test_captured_success_is_replayed_after_a_crash_without_new_sends(tmp_path):
    world = World(tmp_path, [OK, OK])
    _, client = world.process(1, fault=crash_at("after_capture"))
    with pytest.raises(SimulatedCrash):
        generate(client)

    world.lease(2)
    gate, fresh_client = world.process(2)
    assert generate(fresh_client) == "Synthetic model answer"

    assert world.counts() == {"R": 1, "F": 1, "A": 1, "P": 1}
    assert gate.delivered == [world.view().reservations[0]["seq"]]


def test_captured_503_replays_free_then_one_real_send_follows(tmp_path):
    world = World(tmp_path, [UNAVAILABLE, OK])
    _, client = world.process(1, fault=crash_at("after_capture"))
    with pytest.raises(SimulatedCrash):
        generate(client)

    world.lease(2)
    _, fresh_client = world.process(2)
    assert generate(fresh_client) == "Synthetic model answer"

    assert world.counts() == {"R": 2, "F": 2, "A": 2, "P": 1}


def rechain(record):
    previous = sha256_hex(b"sentryinsight-runtime-adapter-ledger\0" + JOB.encode())
    for entry in record["ledger"]:
        body = {key: value for key, value in entry.items() if key != "chain"}
        entry["chain"] = sha256_hex(previous.encode() + canonical_json(body))
        previous = entry["chain"]


def corrupt_blob(world, _path):
    view = world.view()
    outcome = view.outcomes(view.reservations[0]["seq"])[0]
    world.store.blob_path(JOB, outcome["body_sha256"]).write_bytes(b"{}")


def rebind_request(_world, path):
    record = json.loads(path.read_text())
    record["ledger"][0]["request_sha256"] = "e" * 64
    rechain(record)
    path.write_text(json.dumps(record))


@pytest.mark.parametrize("tamper", [corrupt_blob, rebind_request])
def test_unverifiable_capture_fails_closed_before_forwarding(tmp_path, tamper):
    world = World(tmp_path, [OK, OK])
    _, client = world.process(1, fault=crash_at("after_capture"))
    with pytest.raises(SimulatedCrash):
        generate(client)

    tamper(world, tmp_path / "store" / "jobs" / JOB / "record.json")
    world.lease(2)
    gate, fresh_client = world.process(2)
    with pytest.raises(OpenRouterError):
        generate(fresh_client)

    assert gate.refusal_reason == "checkpoint_state_stale"
    assert world.counts() == {"R": 1, "F": 1, "A": 1, "P": 0}


def test_total_reservations_stay_bounded_across_processes_and_leases(tmp_path):
    world = World(tmp_path, [UNAVAILABLE])
    _, client = world.process(1, fault=crash_at("after_capture"))
    with pytest.raises(SimulatedCrash):
        generate(client)

    world.lease(2)
    gate, fresh_client = world.process(2)
    with pytest.raises(OpenRouterError) as raised:
        generate(fresh_client)
    assert raised.value.retryable is True
    assert world.counts() == {"R": 3, "F": 3, "A": 3, "P": 1}

    world.consume(2)
    world.lease(3)
    gate, _ = world.process(3)
    with pytest.raises(SendGateRefusal) as refused:
        direct_forward(gate)
    assert refused.value.reason == "provider_budget_exhausted"
    assert world.counts()["F"] == 3


def test_failed_reservation_write_forwards_nothing(tmp_path):
    world = World(tmp_path, [OK], fault_kinds={"reservation"})
    gate, client = world.process(1)

    with pytest.raises(OpenRouterError):
        generate(client)

    assert gate.refusal_reason == "checkpoint_store_failed"
    assert world.counts() == {"R": 0, "F": 0, "A": 0, "P": 0}


@pytest.mark.parametrize("kind", ["blob", "outcome"])
def test_capture_persistence_failure_is_ambiguous(tmp_path, kind):
    world = World(tmp_path, [OK, OK], fault_kinds={kind})
    gate, client = world.process(1)

    with pytest.raises(OpenRouterError):
        generate(client)

    assert gate.refusal_reason == "provider_intent_unresolved"
    assert world.counts() == {"R": 1, "F": 1, "A": 1, "P": 0}
    world.store.fault = None
    world.lease(2)
    gate, _ = world.process(2)
    with pytest.raises(SendGateRefusal) as refused:
        direct_forward(gate)
    assert refused.value.reason == "provider_intent_unresolved"
    assert world.counts()["F"] == 1


def test_persisted_not_before_blocks_early_sends_on_every_lease(tmp_path):
    world = World(
        tmp_path, [Respond(429, {"error": {"code": 429}}, {"Retry-After": "60"}), OK]
    )
    start = world.clock.now()
    with pytest.raises(OpenRouterError) as raised:
        generate(world.process(1)[1])
    assert raised.value.retryable is True
    assert world.view().not_before == int(start) + 60

    world.consume(1)
    world.lease(2)
    gate, _ = world.process(2)
    world.clock.advance(59)
    with pytest.raises(SendGateRefusal) as refused:
        direct_forward(gate)
    assert refused.value.reason == "provider_retry_after_deferred"

    world.clock.advance(1)
    gate, client = world.process(2)
    assert generate(client) == "Synthetic model answer"
    assert world.counts() == {"R": 2, "F": 2, "A": 2, "P": 0}


def test_lost_or_superseded_lease_is_refused_before_reserving(tmp_path):
    world = World(tmp_path, [OK])
    gate, _ = world.process(1)
    gate.lease.lost = True
    with pytest.raises(SendGateRefusal) as refused:
        direct_forward(gate)
    assert refused.value.reason == "lease_lost"

    world.lease(2)
    stale_gate, _ = world.process(1)
    with pytest.raises(SendGateRefusal) as refused:
        direct_forward(stale_gate)
    assert refused.value.reason == "lease_lost"
    assert world.counts() == {"R": 0, "F": 0, "A": 0, "P": 0}


def test_stale_process_paused_after_reservation_cannot_forward(tmp_path):
    world = World(tmp_path, [OK])

    async def scenario():
        paused, release = asyncio.Event(), asyncio.Event()

        async def pause(point):
            if point == "after_reservation":
                paused.set()
                await release.wait()

        stale_gate, stale_client = world.process(1, fault=pause)
        stale = asyncio.ensure_future(
            stale_client.generate(
                system_prompt="s",
                user_prompt="u",
                model=parse_model_selection(SYNTHETIC_MODEL),
            )
        )
        await paused.wait()
        world.lease(2)
        release.set()
        with pytest.raises(OpenRouterError):
            await stale
        return stale_gate

    stale_gate = asyncio.run(scenario())

    assert stale_gate.refusal_reason == "lease_lost"
    view = world.view()
    assert world.counts() == {"R": 1, "F": 0, "A": 0, "P": 0}
    assert view.disposition(view.reservations[0]["seq"]) == "failed_before_forward"


def test_no_request_or_response_headers_are_persisted(tmp_path):
    world = World(
        tmp_path, [Respond(200, completion_body(), {"X-Private": "header-value"})]
    )
    generate(world.process(1)[1])

    persisted = "".join(
        path.read_text(errors="ignore")
        for path in tmp_path.rglob("*")
        if path.is_file()
    )
    for marker in (FAKE_PROVIDER_KEY, "Authorization", "Bearer", "header-value"):
        assert marker not in persisted

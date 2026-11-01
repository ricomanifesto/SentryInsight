"""Mandatory retry checkpoint writes and reads fail closed.

A delay sample or retry disposition that cannot be read or written durably
stops the job with a fixed reason instead of retrying or deferring on an
in-memory decision. Captured responses stay in the ledger, an open or
ambiguous intent still dominates, and the reported persistence is truthful.
"""

import asyncio

import httpx
import pytest

from src.core.opencode_client import parse_model_selection
from src.core.openrouter_client import OpenRouterClient, OpenRouterError
from src.runtime_adapter.checkpoint import (
    CheckpointStateStale,
    CheckpointStore,
    CheckpointStoreError,
    ledger_view,
)
from src.runtime_adapter.fakes import (
    AcceptThenFail,
    FakeModelService,
    Respond,
    SyntheticClock,
)
from src.runtime_adapter.harness import Harness
from src.runtime_adapter.send_gate import (
    JitterPolicy,
    Lease,
    ProviderSendGate,
    RetryDispositionRecorder,
    SendGateRefusal,
)
from src.runtime_adapter.synthetic import (
    FAKE_PROVIDER_KEY,
    SYNTHETIC_MODEL,
    completion_body,
)

JOB = "b" * 64
OK = Respond(200, completion_body())
UNAVAILABLE = Respond(503, {"error": {"code": 503}})
LONG_WAIT = Respond(503, {"error": {"code": 503}}, {"Retry-After": "120"})
HARNESSES = []


@pytest.fixture(autouse=True)
def synthetic_sleep(monkeypatch):
    HARNESSES.clear()
    delays = []

    async def sleep(delay, *_args, **_kwargs):
        delays.append(delay)
        for harness in HARNESSES:
            harness.clock.advance(delay)

    monkeypatch.setattr(asyncio, "sleep", sleep)
    return delays


def world(tmp_path, script):
    harness = Harness(tmp_path / "world", script)
    HARNESSES.append(harness)
    job = harness.freeze()
    run = harness.admit(job)
    return harness, job, run


def view_of(harness, job):
    return ledger_view(harness.store().load(job.manifest_digest))


def assert_capture_retained(harness, job, *, http_status):
    view = view_of(harness, job)
    (reservation,) = view.reservations
    (outcome,) = view.outcomes(reservation["seq"])
    assert outcome["disposition"] == "resolved"
    assert outcome["http_status"] == http_status
    blob = harness.store().get_blob(job.manifest_digest, outcome["body_sha256"])
    assert blob
    return outcome


# Worker: the two reproduced write failures ------------------------------------


def test_failed_delay_sample_write_stops_before_a_second_forward(
    tmp_path, synthetic_sleep
):
    harness, job, run = world(tmp_path, [UNAVAILABLE, OK])

    result = harness.run_worker(store_fault={"delay_sample"})

    assert (result.outcome, result.reason) == ("failed", "checkpoint_store_failed")
    assert result.persisted is True
    assert harness.observe(job) == {"R": 1, "F": 1, "A": 1, "P": 0, "C": 1}
    assert synthetic_sleep == []
    final = harness.run_doc(run["run_id"])
    assert (final["state"], final["error_code"]) == ("failed", "invalid_result")
    assert final["error_summary"] == "checkpoint_store_failed reserved=1"
    view = view_of(harness, job)
    assert view.of_type("delay_sample") == []
    assert_capture_retained(harness, job, http_status=503)
    disposition = harness.store().load(job.manifest_digest)["disposition"]
    assert (disposition["reason"], disposition["terminal"]) == (
        "checkpoint_store_failed",
        True,
    )


def test_failed_retry_disposition_write_is_terminal_not_deferred(tmp_path):
    harness, job, run = world(tmp_path, [LONG_WAIT])

    result = harness.run_worker(store_fault={"retry_disposition"})

    assert (result.outcome, result.reason) == ("failed", "checkpoint_store_failed")
    assert result.run_state == "failed"
    assert result.persisted is True
    assert harness.observe(job) == {"R": 1, "F": 1, "A": 1, "P": 0, "C": 1}
    final = harness.run_doc(run["run_id"])
    assert (final["state"], final["error_code"]) == ("failed", "invalid_result")
    assert final["error_summary"] == "checkpoint_store_failed reserved=1"
    assert view_of(harness, job).of_type("retry_disposition") == []
    outcome = assert_capture_retained(harness, job, http_status=503)
    assert outcome["not_before"] == outcome["received_at"] + 120


def test_failed_store_reports_no_persisted_reason_when_nothing_is_writable(
    tmp_path,
):
    harness, job, run = world(tmp_path, [LONG_WAIT])

    result = harness.run_worker(
        store_fault={"retry_disposition", "disposition", "pending_action"}
    )

    assert (result.outcome, result.reason) == ("failed", "checkpoint_store_failed")
    assert result.persisted is False
    assert harness.store().load(job.manifest_digest)["disposition"] is None
    final = harness.run_doc(run["run_id"])
    assert (final["state"], final["error_code"]) == ("failed", "invalid_result")
    assert_capture_retained(harness, job, http_status=503)


def test_ambiguity_still_dominates_a_failed_disposition_write(tmp_path):
    lost = AcceptThenFail(lambda: httpx.ReadTimeout("synthetic"))
    harness, job, run = world(tmp_path, [lost])

    result = harness.run_worker(store_fault={"retry_disposition"})

    assert result.reason == "provider_intent_unresolved"
    final = harness.run_doc(run["run_id"])
    assert (final["state"], final["error_code"]) == ("failed", "side_effect_conflict")
    assert harness.observe(job) == {"R": 1, "F": 1, "A": 1, "P": 0, "C": 1}


def test_successful_writes_keep_the_recorded_retry_path(tmp_path, synthetic_sleep):
    harness, job, _ = world(tmp_path, [UNAVAILABLE, OK])

    assert harness.run_worker().outcome == "completed"

    assert harness.observe(job) == {"R": 2, "F": 2, "A": 2, "P": 0, "C": 1}
    (sample,) = view_of(harness, job).of_type("delay_sample")
    assert synthetic_sleep == [sample["delay"]]


# Gate, policy and recorder: read failure and stale fencing ---------------------


class FlakyStore(CheckpointStore):
    """A real store whose reads can be made to fail on demand."""

    load_error = None

    def load(self, job_id):
        if self.load_error is not None:
            raise self.load_error()
        return super().load(job_id)


@pytest.fixture
def gate_world(tmp_path):
    class GateWorld:
        def __init__(self):
            self.clock = SyntheticClock(tmp_path / "clock.json")
            self.store = FlakyStore(tmp_path / "store")
            self.store.create_job(JOB, "key")
            self.store.record_run(JOB, "run-1")
            self.store.record_lease(JOB, "run-1", 1, attempt=1, now=self.clock.now())
            self.provider = FakeModelService(
                tmp_path / "provider.json", [UNAVAILABLE, OK]
            )
            self.gate = ProviderSendGate(
                store=self.store,
                job_id=JOB,
                lease=Lease(run_id="run-1", owner="w", version=1),
                inner=self.provider,
                clock=self.clock.now,
            )
            self.policy = JitterPolicy(self.gate, lambda: 0.5)

        def send(self):
            request = httpx.Request(
                "POST", "https://model.example.test/api/v1/chat", content=b"{}"
            )
            return asyncio.run(self.gate.handle_async_request(request))

        def view(self):
            return ledger_view(CheckpointStore(tmp_path / "store").load(JOB))

    return GateWorld()


def assert_halted(world, reason):
    assert world.gate.refusal_reason == reason
    forwards, reserved = world.provider.forwards, world.view().reserved
    world.store.load_error = None
    with pytest.raises(SendGateRefusal) as refused:
        world.send()
    assert refused.value.reason == reason
    assert (world.provider.forwards, world.view().reserved) == (forwards, reserved)


@pytest.mark.parametrize(
    "error, reason",
    [
        (CheckpointStoreError, "checkpoint_store_failed"),
        (CheckpointStateStale, "checkpoint_state_stale"),
    ],
)
def test_policy_read_failure_halts_instead_of_resampling(gate_world, error, reason):
    assert gate_world.send().status_code == 503
    gate_world.store.load_error = error

    with pytest.raises(SendGateRefusal) as refused:
        gate_world.policy(1.0, 30.0)

    assert refused.value.reason == reason
    assert gate_world.view().of_type("delay_sample") == []
    assert_halted(gate_world, reason)


def broken_writes(_kind):
    raise OSError("synthetic store failure")


def test_policy_write_failure_halts(gate_world):
    assert gate_world.send().status_code == 503

    gate_world.store.fault = broken_writes
    with pytest.raises(SendGateRefusal) as refused:
        gate_world.policy(1.0, 30.0)

    gate_world.store.fault = None
    assert refused.value.reason == "checkpoint_store_failed"
    assert_halted(gate_world, "checkpoint_store_failed")


def test_policy_write_from_a_stale_lease_is_lease_lost(gate_world):
    assert gate_world.send().status_code == 503
    gate_world.store.record_lease(
        JOB, "run-1", 2, attempt=2, now=gate_world.clock.now()
    )

    with pytest.raises(SendGateRefusal) as refused:
        gate_world.policy(1.0, 30.0)

    assert refused.value.reason == "lease_lost"
    assert gate_world.view().of_type("delay_sample") == []
    assert gate_world.gate.refusal_reason == "lease_lost"


def test_recorded_sample_is_still_reused_when_reads_work(gate_world):
    assert gate_world.send().status_code == 503
    first = gate_world.policy(1.0, 30.0)
    assert gate_world.policy(1.0, 30.0) == first
    assert len(gate_world.view().of_type("delay_sample")) == 1
    assert gate_world.gate.refusal_reason is None


class Failing:
    def __init__(self, error):
        self.error = error

    async def generate(self, **_kwargs):
        raise self.error


def provider_error():
    error = OpenRouterError("synthetic", retryable=True, http_status=503)
    error.attempts = 1
    return error


@pytest.mark.parametrize(
    "break_store, reason",
    [
        ("write", "checkpoint_store_failed"),
        ("read", "checkpoint_store_failed"),
        ("stale_read", "checkpoint_state_stale"),
        ("stale_lease", "lease_lost"),
    ],
)
def test_recorder_failure_halts_and_reraises_the_same_error(
    gate_world, break_store, reason
):
    assert gate_world.send().status_code == 503
    error = provider_error()
    recorder = RetryDispositionRecorder(Failing(error), gate_world.gate)
    if break_store == "write":
        gate_world.store.fault = broken_writes
    elif break_store == "read":
        gate_world.store.load_error = CheckpointStoreError
    elif break_store == "stale_read":
        gate_world.store.load_error = CheckpointStateStale
    else:
        gate_world.store.record_lease(
            JOB, "run-1", 2, attempt=2, now=gate_world.clock.now()
        )

    with pytest.raises(OpenRouterError) as raised:
        asyncio.run(recorder.generate(system_prompt="s", user_prompt="u"))

    gate_world.store.fault = None
    gate_world.store.load_error = None
    assert raised.value is error
    assert gate_world.view().of_type("retry_disposition") == []
    assert gate_world.gate.refusal_reason == reason
    assert recorder.persisted is False


def test_recorder_keeps_an_earlier_refusal_reason(gate_world):
    gate_world.gate.refusal_reason = "provider_intent_unresolved"
    recorder = RetryDispositionRecorder(Failing(provider_error()), gate_world.gate)
    gate_world.store.load_error = CheckpointStoreError

    with pytest.raises(OpenRouterError):
        asyncio.run(recorder.generate(system_prompt="s", user_prompt="u"))

    assert gate_world.gate.refusal_reason == "provider_intent_unresolved"


def test_recorder_reports_durable_disposition(gate_world):
    assert gate_world.send().status_code == 503
    recorder = RetryDispositionRecorder(Failing(provider_error()), gate_world.gate)

    with pytest.raises(OpenRouterError):
        asyncio.run(recorder.generate(system_prompt="s", user_prompt="u"))

    assert recorder.persisted is True
    assert len(gate_world.view().of_type("retry_disposition")) == 1
    assert gate_world.gate.refusal_reason is None


# Seam property the policy relies on --------------------------------------------


def test_a_raising_policy_stops_the_legacy_loop_before_sleeping(synthetic_sleep):
    requests = []

    def handler(request):
        requests.append(request)
        return httpx.Response(503, json={"error": {"code": 503}})

    def policy(_floor, _cap):
        raise SendGateRefusal("checkpoint_store_failed")

    client = OpenRouterClient(
        api_key=FAKE_PROVIDER_KEY,
        transport=httpx.MockTransport(handler),
        retry_delay_policy=policy,
    )
    with pytest.raises(SendGateRefusal):
        asyncio.run(
            client.generate(
                system_prompt="s",
                user_prompt="u",
                model=parse_model_selection(SYNTHETIC_MODEL),
            )
        )

    assert len(requests) == 1
    assert synthetic_sleep == []

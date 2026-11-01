"""Concurrent lease maintenance while ``run_once`` owns a lease.

Maintenance only renews the claimed lease. Here it is driven by the harness's
injected manual wait and the synthetic clock, so no real time passes and the
global ``asyncio.sleep`` never schedules a heartbeat. Every check of sends uses
the independent R/F/A/P/C observations.
"""

import asyncio
import math

import pytest

from src.runtime_adapter.checkpoint import ledger_view
from src.runtime_adapter.fakes import AcceptThenWait, Respond, SimulatedCrash
from src.runtime_adapter.harness import Harness
from src.runtime_adapter.identity import PRODUCT, WORKFLOW_NAME, WORKFLOW_VERSION
from src.runtime_adapter.synthetic import GROUNDING_REJECTED_REPORT, completion_body
from src.runtime_adapter import worker as worker_module
from src.runtime_adapter.worker import Worker

REAL_SLEEP = asyncio.sleep
OK = Respond(200, completion_body())
INTERVAL = 200.0  # a third of the harness's 600 s lease


async def settle():
    """Let in-memory fakes and the maintenance task run; no real time passes."""
    for _ in range(100):
        await REAL_SLEEP(0)


async def until(predicate):
    for _ in range(500):
        if predicate():
            return
        await REAL_SLEEP(0)
    raise AssertionError("condition not reached")


async def elapse(harness, intervals):
    """Let maintenance intervals pass on the synthetic clock."""
    for _ in range(intervals):
        await settle()
        if not harness.ticker.tick():
            harness.clock.advance(INTERVAL)
        await settle()


def heartbeats(harness, run):
    return sum(
        1
        for event in harness.runtime_service.events(run["run_id"])
        if event["event_type"] == "heartbeat_recorded"
    )


def other_tasks():
    return [task for task in asyncio.all_tasks() if task is not asyncio.current_task()]


async def claim_as(harness, owner):
    return await harness.runtime().claim(
        product=PRODUCT,
        workflow_name=WORKFLOW_NAME,
        workflow_version=WORKFLOW_VERSION,
        lease_owner=owner,
        lease_duration_seconds=harness.lease_duration,
    )


def world(tmp_path, script):
    harness = Harness(tmp_path / "world", script)
    job = harness.freeze()
    run = harness.admit(job)
    return harness, job, run


def blocked_world(tmp_path, then=OK):
    release = asyncio.Event()
    harness, job, run = world(tmp_path, [AcceptThenWait(release, then)])
    return harness, job, run, release


def test_maintenance_renews_the_lease_through_a_long_provider_await(tmp_path):
    harness, job, run, release = blocked_world(tmp_path)

    async def scenario():
        task = asyncio.create_task(harness.worker().run_once())
        await until(lambda: harness.provider.forwards == 1)
        before, started = heartbeats(harness, run), harness.clock.now()

        await elapse(harness, 4)

        assert harness.clock.now() - started == 4 * INTERVAL
        assert 4 * INTERVAL > harness.lease_duration
        # The lease is still current, so no other worker can take the run.
        assert await claim_as(harness, "other") is None
        assert heartbeats(harness, run) == before + 4
        assert harness.run_doc(run["run_id"])["state"] == "running"
        assert harness.observe(job) == {"R": 1, "F": 1, "A": 1, "P": 0, "C": 1}
        release.set()
        return await task

    result = asyncio.run(scenario())

    assert result.outcome == "completed"
    assert harness.observe(job) == {"R": 1, "F": 1, "A": 1, "P": 0, "C": 1}
    assert set(harness.ticker.requested) == {INTERVAL}
    assert harness.ticker.waiting == 0
    assert len(harness.runtime_service.runs()) == 1


def test_fenced_maintenance_stops_promotion_of_the_captured_result(tmp_path):
    harness, job, run, release = blocked_world(tmp_path)

    async def scenario():
        task = asyncio.create_task(harness.worker().run_once())
        await until(lambda: harness.provider.forwards == 1)
        # The worker stalls past its lease and Runtime re-leases the run.
        harness.clock.advance(harness.lease_duration + 1)
        taken = await claim_as(harness, "other")
        assert taken["lease_version"] == 2
        await elapse(harness, 1)
        release.set()
        return await task

    result = asyncio.run(scenario())

    assert (result.outcome, result.reason) == ("lease_lost", "lease_lost")
    record = harness.store().load(job.manifest_digest)
    assert record["analysis"] is None
    assert record["artifact"] is None
    view = ledger_view(record)
    # The stale opener keeps its own captured outcome but never promotes it.
    assert [o["disposition"] for o in view.outcomes(1)] == ["resolved"]
    assert len(view.unconsumed_resolved) == 1
    assert harness.observe(job) == {"R": 1, "F": 1, "A": 1, "P": 0, "C": 2}
    assert harness.ticker.waiting == 0


@pytest.mark.parametrize(
    "mode, reason",
    [
        ("unreachable", "runtime_unreachable"),
        ("draining", "runtime_draining"),
        ("unauthorized", "runtime_auth_rejected"),
    ],
)
def test_failed_maintenance_stops_the_invocation_and_keeps_the_capture(
    tmp_path, mode, reason
):
    harness, job, run, release = blocked_world(tmp_path)

    async def scenario():
        task = asyncio.create_task(harness.worker().run_once())
        await until(lambda: harness.provider.forwards == 1)
        harness.runtime_service.unavailable = mode
        await elapse(harness, 1)
        release.set()
        return await task

    result = asyncio.run(scenario())

    assert (result.exit_code, result.outcome, result.reason) == (
        1,
        "runtime_unavailable",
        reason,
    )
    record = harness.store().load(job.manifest_digest)
    assert record["analysis"] is None
    assert record["disposition"] is None
    assert len(ledger_view(record).unconsumed_resolved) == 1
    assert harness.observe(job) == {"R": 1, "F": 1, "A": 1, "P": 0, "C": 1}
    assert harness.ticker.waiting == 0

    # Once Runtime is back, the next lease replays the capture; nothing is resent.
    harness.runtime_service.unavailable = None
    harness.expire_lease()
    assert harness.run_worker(owner="worker-2").outcome == "completed"
    assert harness.observe(job) == {"R": 1, "F": 1, "A": 1, "P": 1, "C": 2}


def test_unexpected_maintenance_failure_is_reported_not_silent(tmp_path):
    harness, job, run, release = blocked_world(tmp_path)

    async def scenario():
        task = asyncio.create_task(harness.worker().run_once())
        await until(lambda: harness.provider.forwards == 1)
        await until(lambda: harness.ticker.waiting == 1)
        assert harness.ticker.fail(RuntimeError("synthetic maintenance fault"))
        await settle()
        release.set()
        return await task

    result = asyncio.run(scenario())

    assert (result.outcome, result.reason) == ("failed", "worker_unclassified")
    final = harness.run_doc(run["run_id"])
    assert (final["state"], final["error_code"]) == ("failed", "invalid_result")
    assert final["error_summary"] == "worker_unclassified reserved=1 attempts=1"
    assert harness.store().load(job.manifest_digest)["analysis"] is None
    assert harness.observe(job) == {"R": 1, "F": 1, "A": 1, "P": 0, "C": 1}


def test_failed_maintenance_during_artifact_preparation_records_nothing(
    tmp_path, monkeypatch
):
    harness, job, run = world(tmp_path, [OK])
    building, proceed = asyncio.Event(), asyncio.Event()
    original = worker_module.generate_report

    async def slow_build(state):
        building.set()
        await proceed.wait()
        return await original(state)

    monkeypatch.setattr(worker_module, "generate_report", slow_build)

    async def scenario():
        task = asyncio.create_task(harness.worker().run_once())
        await until(building.is_set)
        harness.runtime_service.unavailable = "draining"
        await elapse(harness, 1)
        proceed.set()
        return await task

    result = asyncio.run(scenario())

    assert (result.outcome, result.reason) == (
        "runtime_unavailable",
        "runtime_draining",
    )
    record = harness.store().load(job.manifest_digest)
    assert record["analysis"] is not None
    assert record["artifact"] is None
    assert harness.observe(job) == {"R": 1, "F": 1, "A": 1, "P": 0, "C": 1}


def test_cancelled_await_stays_ambiguous_and_stops_maintenance(tmp_path):
    harness, job, run, release = blocked_world(tmp_path)

    async def scenario():
        task = asyncio.create_task(harness.worker().run_once())
        await until(lambda: harness.provider.forwards == 1)
        await elapse(harness, 2)
        task.cancel()
        with pytest.raises(asyncio.CancelledError):
            await task
        await settle()
        assert other_tasks() == []

    asyncio.run(scenario())

    view = ledger_view(harness.store().load(job.manifest_digest))
    assert [o["disposition"] for o in view.outcomes(1)] == ["ambiguous"]
    assert view.unresolved_intent
    assert harness.ticker.requested == [INTERVAL] * 3
    assert harness.ticker.waiting == 0


def crash_after_analysis(name):
    async def fault(point):
        if point == name:
            raise SimulatedCrash(point)

    return fault


@pytest.mark.parametrize(
    "path", ["completed", "product_failure", "lease_lost", "runtime", "crash"]
)
def test_every_exit_path_stops_maintenance(tmp_path, path):
    rejected = Respond(200, completion_body(GROUNDING_REJECTED_REPORT))
    then = rejected if path == "product_failure" else OK
    harness, job, run, release = blocked_world(tmp_path, then)
    fault = crash_after_analysis("after_analysis_record") if path == "crash" else None

    async def scenario():
        task = asyncio.create_task(harness.worker(fault=fault).run_once())
        await until(lambda: harness.provider.forwards == 1)
        if path == "lease_lost":
            harness.clock.advance(harness.lease_duration + 1)
            await claim_as(harness, "other")
        elif path == "runtime":
            harness.runtime_service.unavailable = "unreachable"
        await elapse(harness, 1)
        assert harness.ticker.requested, "maintenance never ran"
        release.set()
        try:
            outcome = (await task).outcome
        except SimulatedCrash:
            outcome = "crashed"
        harness.runtime_service.unavailable = None
        assert harness.ticker.waiting == 0
        await settle()
        assert other_tasks() == []
        count = heartbeats(harness, run)
        assert not harness.ticker.tick()
        await settle()
        assert heartbeats(harness, run) == count
        return outcome

    outcome = asyncio.run(scenario())

    assert (
        outcome
        == {
            "completed": "completed",
            "product_failure": "failed",
            "lease_lost": "lease_lost",
            "runtime": "runtime_unavailable",
            "crash": "crashed",
        }[path]
    )


def test_a_job_that_never_yields_leaves_no_maintenance_behind(tmp_path):
    harness, job, run = world(tmp_path, [OK])

    async def scenario():
        result = await harness.worker().run_once()
        await settle()
        assert other_tasks() == []
        return result

    assert asyncio.run(scenario()).outcome == "completed"
    assert harness.ticker.waiting == 0


def test_idle_worker_starts_no_maintenance(tmp_path):
    harness = Harness(tmp_path / "world", [OK])

    assert harness.run_worker().outcome == "idle"

    assert harness.ticker.requested == []


def test_interval_is_bounded_by_a_third_of_the_lease(tmp_path):
    harness = Harness(tmp_path / "world", [OK])
    kwargs = harness.worker_kwargs()

    assert Worker(**kwargs).heartbeat_interval == INTERVAL
    assert Worker(**kwargs, heartbeat_interval_seconds=150).heartbeat_interval == 150
    for interval in (INTERVAL + 1, 0, -1, math.nan, math.inf):
        with pytest.raises(ValueError):
            Worker(**kwargs, heartbeat_interval_seconds=interval)


def test_default_wait_is_not_the_patched_global_sleep(tmp_path, monkeypatch):
    harness = Harness(tmp_path / "world", [OK])
    kwargs = harness.worker_kwargs()
    del kwargs["heartbeat_wait"]

    async def busy(_delay, *_args, **_kwargs):
        harness.clock.advance(_delay)

    monkeypatch.setattr(asyncio, "sleep", busy)

    assert Worker(**kwargs).heartbeat_wait is REAL_SLEEP


def test_global_sleep_patch_does_not_drive_maintenance(tmp_path, monkeypatch):
    release = asyncio.Event()
    unavailable = Respond(503, {"error": {"code": 503}})
    harness, job, run = world(tmp_path, [unavailable, AcceptThenWait(release, OK)])
    delays = []

    async def in_call_delay(delay, *_args, **_kwargs):
        # Advances the clock without yielding, as the worker tests do.
        delays.append(delay)
        harness.clock.advance(delay)

    monkeypatch.setattr(asyncio, "sleep", in_call_delay)

    async def scenario():
        started = harness.clock.now()
        task = asyncio.create_task(harness.worker().run_once())
        await until(lambda: harness.provider.forwards == 2)
        await settle()
        # Maintenance waits on the injected wait; time moved only for the delay.
        assert harness.ticker.waiting == 1
        assert harness.ticker.requested == [INTERVAL]
        assert harness.clock.now() - started == sum(delays)
        release.set()
        return await task

    assert asyncio.run(scenario()).outcome == "completed"
    assert len(delays) == 1
    assert harness.observe(job) == {"R": 2, "F": 2, "A": 2, "P": 0, "C": 1}

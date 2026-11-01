"""Lease maintenance ends on purpose only through ``Lease.release``.

Every exit of ``run_once``, including cancellation of the worker itself, stops
maintenance through ``release``. Any other cancellation, such as one raised by
the maintenance wait, is a maintenance fault: it is reported like any other so
product work never continues on a lease nobody renews. The harness's manual
wait and synthetic clock drive maintenance, so no real time passes.
"""

import asyncio

import pytest

from src.runtime_adapter.checkpoint import ledger_view
from src.runtime_adapter.fakes import AcceptThenWait, Respond
from src.runtime_adapter.harness import Harness
from src.runtime_adapter.identity import PRODUCT, WORKFLOW_NAME, WORKFLOW_VERSION
from src.runtime_adapter.send_gate import Lease
from src.runtime_adapter.synthetic import completion_body

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


def other_tasks(*known):
    current = asyncio.current_task()
    return [task for task in asyncio.all_tasks() if task not in (current, *known)]


def heartbeats(harness, run_id):
    return sum(
        1
        for event in harness.runtime_service.events(run_id)
        if event["event_type"] == "heartbeat_recorded"
    )


def blocked_world(tmp_path):
    release = asyncio.Event()
    harness = Harness(tmp_path / "world", [AcceptThenWait(release, OK)])
    job = harness.freeze()
    run = harness.admit(job)
    return harness, job, run, release


async def claimed_lease(harness):
    run = await harness.runtime().claim(
        product=PRODUCT,
        workflow_name=WORKFLOW_NAME,
        workflow_version=WORKFLOW_VERSION,
        lease_owner="worker-1",
        lease_duration_seconds=harness.lease_duration,
    )
    return Lease(
        run_id=run["run_id"],
        owner="worker-1",
        version=run["lease_version"],
        duration=harness.lease_duration,
        runtime=harness.runtime(),
    )


def cancel_wait(harness, *_known):
    """The pending maintenance wait itself raises a cancellation."""
    assert harness.ticker.fail(asyncio.CancelledError())


def cancel_task(harness, *known):
    """Something other than ``release`` cancels the maintenance task."""
    (maintenance,) = other_tasks(*known)
    maintenance.cancel()


CANCELLATIONS = {"wait_cancelled": cancel_wait, "task_cancelled": cancel_task}


# Lease: only release stops maintenance quietly ---------------------------------


@pytest.mark.parametrize("cancel", CANCELLATIONS)
def test_unexpected_cancellation_of_maintenance_is_a_fault(tmp_path, cancel):
    harness, _, run, _ = blocked_world(tmp_path)

    async def scenario():
        lease = await claimed_lease(harness)
        lease.maintain(INTERVAL, harness.ticker.wait)
        await until(lambda: harness.ticker.waiting == 1)
        CANCELLATIONS[cancel](harness)
        await settle()
        assert other_tasks() == []
        problem = lease.problem
        # Every later confirmation reports it, so the gate and worker stop.
        confirmed = await lease.confirm()
        await lease.release()
        return problem, confirmed

    assert asyncio.run(scenario()) == ("worker_unclassified", "worker_unclassified")
    assert harness.ticker.requested == [INTERVAL]
    assert heartbeats(harness, run["run_id"]) == 0


def test_release_stops_maintenance_without_a_fault(tmp_path):
    harness, _, run, _ = blocked_world(tmp_path)

    async def scenario():
        lease = await claimed_lease(harness)
        lease.maintain(INTERVAL, harness.ticker.wait)
        await until(lambda: harness.ticker.waiting == 1)
        await lease.release()
        assert other_tasks() == []
        return lease.problem, await lease.confirm()

    assert asyncio.run(scenario()) == (None, None)
    assert harness.ticker.waiting == 0
    # Only the explicit confirmation above heartbeats; maintenance never did.
    assert heartbeats(harness, run["run_id"]) == 1


def test_cancelling_the_owner_stops_maintenance_without_a_fault(tmp_path):
    harness, _, _, _ = blocked_world(tmp_path)

    async def owner(lease):
        lease.maintain(INTERVAL, harness.ticker.wait)
        try:
            await asyncio.Event().wait()
        finally:
            await lease.release()

    async def scenario():
        lease = await claimed_lease(harness)
        task = asyncio.create_task(owner(lease))
        await until(lambda: harness.ticker.waiting == 1)
        task.cancel()
        with pytest.raises(asyncio.CancelledError):
            await task
        assert other_tasks() == []
        return lease.problem

    assert asyncio.run(scenario()) is None
    assert harness.ticker.waiting == 0


# Worker: an unexpected cancellation stops the invocation -----------------------


@pytest.mark.parametrize("cancel", CANCELLATIONS)
def test_cancelled_maintenance_stops_the_invocation_and_keeps_the_capture(
    tmp_path, cancel
):
    harness, job, run, release = blocked_world(tmp_path)

    async def scenario():
        worker = asyncio.create_task(harness.worker().run_once())
        await until(lambda: harness.provider.forwards == 1)
        await until(lambda: harness.ticker.waiting == 1)
        CANCELLATIONS[cancel](harness, worker)
        await settle()
        # Neither the worker nor release was cancelled; only maintenance ended.
        assert not worker.done()
        assert other_tasks(worker) == []
        renewed = heartbeats(harness, run["run_id"])
        release.set()
        result = await worker
        await settle()
        assert other_tasks() == []
        return result, renewed

    result, renewed = asyncio.run(scenario())

    assert (result.outcome, result.reason) == ("failed", "worker_unclassified")
    final = harness.run_doc(run["run_id"])
    assert (final["state"], final["error_code"]) == ("failed", "invalid_result")
    assert final["error_summary"] == "worker_unclassified reserved=1 attempts=1"
    record = harness.store().load(job.manifest_digest)
    assert record["analysis"] is None
    assert record["artifact"] is None
    view = ledger_view(record)
    # The answer that arrived is kept but never promoted; only the failure
    # record consumes it.
    (outcome,) = view.outcomes(1)
    assert (outcome["disposition"], outcome["http_status"]) == ("resolved", 200)
    assert harness.store().get_blob(job.manifest_digest, outcome["body_sha256"])
    assert view.consumed_through == 1
    assert harness.observe(job) == {"R": 1, "F": 1, "A": 1, "P": 0, "C": 1}
    # Maintenance was not silently restarted after the fault.
    assert heartbeats(harness, run["run_id"]) == renewed
    assert harness.ticker.requested == [INTERVAL]
    assert harness.ticker.waiting == 0


def test_ambiguity_still_dominates_after_cancelled_maintenance(tmp_path):
    harness, job, run, _ = blocked_world(tmp_path)

    async def scenario():
        worker = asyncio.create_task(harness.worker().run_once())
        await until(lambda: harness.provider.forwards == 1)
        await until(lambda: harness.ticker.waiting == 1)
        cancel_wait(harness)
        await settle()
        # The worker itself is then cancelled during the provider await.
        worker.cancel()
        with pytest.raises(asyncio.CancelledError):
            await worker
        await settle()
        assert other_tasks() == []

    asyncio.run(scenario())

    view = ledger_view(harness.store().load(job.manifest_digest))
    assert [o["disposition"] for o in view.outcomes(1)] == ["ambiguous"]
    assert view.unresolved_intent
    assert harness.run_doc(run["run_id"])["state"] == "running"
    assert harness.observe(job) == {"R": 1, "F": 1, "A": 1, "P": 0, "C": 1}
    assert harness.ticker.waiting == 0

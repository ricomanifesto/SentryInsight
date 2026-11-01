"""Worker ``run_once`` recovery scenarios against the fakes.

Every assertion about sends uses the independent observations: R from the
durable ledger, F and A from the fake provider's ledger, P from replay entries
and C from the fake Runtime's lease events.
"""

import asyncio
import json
import os
import shutil
import stat

import httpx
import pytest

from src.runtime_adapter.checkpoint import ledger_view
from src.runtime_adapter.fakes import (
    AcceptThenFail,
    AcceptThenWait,
    Respond,
    SimulatedCrash,
)
from src.runtime_adapter.harness import Harness
from src.runtime_adapter.identity import INPUT_REF_KIND, OUTPUT_REF_KIND
from src.runtime_adapter.runtime_client import RuntimeApiError
from src.runtime_adapter.synthetic import (
    GROUNDING_REJECTED_REPORT,
    completion_body,
    synthetic_config,
)
from src.runtime_adapter.worker import Worker

OK = Respond(200, completion_body())
REAL_SLEEP = asyncio.sleep
UNAVAILABLE = Respond(503, {"error": {"code": 503}})
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


def world(tmp_path, script=(OK,), **kwargs):
    harness = Harness(tmp_path / "world", script, **kwargs)
    HARNESSES.append(harness)
    job = harness.freeze()
    run = harness.admit(job)
    return harness, job, run


def crash_at(point, *, times=1):
    remaining = [times]

    async def fault(name):
        if name == point and remaining[0]:
            remaining[0] -= 1
            raise SimulatedCrash(point)

    return fault


def raise_at(point, error):
    async def fault(name):
        if name == point:
            raise error

    return fault


def crash(harness, **kwargs):
    with pytest.raises(SimulatedCrash):
        harness.run_worker(**kwargs)


def outcome_types(harness, job):
    view = ledger_view(harness.store().load(job.manifest_digest))
    return [
        [o["disposition"] for o in view.outcomes(entry["seq"])]
        for entry in view.reservations
    ]


def assert_failed(harness, run, code, summary_prefix):
    final = harness.run_doc(run["run_id"])
    assert final["state"] == "failed"
    assert final["error_code"] == code
    assert final["error_summary"].startswith(summary_prefix)
    assert final["error_code"] not in ("unknown", "worker_error")
    return final


def artifact_dirs(harness, job):
    root = harness.artifact_root / job.manifest_digest
    if not root.exists():
        return []
    return sorted(path.name for path in root.iterdir() if not path.name.startswith("."))


# Normal path and determinism ---------------------------------------------


def test_one_job_completes_with_a_prepared_artifact_reference(tmp_path):
    harness, job, run = world(tmp_path)

    result = harness.run_worker()

    assert (result.exit_code, result.outcome) == (0, "completed")
    final = harness.run_doc(run["run_id"])
    assert final["state"] == "succeeded"
    output = final["output_ref"]
    assert set(output) == {
        "kind",
        "manifest_sha256",
        "artifact_sha256",
        "artifact_files",
        "artifact_bytes",
    }
    assert output["kind"] == OUTPUT_REF_KIND
    assert output["manifest_sha256"] == job.manifest_digest
    assert artifact_dirs(harness, job) == [output["artifact_sha256"]]
    assert (
        harness.artifact_root
        / job.manifest_digest
        / output["artifact_sha256"]
        / "index.html"
    ).is_file()
    assert harness.observe(job) == {"R": 1, "F": 1, "A": 1, "P": 0, "C": 1}
    record = harness.store().load(job.manifest_digest)
    assert record["stage"] == "completed"
    assert record["publication"] is None
    assert harness.run_worker().outcome == "idle"
    assert harness.observe(job)["C"] == 1


def test_prepared_artifact_is_never_written_into_the_repository(tmp_path):
    from src.runtime_adapter.identity import REPO_ROOT

    before = sorted(p.name for p in REPO_ROOT.iterdir())
    harness, _, _ = world(tmp_path)
    harness.run_worker()

    assert sorted(p.name for p in REPO_ROOT.iterdir()) == before
    assert not harness.artifact_root.resolve().is_relative_to(REPO_ROOT)


def test_worker_rejects_a_lease_shorter_than_its_send_window(tmp_path):
    harness, _, _ = world(tmp_path)

    with pytest.raises(ValueError):
        Worker(**dict(harness.worker_kwargs(), lease_duration_seconds=60))


# A: ambiguity and replay --------------------------------------------------


def test_a1_read_timeout_after_acceptance_stops_in_the_first_process(tmp_path):
    harness, job, run = world(
        tmp_path, [AcceptThenFail(lambda: httpx.ReadTimeout("x")), OK]
    )

    result = harness.run_worker()

    assert result.reason == "provider_intent_unresolved"
    assert_failed(harness, run, "side_effect_conflict", "provider_intent_unresolved")
    assert harness.observe(job) == {"R": 1, "F": 1, "A": 1, "P": 0, "C": 1}
    assert artifact_dirs(harness, job) == []


def test_a2_restart_after_ambiguity_never_infers_no_work(tmp_path):
    harness, job, run = world(
        tmp_path, [AcceptThenFail(lambda: SimulatedCrash("F3b")), OK]
    )
    crash(harness)
    harness.expire_lease()

    result = harness.run_worker(owner="worker-2")

    assert result.reason == "provider_intent_unresolved"
    assert_failed(harness, run, "side_effect_conflict", "provider_intent_unresolved")
    assert harness.observe(job) == {"R": 1, "F": 1, "A": 1, "P": 0, "C": 2}
    assert (
        harness.store()
        .load(job.manifest_digest)["idempotency_key"]
        .endswith(job.manifest_digest)
    )


@pytest.mark.parametrize(
    "error",
    [
        lambda: httpx.WriteTimeout("x"),
        lambda: httpx.ReadError("x"),
        lambda: httpx.RemoteProtocolError("x"),
        lambda: RuntimeError("unexpected after forwarding began"),
    ],
    ids=["write_timeout", "read_disconnect", "remote_protocol", "d3_unexpected"],
)
def test_a3_d3_other_post_forward_failures_are_ambiguous(tmp_path, error):
    harness, job, run = world(tmp_path, [AcceptThenFail(error), OK])

    harness.run_worker()

    assert_failed(harness, run, "side_effect_conflict", "provider_intent_unresolved")
    assert outcome_types(harness, job) == [["ambiguous"]]
    assert harness.observe(job)["F"] == 1


def test_a3_cancellation_propagates_and_the_next_lease_stops(tmp_path):
    harness, job, run = world(tmp_path, [AcceptThenFail(asyncio.CancelledError), OK])
    with pytest.raises(asyncio.CancelledError):
        harness.run_worker()
    harness.expire_lease()

    harness.run_worker(owner="worker-2")

    assert_failed(harness, run, "side_effect_conflict", "provider_intent_unresolved")
    assert harness.observe(job) == {"R": 1, "F": 1, "A": 1, "P": 0, "C": 2}


def test_a4_crash_after_reservation_is_treated_as_ambiguous(tmp_path):
    harness, job, run = world(tmp_path)
    crash(harness, fault=crash_at("after_reservation"))
    harness.expire_lease()

    harness.run_worker(owner="worker-2")

    assert_failed(harness, run, "side_effect_conflict", "provider_intent_unresolved")
    assert harness.observe(job) == {"R": 1, "F": 0, "A": 0, "P": 0, "C": 2}
    assert outcome_types(harness, job) == [["ambiguous"]]


def test_a6_captured_success_is_replayed_into_the_same_artifact(tmp_path):
    harness, job, run = world(tmp_path)
    crash(harness, fault=crash_at("after_capture"))
    harness.expire_lease()

    assert harness.run_worker(owner="worker-2").outcome == "completed"

    assert harness.observe(job) == {"R": 1, "F": 1, "A": 1, "P": 1, "C": 2}
    clean, clean_job, clean_run = world(tmp_path / "clean")
    clean.run_worker()
    replayed = harness.run_doc(run["run_id"])["output_ref"]["artifact_sha256"]
    direct = clean.run_doc(clean_run["run_id"])["output_ref"]["artifact_sha256"]
    assert replayed == direct
    assert artifact_dirs(harness, job) == [replayed]


def test_a7_captured_503_replays_free_and_one_real_send_follows(tmp_path):
    harness, job, _ = world(tmp_path, [UNAVAILABLE, OK])
    crash(harness, fault=crash_at("after_capture"))
    harness.expire_lease()

    assert harness.run_worker(owner="worker-2").outcome == "completed"

    assert harness.observe(job) == {"R": 2, "F": 2, "A": 2, "P": 1, "C": 2}
    assert len(artifact_dirs(harness, job)) == 1


def test_a8_corrupted_capture_fails_closed_without_regeneration(tmp_path):
    harness, job, run = world(tmp_path)
    crash(harness, fault=crash_at("after_capture"))
    store = harness.store()
    view = ledger_view(store.load(job.manifest_digest))
    outcome = view.outcomes(view.reservations[0]["seq"])[0]
    store.blob_path(job.manifest_digest, outcome["body_sha256"]).write_bytes(b"{}")
    harness.expire_lease()

    harness.run_worker(owner="worker-2")

    assert_failed(harness, run, "invalid_result", "checkpoint_state_stale")
    assert harness.observe(job) == {"R": 1, "F": 1, "A": 1, "P": 0, "C": 2}
    assert artifact_dirs(harness, job) == []


# B: budget, admission and store recovery ---------------------------------


def test_b1_budget_stays_bounded_and_the_fourth_forward_is_blocked(tmp_path):
    retry_later = Respond(429, {"error": {"code": 429}}, {"Retry-After": "31"})
    harness, job, run = world(tmp_path, [UNAVAILABLE, retry_later, UNAVAILABLE, OK])
    crash(harness, fault=crash_at("after_capture"))
    harness.expire_lease()

    second = harness.run_worker(owner="worker-2")
    assert second.reason == "provider_retry_after_deferred"
    assert harness.run_doc(run["run_id"])["state"] == "retry_wait"
    # Not-before is ceil(capture + 31) and capture followed a jittered delay.
    harness.clock.advance(32)

    third = harness.run_worker(owner="worker-3")

    assert third.reason == "provider_budget_exhausted"
    assert_failed(harness, run, "side_effect_conflict", "provider_budget_exhausted")
    assert harness.observe(job) == {"R": 3, "F": 3, "A": 3, "P": 1, "C": 3}


def test_b2_duplicate_trigger_and_lost_submit_ack_yield_one_run(tmp_path):
    harness = Harness(tmp_path / "world", [OK])
    job = harness.freeze()
    harness.runtime_service.drop_next_response("submit")

    with pytest.raises(RuntimeApiError):
        harness.admit(job)
    run = harness.admit(job)
    again = harness.admit(job)

    assert run["run_id"] == again["run_id"]
    assert len(harness.runtime_service.runs()) == 1
    assert ledger_view(harness.store().load(job.manifest_digest)).reserved == 0
    with pytest.raises(RuntimeApiError) as raised:
        harness.admit(job, input_ref=dict(run["input_ref"], manifest_sha256="b" * 64))
    assert raised.value.reason == "idempotency_conflict"
    assert len(harness.runtime_service.runs()) == 1


def test_b3_lost_completion_ack_is_reconciled_by_reading_the_run(tmp_path):
    harness, job, run = world(tmp_path)
    harness.runtime_service.drop_next_response("complete")

    first = harness.run_worker()
    assert (first.exit_code, first.reason) == (1, "runtime_unreachable")
    record = harness.store().load(job.manifest_digest)
    assert record["pending_action"]["kind"] == "complete"
    assert harness.run_doc(run["run_id"])["state"] == "succeeded"

    second = harness.run_worker()

    assert (second.exit_code, second.outcome, second.reconciled) == (0, "idle", 1)
    record = harness.store().load(job.manifest_digest)
    assert record["stage"] == "completed" and record["pending_action"] is None
    assert harness.observe(job) == {"R": 1, "F": 1, "A": 1, "P": 0, "C": 1}
    assert len(artifact_dirs(harness, job)) == 1
    assert len(harness.runtime_service.runs()) == 1


def deferred_world(tmp_path):
    retry_later = Respond(429, {"error": {"code": 429}}, {"Retry-After": "31"})
    return world(tmp_path, [retry_later, OK])


def record_path(harness, job):
    return harness.store_root / "jobs" / job.manifest_digest / "record.json"


def lease_ahead(harness, job, _snapshot):
    path = record_path(harness, job)
    record = json.loads(path.read_text())
    record["highest_lease_version"] = 9
    path.write_text(json.dumps(record))


def chain_break(harness, job, _snapshot):
    path = record_path(harness, job)
    record = json.loads(path.read_text())
    record["ledger"][0]["reserved_at"] = 0
    path.write_text(json.dumps(record))


def restored_older_snapshot(harness, _job, snapshot):
    shutil.rmtree(harness.store_root)
    shutil.copytree(snapshot, harness.store_root)


@pytest.mark.parametrize("tamper", [lease_ahead, chain_break, restored_older_snapshot])
def test_b4_stale_or_corrupt_store_is_rejected_before_any_send(tmp_path, tamper):
    harness, job, run = deferred_world(tmp_path)
    snapshot = tmp_path / "snapshot"

    async def copy_after_claim(name):
        if name == "after_claim":
            shutil.copytree(harness.store_root, snapshot)

    first = harness.run_worker(fault=copy_after_claim)
    assert first.reason == "provider_retry_after_deferred"
    assert "reserved=1" in harness.run_doc(run["run_id"])["error_summary"]
    tamper(harness, job, snapshot)
    harness.clock.advance(31)

    result = harness.run_worker(owner="worker-2")

    assert result.reason == "checkpoint_state_stale"
    assert_failed(harness, run, "invalid_result", "checkpoint_state_stale")
    assert harness.observe(job)["F"] == 1
    assert artifact_dirs(harness, job) == []


def test_b5_failed_reservation_write_sends_nothing_and_claims_nothing(tmp_path):
    harness, job, run = world(tmp_path)
    broken = {"reservation", "disposition", "pending_action", "runtime_ack", "refusal"}

    result = harness.run_worker(store_fault=broken)

    assert (result.reason, result.persisted) == ("checkpoint_store_failed", False)
    assert_failed(harness, run, "invalid_result", "checkpoint_store_failed")
    assert harness.observe(job) == {"R": 0, "F": 0, "A": 0, "P": 0, "C": 1}
    assert harness.store().load(job.manifest_digest)["disposition"] is None


def test_b6_capture_persistence_failure_is_never_resent(tmp_path):
    harness, job, run = world(tmp_path, [OK, OK])

    result = harness.run_worker(store_fault={"outcome"})

    assert result.reason == "provider_intent_unresolved"
    assert_failed(harness, run, "side_effect_conflict", "provider_intent_unresolved")
    assert harness.observe(job) == {"R": 1, "F": 1, "A": 1, "P": 0, "C": 1}
    assert ledger_view(harness.store().load(job.manifest_digest)).open_reservations


def test_b7_lease_changes_without_provider_calls_spend_nothing(tmp_path):
    harness, job, run = world(tmp_path)

    async def runtime_down(name):
        if name == "before_runtime_report":
            harness.runtime_service.unavailable = "unreachable"

    first = harness.run_worker(fault=runtime_down)
    assert (first.exit_code, first.reason) == (1, "runtime_unreachable")
    harness.runtime_service.unavailable = None
    assert harness.run_worker(owner="worker-2").outcome == "idle"
    harness.expire_lease()

    assert harness.run_worker(owner="worker-2").outcome == "completed"

    assert harness.observe(job) == {"R": 1, "F": 1, "A": 1, "P": 0, "C": 2}
    assert harness.run_doc(run["run_id"])["state"] == "succeeded"
    assert len(artifact_dirs(harness, job)) == 1


# C: Retry-After and lease fencing during an in-call delay ----------------


def test_c5_long_retry_after_exhausts_leases_without_sending(tmp_path):
    long_wait = Respond(429, {"error": {"code": 429}}, {"Retry-After": "120"})
    harness, job, run = world(tmp_path, [long_wait, OK])
    start = harness.clock.now()

    reasons = [harness.run_worker().reason]
    for _ in range(2):
        harness.clock.advance(5)
        reasons.append(harness.run_worker(owner="worker-2").reason)

    assert reasons == ["provider_retry_after_deferred"] * 3
    final = assert_failed(
        harness, run, "dependency_unavailable", "provider_retry_after_deferred"
    )
    assert final["attempt"] == final["max_attempts"] == 3
    record = harness.store().load(job.manifest_digest)
    assert ledger_view(record).not_before == int(start) + 120
    assert harness.observe(job) == {"R": 1, "F": 1, "A": 1, "P": 0, "C": 3}


def test_c5_advancing_past_the_deadline_sends_once_more(tmp_path):
    long_wait = Respond(429, {"error": {"code": 429}}, {"Retry-After": "120"})
    harness, job, _ = world(tmp_path, [long_wait, OK])
    harness.run_worker()
    harness.clock.advance(121)

    assert harness.run_worker(owner="worker-2").outcome == "completed"
    assert harness.observe(job) == {"R": 2, "F": 2, "A": 2, "P": 0, "C": 2}


def test_c6_fenced_heartbeat_during_an_in_call_delay_stops_forwarding(
    tmp_path, monkeypatch
):
    harness, job, run = world(tmp_path, [UNAVAILABLE, OK])

    async def another_worker_takes_over(delay, *_args, **_kwargs):
        harness.clock.advance(601)
        claimed = await harness.runtime().claim(
            product="sentryinsight",
            workflow_name="exploitation-report",
            workflow_version="1",
            lease_owner="other",
            lease_duration_seconds=600,
        )
        assert claimed["lease_version"] == 2

    monkeypatch.setattr(asyncio, "sleep", another_worker_takes_over)
    result = harness.run_worker()

    assert (result.outcome, result.reason) == ("lease_lost", "lease_lost")
    assert harness.observe(job) == {"R": 1, "F": 1, "A": 1, "P": 0, "C": 2}
    view = ledger_view(harness.store().load(job.manifest_digest))
    assert len(view.unconsumed_resolved) == 1

    harness.clock.advance(601)

    async def no_wait(*_args, **_kwargs):
        return None

    monkeypatch.setattr(asyncio, "sleep", no_wait)
    assert harness.run_worker(owner="worker-3").outcome == "completed"
    assert harness.observe(job) == {"R": 2, "F": 2, "A": 2, "P": 1, "C": 3}
    assert harness.run_doc(run["run_id"])["state"] == "succeeded"


# D: terminal unknowns and exact classification ---------------------------


def test_d1_unknown_exception_before_any_reservation_is_terminal(tmp_path):
    harness, job, run = world(tmp_path)

    harness.run_worker(fault=raise_at("after_claim", RuntimeError("secret-bug")))

    final = assert_failed(harness, run, "invalid_result", "worker_unclassified")
    assert "secret" not in final["error_summary"]
    assert "RuntimeError" not in json.dumps(
        harness.runtime_service.events(run["run_id"])
    )
    assert harness.observe(job) == {"R": 0, "F": 0, "A": 0, "P": 0, "C": 1}


def test_d2_unknown_exception_after_capture_quarantines_the_candidate(tmp_path):
    harness, job, run = world(tmp_path)

    harness.run_worker(fault=raise_at("after_analysis_record", RuntimeError("bug")))

    assert_failed(harness, run, "invalid_result", "worker_unclassified")
    record = harness.store().load(job.manifest_digest)
    assert record["stage"] == "analyzed" and record["analysis"]["sha256"]
    assert record["disposition"]["terminal"] is True
    assert artifact_dirs(harness, job) == []
    assert harness.observe(job)["R"] == 1


def test_d4_staging_permission_error_is_terminal_and_keeps_prepared_state(tmp_path):
    harness, job, run = world(tmp_path)
    harness.artifact_root.mkdir(parents=True)
    os.chmod(harness.artifact_root, stat.S_IRUSR | stat.S_IXUSR)
    try:
        result = harness.run_worker()
    finally:
        os.chmod(harness.artifact_root, stat.S_IRWXU)

    assert result.reason == "staging_failed"
    assert_failed(harness, run, "invalid_result", "staging_failed")
    record = harness.store().load(job.manifest_digest)
    assert record["stage"] == "analyzed" and record["analysis"] is not None


@pytest.mark.parametrize(
    "script, summary",
    [
        (
            [Respond(401), OK],
            "model_auth_rejected reserved=1 attempts=1 http_status=401",
        ),
        (
            [Respond(403), OK],
            "model_auth_rejected reserved=1 attempts=1 http_status=403",
        ),
        (
            [UNAVAILABLE, Respond(401), OK],
            "model_auth_rejected reserved=2 attempts=2 http_status=401",
        ),
        (
            [Respond(400, {"error": {"code": 503}}), OK],
            "model_response_rejected reserved=1 attempts=1 http_status=400 "
            "provider_code=503",
        ),
    ],
    ids=["401", "403", "auth_after_transient", "400_provider_503"],
)
def test_d5_auth_and_rejections_report_the_actual_ledger_count(
    tmp_path, script, summary
):
    harness, _, run = world(tmp_path, script)

    harness.run_worker()

    final = assert_failed(harness, run, "invalid_input", summary.split()[0])
    assert final["error_summary"] == summary


def test_d6_529_with_secret_text_is_rejected_and_sanitized(tmp_path):
    body = {"error": {"code": 529, "message": "fake-secret-token PROMPT-MARKER"}}
    harness, job, run = world(tmp_path, [Respond(529, body), OK])

    harness.run_worker()

    final = assert_failed(harness, run, "invalid_input", "model_response_rejected")
    assert harness.observe(job)["F"] == 1
    exported = json.dumps([final, harness.runtime_service.events(run["run_id"])])
    for marker in ("fake-secret", "PROMPT-MARKER", "OpenRouter", "Error", "Example"):
        assert marker not in exported


def test_d7_lost_fail_ack_is_reconciled_and_never_erased(tmp_path):
    harness, job, run = world(tmp_path, [Respond(400), OK])
    harness.runtime_service.drop_next_response("fail")

    first = harness.run_worker()
    assert (first.exit_code, first.reason) == (1, "runtime_unreachable")
    assert harness.store().load(job.manifest_digest)["runtime_ack"] is None

    second = harness.run_worker()

    assert (second.outcome, second.reconciled) == ("idle", 1)
    record = harness.store().load(job.manifest_digest)
    assert record["runtime_ack"]["state"] == "failed"
    assert record["disposition"]["reason"] == "model_response_rejected"
    assert harness.observe(job)["F"] == 1


def test_d7_unreported_quarantine_is_re_reported_by_a_new_lease(tmp_path):
    harness, job, run = world(tmp_path, [Respond(400), OK])

    async def runtime_down(name):
        if name == "before_runtime_report":
            harness.runtime_service.unavailable = "unreachable"

    first = harness.run_worker(fault=runtime_down)
    assert (first.exit_code, first.persisted) == (1, True)
    assert harness.run_doc(run["run_id"])["state"] == "running"
    harness.runtime_service.unavailable = None
    harness.expire_lease()

    second = harness.run_worker(owner="worker-2")

    assert second.reason == "model_response_rejected"
    assert_failed(harness, run, "invalid_input", "model_response_rejected")
    assert harness.observe(job) == {"R": 1, "F": 1, "A": 1, "P": 0, "C": 2}


# O: overlap ---------------------------------------------------------------


def test_o1_two_claimers_produce_one_lease_and_one_artifact(tmp_path):
    harness, job, run = world(tmp_path)

    async def both():
        return await asyncio.gather(
            harness.worker(owner="worker-1").run_once(),
            harness.worker(owner="worker-2").run_once(),
        )

    results = asyncio.run(both())

    assert sorted(result.outcome for result in results) == ["completed", "idle"]
    assert harness.observe(job) == {"R": 1, "F": 1, "A": 1, "P": 0, "C": 1}
    assert len(artifact_dirs(harness, job)) == 1


def test_o2_stale_process_paused_before_forward_cannot_send(tmp_path):
    harness, job, run = world(tmp_path)

    async def scenario():
        paused, release = asyncio.Event(), asyncio.Event()

        async def pause(name):
            if name == "after_reservation":
                paused.set()
                await release.wait()

        stale = asyncio.ensure_future(harness.worker(fault=pause).run_once())
        await paused.wait()
        harness.expire_lease()
        newer = await harness.worker(owner="worker-2").run_once()
        release.set()
        return newer, await stale

    newer, stale = asyncio.run(scenario())

    assert newer.reason == "provider_intent_unresolved"
    assert stale.outcome == "lease_lost"
    assert_failed(harness, run, "side_effect_conflict", "provider_intent_unresolved")
    assert harness.observe(job) == {"R": 1, "F": 0, "A": 0, "P": 0, "C": 2}


def test_o3_stale_forward_already_handed_over_completes_but_is_never_promoted(
    tmp_path,
):
    release = asyncio.Event()
    harness, job, run = world(tmp_path, [AcceptThenWait(release, OK), OK])

    async def scenario():
        stale = asyncio.ensure_future(harness.worker().run_once())
        while harness.provider.accepted == 0:
            await REAL_SLEEP(0)
        harness.expire_lease()
        newer = await harness.worker(owner="worker-2").run_once()
        release.set()
        return newer, await stale

    newer, stale = asyncio.run(scenario())

    assert newer.reason == "provider_intent_unresolved"
    assert stale.outcome == "lease_lost"
    assert harness.observe(job) == {"R": 1, "F": 1, "A": 1, "P": 0, "C": 2}
    assert outcome_types(harness, job) == [["ambiguous", "resolved"]]
    assert artifact_dirs(harness, job) == []
    assert harness.store().load(job.manifest_digest)["analysis"] is None
    assert_failed(harness, run, "side_effect_conflict", "provider_intent_unresolved")


# E: identity, configuration and stage recovery ---------------------------


def test_e2_environment_model_override_fails_closed(tmp_path, monkeypatch):
    harness, job, run = world(tmp_path)
    monkeypatch.setenv("SENTRYINSIGHT_MODEL", "openrouter/example/override:free")

    harness.run_worker()

    assert_failed(harness, run, "invalid_input", "effective_config_invalid")
    assert harness.observe(job)["F"] == 0


def test_code_identity_mismatch_fails_closed(tmp_path):
    harness = Harness(tmp_path / "world", [OK])
    job = harness.freeze(code_identity="0" * 64)
    run = harness.admit(job)

    harness.run_worker()

    assert_failed(harness, run, "unsupported_workflow", "unsupported_workflow_version")
    assert harness.observe(job)["F"] == 0


@pytest.mark.parametrize(
    "input_ref, code, reason",
    [
        (
            {
                "kind": INPUT_REF_KIND,
                "manifest_sha256": "../../x",
                "manifest_version": 1,
            },
            "invalid_input",
            "snapshot_invalid",
        ),
        (
            {
                "kind": INPUT_REF_KIND,
                "manifest_sha256": "f" * 64,
                "manifest_version": 1,
            },
            "invalid_input",
            "snapshot_invalid",
        ),
        (
            {
                "kind": INPUT_REF_KIND,
                "manifest_sha256": "f" * 64,
                "manifest_version": 2,
            },
            "unsupported_workflow",
            "unsupported_manifest_version",
        ),
    ],
    ids=["path_escape", "missing_snapshot", "manifest_version"],
)
def test_e3_unusable_input_is_rejected_before_any_send(
    tmp_path, input_ref, code, reason
):
    harness = Harness(tmp_path / "world", [OK])
    job = harness.freeze()
    run = harness.admit(job, input_ref=input_ref)

    harness.run_worker()

    assert_failed(harness, run, code, reason)
    assert harness.provider.forwards == 0


def test_e3_input_budget_overflow_is_rejected_before_any_send(tmp_path):
    harness = Harness(tmp_path / "world", [OK])
    job = harness.freeze(config=synthetic_config(max_input_tokens=10))
    run = harness.admit(job)

    harness.run_worker()

    assert_failed(harness, run, "invalid_input", "input_budget_exceeded")
    assert harness.observe(job)["F"] == 0


def test_e4_grounding_rejection_keeps_the_candidate_and_never_regenerates(tmp_path):
    harness, job, run = world(
        tmp_path, [Respond(200, completion_body(GROUNDING_REJECTED_REPORT)), OK]
    )

    harness.run_worker()

    assert_failed(harness, run, "invalid_result", "report_grounding_rejected")
    store = harness.store()
    record = store.load(job.manifest_digest)
    candidate = json.loads(
        store.get_blob(job.manifest_digest, record["analysis"]["sha256"])
    )
    assert candidate["exploitation_report"] == GROUNDING_REJECTED_REPORT
    diagnostic = record["disposition"]["diagnostic"]
    assert diagnostic["stage"] in ("finding_evidence", "reporting_identity")
    assert harness.observe(job)["R"] == 1
    assert artifact_dirs(harness, job) == []


def test_e5_f2_crash_after_claim_reserves_and_sends_normally(tmp_path):
    harness, job, _ = world(tmp_path)
    crash(harness, fault=crash_at("after_claim"))
    harness.expire_lease()

    assert harness.run_worker(owner="worker-2").outcome == "completed"
    assert harness.observe(job) == {"R": 1, "F": 1, "A": 1, "P": 0, "C": 2}


@pytest.mark.parametrize(
    "point", ["after_analysis_record", "after_artifact_record"], ids=["F5", "F6"]
)
def test_e5_stage_crashes_rebuild_or_reuse_the_same_artifact(tmp_path, point):
    harness, job, run = world(tmp_path)
    crash(harness, fault=crash_at(point))
    harness.expire_lease()

    assert harness.run_worker(owner="worker-2").outcome == "completed"

    assert harness.observe(job) == {"R": 1, "F": 1, "A": 1, "P": 0, "C": 2}
    clean, _, clean_run = world(tmp_path / "clean")
    clean.run_worker()
    assert (
        harness.run_doc(run["run_id"])["output_ref"]
        == clean.run_doc(clean_run["run_id"])["output_ref"]
    )
    assert len(artifact_dirs(harness, job)) == 1

"""Runtime client against the execution-service test double."""

import asyncio

import pytest

from src.runtime_adapter.fakes import FakeRuntimeService, SyntheticClock
from src.runtime_adapter.runtime_client import RuntimeApiError, RuntimeClient

SCOPE = {
    "product": "sentryinsight",
    "workflow_name": "exploitation-report",
    "workflow_version": "1",
}
INPUT = {"kind": "sentryinsight.frozen_job", "manifest_sha256": "a" * 64}


@pytest.fixture
def runtime(tmp_path):
    clock = SyntheticClock(tmp_path / "clock.json")
    service = FakeRuntimeService(tmp_path / "runtime.json", clock, retry_delay=5)
    client = RuntimeClient(transport=service.transport())
    return clock, service, client


def run(coroutine):
    return asyncio.run(coroutine)


def submit(client, key="job-key", input_ref=INPUT, max_attempts=3):
    return run(
        client.submit(
            **SCOPE,
            idempotency_key=key,
            input_ref=input_ref,
            max_attempts=max_attempts,
        )
    )


def claim(client, owner="worker-a", duration=600, **scope):
    return run(
        client.claim(
            **dict(SCOPE, **scope), lease_owner=owner, lease_duration_seconds=duration
        )
    )


def fail(client, lease, code, summary=None, owner="worker-a"):
    return run(
        client.fail(
            lease["run_id"],
            lease_owner=owner,
            lease_version=lease["lease_version"],
            error_code=code,
            error_summary=summary,
        )
    )


def event_types(service, run_id):
    return [event["event_type"] for event in service.events(run_id)]


def test_submit_is_idempotent_and_returns_the_existing_run(runtime):
    _, service, client = runtime

    first, created = submit(client)
    second, created_again = submit(client)

    assert (created, created_again) == (True, False)
    assert first["run_id"] == second["run_id"]
    assert first["state"] == "queued" and first["attempt"] == 0
    assert len(service.runs()) == 1
    assert event_types(service, first["run_id"]) == ["submitted"]


def test_lost_submit_acknowledgement_resolves_to_the_same_run(runtime):
    _, service, client = runtime
    service.drop_next_response("submit")

    with pytest.raises(RuntimeApiError) as raised:
        submit(client)
    assert raised.value.reason == "runtime_unreachable"

    run_doc, created = submit(client)
    assert created is False
    assert len(service.runs()) == 1
    assert event_types(service, run_doc["run_id"]) == ["submitted"]


def test_same_key_with_a_different_request_surfaces_conflict(runtime):
    _, service, client = runtime
    original, _ = submit(client)

    for changed in (
        {"input_ref": dict(INPUT, manifest_sha256="b" * 64)},
        {"max_attempts": 4},
    ):
        with pytest.raises(RuntimeApiError) as raised:
            submit(client, **changed)
        assert raised.value.reason == "idempotency_conflict"
        assert raised.value.existing_run_id == original["run_id"]
    assert len(service.runs()) == 1


def test_claim_is_scoped_and_reports_no_eligible_run(runtime):
    _, _, client = runtime
    assert claim(client) is None
    run_doc, _ = submit(client)

    assert claim(client, workflow_version="2") is None
    lease = claim(client)
    assert (lease["run_id"], lease["state"]) == (run_doc["run_id"], "running")
    assert (lease["attempt"], lease["lease_version"]) == (1, 1)
    assert claim(client, owner="worker-b") is None


def test_heartbeat_and_completion_are_fenced_by_lease(runtime):
    clock, service, client = runtime
    run_doc, _ = submit(client)
    lease = claim(client)

    run(
        client.heartbeat(
            run_doc["run_id"],
            lease_owner="worker-a",
            lease_version=1,
            lease_duration_seconds=600,
        )
    )
    clock.advance(601)
    newer = claim(client, owner="worker-b")
    assert (newer["attempt"], newer["lease_version"]) == (2, 2)

    for stale_call in (
        client.heartbeat(
            lease["run_id"],
            lease_owner="worker-a",
            lease_version=1,
            lease_duration_seconds=600,
        ),
        client.complete(
            lease["run_id"],
            lease_owner="worker-a",
            lease_version=1,
            output_ref={"artifact_sha256": "c" * 64},
        ),
    ):
        with pytest.raises(RuntimeApiError) as raised:
            run(stale_call)
        assert raised.value.reason == "lease_fenced"

    assert event_types(service, run_doc["run_id"]) == [
        "submitted",
        "lease_acquired",
        "heartbeat_recorded",
        "lease_expired",
        "retry_scheduled",
        "lease_acquired",
    ]


def test_expired_lease_with_no_attempts_left_fails_as_worker_error(runtime):
    clock, service, client = runtime
    run_doc, _ = submit(client, max_attempts=1)
    claim(client)
    clock.advance(601)

    assert claim(client, owner="worker-b") is None

    final = run(client.get_run(run_doc["run_id"]))
    assert (final["state"], final["error_code"]) == ("failed", "worker_error")
    assert final["error_summary"] == "lease expired and attempt budget exhausted"
    assert event_types(service, run_doc["run_id"])[-2:] == ["lease_expired", "failed"]


def test_retry_codes_use_fixed_delay_until_attempts_run_out(runtime):
    clock, _, client = runtime
    run_doc, _ = submit(client, max_attempts=2)

    first = claim(client)
    retried = fail(client, first, "dependency_unavailable", "reason reserved=1")
    assert retried["state"] == "retry_wait"
    assert retried["error_summary"] == "reason reserved=1"
    assert claim(client) is None
    clock.advance(5)
    second = claim(client)
    assert (second["attempt"], second["lease_version"]) == (2, 2)
    assert second.get("error_summary") is None

    final = fail(client, second, "dependency_unavailable")
    assert (final["state"], final["error_code"]) == ("failed", "dependency_unavailable")
    assert run(client.get_run(run_doc["run_id"]))["state"] == "failed"


@pytest.mark.parametrize(
    "code",
    ["invalid_input", "invalid_result", "unsupported_workflow", "side_effect_conflict"],
)
def test_terminal_codes_fail_immediately_and_runs_are_immutable(runtime, code):
    _, _, client = runtime
    submit(client)
    lease = claim(client)

    failed = fail(client, lease, code)

    assert failed["state"] == "failed"
    with pytest.raises(RuntimeApiError) as raised:
        fail(client, lease, code)
    assert raised.value.reason == "lease_fenced"
    with pytest.raises(RuntimeApiError):
        run(
            client.complete(
                lease["run_id"],
                lease_owner="worker-a",
                lease_version=lease["lease_version"],
                output_ref={"artifact_sha256": "c" * 64},
            )
        )


@pytest.mark.parametrize(
    "code, summary",
    [("worker_crashed", None), ("unknown", "x" * 513)],
)
def test_fail_rejects_codes_outside_the_closed_set_and_long_summaries(
    runtime, code, summary
):
    _, _, client = runtime
    submit(client)
    lease = claim(client)

    with pytest.raises(RuntimeApiError) as raised:
        fail(client, lease, code, summary)

    assert raised.value.reason == "runtime_invalid_request"
    assert run(client.get_run(lease["run_id"]))["state"] == "running"


def test_completion_records_output_and_is_terminal(runtime):
    _, service, client = runtime
    run_doc, _ = submit(client)
    lease = claim(client)
    output = {"kind": "sentryinsight.prepared_artifact", "artifact_sha256": "c" * 64}

    done = run(
        client.complete(
            run_doc["run_id"],
            lease_owner="worker-a",
            lease_version=lease["lease_version"],
            output_ref=output,
        )
    )

    assert (done["state"], done["output_ref"]) == ("succeeded", output)
    events = run(client.list_events(run_doc["run_id"]))
    assert [event["sequence"] for event in events] == [1, 2, 3]
    assert events[-1]["event_type"] == "succeeded"


@pytest.mark.parametrize(
    "mode, reason",
    [
        ("draining", "runtime_draining"),
        ("unauthorized", "runtime_auth_rejected"),
        ("forbidden", "runtime_auth_rejected"),
        ("unreachable", "runtime_unreachable"),
    ],
)
def test_control_plane_failures_never_map_to_success(runtime, mode, reason):
    _, service, client = runtime
    run_doc, _ = submit(client)
    service.unavailable = mode

    for call in (
        client.get_run(run_doc["run_id"]),
        client.claim(**SCOPE, lease_owner="worker-a", lease_duration_seconds=600),
        client.list_events(run_doc["run_id"]),
    ):
        with pytest.raises(RuntimeApiError) as raised:
            run(call)
        assert raised.value.reason == reason


def test_unknown_run_is_reported_as_not_found(runtime):
    _, _, client = runtime

    with pytest.raises(RuntimeApiError) as raised:
        run(client.get_run("00000000-0000-0000-0000-000000000000"))

    assert raised.value.reason == "run_not_found"


def test_due_retry_is_claimed_before_a_queued_run(runtime):
    # The test double prioritizes a due retry over an unscheduled queued run.
    clock, _, client = runtime
    retrying, _ = submit(client, key="first")
    fail(client, claim(client), "dependency_unavailable")
    submit(client, key="second", input_ref=dict(INPUT, manifest_sha256="b" * 64))
    clock.advance(5)

    assert claim(client)["run_id"] == retrying["run_id"]


def test_fake_runtime_state_survives_a_restart(runtime, tmp_path):
    clock, _, client = runtime
    run_doc, _ = submit(client)
    claim(client)

    restarted = FakeRuntimeService(tmp_path / "runtime.json", clock, retry_delay=5)
    fresh_client = RuntimeClient(transport=restarted.transport())

    assert run(fresh_client.get_run(run_doc["run_id"]))["lease_version"] == 1
    assert restarted.lease_grants(run_doc["run_id"]) == 1

"""A closed manual trial cannot expand its two approved requests."""

from dataclasses import replace
import json
import os
from pathlib import Path
import stat
import sys

import httpx
import pytest

from scripts.verify_selected_models_once import (
    CASES,
    Case,
    Claim,
    Context,
    Layout,
    TrialError,
    execute,
    prepare_all,
    validate_context,
    validate_prior_runs,
    validate_wire,
    worker_environment,
)


@pytest.fixture(scope="module")
def layout():
    names = (
        "SELECTED_TRIAL_SENTRY_SOURCE",
        "SELECTED_TRIAL_GRC_SOURCE",
        "SELECTED_TRIAL_GRC_PYTHON",
    )
    if any(not os.environ.get(name) for name in names):
        pytest.fail(reason="Set the three documented accepted-source/interpreter paths")
    return Layout(
        Path(os.environ[names[0]]),
        Path(os.environ[names[1]]),
        Path(sys.executable),
        Path(os.environ[names[2]]),
        Path(os.environ["TIKTOKEN_CACHE_DIR"]),
    )


@pytest.fixture(scope="module")
def prepared(layout):
    return prepare_all(layout)


def context_env():
    return {
        "GITHUB_ACTIONS": "true",
        "GITHUB_REPOSITORY": "ricomanifesto/SentryInsight",
        "GITHUB_EVENT_NAME": "workflow_dispatch",
        "GITHUB_REF": "refs/heads/test/selected-model-fixtures-20261104",
        "GITHUB_SHA": "a" * 40,
        "GITHUB_RUN_ID": "12345",
        "GITHUB_RUN_ATTEMPT": "1",
        "GITHUB_ACTOR": "ricomanifesto",
        "GITHUB_TRIGGERING_ACTOR": "ricomanifesto",
        "GITHUB_WORKFLOW_REF": "ricomanifesto/SentryInsight/.github/workflows/verify-nemotron.yml@refs/heads/test/selected-model-fixtures-20261104",
    }


@pytest.mark.parametrize(
    "key,value",
    [
        ("GITHUB_ACTIONS", "false"),
        ("GITHUB_REF", "refs/heads/main"),
        ("GITHUB_EVENT_NAME", "push"),
        ("GITHUB_RUN_ATTEMPT", "2"),
        ("GITHUB_ACTOR", "someone"),
        ("GITHUB_TRIGGERING_ACTOR", "someone"),
        ("GITHUB_SHA", "b" * 40),
    ],
)
def test_wrong_manual_context_is_refused_before_any_sender(key, value):
    env = context_env()
    env[key] = value
    with pytest.raises(TrialError):
        validate_context(env, "a" * 40)


def test_prior_run_guard_refuses_fresh_dispatch_replay():
    context = validate_context(context_env(), "a" * 40)
    current = {
        "id": 12345,
        "head_sha": "a" * 40,
        "head_branch": context.ref.removeprefix("refs/heads/"),
        "event": "workflow_dispatch",
        "run_attempt": 1,
        "actor": {"login": "ricomanifesto"},
        "triggering_actor": {"login": "ricomanifesto"},
        "path": ".github/workflows/verify-nemotron.yml",
    }
    validate_prior_runs(context, {"total_count": 1, "workflow_runs": [current]})
    with pytest.raises(TrialError):
        validate_prior_runs(
            context,
            {"total_count": 2, "workflow_runs": [current, dict(current, id=99)]},
        )


def test_both_actual_offline_workers_reproduce_approved_exact_wire(prepared):
    assert set(prepared) == {Case.SENTRY, Case.GRC}
    for case, value in prepared.items():
        assert value.spec is CASES[case]
        assert len(value.wire) == value.spec.wire_bytes
        assert validate_wire(case, value.wire).wire == value.wire
        with pytest.raises(TrialError):
            validate_wire(case, value.wire + b" ")
        altered = json.loads(value.wire)
        altered["provider"]["allow_fallbacks"] = True
        with pytest.raises(TrialError):
            validate_wire(case, json.dumps(altered).encode())
        assert "messages" not in repr(value)


def test_worker_environment_omits_every_real_credential(tmp_path):
    env = worker_environment(
        tmp_path,
        tmp_path,
        {
            "PATH": os.defpath,
            "OPENROUTER_API_KEY": "must-not-escape",
            "GITHUB_TOKEN": "must-not-escape",
            "AWS_PROFILE": "must-not-escape",
            "LOGFIRE_TOKEN": "must-not-escape",
        },
    )
    assert "must-not-escape" not in json.dumps(env)
    assert env["AWS_CONFIG_FILE"] == env["AWS_SHARED_CREDENTIALS_FILE"] == "/dev/null"
    assert env["AWS_EC2_METADATA_DISABLED"] == "true"


def test_claim_is_exclusive_private_and_sending_is_durable(tmp_path):
    path = tmp_path / "claim.json"
    with Claim(path, Context("a" * 40, "12345", context_env()["GITHUB_REF"])) as claim:
        assert stat.S_IMODE(path.stat().st_mode) == 0o600
        claim.start(Case.SENTRY)
        assert json.loads(path.read_text())["states"]["sentry"] == "sending"
        with pytest.raises(TrialError):
            claim.start(Case.SENTRY)
        with pytest.raises(TrialError):
            Claim(path, Context("a" * 40, "12345", context_env()["GITHUB_REF"]))
    with pytest.raises(TrialError):
        Claim(path, Context("a" * 40, "12345", context_env()["GITHUB_REF"]))


@pytest.mark.parametrize("replacement", ["symlink", "hardlink", "mode"])
def test_claim_path_replacement_is_refused_before_state_update(tmp_path, replacement):
    path = tmp_path / "claim.json"
    with Claim(path, Context("a" * 40, "12345", context_env()["GITHUB_REF"])) as claim:
        if replacement == "mode":
            path.chmod(0o644)
        elif replacement == "hardlink":
            os.link(path, tmp_path / "second-link")
        else:
            saved = tmp_path / "saved"
            path.rename(saved)
            path.symlink_to(saved)
        with pytest.raises(TrialError):
            claim.start(Case.SENTRY)


def fake_response(case, layout):
    spec = CASES[case]
    if case is Case.SENTRY:
        value = json.loads((layout.sentry / spec.fixture).read_text())[
            "calibration_response"
        ]
    else:
        value = json.dumps(
            json.loads((layout.grc / spec.fixture).read_text())["calibration_plan"]
        )
    return {
        "model": spec.model,
        "service_tier": "default",
        "id": "gen-fixed-test",
        "choices": [{"finish_reason": "stop", "message": {"content": value}}],
        "usage": {
            "prompt_tokens": 4000,
            "completion_tokens": 1000,
            "total_tokens": 5000,
            "completion_tokens_details": {"reasoning_tokens": 300},
            "cost": 0.018,
        },
    }


def test_exact_two_posts_actual_host_replay_and_no_raw_receipt(
    tmp_path, prepared, layout
):
    seen = []

    def handler(request):
        case = list(Case)[len(seen)]
        seen.append(request)
        assert request.content == prepared[case].wire
        assert str(request.url) == "https://openrouter.ai/api/v1/chat/completions"
        return httpx.Response(200, json=fake_response(case, layout))

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        receipt = execute(
            prepared,
            layout,
            Context("a" * 40, "12345", context_env()["GITHUB_REF"]),
            tmp_path / "claim.json",
            lambda: "synthetic-test-key",
            client,
        )
    assert len(seen) == 2
    assert all(row["host"]["outcome"] == "passed" for row in receipt["cases"])
    assert receipt["actual_cost"] == pytest.approx(0.036)
    encoded = json.dumps(receipt)
    for marker in (
        "synthetic-test-key",
        "Executive Summary",
        "Customers should",
        "Example Supplier",
        "choices",
        "content",
    ):
        assert marker not in encoded


@pytest.mark.parametrize(
    "failure", ["401", "402", "redirect", "timeout", "invalid_json", "wrong_model"]
)
def test_first_response_failure_consumes_claim_and_stops_argon(
    tmp_path, prepared, layout, failure
):
    seen = []

    def handler(request):
        seen.append(request)
        if failure == "timeout":
            raise httpx.ReadTimeout("untrusted provider detail")
        if failure in {"401", "402", "redirect"}:
            return httpx.Response(
                302 if failure == "redirect" else int(failure),
                text="untrusted provider detail",
                headers={"Location": "https://example.invalid/leak"},
            )
        if failure == "invalid_json":
            return httpx.Response(200, text="untrusted provider detail")
        response = fake_response(Case.SENTRY, layout)
        response["model"] = "wrong/model"
        return httpx.Response(200, json=response)

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        receipt = execute(
            prepared,
            layout,
            Context("a" * 40, "12345", context_env()["GITHUB_REF"]),
            tmp_path / "claim.json",
            lambda: "synthetic-test-key",
            client,
        )
    assert len(seen) == 1
    assert (
        json.loads((tmp_path / "claim.json").read_text())["states"]["grc"] == "pending"
    )
    assert "untrusted provider detail" not in json.dumps(receipt)


def test_mutated_preparation_cannot_read_key_or_send(tmp_path, prepared, layout):
    bad = dict(prepared)
    bad[Case.GRC] = replace(prepared[Case.GRC], wire=b"invalid")
    with httpx.Client(
        transport=httpx.MockTransport(lambda _: pytest.fail(reason="POST"))
    ) as client:
        with pytest.raises(TrialError):
            execute(
                bad,
                layout,
                Context("a" * 40, "12345", context_env()["GITHUB_REF"]),
                tmp_path / "claim.json",
                lambda: pytest.fail(reason="credential accessed"),
                client,
            )
    assert not (tmp_path / "claim.json").exists()


def test_known_complete_host_failure_can_continue_without_repair(
    tmp_path, prepared, layout
):
    seen = []

    def handler(request):
        case = list(Case)[len(seen)]
        seen.append(request)
        response = fake_response(case, layout)
        if case is Case.SENTRY:
            response["choices"][0]["message"][
                "content"
            ] = "A complete but unsupported answer."
        return httpx.Response(200, json=response)

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        receipt = execute(
            prepared,
            layout,
            Context("a" * 40, "12345", context_env()["GITHUB_REF"]),
            tmp_path / "claim.json",
            lambda: "synthetic-test-key",
            client,
        )
    assert len(seen) == 2
    assert [row["outcome"] for row in receipt["cases"]] == [
        "host_validation_failed",
        "passed",
    ]


@pytest.mark.parametrize(
    "field,value",
    [
        ("service_tier", "priority"),
        ("provider", "Other provider"),
        ("usage", {"completion_tokens": 32001}),
        ("usage", {"prompt_tokens": 20001}),
        ("usage", {"cost": 0.361}),
        (
            "usage",
            {
                "completion_tokens": 1,
                "completion_tokens_details": {"reasoning_tokens": 2},
            },
        ),
    ],
)
def test_unapproved_response_metadata_stops_second_request(
    tmp_path, prepared, layout, field, value
):
    seen = []

    def handler(request):
        seen.append(request)
        response = fake_response(Case.SENTRY, layout)
        response[field] = value
        return httpx.Response(200, json=response)

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        receipt = execute(
            prepared,
            layout,
            Context("a" * 40, "12345", context_env()["GITHUB_REF"]),
            tmp_path / "claim.json",
            lambda: "synthetic-test-key",
            client,
        )
    assert len(seen) == 1
    assert receipt["cases"][0]["outcome"] == "transport_or_protocol_unknown"


@pytest.mark.parametrize(
    "missing",
    [
        "usage",
        "service_tier",
        "null_tier",
        "cost",
        "total_tokens",
        "inconsistent_total",
    ],
)
def test_missing_usage_or_tier_remains_unknown_and_stops(
    tmp_path, prepared, layout, missing
):
    seen = []

    def handler(request):
        case = list(Case)[len(seen)]
        seen.append(request)
        response = fake_response(case, layout)
        if missing in {"usage", "service_tier"}:
            del response[missing]
        elif missing == "null_tier":
            response["service_tier"] = None
        elif missing == "inconsistent_total":
            response["usage"]["total_tokens"] = 9999
        else:
            del response["usage"][missing]
        return httpx.Response(200, json=response)

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        receipt = execute(
            prepared,
            layout,
            Context("a" * 40, "12345", context_env()["GITHUB_REF"]),
            tmp_path / "claim.json",
            lambda: "synthetic-test-key",
            client,
        )
    assert len(seen) == 1
    row = receipt["cases"][0]
    assert (
        row["outcome"] == "accounting_or_tier_unknown"
        and row["host"]["outcome"] == "passed"
    )
    assert row["serving_provider"] is None
    assert (
        json.loads((tmp_path / "claim.json").read_text())["states"]["grc"] == "pending"
    )
    if missing in {"usage", "cost"}:
        assert receipt["actual_cost"] is None
    if missing in {"service_tier", "null_tier"}:
        assert row["actual_service_tier"] is None


def test_metadata_worker_cannot_export_answer_or_unbounded_diagnostics():
    from scripts.verify_selected_models_once import validate_host_metadata

    for value in (
        {"outcome": "failed", "stage": "raw answer"},
        {"outcome": "failed", "stage": "host_rejected", "answer": "raw answer"},
    ):
        with pytest.raises(TrialError):
            validate_host_metadata(Case.SENTRY, value)


def test_oversized_success_body_stops_without_reading_second_case(
    tmp_path, prepared, layout
):
    from scripts.verify_selected_models_once import RESPONSE_LIMIT

    seen = []

    def handler(request):
        seen.append(request)
        return httpx.Response(200, content=b"x" * (RESPONSE_LIMIT + 1))

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        receipt = execute(
            prepared,
            layout,
            Context("a" * 40, "12345", context_env()["GITHUB_REF"]),
            tmp_path / "claim.json",
            lambda: "synthetic-test-key",
            client,
        )
    assert (
        len(seen) == 1
        and receipt["cases"][0]["outcome"] == "transport_or_protocol_unknown"
    )


def test_remote_commit_and_blob_fences_are_read_only_and_fail_closed():
    from scripts.verify_selected_models_once import REMOTE_MAIN, remote_snapshot

    seen = []
    moved = False

    def handler(request):
        seen.append(request)
        assert request.method == "GET" and "authorization" not in request.headers
        repo = request.url.path.split("/")[3]
        if "/git/ref/" in request.url.path:
            return httpx.Response(
                200, json={"object": {"sha": "b" * 40 if moved else REMOTE_MAIN[repo]}}
            )
        return httpx.Response(
            200,
            json={
                "truncated": False,
                "tree": [{"type": "blob", "path": "index.md", "sha": "c" * 40}],
            },
        )

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        before = remote_snapshot(client)
        assert before == remote_snapshot(client)
        moved = True
        with pytest.raises(TrialError):
            remote_snapshot(client)
    assert len(seen) == 9


def test_branch_workflow_has_only_fixed_read_only_nonpublishing_authority():
    import yaml
    from scripts.verify_selected_models_once import ROOT, TEST_REF

    workflow = yaml.load(
        (ROOT / ".github/workflows/verify-nemotron.yml").read_text(),
        Loader=yaml.BaseLoader,
    )
    assert set(workflow["on"]) == {"workflow_dispatch"}
    assert workflow["permissions"] == {"contents": "read"}
    job = workflow["jobs"]["verify"]
    for guard in (
        TEST_REF,
        "github.sha == inputs.expected_commit",
        "github.run_attempt == 1",
        "github.actor == 'ricomanifesto'",
        "github.triggering_actor == 'ricomanifesto'",
    ):
        assert guard in job["if"]
    secret_steps = [row for row in job["steps"] if "secrets." in json.dumps(row)]
    assert len(secret_steps) == 1 and secret_steps[0]["id"] == "trial"
    assert "continue_vertex_trial_once.py" in secret_steps[0]["run"]
    assert "verify_selected_models_once.py" not in secret_steps[0]["run"]
    checkouts = [
        row
        for row in job["steps"]
        if row.get("uses", "").startswith("actions/checkout@")
    ]
    assert len(checkouts) == 3
    assert all(row["with"]["persist-credentials"] == "false" for row in checkouts)
    assert {row["with"]["ref"] for row in checkouts} == {
        "${{ github.sha }}",
        *(s.source_sha for s in CASES.values()),
    }
    artifact = job["steps"][-1]["with"]
    assert artifact["retention-days"] == "7" and "*" not in artifact["path"]
    assert (
        json.loads((ROOT / "vercel.json").read_text())["git"]["deploymentEnabled"]
        is False
    )


@pytest.mark.parametrize(
    "failure", ["unavailable", "timeout", "malformed", "extra_metadata"]
)
def test_unknown_replay_execution_stops_before_second_post(
    tmp_path, prepared, layout, monkeypatch, failure
):
    import scripts.verify_selected_models_once as trial

    seen = []

    def handler(request):
        seen.append(request)
        return httpx.Response(200, json=fake_response(Case.SENTRY, layout))

    async def replay(*_args):
        if failure == "timeout":
            raise TimeoutError("untrusted child detail")
        if failure == "unavailable":
            raise TrialError("worker_failed")
        if failure == "malformed":
            return b"not JSON"
        return b'{"outcome":"failed","stage":"host_rejected","raw":"untrusted child detail"}'

    monkeypatch.setattr(trial, "_worker", replay)
    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        receipt = execute(
            prepared,
            layout,
            Context("a" * 40, "12345", context_env()["GITHUB_REF"]),
            tmp_path / "claim.json",
            lambda: "synthetic-test-key",
            client,
        )
    assert len(seen) == 1 and receipt["cases"][0]["outcome"] == "replay_unknown"
    assert (
        json.loads((tmp_path / "claim.json").read_text())["states"]["grc"] == "pending"
    )
    assert "untrusted child detail" not in json.dumps(receipt)


@pytest.fixture(scope="module")
def argon_prepared(layout):
    from scripts.continue_argon_trial_once import prepare_argon

    return prepare_argon(layout)


def test_argon_first_durable_claim_marks_prior_consumed_and_never_rearms(
    tmp_path, monkeypatch
):
    from scripts.continue_argon_trial_once import ArgonClaim, PRIOR_RUN, PRIOR_EXECUTOR

    snapshots = []
    original = Claim._save

    def save(claim):
        snapshots.append(json.loads(json.dumps(claim.value)))
        original(claim)

    monkeypatch.setattr(Claim, "_save", save)
    with ArgonClaim(
        tmp_path / "claim.json", Context("a" * 40, "54321", context_env()["GITHUB_REF"])
    ) as claim:
        assert snapshots[0]["states"] == {
            "sentry": "consumed_prior_run",
            "grc": "pending",
        }
        assert snapshots[0]["prior_run_id"] == PRIOR_RUN == "41777105615"
        assert (
            snapshots[0]["prior_executor_commit"]
            == PRIOR_EXECUTOR
            == "26234bd3f1cd7e580c739c019c50bf217ed13d84"
        )
        assert snapshots[0]["reserved_microusd"] == 484000
        for case in (Case.SENTRY,):
            with pytest.raises(TrialError):
                claim.start(case)
            with pytest.raises(TrialError):
                claim.finish(case, "response_received")
        claim.start(Case.GRC)
        claim.finish(Case.GRC, "response_received")
    assert all(row["states"]["sentry"] == "consumed_prior_run" for row in snapshots)


def test_argon_only_preparation_never_invokes_kimi_worker(layout, monkeypatch):
    import scripts.continue_argon_trial_once as continuation
    import scripts.verify_selected_models_once as base

    called = []
    worker = base._worker

    async def guard(layout, case, mode, response=b""):
        called.append((case, mode))
        assert case is Case.GRC
        return await worker(layout, case, mode, response)

    monkeypatch.setattr(base, "_worker", guard)
    result = continuation.prepare_argon(layout)
    assert called == [(Case.GRC, "prepare")]
    assert result.spec is CASES[Case.GRC]


def test_argon_continuation_posts_only_exact_remaining_body(
    tmp_path, argon_prepared, layout
):
    from scripts.continue_argon_trial_once import execute_argon

    seen = []

    def read_key():
        claim = json.loads((tmp_path / "claim.json").read_text())
        assert claim["states"] == {"sentry": "consumed_prior_run", "grc": "pending"}
        return "synthetic-test-key"

    def handler(request):
        seen.append(request)
        assert len(seen) == 1 and request.content == argon_prepared.wire
        assert json.loads(request.content)["model"] == "google/gemini-4-argon"
        return httpx.Response(200, json=fake_response(Case.GRC, layout))

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        receipt = execute_argon(
            argon_prepared,
            layout,
            Context("a" * 40, "54321", context_env()["GITHUB_REF"]),
            tmp_path / "claim.json",
            read_key,
            client,
        )
    assert len(seen) == 1 and len(receipt["cases"]) == 1
    assert receipt["cases"][0]["host"]["outcome"] == "passed"
    assert (
        receipt["actual_cost"] == 0.018
        and receipt["cost_scope"] == "this_continuation_only"
    )
    assert receipt["upper_estimate_usd"] == 0.484
    assert receipt["prior_run_id"] == "41777105615"
    assert "synthetic-test-key" not in json.dumps(receipt)


@pytest.mark.parametrize(
    "failure", ["401", "timeout", "null_tier", "missing_cost", "bad_replay"]
)
def test_argon_continuation_failure_has_no_retry_or_kimi(
    tmp_path, argon_prepared, layout, monkeypatch, failure
):
    from scripts.continue_argon_trial_once import execute_argon
    import scripts.verify_selected_models_once as base

    seen = []

    def handler(request):
        seen.append(request)
        if failure == "401":
            return httpx.Response(401, text="raw error must stay private")
        if failure == "timeout":
            raise httpx.ReadTimeout("raw error must stay private")
        response = fake_response(Case.GRC, layout)
        if failure == "null_tier":
            response["service_tier"] = None
        if failure == "missing_cost":
            del response["usage"]["cost"]
        return httpx.Response(200, json=response)

    async def bad_worker(*_args):
        raise TrialError("worker_failed")

    if failure == "bad_replay":
        monkeypatch.setattr(base, "_worker", bad_worker)
    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        receipt = execute_argon(
            argon_prepared,
            layout,
            Context("a" * 40, "54321", context_env()["GITHUB_REF"]),
            tmp_path / "claim.json",
            lambda: "synthetic-test-key",
            client,
        )
    assert len(seen) == 1 and receipt["cases"][0]["outcome"] != "passed"
    assert (
        json.loads((tmp_path / "claim.json").read_text())["states"]["sentry"]
        == "consumed_prior_run"
    )
    assert "raw error must stay private" not in json.dumps(receipt)


def test_argon_continuation_refuses_kimi_or_mutation_before_key(
    tmp_path, prepared, layout
):
    from scripts.continue_argon_trial_once import execute_argon

    for value in (prepared[Case.SENTRY], replace(prepared[Case.GRC], wire=b"invalid")):
        with httpx.Client(
            transport=httpx.MockTransport(lambda _: pytest.fail(reason="POST"))
        ) as client:
            with pytest.raises(TrialError):
                execute_argon(
                    value,
                    layout,
                    Context("a" * 40, "54321", context_env()["GITHUB_REF"]),
                    tmp_path / "claim.json",
                    lambda: pytest.fail(reason="key"),
                    client,
                )
    assert not (tmp_path / "claim.json").exists()

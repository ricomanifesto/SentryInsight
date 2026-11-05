"""One synthetic request, explicit recipient, and no production writer."""

import asyncio
import copy
import json
from pathlib import Path

import httpx
import pytest
import yaml

from scripts import verify_nemotron_once as trial


def reply(content, **overrides):
    return httpx.Response(
        200,
        json={
            "model": trial.MODEL_ID,
            "choices": [{"finish_reason": "stop", "message": {"content": content}}],
            "usage": {"cost": 0, "prompt_tokens": 5000, "completion_tokens": 500},
            **overrides,
        },
    )


def test_offline_calibration_binds_small_synthetic_prompt_and_held_source():
    receipt = asyncio.run(trial.calibrate())
    assert receipt["calibration_passed"] is True
    assert receipt["source_counts"] == {"eligible": 1, "review_required": 1}
    assert receipt["live_attempted"] == 0
    assert 0 < receipt["input_tokens_with_reserve"] <= 16000
    assert receipt["provider_policy"] == {
        "only": ["nvidia"],
        "allow_fallbacks": False,
        "max_price": {"prompt": 0, "completion": 0, "request": 0, "image": 0},
    }
    assert receipt["published"] is receipt["production_ready"] is False
    assert receipt["human_review"] == "not_performed"


@pytest.mark.parametrize("valid", [True, False])
def test_real_validation_accepts_supported_output_and_rejects_unsupported_claim(
    valid, tmp_path, monkeypatch
):
    calibration = asyncio.run(trial.calibrate())
    case = trial.load_case()
    content = case["calibration_response"]
    if not valid:
        content = content.replace(
            "version-71841d46af47ebc043156fad6820c826", "Example Gateway before 99.0"
        )
    requests = []

    def provider(request):
        payload = json.loads(request.content)
        requests.append(payload)
        assert str(request.url) == trial.ENDPOINT
        assert payload["provider"] == trial.POLICY
        assert payload["max_tokens"] == 32000
        assert payload["model"] == trial.MODEL_ID
        prompt = json.dumps(payload["messages"])
        assert case["articles"][0]["content"].split("\n")[0] in prompt
        assert "withheld" not in prompt
        assert "version 3.2 or earlier" not in prompt
        return reply(content)

    monkeypatch.chdir(tmp_path)
    Path("index.md").write_text("last-good report")
    receipt = asyncio.run(
        trial.run_trial(calibration, "test-secret", inner=httpx.MockTransport(provider))
    )
    assert receipt["result"]["outcome"] == (
        "validation_passed" if valid else "validation_failed"
    )
    assert receipt["live_attempted"] == len(requests) == 1
    if valid:
        assert "validation_diagnostic" not in receipt["result"]
    else:
        diagnostic = receipt["result"]["validation_diagnostic"]
        assert diagnostic["stage"] == "version_references"
        assert diagnostic["codes"] == ["invalid_version_reference"]
        assert diagnostic["field"] == "Affected Versions"
    assert "test-secret" not in json.dumps(receipt)
    assert content not in json.dumps(receipt)
    assert Path("index.md").read_text() == "last-good report"
    assert list(tmp_path.iterdir()) == [tmp_path / "index.md"]


@pytest.mark.parametrize("code", [401, 429, 500])
def test_provider_errors_consume_one_attempt_without_retry_or_raw_error(code):
    calibration = asyncio.run(trial.calibrate())
    calls = []

    def provider(request):
        calls.append(request)
        return httpx.Response(code, json={"error": {"message": "private marker"}})

    receipt = asyncio.run(
        trial.run_trial(calibration, "test-secret", inner=httpx.MockTransport(provider))
    )
    assert receipt["result"]["outcome"] == "analysis_failed"
    assert receipt["live_attempted"] == len(calls) == 1
    assert receipt["result"]["provider"]["http_status"] == code
    assert "private marker" not in json.dumps(receipt)


def test_valid_content_with_http_201_does_not_pass_trial():
    calibration = asyncio.run(trial.calibrate())
    content = trial.load_case()["calibration_response"]
    calls = []

    def provider(request):
        calls.append(request)
        return httpx.Response(201, json=reply(content).json())

    receipt = asyncio.run(
        trial.run_trial(calibration, "test-secret", inner=httpx.MockTransport(provider))
    )
    assert receipt["result"]["outcome"] == "verification_failed"
    assert receipt["result"]["provider"]["http_status"] == 201
    assert receipt["live_attempted"] == len(calls) == 1
    assert receipt["published"] is receipt["production_ready"] is False


def test_changed_prompt_is_refused_before_network():
    calibration = asyncio.run(trial.calibrate())
    calibration["request_sha256"] = "0" * 64
    calls = []
    receipt = asyncio.run(
        trial.run_trial(
            calibration,
            "test-secret",
            inner=httpx.MockTransport(lambda request: calls.append(request)),
        )
    )
    assert not calls
    assert receipt["live_attempted"] == 0
    assert receipt["result"]["outcome"] == "analysis_failed"


def test_fixture_and_tokenizer_tampering_fail_offline(tmp_path, monkeypatch):
    fixture = tmp_path / "case.json"
    fixture.write_text("{}")
    monkeypatch.setattr(trial, "CASE", fixture)
    with pytest.raises(ValueError, match="fixture"):
        trial.load_case()
    monkeypatch.setenv("TIKTOKEN_CACHE_DIR", str(tmp_path))
    with pytest.raises(FileNotFoundError):
        trial.require_tokenizer_cache()


@pytest.mark.parametrize(
    "change",
    [
        {"GITHUB_RUN_ATTEMPT": "2"},
        {"GITHUB_REF": "refs/heads/another"},
        {"GITHUB_EVENT_NAME": "push"},
        {"GITHUB_SHA": "b" * 40},
        {"GITHUB_REPOSITORY": "someone/else"},
    ],
)
def test_live_context_requires_exact_first_manual_main_attempt(
    change, tmp_path, monkeypatch
):
    commit = "a" * 40
    environment = {
        "GITHUB_REPOSITORY": "ricomanifesto/SentryInsight",
        "GITHUB_REF": "refs/heads/main",
        "GITHUB_SHA": commit,
        "GITHUB_EVENT_NAME": "workflow_dispatch",
        "GITHUB_RUN_ATTEMPT": "1",
        "RUNNER_TEMP": str(tmp_path),
    }
    for name, value in environment.items():
        monkeypatch.setenv(name, value)
    monkeypatch.setattr(
        trial.subprocess,
        "check_output",
        lambda args, **_: commit + "\n" if args[1] == "rev-parse" else "",
    )
    output = tmp_path / "nemotron-verification/live.json"
    trial.require_live_context(commit, output)
    for name, value in change.items():
        monkeypatch.setenv(name, value)
    with pytest.raises(ValueError, match="context"):
        trial.require_live_context(commit, output)


def test_canary_workflow_has_only_closed_manual_authority_and_proposed_next_day_scope():
    path = Path(".github/workflows/verify-nemotron.yml")
    workflow = yaml.load(path.read_text(), Loader=yaml.BaseLoader)
    assert set(workflow["on"]) == {"workflow_dispatch"}
    assert workflow["permissions"] == {"contents": "write"}
    job = workflow["jobs"]["canary"]
    assert "github.sha == inputs.expected_commit" in job["if"]
    assert "github.run_attempt == 1" in job["if"]
    assert "github.actor == 'ricomanifesto'" in job["if"]
    assert "github.ref == 'refs/heads/canary/sentry-full-feed-20261105'" in job["if"]
    steps = job["steps"]
    secret_steps = [step for step in steps if "secrets." in json.dumps(step)]
    assert len(secret_steps) == 1
    assert secret_steps[0]["id"] == "trial"
    assert "steps.gate.outputs.ready == 'true'" in secret_steps[0]["if"]
    assert "runner.debug != '1'" in secret_steps[0]["if"]
    assert (
        secret_steps[0]["env"]["OPENROUTER_API_KEY"]
        == "${{ secrets.OPENROUTER_API_KEY }}"
    )
    assert steps[-1]["with"]["retention-days"] == "7"
    assert steps[-1]["with"]["path"].endswith("sentry-canary-metadata.json")
    manifest = json.loads(Path("config/full-feed-canary.json").read_bytes())
    assert manifest["enabled"] is True
    assert manifest["execution_date"] == "2026-11-06"
    assert manifest["production_main"] == "5fc68212f1a9772ab56872ad20ad94ccc8322f3e"
    assert manifest["pilot"] == {
        "month": "2026-11",
        "activationStart": "2026-11-05T00:00:00.000Z",
        "opening": {
            "amountMicrousd": 0,
            "basisSha256": "f6f4a755142ca658dcc2d9abdf830a456515ffe51f51de9ee057b4862228f9c7",
        },
    }
    assert manifest["metadata_audience_approved"] is True
    assert (
        manifest["billing_basis"] == "verified_openrouter_credit_only"
        and manifest["data_approval_sha256"]
        == "fabfc6610161e7e92466f2e0ba59954517a1e7a23c00be26e7b44fa6b0c8f16e"
    )
    assert manifest["output_fate"] == "conditional_publish"
    assert (
        manifest["whole_hold_microusd"] == 7251456 and manifest["physical_limit"] == 1
    )
    assert (
        json.loads(Path("vercel.json").read_bytes())["git"]["deploymentEnabled"]
        is False
    )
    commands = "\n".join(step.get("run", "") for step in steps)
    assert "--execute-approved-canary" in commands and "--preflight-only" in commands
    assert "main.py" not in commands and "git push" not in commands


def test_unexpected_transport_endpoint_cannot_forward_a_credential():
    calls = []
    transport = trial.NvidiaBoundary(
        httpx.MockTransport(lambda request: calls.append(request))
    )
    request = httpx.Request("POST", "https://example.test/wrong", json={})
    with pytest.raises(ValueError, match="boundary"):
        asyncio.run(transport.handle_async_request(request))
    assert not calls


def test_initializer_workflow_is_separate_from_model_authority():
    workflow = yaml.load(
        Path(".github/workflows/verify-nemotron.yml").read_text(),
        Loader=yaml.BaseLoader,
    )
    option = workflow["on"]["workflow_dispatch"]["inputs"]["initialize_ledger"]
    assert option["type"] == "boolean" and option["default"] == "false"
    assert "!inputs.initialize_ledger" in workflow["jobs"]["canary"]["if"]
    job = workflow["jobs"]["initialize_ledger"]
    for guard in [
        "inputs.initialize_ledger",
        "github.sha == inputs.expected_commit",
        "github.run_attempt == 1",
        "github.actor == 'ricomanifesto'",
        "github.ref == 'refs/heads/canary/sentry-full-feed-20261105'",
    ]:
        assert guard in job["if"]
    assert workflow["permissions"] == {"contents": "write"}
    text = json.dumps(job)
    for forbidden in [
        "secrets.",
        "OPENROUTER_API_KEY",
        "upload-artifact",
        "setup-uv",
        "--execute-approved-canary",
    ]:
        assert forbidden not in text
    for step in job["steps"]:
        assert step["if"] == "runner.debug != '1'"
    checkout = job["steps"][0]
    assert checkout["with"]["ref"] == "${{ github.sha }}"
    assert checkout["with"]["persist-credentials"] == "true"
    command = "\n".join(step.get("run", "") for step in job["steps"])
    assert (
        "bootstrap_canary_ledger.cjs" in command
        and "--initialize-public-ledger" in command
    )
    assert "--expected-manifest" in command and "--expected-commit" in command


def test_request_policy_cannot_gain_paid_or_other_model_fallbacks():
    calls = []
    transport = trial.NvidiaBoundary(
        httpx.MockTransport(lambda request: calls.append(request))
    )
    payload = {
        "model": trial.MODEL_ID,
        "max_tokens": 32000,
        "provider": copy.deepcopy(trial.BASE_POLICY),
        "messages": [],
    }
    payload["provider"]["allow_fallbacks"] = True
    request = httpx.Request("POST", trial.ENDPOINT, json=payload)
    with pytest.raises(ValueError, match="policy"):
        asyncio.run(transport.handle_async_request(request))
    assert not calls

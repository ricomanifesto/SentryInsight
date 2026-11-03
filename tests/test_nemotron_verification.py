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


def test_workflow_has_no_automatic_trigger_or_publication_authority():
    path = Path(".github/workflows/verify-nemotron.yml")
    workflow = yaml.load(path.read_text(), Loader=yaml.BaseLoader)
    assert set(workflow["on"]) == {"workflow_dispatch"}
    assert workflow["permissions"] == {"contents": "read"}
    job = workflow["jobs"]["verify"]
    assert "github.sha == inputs.expected_commit" in job["if"]
    assert "github.run_attempt == 1" in job["if"]
    assert "github.ref == 'refs/heads/main'" in job["if"]
    steps = job["steps"]
    assert steps[0]["with"]["persist-credentials"] == "false"
    secret_steps = [step for step in steps if "secrets." in json.dumps(step)]
    assert len(secret_steps) == 1
    assert secret_steps[0]["id"] == "trial"
    assert (
        secret_steps[0]["env"]["OPENROUTER_API_KEY"]
        == "${{ secrets.OPENROUTER_API_KEY }}"
    )
    assert steps[-1]["with"]["retention-days"] == "7"
    commands = "\n".join(step.get("run", "") for step in steps)
    assert "publication/cli" not in commands
    assert "git push" not in commands
    assert "main.py" not in commands
    assert not any("publish-production" in step.get("uses", "") for step in steps)


def test_unexpected_transport_endpoint_cannot_forward_a_credential():
    calls = []
    transport = trial.NvidiaBoundary(
        httpx.MockTransport(lambda request: calls.append(request))
    )
    request = httpx.Request("POST", "https://example.test/wrong", json={})
    with pytest.raises(ValueError, match="boundary"):
        asyncio.run(transport.handle_async_request(request))
    assert not calls


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

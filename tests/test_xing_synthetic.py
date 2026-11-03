"""Offline provider/fixture/retention regressions; never a live-model test."""

import asyncio
from copy import deepcopy
import json
import socket

import httpx
import pytest

from evals.xing_synthetic import fixtures, policy, runner
from evals.xing_synthetic.__main__ import check_live_environment
from evals.xing_synthetic import __main__ as cli
from src.core.source_review import prepare_source_review
from src.core.version_references import build_version_reference_context

SECRET = "synthetic-unused-secret-for-test"
SHA = "a" * 40


class FixedBudget(policy.TokenBudget):
    def __init__(self, count=5000):
        self.value = count

    def count(self, messages):
        return self.value


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("Live network forbidden in synthetic evaluation tests")

    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket, "create_connection", denied)
    monkeypatch.delenv("SENTRYINSIGHT_MODEL", raising=False)


@pytest.fixture(scope="module")
def prepared():
    # Transport tests use a deterministic counter. The separately documented
    # calibration command verifies the real, pinned author tokenizer offline.
    return asyncio.run(fixtures.prepare_cases(FixedBudget()))


@pytest.fixture(scope="module")
def reports(prepared):
    return [fixtures.reference_report(case) for case in prepared]


def endpoints():
    row = {
        "model_id": policy.MODEL,
        "tag": "phala",
        "provider_name": "Phala",
        "status": 0,
        "context_length": policy.CONTEXT,
        "max_completion_tokens": 235929,
        "supported_parameters": ["max_tokens", "reasoning", "temperature"],
        "pricing": {"prompt": "0", "completion": "0", "discount": 0},
    }
    return {"data": {"id": policy.MODEL, "endpoints": [row]}}


def retention():
    return {
        "data": [
            {
                "model_id": policy.MODEL,
                "tag": "phala",
                "provider_name": "Phala",
                "safety_retention": False,
            }
        ]
    }


def response(text):
    return {
        "id": "gen-synthetic-test",
        "model": policy.MODEL,
        "provider": "Phala",
        "choices": [{"finish_reason": "stop", "message": {"content": text}}],
        "usage": {
            "prompt_tokens": 5000,
            "completion_tokens": 1000,
            "total_tokens": 6000,
            "cost": 0,
            "completion_tokens_details": {"reasoning_tokens": 100},
        },
    }


class Provider:
    def __init__(self, reports, mutate=None, status=200):
        self.reports = reports
        self.mutate = mutate
        self.status = status
        self.calls = []
        self.gets = []
        self.endpoint = endpoints()
        self.retained = retention()

    def handle(self, request):
        if request.method == "GET":
            assert "authorization" not in request.headers
            self.gets.append(str(request.url))
            if str(request.url) == policy.ENDPOINTS:
                return httpx.Response(200, json=self.endpoint)
            assert str(request.url) == policy.ZDR
            return httpx.Response(200, json=self.retained)
        assert request.method == "POST" and str(request.url) == policy.API
        assert request.headers["authorization"] == "Bearer " + SECRET
        payload = json.loads(request.content)
        policy.validate_payload(payload)
        assert payload["provider"] == policy.PROVIDER
        self.calls.append(payload)
        body = response(self.reports[len(self.calls) - 1])
        if self.mutate:
            body = self.mutate(body)
        return httpx.Response(
            self.status,
            content=json.dumps(body),
            headers={"Location": "https://example.invalid/forbidden"},
        )


def execute(prepared, provider, output, review=False):
    waits = []

    async def sleep(delay):
        waits.append(delay)

    result = asyncio.run(
        runner.run_cases(
            prepared,
            secret=SECRET,
            output=output,
            candidate_sha=SHA,
            review_outputs=review,
            transport=httpx.MockTransport(provider.handle),
            sleep=sleep,
            clock=lambda: 100,
        )
    )
    return result, waits


def test_all_six_calibration_reports_pass_shared_gate_and_gold(prepared, reports):
    for case, raw in zip(prepared, reports, strict=True):
        _, checks = fixtures.evaluate(case, raw)
        assert all(checks.values()), case.name


def test_six_calls_are_sequential_bounded_private_by_default(
    prepared, reports, tmp_path, capsys
):
    public = {
        name: b"last-good"
        for name in ["index.md", "index.html", "current-findings.json"]
    }
    for name, body in public.items():
        (tmp_path / name).write_bytes(body)
    provider = Provider(reports)
    out = tmp_path / "pilot"
    result, waits = execute(prepared, provider, out)
    assert result["complete"] and result["attempted"] == result["automated_passes"] == 6
    assert len(provider.calls) == 6 and waits == [60] * 5
    assert len(provider.gets) == 12
    assert (
        result["human_review"] == "not_performed"
        and result["production_ready"] is False
    )
    assert sorted(str(p.relative_to(out)) for p in out.rglob("*") if p.is_file()) == [
        "metadata/receipt.json"
    ]
    data = (out / "metadata/receipt.json").read_text()
    assert SECRET not in data and all(raw not in data for raw in reports)
    assert "# Exploitation Report" not in data
    assert capsys.readouterr().out == ""
    assert all((tmp_path / name).read_bytes() == body for name, body in public.items())


def test_explicit_synthetic_review_is_separate_and_never_marks_human_pass(
    prepared, reports, tmp_path
):
    result, _ = execute(prepared, Provider(reports), tmp_path / "review", review=True)
    paths = sorted((tmp_path / "review/synthetic-review").glob("*.txt"))
    assert len(paths) == 6
    assert result["synthetic_review_outputs"] is True
    assert result["human_review"] == "not_performed"
    for case, raw in zip(prepared, reports, strict=True):
        path = tmp_path / "review/synthetic-review" / (case.name + ".txt")
        assert path.read_text() == raw and path.stat().st_mode & 0o777 == 0o600


@pytest.mark.parametrize("status", [301, 307, 401, 402, 429, 500, 503])
def test_http_failure_never_retries_or_leaks_body(prepared, reports, tmp_path, status):
    provider = Provider(reports, mutate=lambda _: {"error": SECRET}, status=status)
    result, _ = execute(prepared, provider, tmp_path / "out", review=True)
    assert result["attempted"] == len(provider.calls) == 1
    assert not result["complete"] and result["automated_passes"] == 0
    assert result["trials"][0]["http_status"] == status
    assert all(r["outcome"] == "not_attempted" for r in result["trials"][1:])
    assert SECRET not in json.dumps(result)
    assert not (tmp_path / "out/synthetic-review").exists()


@pytest.mark.parametrize(
    "change,code",
    [
        (lambda r: r.update(provider="Unknown " + SECRET), "provider_mismatch"),
        (lambda r: r.update(model="paid/model"), "model_mismatch"),
        (
            lambda r: r["choices"][0].update(finish_reason="length"),
            "incomplete_completion",
        ),
        (lambda r: r["usage"].update(cost=0.01), "unexpected_cost"),
        (lambda r: r["usage"].update(prompt_tokens=200001), "provider_input_budget"),
        (
            lambda r: r["usage"].update(completion_tokens=32001),
            "provider_output_budget",
        ),
        (lambda r: r["usage"].update(cost=float("nan")), "invalid_usage"),
        (
            lambda r: r["choices"][0]["message"].update(content=SECRET),
            "invalid_completion",
        ),
    ],
)
def test_response_policy_failures_stop_with_safe_usage(
    prepared, reports, tmp_path, change, code
):
    def mutate(body):
        change(body)
        return body

    provider = Provider(reports, mutate=mutate)
    result, _ = execute(prepared, provider, tmp_path / "out", review=True)
    trial = result["trials"][0]
    assert trial["code"] == code and len(provider.calls) == 1
    assert SECRET not in json.dumps(result)
    if code == "unexpected_cost":
        assert trial["usage"]["cost"] == 0.01
    if code == "incomplete_completion":
        assert trial["usage"]["completion_tokens"] == 1000


@pytest.mark.parametrize(
    "change",
    [
        lambda p: p.retained["data"][0].update(safety_retention=True),
        lambda p: p.retained["data"][0].pop("safety_retention"),
        lambda p: p.endpoint["data"]["endpoints"][0]["pricing"].update(prompt="0.001"),
        lambda p: p.endpoint["data"]["endpoints"][0]["pricing"].pop("completion"),
        lambda p: p.endpoint["data"]["endpoints"][0].update(status=-5),
        lambda p: p.endpoint["data"]["endpoints"][0].update(context_length=100000),
        lambda p: p.endpoint["data"]["endpoints"][0].update(supported_parameters=[]),
        lambda p: p.endpoint["data"].update(id="other/model:free"),
    ],
)
def test_policy_changes_fail_before_any_model_request(
    prepared, reports, tmp_path, change
):
    provider = Provider(reports)
    change(provider)
    result, _ = execute(prepared, provider, tmp_path / "out")
    assert result["attempted"] == len(provider.calls) == 0
    assert result["trials"][0]["code"] == "endpoint_policy"


def test_mutated_request_cannot_introduce_paid_model_or_fallback(
    prepared, reports, tmp_path
):
    altered = deepcopy(prepared)
    altered[0].payload["provider"]["allow_fallbacks"] = True
    result, _ = execute(altered, Provider(reports), tmp_path / "out")
    assert result["attempted"] == 0 and result["trials"][0]["code"] == "request_policy"


def test_mutated_message_is_rejected_by_prepared_request_identity(
    prepared, reports, tmp_path
):
    altered = deepcopy(prepared)
    altered[0].payload["messages"][1]["content"] += "unreviewed input"
    result, _ = execute(altered, Provider(reports), tmp_path / "out")
    assert (
        result["attempted"] == 0 and result["trials"][0]["code"] == "request_identity"
    )


def test_transport_exception_is_sanitized_and_not_retried(prepared, reports, tmp_path):
    p = Provider(reports)
    original = p.handle

    def transport(req):
        if req.method == "POST":
            p.calls.append({})
            raise httpx.ReadTimeout(SECRET)
        return original(req)

    p.handle = transport
    result, _ = execute(prepared, p, tmp_path / "out")
    assert result["attempted"] == len(p.calls) == 1
    assert SECRET not in json.dumps(result)


def test_maximum_plan_and_existing_output_cannot_be_reused(prepared, reports, tmp_path):
    with pytest.raises(policy.PilotError, match="invalid_run_plan"):
        execute([*prepared, prepared[0]], Provider(reports), tmp_path / "seven")
    output = tmp_path / "existing"
    output.mkdir()
    with pytest.raises(FileExistsError):
        execute(prepared, Provider(reports), output)


def test_model_output_cannot_forge_coverage_or_omit_a_constraint(prepared, reports):
    c = prepared[0]
    plan = prepare_source_review(c.articles)
    scope = build_version_reference_context(plan.eligible_catalog)[0]
    assert len(scope["constraints"]) == 2
    omitted = reports[0].replace("; " + scope["constraints"][1]["id"], "")
    if omitted == reports[0]:
        omitted = reports[0].replace(scope["constraints"][1]["id"] + "; ", "")
    assert omitted != reports[0]
    with pytest.raises(ValueError):
        fixtures.evaluate(c, omitted)
    held_key = next(
        r["key"]
        for r in prepared[3].analysis["source_review_plan"]["sources"]
        if r["state"] != "eligible"
    )
    allowed_key = next(
        r["key"]
        for r in prepared[3].analysis["source_review_plan"]["sources"]
        if r["state"] == "eligible"
    )
    with pytest.raises(ValueError):
        fixtures.evaluate(prepared[3], reports[3].replace(allowed_key, held_key))


def test_fixture_bytes_are_closed_to_unreviewed_real_content(tmp_path, monkeypatch):
    for name in ["sources.json", "answers.json"]:
        (tmp_path / name).write_bytes((fixtures.ROOT / name).read_bytes())
    source = tmp_path / "sources.json"
    source.write_text(
        source.read_text().replace("example.invalid", "real-site.example")
    )
    monkeypatch.setattr(fixtures, "ROOT", tmp_path)
    with pytest.raises(policy.PilotError, match="fixture_identity"):
        fixtures.load_fixtures()


def test_input_budget_and_tokenizer_identity_fail_closed(tmp_path):
    messages = [
        {"role": "system", "content": "Synthetic instruction"},
        {"role": "user", "content": "Synthetic source"},
    ]
    assert policy.payload_for(messages, FixedBudget(200000))["max_tokens"] == 32000
    with pytest.raises(policy.PilotError, match="input_budget"):
        policy.payload_for(messages, FixedBudget(200001))
    data = tmp_path / "bad.model"
    data.write_bytes(b"not the pinned public tokenizer")
    with pytest.raises(policy.PilotError, match="tokenizer_identity"):
        policy.TokenBudget(data)


@pytest.mark.parametrize(
    "field,value",
    [
        ("GITHUB_ACTIONS", "false"),
        ("GITHUB_EVENT_NAME", "push"),
        ("GITHUB_REF", "refs/heads/other"),
        ("GITHUB_RUN_ATTEMPT", "2"),
        ("GITHUB_REPOSITORY", "someone/else"),
    ],
)
def test_live_environment_rejects_other_events_refs_and_reruns(
    monkeypatch, tmp_path, field, value
):
    for key, item in {
        "GITHUB_ACTIONS": "true",
        "GITHUB_EVENT_NAME": "workflow_dispatch",
        "GITHUB_REF": "refs/heads/main",
        "GITHUB_RUN_ATTEMPT": "1",
        "GITHUB_REPOSITORY": "ricomanifesto/SentryInsight",
    }.items():
        monkeypatch.setenv(key, item)
    monkeypatch.setenv(field, value)
    with pytest.raises(policy.PilotError, match="execution_context"):
        check_live_environment(SHA, tmp_path / "out")


def configure_live_guard(monkeypatch, tmp_path):
    for key, value in {
        "GITHUB_ACTIONS": "true",
        "GITHUB_EVENT_NAME": "workflow_dispatch",
        "GITHUB_REF": "refs/heads/main",
        "GITHUB_RUN_ATTEMPT": "1",
        "GITHUB_REPOSITORY": "ricomanifesto/SentryInsight",
        "RUNNER_TEMP": str(tmp_path),
    }.items():
        monkeypatch.setenv(key, value)
    monkeypatch.setattr(
        cli.subprocess,
        "check_output",
        lambda args, **kwargs: SHA if args[1] == "rev-parse" else "",
    )


@pytest.mark.parametrize(
    "condition,code",
    [
        ("wrong_sha", "candidate_identity"),
        ("dirty", "candidate_identity"),
        ("outside_temp", "output_location"),
        ("production", "production_output_location"),
        ("override", "model_override"),
    ],
)
def test_live_guard_requires_exact_clean_commit_and_disposable_output(
    monkeypatch, tmp_path, condition, code
):
    configure_live_guard(monkeypatch, tmp_path)
    output = tmp_path / "out"
    if condition == "wrong_sha":
        monkeypatch.setattr(cli.subprocess, "check_output", lambda *a, **kw: "b" * 40)
    elif condition == "dirty":
        monkeypatch.setattr(cli.subprocess, "check_output", lambda *a, **kw: SHA)
    elif condition == "outside_temp":
        output = tmp_path.parent / "outside"
    elif condition == "production":
        monkeypatch.setattr(cli, "REPO", tmp_path)
    elif condition == "override":
        monkeypatch.setenv("SENTRYINSIGHT_MODEL", "paid/model")
    with pytest.raises(policy.PilotError, match=code):
        check_live_environment(SHA, output)


def test_absent_usage_is_unknown_instead_of_zero():
    data = response("synthetic answer")
    del data["usage"]
    _, metadata = policy.completion(data, SECRET)
    assert all(value is None for value in metadata["usage"].values())


def test_oversized_body_is_never_retained_or_retried(prepared, reports, tmp_path):
    provider = Provider(
        reports, mutate=lambda r: {**r, "extra": "x" * policy.MAX_RESPONSE_BYTES}
    )
    result, _ = execute(prepared, provider, tmp_path / "out", review=True)
    assert len(provider.calls) == 1
    assert result["trials"][0]["code"] == "response_size"
    assert not (tmp_path / "out" / "synthetic-review").exists()


def test_total_deadline_stops_without_another_attempt(
    prepared, reports, tmp_path, monkeypatch
):
    real = runner.bounded_json

    async def expired(client, method, url, **kwargs):
        if method == "POST":
            raise TimeoutError("untrusted transport " + SECRET)
        return await real(client, method, url, **kwargs)

    monkeypatch.setattr(runner, "bounded_json", expired)
    result, _ = execute(prepared, Provider(reports), tmp_path / "out")
    assert result["attempted"] == 1
    assert result["trials"][0]["outcome"] == "failed"
    assert all(t["outcome"] == "not_attempted" for t in result["trials"][1:])
    assert SECRET not in json.dumps(result)

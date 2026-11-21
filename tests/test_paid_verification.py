"""One explicit paid run: read-only preflight, durable reserve, no paid probes."""

import asyncio
import hashlib
import json
from pathlib import Path
import subprocess
from datetime import datetime

import httpx
import pytest

from src.core import paid_verification as paid
from src.core.attempt_budget import AttemptBudgetError

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def setup(monkeypatch, tmp_path):
    exported = json.loads(
        subprocess.check_output(
            [
                "node",
                "-e",
                "const p=require('./publication/kit/verification-budget');"
                "console.log(JSON.stringify({profile:p.PROFILE,sha256:p.PROFILE_SHA256}))",
            ],
            cwd=ROOT,
            text=True,
        )
    )
    evidence = dict(
        billing="credits-no-applicable-byok",
        coverage="all-applicable-ci-keys",
        periodStart=exported["profile"]["periodStart"],
        periodEnd=exported["profile"]["periodEnd"],
        actualMicrousd=1400000,
        checkedAt="2026-11-17T16:00:00.000Z",
        scopeSha256=hashlib.sha256(b"workspace:test-workspace").hexdigest(),
        keySha256=hashlib.sha256(b"test-only-key").hexdigest(),
    )
    proof = tmp_path / "billing.json"
    proof.write_text(json.dumps(evidence))
    env = {
        "SENTRYINSIGHT_PAID_VERIFICATION": paid.PROFILE_ID,
        "SENTRYINSIGHT_BILLING_EVIDENCE": str(proof),
        "GITHUB_EVENT_NAME": "workflow_dispatch",
        "GITHUB_REF": "refs/heads/main",
        "GITHUB_RUN_ID": "100",
        "GITHUB_RUN_ATTEMPT": "1",
        "SENTRYINSIGHT_SOURCE_REVISION": "a" * 40,
        "SENTRYINSIGHT_ADMISSION_KEY": "run:100",
        "SENTRYINSIGHT_ATTEMPT_STORE": "admission",
        "SENTRYINSIGHT_FAILURE_RECEIPT": str(tmp_path / "failure.json"),
        "OPENROUTER_API_KEY": "test-only-key",
        "SENTRYINSIGHT_MODEL": "openrouter/nvidia/nemotron-3.5-super-vl:free",
    }
    for key, value in env.items():
        monkeypatch.setenv(key, value)
    monkeypatch.setattr(paid, "_current", None)
    clock = [datetime.fromisoformat("2026-11-17T16:10:00+00:00").timestamp() * 1000]
    monkeypatch.setattr(paid, "_now_ms", lambda: clock[0], raising=False)
    config = json.loads((ROOT / "config/config.json").read_text())
    calls = []

    class Bridge:
        def __init__(self):
            from src.core.attempt_budget import MemoryAttemptBudget

            self.memory = MemoryAttemptBudget()

        async def reserve(self, request_sha256, limit):
            calls.append(("report-attempt", limit))
            return await self.memory.reserve(request_sha256, limit)

        async def finish(self, reservation, disposition, **kwargs):
            await self.memory.finish(reservation, disposition, **kwargs)

        def _invoke(self, command, arguments):
            calls.append((command, arguments))
            if command == "verification-profile":
                return exported
            if command == "verification-reserve":
                return dict(
                    reservedMicrousd=7956100,
                    profileSha256=exported["sha256"],
                    validUntil=1794934800000,
                )
            if command == "verification-triage":
                return {"claimed": True}
            if command == "verification-report":
                return {"verified": True}
            raise AssertionError(command)

    def handler(request):
        assert request.method == "GET", "Preflight must never send inference"
        calls.append((request.url.path, None))
        if request.url.path.endswith("/key"):
            assert request.headers["authorization"] == "Bearer test-only-key"
            return httpx.Response(
                200,
                json={
                    "data": {
                        "workspace_id": "test-workspace",
                        "byok_usage_monthly": 0,
                        "usage_monthly": 0.252,
                    }
                },
            )
        assert "authorization" not in request.headers
        report = "moonshotai/kimi-k3.1-pro" in request.url.path
        p = exported["profile"]
        return httpx.Response(
            200,
            json={
                "data": {
                    "id": p["model"] if report else p["triageModel"],
                    "endpoints": [
                        {
                            "tag": p["provider"] if report else p["triageProvider"],
                            "context_length": (
                                p["reportContext"] if report else p["triageContext"]
                            ),
                            "max_completion_tokens": 32000 if report else 235929,
                            "pricing": {
                                "prompt": "0.000002" if report else "0.000000042",
                                "completion": "0.00001" if report else "0",
                            },
                        }
                    ],
                }
            },
        )

    return (
        config,
        Bridge(),
        httpx.MockTransport(handler),
        calls,
        exported,
        evidence,
        proof,
        clock,
    )


def initialize(setup, **kwargs):
    config, bridge, transport, *_ = setup
    transport = kwargs.pop("transport", transport)
    return asyncio.run(
        paid.initialize_verification(
            config, bridge=bridge, transport=transport, **kwargs
        )
    )


def test_disabled_profile_never_reads_metadata_or_reserves(monkeypatch):
    monkeypatch.delenv("SENTRYINSIGHT_PAID_VERIFICATION", raising=False)
    assert asyncio.run(paid.initialize_verification({})) is None
    assert paid.active_verification() is None


def test_readonly_identity_and_metadata_precede_one_durable_reservation(
    setup, monkeypatch
):
    monkeypatch.setenv(
        "SENTRYINSIGHT_MODEL", "openrouter/nvidia/nemotron-3.5-super-vl:free"
    )
    before = json.loads(json.dumps(setup[0]))
    verification = initialize(setup)
    assert setup[0] == before
    assert setup[3][-1][0] == "verification-reserve"
    assert len([x for x in setup[3] if x[0].startswith("/api/")]) == 3
    assert paid.active_verification() is verification
    import os

    assert os.environ["SENTRYINSIGHT_MODEL"] == "openrouter/moonshotai/kimi-k3.1-pro"
    assert setup[0]["analysis"]["model"].endswith(":free")


@pytest.mark.parametrize(
    "key,value",
    [
        ("SENTRYINSIGHT_PAID_VERIFICATION", "other"),
        ("GITHUB_EVENT_NAME", "schedule"),
        ("GITHUB_REF", "refs/heads/other"),
        ("GITHUB_RUN_ATTEMPT", "2"),
        ("OPENROUTER_API_KEY", ""),
        ("SENTRYINSIGHT_BILLING_EVIDENCE", ""),
        ("SENTRYINSIGHT_ATTEMPT_STORE", ""),
    ],
)
def test_invalid_activation_fails_before_read_or_reserve(
    setup, monkeypatch, key, value
):
    monkeypatch.setenv(key, value)
    with pytest.raises(paid.PaidVerificationError):
        initialize(setup)
    assert setup[3] == []


def test_flag_alone_cannot_construct_a_client_or_reuse_an_unprepared_run(setup):
    with pytest.raises(paid.PaidVerificationError):
        paid.active_verification()
    from src.core.model_client import build_model_client

    with pytest.raises(paid.PaidVerificationError):
        build_model_client(timeout=30, max_tokens=32000)


@pytest.mark.parametrize(
    "data",
    [
        {"workspace_id": "other", "byok_usage_monthly": 0},
        {"workspace_id": "test-workspace", "byok_usage_monthly": 1},
        {"workspace_id": "test-workspace"},
        {},
    ],
)
def test_actual_ci_key_must_match_checked_workspace_and_credit_billing(setup, data):
    original = setup[2]

    def handler(request):
        if request.url.path.endswith("/key"):
            return httpx.Response(200, json={"data": data})
        return original.handler(request)

    with pytest.raises(paid.PaidVerificationError):
        initialize(setup, transport=httpx.MockTransport(handler))
    assert not any(x[0] == "verification-reserve" for x in setup[3])


@pytest.mark.parametrize(
    "change", ["price", "context", "missing_provider", "missing_price", "request_fee"]
)
def test_changed_or_unpriced_metadata_never_reserves_or_sends(setup, change):
    original = setup[2]

    def handler(request):
        response = original.handler(request)
        if request.url.path.endswith("/key"):
            return response
        data = response.json()
        endpoint = data["data"]["endpoints"][0]
        if change == "price":
            endpoint["pricing"]["prompt"] = "1"
        if change == "context":
            endpoint["context_length"] = 2000000
        if change == "missing_provider":
            endpoint["tag"] = "other"
        if change == "missing_price":
            endpoint["pricing"].pop("prompt")
        if change == "request_fee":
            endpoint["pricing"]["request"] = "1"
        return httpx.Response(200, json=data)

    with pytest.raises(paid.PaidVerificationError):
        initialize(setup, transport=httpx.MockTransport(handler))
    assert not any(x[0] == "verification-reserve" for x in setup[3])


def test_provider_policy_is_fixed_for_both_operations(setup):
    v = initialize(setup)
    for operation, provider, prompt, completion in [
        ("report", "moonshotai/mxfp4", "2", "10"),
        ("triage", "typesafe", "0.042", "0"),
    ]:
        assert v.provider_policy(operation) == {
            "only": [provider],
            "order": [provider],
            "allow_fallbacks": False,
            "require_parameters": True,
            "max_price": {"prompt": prompt, "completion": completion, "request": "0"},
        }


def test_reserved_profile_cannot_change_after_preflight(setup):
    verification = initialize(setup)
    with pytest.raises(TypeError):
        verification.profile["reportOutput"] = 100000


def test_budget_acknowledgement_failure_cannot_activate(setup):
    def fail(command, arguments):
        raise AttemptBudgetError()

    setup[1]._invoke = fail
    with pytest.raises(paid.PaidVerificationError):
        initialize(setup)
    with pytest.raises(paid.PaidVerificationError):
        paid.active_verification()


def test_report_client_pins_provider_and_checks_durable_reservation_before_send(setup):
    v = initialize(setup)
    from src.core.openrouter_client import OpenRouterClient
    from src.core.opencode_client import parse_model_selection

    def handler(request):
        assert setup[3][-2][0] == "verification-report"
        assert setup[3][-1] == ("report-attempt", 3)
        payload = json.loads(request.content)
        assert payload["provider"] == v.provider_policy("report")
        assert payload["model"] == v.profile["model"]
        return httpx.Response(
            200,
            json={
                "model": v.profile["model"],
                "choices": [{"message": {"content": "done"}, "finish_reason": "stop"}],
            },
        )

    client = OpenRouterClient(
        api_key="test-only-key",
        max_tokens=32000,
        transport=httpx.MockTransport(handler),
    )
    assert client.attempt_budget is v.bridge
    assert (
        asyncio.run(
            client.generate(
                system_prompt="s",
                user_prompt="u",
                model=parse_model_selection("openrouter/" + v.profile["model"]),
            )
        )
        == "done"
    )


@pytest.mark.parametrize(
    "model,tokens",
    [
        ("openrouter/nvidia/nemotron-3.5-super-vl:free", 32000),
        ("openrouter/moonshotai/kimi-k3.1-pro", 32001),
    ],
)
def test_paid_report_model_or_output_drift_never_sends(setup, model, tokens):
    initialize(setup)
    from src.core.openrouter_client import OpenRouterClient
    from src.core.opencode_client import parse_model_selection

    def handler(_request):
        raise AssertionError("Forbidden send")

    client = OpenRouterClient(
        api_key="test-only-key",
        max_tokens=tokens,
        transport=httpx.MockTransport(handler),
    )
    with pytest.raises(paid.PaidVerificationError):
        asyncio.run(
            client.generate(
                system_prompt="s", user_prompt="u", model=parse_model_selection(model)
            )
        )


def test_both_clients_reject_a_different_key_from_the_verified_workspace(setup):
    initialize(setup)
    from src.core.openrouter_client import OpenRouterClient
    from src.core.exploitation_decisions import DecisionClient

    with pytest.raises(paid.PaidVerificationError):
        OpenRouterClient(api_key="different-dummy", max_tokens=32000)
    with pytest.raises(paid.PaidVerificationError):
        DecisionClient(api_key="different-dummy", timeout=5)


def test_triage_claim_precedes_pinned_request_and_budget_errors_never_fallback(setup):
    v = initialize(setup)
    from src.core.exploitation_decisions import DecisionClient
    from src.core.exploitation_triage import triage_articles

    def handler(request):
        assert setup[3][-1][0] == "verification-triage"
        assert json.loads(request.content)["provider"] == v.provider_policy("triage")
        return httpx.Response(503)

    # A provider error retains legacy full-source behavior, within the existing reservation.
    from src.core.exploitation_decisions import DecisionError

    with pytest.raises(DecisionError):
        asyncio.run(
            DecisionClient(
                api_key="test-only-key",
                timeout=5,
                transport=httpx.MockTransport(handler),
            ).classify([{"title": "one", "content": "x"}])
        )

    def fail(command, arguments):
        raise AttemptBudgetError()

    setup[1]._invoke = fail
    with pytest.raises(paid.PaidVerificationError):
        asyncio.run(
            triage_articles(
                [{"title": "one", "content": "x"}],
                setup[0],
                client_factory=lambda settings: DecisionClient(
                    api_key="test-only-key",
                    timeout=settings.timeout_seconds,
                    transport=httpx.MockTransport(handler),
                ),
                estimator=lambda items: 0,
            )
        )


def test_workflow_initializes_paid_budget_before_graph_or_triage():
    source = (ROOT / "src/core/workflow.py").read_text()
    body = source[source.index("async def run_exploitation_analysis") :]
    assert body.index("await initialize_verification(config)") < body.index(
        "graph.ainvoke"
    )


def test_paid_workflow_option_routes_only_to_the_readiness_job():
    """The manual paid option no longer reaches the whole-run verification."""
    source = (ROOT / ".github/workflows/generate-report.yml").read_text()
    assert "paid_verification:" in source and "billing_evidence:" in source
    # The hosted legacy generator, its admission and its push are held.
    assert "      - name: Admit generation" not in source
    assert "uv run python main.py" not in source
    assert "SENTRYINSIGHT_PAID_VERIFICATION" not in source
    assert paid.PROFILE_ID not in source
    assert "SENTRYINSIGHT_PAID_READINESS: kimi-moonshot-readiness-20261121" in source


@pytest.mark.parametrize("mode", ["ordinary", "verified", "blocked"])
def test_verified_paid_intent_exercises_unchanged_eligible_plan_only(
    setup, monkeypatch, tmp_path, mode
):
    initialize(setup)
    if mode == "ordinary":
        monkeypatch.delenv(paid.FLAG)
    from test_workflow_guards import import_workflow_with_stubs
    from src.core.source_review import prepare_source_review, digest
    from src.core.content_fingerprint import write_stored_fingerprint
    from unittest.mock import AsyncMock

    workflow = import_workflow_with_stubs()
    monkeypatch.setattr(
        workflow,
        "run_triage",
        AsyncMock(side_effect=lambda items, config: (items, None)),
    )
    content = (
        "An attack vector targets instances running version 3.2 or earlier."
        if mode == "blocked"
        else "An advisory."
    )
    articles = [
        dict(
            title="Same advisory",
            source="Example",
            content=content,
            link="https://example.test/advisory",
        )
    ]
    plan = prepare_source_review(articles)
    assert bool(plan.eligible_keys) == (mode != "blocked")
    fingerprint = digest({"generation_schema": 5, "plan_id": plan.packet["plan_id"]})
    path = tmp_path / ".sentryinsight-articles-fingerprint"
    write_stored_fingerprint(fingerprint, str(path))
    config = json.loads(json.dumps(setup[0]))
    config["analysis"]["grounding"] = "strict"
    config["output_path"] = str(tmp_path / "index.md")
    state = dict(articles=articles, config=config, status="started")
    result = asyncio.run(workflow.filter_articles(state))
    expected = {
        "ordinary": "completed_unchanged",
        "verified": "started",
        "blocked": "review_required",
    }[mode]
    assert result["status"] == expected
    assert result["articles_fingerprint"] == fingerprint
    assert path.read_text().strip() == fingerprint


def test_expiry_during_report_reservation_stops_the_post_and_keeps_claim(setup):
    verification = initialize(setup)
    clock = setup[7]
    original = verification.bridge.reserve

    async def delayed(*args):
        reserved = await original(*args)
        clock[0] = (
            datetime.fromisoformat("2026-11-17T17:00:00+00:00").timestamp() * 1000
        )
        return reserved

    verification.bridge.reserve = delayed
    from src.core.openrouter_client import OpenRouterClient
    from src.core.opencode_client import parse_model_selection

    sent = []

    def handler(request):
        sent.append(request)
        return httpx.Response(
            200,
            json={
                "model": verification.profile["model"],
                "choices": [{"message": {"content": "done"}, "finish_reason": "stop"}],
            },
        )

    client = OpenRouterClient(
        api_key="test-only-key",
        max_tokens=32000,
        transport=httpx.MockTransport(handler),
    )
    with pytest.raises(paid.PaidVerificationError):
        asyncio.run(
            client.generate(
                system_prompt="s",
                user_prompt="u",
                model=parse_model_selection(
                    "openrouter/" + verification.profile["model"]
                ),
            )
        )
    assert sent == []
    assert verification.bridge.memory.disposition in {"reserved", "uncertain"}


def test_expiry_during_triage_claim_stops_the_post(setup):
    verification = initialize(setup)
    original = verification.bridge._invoke

    def delayed(command, arguments):
        result = original(command, arguments)
        if command == "verification-triage":
            setup[7][0] = (
                datetime.fromisoformat("2026-11-17T17:00:00+00:00").timestamp() * 1000
            )
        return result

    verification.bridge._invoke = delayed
    from src.core.exploitation_decisions import DecisionClient, RELEVANT, LABELS

    sent = []

    def handler(request):
        sent.append(request)
        return httpx.Response(
            200,
            json={
                "model": "typesafe/jev-1.13",
                "answers": {
                    "article_0": {
                        "type": "choice",
                        "choice": RELEVANT,
                        "probabilities": {
                            label: int(label == RELEVANT) for label in LABELS
                        },
                        "confidence": 1,
                    }
                },
            },
        )

    with pytest.raises(paid.PaidVerificationError):
        asyncio.run(
            DecisionClient(
                api_key="test-only-key",
                timeout=5,
                transport=httpx.MockTransport(handler),
            ).classify([{"title": "one", "content": "x"}])
        )
    assert sent == []


@pytest.mark.parametrize(
    "event,ref,attempt,requested,head,fact,surface,allowed",
    [
        (
            "workflow_dispatch",
            "refs/heads/main",
            "1",
            "false",
            "a" * 40,
            "b" * 64,
            "",
            True,
        ),
        (
            "workflow_dispatch",
            "refs/heads/main",
            "1",
            "false",
            "a" * 40,
            "b" * 64,
            "c" * 64,
            True,
        ),
        ("schedule", "refs/heads/main", "1", "false", "a" * 40, "b" * 64, "", False),
        (
            "workflow_dispatch",
            "refs/heads/other",
            "1",
            "false",
            "a" * 40,
            "b" * 64,
            "",
            False,
        ),
        (
            "workflow_dispatch",
            "refs/heads/main",
            "2",
            "false",
            "a" * 40,
            "b" * 64,
            "",
            False,
        ),
        (
            "workflow_dispatch",
            "refs/heads/main",
            "1",
            "true",
            "a" * 40,
            "b" * 64,
            "",
            False,
        ),
        (
            "workflow_dispatch",
            "refs/heads/main",
            "1",
            "false",
            "d" * 40,
            "b" * 64,
            "",
            False,
        ),
        ("workflow_dispatch", "refs/heads/main", "1", "false", "", "b" * 64, "", False),
        ("workflow_dispatch", "refs/heads/main", "1", "false", "a" * 40, "", "", False),
        (
            "workflow_dispatch",
            "refs/heads/main",
            "1",
            "false",
            "a" * 40,
            "b" * 64,
            "x",
            False,
        ),
    ],
)
def test_actual_paid_readiness_shell_guard_admits_only_the_exact_first_attempt(
    event, ref, attempt, requested, head, fact, surface, allowed
):
    source = (ROOT / ".github/workflows/generate-report.yml").read_text()
    job = source[source.index("  paid-readiness:") :]
    start = job.index('          if [ "$GITHUB_EVENT_NAME" != "workflow_dispatch" ]')
    finish = job.index("      - name: Checkout the exact dispatched head", start)
    script = "\n".join(
        line[10:]
        for line in job[start:finish].splitlines()
        if not line.lstrip().startswith("#")
    )
    result = subprocess.run(
        ["bash", "-c", script],
        env={
            "PATH": "/usr/bin:/bin",
            "GITHUB_EVENT_NAME": event,
            "GITHUB_REF": ref,
            "GITHUB_RUN_ATTEMPT": attempt,
            "GITHUB_SHA": "a" * 40,
            "READMIT": requested,
            "EXPECTED_HEAD": head,
            "FACT_MANIFEST_SHA256": fact,
            "SURFACE_APPROVAL_SHA256": surface,
        },
        capture_output=True,
        text=True,
    )
    assert (result.returncode == 0) is allowed

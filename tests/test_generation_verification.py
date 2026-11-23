"""Real prompt/resolver verification with an offline transport and no publication."""

import asyncio
import json
from pathlib import Path

import httpx
import pytest

from scripts.verify_report_generation import (
    MODEL_ID,
    VerificationClient,
    verify_articles,
)
from src.core.openrouter_client import OpenRouterClient, OpenRouterError
from src.core.opencode_client import parse_model_selection
from src.core.public_site import accepted_origins
from src.core import reviewed_report
from src.core.report_artifact import parse_report_artifact
from src.core.reviewed_report import resolve_reviewed_analysis
from test_reviewed_report import prepared_result
from test_source_review import AMBIGUOUS
from test_version_references import source


def articles():
    return [source("A service advisory.", "good"), source(AMBIGUOUS, "held")]


def response(content, **overrides):
    return httpx.Response(
        200,
        json={
            "model": MODEL_ID,
            "choices": [{"finish_reason": "stop", "message": {"content": content}}],
            "usage": {"prompt_tokens": 100, "completion_tokens": 200, "cost": 0},
            **overrides,
        },
    )


def test_offline_preflight_and_all_held_do_not_contact_a_provider():
    calls = []
    client = VerificationClient(
        "synthetic-key", httpx.MockTransport(lambda request: calls.append(request))
    )
    dry = asyncio.run(verify_articles(articles()))
    assert dry["outcome"] == "preflight_only"
    assert dry["attempted"] == 0
    held = asyncio.run(verify_articles([source(AMBIGUOUS, "held")], client=client))
    assert held["outcome"] == "review_required"
    assert held["attempted"] == 0
    assert not calls


@pytest.mark.parametrize("valid", [True, False])
def test_verification_uses_actual_guards_and_never_writes_a_report(
    valid, tmp_path, monkeypatch
):
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("SENTRYINSIGHT_MODEL", raising=False)
    last_good = tmp_path / "index.md"
    last_good.write_bytes(b"last-good sentinel")
    content = prepared_result(articles())["exploitation_report"]
    if not valid:
        content = content.replace(
            "Not stated in supplied sources.", "Gateway before 99.0"
        )
    requests = []

    def provider(request):
        payload = json.loads(request.content)
        requests.append(payload)
        assert payload["model"] == MODEL_ID
        assert payload["max_tokens"] == 32000
        assert payload["provider"] == {
            "allow_fallbacks": False,
            "max_price": {"prompt": 0, "completion": 0, "request": 0, "image": 0},
        }
        assert "https://example.test/held" not in payload["messages"][1]["content"]
        return response(content)

    client = VerificationClient("synthetic-key", httpx.MockTransport(provider))
    receipt = asyncio.run(verify_articles(articles(), client=client))
    assert receipt["outcome"] == ("validation_passed" if valid else "validation_failed")
    assert len(requests) == receipt["attempted"] == 1
    assert receipt["published"] is receipt["production_ready"] is False
    assert content not in json.dumps(receipt)
    assert last_good.read_bytes() == b"last-good sentinel"
    assert list(tmp_path.iterdir()) == [last_good]
    assert client.last_generation == {
        "requested_model": MODEL_ID,
        "resolved_model": MODEL_ID,
    }


def test_verification_does_not_retry_a_transient_error_or_allow_a_second_call():
    requests = []

    def provider(request):
        requests.append(request)
        return httpx.Response(429)

    client = VerificationClient("synthetic-key", httpx.MockTransport(provider))
    kwargs = {
        "system_prompt": "synthetic",
        "user_prompt": "synthetic",
        "model": parse_model_selection("openrouter/" + MODEL_ID),
    }
    with pytest.raises(OpenRouterError):
        asyncio.run(client.generate(**kwargs))
    with pytest.raises(OpenRouterError):
        asyncio.run(client.generate(**kwargs))
    assert len(requests) == 1


@pytest.mark.parametrize("resolved", [None, "another/model", 1, {"text": "private"}])
def test_wrong_or_missing_model_identity_fails_without_retry(resolved, caplog):
    requests = []

    def provider(request):
        requests.append(request)
        return response("private answer", model=resolved)

    client = OpenRouterClient(
        api_key="synthetic-key", transport=httpx.MockTransport(provider)
    )
    with pytest.raises(OpenRouterError, match="resolved model"):
        asyncio.run(
            client.generate(
                system_prompt="synthetic",
                user_prompt="synthetic",
                model=parse_model_selection("openrouter/" + MODEL_ID),
            )
        )
    assert len(requests) == 1
    assert client.last_generation is None
    assert "private answer" not in caplog.text


@pytest.mark.parametrize("attempts", [0, 4, True, 1.5])
def test_attempt_bound_cannot_expand_the_production_allowance(attempts):
    with pytest.raises(ValueError):
        OpenRouterClient(api_key="synthetic-key", max_attempts=attempts)


@pytest.mark.parametrize("origin", accepted_origins("SentryDigest"))
def test_reviewed_report_emits_current_origin_and_accepts_historical_origin(
    origin, monkeypatch
):
    monkeypatch.setattr(reviewed_report, "DIGEST_ARCHIVE_ROOT", origin + "archive/")
    candidate = resolve_reviewed_analysis(prepared_result())
    current = origin + "archive/2026-11-02/"
    assert parse_report_artifact(candidate.source).digest_issue_url == current
    historical = candidate.source.replace(
        current, "https://ricomanifesto.github.io/SentryDigest/archive/2026-11-02/"
    )
    assert parse_report_artifact(historical).source_coverage == candidate.coverage


def test_merged_workflow_retains_both_admission_and_review_publication_gates():
    workflow = Path(".github/workflows/generate-report.yml").read_text()
    publish = workflow.split("- name: Commit and push updated report", 1)[1].split(
        "run: |", 1
    )[0]
    for required in (
        "steps.admission.outputs.decision == 'admitted'",
        "steps.generate.outputs.report_generated == 'true'",
        "steps.source-review-summary.outcome == 'success'",
        "github.ref == 'refs/heads/main'",
    ):
        assert required in publish
    assert "node publication/cli.js complete" in workflow
    assert "uses: ./.github/workflows/publish-production.yml" in workflow

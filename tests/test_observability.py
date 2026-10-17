import asyncio
import json
import types
from pathlib import Path
from unittest.mock import AsyncMock

import httpx
import logfire
import pytest
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.trace import StatusCode

from src.core import workflow
from src.core.model_config import DEFAULT_MODEL
from src.core import analyze, observability
from src.core.analysis_errors import ANALYSIS_ERROR_CLASSES, classify_analysis_error
from src.core.observability import (
    ci_attributes,
    logfire_options,
    model_attributes,
    state_attributes,
    traced_stage,
)
from src.core.openrouter_client import (
    OpenRouterClient,
    OpenRouterError,
    OpenRouterUnavailable,
)
from src.core.report_validation import ReportValidationIssue

ARTICLE_TEXT = "SECRET_ARTICLE_BODY"
ARTICLE_TITLE = "SECRET_ARTICLE_TITLE"
MODEL_PROSE = "SECRET_MODEL_PROSE"
VALIDATION_MESSAGE = "SECRET_VALIDATION_MESSAGE"
CREDENTIAL = "sk-or-SECRET_CREDENTIAL"
PROVIDER_MESSAGE = "SECRET_PROVIDER_MESSAGE"
REPO_ROOT = Path(__file__).resolve().parents[1]


def exported(capfire):
    return capfire.exporter.exported_spans_as_dict(parse_json_attributes=True)


def spans_by_name(capfire):
    return {span["name"]: span for span in exported(capfire)}


def assert_no_content(capfire):
    payload = json.dumps(exported(capfire))
    for value in (ARTICLE_TEXT, ARTICLE_TITLE, MODEL_PROSE, VALIDATION_MESSAGE):
        assert value not in payload


def report_state(report):
    return {
        "status": "started",
        "articles": [{"title": ARTICLE_TITLE, "content": ARTICLE_TEXT}],
        "filtered_articles": [{"title": ARTICLE_TITLE, "content": ARTICLE_TEXT}],
        "config": {"output_path": "index.md"},
        "analysis_results": {
            "exploitation_report": report,
            "reporting_sources": [],
            "cves_identified": ["CVE-2026-0001", "CVE-2026-0002"],
            "analyzed_article_count": 1,
        },
    }


def test_stage_span_records_bounded_state_attributes(capfire):
    async def stage(state):
        state["filtered_articles"] = state["articles"][:1]
        return state

    state = {
        "status": "started",
        "articles": [
            {"title": ARTICLE_TITLE, "content": ARTICLE_TEXT},
            {"title": "Other", "content": ARTICLE_TEXT},
        ],
        "filtered_articles": [],
        "analysis_results": {},
        "config": {},
    }

    asyncio.run(traced_stage("filter", stage)(state))

    [span] = exported(capfire)
    assert span["name"] == "sentryinsight.filter"
    attributes = span["attributes"]
    assert attributes["stage"] == "filter"
    assert attributes["workflow.status"] == "started"
    assert attributes["articles.count"] == 2
    assert attributes["filtered_articles.count"] == 1
    assert "analysis.outcome" not in attributes
    assert_no_content(capfire)


def test_grounding_failure_records_stage_and_code(capfire):
    report = f"# Exploitation Report\n\n## Executive Summary\n\n{MODEL_PROSE}\n"

    result = asyncio.run(
        traced_stage("generate", workflow.generate_report)(report_state(report))
    )

    assert result["status"] == "failed"
    assert result["failure"] == {
        "stage": "reporting_identity",
        "codes": ["reporting_identity_rejected"],
        "field": None,
    }
    attributes = spans_by_name(capfire)["sentryinsight.generate"]["attributes"]
    assert attributes["failure.stage"] == "reporting_identity"
    assert attributes["failure.codes"] == ["reporting_identity_rejected"]
    assert "failure.field" not in attributes
    assert attributes["analysis.outcome"] == "analyzed"
    assert attributes["analysis.article_count"] == 1
    assert attributes["analysis.cve_count"] == 2
    assert_no_content(capfire)


def test_virtual_event_failure_records_policy_code(capfire):
    report = f"# Exploitation Report\n\n[Virtual Event] {MODEL_PROSE}\n"

    result = asyncio.run(
        traced_stage("generate", workflow.generate_report)(report_state(report))
    )

    assert result["failure"]["codes"] == ["virtual_event_promotion"]
    attributes = spans_by_name(capfire)["sentryinsight.generate"]["attributes"]
    assert attributes["failure.stage"] == "report_policy"
    assert_no_content(capfire)


def test_validation_failure_records_unique_issue_codes(capfire, monkeypatch):
    monkeypatch.setattr(workflow, "deserialize_reporting_catalog", lambda _rows: {})
    monkeypatch.setattr(workflow, "validate_finding_evidence", lambda *_args: None)
    monkeypatch.setattr(
        workflow, "resolve_reporting_keys", lambda report, _catalog: report
    )
    monkeypatch.setattr(
        workflow,
        "validate_report_content",
        lambda *_args, **_kwargs: [
            ReportValidationIssue("error_marker", VALIDATION_MESSAGE),
            ReportValidationIssue("active_content", VALIDATION_MESSAGE),
            ReportValidationIssue("error_marker", VALIDATION_MESSAGE),
        ],
    )
    report = f"# Exploitation Report\n\n{MODEL_PROSE}\n"

    result = asyncio.run(
        traced_stage("generate", workflow.generate_report)(report_state(report))
    )

    assert result["report_validation_errors"][0] == VALIDATION_MESSAGE
    attributes = spans_by_name(capfire)["sentryinsight.generate"]["attributes"]
    assert attributes["failure.stage"] == "report_validation"
    assert attributes["failure.codes"] == ["error_marker", "active_content"]
    assert_no_content(capfire)


def test_missing_feed_url_records_fetch_failure(capfire):
    state = {
        "status": "started",
        "articles": [],
        "filtered_articles": [],
        "analysis_results": {},
        "config": {},
    }

    result = asyncio.run(traced_stage("fetch", workflow.fetch_articles)(state))

    assert result["status"] == "failed"
    attributes = spans_by_name(capfire)["sentryinsight.fetch"]["attributes"]
    assert attributes["failure.stage"] == "fetch"
    assert attributes["failure.codes"] == ["feed_url_missing"]


def test_run_nests_stage_spans_under_one_root(capfire, monkeypatch, tmp_path):
    monkeypatch.delenv("SENTRYINSIGHT_MODEL", raising=False)
    monkeypatch.setattr(
        workflow,
        "load_config",
        lambda: {"feed_url": "test", "output_path": str(tmp_path / "index.md")},
    )
    monkeypatch.setattr(
        workflow,
        "SentryDigestFeedClient",
        lambda *_args: types.SimpleNamespace(
            fetch_articles=AsyncMock(return_value=[]),
            enrich_article_content=AsyncMock(return_value=[]),
        ),
    )

    result = asyncio.run(workflow.run_exploitation_analysis())

    assert result["status"] == "completed_with_warnings"
    spans = spans_by_name(capfire)
    root = spans["sentryinsight.run"]
    assert root["parent"] is None
    assert root["attributes"]["model.id"] == DEFAULT_MODEL
    assert root["attributes"]["workflow.status"] == "completed_with_warnings"
    assert root["attributes"]["articles.count"] == 0
    stages = [
        "sentryinsight.fetch",
        "sentryinsight.enrich",
        "sentryinsight.filter",
        "sentryinsight.generate",
        "sentryinsight.publish",
    ]
    for name in stages:
        assert spans[name]["parent"]["span_id"] == root["context"]["span_id"]
    assert "sentryinsight.analyze" not in spans


def test_handled_analysis_error_records_failure_code(capfire, monkeypatch):
    async def failed_analysis(_articles, _config):
        return {"error": MODEL_PROSE, "exploitation_report": MODEL_PROSE}

    monkeypatch.setattr(workflow, "analyze_exploitation", failed_analysis)
    state = report_state("")

    result = asyncio.run(traced_stage("analyze", workflow.analyze_articles)(state))

    assert result["status"] == "failed"
    attributes = spans_by_name(capfire)["sentryinsight.analyze"]["attributes"]
    assert attributes["analysis.outcome"] == "error"
    assert attributes["failure.stage"] == "analysis"
    assert attributes["failure.codes"] == ["analysis_failed"]
    assert_no_content(capfire)


def test_missing_configuration_still_records_a_run_span(capfire, monkeypatch):
    monkeypatch.setattr(workflow, "load_config", lambda: {})

    assert asyncio.run(workflow.run_exploitation_analysis()) is None

    root = spans_by_name(capfire)["sentryinsight.run"]
    assert root["attributes"]["workflow.status"] == "failed"
    assert root["attributes"]["failure.stage"] == "config"
    assert root["attributes"]["failure.codes"] == ["config_unavailable"]


def test_graph_exception_marks_the_run_span_with_its_type(capfire, monkeypatch):
    class BrokenGraph:
        async def ainvoke(self, _state):
            raise RuntimeError(f"Illegal header value b'Bearer {CREDENTIAL}'")

    monkeypatch.setattr(workflow, "load_config", lambda: {"feed_url": "test"})
    monkeypatch.setattr(workflow, "create_exploitation_analysis_graph", BrokenGraph)

    assert asyncio.run(workflow.run_exploitation_analysis()) is None

    root = spans_by_name(capfire)["sentryinsight.run"]
    assert root["attributes"]["workflow.status"] == "failed"
    assert root["attributes"]["error.type"] == "RuntimeError"
    assert root["attributes"]["logfire.level_num"] == 17
    assert CREDENTIAL not in json.dumps(exported(capfire))


@pytest.mark.parametrize("model", ["Not A Model", "openrouter/" + ARTICLE_TITLE])
def test_invalid_model_identifier_is_not_recorded(model, monkeypatch):
    monkeypatch.setenv("SENTRYINSIGHT_MODEL", model)

    assert model_attributes({}) == {"model.id_valid": "false"}


@pytest.fixture
def production_capfire(capfire):
    """Capture spans with the entrypoint's own Logfire options."""
    options = {**logfire_options(), "send_to_logfire": False}
    logfire.configure(
        **options, additional_span_processors=[SimpleSpanProcessor(capfire.exporter)]
    )
    return capfire


def test_escaping_exception_records_only_its_type(production_capfire):
    async def stage(_state):
        raise RuntimeError(f"Illegal header value b'Bearer {CREDENTIAL}'")

    with pytest.raises(RuntimeError, match="Illegal header value"):
        asyncio.run(traced_stage("enrich", stage)({"status": "started"}))

    [span] = [
        span
        for span in production_capfire.exporter.exported_spans
        if span.attributes.get("logfire.span_type") == "span"
    ]
    assert span.attributes["error.type"] == "RuntimeError"
    assert span.status.status_code is StatusCode.ERROR
    assert span.status.description == "RuntimeError"
    assert not [event for event in span.events if event.name == "exception"]
    assert CREDENTIAL not in json.dumps(exported(production_capfire))
    assert CREDENTIAL not in str(span.status.description)


def test_handled_exception_logging_records_only_its_type(production_capfire):
    with logfire.span("handled"):
        try:
            raise ValueError(CREDENTIAL)
        except ValueError:
            logfire.exception("handled failure")

    payload = json.dumps(exported(production_capfire))
    assert CREDENTIAL not in payload
    assert '"error.type": "ValueError"' in payload


@pytest.mark.parametrize("value", [None, "", "   "])
def test_export_is_disabled_without_an_environment_token(value, monkeypatch):
    if value is None:
        monkeypatch.delenv("LOGFIRE_TOKEN", raising=False)
    else:
        monkeypatch.setenv("LOGFIRE_TOKEN", value)

    options = logfire_options()

    # False also stops Logfire from reading a token saved under .logfire.
    assert options["send_to_logfire"] is False
    assert options["token"] is None


@pytest.mark.parametrize("token", [None, ""])
def test_logfire_stays_unconfigured_without_a_token(token, monkeypatch):
    calls = []
    if token is None:
        monkeypatch.delenv("LOGFIRE_TOKEN", raising=False)
    else:
        monkeypatch.setenv("LOGFIRE_TOKEN", token)
    # Logfire adds an OTLP exporter for these regardless of send_to_logfire.
    monkeypatch.setenv("OTEL_EXPORTER_OTLP_ENDPOINT", "https://collector.example")
    monkeypatch.setattr(
        observability.logfire, "configure", lambda **kw: calls.append(kw)
    )

    observability.configure_observability()

    assert calls == []


def test_logfire_is_configured_with_the_environment_token(monkeypatch):
    calls = []
    monkeypatch.setenv("LOGFIRE_TOKEN", "pylf_v1_us_example")
    monkeypatch.setattr(
        observability.logfire, "configure", lambda **kw: calls.append(kw)
    )

    observability.configure_observability()

    [options] = calls
    assert options["token"] == "pylf_v1_us_example"
    assert options["send_to_logfire"] is True


def test_export_uses_only_the_environment_token(monkeypatch):
    monkeypatch.setenv("LOGFIRE_TOKEN", " pylf_v1_us_example ")

    options = logfire_options()

    assert options["send_to_logfire"] is True
    assert options["token"] == "pylf_v1_us_example"


def test_logfire_token_reaches_only_the_generation_step():
    workflow_file = REPO_ROOT / ".github" / "workflows" / "generate-report.yml"
    header, *steps = workflow_file.read_text().split("\n      - name: ")

    assert "LOGFIRE_TOKEN" not in header
    holders = [step.splitlines()[0] for step in steps if "LOGFIRE_TOKEN" in step]
    assert holders == ["Generate exploitation report"]


@pytest.mark.parametrize(
    ("error", "error_class"),
    [
        (
            OpenRouterError("x", http_status=200, provider_code=503),
            "model_provider_unavailable",
        ),
        (
            OpenRouterError("x", http_status=200, provider_code=504),
            "model_provider_unavailable",
        ),
        (OpenRouterError("x", http_status=502), "model_provider_unavailable"),
        (OpenRouterError("x", http_status=529), "model_provider_unavailable"),
        (OpenRouterError("x", http_status=429), "model_rate_limited"),
        (
            OpenRouterError("x", http_status=200, provider_code=429),
            "model_rate_limited",
        ),
        (OpenRouterError("x", http_status=401), "model_auth_rejected"),
        (OpenRouterError("x", http_status=403), "model_auth_rejected"),
        (
            OpenRouterError("x", http_status=503, provider_code=400),
            "model_request_failed",
        ),
        (OpenRouterError("x", http_status=400), "model_request_failed"),
        (OpenRouterError("x"), "model_request_failed"),
        (OpenRouterUnavailable("x", retryable=True), "model_request_failed"),
        (ValueError("x"), "analysis_exception"),
    ],
)
def test_analysis_errors_map_to_the_fixed_vocabulary(error, error_class):
    assert classify_analysis_error(error)[0] == error_class
    assert error_class in ANALYSIS_ERROR_CLASSES


def test_error_detail_keeps_integers_only():
    error = OpenRouterError("x", http_status=200, provider_code=503)
    error.attempts = 3
    assert classify_analysis_error(error)[1] == {
        "http_status": 200,
        "provider_code": 503,
        "attempts": 3,
    }

    malformed = OpenRouterError("x", http_status="503", provider_code=True)  # type: ignore[arg-type]
    malformed.attempts = None
    assert classify_analysis_error(malformed)[1] == {}

    attributes = state_attributes(
        {
            "analysis_results": {
                "error": PROVIDER_MESSAGE,
                "error_class": PROVIDER_MESSAGE,
                "error_detail": {
                    "http_status": "200",
                    "provider_code": True,
                    "attempts": 3,
                },
            }
        }
    )
    assert "analysis.error_class" not in attributes
    assert "model.http_status" not in attributes
    assert "model.provider_code" not in attributes
    assert attributes["model.attempts"] == 3

    unexpected = state_attributes(
        {
            "analysis_results": {
                "error": "x",
                "error_class": ["x"],
                "error_detail": [503],
            }
        }
    )
    assert "analysis.error_class" not in unexpected
    assert not [key for key in unexpected if key.startswith("model.")]


def test_provider_failure_records_bounded_detail_without_its_message(
    capfire, monkeypatch
):
    monkeypatch.setattr(asyncio, "sleep", AsyncMock())
    requests = []

    def provider(request):
        requests.append(request)
        return httpx.Response(
            200,
            json={
                "error": {
                    "code": 503,
                    "message": PROVIDER_MESSAGE,
                    "metadata": {"raw": PROVIDER_MESSAGE},
                }
            },
        )

    client = OpenRouterClient(
        api_key=CREDENTIAL, transport=httpx.MockTransport(provider)
    )

    async def analysis(_articles, config):
        return await analyze.analyze_exploitation([], config, model_client=client)

    monkeypatch.setattr(workflow, "analyze_exploitation", analysis)
    monkeypatch.delenv("SENTRYINSIGHT_MODEL", raising=False)
    state = report_state("")
    state["config"] = {"analysis": {"model": DEFAULT_MODEL}}

    result = asyncio.run(traced_stage("analyze", workflow.analyze_articles)(state))

    assert len(requests) == 3
    assert result["status"] == "failed"
    assert result["analysis_results"]["error_class"] == "model_provider_unavailable"
    attributes = spans_by_name(capfire)["sentryinsight.analyze"]["attributes"]
    assert attributes["analysis.error_class"] == "model_provider_unavailable"
    assert attributes["model.http_status"] == 200
    assert attributes["model.provider_code"] == 503
    assert attributes["model.attempts"] == 3
    assert attributes["failure.codes"] == [
        "analysis_failed",
        "model_provider_unavailable",
    ]
    payload = json.dumps(exported(capfire))
    assert PROVIDER_MESSAGE not in payload
    assert CREDENTIAL not in payload
    assert_no_content(capfire)


def test_input_budget_failure_records_its_class(capfire, monkeypatch):
    async def over_budget(_articles, _config):
        return {
            "error": MODEL_PROSE,
            "error_class": "input_budget_exceeded",
            "error_detail": {},
            "exploitation_report": "",
        }

    monkeypatch.setattr(workflow, "analyze_exploitation", over_budget)

    asyncio.run(traced_stage("analyze", workflow.analyze_articles)(report_state("")))

    attributes = spans_by_name(capfire)["sentryinsight.analyze"]["attributes"]
    assert attributes["failure.codes"] == ["analysis_failed", "input_budget_exceeded"]
    assert "model.http_status" not in attributes
    assert_no_content(capfire)


def test_ci_attributes_require_well_formed_values():
    assert ci_attributes(
        {
            "GITHUB_RUN_ID": "18712345678",
            "GITHUB_RUN_ATTEMPT": "2",
            "GITHUB_EVENT_NAME": "repository_dispatch",
        }
    ) == {
        "ci.run_id": 18712345678,
        "ci.run_attempt": 2,
        "ci.event": "repository_dispatch",
    }
    assert ci_attributes({}) == {}
    assert (
        ci_attributes(
            {
                "GITHUB_RUN_ID": "12; " + ARTICLE_TITLE,
                "GITHUB_RUN_ATTEMPT": "",
                "GITHUB_EVENT_NAME": "Schedule " + ARTICLE_TITLE,
            }
        )
        == {}
    )


def test_run_span_records_ci_identity_from_the_environment(capfire, monkeypatch):
    monkeypatch.setenv("GITHUB_RUN_ID", "18712345678")
    monkeypatch.setenv("GITHUB_RUN_ATTEMPT", "1")
    monkeypatch.setenv("GITHUB_EVENT_NAME", "schedule")
    monkeypatch.setattr(workflow, "load_config", lambda: {})

    asyncio.run(workflow.run_exploitation_analysis())

    attributes = spans_by_name(capfire)["sentryinsight.run"]["attributes"]
    assert attributes["ci.run_id"] == 18712345678
    assert attributes["ci.run_attempt"] == 1
    assert attributes["ci.event"] == "schedule"


def test_service_version_is_the_commit_in_the_generation_step_only():
    workflow_file = REPO_ROOT / ".github" / "workflows" / "generate-report.yml"
    header, *steps = workflow_file.read_text().split("\n      - name: ")

    assert "LOGFIRE_SERVICE_VERSION" not in header
    holders = [step for step in steps if "LOGFIRE_SERVICE_VERSION" in step]
    assert [step.splitlines()[0] for step in holders] == [
        "Generate exploitation report"
    ]
    assert "LOGFIRE_SERVICE_VERSION: ${{ github.sha }}" in holders[0]

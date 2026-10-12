import asyncio
import json
import types
from pathlib import Path
from unittest.mock import AsyncMock

import logfire
import pytest
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.trace import StatusCode

from src.core import workflow
from src.core.model_config import DEFAULT_MODEL
from src.core.observability import logfire_options, model_attributes, traced_stage
from src.core.report_validation import ReportValidationIssue

ARTICLE_TEXT = "SECRET_ARTICLE_BODY"
ARTICLE_TITLE = "SECRET_ARTICLE_TITLE"
MODEL_PROSE = "SECRET_MODEL_PROSE"
VALIDATION_MESSAGE = "SECRET_VALIDATION_MESSAGE"
CREDENTIAL = "sk-or-SECRET_CREDENTIAL"
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

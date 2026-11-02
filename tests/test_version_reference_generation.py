import asyncio
import json
from unittest.mock import AsyncMock

import pytest

from src.core.finding_evidence import ABSENT, EvidenceError
from src.core.reporting import build_reporting_catalog, serialize_reporting_catalog
from src.core.version_references import PROTOCOL_KEY, PROTOCOL_VERSION
from test_analyze_guards import import_analyze_with_stubs
from test_version_references import CVE, contract, report, source
from test_workflow_guards import import_workflow_with_stubs


def analysis(catalog, value):
    return {
        PROTOCOL_KEY: PROTOCOL_VERSION,
        "exploitation_report": report(catalog, value),
        "reporting_sources": serialize_reporting_catalog(catalog),
    }


def test_analysis_supplies_source_owned_contract_and_host_protocol(monkeypatch):
    analyze = import_analyze_with_stubs()
    content = (
        f"{CVE} is actively exploited.\n\nAffected versions: Gateway 2.3 (Windows only)"
    )
    article = source(content)
    catalog = build_reporting_catalog([article])
    reference = contract(catalog)["constraints"][0]["id"]
    client = type(
        "Client", (), {"generate": AsyncMock(return_value=report(catalog, reference))}
    )()
    result = asyncio.run(
        analyze.analyze_exploitation([article], {}, model_client=client)
    )
    prompt = client.generate.call_args.kwargs["user_prompt"]
    context = json.loads(
        prompt.split("BEGIN AFFECTED VERSION REFERENCES\n", 1)[1].split(
            "\nEND AFFECTED VERSION REFERENCES", 1
        )[0]
    )
    assert contract(catalog) in context
    assert content in prompt
    assert "Do not output free-text version claims" in prompt
    assert result[PROTOCOL_KEY] == PROTOCOL_VERSION
    assert result["exploitation_report"] == report(catalog, reference)
    assert client.generate.await_count == 1


def test_workflow_resolves_before_unchanged_grounding_and_report_checks(
    monkeypatch, tmp_path
):
    workflow = import_workflow_with_stubs()
    catalog = build_reporting_catalog(
        [
            source(
                f"{CVE} is actively exploited.\n\nAffected versions: Gateway 2.3 (Windows only)"
            )
        ]
    )
    reference = contract(catalog)["constraints"][0]["id"]
    seen = []

    class ReachedReportValidation(Exception):
        pass

    def inspect(candidate, **_):
        seen.append(candidate)
        raise ReachedReportValidation

    monkeypatch.setattr(workflow, "validate_report_content", inspect)
    with pytest.raises(ReachedReportValidation):
        asyncio.run(
            workflow.generate_report(
                {
                    "analysis_results": analysis(catalog, reference),
                    "config": {"output_path": str(tmp_path / "index.md")},
                    "status": "started",
                }
            )
        )
    assert "**Affected Versions**: Gateway 2.3 (Windows only)" in seen[0]
    assert reference not in seen[0]
    assert "https://example.test/one" in seen[0]
    assert not list(tmp_path.iterdir())


@pytest.mark.parametrize("value", ["Gateway before 9.0", "version-" + "a" * 32])
def test_reference_failures_preserve_last_good_and_bounded_diagnostics(
    value, tmp_path, caplog
):
    workflow = import_workflow_with_stubs()
    catalog = build_reporting_catalog(
        [source(f"{CVE} is actively exploited.\n\nPRIVATE-SYNTHETIC-CONTENT")]
    )
    paths = [tmp_path / "index.md", tmp_path / ".sentryinsight-articles-fingerprint"]
    for path in paths:
        path.write_text("last good")
    with caplog.at_level("ERROR", logger="src.core.workflow"):
        result = asyncio.run(
            workflow.generate_report(
                {
                    "analysis_results": analysis(catalog, value),
                    "config": {"output_path": str(paths[0])},
                    "status": "started",
                }
            )
        )
    assert result["status"] == "failed"
    assert all(path.read_text() == "last good" for path in paths)
    diagnostic = json.loads(
        next(
            record.getMessage().split("Report grounding failed: ", 1)[1]
            for record in caplog.records
            if record.getMessage().startswith("Report grounding failed: ")
        )
    )
    assert diagnostic["code"] in {
        "invalid_version_reference",
        "unsupported_version_reference",
    }
    assert diagnostic["finding_index"] == 1
    assert diagnostic["cves"] == [CVE]
    assert value not in caplog.text
    assert "PRIVATE-SYNTHETIC-CONTENT" not in caplog.text


@pytest.mark.parametrize("protocol", [False, 2, "1"])
def test_invalid_host_protocol_cannot_fall_back_to_free_text(protocol, tmp_path):
    workflow = import_workflow_with_stubs()
    catalog = build_reporting_catalog([source(f"{CVE} is actively exploited.")])
    result = asyncio.run(
        workflow.generate_report(
            {
                "analysis_results": {
                    **analysis(catalog, ABSENT),
                    PROTOCOL_KEY: protocol,
                },
                "config": {"output_path": str(tmp_path / "index.md")},
                "status": "started",
            }
        )
    )
    assert result["status"] == "failed"
    assert result["report_validation_errors"] == ["Missing version reference protocol"]
    assert not list(tmp_path.iterdir())


@pytest.mark.parametrize("valid", [True, False])
def test_eval_adapter_uses_the_same_reference_resolution_offline(
    monkeypatch, tmp_path, valid
):
    from evals.grounding import model_task
    from evals.grounding.dataset import Article, TaskInput

    monkeypatch.setenv("OPENROUTER_API_KEY", "synthetic-unused-key")
    monkeypatch.delenv("SENTRYINSIGHT_MODEL", raising=False)
    article = source(
        f"{CVE} is actively exploited.\n\nAffected versions: Gateway 2.3 (Windows only)"
    )
    catalog = build_reporting_catalog([article])
    reference = contract(catalog)["constraints"][0]["id"]
    monkeypatch.setattr(
        model_task,
        "analyze_exploitation",
        AsyncMock(
            return_value=analysis(catalog, reference if valid else "Gateway before 9.0")
        ),
    )
    task = model_task.ModelTask(
        model="openrouter/example/model:free",
        receipts=tmp_path / "synthetic-receipts.jsonl",
        max_requests=1,
    )
    inputs = TaskInput(
        name="synthetic-protocol",
        articles=[Article(**article, source_links=[])],
        variant="baseline",
    )
    if valid:
        result = asyncio.run(task(inputs))
        assert "**Affected Versions**: Gateway 2.3 (Windows only)" in result
        assert reference not in result
    else:
        with pytest.raises(EvidenceError, match="references"):
            asyncio.run(task(inputs))
    assert task.requests == 1
    receipt = (tmp_path / "synthetic-receipts.jsonl").read_text()
    assert reference not in receipt and "Gateway before 9.0" not in receipt


@pytest.mark.parametrize("outcome", ["success", "protocol", "promotion"])
def test_adapters_prepare_identical_raw_reports_before_resolving(
    monkeypatch, tmp_path, outcome
):
    from evals.grounding import model_task
    from evals.grounding.dataset import Article, TaskInput
    from src.core.finding_evidence import validate_finding_evidence
    from src.core.report_validation import (
        ReportPreparationError,
        remove_source_attribution_section,
        split_overlong_executive_summary,
    )

    monkeypatch.setenv("OPENROUTER_API_KEY", "synthetic-unused-key")
    monkeypatch.delenv("SENTRYINSIGHT_MODEL", raising=False)
    article = source(f"{CVE} is actively exploited.\n\nAffected versions: Gateway 2.3")
    catalog = build_reporting_catalog([article])
    reference = contract(catalog)["constraints"][0]["id"]
    summary = " ".join(
        ["Defenders should review the available source evidence carefully."] * 8
    )
    raw = f"# Exploitation Report\n\n## Executive Summary\n\n{summary}\n\n" + report(
        catalog, reference
    )
    raw += f"\n## Source Attribution\n\nSelected reference: {reference}\n"
    if outcome == "promotion":
        raw += "[Virtual Event] A promotion must remain blocked before removal.\n"
    elif outcome == "protocol":
        raw = raw.replace(
            f"**Affected Versions**: {reference}",
            "**Affected Versions**: Gateway before 9.0",
        )
    result = {**analysis(catalog, reference), "exploitation_report": raw}
    expected = split_overlong_executive_summary(
        remove_source_attribution_section(raw)
    ).replace(reference, "Gateway 2.3")
    assert "## Source Attribution" not in expected
    monkeypatch.setattr(
        model_task, "analyze_exploitation", AsyncMock(return_value=result)
    )
    task = model_task.ModelTask(
        model="openrouter/example/model:free",
        receipts=tmp_path / "synthetic-receipts.jsonl",
        max_requests=1,
    )
    inputs = TaskInput(
        name="synthetic-preparation",
        articles=[Article(**article, source_links=[])],
        variant="baseline",
    )

    workflow = import_workflow_with_stubs()
    seen = []

    class ReachedGrounding(Exception):
        pass

    def inspect(candidate, sources):
        validate_finding_evidence(candidate, sources)
        seen.append(candidate)
        raise ReachedGrounding

    monkeypatch.setattr(workflow, "validate_finding_evidence", inspect)
    output = tmp_path / "index.md"
    output.write_text("last good")
    state = {
        "analysis_results": result,
        "config": {"output_path": str(output)},
        "status": "started",
    }
    if outcome == "promotion":
        production = asyncio.run(workflow.generate_report(state))
        assert production["failure"]["codes"] == ["virtual_event_promotion"]
        with pytest.raises(ReportPreparationError, match=r"blocked \[Virtual Event\]"):
            asyncio.run(task(inputs))
        assert seen == []
    elif outcome == "protocol":
        production = asyncio.run(workflow.generate_report(state))
        assert production["failure"]["codes"] == ["invalid_version_reference"]
        with pytest.raises(EvidenceError) as caught:
            asyncio.run(task(inputs))
        assert caught.value.code == "invalid_version_reference"
        assert seen == []
    else:
        with pytest.raises(ReachedGrounding):
            asyncio.run(workflow.generate_report(state))
        evaluation = asyncio.run(task(inputs))
        assert seen == [evaluation] == [expected]
    assert output.read_text() == "last good"
    assert task.requests == 1

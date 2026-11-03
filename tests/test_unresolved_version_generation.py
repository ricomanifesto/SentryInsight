"""Synthetic production/evaluation parity and last-good publication guards."""

import asyncio
import json
from unittest.mock import AsyncMock

import pytest

from src.core.finding_evidence import ABSENT, EvidenceError
from src.core.reporting import (
    build_reporting_catalog,
    serialize_reporting_catalog,
)
from src.core.version_references import PROTOCOL_KEY, PROTOCOL_VERSION
from test_unresolved_versions import (
    NARRATIVE,
    raw_report,
    unresolved_refs,
    artifact_text,
)
from test_version_references import source
from test_workflow_guards import import_workflow_with_stubs


@pytest.mark.parametrize(
    "outcome", ["unresolved", "absence", "invented", "contradiction"]
)
def test_production_and_eval_apply_the_same_uncertainty_contract(
    monkeypatch, tmp_path, caplog, outcome
):
    from evals.grounding import model_task
    from evals.grounding.dataset import Article, TaskInput
    from evals.grounding.runner import gate_result
    from src.core.report_artifact import parse_report_artifact
    from test_report_artifact import REPORT

    content = NARRATIVE
    if outcome == "contradiction":
        content += (
            "\n\nAffected versions: Gateway 7\n\n"
            "Affected versions: users of Gateway 7 are not affected"
        )
    article = source(content)
    catalog = build_reporting_catalog([article])
    value = unresolved_refs(catalog)[0]["id"]
    if outcome == "absence":
        value = ABSENT
    elif outcome == "invented":
        value = "Gateway 3.1"
    raw = raw_report(catalog, value)
    result = {
        PROTOCOL_KEY: PROTOCOL_VERSION,
        "exploitation_report": raw,
        "reporting_sources": serialize_reporting_catalog(catalog),
        "date": "2026-11-02",
        "generated_at": "2026-11-02T12:00:00Z",
    }
    monkeypatch.setenv("OPENROUTER_API_KEY", "synthetic-unused-key")
    monkeypatch.delenv("SENTRYINSIGHT_MODEL", raising=False)
    analyze = AsyncMock(return_value=result)
    monkeypatch.setattr(model_task, "analyze_exploitation", analyze)
    inputs = TaskInput(
        name="synthetic-unresolved-versions",
        articles=[Article(**article, source_links=[])],
        variant="baseline",
    )
    receipts = tmp_path / "synthetic-receipts.jsonl"
    task = model_task.ModelTask(
        model="openrouter/example/model:free", receipts=receipts, max_requests=1
    )
    workflow = import_workflow_with_stubs()
    output = tmp_path / "index.md"
    output.write_text(REPORT)
    public_paths = [
        tmp_path / "index.html",
        tmp_path / "current-findings.json",
        tmp_path / ".sentryinsight-articles-fingerprint",
    ]
    for path in public_paths:
        path.write_text("last good")
    state = {
        "analysis_results": result,
        "config": {"output_path": str(output)},
        "status": "started",
        "articles_fingerprint": "synthetic-next-fingerprint",
    }
    from src.core.version_references import resolve_analysis_version_references

    if outcome == "unresolved":
        # Historical schema4 replay remains valid and preserves explicit uncertainty.
        evaluated = resolve_analysis_version_references(result)
        artifact = parse_report_artifact(artifact_text(evaluated, catalog))
        assert artifact.schema_version == 4
        assert artifact.unresolved_version_count == 1
        assert gate_result(inputs, evaluated) == {"passed": True, "code": None}
        forged = evaluated.replace("Status**: unresolved", "Status**: not_stated")
        assert gate_result(inputs, forged) == {
            "passed": False,
            "code": "invalid_version_evidence_state",
        }
    else:
        with pytest.raises(EvidenceError):
            resolve_analysis_version_references(result)
    # New live work holds every source of this ambiguous/contradictory scope.
    state["articles"] = [article]
    with caplog.at_level("INFO", logger="src.core.workflow"):
        production = asyncio.run(workflow.filter_articles(state))
        production = asyncio.run(workflow.generate_report(production))
    assert production["status"] == "review_required"
    assert output.read_text() == REPORT
    assert all(path.read_text() == "last good" for path in public_paths)
    assert not (tmp_path / "reports").exists()
    assert list((tmp_path / ".sentryinsight-review").glob("*.json"))
    with pytest.raises(model_task.SourceReviewRequired):
        asyncio.run(task(inputs))
    assert task.requests == 0
    assert analyze.await_count == 0
    receipt = json.loads(receipts.read_text())
    assert receipt["attempts"] == 0
    assert receipt["outcome"] == "source_review_required"
    assert NARRATIVE not in receipts.read_text()
    assert raw not in receipts.read_text()
    assert value not in caplog.text

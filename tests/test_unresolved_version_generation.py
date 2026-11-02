"""Synthetic production/evaluation parity and last-good publication guards."""

import asyncio
import json
from unittest.mock import AsyncMock

import pytest

from src.core.finding_evidence import ABSENT, EvidenceError
from src.core.reporting import (
    build_reporting_catalog,
    resolve_reporting_keys,
    serialize_reporting_catalog,
)
from src.core.version_references import PROTOCOL_KEY, PROTOCOL_VERSION
from test_unresolved_versions import NARRATIVE, raw_report, unresolved_refs
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
    with caplog.at_level("INFO", logger="src.core.workflow"):
        production = asyncio.run(workflow.generate_report(state))
    if outcome == "unresolved":
        assert production["status"] != "failed", production.get("failure")
        assert production["unresolved_version_count"] == 1
        assert "1 finding(s) with unresolved affected-version evidence" in caplog.text
        artifact = parse_report_artifact(output.read_text())
        assert artifact.schema_version == 4
        assert artifact.unresolved_version_count == 1
        assert (tmp_path / "reports" / "2026-08-13.md").read_text() == REPORT
        assert "Affected versions unresolved" in public_paths[0].read_text()
        manifest = json.loads(public_paths[1].read_text())
        assert manifest["schema_version"] == 1
        assert manifest["finding_count"] == 1
        assert public_paths[2].read_text().strip() == "synthetic-next-fingerprint"
        evaluated = asyncio.run(task(inputs))
        assert (
            artifact.body.strip() == resolve_reporting_keys(evaluated, catalog).strip()
        )
        assert gate_result(inputs, evaluated) == {"passed": True, "code": None}
        forged = evaluated.replace("Status**: unresolved", "Status**: not_stated")
        assert gate_result(inputs, forged) == {
            "passed": False,
            "code": "invalid_version_evidence_state",
        }
    else:
        assert production["status"] == "failed"
        assert "unresolved_version_count" not in production
        assert output.read_text() == REPORT
        assert all(path.read_text() == "last good" for path in public_paths)
        assert not (tmp_path / "reports").exists()
        with pytest.raises(EvidenceError) as caught:
            asyncio.run(task(inputs))
        assert production["failure"]["codes"] == [caught.value.code]
    assert analyze.await_count == 1  # Mock only; no provider transport is called.
    assert NARRATIVE not in receipts.read_text()
    assert raw not in receipts.read_text()
    assert value not in caplog.text

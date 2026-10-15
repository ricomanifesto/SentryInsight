"""Nominal event evidence survives the actual generation and publication graph."""

from pathlib import Path
import httpx
import pytest
from publication_evidence import capture_generated_evidence
from src.core.finding_evidence import EvidenceError, validate_finding_evidence
from src.core.report_artifact import parse_report_artifact
from src.core.reporting import build_reporting_catalog
from test_finding_generation_pipeline import run_real_pipeline
from test_owned_relation_contract import article

A = "CVE-2026-1234"


@pytest.mark.parametrize(
    "text,expected",
    [
        (f"{A} is under attack.", "active"),
        (f"{A} was under attack.", "observed"),
        (f"{A} may be under attack.", "potential"),
        (f"{A} is not under attack. {A} is actively exploited.", "unknown"),
        (
            f"{A} is not known to be under attack. {A} was exploited yesterday.",
            "observed",
        ),
        (f"{A} is under attack tomorrow.", "unsupported"),
        (f"{A} may under active exploitation.", "unsupported"),
        (f"The vendor has confirmed that {A} is under attack.", "unsupported"),
    ],
)
def test_complete_event_publication(monkeypatch, tmp_path, text, expected):
    def forbidden(*args, **kwargs):
        raise AssertionError("Real model/HTTP transport forbidden")

    monkeypatch.setattr(httpx.Client, "send", forbidden)
    monkeypatch.setattr(httpx.AsyncClient, "send", forbidden)
    root = Path(__file__).resolve().parents[1]
    previous = {
        name: (root / name).read_bytes()
        for name in (
            "index.md",
            "index.html",
            "current-findings.json",
            ".sentryinsight-articles-fingerprint",
        )
    }
    for name, data in previous.items():
        (tmp_path / name).write_bytes(data)
    source = article(
        f"## {A}\n\n{text} {A} allows remote code execution on the gateway."
    )
    published_baseline = capture_generated_evidence(monkeypatch)
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[source],
        expect_model_call=expected != "unsupported",
    )
    if expected == "unsupported":
        assert result["status"] == "failed"
        assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
        assert all(
            (tmp_path / name).read_bytes() == data for name, data in previous.items()
        )
        return
    assert result["status"] == "completed"
    report = (tmp_path / "index.md").read_text()
    finding = parse_report_artifact(report).findings[0]
    assert finding.exploitation_status.value == expected
    evidence = next(
        line
        for line in report.splitlines()
        if line.startswith("- **Source Evidence**:")
    )
    assert all(
        statement.strip() + "." in evidence
        for statement in text.split(".")
        if statement.strip()
    )
    catalog = build_reporting_catalog([source])
    baseline = published_baseline(report, catalog)
    damaged = baseline.replace(
        evidence, evidence.replace("under attack", "under review")
    )
    assert damaged != baseline
    with pytest.raises(EvidenceError) as failure:
        validate_finding_evidence(damaged, catalog)
    assert failure.value.code == "incomplete_source_evidence"
    assert failure.value.field == "Source Evidence"
    omitted = baseline.replace(evidence, "")
    if "not" in text:
        with pytest.raises(EvidenceError) as failure:
            validate_finding_evidence(omitted, catalog)
        assert failure.value.code == "incomplete_source_evidence"
        assert failure.value.field == "Source Evidence"
    else:
        # Simple legacy findings can omit the field; generated findings above
        # must still carry it, and an incomplete supplied field is rejected.
        validate_finding_evidence(omitted, catalog)

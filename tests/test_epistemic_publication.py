"""Knowledge ownership reaches publication without weakening source gates."""

from pathlib import Path

import httpx
import pytest

from src.core.finding_evidence import EvidenceError, validate_finding_evidence
from src.core.report_artifact import parse_report_artifact
from src.core.reporting import build_reporting_catalog
from publication_evidence import capture_generated_evidence
from test_finding_generation_pipeline import run_real_pipeline
from test_owned_relation_contract import article

A = "CVE-2026-1234"


@pytest.mark.parametrize(
    "text,expected",
    [
        (f"{A} is not known to be exploited.", "unknown"),
        (f"Attackers are not known to be exploiting {A}.", "unknown"),
        (
            f"{A} is not currently known to be exploited. {A} is actively exploited.",
            "active",
        ),
        (f"{A} is not known to be exploited. {A} was exploited yesterday.", "observed"),
        (f"{A} is not known not to be exploited.", "unsupported"),
        (f"{A} has been known to be exploited.", "unsupported"),
    ],
)
def test_owned_knowledge_publication_and_prior_artifact_preservation(
    monkeypatch, tmp_path, text, expected
):
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
    for name, content in previous.items():
        (tmp_path / name).write_bytes(content)
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
            (tmp_path / name).read_bytes() == content
            for name, content in previous.items()
        )
        return
    assert result["status"] == "completed"
    report = (tmp_path / "index.md").read_text()
    finding = parse_report_artifact(report).findings[0]
    assert finding.exploitation_status.value == expected
    for statement in text.split("."):
        if statement.strip():
            assert statement.strip() + "." in report
    evidence = next(
        line
        for line in report.splitlines()
        if line.startswith("- **Source Evidence**:")
    )
    for statement in text.split("."):
        if statement.strip():
            assert statement.strip() + "." in evidence
    catalog = build_reporting_catalog([source])
    baseline = published_baseline(report, catalog)
    damaged = baseline.replace(evidence, "")
    assert damaged != baseline
    if expected == "active":
        with pytest.raises(EvidenceError) as failure:
            validate_finding_evidence(damaged, catalog)
        assert failure.value.code == "incomplete_source_evidence"
        assert failure.value.field == "Source Evidence"
    else:
        # Legacy inputs may omit this field for these three unqualified
        # forms. Closed generation still emits every complete statement.
        validate_finding_evidence(damaged, catalog)

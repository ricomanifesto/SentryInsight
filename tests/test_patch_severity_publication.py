"""Complete guidance and rating context survive actual offline publication."""

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
    "rating,advice,severity,action",
    [
        (
            f"{A} is critical.",
            "Users should apply the vendor patch.",
            "critical",
            "patch",
        ),
        (
            "The severity is high.",
            "The vendor update should be installed.",
            "high",
            "patch",
        ),
        ("The vulnerability was low.", "Apply the vendor hotfix.", "low", "patch"),
        (
            "The severity rating is medium.",
            "Users should deploy the vendor fixes.",
            "medium",
            "patch",
        ),
        (
            f"{A} is not critical.",
            "Users should not apply the vendor patch.",
            "unknown",
            "none",
        ),
        (
            f"{A} may be critical.",
            "Users should apply the vendor patch if exposed.",
            "unknown",
            "none",
        ),
        (
            f"The vendor says {A} is critical.",
            "Users should apply the vendor patch.",
            "unknown",
            "patch",
        ),
        (
            f"Severity: critical. {A} is not critical.",
            "Users should apply the vendor patch.",
            "unknown",
            "patch",
        ),
        (
            f"{A} was low. {A} is critical.",
            "Users should apply the vendor patch.",
            "unknown",
            "patch",
        ),
        (
            f"{A} is critical. Its CVSS score is 9.8.",
            "Users should apply the vendor patch.",
            "critical",
            "patch",
        ),
        ("It is critical.", "Users should apply the vendor patch.", "unknown", "patch"),
        (
            "Its severity is critical.",
            "Users should apply the vendor patch.",
            "unknown",
            "patch",
        ),
        (
            "The severity is critical if reports are accurate.",
            "Users should apply the vendor patch.",
            "unknown",
            "patch",
        ),
        (
            "The severity is critical.",
            "Users should review logs after applying the vendor patch.",
            "unsupported",
            "none",
        ),
        (
            "The severity is critical.",
            "Users should apply the vendor-supplied patch.",
            "unsupported",
            "none",
        ),
        (
            "The severity is critical.",
            "Users should monitor the vendor patch.",
            "unsupported",
            "none",
        ),
        (
            "The severity is critical.",
            "Users should apply the vendor patch and arbitrary objects.",
            "unsupported",
            "none",
        ),
    ],
)
def test_patch_severity_publication(
    monkeypatch, tmp_path, rating, advice, severity, action
):
    def forbidden(*args, **kwargs):
        raise AssertionError("Real HTTP/model transport forbidden")

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
    source = article(f"## {A}\n\n{A} is actively exploited.\n\n{rating}\n\n{advice}")
    baseline_for = capture_generated_evidence(monkeypatch)
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[source],
        expect_model_call=severity != "unsupported",
    )
    if severity == "unsupported":
        assert result["status"] == "failed"
        assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
        assert all(
            (tmp_path / name).read_bytes() == data for name, data in previous.items()
        )
        return
    assert result["status"] == "completed"
    published = (tmp_path / "index.md").read_text()
    (finding,) = parse_report_artifact(published).findings
    assert finding.severity.value == severity
    assert finding.action.value == action
    assert advice in finding.recommended_actions
    catalog = build_reporting_catalog([source])
    baseline = baseline_for(published, catalog)
    context = next(
        line
        for line in baseline.splitlines()
        if line.startswith("- **Severity Context**:")
    )
    # Each complete sentence must survive; never substitute a summary for the
    # qualified or conflicting source statement to obtain an unknown badge.
    for statement in rating.split(". "):
        assert statement in context
    guidance = next(
        line
        for line in baseline.splitlines()
        if line.startswith("- **Recommended Actions**:")
    )
    mutations = [
        (
            context,
            "- **Severity Context**: incomplete rating context",
            "severity_context_not_grounded",
            "Severity Context",
        ),
        (
            guidance,
            "- **Recommended Actions**: Apply patches.",
            "recommendation_not_grounded",
            "Recommended Actions",
        ),
    ]
    for original, replacement, code, field in mutations:
        mutated = baseline.replace(original, replacement)
        assert mutated != baseline
        with pytest.raises(EvidenceError) as failure:
            validate_finding_evidence(mutated, catalog)
        assert (failure.value.code, failure.value.field) == (code, field)

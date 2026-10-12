"""Source-owned group references keep guidance distributive and complete."""

import pytest

from test_composed_document_pipeline_contract import article
from test_finding_generation_pipeline import run_real_pipeline
from src.core.report_artifact import parse_report_artifact


def source(guidance, extra=""):
    return article(
        "<h2>Advisory</h2><p>The advisory lists two known flaws that it says were successfully exploited.</p><table><tr><th>Flaw</th><th>Product</th></tr><tr><td>CVE-2026-1234</td><td>Example Server</td></tr><tr><td>CVE-2026-5678</td><td>Example Gateway</td></tr></table>"
        + extra
        + "<h2>Response</h2><p>"
        + guidance
        + "</p>"
    )


@pytest.mark.parametrize(
    "guidance,action",
    [
        ("Apply patches, including for the two flaws listed above.", "patch"),
        ("Do not apply patches, including for the two flaws listed above.", "none"),
        (
            "Users should apply patches, including for the two flaws listed above, if exposed.",
            "none",
        ),
    ],
)
def test_explicit_group_reference_preserves_guidance_without_duplicate_findings(
    monkeypatch, tmp_path, guidance, action
):
    result = run_real_pipeline(
        monkeypatch, tmp_path / "index.md", articles=[source(guidance)]
    )
    assert result["status"] == "completed", result
    report = (tmp_path / "index.md").read_text()
    findings = parse_report_artifact(report).findings
    assert {f.cve_ids for f in findings} == {("CVE-2026-1234",), ("CVE-2026-5678",)}
    assert len(findings) == 2
    assert all(f.recommended_actions == guidance for f in findings)
    assert all(f.action.value == action for f in findings)


@pytest.mark.parametrize(
    "guidance",
    [
        "Apply patches, including for the three flaws listed above.",
        "Apply patches, including for the two flaws listed below.",
        "Apply patches, including for the two flaws listed above, with unknown advice.",
    ],
)
def test_unresolved_reference_or_residual_fails_closed(monkeypatch, tmp_path, guidance):
    paths = [
        tmp_path / name
        for name in (
            "index.md",
            "index.html",
            "current-findings.json",
            ".sentryinsight-articles-fingerprint",
        )
    ]
    for path in paths:
        path.write_bytes(b"Prior validated artifact")
    result = run_real_pipeline(
        monkeypatch, paths[0], articles=[source(guidance)], expect_model_call=False
    )
    assert (
        result["status"] == "failed"
        and result["analysis_results"]["error"] == "unsupported_evidence_relation"
    )
    assert all(path.read_bytes() == b"Prior validated artifact" for path in paths)

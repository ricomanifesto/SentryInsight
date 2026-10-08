"""Finding membership differs from complete evidence retention and coverage."""

import json

import pytest

from test_finding_generation_pipeline import run_real_pipeline

CVE = "CVE-2026-1234"
OTHER = "CVE-2026-5678"


def article(content, path="scope"):
    return dict(
        title="Example reporting",
        source="Publisher",
        link=f"https://example.test/{path}",
        content_kind="article",
        content=content,
    )


@pytest.mark.parametrize(
    "statement",
    [
        f"{CVE} is actively exploited.",
        f"{CVE} exploitation has not been observed.",
        f"{CVE} exploitation status is unknown.",
        f"{CVE} is a critical vulnerability that allows remote code execution.",
    ],
)
def test_pipeline_selects_relevant_scope_without_incidental_cves_or_routine_sources(
    monkeypatch, tmp_path, statement
):
    source = f"## {CVE}\n\n{statement}\n\nUsers should install the patch.\n\n## {OTHER}\n\nThe release notes mention {OTHER}."
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[
            article(source),
            article("The product release adds a new color theme.", "routine"),
        ],
    )
    assert result["status"] == "completed", result
    artifact = json.loads((tmp_path / "current-findings.json").read_text())
    assert artifact["finding_count"] == 1
    assert artifact["cve_ids"] == [CVE]
    assert "color theme" not in (tmp_path / "index.md").read_text()


def test_selected_cve_keeps_every_contrary_source_and_complete_guidance(
    monkeypatch, tmp_path
):
    negative = f"{CVE} exploitation has not been observed. Users should not install the patch until the vendor confirms availability."
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[
            article(f"{CVE} is actively exploited.", "positive"),
            article(negative, "negative"),
            article("Routine release notes.", "routine"),
        ],
    )
    assert result["status"] == "completed", result
    report = (tmp_path / "index.md").read_text()
    assert "**Exploitation Status**: unknown" in report
    assert "conflicting" in report
    assert negative in report
    assert len(result["analysis_results"]["reporting_sources"]) == 3


def test_joint_detail_closure_preserves_context_for_relevant_member(
    monkeypatch, tmp_path
):
    guidance = f"For {CVE} and {OTHER}, users should install the patch."
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[article(f"{CVE} is actively exploited.\n\n{guidance}")],
    )
    assert result["status"] == "completed", result
    report = (tmp_path / "index.md").read_text()
    artifact = json.loads((tmp_path / "current-findings.json").read_text())
    assert artifact["finding_count"] == 1
    assert set(artifact["cve_ids"]) == {CVE, OTHER}
    assert guidance in report


@pytest.mark.parametrize(
    "content",
    [
        "Exploitation status is unknown for the gateway.",
        "A malware campaign targets the gateway.",
        "Exploitation has not been observed for the gateway.",
    ],
)
def test_relevant_cveless_findings_remain_eligible(monkeypatch, tmp_path, content):
    result = run_real_pipeline(
        monkeypatch, tmp_path / "index.md", articles=[article(content)]
    )
    assert result["status"] == "completed", result
    artifact = json.loads((tmp_path / "current-findings.json").read_text())
    assert artifact["finding_count"] == 1
    assert artifact["cve_ids"] == []
    assert content in (tmp_path / "index.md").read_text()


@pytest.mark.parametrize(
    "content",
    [
        "The product release adds a new color theme.",
        f"Release notes mention {CVE} and {OTHER}.",
    ],
)
def test_no_relevant_finding_fails_before_model_and_preserves_report(
    monkeypatch, tmp_path, content
):
    output = tmp_path / "index.md"
    output.write_text("Previous validated report")
    fingerprint = tmp_path / ".sentryinsight-articles-fingerprint"
    fingerprint.write_text("previous\n")
    result = run_real_pipeline(
        monkeypatch, output, articles=[article(content)], expect_model_call=False
    )
    assert result["status"] == "failed"
    assert result["analysis_results"]["error"] == "empty_generation_evidence"
    assert output.read_text() == "Previous validated report"
    assert fingerprint.read_text() == "previous\n"

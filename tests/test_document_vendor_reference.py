"""Named advisory links require the same source-owned vendor declaration."""

from dataclasses import asdict

import pytest

from src.core.finding_generation import compile_finding_records
from src.core.finding_evidence import EvidenceError
from src.core.report_artifact import parse_report_artifact
from src.core.reporting import build_reporting_catalog
from src.services.article_content import extract_article_content
from test_finding_generation_pipeline import run_real_pipeline


def fixture(owner="Example", duplicate=False, qualification=False):
    paragraph = f'<p>See <a href="https://vendor.example/security/advisory">{owner}\'s advisory</a> for CVE-2026-1234 and CVE-2026-5678.</p>'
    if qualification:
        from test_document_capability_completeness import QUALIFICATIONS

        paragraph = (
            "<p>"
            + QUALIFICATIONS[1].replace(
                "Example's advisory",
                f'<a href="https://vendor.example/security/advisory">{owner}\'s advisory</a>',
            )
            + "</p>"
        )
    html = (
        "<p>Example released security advisories for two critical vulnerabilities in its Example data center network operating system that could be exploited to run arbitrary code with root privileges on Example switches.</p>"
        "<p>All two vulnerabilities are listed below:</p><ul><li>CVE-2026-1234: A gateway flaw.</li><li>CVE-2026-5678: Another gateway flaw.</li></ul>"
        "<p>All two vulnerabilities were discovered during internal security testing, and Example said it was unaware of public announcements or malicious exploitation at the time of publishing the advisories.</p>"
        + paragraph
        + ("<h2>CVE-2026-9999</h2>" + paragraph if duplicate else "")
    )
    result = extract_article_content(
        f"<article>{html}</article>", "https://example.test/advisory"
    )
    return dict(
        title="Security report",
        source="Publisher",
        link="https://example.test/advisory",
        content=result.text,
        content_kind="article",
        source_blocks=[asdict(b) for b in result.blocks],
        source_links=list(result.links),
        source_link_contexts=[asdict(link) for link in result.link_contexts],
    )


@pytest.mark.parametrize("qualification", [False, True])
def test_named_advisory_of_declared_vendor_survives_pipeline(
    monkeypatch, tmp_path, qualification
):
    item = fixture(qualification=qualification)
    result = run_real_pipeline(monkeypatch, tmp_path / "index.md", articles=[item])
    assert result["status"] == "completed", result
    (finding,) = parse_report_artifact((tmp_path / "index.md").read_text()).findings
    assert finding.vendor_links == ("https://vendor.example/security/advisory",)


def test_unowned_named_advisory_cannot_gain_vendor_role():
    catalog = build_reporting_catalog([fixture("Unrelated")])
    records = compile_finding_records(catalog, ["CVE-2026-1234", "CVE-2026-5678"])
    selected = next(r for r in records if "CVE-2026-1234" in dict(r.fields)["CVE IDs"])
    assert not selected.links


def test_duplicate_owned_advisory_fails_before_transport_and_preserves_artifacts(
    monkeypatch, tmp_path
):
    item = fixture(duplicate=True)
    with pytest.raises(EvidenceError) as exc:
        compile_finding_records(
            build_reporting_catalog([item]), ["CVE-2026-1234", "CVE-2026-5678"]
        )
    assert exc.value.code == "ambiguous_advisory_link_scope"
    names = (
        "index.md",
        "index.html",
        "current-findings.json",
        ".sentryinsight-articles-fingerprint",
    )
    for name in names:
        (tmp_path / name).write_bytes(b"Previous validated artifact")
    result = run_real_pipeline(
        monkeypatch, tmp_path / "index.md", articles=[item], expect_model_call=False
    )
    assert result["analysis_results"]["error"] == "ambiguous_advisory_link_scope"
    assert all(
        (tmp_path / name).read_bytes() == b"Previous validated artifact"
        for name in names
    )

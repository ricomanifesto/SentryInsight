from __future__ import annotations

import json
from pathlib import Path
from xml.etree import ElementTree as ET

import pytest

from src.core.report_artifact import parse_report_artifact
from scripts.build_site import (
    ArchiveConflictError,
    archive_previous_report,
    build_site,
    check_site,
)

from test_report_artifact import REPORT

ROOT = Path(__file__).resolve().parents[1]


def report_v2() -> str:
    return (
        REPORT.replace("schema_version: 1", "schema_version: 2")
        .replace(
            "generated_at: 2026-08-13T13:21:22Z",
            "generated_at: 2026-08-13T13:21:22Z\n"
            "digest_issue_url: https://ricomanifesto.github.io/"
            "SentryDigest/archive/2026-08-13/",
        )
        .replace(
            "- **CVE IDs**: CVE-2026-1234, CVE-2026-12345678",
            "- **CVE IDs**: CVE-2026-1234, CVE-2026-12345678\n"
            "- **Reporting**: [Example Security — Critical vendor flaw exploited]"
            "(https://example.com/security/advisory)",
        )
        .replace(
            "- **Action**: investigate",
            "- **Action**: investigate\n"
            "- **Reporting**: [Research Team — Independent follow-up]"
            "(https://research.example.net/follow-up)",
        )
    )


def build_fixture(tmp_path: Path, report: str = REPORT) -> Path:
    report_path = tmp_path / "index.md"
    report_path.write_text(report)
    output_path = tmp_path / "site"
    build_site(
        report_path=report_path,
        output_path=output_path,
        template_path=ROOT / "site",
    )
    return output_path


def test_site_builder_renders_meaningful_initial_html_without_runtime_markdown(
    tmp_path,
):
    output_path = build_fixture(tmp_path)
    html = (output_path / "index.html").read_text()

    assert "Attackers are exploiting an exposed service." in html
    assert (
        '<span class="report-kicker">Exploitation Report</span>'
        '<time datetime="2026-08-13">August 13, 2026</time>' in html
    )
    assert html.count("<h1") == 1
    assert "Report for Thursday, August 13, 2026" not in html
    assert 'datetime="2026-08-13T13:21:22Z"' in html
    assert "Example vulnerability (CVE-2026-1234)" in html
    assert "fetch(" not in html
    assert "Date.now()" not in html
    assert "marked" not in html.lower()
    assert "jsdelivr" not in html.lower()
    assert 'src="assets/vendor/dompurify.min.js?' in html
    assert "Last-Modified" not in html


def test_site_builder_embeds_source_owned_finding_metadata(tmp_path):
    output_path = build_fixture(tmp_path)
    html = (output_path / "index.html").read_text()

    assert 'data-severity="critical"' in html
    assert 'data-exploitation-status="active"' in html
    assert 'data-action="patch"' in html
    assert (
        '<span id="cve-2026-1234" class="cve-handoff-target" aria-hidden="true"></span>'
        in html
    )
    assert (
        '<span id="cve-2026-12345678" class="cve-handoff-target" aria-hidden="true"></span>'
        in html
    )
    assert html.count('data-severity="critical"') == 1


def test_site_builder_renders_each_finding_classification_once_in_initial_html(
    tmp_path,
):
    output_path = build_fixture(tmp_path)
    html = (output_path / "index.html").read_text()

    assert html.count('class="finding-disclosure"') == 2
    assert html.count('class="badge badge-severity"') == 2
    assert html.count('class="badge badge-exploitation-status"') == 2
    assert html.count('class="badge badge-action"') == 2
    assert html.count('class="cve-chip"') == 2
    disclosure = html.split('class="finding-disclosure"', maxsplit=1)[1].split(
        "</button>", maxsplit=1
    )[0]
    assert disclosure.index('class="disclosure-icon"') < disclosure.index(
        'class="finding-title"'
    )
    assert "<strong>Severity</strong>" not in html
    assert "<strong>Exploitation Status</strong>" not in html
    assert "<strong>Action</strong>" not in html
    assert "<strong>CVE IDs</strong>" not in html
    assert ">Critical</span>" in html
    assert ">Active exploitation</span>" in html
    assert ">Patch</span>" in html
    assert 'target="_blank" rel="noopener noreferrer"' in html


def test_site_builder_renders_computed_report_shape_and_human_provenance(tmp_path):
    output_path = build_fixture(tmp_path)
    html = (output_path / "index.html").read_text()

    assert "2 findings · 2 CVEs" in html
    assert 'class="report-method"' in html
    assert "AI-assisted" in html
    assert 'href="https://ricomanifesto.github.io/SentryDigest/"' in html
    assert 'href="https://ricomanifesto.com/"' in html
    assert "Verify NVD and vendor guidance before action." in html
    assert 'class="site-footer"' in html


def test_site_builder_publishes_a_minimal_current_finding_manifest(tmp_path):
    output_path = build_fixture(tmp_path)
    manifest = json.loads((output_path / "current-findings.json").read_text())

    assert manifest == {
        "schema_version": 1,
        "report_date": "2026-08-13",
        "generated_at": "2026-08-13T13:21:22Z",
        "report_url": "https://ricomanifesto.github.io/SentryInsight/",
        "finding_count": 2,
        "complete_cve_count": 2,
        "cve_ids": ["CVE-2026-1234", "CVE-2026-12345678"],
    }


def test_site_builder_renders_input_grounded_reporting_and_dated_digest_handoffs(
    tmp_path,
):
    output_path = build_fixture(tmp_path, report_v2())
    html = (output_path / "index.html").read_text()

    assert html.count('class="finding-reporting"') == 2
    assert (
        'class="reporting-source" href="https://example.com/security/advisory" '
        'target="_blank" rel="noopener noreferrer"' in html
    )
    assert (
        'href="https://ricomanifesto.github.io/SentryDigest/archive/2026-08-13/'
        '#reporting-cc16b55febdc">Digest context</a>' in html
    )
    assert (
        'href="https://ricomanifesto.github.io/SentryDigest/archive/2026-08-13/">'
        "Sentry Digest issue for this report date</a>" in html
    )
    assert "<strong>Reporting</strong>:" not in html
    metadata = json.loads(
        html.split('<script id="report-metadata" type="application/json">', 1)[1].split(
            "</script>", 1
        )[0]
    )
    assert metadata["digest_issue_url"].endswith("/archive/2026-08-13/")
    assert metadata["findings"][0]["reporting"][0]["publisher"] == "Example Security"


def test_site_builder_sets_theme_before_styles_and_renders_both_logo_variants(
    tmp_path,
):
    output_path = build_fixture(tmp_path)
    report_html = (output_path / "index.html").read_text()
    archive_html = (output_path / "reports" / "index.html").read_text()

    for html in (report_html, archive_html):
        head = html.split("</head>", maxsplit=1)[0]
        assert '<html lang="en" data-theme="light">' in head
        assert head.index("sentryinsight-theme") < head.index('rel="stylesheet"')
        assert 'class="brand-logo brand-logo-light"' in html
        assert 'class="brand-logo brand-logo-dark"' in html
        assert "logo-lockup-light.png" in html
        assert "logo-lockup-dark.png" in html


def test_site_builder_injects_one_canonical_theme_bootstrap(tmp_path):
    output_path = build_fixture(tmp_path)
    bootstrap = (ROOT / "site" / "theme-bootstrap.js").read_text().strip()

    assert "localStorage.getItem" not in (ROOT / "site" / "report.html").read_text()
    assert "localStorage.getItem" not in (ROOT / "site" / "archive.html").read_text()
    assert (output_path / "index.html").read_text().count(bootstrap) == 1
    assert (output_path / "reports" / "index.html").read_text().count(bootstrap) == 1
    assert "prefers-color-scheme" not in bootstrap
    assert 'theme = "light"' in bootstrap


def test_site_builder_generates_clean_desktop_and_mobile_section_maps(tmp_path):
    output_path = build_fixture(tmp_path)
    html = (output_path / "index.html").read_text()

    assert html.count('href="#example-vulnerability-cve-2026-1234"') == 3
    assert 'aria-label="Report sections"' in html
    assert "<summary>On this page</summary>" in html
    toc_label = "Example vulnerability (CVE-2026-1234)"
    assert f">{toc_label}</a>" in html
    assert f">{toc_label} Critical" not in html


def test_site_builder_generates_truthful_archive_manifest_and_pages(tmp_path):
    output_path = build_fixture(tmp_path)
    manifest = json.loads((output_path / "reports" / "index.json").read_text())
    archive_html = (output_path / "reports" / "index.html").read_text()

    assert manifest["schema_version"] == 1
    assert manifest["reports"] == []
    assert "No archived reports yet" in archive_html
    assert (
        "Reports accumulate through daily rollovers. Retained history begins with the "
        "Thursday, August 13, 2026 report at the first date change." in archive_html
    )
    assert "archiveReports = [" not in archive_html
    assert "archive artifacts tracked" not in archive_html
    assert not (output_path / "reports" / "search.js").exists()


def test_previous_report_rolls_into_immutable_history_when_date_advances(tmp_path):
    reports_path = tmp_path / "site" / "reports"
    reports_path.mkdir(parents=True)
    next_report = parse_report_artifact(REPORT.replace("2026-08-13", "2026-08-14"))

    archive_previous_report(
        current_source=REPORT,
        next_report=next_report,
        reports_path=reports_path,
    )

    archived_report = reports_path / "2026-08-13.md"
    assert archived_report.read_text() == REPORT

    current_report = tmp_path / "index.md"
    current_report.write_text(next_report.source)
    build_site(
        report_path=current_report,
        output_path=tmp_path / "site",
        template_path=ROOT / "site",
    )
    manifest = json.loads((reports_path / "index.json").read_text())
    assert manifest["reports"] == [
        {
            "report_date": "2026-08-13",
            "generated_at": "2026-08-13T13:21:22Z",
            "html_path": "2026-08-13.html",
            "markdown_path": "2026-08-13.md",
            "finding_count": 2,
            "cve_count": 2,
        }
    ]
    assert (
        "Reports accumulate through daily rollovers. Retained history begins "
        "Thursday, August 13, 2026." in (reports_path / "index.html").read_text()
    )
    current_html = (tmp_path / "site" / "index.html").read_text()
    archived_html = (reports_path / "2026-08-13.html").read_text()
    assert '<span id="report-age"></span>' in current_html
    assert "Archived snapshot" not in current_html
    assert 'id="report-age"' not in archived_html
    assert '<span class="report-frozen"> · Archived snapshot</span>' in archived_html


def test_second_rollover_accumulates_ordered_history_and_pluralizes(tmp_path):
    output_path = tmp_path / "site"
    reports_path = output_path / "reports"
    reports_path.mkdir(parents=True)
    second_source = REPORT.replace("2026-08-13", "2026-08-14")
    third_source = REPORT.replace("2026-08-13", "2026-08-15")

    archive_previous_report(
        current_source=REPORT,
        next_report=parse_report_artifact(second_source),
        reports_path=reports_path,
    )
    first_bytes = (reports_path / "2026-08-13.md").read_bytes()
    archive_previous_report(
        current_source=second_source,
        next_report=parse_report_artifact(third_source),
        reports_path=reports_path,
    )
    current_report = tmp_path / "index.md"
    current_report.write_text(third_source)
    build_site(
        report_path=current_report,
        output_path=output_path,
        template_path=ROOT / "site",
    )

    assert (reports_path / "2026-08-13.md").read_bytes() == first_bytes
    assert (reports_path / "2026-08-14.md").read_text() == second_source
    manifest = json.loads((reports_path / "index.json").read_text())
    assert [entry["report_date"] for entry in manifest["reports"]] == [
        "2026-08-14",
        "2026-08-13",
    ]
    archive_html = (reports_path / "index.html").read_text()
    assert "2 reports available" in archive_html
    assert "1 report available" not in archive_html
    assert archive_html.index("2026-08-14.html") < archive_html.index("2026-08-13.html")
    assert "Retained history begins Thursday, August 13, 2026." in archive_html
    for report_date in ("2026-08-13", "2026-08-14"):
        dated_html = (reports_path / f"{report_date}.html").read_text()
        assert 'id="report-age"' not in dated_html
        assert "Archived snapshot" in dated_html

    namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    sitemap = ET.parse(output_path / "sitemap.xml")
    locations = [node.text for node in sitemap.findall("s:url/s:loc", namespace)]
    assert locations == [
        "https://ricomanifesto.github.io/SentryInsight/",
        "https://ricomanifesto.github.io/SentryInsight/reports/",
        "https://ricomanifesto.github.io/SentryInsight/reports/2026-08-14.html",
        "https://ricomanifesto.github.io/SentryInsight/reports/2026-08-13.html",
    ]


def test_same_day_refresh_does_not_archive_or_conflict(tmp_path):
    reports_path = tmp_path / "reports"
    next_report = parse_report_artifact(
        REPORT.replace("exposed service", "edge appliance")
    )

    archive_previous_report(
        current_source=REPORT,
        next_report=next_report,
        reports_path=reports_path,
    )

    assert not reports_path.exists()


def test_site_builder_refuses_to_overwrite_different_content_for_same_date(tmp_path):
    reports_path = tmp_path / "reports"
    reports_path.mkdir()
    (reports_path / "2026-08-13.md").write_text("other content")
    next_report = parse_report_artifact(REPORT.replace("2026-08-13", "2026-08-14"))

    with pytest.raises(ArchiveConflictError, match="2026-08-13"):
        archive_previous_report(
            current_source=REPORT,
            next_report=next_report,
            reports_path=reports_path,
        )


def test_site_builder_disables_raw_html_and_active_link_protocols(tmp_path):
    malicious = REPORT.replace(
        "Attackers are exploiting an exposed service.",
        '<img src=x onerror="alert(1)"> '
        "<script>alert(1)</script> "
        "[unsafe](javascript:alert(1))",
    )
    output_path = build_fixture(tmp_path, malicious)
    html = (output_path / "index.html").read_text()

    assert "<script>alert(1)</script>" not in html
    assert "<img src=x" not in html
    assert 'href="javascript:' not in html
    assert "onerror=" not in html


def test_site_builder_has_no_audio_probe_or_stale_podcast_surface(tmp_path):
    output_path = build_fixture(tmp_path)
    html = (output_path / "index.html").read_text()

    assert "executive_summary.mp3" not in html
    assert "podcast/latest.mp3" not in html
    assert "Podcast Briefing" not in html
    assert "method: 'HEAD'" not in html


def test_site_check_detects_generated_output_drift(tmp_path):
    output_path = build_fixture(tmp_path)

    assert (
        check_site(
            report_path=tmp_path / "index.md",
            output_path=output_path,
            template_path=ROOT / "site",
        )
        == []
    )

    (output_path / "index.html").write_text("stale viewer")

    assert check_site(
        report_path=tmp_path / "index.md",
        output_path=output_path,
        template_path=ROOT / "site",
    ) == ["index.html"]

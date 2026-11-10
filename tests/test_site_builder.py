from __future__ import annotations

import html as _html
import json
import re
import shutil
from datetime import date as _date
from pathlib import Path
from xml.etree import ElementTree as ET

import pytest

import scripts.build_site as site_builder
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


def test_site_builder_emits_one_handoff_target_for_a_cve_shared_by_findings(
    tmp_path,
):
    report = REPORT.replace(
        "- **Action**: investigate\n\n## Affected Systems and Products",
        "- **Action**: investigate\n"
        "- **CVE IDs**: CVE-2026-1234\n\n"
        "## Affected Systems and Products",
    )

    output_path = build_fixture(tmp_path, report)
    html = (output_path / "index.html").read_text()

    assert html.count('id="cve-2026-1234" class="cve-handoff-target"') == 1
    assert html.count('href="https://nvd.nist.gov/vuln/detail/CVE-2026-1234"') == 2


@pytest.mark.parametrize(
    "title", ["CVE-2026-1234", "cve-2026-1234", "CVE-2026-12345678"]
)
@pytest.mark.parametrize("later_finding", [False, True])
def test_cve_only_headings_preserve_unique_handoff_and_navigation_targets(
    tmp_path, title, later_finding
):
    original_title = (
        "Vulnerability without an assigned CVE"
        if later_finding
        else "Example vulnerability (CVE-2026-1234)"
    )
    report = REPORT.replace(f"### {original_title}\n", f"### {title}\n")
    artifact = parse_report_artifact(report)
    finding = artifact.findings[int(later_finding)]
    output_path = build_fixture(tmp_path, report)
    page = (output_path / "index.html").read_text()

    ids = re.findall(r'\bid="([^"]+)"', page)
    assert len(ids) == len(set(ids))
    assert page.count(f'id="{title.lower()}" class="cve-handoff-target"') == 1
    assert finding.slug != title.lower()
    assert page.count(f'id="{finding.slug}"') == 1
    assert page.count(f'class="finding-link" href="#{finding.slug}"') == 2
    assert f'aria-controls="{finding.slug}-details"' in page
    assert page.count(f'id="{finding.slug}-details"') == 1


def test_descriptive_headings_keep_former_cve_only_bookmark_targets(tmp_path):
    output = build_fixture(tmp_path)
    page = (output / "index.html").read_text()
    assert page.count('id="finding-cve-2026-1234"') == 1
    assert page.count('id="finding-cve-2026-12345678"') == 1
    ids = re.findall(r'\bid="([^"]+)"', page)
    assert len(ids) == len(set(ids))


def test_bookmark_alias_cannot_steal_a_section_heading_id(tmp_path):
    report = REPORT + "\n## Finding CVE-2026-1234\n\nSupporting notes.\n"
    output = build_fixture(tmp_path, report)
    page = (output / "index.html").read_text()
    assert page.count('id="finding-cve-2026-1234"') == 1
    assert '<h2 id="finding-cve-2026-1234">' in page


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
    assert ">Exploited in the wild</span>" in html
    assert (
        'title="A source directly confirms attackers are exploiting this CVE."' in html
    )
    assert html.count('class="badge-legend"') == 1
    assert ">Patch</span>" in html
    assert 'target="_blank" rel="noopener noreferrer"' in html


def test_site_builder_renders_computed_report_shape_and_human_provenance(tmp_path):
    output_path = build_fixture(tmp_path)
    html = (output_path / "index.html").read_text()

    assert "2 findings · 2 CVEs" in html
    assert 'class="report-method"' in html
    assert "AI-assisted" in html
    assert 'href="https://sentrydigest.ricomanifesto.com/"' in html
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
        "report_url": "https://sentryinsight.ricomanifesto.com/",
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
        'href="https://sentrydigest.ricomanifesto.com/archive/2026-08-13/'
        '#reporting-cc16b55febdc">Digest context</a>' in html
    )
    assert (
        'href="https://sentrydigest.ricomanifesto.com/archive/2026-08-13/">'
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
    # The CVE suffix repeats the linked CVE chip, so labels drop it.
    toc_label = "Example vulnerability"
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
        "https://sentryinsight.ricomanifesto.com/",
        "https://sentryinsight.ricomanifesto.com/reports/",
        "https://sentryinsight.ricomanifesto.com/reports/2026-08-14.html",
        "https://sentryinsight.ricomanifesto.com/reports/2026-08-13.html",
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


def test_vendor_advisory_remains_a_link_instead_of_an_embedded_nvd_cve(tmp_path):
    source = REPORT.replace(
        "- **CVE IDs**:",
        "- **Vendor Links**: https://vendor.example/security/CVE-2026-1234\n- **CVE IDs**:",
        1,
    )
    html = (build_fixture(tmp_path, source) / "index.html").read_text()
    assert 'href="https://vendor.example/security/CVE-2026-1234"' in html


def test_titles_drop_only_a_cve_suffix_that_repeats_the_chips():
    from scripts.build_site import _display_title

    class F:
        def __init__(self, title, cves):
            self.title, self.cve_ids = title, tuple(cves)

    a, b = "CVE-2026-1234", "CVE-2026-5678"
    assert _display_title(F(f"Gateway RCE — {a}", [a])) == "Gateway RCE"
    assert _display_title(F(f"Gateway RCE ({a})", [a])) == "Gateway RCE"
    assert _display_title(F(f"Gateway — {a}, {b}", [a, b])) == "Gateway"
    # A suffix naming a CVE the finding does not carry stays visible.
    assert _display_title(F(f"Gateway — {b}", [a])) == f"Gateway — {b}"
    assert _display_title(F("Gateway RCE", [a])) == "Gateway RCE"
    assert _display_title(F(a, [a])) == a


def test_single_asterisks_stay_literal_while_bold_labels_render():
    from markdown_it import MarkdownIt

    from scripts.build_site import _literal_single_asterisks

    markdown = MarkdownIt("commonmark")
    tokens = markdown.parse(
        '- **Description**: "*sshole" accounts with hash "*" in /etc/shadow'
    )
    _literal_single_asterisks(tokens)
    rendered = markdown.renderer.render(tokens, markdown.options, {})
    assert "<strong>Description</strong>" in rendered
    assert "<em>" not in rendered
    assert "&quot;*sshole&quot; accounts with hash &quot;*&quot; in" in rendered


def test_vendor_links_are_labelled_by_host():
    from scripts.build_site import _vendor_link_labels

    assert _vendor_link_labels(
        [
            "https://www.zyxel.com/advisory-1",
            "https://nvd.nist.gov/vuln/detail/CVE-2026-1234",
            "https://www.zyxel.com/advisory-2",
        ]
    ) == ["zyxel.com", "nvd.nist.gov", "zyxel.com (2)"]


# CVE reporting history: computed from the retained archive for the current
# report only. Dated pages never change.


def history_report(report_date: str, findings, schema: int = 2) -> str:
    """A minimal valid report; findings are (title, cves, labels, sources)."""
    blocks = []
    for title, cves, labels, sources in findings:
        severity, status, action = labels
        lines = [
            f"### {title}",
            "- **Description**: A described vulnerability.",
            f"- **Severity**: {severity}",
            f"- **Exploitation Status**: {status}",
            f"- **Action**: {action}",
        ]
        if cves:
            lines.append(f"- **CVE IDs**: {', '.join(cves)}")
        if schema >= 2:
            lines.append(
                "- **Reporting**: "
                + ", ".join(
                    f"[{publisher} — {headline}]({url})"
                    for publisher, headline, url in sources
                )
            )
        blocks.append("\n".join(lines))
    header = f"---\nschema_version: {schema}\nreport_date: {report_date}\ngenerated_at: {report_date}T12:00:00Z\n"
    if schema >= 2:
        header += f"digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/{report_date}/\n"
    return (
        header
        + "---\n# Exploitation Report\n\n## Executive Summary\n\nSummary.\n\n"
        + "## Active Exploitation Details\n\n"
        + "\n\n".join(blocks)
        + "\n"
    )


SRC_A = ("Example News", "Flaw exploited", "https://news.example.com/a")
SRC_B = ("Other Desk", "CISA warns", "https://desk.example.org/b")
HIGH_POTENTIAL = ("high", "potential", "patch")
HIGH_UNKNOWN = ("high", "unknown", "patch")


def build_history(tmp_path: Path, current: str, archived: dict[str, str]) -> Path:
    output = tmp_path / "site"
    reports = output / "reports"
    reports.mkdir(parents=True)
    for day, text in archived.items():
        (reports / f"{day}.md").write_text(text)
    (tmp_path / "index.md").write_text(current)
    build_site(
        report_path=tmp_path / "index.md",
        output_path=output,
        template_path=ROOT / "site",
    )
    return output


def history_notes(page: str) -> str:
    match = re.findall(
        r'<aside class="finding-reporting finding-history".*?</aside>', page, re.S
    )
    return "\n".join(match)


def text_of(fragment: str) -> str:
    return _html.unescape(re.sub(r"<[^>]+>", "", fragment))


def test_history_counts_earlier_report_dates_and_links_each_in_date_order(tmp_path):
    finding = ("Flaw (CVE-2026-1111)", ["CVE-2026-1111"], HIGH_POTENTIAL, [SRC_A])
    archived = {
        d: history_report(d, [finding])
        for d in ("2026-08-14", "2026-08-15", "2026-08-17")
    }
    site = build_history(tmp_path, history_report("2026-08-18", [finding]), archived)
    notes = history_notes((site / "index.html").read_text())
    assert "Reported on 3 earlier report dates since August 14" in text_of(notes)
    links = re.findall(r'href="(reports/[^"]+)"', notes)
    assert links == [
        f"reports/{d}.html#cve-2026-1111"
        for d in ("2026-08-14", "2026-08-15", "2026-08-17")
    ]


def test_a_cve_listed_twice_in_one_report_is_one_observation_on_its_first_finding(
    tmp_path,
):
    first = ("First flaw", ["CVE-2026-2222"], HIGH_POTENTIAL, [SRC_A])
    second = ("Second flaw", ["CVE-2026-2222"], HIGH_UNKNOWN, [SRC_B])
    site = build_history(
        tmp_path,
        history_report("2026-08-20", [first]),
        {"2026-08-19": history_report("2026-08-19", [first, second])},
    )
    notes = text_of(history_notes((site / "index.html").read_text()))
    assert "Reported on 1 earlier report date since August 19" in notes
    archived_page = (site / "reports" / "2026-08-19.html").read_text()
    anchor = archived_page.index('id="cve-2026-2222"')
    assert (
        archived_page.index('id="first-flaw"')
        < anchor
        < archived_page.index('id="second-flaw"')
    )
    assert archived_page.count('id="cve-2026-2222"') == 1
    # The earlier observation is the first finding, so its sources are compared.
    assert "This finding and the August 19 finding cite the same source." in notes


def test_classification_names_the_previous_retained_report_even_days_back(tmp_path):
    keep = ("Kept", ["CVE-2026-3001"], HIGH_POTENTIAL, [SRC_A])
    older = ("Older", ["CVE-2026-3002"], HIGH_POTENTIAL, [SRC_A])
    fresh = ("Fresh", ["CVE-2026-3003"], HIGH_POTENTIAL, [SRC_A])
    archived = {
        "2026-08-10": history_report("2026-08-10", [older]),
        "2026-08-14": history_report("2026-08-14", [keep]),
    }
    site = build_history(
        tmp_path, history_report("2026-08-21", [keep, older, fresh]), archived
    )
    page = (site / "index.html").read_text()
    summary = text_of(
        re.search(r'<p id="cve-history-summary".*?</p>', page, re.S).group(0)
    )
    assert summary == (
        "Compared with the retained archive: 1 CVE is new to it, 1 was also in the "
        "August 14 report, and 1 was last reported earlier. CVE reporting history"
    )
    assert 'href="reports/#cve-history"' in page
    notes = text_of(history_notes(page))
    assert "CVE-2026-3003. First report of this CVE in the retained archive." in notes


def test_an_earlier_report_format_gives_dates_and_links_but_no_label_comparison(
    tmp_path,
):
    finding = (
        "Flaw (CVE-2026-4444)",
        ["CVE-2026-4444"],
        ("critical", "active", "patch"),
        [SRC_A],
    )
    site = build_history(
        tmp_path,
        history_report("2026-08-20", [finding]),
        {"2026-08-13": history_report("2026-08-13", [finding], schema=1)},
    )
    notes = history_notes((site / "index.html").read_text())
    text = text_of(notes)
    assert (
        "That report used an earlier report format, so its labels are not compared."
        in text
    )
    assert 'href="reports/2026-08-13.html#cve-2026-4444"' in notes
    for label in ("labelled", "Critical", "Exploited", "cite"):
        assert label not in text


def test_same_format_names_sources_and_quotes_dated_labels(tmp_path):
    before = ("Flaw (CVE-2026-5555)", ["CVE-2026-5555"], HIGH_POTENTIAL, [SRC_A])
    same_sources = ("Flaw (CVE-2026-5555)", ["CVE-2026-5555"], HIGH_UNKNOWN, [SRC_A])
    site = build_history(
        tmp_path,
        history_report("2026-08-20", [same_sources]),
        {"2026-08-19": history_report("2026-08-19", [before])},
    )
    text = text_of(history_notes((site / "index.html").read_text()))
    assert (
        "The August 19 finding was labelled High · Exploitable, no attacks seen · Patch."
        in text
    )
    assert "This finding and the August 19 finding cite the same source." in text
    assert "cites a source" not in text

    new_source = (
        "Flaw (CVE-2026-5555)",
        ["CVE-2026-5555"],
        HIGH_POTENTIAL,
        [SRC_A, SRC_B],
    )
    site = build_history(
        tmp_path / "b",
        history_report("2026-08-20", [new_source]),
        {"2026-08-19": history_report("2026-08-19", [before])},
    )
    notes = history_notes((site / "index.html").read_text())
    text = text_of(notes)
    assert (
        "This finding cites a source the August 19 finding did not: Other Desk — CISA warns."
        in text
    )
    assert 'href="https://desk.example.org/b"' in notes
    assert "The August 19 finding had the same labels." in text
    for banned in (
        "changed",
        "rose",
        "fell",
        "escalat",
        "downgrad",
        " now ",
        "no longer",
        "confirmed",
        "first seen",
        "times",
        " days",
    ):
        assert banned not in text.lower(), banned


def test_no_archive_and_no_cve_findings_render_no_history_markup(tmp_path):
    no_cve = ("Unnumbered flaw", [], HIGH_POTENTIAL, [SRC_A])
    site = build_history(tmp_path, history_report("2026-08-20", [no_cve]), {})
    page = (site / "index.html").read_text()
    assert "cve-history" not in page and "finding-history" not in page
    assert 'id="cve-history"' not in (site / "reports" / "index.html").read_text()

    site = build_history(
        tmp_path / "b",
        history_report("2026-08-20", [no_cve]),
        {"2026-08-19": history_report("2026-08-19", [no_cve])},
    )
    page = (site / "index.html").read_text()
    assert "cve-history-summary" not in page and "finding-history" not in page
    archive = (site / "reports" / "index.html").read_text()
    assert (
        "<ol" not in archive.split('id="cve-history"')[1].split("</section>")[0]
    ), "no empty list"


def test_history_text_is_escaped_and_links_are_http_or_relative(tmp_path):
    # The report parser already refuses tags in reporting labels; these are
    # the characters it accepts that still need escaping.
    hostile = (
        'Pub & "Co" <x',
        '5 < 6 & "quoted" > 4',
        "https://news.example.com/x?a=1&b='2'",
    )
    before = ("Flaw (CVE-2026-6666)", ["CVE-2026-6666"], HIGH_POTENTIAL, [SRC_A])
    after = (
        "Flaw (CVE-2026-6666)",
        ["CVE-2026-6666"],
        HIGH_POTENTIAL,
        [SRC_A, hostile],
    )
    site = build_history(
        tmp_path,
        history_report("2026-08-20", [after]),
        {"2026-08-19": history_report("2026-08-19", [before])},
    )
    notes = history_notes((site / "index.html").read_text())
    assert "Pub &amp; &quot;Co&quot; &lt;x" in notes
    assert "5 &lt; 6 &amp; &quot;quoted&quot; &gt; 4" in notes
    assert 'href="https://news.example.com/x?a=1&amp;b=&#x27;2&#x27;"' in notes
    for href in re.findall(r'href="([^"]*)"', notes):
        assert href.startswith(("https://", "http://", "reports/")), href


def test_every_history_link_lands_on_an_existing_id(tmp_path):
    finding = ("Flaw (CVE-2026-7777)", ["CVE-2026-7777"], HIGH_POTENTIAL, [SRC_A])
    other = ("Other (CVE-2026-7778)", ["CVE-2026-7778"], HIGH_POTENTIAL, [SRC_A])
    archived = {
        d: history_report(d, [other, finding]) for d in ("2026-08-14", "2026-08-15")
    }
    site = build_history(tmp_path, history_report("2026-08-20", [finding]), archived)
    assert_history_links_resolve(site)


def assert_history_links_resolve(site: Path) -> int:
    checked = 0
    pages = {
        site / "index.html": history_notes((site / "index.html").read_text())
        + (
            re.search(
                r'<p id="cve-history-summary".*?</p>',
                (site / "index.html").read_text(),
                re.S,
            )
            or [""]
        )[0],
        site
        / "reports"
        / "index.html": (site / "reports" / "index.html")
        .read_text()
        .split('id="cve-history"', 1)[-1],
    }
    for page, fragment in pages.items():
        for href in re.findall(r'href="([^"#]*\.html|[^"#]*/)?#([^"]+)"', fragment):
            target_path, anchor = href
            target = (page.parent / target_path) if target_path else page
            if target.is_dir():
                target = target / "index.html"
            assert f'id="{anchor}"' in target.read_text(), (page.name, href)
            checked += 1
    return checked


def test_a_failing_projection_publishes_the_report_without_history(
    tmp_path, monkeypatch, capsys
):
    finding = ("Flaw (CVE-2026-8888)", ["CVE-2026-8888"], HIGH_POTENTIAL, [SRC_A])
    archived = {"2026-08-19": history_report("2026-08-19", [finding])}
    monkeypatch.setattr(site_builder, "_history_view", lambda *a: None)
    plain = build_history(
        tmp_path / "plain", history_report("2026-08-20", [finding]), archived
    )

    def broken(*args):
        raise RuntimeError("history projection failure")

    monkeypatch.setattr(site_builder, "_history_view", broken)
    capsys.readouterr()
    failed = build_history(
        tmp_path / "failed", history_report("2026-08-20", [finding]), archived
    )
    warning = capsys.readouterr().err
    assert warning.count("\n") == 1 and "CVE reporting history omitted" in warning
    for name in ("index.html", "reports/index.html", "reports/2026-08-19.html"):
        assert (failed / name).read_bytes() == (plain / name).read_bytes(), name
    assert "finding-history" not in (failed / "index.html").read_text()


@pytest.mark.parametrize(
    "days, gaps",
    [
        (["2026-08-10", "2026-08-12", "2026-08-13"], "(Aug 11)"),
        (["2026-08-10", "2026-08-11", "2026-08-14"], "(Aug 12–Aug 13)"),
        (["2026-08-10", "2026-08-11", "2026-08-12"], None),
    ],
)
def test_coverage_names_gap_ranges_exactly_at_the_edges(tmp_path, days, gaps):
    finding = ("Flaw (CVE-2026-9999)", ["CVE-2026-9999"], HIGH_POTENTIAL, [SRC_A])
    *older, current = days
    site = build_history(
        tmp_path,
        history_report(current, [finding]),
        {d: history_report(d, [finding]) for d in older},
    )
    archive = text_of(
        (site / "reports" / "index.html")
        .read_text()
        .split('id="cve-history"', 1)[1]
        .split("</section>")[0]
    )
    assert (
        f"This archive holds 3 report dates from August 10 to August {current[-2:].lstrip('0')}, 2026, one report per date."
        in archive
    )
    if gaps is None:
        assert "It has a report for every date in that span." in archive
    else:
        missing = 1 if "–" not in gaps else 2
        assert (
            f"It has no report for {missing} date{'s' if missing > 1 else ''} in that span {gaps}"
            in archive
        )


def test_history_build_is_deterministic_and_check_is_clean(tmp_path):
    finding = ("Flaw (CVE-2026-1212)", ["CVE-2026-1212"], HIGH_POTENTIAL, [SRC_A])
    archived = {d: history_report(d, [finding]) for d in ("2026-08-14", "2026-08-15")}
    first = build_history(
        tmp_path / "one", history_report("2026-08-20", [finding]), archived
    )
    second = build_history(
        tmp_path / "two", history_report("2026-08-20", [finding]), archived
    )
    for path in sorted(p.relative_to(first) for p in first.rglob("*") if p.is_file()):
        assert (first / path).read_bytes() == (second / path).read_bytes(), path
    assert (
        check_site(
            report_path=tmp_path / "one" / "index.md",
            output_path=first,
            template_path=ROOT / "site",
        )
        == []
    )


def real_archive_copy(tmp_path: Path) -> Path:
    site = tmp_path / "real"
    shutil.copytree(ROOT / "reports", site / "reports")
    for relative in ("index.html", "assets/site.css", "assets/report.js"):
        (site / relative).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / relative, site / relative)
    return site


def test_real_archive_dated_pages_and_markdown_are_unchanged(tmp_path):
    site = real_archive_copy(tmp_path)
    before = {p.name: p.read_bytes() for p in (site / "reports").glob("????-??-??.*")}
    build_site(
        report_path=ROOT / "index.md", output_path=site, template_path=ROOT / "site"
    )
    after = {p.name: p.read_bytes() for p in (site / "reports").glob("????-??-??.*")}
    assert before.keys() == after.keys()
    version = re.compile(rb"\?v=[0-9a-f]{12}")
    for name in sorted(before):
        if name.endswith(".md"):
            assert after[name] == before[name], name
        else:
            assert version.sub(b"", after[name]) == version.sub(b"", before[name]), name


def test_real_archive_history_matches_a_recount_from_parsed_artifacts(tmp_path):
    site = real_archive_copy(tmp_path)
    build_site(
        report_path=ROOT / "index.md", output_path=site, template_path=ROOT / "site"
    )
    current = parse_report_artifact((ROOT / "index.md").read_text())
    archived = [
        parse_report_artifact(p.read_text())
        for p in sorted((ROOT / "reports").glob("????-??-??.md"))
    ]
    earlier_by_cve: dict[str, set[_date]] = {}
    for artifact in archived:
        for finding in artifact.findings:
            for cve in finding.cve_ids:
                earlier_by_cve.setdefault(cve, set()).add(artifact.report_date)
    previous = max(a.report_date for a in archived)
    current_cves = list(dict.fromkeys(c for f in current.findings for c in f.cve_ids))
    new = sum(1 for c in current_cves if c not in earlier_by_cve)
    also = sum(1 for c in current_cves if previous in earlier_by_cve.get(c, ()))
    earlier = len(current_cves) - new - also
    page = (site / "index.html").read_text()
    summary = text_of(
        re.search(r'<p id="cve-history-summary".*?</p>', page, re.S).group(0)
    )
    assert summary.startswith("Compared with the retained archive:")
    numbers = [
        int(n) for n in re.findall(r"(\d+) (?:CVEs? )?(?:is|are|was|were)", summary)
    ]
    assert numbers == [n for n in (new, also, earlier) if n], summary
    all_dates = {a.report_date for a in archived} | {current.report_date}
    by_cve = {c: set(d) for c, d in earlier_by_cve.items()}
    for finding in current.findings:
        for cve in finding.cve_ids:
            by_cve.setdefault(cve, set()).add(current.report_date)
    repeated = sum(1 for dates in by_cve.values() if len(dates) >= 2)
    archive = text_of(
        (site / "reports" / "index.html")
        .read_text()
        .split('id="cve-history"', 1)[1]
        .split("</section>")[0]
    )
    assert f"This archive holds {len(all_dates)} report dates" in archive
    total = sum(len(a.findings) for a in [*archived, current])
    with_cve = sum(1 for a in [*archived, current] for f in a.findings if f.cve_ids)
    assert (
        f"{with_cve} of {total} findings name a CVE; the other {total - with_cve} are not compared."
        in archive
    )
    assert f"{repeated} CVEs appear on more than one report date" in archive
    assert (
        len(
            re.findall(
                r'<li id="history-cve-', (site / "reports" / "index.html").read_text()
            )
        )
        == repeated
    )
    assert assert_history_links_resolve(site) > repeated


def test_every_current_finding_listing_a_cve_gets_its_own_note_counted_once(tmp_path):
    earlier = ("Flaw (CVE-2026-2323)", ["CVE-2026-2323"], HIGH_POTENTIAL, [SRC_A])
    first = ("First flaw", ["CVE-2026-2323"], HIGH_POTENTIAL, [SRC_A])
    second = ("Second flaw", ["CVE-2026-2323"], HIGH_UNKNOWN, [SRC_B])
    site = build_history(
        tmp_path,
        history_report("2026-08-20", [first, second]),
        {"2026-08-19": history_report("2026-08-19", [earlier])},
    )
    page = (site / "index.html").read_text()
    asides = re.findall(
        r'<aside class="finding-reporting finding-history".*?</aside>', page, re.S
    )
    assert len(asides) == 2, "one note in each finding"
    one, two = (text_of(a) for a in asides)
    for aside, note in zip(asides, (one, two)):
        assert "Reported on 1 earlier report date since August 19" in note
        assert 'href="reports/2026-08-19.html#cve-2026-2323"' in aside
    # Each note compares its own finding.
    assert "This finding and the August 19 finding cite the same source." in one
    assert "had the same labels" in one and "lists it first" not in one
    assert (
        "This finding cites a source the August 19 finding did not: Other Desk — CISA warns."
        in two
    )
    assert (
        "The August 19 finding was labelled High · Exploitable, no attacks seen · Patch."
        in two
    )
    assert "This report lists it first under First flaw." in two
    assert 'href="#first-flaw"' in asides[1]
    # One anchor, one count.
    assert page.count('id="cve-2026-2323"') == 1
    summary = text_of(
        re.search(r'<p id="cve-history-summary".*?</p>', page, re.S).group(0)
    )
    assert summary.startswith(
        "Compared with the retained archive: 1 CVE was also in the August 19 report."
    )
    assert_history_links_resolve(site)


def test_sources_are_compared_with_the_first_earlier_finding_not_the_whole_report(
    tmp_path,
):
    # The earlier report lists the CVE in two findings with different sources.
    # Its observation is the first one, so a source only the second cited is
    # still new relative to the compared finding, and the note says so.
    first = ("Flaw (CVE-2026-3434)", ["CVE-2026-3434"], HIGH_POTENTIAL, [SRC_A])
    second = ("Follow-up (CVE-2026-3434)", ["CVE-2026-3434"], HIGH_POTENTIAL, [SRC_B])
    current = ("Flaw (CVE-2026-3434)", ["CVE-2026-3434"], HIGH_POTENTIAL, [SRC_B])
    site = build_history(
        tmp_path,
        history_report("2026-08-20", [current]),
        {"2026-08-19": history_report("2026-08-19", [first, second])},
    )
    notes = history_notes((site / "index.html").read_text())
    text = text_of(notes)
    assert (
        "This finding cites a source the August 19 finding did not: Other Desk — CISA warns."
        in text
    )
    assert "report did not" not in text and "Reported on 1 earlier report date" in text
    assert notes.count('href="reports/2026-08-19.html#cve-2026-3434"') == 1

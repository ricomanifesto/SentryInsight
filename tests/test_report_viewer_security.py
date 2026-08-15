import hashlib
import html
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

from src.core.report_artifact import parse_report_artifact

REPORT = Path("index.md")
REPORT_PAGE = Path("index.html")
ARCHIVE_PAGE = Path("reports/index.html")
ARCHIVE_MANIFEST = Path("reports/index.json")
SITEMAP = Path("sitemap.xml")
SITE_CSS = Path("assets/site.css")
SITE_JS = Path("assets/report.js")
DOMPURIFY_JS = Path("assets/vendor/dompurify.min.js")
PUBLIC_SITE_URL = "https://ricomanifesto.github.io/SentryInsight/"
PUBLIC_ARCHIVE_URL = f"{PUBLIC_SITE_URL}reports/"
PUBLIC_DESCRIPTION = "Current exploitation intelligence for rapid defensive triage."


def extract_json_ld(page: str) -> dict:
    match = re.search(
        r'<script type="application/ld\+json">(.*?)</script>', page, re.DOTALL
    )
    assert match is not None
    return json.loads(match.group(1))


def test_public_pages_publish_canonical_identity_metadata_and_sitemap():
    report_page = REPORT_PAGE.read_text()
    archive_page = ARCHIVE_PAGE.read_text()

    assert f'<meta name="description" content="{PUBLIC_DESCRIPTION}">' in report_page
    assert f'<link rel="canonical" href="{PUBLIC_SITE_URL}">' in report_page
    assert f'<meta property="og:url" content="{PUBLIC_SITE_URL}">' in report_page
    assert '<meta name="twitter:card" content="summary_large_image">' in report_page
    report_identity = extract_json_ld(report_page)
    assert report_identity["@type"] == "WebSite"
    assert report_identity["name"] == "SentryInsight"
    assert report_identity["url"] == PUBLIC_SITE_URL

    assert f'<link rel="canonical" href="{PUBLIC_ARCHIVE_URL}">' in archive_page
    assert f'<meta property="og:url" content="{PUBLIC_ARCHIVE_URL}">' in archive_page
    archive_identity = extract_json_ld(archive_page)
    assert archive_identity["@type"] == "CollectionPage"
    assert archive_identity["url"] == PUBLIC_ARCHIVE_URL

    sitemap = ET.parse(SITEMAP)
    namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locations = [element.text for element in sitemap.findall("s:url/s:loc", namespace)]
    archive_manifest = json.loads(ARCHIVE_MANIFEST.read_text())
    archived_urls = [
        f"{PUBLIC_ARCHIVE_URL}{entry['html_path']}"
        for entry in archive_manifest["reports"]
    ]
    assert locations == [PUBLIC_SITE_URL, PUBLIC_ARCHIVE_URL, *archived_urls]


def test_report_is_meaningful_static_html_before_javascript_runs():
    artifact = parse_report_artifact(REPORT.read_text())
    page = REPORT_PAGE.read_text()

    assert '<main id="report-content"' in page
    assert '<h2 id="executive-summary">Executive Summary</h2>' in page
    assert (
        '<h2 id="active-exploitation-details">Active Exploitation Details</h2>' in page
    )
    assert html.escape(artifact.findings[0].title) in page
    assert "spinner" not in page.casefold()
    assert "fetch(" not in page
    assert "cache: 'no-store'" not in page
    assert "Date.now()" not in page
    assert "Last-Modified" not in page


def test_report_uses_artifact_owned_utc_time_metadata():
    artifact = parse_report_artifact(REPORT.read_text())
    page = REPORT_PAGE.read_text()
    report_date_iso = artifact.report_date.isoformat()
    report_date_label = (
        artifact.report_date.strftime("%B ")
        + str(artifact.report_date.day)
        + artifact.report_date.strftime(", %Y")
    )
    generated_at_iso = artifact.generated_at.isoformat().replace("+00:00", "Z")
    generated_at_label = (
        artifact.generated_at.strftime("%B ")
        + str(artifact.generated_at.day)
        + artifact.generated_at.strftime(", %Y at %H:%M UTC")
    )

    assert (
        '<span class="report-kicker">Exploitation Report</span>'
        f'<time datetime="{report_date_iso}">{report_date_label}</time>' in page
    )
    assert f"Report for {report_date_label}" not in page
    assert f'<time datetime="{generated_at_iso}">{generated_at_label}</time>' in page
    assert "toLocaleString" not in page


def test_complete_cves_are_linked_without_a_sequence_length_cap():
    artifact = parse_report_artifact(REPORT.read_text())
    page = REPORT_PAGE.read_text()
    cves = {cve for finding in artifact.findings for cve in finding.cve_ids}

    for cve in cves:
        assert f'href="https://nvd.nist.gov/vuln/detail/{cve}"' in page
        assert page.count(f'id="{cve.lower()}" class="cve-handoff-target"') == 1
    assert page.count('target="_blank" rel="noopener noreferrer"') >= len(cves)
    assert not re.search(r"CVE-\d{4}-\d{0,7}(?:\.\.\.|…)", page)
    assert "CVE ID assigned but not specified" not in page
    assert "CVE pending" not in page


def test_triage_badges_can_only_project_source_owned_allowed_values():
    artifact = parse_report_artifact(REPORT.read_text())
    page = REPORT_PAGE.read_text()
    metadata_match = re.search(
        r'<script id="report-metadata" type="application/json">(.*?)</script>',
        page,
        re.DOTALL,
    )
    assert metadata_match is not None
    metadata = json.loads(metadata_match.group(1))

    unique_cves = {cve for finding in artifact.findings for cve in finding.cve_ids}
    assert len(metadata["findings"]) == len(artifact.findings)
    assert metadata["finding_count"] == len(artifact.findings)
    assert metadata["complete_cve_count"] == len(unique_cves)
    for finding in artifact.findings:
        assert page.count(f'id="{finding.slug}"') == 1
        assert page.count(f'data-severity="{finding.severity.value}"') >= 1
        assert (
            page.count(
                f'data-exploitation-status="{finding.exploitation_status.value}"'
            )
            >= 1
        )
        assert page.count(f'data-action="{finding.action.value}"') >= 1
        heading_start = page.index(f'id="{finding.slug}"')
        heading_end = page.index("</h3>", heading_start)
        heading = page[heading_start:heading_end]
        assert heading.count('class="badge ') == 3
    assert page.count('class="badge badge-severity"') == len(artifact.findings)
    assert page.count('class="badge badge-exploitation-status"') == len(
        artifact.findings
    )
    assert page.count('class="badge badge-action"') == len(artifact.findings)
    assert "<strong>Severity</strong>" not in page
    assert "<strong>Exploitation Status</strong>" not in page
    assert "<strong>Action</strong>" not in page
    assert "<strong>CVE IDs</strong>" not in page
    assert Path("config/ui.json").exists() is False


def test_static_builder_replaces_runtime_markdown_and_bundles_sanitization():
    page = REPORT_PAGE.read_text()
    builder = Path("scripts/build_site.py").read_text()
    package = json.loads(Path("package.json").read_text())

    assert "marked" not in page.casefold()
    assert "jsdelivr" not in page.casefold()
    assert "unpkg" not in page.casefold()
    assert 'src="assets/vendor/dompurify.min.js?' in page
    assert "DOMPurify.sanitize" in SITE_JS.read_text()
    assert package["dependencies"]["dompurify"] == "3.4.13"
    assert DOMPURIFY_JS.exists()
    assert (
        hashlib.sha256(DOMPURIFY_JS.read_bytes()).hexdigest()
        == "9ab3d44d73c3e3947f9ab72e0f0bc15c7f1931d60b365ba261fc85fe59013c56"
    )
    assert "MarkdownIt" in builder
    assert "_strip_raw_html(tokens)" in builder
    assert "Rendered report contains active content" in builder


def test_one_canonical_publication_tree_prevents_viewer_drift():
    assert REPORT_PAGE.exists()
    assert ARCHIVE_PAGE.exists()
    assert Path(".nojekyll").exists()
    assert not Path("docs").exists()
    assert Path("site/report.html").exists()
    assert Path("site/archive.html").exists()
    assert (
        "scripts/build_site.py --check"
        in Path("scripts/local_validation.sh").read_text()
    )
    assert "scripts/package_pages.py" in Path("scripts/local_validation.sh").read_text()


def test_report_exposes_method_maintainer_and_computed_shape_to_readers():
    artifact = parse_report_artifact(REPORT.read_text())
    page = REPORT_PAGE.read_text()

    unique_cves = {cve for finding in artifact.findings for cve in finding.cve_ids}
    finding_label = "finding" if len(artifact.findings) == 1 else "findings"
    cve_label = "CVE" if len(unique_cves) == 1 else "CVEs"
    assert f"{len(artifact.findings)} {finding_label}" in page
    assert f"{len(unique_cves)} {cve_label}" in page
    assert "AI-assisted" in page
    assert f'href="{artifact.digest_issue_url}"' in page
    assert page.count('class="finding-reporting"') == len(artifact.findings)
    reporting_count = sum(len(finding.reporting) for finding in artifact.findings)
    assert page.count('class="reporting-source"') == reporting_count
    assert page.count('class="reporting-context"') == reporting_count
    assert 'href="https://ricomanifesto.com/"' in page
    assert "Verify NVD and vendor guidance before action." in page
    assert 'class="site-footer"' in page


def test_report_keeps_secondary_markdown_access_out_of_the_primary_header():
    page = REPORT_PAGE.read_text()
    header = page.split('<header class="site-header">', maxsplit=1)[1].split(
        "</header>", maxsplit=1
    )[0]
    footer = page.split('<footer class="site-footer">', maxsplit=1)[1].split(
        "</footer>", maxsplit=1
    )[0]

    assert 'href="index.md"' not in header
    assert '<a class="footer-markdown" href="index.md">Report Markdown</a>' in footer


def test_theme_and_brand_are_correct_before_deferred_javascript_runs():
    report_page = REPORT_PAGE.read_text()
    archive_page = ARCHIVE_PAGE.read_text()
    css = SITE_CSS.read_text()
    bootstrap = Path("site/theme-bootstrap.js").read_text().strip()

    for page in (report_page, archive_page):
        head = page.split("</head>", maxsplit=1)[0]
        assert head.index("sentryinsight-theme") < head.index('rel="stylesheet"')
        assert 'class="brand-logo brand-logo-light"' in page
        assert 'class="brand-logo brand-logo-dark"' in page
        assert page.count(bootstrap) == 1
    assert "localStorage.getItem" not in Path("site/report.html").read_text()
    assert "localStorage.getItem" not in Path("site/archive.html").read_text()
    assert ':root[data-theme="dark"] .brand-logo-light' in css
    assert ':root[data-theme="dark"] .brand-logo-dark' in css
    assert ":root:not([data-theme]) .brand-logo-light" not in css
    assert ":root:not([data-theme]) .brand-logo-dark" not in css


def test_archive_page_matches_real_dated_artifacts():
    manifest = json.loads(ARCHIVE_MANIFEST.read_text())
    archive_page = ARCHIVE_PAGE.read_text()

    assert manifest["schema_version"] == 1
    for report in manifest["reports"]:
        report_html = Path("reports") / report["html_path"]
        report_markdown = Path("reports") / report["markdown_path"]
        assert report_html.exists()
        assert report_markdown.exists()
        artifact = parse_report_artifact(report_markdown.read_text())
        unique_cves = {cve for finding in artifact.findings for cve in finding.cve_ids}
        assert report["finding_count"] == len(artifact.findings)
        assert report["cve_count"] == len(unique_cves)
    report_count = len(manifest["reports"])
    report_label = "report" if report_count == 1 else "reports"
    assert f"{report_count} {report_label} available" in archive_page
    if report_count == 0:
        assert "No archived reports yet" in archive_page
    else:
        assert "No archived reports yet" not in archive_page
    assert "archiveReports = [" not in archive_page
    assert "archive artifacts tracked" not in archive_page
    assert "Filter" not in archive_page


def test_report_has_clean_desktop_and_mobile_section_maps():
    artifact = parse_report_artifact(REPORT.read_text())
    page = REPORT_PAGE.read_text()

    assert page.count('aria-label="Report sections"') == 2
    assert "<summary>On this page</summary>" in page
    assert 'class="desktop-toc"' in page
    assert "Critical Patch" not in page
    assert "▼" not in page
    first_title = html.escape(artifact.findings[0].title)
    assert page.count(f">{first_title}</a>") == 2


def test_styles_guard_mobile_overflow_focus_and_print_layouts():
    css = SITE_CSS.read_text()

    assert "* { box-sizing: border-box; }" in css
    assert "min-width: 0;" in css
    assert "overflow-wrap: anywhere;" in css
    assert ":focus-visible" in css
    assert "@media (max-width: 900px)" in css
    assert ".desktop-toc { display: none; }" in css
    assert ".mobile-toc { display: block; }" in css
    assert "@media print" in css
    assert ".finding-body[hidden] { display: block; }" in css


def test_report_styles_use_one_compact_type_step_and_standard_weights():
    css = SITE_CSS.read_text()

    assert "--text-small: 0.875rem;" in css
    assert "--text-label" not in css
    assert "Inter" not in css
    assert set(re.findall(r"font-weight:\s*(\d+)", css)) <= {"400", "600", "700"}
    for ad_hoc_size in ("1.08rem", "1.15rem", "1.2rem"):
        assert ad_hoc_size not in css
    for ad_hoc_size in ("0.72rem", "0.8rem", "0.85rem", "0.86rem", "0.88rem", "0.9rem"):
        assert ad_hoc_size not in css


def test_theme_control_is_discoverable_and_has_no_hidden_shortcut():
    page = REPORT_PAGE.read_text()
    script = SITE_JS.read_text()

    assert (
        '<button id="theme-toggle" type="button" aria-pressed="false">Theme</button>'
        in page
    )
    assert 'themeToggle.setAttribute("aria-pressed"' in script
    assert 'localStorage.setItem("sentryinsight-theme"' in script
    assert "keydown" not in script
    assert 'key === "t"' not in script


def test_audio_and_stale_podcast_dead_ends_are_removed():
    public_text = REPORT_PAGE.read_text() + ARCHIVE_PAGE.read_text()

    assert "executive_summary.mp3" not in public_text
    assert "podcast/latest.mp3" not in public_text
    assert "Podcast Briefing" not in public_text
    assert not Path("executive_summary.mp3").exists()
    assert not Path("podcast").exists()
    assert not Path("podcast.xml").exists()
    assert not Path("assets/podcast-cover.png").exists()
    assert not list(Path("assets").rglob("*.mp3"))


def test_report_omits_operator_metric_panels_and_leads_with_content():
    page = REPORT_PAGE.read_text()
    removed_markers = (
        'id="provenance"',
        'id="uncertainty"',
        'id="coverage-notes"',
        'id="section-filter-panel"',
        "Report Provenance",
        "Uncertainty Signals",
        "Report Coverage",
    )
    for marker in removed_markers:
        assert marker not in page
    assert page.index('<main id="report-content"') < page.index(
        '<script id="report-metadata"'
    )

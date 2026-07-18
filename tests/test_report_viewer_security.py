import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

REPORT_VIEWERS = (
    Path("index.html"),
    Path("docs/index.html"),
)
ARCHIVE_INDEX = Path("docs/reports/index.html")
SITEMAP = Path("sitemap.xml")
PUBLIC_SITE_URL = "https://ricomanifesto.github.io/SentryInsight/"
PUBLIC_ARCHIVE_URL = f"{PUBLIC_SITE_URL}docs/reports/"
PUBLIC_DESCRIPTION = (
    "SentryInsight turns security RSS feeds into exploitation-focused threat "
    "reports, with CVE correlation, affected systems, attack vectors, and "
    "executive summaries ready for review."
)


def extract_json_ld(html: str) -> dict:
    match = re.search(
        r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL
    )
    assert match is not None
    return json.loads(match.group(1))


def test_public_pages_publish_canonical_identity_metadata_and_sitemap():
    for viewer_path in REPORT_VIEWERS:
        viewer = viewer_path.read_text()
        assert f'<meta name="description" content="{PUBLIC_DESCRIPTION}">' in viewer
        assert f'<link rel="canonical" href="{PUBLIC_SITE_URL}">' in viewer
        assert f'<meta property="og:url" content="{PUBLIC_SITE_URL}">' in viewer
        assert '<meta name="twitter:card" content="summary">' in viewer
        assert 'href="https://ricomanifesto.com/">Michael Rico</a>' in viewer
        assert "<noscript>" in viewer
        identity = extract_json_ld(viewer)
        assert identity["@context"] == "https://schema.org"
        assert identity["@type"] == "WebSite"
        assert identity["name"] == "SentryInsight"
        assert identity["url"] == PUBLIC_SITE_URL
        assert identity["description"] == PUBLIC_DESCRIPTION
        assert identity["author"] == {
            "@type": "Person",
            "name": "Michael Rico",
            "url": "https://ricomanifesto.com/",
        }
        assert identity["sameAs"] == "https://github.com/ricomanifesto/SentryInsight"

    archive = ARCHIVE_INDEX.read_text()
    assert f'<link rel="canonical" href="{PUBLIC_ARCHIVE_URL}">' in archive
    assert f'<meta property="og:url" content="{PUBLIC_ARCHIVE_URL}">' in archive
    assert '<meta name="twitter:card" content="summary">' in archive
    assert 'href="https://ricomanifesto.com/">Michael Rico</a>' in archive
    archive_identity = extract_json_ld(archive)
    assert archive_identity["@type"] == "CollectionPage"
    assert archive_identity["url"] == PUBLIC_ARCHIVE_URL
    assert archive_identity["author"]["name"] == "Michael Rico"

    sitemap = ET.parse(SITEMAP)
    namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locations = [element.text for element in sitemap.findall("s:url/s:loc", namespace)]
    assert locations == [PUBLIC_SITE_URL, PUBLIC_ARCHIVE_URL]


def test_report_viewers_sanitize_marked_output_before_rendering():
    for viewer_path in REPORT_VIEWERS:
        viewer = viewer_path.read_text()

        assert "dompurify@3" in viewer
        assert "DOMPurify.sanitize(marked.parse(text)" in viewer
        assert "let html = marked.parse(text);" not in viewer


def test_report_viewers_do_not_rewrite_sanitized_report_html_for_cve_links():
    for viewer_path in REPORT_VIEWERS:
        viewer = viewer_path.read_text()

        assert "document.createTreeWalker" in viewer
        assert "el.innerHTML = el.innerHTML.replace" not in viewer


def test_report_viewers_include_mobile_overflow_guards():
    for viewer_path in REPORT_VIEWERS:
        viewer = viewer_path.read_text()

        assert "box-sizing: border-box;" in viewer
        assert "min-width: 0;" in viewer
        assert "overflow-wrap: anywhere;" in viewer
        assert "word-break: break-word;" in viewer
        assert "white-space: normal;" in viewer
        assert "max-width: 100%;" in viewer
        assert ".layout { width: 100%; }" in viewer
        assert (
            "main, .exec, #content { width: 100%; max-width: calc(100vw - 24px); overflow-x: hidden; }"
            in viewer
        )
        assert (
            "#content p, #content li, .exec p { overflow-wrap: anywhere; word-break: break-word; }"
            in viewer
        )
        assert "aside#toc { display: none; width: 100%; overflow-x: hidden; }" in viewer
        assert "#content { padding: 1.25em;" in viewer
        assert (
            "header.topbar { align-items: flex-start; flex-wrap: wrap; padding: 12px; }"
            in viewer
        )
        assert ".brand { flex: 1 1 100%; min-width: 0; }" in viewer
        assert ".spacer { display: none; }" in viewer
        assert ".toolbar { flex-wrap: wrap; width: 100%; }" in viewer


def test_report_viewers_extract_named_executive_summary_section():
    for viewer_path in REPORT_VIEWERS:
        viewer = viewer_path.read_text()

        assert "function extractExecutiveSummaryNodes()" in viewer
        assert "function renderExecutiveSummary()" in viewer
        assert "function appendExecutiveSummaryAudio()" in viewer
        assert (
            "const summaryHeading = Array.from(contentEl.querySelectorAll('h2')).find"
            in viewer
        )
        assert "label === 'executive summary'" in viewer
        assert (
            "paragraphs.forEach(paragraph => execEl.appendChild(paragraph.cloneNode(true)))"
            in viewer
        )
        assert "summaryNodes.forEach(node => node.remove())" in viewer
        assert "renderExecutiveSummary()" in viewer
        assert "first paragraph after H1" not in viewer


def test_report_viewers_resolve_logo_assets_without_project_path_lock():
    for viewer_path in REPORT_VIEWERS:
        viewer = viewer_path.read_text()

        assert 'src="/SentryInsight/assets/logo.png"' not in viewer
        assert 'href="/SentryInsight/assets/logo.png"' not in viewer
        assert 'data-logo-asset="icon"' in viewer
        assert 'data-logo-asset="shortcut-icon"' in viewer
        assert 'data-logo-asset="header-logo"' in viewer
        assert "function resolveLogoAssetPath()" in viewer
        assert "function applyLogoAssetPath()" in viewer
        assert "location.pathname.includes('/docs/')" in viewer
        assert "const logoPath = resolveLogoAssetPath()" in viewer
        assert "applyLogoAssetPath()" in viewer


def test_report_viewers_include_archive_navigation_affordance():
    for viewer_path in REPORT_VIEWERS:
        viewer = viewer_path.read_text()

        assert 'id="archive-link"' in viewer
        assert "resolveReportPath" in viewer
        assert "new URLSearchParams(window.location.search)" in viewer
        assert "requestedReport.startsWith('reports/')" in viewer
        assert "requestedReport.startsWith('docs/reports/')" in viewer
        assert "requestedReport.endsWith('.md')" in viewer
        assert "!requestedReport.includes('?')" in viewer
        assert "!requestedReport.includes('#')" in viewer
        assert "!requestedReport.includes('%')" in viewer
        assert "requestedReport.split('/')" in viewer
        assert "segment !== '..'" in viewer
        assert "return 'index.md'" in viewer
        assert "const reportPath = resolveReportPath()" in viewer
        assert "const isArchiveReport = reportPath !== 'index.md'" in viewer
        assert "if (!isArchiveReport)" in viewer
        assert "resolveArchiveLink" in viewer
        assert "reports/" in viewer
        assert "docs/reports/" in viewer
        assert "Promise.any" not in viewer
        assert "function probe(index)" in viewer
        assert "probe(index + 1)" in viewer
        assert "archiveLinkEl.hidden = false" in viewer
        assert "location.search" in viewer


def test_report_viewers_expose_loaded_markdown_action_link():
    for viewer_path in REPORT_VIEWERS:
        viewer = viewer_path.read_text()

        assert 'id="markdown-link"' in viewer
        assert 'href="index.md"' in viewer
        assert "Markdown" in viewer
        assert (
            "const markdownLinkEl = document.getElementById('markdown-link')" in viewer
        )
        assert "const reportPath = resolveReportPath()" in viewer
        assert "markdownLinkEl.href = reportPath" in viewer
        assert viewer.index("const reportPath = resolveReportPath()") < viewer.index(
            "markdownLinkEl.href = reportPath"
        )


def test_report_viewers_label_archived_report_metadata():
    for viewer_path in REPORT_VIEWERS:
        viewer = viewer_path.read_text()

        assert "renderReportMetadata" in viewer
        assert (
            "function renderReportMetadata(dateStr, archiveReport, fallbackDateStr = '')"
            in viewer
        )
        assert "Archived report" in viewer
        assert "Latest report" in viewer
        assert "metaEl.textContent = `Last updated:" not in viewer
        assert "const d = new Date()" not in viewer
        assert "dateStr || now" not in viewer
        assert "response.headers.get('Last-Modified') || ''" in viewer
        assert (
            "renderReportMetadata(m ? m[1] : '', isArchiveReport, lastModified)"
            in viewer
        )
        assert "fallbackDateStr ? new Date(fallbackDateStr) : null" in viewer


def test_report_viewers_reject_failed_markdown_fetches_before_rendering():
    for viewer_path in REPORT_VIEWERS:
        viewer = viewer_path.read_text()

        assert "if (!response.ok)" in viewer
        assert "Report fetch failed: ${response.status}" in viewer
        assert "return response.text().then(text => ({" in viewer
        assert "lastModified: response.headers.get('Last-Modified') || ''" in viewer
        assert "DOMPurify.sanitize(marked.parse(text))" in viewer


def test_report_viewers_render_load_error_details_as_text():
    for viewer_path in REPORT_VIEWERS:
        viewer = viewer_path.read_text()

        assert "function renderReportLoadError(error)" in viewer
        assert "contentEl.textContent = ''" in viewer
        assert "pre.textContent = String(error)" in viewer
        assert "renderReportLoadError(error)" in viewer
        assert "<pre>${error}</pre>" not in viewer


def test_report_viewers_reset_report_chrome_on_load_error():
    for viewer_path in REPORT_VIEWERS:
        viewer = viewer_path.read_text()

        assert "metaEl.textContent = 'Report unavailable'" in viewer
        assert "tocEl.textContent = ''" in viewer
        assert "execEl.textContent = ''" in viewer


def test_report_viewers_hide_report_navigation_on_load_error():
    for viewer_path in REPORT_VIEWERS:
        viewer = viewer_path.read_text()
        load_error_helper = viewer[
            viewer.index("function renderReportLoadError(error)") : viewer.index(
                "Promise.all([configPromise])"
            )
        ]
        success_path = viewer[
            viewer.index(".then(({ text, lastModified }) => {") : viewer.index(
                "markdownCache = text;"
            )
        ]

        assert ".layout.report-unavailable" in viewer
        assert ".layout.report-unavailable main" in viewer
        assert "const layoutEl = document.querySelector('.layout')" in viewer
        assert "const tocAsideEl = document.getElementById('toc')" in viewer
        assert "layoutEl.classList.add('report-unavailable')" in load_error_helper
        assert "tocAsideEl.classList.add('hidden')" in load_error_helper
        assert "layoutEl.classList.remove('report-unavailable')" in success_path
        assert "tocAsideEl.classList.remove('hidden')" in success_path


def test_report_archive_route_has_static_index():
    archive = ARCHIVE_INDEX.read_text()

    assert "Report Archive" in archive
    assert "../index.html" in archive
    assert "../index.html?report=reports/index.md" in archive
    assert "index.md" in archive
    assert 'id="archive-filter"' in archive
    assert (
        'id="archive-filter" type="search" autocomplete="off" aria-controls="archive-results"'
        in archive
    )
    assert 'aria-describedby="archive-count archive-filter-summary"' in archive
    assert 'id="archive-summary"' in archive
    assert 'href="#archive-summary"' in archive
    assert 'id="archive-count"' in archive
    assert (
        'id="archive-count" role="status" aria-live="polite" aria-atomic="true"'
        in archive
    )
    assert 'href="#archive-results"' in archive
    assert 'class="archive-results" id="archive-results"' in archive
    assert 'id="archive-empty"' in archive
    assert archive.index('id="archive-results"') < archive.index('id="archive-empty"')
    assert archive.index('id="archive-results"') < archive.index('id="archive-list"')
    assert "filterArchive" in archive
    assert "renderArchiveSummary" in archive
    assert "archiveSummaryEl.textContent" in archive
    assert "latestReport.archivedLabel" in archive
    assert "Latest archive:" in archive
    assert "latestArchiveLink.href = latestReport.href" in archive
    assert "latestArchiveLink.textContent = latestReport.archivedLabel" in archive
    assert "if (!latestReport)" in archive
    assert "No archived reports yet" in archive
    assert "dataset.search" in archive
    assert "archivedAt: '2026-06-23'" in archive
    assert "time.dateTime = report.archivedAt" in archive
    assert "Archived" in archive
    assert "sortNewestFirst" in archive
    assert 'id="archive-topic-filters"' in archive
    assert "filterArchiveByTopic" in archive
    assert "aria-pressed" in archive
    assert "button.setAttribute('aria-controls', 'archive-results')" in archive
    assert (
        "button.setAttribute('aria-describedby', 'archive-count archive-filter-summary')"
        in archive
    )
    assert 'id="archive-clear-filters"' in archive
    assert "clearArchiveFilters" in archive
    assert "archiveClearFiltersEl.disabled" in archive
    assert 'id="archive-empty-clear"' in archive
    assert (
        'id="archive-clear-filters" type="button" aria-controls="archive-results"'
        in archive
    )
    assert (
        'id="archive-empty-clear" type="button" aria-controls="archive-results"'
        in archive
    )
    assert (
        "archiveEmptyClearEl.addEventListener('click', clearArchiveFilters)" in archive
    )
    assert archive.count('aria-describedby="archive-count archive-filter-summary"') >= 3
    assert "archive-empty-clear archive-focus-target" in archive
    assert "const archiveReports = [" in archive
    assert "renderArchiveReports" in archive
    assert "renderArchiveTopicFilters" in archive
    assert "topicCounts" in archive
    assert "label.textContent = topic || 'All'" in archive
    assert "count.textContent = String(total)" in archive
    assert "count.setAttribute('aria-label'" not in archive
    assert "button.append(label, ' ', count)" in archive
    assert "createElement('article')" in archive
    assert "createElement('button')" in archive
    assert "archiveTagLabel.className = 'archive-tag-label'" in archive
    assert "archiveTagLabel.textContent = 'Topics'" in archive
    assert "tag.type = 'button'" in archive
    assert "tag.setAttribute('aria-controls', 'archive-results')" in archive
    assert (
        "tag.setAttribute('aria-describedby', 'archive-count archive-filter-summary')"
        in archive
    )
    assert "filterArchiveByTopic(topic)" in archive
    assert ".archive-focus-target:focus-visible" in archive
    assert "outline: 3px solid #2563eb" in archive
    assert "outline-offset: 3px" in archive
    assert "classList.add('archive-focus-target')" in archive
    assert "CVE-2025-5777" in archive
    assert "archiveEmptyEl.hidden = visible !== 0" in archive


def test_report_archive_filter_state_uses_canonical_query_params():
    archive = ARCHIVE_INDEX.read_text()

    assert "function readArchiveQueryState()" in archive
    assert "function writeArchiveQueryState()" in archive
    assert 'id="archive-filter-summary"' in archive
    assert (
        'id="archive-filter-summary" role="status" aria-live="polite" aria-atomic="true"'
        in archive
    )
    assert (
        "const archiveFilterSummaryEl = document.getElementById('archive-filter-summary')"
        in archive
    )
    assert "function renderArchiveFilterSummary(query, visible, total)" in archive
    assert "archiveFilterSummaryEl.textContent" in archive
    assert "Filtering by" in archive
    assert "Showing all archived reports." in archive
    assert "renderArchiveFilterSummary(query, visible, archiveItems.length)" in archive
    assert "new URLSearchParams(window.location.search)" in archive
    assert "params.get('q')" in archive
    assert "params.get('topic')" in archive
    assert "params.set('q', query)" in archive
    assert "params.set('topic', activeTopic)" in archive
    assert "history.replaceState" in archive
    assert "readArchiveQueryState()" in archive
    assert "writeArchiveQueryState()" in archive
    assert "archiveFilterEl.value = query" in archive
    assert "filterArchiveByTopic(topic, { syncQuery: false })" in archive
    assert "archiveFilterEl.addEventListener('input', () => filterArchive())" in archive


def test_report_archive_exposes_static_section_index():
    archive = ARCHIVE_INDEX.read_text()

    assert 'class="archive-section-index"' in archive
    assert 'aria-label="Archive sections"' in archive
    assert 'href="#archive-summary"' in archive
    assert 'href="#archive-filter-panel"' in archive
    assert 'href="#archive-results"' in archive
    assert 'id="archive-summary"' in archive
    assert 'id="archive-filter-panel"' in archive
    assert (
        'id="archive-filter-panel" role="region" '
        'aria-labelledby="archive-filter-title"' in archive
    )
    assert 'id="archive-filter-title" for="archive-filter"' in archive
    assert 'id="archive-results"' in archive
    assert (
        'class="archive-results" id="archive-results" role="region" '
        'aria-label="Available reports"' in archive
    )
    assert 'id="archive-list"' in archive
    assert "#archive-summary, #archive-filter-panel, #archive-results" in archive
    assert "scroll-margin-top: 32px" in archive
    assert "Latest" in archive
    assert "Filter" in archive
    assert "Reports" in archive
    assert ".archive-section-index" in archive
    assert ".archive-section-index a" in archive


def test_report_archive_entries_render_canonical_metric_chips():
    archive = ARCHIVE_INDEX.read_text()

    assert "metrics: {" in archive
    assert "sections: 6" in archive
    assert "topics: 4" in archive
    assert "uncertaintySignals: 1" in archive
    assert "function buildArchiveMetricChips(report)" in archive
    assert "Object.entries(report.metrics || {})" in archive
    assert "archive-metrics" in archive
    assert "archive-metric" in archive
    assert "archiveMetricLabels" in archive
    assert "Archive sections" in archive
    assert "Tracked topics" in archive
    assert "Uncertainty signals" in archive
    assert "article.appendChild(buildArchiveMetricChips(report))" in archive


def test_report_archive_entries_render_canonical_action_links():
    archive = ARCHIVE_INDEX.read_text()

    assert "links: {" in archive
    assert "report: '../index.html?report=reports/index.md'" in archive
    assert "markdown: 'index.md'" in archive
    assert "function buildArchiveActionLinks(report)" in archive
    assert "archive-actions" in archive
    assert "archive-action" in archive
    assert "Open report" in archive
    assert "Source markdown" in archive
    assert "action.href = href" in archive
    assert "article.appendChild(buildArchiveActionLinks(report))" in archive


def test_report_archive_entries_render_canonical_coverage_signals():
    archive = ARCHIVE_INDEX.read_text()

    assert "coverage: [" in archive
    assert "label: 'Source attribution'" in archive
    assert "label: 'Archived artifact'" in archive
    assert "function buildArchiveCoverageNotes(report)" in archive
    assert "archive-coverage" in archive
    assert "archive-coverage-note" in archive
    assert "Coverage" in archive
    assert "coverage.forEach" in archive
    assert "article.appendChild(buildArchiveCoverageNotes(report))" in archive


def test_report_archive_renders_derived_coverage_summary():
    archive = ARCHIVE_INDEX.read_text()

    assert 'id="archive-coverage-summary"' in archive
    assert "archiveCoverageSummaryEl" in archive
    assert "function renderArchiveCoverageSummary()" in archive
    assert (
        "archiveReports.reduce((total, report) => total + Object.keys(report.links || {}).length, 0)"
        in archive
    )
    assert "report.coverage || []" in archive
    assert "source attribution gap" in archive
    assert "archive artifacts tracked" in archive
    assert "renderArchiveCoverageSummary();" in archive


def test_report_archive_entries_render_artifact_rows_from_links():
    archive = ARCHIVE_INDEX.read_text()

    assert "function buildArchiveArtifactRows(report)" in archive
    assert "archive-artifacts" in archive
    assert "archive-artifact-table" in archive
    assert "archiveArtifactLabels" in archive
    assert "Object.entries(report.links || {})" in archive
    assert "Artifact" in archive
    assert "Path" in archive
    assert "Rendered report" in archive
    assert "Source markdown" in archive
    assert "article.appendChild(buildArchiveArtifactRows(report))" in archive


def test_report_viewers_omit_operator_metric_panels():
    """The viewer leads with the report itself; operator analytics panels
    (summary stat cards, provenance, uncertainty, coverage, section filter, and
    the reading-index nav) are not rendered before the content."""
    removed_markers = (
        'id="summary"',
        'id="provenance"',
        'id="uncertainty"',
        'id="coverage-notes"',
        'id="section-filter-panel"',
        'class="reading-index"',
        "CVEs Mentioned",
        "Report Provenance",
        "Uncertainty Signals",
        "Report Coverage",
        "function computeSummary()",
        "function renderProvenance()",
        "function renderUncertaintySignals()",
        "function renderCoverageNotes()",
        "function filterSections()",
    )
    for viewer_path in REPORT_VIEWERS:
        viewer = viewer_path.read_text()
        for marker in removed_markers:
            assert marker not in viewer, f"operator UI should be removed: {marker}"
        # The report content still leads the page.
        assert 'id="exec"' in viewer
        assert 'id="content"' in viewer
        assert "renderExecutiveSummary()" in viewer

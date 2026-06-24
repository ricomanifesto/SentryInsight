from pathlib import Path

REPORT_VIEWERS = (
    Path("index.html"),
    Path("docs/index.html"),
)
ARCHIVE_INDEX = Path("docs/reports/index.html")


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


def test_report_viewers_render_full_summary_cards():
    for viewer_path in REPORT_VIEWERS:
        viewer = viewer_path.read_text()

        assert (
            '<div class="meta" id="meta"></div>\n                <div id="summary" class="summary"></div>'
            in viewer
        )
        assert "CVEs Mentioned" in viewer
        assert "Active Items" in viewer
        assert "Affected Products" in viewer
        assert "Report Sections" in viewer


def test_report_viewers_include_section_filter_controls():
    for viewer_path in REPORT_VIEWERS:
        viewer = viewer_path.read_text()

        assert 'id="section-filter"' in viewer
        assert 'id="section-filter-count"' in viewer
        assert 'id="section-filter-empty"' in viewer
        assert "filterSections" in viewer
        assert "buildFilterGroups" in viewer
        assert "flushDirectGroup" in viewer
        assert "h2.report-filter-heading" in viewer
        assert "visibleHeadings" in viewer
        assert "visibleTocIds" in viewer
        assert "tocEl.querySelectorAll('a[href^=\"#\"]')" in viewer
        assert "contentEl.querySelectorAll('.section-collapsible')" in viewer
        assert "section-filter-hidden" in viewer
        assert "sectionFilterEl.addEventListener('input', filterSections)" in viewer


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


def test_report_viewers_label_archived_report_metadata():
    for viewer_path in REPORT_VIEWERS:
        viewer = viewer_path.read_text()

        assert "renderReportMetadata" in viewer
        assert "Archived report" in viewer
        assert "Latest report" in viewer
        assert "metaEl.textContent = `Last updated:" not in viewer


def test_report_archive_route_has_static_index():
    archive = ARCHIVE_INDEX.read_text()

    assert "Report Archive" in archive
    assert "../index.html" in archive
    assert "../index.html?report=reports/index.md" in archive
    assert "index.md" in archive
    assert 'id="archive-filter"' in archive
    assert 'id="archive-summary"' in archive
    assert 'id="archive-count"' in archive
    assert 'id="archive-empty"' in archive
    assert "filterArchive" in archive
    assert "renderArchiveSummary" in archive
    assert "archiveSummaryEl.textContent" in archive
    assert "latestReport.archivedLabel" in archive
    assert "Latest archive:" in archive
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
    assert 'id="archive-clear-filters"' in archive
    assert "clearArchiveFilters" in archive
    assert "archiveClearFiltersEl.disabled" in archive
    assert "const archiveReports = [" in archive
    assert "renderArchiveReports" in archive
    assert "renderArchiveTopicFilters" in archive
    assert "topicCounts" in archive
    assert "label.textContent = topic || 'All'" in archive
    assert "count.textContent = String(total)" in archive
    assert "createElement('article')" in archive
    assert "CVE-2025-5777" in archive
    assert "archiveEmptyEl.hidden = visible !== 0" in archive


def test_report_viewers_include_source_provenance_panel():
    for viewer_path in REPORT_VIEWERS:
        viewer = viewer_path.read_text()

        assert 'id="provenance"' in viewer
        assert "Report Provenance" in viewer
        assert "Source entries" in viewer
        assert "isPlaceholderSourceAttributionEntry" in viewer
        assert "no sources were provided" in viewer
        assert "article title: source name - url" in viewer
        assert "n/a" in viewer
        assert "extractSourceAttributionEntries" in viewer
        assert "renderProvenance" in viewer
        assert "renderSourcePreview" in viewer
        assert "source-preview" in viewer
        assert "sourcePreviewList" in viewer
        assert "entryEl.textContent = entry" in viewer
        assert "sourcePreviewList.innerHTML = ''" in viewer
        assert "findSourceAttributionHeading" in viewer
        assert "provenanceEl.hidden = true" in viewer
        assert "provenanceEl.hidden = false" in viewer


def test_report_viewers_include_uncertainty_signal_panel():
    for viewer_path in REPORT_VIEWERS:
        viewer = viewer_path.read_text()

        assert 'id="uncertainty"' in viewer
        assert "Uncertainty Signals" in viewer
        assert "countUncertaintySignals" in viewer
        assert "renderUncertaintySignals" in viewer
        assert "getVisibleReportText" in viewer
        assert "const textRoots = [execEl, contentEl]" in viewer
        assert "code, pre, script, style, noscript" in viewer
        assert "const reportText = getVisibleReportText()" in viewer
        assert "const reportText = contentEl.textContent || ''" not in viewer
        assert "markdownCache.match(/\\b(unknown|uncertain" not in viewer
        assert "uncertaintyEl.hidden = true" in viewer
        assert "uncertaintyEl.hidden = false" in viewer
        assert "unknown|uncertain|suspected|likely|possible|potential|could" in viewer
        assert "potential, or could" in viewer

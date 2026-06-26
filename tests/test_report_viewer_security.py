from pathlib import Path
import json
import subprocess
import textwrap

REPORT_VIEWERS = (
    Path("index.html"),
    Path("docs/index.html"),
)
ARCHIVE_INDEX = Path("docs/reports/index.html")


def extract_js_function(source, function_name):
    signature = f"function {function_name}"
    start = source.index(signature)
    body_start = source.index("{", start)
    depth = 0
    for index in range(body_start, len(source)):
        char = source[index]
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return source[start : index + 1]
    raise AssertionError(f"Could not extract {function_name}")


def run_source_attribution_parser(viewer):
    parser = extract_js_function(viewer, "parseSourceAttributionEntry")
    cases = [
        {
            "raw": "- **CISA: exploited KEV update**: Example Research - https://example.test/kev",
            "title": "CISA: exploited KEV update",
            "attribution": "Example Research - https://example.test/kev",
        },
        {
            "raw": "- **Parenthesized URL report**: Example Source - https://example.test/report(1)",
            "title": "Parenthesized URL report",
            "attribution": "Example Source - https://example.test/report(1)",
        },
        {
            "raw": "- **Critical **edge** [gateway] _update_ \\ <em>`advisory`</em> & ~~notes~~**: Vendor **Research** [Team] _analysis_ \\ <desk>`notes`</desk> & ~~feed~~ - https://example.test/report(1)",
            "title": "Critical **edge** [gateway] _update_ \\ <em>`advisory`</em> & ~~notes~~",
            "attribution": "Vendor **Research** [Team] _analysis_ \\ <desk>`notes`</desk> & ~~feed~~ - https://example.test/report(1)",
        },
    ]
    script = textwrap.dedent(f"""
        {parser}
        const cases = {json.dumps(cases)};
        process.stdout.write(JSON.stringify(cases.map(parseSourceAttributionEntry)));
        """)
    result = subprocess.run(
        ["node", "-e", script],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(result.stdout)


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
        assert (
            'id="section-filter-count" role="status" aria-live="polite" aria-atomic="true"'
            in viewer
        )
        assert 'id="section-filter-empty"' in viewer
        assert 'id="section-filter-clear-empty"' in viewer
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
        assert "sectionFilterClearEmptyEl.addEventListener('click'" in viewer
        assert "sectionFilterEl.value = ''" in viewer
        assert "sectionFilterEl.focus()" in viewer


def test_report_viewers_expose_static_reading_index():
    for viewer_path in REPORT_VIEWERS:
        viewer = viewer_path.read_text()

        assert 'class="reading-index"' in viewer
        assert 'aria-label="Report reading sections"' in viewer
        assert 'id="reading-index-sources"' in viewer
        assert 'id="reading-index-sources" hidden href="#provenance"' in viewer
        assert 'id="reading-index-uncertainty" hidden href="#uncertainty"' in viewer
        assert 'href="#provenance"' in viewer
        assert 'href="#uncertainty"' in viewer
        assert 'href="#coverage-notes"' in viewer
        assert 'href="#section-filter-panel"' in viewer
        assert 'href="#report-results"' in viewer
        assert 'id="section-filter-panel"' in viewer
        assert 'id="report-results"' in viewer
        assert 'aria-label="Report sections"' in viewer
        assert 'id="content"' in viewer
        assert viewer.index('id="report-results"') < viewer.index(
            'id="section-filter-empty"'
        )
        assert viewer.index('id="report-results"') < viewer.index('id="content"')
        assert 'id="provenance"' in viewer
        assert 'id="uncertainty"' in viewer
        assert 'id="coverage-notes"' in viewer
        assert (
            "#provenance, #uncertainty, #coverage-notes, #section-filter-panel, #report-results, #content"
            in viewer
        )
        assert "scroll-margin-top: 80px" in viewer
        assert (
            "const readingIndexSourceEl = document.getElementById('reading-index-sources')"
            in viewer
        )
        assert (
            "const readingIndexUncertaintyEl = document.getElementById('reading-index-uncertainty')"
            in viewer
        )
        assert "function syncReadingIndex()" in viewer
        assert "readingIndexSourceEl.hidden = provenanceEl.hidden" in viewer
        assert "readingIndexUncertaintyEl.hidden = uncertaintyEl.hidden" in viewer
        assert "syncReadingIndex()" in viewer
        assert ".reading-index" in viewer
        assert ".reading-index a" in viewer
        assert "Sources" in viewer
        assert "Uncertainty" in viewer
        assert "Coverage" in viewer
        assert "Filter" in viewer
        assert "Report" in viewer


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
        assert "summaryEl.textContent = ''" in viewer
        assert "tocEl.textContent = ''" in viewer
        assert "execEl.textContent = ''" in viewer
        assert "sectionFilterCountEl.textContent = ''" in viewer
        assert "sectionFilterEmptyEl.style.display = 'none'" in viewer
        assert "provenanceEl.hidden = true" in viewer
        assert "provenanceEl.textContent = ''" in viewer
        assert "uncertaintyEl.hidden = true" in viewer
        assert "uncertaintyEl.textContent = ''" in viewer
        assert "coverageNotesEl.hidden = true" in viewer
        assert "coverageNotesEl.textContent = ''" in viewer
        assert (
            "syncReadingIndex()"
            in viewer[
                viewer.index("function renderReportLoadError(error)") : viewer.index(
                    "Promise.all([configPromise])"
                )
            ]
        )


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
        assert ".reading-index[hidden]" in viewer
        assert (
            "const readingIndexEl = document.querySelector('.reading-index')" in viewer
        )
        assert (
            "const sectionFilterPanelEl = document.getElementById('section-filter-panel')"
            in viewer
        )
        assert "layoutEl.classList.add('report-unavailable')" in load_error_helper
        assert "tocAsideEl.classList.add('hidden')" in load_error_helper
        assert "readingIndexEl.hidden = true" in load_error_helper
        assert "sectionFilterPanelEl.hidden = true" in load_error_helper
        assert "sectionFilterEl.value = ''" in load_error_helper
        assert "layoutEl.classList.remove('report-unavailable')" in success_path
        assert "tocAsideEl.classList.remove('hidden')" in success_path
        assert "readingIndexEl.hidden = false" in success_path
        assert "sectionFilterPanelEl.hidden = false" in success_path


def test_report_archive_route_has_static_index():
    archive = ARCHIVE_INDEX.read_text()

    assert "Report Archive" in archive
    assert "../index.html" in archive
    assert "../index.html?report=reports/index.md" in archive
    assert "index.md" in archive
    assert 'id="archive-filter"' in archive
    assert 'id="archive-summary"' in archive
    assert 'href="#archive-summary"' in archive
    assert 'id="archive-count"' in archive
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
    assert 'id="archive-clear-filters"' in archive
    assert "clearArchiveFilters" in archive
    assert "archiveClearFiltersEl.disabled" in archive
    assert 'id="archive-empty-clear"' in archive
    assert (
        "archiveEmptyClearEl.addEventListener('click', clearArchiveFilters)" in archive
    )
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
    assert 'id="archive-results"' in archive
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


def test_report_viewers_render_source_entries_as_evidence_rows():
    for viewer_path in REPORT_VIEWERS:
        viewer = viewer_path.read_text()

        assert "function parseSourceAttributionEntry(entry)" in viewer
        assert "function renderSourceEvidenceRows(sourceEntries)" in viewer
        assert "const titleEl = li.querySelector('strong')" in viewer
        assert "entries.push({ raw, title, attribution })" in viewer
        assert "const titleFromMarkup = entry.title || ''" in viewer
        assert r"attribution.match(/\bhttps?:\/\/\S+/i)" in viewer
        assert r"replace(/[.,;]+$/, '')" in viewer
        assert "source-evidence-table" in viewer
        assert "source-evidence-row" in viewer
        assert "Source" in viewer
        assert "Evidence" in viewer
        assert "Link" in viewer
        assert "row.link ? 'Available' : 'Not provided'" in viewer
        assert "link.rel = 'noopener noreferrer'" in viewer
        assert "link.target = '_blank'" in viewer
        assert "raw," in viewer
        assert (
            "provenanceEl.appendChild(renderSourceEvidenceRows(sourceEntries))"
            in viewer
        )


def test_report_viewers_parse_source_entries_behaviorally():
    expected = [
        {
            "title": "CISA: exploited KEV update",
            "source": "Example Research",
            "link": "https://example.test/kev",
            "raw": "- **CISA: exploited KEV update**: Example Research - https://example.test/kev",
        },
        {
            "title": "Parenthesized URL report",
            "source": "Example Source",
            "link": "https://example.test/report(1)",
            "raw": "- **Parenthesized URL report**: Example Source - https://example.test/report(1)",
        },
        {
            "title": "Critical **edge** [gateway] _update_ \\ <em>`advisory`</em> & ~~notes~~",
            "source": "Vendor **Research** [Team] _analysis_ \\ <desk>`notes`</desk> & ~~feed~~",
            "link": "https://example.test/report(1)",
            "raw": "- **Critical **edge** [gateway] _update_ \\ <em>`advisory`</em> & ~~notes~~**: Vendor **Research** [Team] _analysis_ \\ <desk>`notes`</desk> & ~~feed~~ - https://example.test/report(1)",
        },
    ]
    for viewer_path in REPORT_VIEWERS:
        viewer = viewer_path.read_text()

        assert run_source_attribution_parser(viewer) == expected


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


def test_report_viewers_include_coverage_notes_panel():
    for viewer_path in REPORT_VIEWERS:
        viewer = viewer_path.read_text()

        assert 'id="coverage-notes"' in viewer
        assert "Report Coverage" in viewer
        assert "renderCoverageNotes" in viewer
        assert "buildCoverageNote" in viewer
        assert "buildCoverageSummaryChip" in viewer
        assert "coverage-summary" in viewer
        assert "coverage-chip" in viewer
        assert "chip.setAttribute('aria-label'" not in viewer
        assert "chip.append(valueEl, document.createTextNode(` ${label}`))" in viewer
        assert "coverageNotesEl.hidden = true" in viewer
        assert "coverageNotesEl.hidden = false" in viewer
        assert "const sections = buildFilterGroups().length" in viewer
        assert "extractSourceAttributionEntries().length" in viewer
        assert "countUncertaintySignals()" in viewer
        assert "Sections" in viewer
        assert "Sources" in viewer
        assert "Uncertainty" in viewer
        assert "Section index" in viewer
        assert "Source coverage" in viewer
        assert "Uncertainty coverage" in viewer
        assert "coverageNotesEl.append(heading, summary, list)" in viewer


def test_report_viewers_include_loaded_artifact_in_coverage_notes():
    for viewer_path in REPORT_VIEWERS:
        viewer = viewer_path.read_text()

        assert "Report artifact" in viewer
        assert "reportPath" in viewer
        assert "Loaded markdown artifact: ${reportPath}." in viewer
        assert (
            "buildCoverageNote('Report artifact', `Loaded markdown artifact: ${reportPath}.`)"
            in viewer
        )

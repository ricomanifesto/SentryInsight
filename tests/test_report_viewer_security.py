from pathlib import Path

REPORT_VIEWERS = (
    Path("index.html"),
    Path("docs/index.html"),
)


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

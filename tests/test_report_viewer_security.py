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

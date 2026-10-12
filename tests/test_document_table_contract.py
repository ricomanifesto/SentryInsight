"""DOM-owned cells are distinct facts; flattened text cannot invent columns."""

from dataclasses import asdict

import pytest

from src.core.finding_evidence import collect_finding_details
from src.core.finding_generation import compile_finding_records
from src.core.reporting import build_reporting_catalog
from src.services.article_content import extract_article_content
from test_finding_generation_pipeline import run_real_pipeline

MARKUP = (
    "<article><h2>CVE-2026-1234</h2><p>CVE-2026-1234 was exploited last year.</p>"
    "<p>The table shows affected and fixed versions.</p><table>"
    "<tr><th>Flaw</th><th>Product</th><th>Affected Versions</th><th>Fixed In</th></tr>"
    "<tr><td>CVE-2026-1234</td><td>Gateway</td><td>2.0 and earlier</td><td>2.1</td></tr>"
    "<tr><td>CVE-2026-5678</td><td>Storage</td><td>4.0</td><td>4.1</td></tr>"
    "</table></article>"
)


def article(structured=True):
    result = extract_article_content(MARKUP, "https://example.test/table")
    return dict(
        title="Example advisory",
        source="Publisher",
        link="https://example.test/table",
        content=result.text,
        content_kind="article",
        source_blocks=[asdict(b) for b in result.blocks] if structured else [],
    )


def test_selected_row_keeps_affected_fixed_and_other_identity_separate():
    item = next(iter(build_reporting_catalog([article()]).values()))
    details = collect_finding_details([item], ["CVE-2026-1234"])
    assert details.version_lines == ("Gateway 2.0 and earlier",)
    assert any("Fixed In: 2.1" in row for row in details.release_details)
    assert not any("Storage" in row or "4.1" in row for row in details.release_details)


def test_real_pipeline_preserves_column_labels_and_does_not_call_fixed_affected(
    monkeypatch, tmp_path
):
    result = run_real_pipeline(monkeypatch, tmp_path / "index.md", articles=[article()])
    assert result["status"] == "completed", result
    report = (tmp_path / "index.md").read_text()
    assert "**Affected Versions**: Gateway 2.0 and earlier" in report
    assert "Fixed In: 2.1" in report
    assert "Affected Versions**: Gateway 2.1" not in report


def test_flattened_table_rows_are_not_narrative_candidates():
    item = article()
    extracted = extract_article_content(
        MARKUP.replace(
            "2.0 and earlier", "2.0 through 2.3, 2.4 through 2.6, and 2.7 through 2.9"
        ),
        item["link"],
    )
    item.update(
        content=extracted.text, source_blocks=[asdict(b) for b in extracted.blocks]
    )
    catalog = build_reporting_catalog([item])
    records = compile_finding_records(catalog)
    row_texts = {
        block["text"] for block in item["source_blocks"] if block["kind"] == "table_row"
    }
    assert all(
        excerpt.text not in row_texts
        for record in records
        for excerpt in record.excerpts
    )
    assert any(
        "Fixed In: 2.1" in value
        for record in records
        for field, value in record.fields
        if field == "Release Details"
    )


def test_missing_table_metadata_cannot_guess_cells(monkeypatch, tmp_path):
    paths = [
        tmp_path / name
        for name in (
            "index.md",
            "index.html",
            "current-findings.json",
            ".sentryinsight-articles-fingerprint",
        )
    ]
    for path in paths:
        path.write_bytes(b"Previous validated bytes\n")
    result = run_real_pipeline(
        monkeypatch, paths[0], articles=[article(False)], expect_model_call=False
    )
    assert result["status"] == "failed"
    assert all(path.read_bytes() == b"Previous validated bytes\n" for path in paths)


@pytest.mark.parametrize(
    "column,value", [("Affected Versions", "9.0"), ("Fixed In", "9.1")]
)
def test_cell_mutation_is_rejected_at_source_boundary(column, value):
    item = article()
    header = next(b for b in item["source_blocks"] if b["header"])
    row = next(
        b for b in item["source_blocks"] if b["kind"] == "table_row" and not b["header"]
    )
    cells = list(row["cells"])
    cells[header["cells"].index(column)] = value
    row["cells"] = cells
    with pytest.raises(ValueError):
        build_reporting_catalog([item])


def test_row_heading_does_not_replace_column_heading():
    html = MARKUP.replace(
        "<td>CVE-2026-1234</td>", '<th scope="row">CVE-2026-1234</th>'
    )
    extracted = extract_article_content(html, "https://example.test/table")
    item = article()
    item.update(
        content=extracted.text, source_blocks=[asdict(b) for b in extracted.blocks]
    )
    row = next(b for b in extracted.blocks if b.cells and b.cells[0] == "CVE-2026-1234")
    assert row.header is False
    details = collect_finding_details(
        list(build_reporting_catalog([item]).values()), ["CVE-2026-1234"]
    )
    assert details.version_lines == ("Gateway 2.0 and earlier",)


def test_image_layout_table_has_no_release_semantics(monkeypatch, tmp_path):
    extracted = extract_article_content(
        '<article><p>Attackers are exploiting the appliance.</p><table><tr><td><img src="capture.png"></td></tr><tr><td>Login page image caption</td></tr></table></article>',
        "https://example.test/table",
    )
    item = article()
    item.update(
        content=extracted.text, source_blocks=[asdict(b) for b in extracted.blocks]
    )
    result = run_real_pipeline(monkeypatch, tmp_path / "index.md", articles=[item])
    assert result["status"] == "completed", result
    report = (tmp_path / "index.md").read_text()
    assert "**Release Details**" not in report
    assert "Affected Versions**: Not stated" in report

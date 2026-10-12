"""Restored row facts include attributed corrections, qualifiers and notes."""

from dataclasses import asdict
import re

import pytest

from src.core.finding_evidence import collect_finding_details, validate_finding_evidence
from src.core.finding_evidence import assess_exploitation
from src.core.reporting import build_reporting_catalog
from src.services.article_content import extract_article_content
from test_finding_generation_pipeline import run_real_pipeline

NOTE = "The advisory marks 2 of the 3 with an asterisk and describes them as newly added to the Known Exploited Vulnerabilities catalog. They were not in the catalog snapshot when the publisher checked at 18:05 UTC on October 8."
WIDER = "ExampleApp's own advisory gives a wider range than the joint advisory. It says versions from 2.0 through 2.8, but not including 2.9, are affected."
CONDITIONS = "Two flaws depend on a setting. The Server flaw works only when Feature Mode is turned on, and the vendor says turning it off is an alternative to upgrading. The ExampleDocs flaw applies when JWT is used, according to its advisory."


def article():
    html = (
        '<article><p>The advisory lists three known flaws that it says were successfully exploited.</p><table><tr><th>Flaw</th><th>Product</th><th>Affected Versions</th><th>Fixed In</th></tr><tr><th scope="row">CVE-2026-1234*</th><td>Vendor Server</td><td>1.0</td><td>1.1</td></tr><tr><th scope="row">CVE-2026-5678</th><td>ExampleDocs</td><td>3.0</td><td>3.1</td></tr><tr><th scope="row">CVE-2026-9012*</th><td>ExampleApp</td><td>Up to 1.5</td><td>2.9</td></tr></table>'
        + "".join(f"<p>{p}</p>" for p in (NOTE, WIDER, CONDITIONS))
        + "</article>"
    )
    result = extract_article_content(html, "https://example.test/rows")
    return dict(
        title="Advisory",
        source="Publisher",
        link="https://example.test/rows",
        content=result.text,
        content_kind="article",
        source_blocks=[asdict(b) for b in result.blocks],
    )


def test_product_row_reference_keeps_both_ranges_and_exclusion():
    source = next(iter(build_reporting_catalog([article()]).values()))
    details = collect_finding_details([source], ["CVE-2026-9012"])
    assert "ExampleApp Up to 1.5" in details.version_lines
    assert (
        "ExampleApp from 2.0 through 2.8, but not including 2.9"
        in details.version_lines
    )
    assert NOTE in details.source_constraints
    assert WIDER in details.source_constraints
    assert not any(
        "JWT" in text or "Feature Mode" in text for text in details.source_constraints
    )


def test_complete_row_constraints_reach_real_pipeline(monkeypatch, tmp_path):
    result = run_real_pipeline(monkeypatch, tmp_path / "index.md", articles=[article()])
    assert result["status"] == "completed", result
    report = (tmp_path / "index.md").read_text()
    assert NOTE in report and WIDER in report
    assert (
        "Feature Mode is turned on" in report
        and "turning it off is an alternative" in report
    )
    assert "when JWT is used" in report
    assert "**Exploitation Status**: observed" in report


@pytest.mark.parametrize(
    "before,after",
    [
        (NOTE, ""),
        ("but not including 2.9", ""),
        ("when JWT is used", "unconditionally"),
        ("turning it off is an alternative", "turning it on is required"),
    ],
)
def test_row_constraint_tampering_is_rejected(monkeypatch, tmp_path, before, after):
    result = run_real_pipeline(monkeypatch, tmp_path / "index.md", articles=[article()])
    assert result["status"] == "completed", result
    report = (tmp_path / "index.md").read_text()
    assert before in report
    catalog = build_reporting_catalog([article()])
    # This validator runs before citation rendering in the real graph. Restore
    # only that phase's closed reporting key, then prove baseline acceptance.
    report = re.sub(
        r"(?m)^- \*\*Reporting\*\*:.*$",
        "- **Reporting**: " + next(iter(catalog)),
        report,
    )
    validate_finding_evidence(report, catalog)
    with pytest.raises(ValueError) as error:
        validate_finding_evidence(report.replace(before, after), catalog)
    assert error.value.code == "source_constraints_not_grounded"


def test_product_reference_cannot_hide_contrary_exploitation_or_unsupported_advice(
    monkeypatch, tmp_path
):
    item = article()
    item["content"] += "\n\nThe ExampleApp flaw has not been exploited."
    item["source_blocks"] = []
    # Re-extract a small DOM source so the explicit row and contrary clause
    # share verified structure, rather than inventing a text-only table.
    html = "<article><p>The advisory lists one known flaws that it says were successfully exploited.</p><table><tr><th>Flaw</th><th>Product</th></tr><tr><td>CVE-2026-9012</td><td>ExampleApp</td></tr></table><p>The ExampleApp flaw has not been exploited.</p></article>"
    extracted = extract_article_content(html, item["link"])
    item.update(
        content=extracted.text, source_blocks=[asdict(b) for b in extracted.blocks]
    )
    assessment = assess_exploitation(
        list(build_reporting_catalog([item]).values()), ["CVE-2026-9012"]
    )
    assert assessment.conflicting and assessment.status == "unknown"


def test_unique_product_component_binds_each_constraint_to_its_own_row():
    item = article()
    # A published product can have multiple words while its local explicit
    # reference uses its unique brand. Neither adjoining clause owns the other.
    source_html = "<article><p>The advisory lists two known flaws that it says were successfully exploited.</p><table><tr><th>Flaw</th><th>Product</th></tr><tr><td>CVE-2026-1234</td><td>Vendor Server</td></tr><tr><td>CVE-2026-5678</td><td>ExampleDocs Document Server</td></tr></table><p>The Vendor Server flaw requires Feature Mode. The ExampleDocs flaw applies when JWT is used, according to its advisory.</p></article>"
    extracted = extract_article_content(source_html, item["link"])
    item.update(
        content=extracted.text, source_blocks=[asdict(b) for b in extracted.blocks]
    )
    source = next(iter(build_reporting_catalog([item]).values()))
    first = collect_finding_details([source], ["CVE-2026-1234"])
    second = collect_finding_details([source], ["CVE-2026-5678"])
    assert first.source_constraints == (
        "The Vendor Server flaw requires Feature Mode.",
    )
    assert second.source_constraints == (
        "The ExampleDocs flaw applies when JWT is used, according to its advisory.",
    )


def test_nonunique_product_component_fails_before_transport(monkeypatch, tmp_path):
    item = article()
    html = "<article><p>The advisory lists two known flaws that it says were successfully exploited.</p><table><tr><th>Flaw</th><th>Product</th></tr><tr><td>CVE-2026-1234</td><td>Example Server</td></tr><tr><td>CVE-2026-5678</td><td>Example Gateway</td></tr></table><p>The Example flaw requires Feature Mode.</p></article>"
    extracted = extract_article_content(html, item["link"])
    item.update(
        content=extracted.text, source_blocks=[asdict(b) for b in extracted.blocks]
    )
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
        path.write_bytes(b"Prior validated artifact")
    result = run_real_pipeline(
        monkeypatch, paths[0], articles=[item], expect_model_call=False
    )
    assert (
        result["status"] == "failed"
        and result["analysis_results"]["error"] == "unsupported_evidence_relation"
    )
    assert all(path.read_bytes() == b"Prior validated artifact" for path in paths)

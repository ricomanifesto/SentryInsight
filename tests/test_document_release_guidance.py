"""DOM lists own release destinations, version audiences and conditions."""

import pytest
from src.core.finding_evidence import collect_finding_details
from src.core.reporting import build_reporting_catalog
from src.services.article_content import article_blocks
from test_composed_document_pipeline_contract import article
from test_finding_generation_pipeline import run_real_pipeline


@pytest.mark.parametrize("negative,action", [("", "patch"), ("not ", "none")])
def test_forward_release_list_is_guidance_not_affected_versions(
    monkeypatch, tmp_path, negative, action
):
    item = article(
        f"<h2>CVE-2026-1234</h2><p>CVE-2026-1234 exploitation status is unknown.</p><p>Example advised customers {negative}to upgrade vulnerable Example ADC and Example Gateway appliances to:</p><ul><li>Example ADC and Example Gateway 14.1-73.46 and later</li><li>Example ADC 13.1-FIPS 13.1.37.283 and later releases of 13.1-FIPS</li></ul>"
    )
    result = run_real_pipeline(monkeypatch, tmp_path / "index.md", articles=[item])
    assert result["status"] == "completed", result
    text = (tmp_path / "index.md").read_text()
    assert f"**Action**: {action}" in text
    assert "**Affected Versions**: Not stated in supplied sources." in text
    assert f"Example advised customers {negative}to upgrade" in text
    assert (
        "14.1-73.46 and later" in text
        and "13.1.37.283 and later releases of 13.1-FIPS" in text
    )


def test_nested_condition_versions_retain_dom_children_and_full_qualified_ranges(
    monkeypatch, tmp_path
):
    item = article(
        "<h2>CVE-2026-1234</h2><p>CVE-2026-1234 exploitation status is unknown.</p><p>The issue impacts the following versions -</p><ul><li>When configured as a SAML IdP -<ul><li>Example ADC between 14.1-73.37 and 14.1-73.41, inclusive</li><li>Example ADC 13.1-FIPS before 13.1-37.279</li></ul></li></ul><p>Users should install the patch.</p>"
    )
    parent = next(
        b
        for b in article_blocks(item["source_blocks"], item["content"])
        if b.kind == "list_item"
    )
    assert len(parent.children) == 2
    source = next(iter(build_reporting_catalog([item]).values()))
    details = collect_finding_details([source], ["CVE-2026-1234"])
    assert len(details.version_lines) == 2
    assert len(details.release_details) == 2 and all(
        "Condition: When configured as a SAML IdP" in line
        for line in details.release_details
    )
    result = run_real_pipeline(monkeypatch, tmp_path / "index.md", articles=[item])
    assert result["status"] == "completed", result
    text = (tmp_path / "index.md").read_text()
    assert "14.1-73.41, inclusive" in text and "13.1-37.279" in text


@pytest.mark.parametrize(
    "prefix,body",
    [
        (
            "Example 11, version 24H2 and Example Server 2025",
            "Install the September 2025 security update or later before June 19, 2027.",
        ),
        (
            "Other supported versions of Example 11, Example Server 2022, and Example 10",
            "Install the July 2026 security update or later before June 19, 2027.",
        ),
    ],
)
def test_version_audience_row_keeps_full_guidance_and_deadline(
    monkeypatch, tmp_path, prefix, body
):
    item = article(
        f"<p>Exploitation status is unknown.</p><p>Example shared the following detailed guidance on the required actions by Example version:</p><ul><li>{prefix}: {body}</li></ul>"
    )
    details = collect_finding_details(
        list(build_reporting_catalog([item]).values()), []
    )
    assert any(
        c.subject == prefix and c.conditions
        for b in details.recommendation_blocks
        for d in b.directives
        for c in getattr(d, "clauses", ())
    )
    result = run_real_pipeline(monkeypatch, tmp_path / "index.md", articles=[item])
    assert result["status"] == "completed", result
    text = (tmp_path / "index.md").read_text()
    assert prefix + ": " + body in text and "**Action**: none" in text
    assert "**Affected Versions**: Not stated in supplied sources." in text


@pytest.mark.parametrize(
    "boundary",
    ["<h2>Different product</h2>", "<p>Unclassified intervening advice.</p>"],
)
def test_forward_release_reference_cannot_cross_unknown_boundary(
    monkeypatch, tmp_path, boundary
):
    item = article(
        "<h2>CVE-2026-1234</h2><p>CVE-2026-1234 exploitation status is unknown.</p><p>Example advised customers to upgrade vulnerable Example appliances to:</p>"
        + boundary
        + "<ul><li>Example 2.0 and later</li></ul>"
    )
    paths = [
        tmp_path / n
        for n in (
            "index.md",
            "index.html",
            "current-findings.json",
            ".sentryinsight-articles-fingerprint",
        )
    ]
    for p in paths:
        p.write_bytes(b"Prior validated artifact")
    result = run_real_pipeline(
        monkeypatch, paths[0], articles=[item], expect_model_call=False
    )
    assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
    assert all(p.read_bytes() == b"Prior validated artifact" for p in paths)

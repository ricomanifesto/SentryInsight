"""A nominal identity declaration owns its product section, not later stories."""

from src.core.finding_evidence import collect_finding_details, assess_exploitation
from src.core.reporting import build_reporting_catalog
from test_composed_document_pipeline_contract import article
from test_finding_generation_pipeline import run_real_pipeline


def fixture():
    return article(
        "<h2>Gateway advisory</h2><p>CVE-2026-1234 is a vulnerability in Example Gateway.</p><p>CVE-2026-1234 was exploited last year.</p><h3>Response</h3><p>Users should install the patch.</p><h2>Unrelated storage context</h2><p>Users should monitor logs.</p><p>CVE-2026-1234 exploitation has not been observed.</p>"
    )


def test_identity_section_closes_at_peer_heading_without_losing_explicit_contrary_evidence():
    item = fixture()
    source = next(iter(build_reporting_catalog([item]).values()))
    details = collect_finding_details([source], ["CVE-2026-1234"])
    assert (
        "Users should install the patch."
        in details.field_evidence["Recommended Actions"]
    )
    assert (
        "Users should monitor logs."
        not in details.field_evidence["Recommended Actions"]
    )
    assessment = assess_exploitation([source], ["CVE-2026-1234"])
    assert assessment.conflicting and assessment.status == "unknown"
    assert "Users should monitor logs." in source.content


def test_real_pipeline_retains_owned_guidance_and_contrary_scope_after_boundary(
    monkeypatch, tmp_path
):
    result = run_real_pipeline(monkeypatch, tmp_path / "index.md", articles=[fixture()])
    assert result["status"] == "completed", result
    text = (tmp_path / "index.md").read_text()
    assert "**Recommended Actions**: Users should install the patch." in text
    assert "Users should monitor logs." not in text
    assert "exploitation has not been observed" in text and "conflict" in text

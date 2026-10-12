"""Canonical guidance retains block ownership through single-line serialization."""

import pytest
from src.core.finding_evidence import EvidenceError, validate_finding_evidence
from src.core.reporting import build_reporting_catalog
from src.core.finding_generation import compile_finding_records, _finding
from test_composed_document_pipeline_contract import article
from test_finding_generation_pipeline import run_real_pipeline


def fixture():
    return article(
        '<h2>CVE-2026-1234</h2><p>"We strongly urge affected customers to install the patch," the company said. "As of the publication of the bulletin, Example is not aware of any unmitigated exploits of this vulnerability."</p><p>Example advised customers to upgrade vulnerable Example appliances to:</p><ul><li>Example 2.0 and later</li><li>Example 3.0 and later</li></ul><p>"Private Access deployments using Example instances are also affected by the vulnerability," Example warned. "Customers need to upgrade these Example instances to the recommended Example versions to address the vulnerability."</p>'
    )


def test_guidance_serialization_retains_negative_assertion_and_list_ownership(
    monkeypatch, tmp_path
):
    result = run_real_pipeline(monkeypatch, tmp_path / "index.md", articles=[fixture()])
    assert result["status"] == "completed", result
    report = (tmp_path / "index.md").read_text()
    assert "**Exploitation Status**: not_observed" in report
    assert "As of the publication of the bulletin" in report
    assert "Private Access deployments" in report and "Example 3.0 and later" in report


def test_rollup_keeps_quoted_guidance_and_release_values_in_separate_owned_blocks(
    monkeypatch, tmp_path
):
    quote = '"We strongly urge affected customers to review the advisory and upgrade impacted Example instances to the recommended versions as soon as possible," the company said. "As of the publication of the bulletin, Example is not aware of any unmitigated exploits of this vulnerability."'
    item = article(
        f"<h2>CVE-2026-1234</h2><p>{quote}</p><p>Affected versions: Example 2.0, 3.0 and 4.0.</p>"
    )
    result = run_real_pipeline(monkeypatch, tmp_path / "index.md", articles=[item])
    assert result["status"] == "completed", result["analysis_results"].get("error")
    report = (tmp_path / "index.md").read_text()
    systems = report.split("## Affected Systems and Products", 1)[1].split(
        "## Attack Vectors", 1
    )[0]
    assert quote in systems and "Affected Versions: Example 2.0" in systems


@pytest.mark.parametrize(
    "old,new",
    [
        ("is not aware of any unmitigated exploits", "is aware of active exploits"),
        ("Example 3.0 and later", "Example 3.0"),
        ("are also affected", "are not affected"),
    ],
)
def test_source_owned_guidance_cannot_hide_semantic_tampering(old, new):
    catalog = build_reporting_catalog([fixture()])
    (record,) = compile_finding_records(catalog, ["CVE-2026-1234"])
    original = "## Active Exploitation Details\n\n" + _finding(record)
    validate_finding_evidence(original, catalog)
    lines = original.splitlines()
    changed = "\n".join(
        line.replace(old, new) if "**Recommended Actions**:" in line else line
        for line in lines
    )
    assert changed != original.rstrip("\n")
    with pytest.raises(EvidenceError):
        validate_finding_evidence(changed, catalog)

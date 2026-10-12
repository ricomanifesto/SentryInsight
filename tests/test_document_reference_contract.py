"""References own local scope; body text and row identities cannot be discarded."""

import pytest

from src.core.finding_evidence import (
    assess_exploitation,
    collect_finding_details,
    source_evidence_text,
)
from src.core.source_document import source_document
from test_source_document_contract import source


@pytest.mark.parametrize(
    "state,expected",
    [
        ("was exploited last year", "observed"),
        ("is actively exploited", "active"),
        ("has not been exploited", "not_observed"),
        ("may be exploited", "potential"),
    ],
)
def test_single_local_reference_owns_event_without_borrowing_other_section(
    state, expected
):
    item = source(
        f"<article><h2>Gateway incident</h2><p>CVE-2026-1234 is a Gateway flaw.</p><p>The flaw {state}.</p><h2>Storage incident</h2><p>CVE-2026-5678 is a Storage flaw.</p><p>The flaw is actively exploited.</p></article>"
    )
    result = assess_exploitation([item], ["CVE-2026-1234"])
    assert result.status == expected and not result.unsupported
    assert f"The flaw {state}." in source_evidence_text([item], ["CVE-2026-1234"])
    assert assess_exploitation([item], ["CVE-2026-5678"]).status == "active"


def test_story_boundary_does_not_inherit_antecedent():
    item = source(
        "<article><h2>Gateway incident</h2><p>CVE-2026-1234 is a Gateway flaw.</p><h2>Other story</h2><p>The flaw is actively exploited.</p></article>"
    )
    assert assess_exploitation([item], ["CVE-2026-1234"]).status == "unknown"


def test_ambiguous_singular_reference_is_not_distributed_to_joint_owners():
    item = source(
        "<article><p>CVE-2026-1234 and CVE-2026-5678 are Gateway flaws.</p><p>The flaw is actively exploited.</p></article>"
    )
    result = assess_exploitation([item], ["CVE-2026-1234", "CVE-2026-5678"])
    assert result.unsupported


def test_explicit_list_group_reference_preserves_all_negative_owners():
    item = source(
        "<article><p>All three vulnerabilities require a feature to be active:</p><ul><li>CVE-2026-1234: Gateway flaw.</li><li>CVE-2026-5678 and CVE-2026-9012: Gateway flaws.</li></ul><p>All three vulnerabilities have not been exploited.</p><p>Users should install the patch.</p><h2>Other product</h2><p>CVE-2026-1111 is actively exploited.</p></article>"
    )
    spans = source_document(item).spans
    reference = next(
        s for s in spans if s.text.startswith("All three vulnerabilities have")
    )
    assert set(reference.reference) == {
        "CVE-2026-1234",
        "CVE-2026-5678",
        "CVE-2026-9012",
    }
    result = assess_exploitation(
        [item], ["CVE-2026-1234", "CVE-2026-5678", "CVE-2026-9012"]
    )
    assert result.status == "not_observed" and not result.unsupported
    assert any(set(c.cves) == set(reference.reference) for c in result.relations)
    details = collect_finding_details([item], reference.reference)
    assert (
        "Users should install the patch."
        in details.field_evidence["Recommended Actions"]
    )


def test_mismatched_declared_group_count_fails_closed():
    item = source(
        "<article><p>All three vulnerabilities require a feature to be active:</p><ul><li>CVE-2026-1234: Gateway flaw.</li><li>CVE-2026-5678: Gateway flaw.</li></ul><p>All three vulnerabilities have not been exploited.</p></article>"
    )
    assert assess_exploitation([item], ["CVE-2026-1234", "CVE-2026-5678"]).unsupported


def test_table_exhaustive_exploitation_reference_is_distributive_with_attribution():
    text = (
        "The advisory lists two known flaws that it says were successfully exploited."
    )
    item = source(
        f"<article><p>{text}</p><table><tr><th>Flaw</th><th>Product</th></tr><tr><td>CVE-2026-1234</td><td>Gateway</td></tr><tr><td>CVE-2026-5678</td><td>Storage</td></tr></table></article>"
    )
    for identity in ("CVE-2026-1234", "CVE-2026-5678"):
        result = assess_exploitation([item], [identity])
        assert result.status == "observed" and not result.unsupported
        assert text in source_evidence_text([item], [identity])
        assert all(c.cves == (identity,) for c in result.relations)


def test_declared_table_count_mismatch_does_not_invent_missing_rows():
    item = source(
        "<article><p>The advisory lists two known flaws that it says were successfully exploited.</p><table><tr><th>Flaw</th><th>Product</th></tr><tr><td>CVE-2026-1234</td><td>Gateway</td></tr></table></article>"
    )
    assert assess_exploitation([item], ["CVE-2026-1234"]).unsupported


def test_local_identity_topic_preserves_details_and_ends_at_next_story():
    item = source(
        "<article><h2>Gateway flaw</h2><p>Tracked as CVE-2026-1234, this flaw allows data access.</p><p>The vulnerability has a CVSS score of 9.5.</p><p>Affected versions: Gateway 2.0 and earlier.</p><p>Users should install the patch.</p><h2>Other incident</h2><p>CVE-2026-5678 is a Storage flaw.</p><p>Affected versions: Storage 4.0.</p><p>Users must not install the patch.</p></article>"
    )
    details = collect_finding_details([item], ["CVE-2026-1234"])
    assert details.version_lines == ("Gateway 2.0 and earlier",)
    assert "CVSS score of 9.5" in details.scoped
    assert (
        "Users should install the patch."
        in details.field_evidence["Recommended Actions"]
    )
    assert "must not" not in details.scoped and "Storage" not in details.scoped


def test_table_does_not_lend_last_row_identity_to_unrelated_next_paragraph():
    item = source(
        "<article><p>The advisory lists two known flaws that it says were successfully exploited.</p><table><tr><th>Flaw</th><th>Product</th></tr><tr><td>CVE-2026-1234</td><td>Gateway</td></tr><tr><td>CVE-2026-5678</td><td>Storage</td></tr></table><p>Users should install mystery artifacts.</p></article>"
    )
    spans = source_document(item).spans
    assert not spans[-1].section and not spans[-1].reference


def test_shared_reference_owner_reaches_full_renderer_and_supported_severity(
    monkeypatch, tmp_path
):
    from test_composed_document_pipeline_contract import article
    from test_finding_generation_pipeline import run_real_pipeline

    markup = "<h2>Gateway flaw</h2><p>Tracked as CVE-2026-1234, this flaw allows data access.</p><p>The flaw was exploited last year. It carries a CVSS score of 9.5.</p><p>Users should install the patch.</p>"
    result = run_real_pipeline(
        monkeypatch, tmp_path / "index.md", articles=[article(markup)]
    )
    assert result["status"] == "completed", result
    report = (tmp_path / "index.md").read_text()
    assert "**Severity**: critical" in report
    assert "**Exploitation Status**: observed" in report
    assert "**Action**: patch" in report
    assert "The flaw was exploited last year." in report

"""Actual nested heading structure isolates factual prose from story furniture."""

from src.core.finding_evidence import assess_exploitation, source_evidence_text
from src.core.source_document import source_document
from test_source_document_contract import source


def test_nested_story_heading_and_prefix_remain_context():
    event = "A file upload vulnerability has been weaponized to compromise three servers by adding a new account, using it to upload web shells, and ultimately stealing payment data."
    item = source(
        f'<article><ol><li><div><span>File upload flaw</span><div role="heading" aria-level="3">A separate headline about exploitation</div><p>{event}</p></div></li></ol></article>'
    )
    document = source_document(item)
    assert any(
        s.kind == "heading" and s.text == "A separate headline about exploitation"
        for s in document.spans
    )
    assert any(
        s.role == "context" and s.text == "File upload flaw" for s in document.spans
    )
    assert any(s.role == "body" and s.text == event for s in document.spans)
    assert "File upload flaw" in document.text
    assessment = assess_exploitation([item], [])
    assert assessment.status == "observed" and not assessment.unsupported
    assert event in source_evidence_text([item], [])
    assert "separate headline" not in source_evidence_text([item], [])


def test_compound_product_subject_does_not_split_joint_completed_onset():
    event = "The development comes as three different flaws in Gateway ADC and Gateway Access appliances (CVE 2026-1234, CVE 2026-5678, and CVE 2026-9012) have come under active exploitation in the wild."
    item = source(f"<article><p>{event}</p></article>")
    result = assess_exploitation(
        [item], ["CVE-2026-1234", "CVE-2026-5678", "CVE-2026-9012"]
    )
    assert result.status == "observed" and not result.unsupported
    assert len(result.relations) == 1
    assert event in source_evidence_text([item], ["CVE-2026-1234"])


def test_completed_onset_cannot_swallow_new_residual_predicate():
    event = "The development comes as three different flaws in Gateway ADC and Gateway Access appliances (CVE 2026-1234, CVE 2026-5678, and CVE 2026-9012) have come under active exploitation in the wild, and attackers will be exploiting CVE-2026-1234."
    item = source(f"<article><p>{event}</p></article>")
    result = assess_exploitation(
        [item], ["CVE-2026-1234", "CVE-2026-5678", "CVE-2026-9012"]
    )
    assert result.unsupported

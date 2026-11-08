"""The per-source evidence table and the CVE-scope filters that read it."""

import uuid

import pytest

from src.core import finding_evidence as evidence_module
from src.core.finding_evidence import (
    EvidenceError,
    _partition_detail_spans,
    source_evidence,
)

A, B = "CVE-2026-1001", "CVE-2026-1002"


def _unique(content: str) -> str:
    # Tables are cached per exact content; a fresh body is derived from scratch.
    return f"{content}\n\nReference {uuid.uuid4().hex}.\n"


def test_rows_carry_the_scope_independent_columns():
    content = (
        "# Advisory\n\n"
        f"Microsoft fixed {A} and {B} in one release.\n\n"
        f"## {A}\n\n"
        "Customers should install the update.\n"
        "The fix ships in build 7.\n\n"
        f"## {B}\n\n"
        f"- {B} is not exploited.\n"
    )
    table = source_evidence(content)

    assert table.cves == (A, B)
    assert table.has_cve_sections
    assert table.joint_scopes == ((A, B),)
    assert [text for text, _ in table.sentences][:1] == [
        f"Microsoft fixed {A} and {B} in one release."
    ]

    rows = {row.span.text: row for row in table.spans}
    assert rows["Advisory"].span.role == "heading"
    assert rows["Advisory"].owner == frozenset()
    assert rows[A].owner == {A}
    joint = rows[f"Microsoft fixed {A} and {B} in one release."]
    assert (joint.owner, joint.cves) == (frozenset(), {A, B})
    advice = rows["Customers should install the update."]
    assert advice.owner == {A}
    assert advice.cves == frozenset()
    assert "Recommended Actions" in advice.span.fields
    # The recommendation cue belongs to the whole paragraph.
    assert "Recommended Actions" in rows["The fix ships in build 7."].span.fields
    assert advice.span.source_block == (
        "Customers should install the update.\nThe fix ships in build 7."
    )
    listed = rows[f"{B} is not exploited."]
    assert (listed.owner, listed.cves, listed.block_cves) == ({B}, {B}, {B})
    assert all(row.role_error is None for row in table.spans)


def test_an_unowned_complete_assertion_records_its_cves():
    table = source_evidence(
        f"{A} affects widget v2.\n\n{B} affects widget v3 and more."
    )
    first, second = table.spans
    assert first.foreign_assertion == {A}
    # Text beyond the assertion grammar cannot certify foreign ownership.
    assert second.foreign_assertion is None


def test_every_scope_filters_the_same_rows(monkeypatch):
    content = _unique(
        f"## {A}\n\nCustomers should install the update.\n\n"
        f"## {B}\n\nVersions affected: widget 2.1 and 2.2.\n"
    )
    calls = []
    original = evidence_module._detail_roles

    def counted(text, context=""):
        calls.append(text)
        return original(text, context)

    monkeypatch.setattr(evidence_module, "_detail_roles", counted)
    for cves in ([], [A], [B], [A, B]):
        _partition_detail_spans({"content": content}, cves)

    body_rows = [
        row for row in source_evidence(content).spans if row.span.role == "body"
    ]
    assert sorted(calls) == sorted(row.span.text for row in body_rows)
    assert source_evidence(content) is source_evidence(content)


def test_a_scope_filter_raises_in_the_same_order_as_a_sequential_scan(monkeypatch):
    content = _unique(
        f"## {A}\n\n"
        f"Customers should install the update. This also fixes {B}.\n\n"
        "Poison sentence.\n"
    )
    original = evidence_module._detail_roles

    def poisoned(text, context=""):
        if text.startswith("Poison"):
            raise EvidenceError(
                "ambiguous affected-version polarity",
                code="ambiguous_affected_version_polarity",
                field="Affected Versions",
            )
        return original(text, context)

    monkeypatch.setattr(evidence_module, "_detail_roles", poisoned)
    rows = source_evidence(content).spans
    assert rows[-1].span.text == "Poison sentence."
    assert rows[-1].role_error is not None  # nothing after it is derived

    # Scope A selects the section's advice first, whose paragraph also names B.
    with pytest.raises(EvidenceError) as first:
        _partition_detail_spans({"content": content}, [A])
    assert first.value.code == "ambiguous_recommendation_scope"

    # Scope B selects only its own sentence, so the scan reaches the rejection.
    raised = []
    for _ in range(2):
        with pytest.raises(EvidenceError) as rejected:
            _partition_detail_spans({"content": content}, [B])
        raised.append(rejected.value)
    assert {error.code for error in raised} == {"ambiguous_affected_version_polarity"}
    assert raised[0] is not raised[1] is not rows[-1].role_error


def test_a_recorded_rejection_keeps_no_caller_frames(monkeypatch):
    content = _unique("Poison sentence.")
    original = evidence_module._detail_roles

    def poisoned(text, context=""):
        if text.startswith("Poison"):
            raise EvidenceError("rejected", code="ambiguous_affected_version_polarity")
        return original(text, context)

    monkeypatch.setattr(evidence_module, "_detail_roles", poisoned)
    try:
        raise RuntimeError("unrelated failure being handled")
    except RuntimeError:
        rows = source_evidence(content).spans
    stored = rows[0].role_error
    assert stored is not None
    assert (stored.__traceback__, stored.__context__, stored.__cause__) == (None,) * 3

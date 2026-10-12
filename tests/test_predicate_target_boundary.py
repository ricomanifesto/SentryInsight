"""Predicate, target and coordination consume one shared finite frame."""

import pytest

from src.core import assertions
from src.core.finding_evidence import EvidenceError, validate_finding_evidence
from test_assertion_subject_contract import publish, rejected
from test_finding_generation import catalog_for, render

A, B = "CVE-2026-1234", "CVE-2026-5678"


@pytest.mark.parametrize(
    "text,voice,operator,event,target,adjunct,tense,aspect",
    [
        (
            f"are actively exploiting {A} and {B} in the wild",
            "actor",
            "are actively",
            "exploiting",
            f"{A} and {B}",
            "in the wild",
            "current",
            "simple",
        ),
        (
            f"continued to exploit {A}, {B} yesterday",
            "actor",
            "continued to",
            "exploit",
            f"{A}, {B}",
            "yesterday",
            "past",
            "continuative",
        ),
        (
            "continues to be actively exploited in the wild",
            "vulnerability",
            "continues to be actively",
            "exploited",
            "",
            "in the wild",
            "current",
            "continuative",
        ),
        (
            "continue to exploit the gateway",
            "actor",
            "continue to",
            "exploit",
            "the gateway",
            "",
            "current",
            "continuative",
        ),
    ],
)
def test_one_frame_owns_exact_nonoverlapping_spans(
    text, voice, operator, event, target, adjunct, tense, aspect
):
    frame = assertions.bind_predicate(text, voice=voice)
    assert frame.supported and frame.end == len(text)
    assert frame.text == text and frame.tense == tense and frame.aspect == aspect
    assert text[slice(*frame.operator_span)] == operator
    assert text[slice(*frame.event_span)] == event
    assert text[slice(*frame.adjunct_span)] == adjunct
    assert frame.target.text == target
    assert text[frame.target.start : frame.target.end] == target
    spans = [
        frame.operator_span,
        frame.event_span,
        (frame.target.start, frame.target.end),
        frame.adjunct_span,
    ]
    assert all(left[1] <= right[0] for left, right in zip(spans, spans[1:]))
    assert frame.target.cves == ((A, B) if A in target else ())


@pytest.mark.parametrize("target", [A, f"{A} and {B}", f"{A}, {B}", f"{A}, and {B}"])
def test_target_binding_stops_before_later_independent_clause(target):
    text = target + f" and Attackers are not exploiting {A}"
    owned = assertions.bind_target(text)
    assert owned and owned.text == target
    assert text[: owned.end] == target
    assert text[owned.end :] == f" and Attackers are not exploiting {A}"


@pytest.mark.parametrize(
    "text",
    [
        "continues to be exploited",
        "continued to be exploited",
        "is actively exploited",
        "has been exploited",
        "can continue to exploit CVE-2026-1234",
    ],
)
def test_start_decision_keeps_supported_and_unsupported_required_predicates(text):
    frame = assertions.bind_predicate(text)
    assert frame.starts_relation
    if text.startswith(("has", "can")):
        assert not frame.supported


@pytest.mark.parametrize(
    "text",
    [
        "newly affected issue was discussed",
        "unknown attackers exploit the gateway",
        "continues policy review",
    ],
)
def test_start_decision_cannot_lend_an_unrecognized_nominal_prefix(text):
    assert not assertions.bind_predicate(text).inherits_subject


def test_amended_joint_target_has_exact_coverage_full_text_and_tamper_guard(
    monkeypatch, tmp_path
):
    text = f"The threat actors are actively exploiting {A} and {B}."
    findings = publish(monkeypatch, tmp_path, text, [A, B], ["active"])
    assert len(findings) == 1 and findings[0].cve_ids == (A, B)
    catalog = catalog_for(
        text,
        "Attackers are actively exploiting CVE-2026-9998.",
        "Attackers are actively exploiting CVE-2026-9999.",
    )
    records, report = render(catalog)
    joint = [record for record in records if A in record.cves]
    assert len(joint) == 1 and joint[0].status == "active"
    assert text in report
    for bad in [
        report.replace(
            "**Exploitation Status**: active", "**Exploitation Status**: not_observed"
        ),
        report.replace(f"{A} and {B}", A),
    ]:
        assert bad != report
        with pytest.raises(EvidenceError):
            validate_finding_evidence(bad, catalog)


def test_complete_joint_target_keeps_contrary_source_and_unrelated_cve_separate():
    texts = [
        f"Attackers continue to exploit {A} and {B}.",
        f"{B} exploitation has not been observed.",
        "CVE-2026-9012 was exploited yesterday.",
    ]
    catalog = catalog_for(*texts)
    records, report = render(catalog)
    assert all(text in report for text in texts)
    joint = next(record for record in records if A in record.cves)
    assert set(joint.cves) == {A, B} and joint.status == "unknown"
    separate = next(record for record in records if "CVE-2026-9012" in record.cves)
    assert separate.status == "observed"


@pytest.mark.parametrize("reverse", [False, True])
def test_existing_reporter_composition_still_owns_independent_comma_clause(reverse):
    clauses = [
        f"Example has not found evidence that attackers have begun exploiting {A} in the wild",
        "the company warned of several other Gateway vulnerabilities that attackers have abused since the start of the year",
    ]
    if reverse:
        clauses.reverse()
    parsed = assertions.parse_assertions(", ".join(clauses) + ".")
    assert len(parsed) == 2 and not any(c.unsupported for c in parsed)
    specific = next(c for c in parsed if c.cves == (A,))
    other = next(c for c in parsed if c.attribution == "other")
    assert specific.status == "not_observed" and other.status == "observed"
    assert other.cves == ()


@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("connector", [" and ", ", but ", "; ", " whereas "])
def test_actor_disambiguates_the_later_subject_without_distributing_joint_target(
    monkeypatch, tmp_path, reverse, connector
):
    third = "CVE-2026-9012"
    parts = [
        f"Attackers continue to exploit {A} and {B}",
        f"The attackers are not exploiting {third}, if reports are accurate",
    ]
    if reverse:
        parts.reverse()
    text = connector.join(parts) + "."
    findings = publish(
        monkeypatch, tmp_path, text, [A, B, third], ["active", "unknown"]
    )
    assert sorted(f.cve_ids for f in findings) == [(A, B), (third,)]
    joint = next(f for f in findings if A in f.cve_ids)
    assert joint.exploitation_status.value == "active"


@pytest.mark.parametrize(
    "suffix",
    [
        " and CVE-2026-9012 can be exploited",
        " and the attackers consider exploiting CVE-2026-9012",
        "; CVE-2026-9012 continues not to be exploited",
    ],
)
def test_target_or_clause_ambiguity_cannot_swallow_unsupported_later_relation(
    monkeypatch, tmp_path, suffix
):
    rejected(
        monkeypatch,
        tmp_path,
        f"Attackers continue to exploit {A} and {B}" + suffix + ".",
    )


def test_unrelated_continuative_context_is_not_a_required_exploitation_predicate():
    text = "The retail giant also says its website and app were at all times, and continue to be, completely safe to use."
    clauses = assertions.parse_assertions(text)
    assert not any(c.unsupported or c.kind == "assertion" for c in clauses)

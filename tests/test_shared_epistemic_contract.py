"""Reported propositions retain literal owners without inventing evidence."""

from dataclasses import replace
import json
from pathlib import Path
import re

import pytest

from src.core.assertions import parse_assertions
from src.core.finding_evidence import (
    EvidenceError,
    assess_exploitation,
    source_assertions,
    validate_finding_evidence,
)
from src.core.finding_generation import compile_finding_records, render_finding_plan
from test_finding_generation import catalog_for, plan_for

CASES = json.loads(
    (Path(__file__).parent / "fixtures/shared_epistemic_contract.json").read_text()
)["cases"]
CVE = "CVE-2026-1234"
PREFIX_CASES = json.loads(
    (Path(__file__).parent / "fixtures/epistemic_intrusion_prefix.json").read_text()
)["cases"]


@pytest.mark.parametrize("case", PREFIX_CASES, ids=lambda case: case["id"])
def test_intrusion_prefix_ownership_preserves_qualified_observations(case):
    sources = tuple(catalog_for(case["text"]).values())
    assessment = assess_exploitation(sources, [CVE])
    assert assessment.status == case["status"]
    assert bool(assessment.unsupported) == case["unsupported"]
    terms = [
        (scope, term)
        for clause in source_assertions(sources[0])
        if clause.kind == "assertion"
        for scope in clause.scopes
        for term in scope.terms
        if term.kind in {"reported", "epistemic"}
    ]
    assert [term.text for _, term in terms] == (
        [case["event_modifier"]] if case["event_modifier"] else []
    )
    assert all(
        term.owner == "event" and scope.text[term.start : term.end] == term.text
        for scope, term in terms
    )


@pytest.mark.parametrize("case", CASES, ids=lambda case: case["id"])
def test_frozen_epistemic_projection_and_complete_source(case):
    expected = case["expected"]
    text = case["text"]
    if expected.get("layer") == "directive":
        text = f"## {CVE}\n\n{CVE} exploitation status is unknown.\n\n{text}"
    catalog = catalog_for(text)
    sources = tuple(catalog.values())
    clauses = source_assertions(sources[0])
    if expected["unsupported"]:
        with pytest.raises(EvidenceError) as error:
            compile_finding_records(catalog)
        assert error.value.code == "unsupported_evidence_relation"
        return
    assert clauses and not any(clause.unsupported for clause in clauses)
    for owner, status in expected["states"].items():
        cves = expected["joint_cves"] if owner == "joint" else [owner] if owner else []
        assessment = assess_exploitation(sources, cves)
        assert assessment.status == status and not assessment.unsupported
        if "conflicting" in expected:
            assert assessment.conflicting == expected["conflicting"]
    for cve, status in expected.get("singleton_statuses", {}).items():
        assert assess_exploitation(sources, [cve]).status == status
    if "clause_states" in expected:
        assert [clause.status for clause in clauses] == expected["clause_states"]
    records = compile_finding_records(catalog)
    report = render_finding_plan(json.dumps(plan_for(records)), records, catalog)
    for statement in re.split(r"(?<=[.!?])\s+", case["text"]):
        assert statement in report
    validate_finding_evidence(report, catalog)


@pytest.mark.parametrize("modifier", ["reportedly", "allegedly"])
@pytest.mark.parametrize(
    ("text", "owner"),
    [
        (f"{CVE} is {{modifier}} being exploited.", "event"),
        (f"{CVE} is {{modifier}} known to be exploited.", "knowledge"),
        (f"{CVE} is known to be {{modifier}} exploited.", "event"),
        (f"Exploitation of {CVE} has {{modifier}} been confirmed.", "evidence"),
        (f"{CVE} has {{modifier}} seen active exploitation.", "evidence"),
        (f"Hackers {{modifier}} gained access by exploiting a flaw ({CVE}).", "event"),
        (f'"Hackers are {{modifier}} exploiting {CVE}," the company said.', "event"),
        (f"If reports are accurate, Hackers {{modifier}} exploited {CVE}.", "event"),
    ],
)
def test_positioned_modifier_owner_survives_wrappers(modifier, text, owner):
    text = text.format(modifier=modifier)
    (clause,) = source_assertions(next(iter(catalog_for(text).values())))
    terms = [
        (scope, term)
        for scope in clause.scopes
        for term in scope.terms
        if term.kind == "reported"
    ]
    assert len(terms) == 1 and not clause.unsupported and clause.status == "unknown"
    scope, term = terms[0]
    assert term.text == modifier and term.owner == owner
    assert scope.text[term.start : term.end] == modifier
    assert clause.modal != "unknown"  # Local qualification is not a governing envelope.
    if participant := clause.actor_participation:
        assert participant.coordinate_text == text
        assert text[slice(*participant.nominal_span)] == "Hackers"
    if clause.reporter:
        assert clause.reporter.subject == "the company"
        assert clause.reporter.qualification == ""
    if operation := clause.evidence_operation:
        assert (
            " ".join(
                operation.text[start:end] for start, end in operation.auxiliary_spans
            )
            == operation.auxiliary
        )
        assert not replace(operation, auxiliary_spans=((0, 1),)).supported
    if observation := clause.observation:
        assert observation.modifiers == (term,)
        assert not replace(observation, modifiers=()).supported


@pytest.mark.parametrize("modifier", ["reportedly", "allegedly"])
@pytest.mark.parametrize(
    "frame",
    [
        f"{CVE} {{modifier}} has seen exploitation.",
        f"{CVE} has not {{modifier}} seen exploitation.",
        f"{CVE} exploitation {{modifier}} has been observed.",
        f"{CVE} exploitation has been {{modifier}} observed.",
        f"{CVE} exploitation has {{modifier}} not been observed.",
    ],
)
def test_reported_operand_positions_preserve_unknown(modifier, frame):
    (clause,) = parse_assertions(frame.format(modifier=modifier))
    assert not clause.unsupported and clause.status == "unknown"


@pytest.mark.parametrize("modifier", ["reportedly", "allegedly", "apparently"])
@pytest.mark.parametrize(
    "frame",
    [
        f"{CVE} has {{modifier}} {{modifier}} seen exploitation.",
        f"{CVE} exploitation has {{modifier}} {{modifier}} been confirmed.",
        f"{CVE} has {{modifier}} seen active frequent exploitation.",
        f"{CVE} exploitation has {{modifier}} was been confirmed.",
        f"{CVE} has {{modifier}} seen exploitation tomorrow.",
    ],
)
def test_qualification_cannot_rescue_malformed_evidence(modifier, frame):
    with pytest.raises(EvidenceError) as error:
        compile_finding_records(catalog_for(frame.format(modifier=modifier)))
    assert error.value.code == "unsupported_evidence_relation"

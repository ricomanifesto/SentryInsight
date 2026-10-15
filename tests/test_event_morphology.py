"""Bounded finite forms retain their own operator slots and literal owners."""

import json
from pathlib import Path

import pytest

from src.core.assertion_bindings import bind_subject
from src.core.assertion_predicates import bind_predicate
from src.core.finding_evidence import (
    EvidenceError,
    assess_exploitation,
    source_assertions,
)
from test_finding_generation import catalog_for, render

CASES = json.loads(
    (Path(__file__).parent / "fixtures/event_morphology.json").read_text()
)["cases"]


@pytest.mark.parametrize("case", CASES, ids=lambda c: c["id"])
def test_finite_inflection_keeps_the_frozen_publication_boundary(case):
    text, expected = case["text"], case["expected"]
    catalog = catalog_for(text)
    clauses = source_assertions(next(iter(catalog.values())))
    assert any(c.unsupported for c in clauses) == expected["unsupported"]
    if not expected["compile"]:
        with pytest.raises(EvidenceError) as error:
            render(catalog)
        assert error.value.code == expected["error"]
        return
    records, report = render(catalog)
    assert {dict(r.fields)["Action"] for r in records} == {expected["action"]}
    assert (text in report) == expected["retain_complete_source"]
    for cve, status in expected["states"].items():
        assessment = assess_exploitation(tuple(catalog.values()), [cve])
        assert assessment.status == status and not assessment.unsupported


@pytest.mark.parametrize(
    "case", [c for c in CASES if c.get("literal_expectations")], ids=lambda c: c["id"]
)
def test_bound_forms_and_qualifiers_keep_original_literal_spans(case):
    text = case["text"]
    clauses = source_assertions(next(iter(catalog_for(text).values())))
    assert clauses and not any(c.unsupported for c in clauses)
    subject = bind_subject(text)
    frame = (
        bind_predicate(text[subject.end :], voice=subject.kind, subject=subject)
        if subject
        else None
    )
    for item in case["literal_expectations"]:
        assert text[slice(*item["span"])] == item["text"]
        if item["kind"] == "actor":
            actors = [c.actor_participation for c in clauses if c.actor_participation]
            assert len(actors) == 1
            assert actors[0].nominal_span == tuple(item["span"])
            assert actors[0].coordinate_text == text
            assert actors[0].binding.number == "singular"
        elif item["kind"] == "event" and frame:
            assert frame.supported and frame.event_binding
            event = frame.event_binding
            assert tuple(x + subject.end for x in event.head_span) == tuple(
                item["span"]
            )
            assert event.descriptor.lemma == item["lemma"]
            assert item["slot"] in event.descriptor.slots
            assert event.descriptor.singular_actor
        elif item["kind"] == "target" and frame:
            assert (
                frame.target.start + subject.end,
                frame.target.end + subject.end,
            ) == tuple(item["span"])
        elif item["kind"] == "attack_context":
            context = frame.event_binding.attack_context
            assert context and context.supported
            assert (context.start + subject.end, context.end + subject.end) == tuple(
                item["span"]
            )
            assert any(q.attack_context is context for q in frame.qualifiers)
        elif item["kind"] in {"reported", "epistemic"}:
            terms = [
                (s, t)
                for c in clauses
                for s in c.scopes
                for t in s.terms
                if t.kind == item["kind"]
            ]
            assert len(terms) == 1
            scope, term = terms[0]
            assert term.text == item["text"] and term.owner == item["owner"]
            assert scope.text[term.start : term.end] == item["text"]
        elif item["kind"] == "negation":
            terms = [
                o
                for c in clauses
                for s in c.scopes
                for o in s.operators
                if o.kind == "negation"
            ]
            assert (
                len(terms) == 1
                and terms[0].text == item["text"]
                and terms[0].target == item["owner"]
            )
        elif item["kind"] == "condition":
            assert any(item["text"] in c.conditions for c in clauses)
        elif item["kind"] == "reporter":
            assert any(
                c.reporter and c.reporter.subject == item["text"] for c in clauses
            )


@pytest.mark.parametrize(
    "head",
    [
        "attacker",
        "operator",
        "actor",
        "threat actor",
        "hacker",
        "cybercriminal",
        "adversary",
    ],
)
def test_number_belongs_to_the_existing_nominal_binding(head):
    plural = "adversaries" if head == "adversary" else head + "s"
    for nominal, number in ((head, "singular"), (plural, "plural")):
        text = "THE\t" + nominal.upper().replace(" ", "\t") + " "
        subject = bind_subject(text)
        assert subject and subject.text == text.rstrip() and subject.number == number
        frame = bind_predicate("exploits CVE-2026-1234", voice="actor", subject=subject)
        assert frame.supported == (number == "singular")
    assert not bind_predicate("exploits CVE-2026-1234", voice="actor").supported

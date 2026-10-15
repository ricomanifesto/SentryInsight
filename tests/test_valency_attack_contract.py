"""Frozen authentication valency, attack cardinality and contextual use facts."""

import json
from pathlib import Path

import httpx
import pytest

from src.core.assertion_bindings import bind_subject
from src.core.assertion_predicates import bind_predicate
from src.core.finding_evidence import EvidenceError, assess_exploitation
from src.core.recommendations import parse_recommendation
from src.core.reporting import build_reporting_catalog
from test_finding_generation import render
from test_owned_relation_contract import article

FROZEN = json.loads(
    (Path(__file__).parent / "fixtures/valency_attack_contract.json").read_text()
)
A = "CVE-2026-1234"


@pytest.fixture(autouse=True)
def no_real_transport(monkeypatch):
    def forbidden(*args, **kwargs):
        raise AssertionError("Real transport forbidden")

    monkeypatch.setattr(httpx.Client, "send", forbidden)
    monkeypatch.setattr(httpx.AsyncClient, "send", forbidden)


@pytest.mark.parametrize("case", FROZEN["cases"], ids=lambda c: c["id"])
def test_complete_source_outcomes(case):
    expected = case["expected"]
    catalog = build_reporting_catalog(
        [
            article(s["content"], title=s["title"], link=f"https://example.test/{i}")
            for i, s in enumerate(case["sources"])
        ]
    )
    if not expected["compile"]:
        with pytest.raises(EvidenceError) as error:
            render(catalog)
        assert error.value.code == expected["error"]
        return
    records, report = render(catalog)
    owned = [r for r in records if A in r.cves]
    assert owned
    assert {r.status for r in owned} == {expected["status"]}
    assert {dict(r.fields)["Action"] for r in owned} == {expected["action"]}
    if expected["complete_guidance"]:
        assert expected["complete_guidance"] in report


@pytest.mark.parametrize("case", FROZEN["owners"], ids=lambda c: c["id"])
def test_source_and_vulnerability_owners(case):
    inputs = [
        article(s, link=f"https://example.test/owner/{i}")
        for i, s in enumerate(case["sources"])
    ]
    for cve, expected in case["expected"].items():
        result = assess_exploitation(inputs, [cve])
        assert {
            "status": result.status,
            "unsupported": bool(result.unsupported),
        } == expected


@pytest.mark.parametrize("context", ["in attacks", "in multiple attacks"])
def test_past_event_today_keeps_the_existing_time_window(context):
    result = assess_exploitation([article(f"{A} was exploited {context} today.")], [A])
    assert result.status == "observed" and not result.unsupported


@pytest.mark.parametrize("verb", ["exploited", "used"])
def test_joint_owner_is_not_an_individual_assessment(verb):
    other = "CVE-2026-5678"
    inputs = [article(f"{A} and {other} were {verb} in attacks.")]
    for scope, status in [
        ([A], "unknown"),
        ([other], "unknown"),
        ([A, other], "observed"),
    ]:
        result = assess_exploitation(inputs, scope)
        assert result.status == status and not result.unsupported


@pytest.mark.parametrize("case", FROZEN["typed_operands"])
def test_literal_operand_spans_and_shared_context(case):
    text = case["text"]
    if "patient_span" in case:
        directive = parse_recommendation(text)
        assert directive and not directive.ambiguous
        clause = directive.clauses[0]
        assert clause.verb == "enable" and clause.object_members == ("authentication",)
        frame = clause.directive_frame
        assert frame and frame.patient_span == tuple(case["patient_span"])
        assert directive.source_text == text
        return
    subject = bind_subject(text)
    assert subject
    offset = subject.end
    frame = bind_predicate(text[offset:], voice=subject.kind)
    assert frame.supported
    contexts = [q.attack_context for q in frame.qualifiers if q.attack_context]
    assert len(contexts) == 1
    context = contexts[0]
    assert context.supported
    assert [context.start + offset, context.end + offset] == case["attack_context_span"]
    assert (
        context.text[context.start : context.end]
        == text[slice(*case["attack_context_span"])]
    )
    if case["reused_operand_required"]:
        assert frame.event_binding and frame.event_binding.attack_context is context
    quantity = context.cardinality
    if expected := case["quantifier"]:
        assert (
            quantity
            and quantity.kind == expected["kind"]
            and quantity.text == expected["text"]
        )
        assert [quantity.start + offset, quantity.end + offset] == expected["span"]
        terms = [t for t in frame.scope.terms if t.kind == "cardinality"]
        assert len(terms) == 1 and terms[0].owner == "event"
        assert terms[0].start == quantity.start and terms[0].end == quantity.end
    else:
        assert quantity is None

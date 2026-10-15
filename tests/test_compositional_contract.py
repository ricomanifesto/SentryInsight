"""Independent bounded perfect/advice outcomes and positioned ownership."""

from dataclasses import replace
import json
from pathlib import Path

import httpx
import pytest

from src.core.assertion_predicates import bind_predicate
from src.core.assertions import parse_assertions
from src.core.finding_evidence import EvidenceError, assess_exploitation
from src.core.recommendations import parse_recommendation
from src.core.relations import OwnedClause
from test_finding_generation import catalog_for, render
from test_owned_relation_contract import article

CONTRACT = json.loads(
    (Path(__file__).parent / "fixtures/compositional_contract.json").read_text()
)
A = "CVE-2026-1234"


@pytest.fixture(autouse=True)
def no_real_transport(monkeypatch):
    def forbidden(*args, **kwargs):
        raise AssertionError("Real transport forbidden")

    monkeypatch.setattr(httpx.Client, "send", forbidden)
    monkeypatch.setattr(httpx.AsyncClient, "send", forbidden)


@pytest.mark.parametrize("case", CONTRACT["cases"], ids=lambda row: row["id"])
def test_independent_compositional_outcome(case):
    expected = case["expected"]
    if not expected["compile"]:
        with pytest.raises(EvidenceError) as error:
            render(catalog_for(case["source"]))
        assert error.value.code == expected["error"]
        return
    records, report = render(catalog_for(case["source"]))
    assert records
    assert {record.status for record in records} == {expected["status"]}
    assert {dict(record.fields)["Action"] for record in records} == {expected["action"]}
    if expected["complete_guidance"]:
        assert expected["complete_guidance"] in report
    if case.get("assertion_admission") is False:
        assert not any(c.kind == "assertion" for c in parse_assertions(case["text"]))


@pytest.mark.parametrize("case", CONTRACT["owners"], ids=lambda row: row["id"])
def test_perfect_source_and_target_owners(case):
    sources = [
        article(text, link=f"https://example.test/owner/{index}")
        for index, text in enumerate(case["sources"])
    ]
    for cve, expected in case["expected"].items():
        result = assess_exploitation(sources, [cve])
        actual = {
            "status": result.status,
            "unsupported": bool(result.unsupported),
            "conflicting": result.conflicting,
        }
        assert all(actual[key] == value for key, value in expected.items())


@pytest.mark.parametrize(
    "auxiliary,tense", [("has", "current"), ("have", "current"), ("had", "past")]
)
@pytest.mark.parametrize(
    "voice,operand,aspect",
    [
        ("actor", f"exploited {A}", "perfect"),
        ("actor", f"been exploiting {A}", "perfect_progressive"),
        ("vulnerability", "been exploited", "perfect"),
        ("vulnerability", "been weaponized", "perfect"),
        ("vulnerability", "been under attack", "perfect"),
        ("vulnerability", "been under active exploitation", "perfect"),
        ("vulnerability", "been under limited, targeted exploitation", "perfect"),
    ],
)
def test_finite_time_aspect_voice_and_literal_spans(
    auxiliary, tense, voice, operand, aspect
):
    text = f"{auxiliary} {operand} yesterday"
    frame = bind_predicate(text, voice=voice)
    assert frame.supported and frame.tense == tense and frame.aspect == aspect
    event = frame.event_binding
    assert event and event.kind == "complete" and event.descriptor
    assert text[slice(*event.head_span)] == event.descriptor.head
    if event.descriptor.complement:
        assert text[slice(*event.complement_span)] == event.descriptor.complement
    if voice == "actor":
        assert frame.target.cves == (A,)
        assert text[frame.target.start : frame.target.end] == A
    clause = OwnedClause(
        kind=frame.kind,
        tense=frame.tense,
        aspect=frame.aspect,
        scopes=(frame.scope,),
        temporal=frame.temporal,
    )
    assert clause.status == "observed"
    assert replace(clause, aspect="unclassified").assertion_status is None


@pytest.mark.parametrize(
    "text,status",
    [
        (f"The threat actors have been exploiting {A}.", "observed"),
        (f"{A} has been exploited and weaponized.", "observed"),
        (f"{A} has been exploited and is actively exploited.", "active"),
        (f"{A} has been under limited, targeted exploitation.", "observed"),
    ],
)
def test_owned_coordination_keeps_aspect_and_nominal_punctuation(text, status):
    result = assess_exploitation([article(text)], [A])
    assert not result.unsupported and result.status == status


@pytest.mark.parametrize("connector", ["and", "or"])
def test_preparatory_object_is_a_literal_forward_edge(connector):
    text = f"Users should download {connector} install the vendor patch."
    directive = parse_recommendation(text)
    assert directive and not directive.ambiguous
    left, right = directive.clauses
    assert left.object_antecedent == 1
    assert left.directive_frame and right.directive_frame
    frame, owner = left.directive_frame, right.directive_frame
    assert frame.patient_owner is owner
    assert frame.patient_span is None
    assert owner.patient_span
    assert owner.text[slice(*owner.patient_span)] == "the vendor patch"
    assert frame.target_binding == owner.target_binding
    assert "patch" not in frame.text
    assert directive.source_text == text


@pytest.mark.parametrize(
    "text,complement,reporter_polarity,operand_polarity",
    [
        (
            "The vendor recommends users install the patch.",
            "mandative",
            "affirmative",
            "affirmative",
        ),
        (
            "The vendor does not recommend users install the patch.",
            "mandative",
            "negative",
            "affirmative",
        ),
        (
            "The vendor recommends that users not install the patch.",
            "that",
            "affirmative",
            "negative",
        ),
        (
            "The vendor does not recommend that users install the patch.",
            "that",
            "negative",
            "affirmative",
        ),
        (
            "The vendor advised users to install the patch.",
            "infinitive",
            "affirmative",
            "affirmative",
        ),
    ],
)
def test_advice_complement_and_negation_have_separate_owners(
    text, complement, reporter_polarity, operand_polarity
):
    directive = parse_recommendation(text)
    assert directive and not directive.ambiguous and directive.envelope
    envelope = directive.envelope
    assert envelope.complement == complement
    assert envelope.reporter_span and envelope.operator_span and envelope.operand_span
    assert envelope.text[slice(*envelope.reporter_span)] == "The vendor"
    assert envelope.text[slice(*envelope.operator_span)] == envelope.reporter.finite
    assert envelope.text[slice(*envelope.operand_span)] == envelope.body
    clause = directive.clauses[0]
    assert clause.subject == "users"
    assert clause.reporter and clause.reporter.polarity == reporter_polarity
    assert clause.polarity == operand_polarity

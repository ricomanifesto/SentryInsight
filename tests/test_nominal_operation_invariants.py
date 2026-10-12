from dataclasses import replace
import pytest
from src.core.assertions import parse_assertions


@pytest.mark.parametrize("aux", ["is", "was", "has been", "has not been"])
@pytest.mark.parametrize("predicate", ["confirmed", "observed", "detected"])
def test_evidence_operation_exact_spans(aux, predicate):
    text = f"Exploitation of CVE-2026-1234 {aux} {predicate}."
    (clause,) = parse_assertions(text)
    op = clause.evidence_operation
    assert op.text[slice(*op.auxiliary_span)] == aux
    assert op.text[slice(*op.predicate_span)] == predicate
    assert clause.polarity == "affirmative"
    assert clause.tense == "unspecified"
    assert clause.text == text


@pytest.mark.parametrize(
    "field,value",
    [
        ("predicate", "invented"),
        ("auxiliary", "might have been"),
        ("polarity", "invalid"),
        ("polarity", "negative"),
    ],
)
@pytest.mark.parametrize("condition", [False, True])
def test_operation_cannot_rescue_invalid_states(field, value, condition):
    (clause,) = parse_assertions("Exploitation of CVE-2026-1234 is confirmed.")
    changed = replace(
        clause,
        evidence_operation=replace(clause.evidence_operation, **{field: value}),
        conditions=("if reports are accurate",) if condition else (),
    )
    assert changed.assertion_status is None

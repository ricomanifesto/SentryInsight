"""Independent perfect-observation contract, including owned rejected operands."""

from dataclasses import replace

import pytest

from src.core.assertions import parse_assertions
from src.core.finding_evidence import assess_exploitation, EvidenceError
from src.core.finding_generation import compile_finding_records
from test_finding_generation import catalog_for
from test_owned_relation_contract import article

A = "CVE-2026-1234"
B = "CVE-2026-5678"


@pytest.mark.parametrize("auxiliary", ["has", "have", "had"])
@pytest.mark.parametrize("nominal", ["exploitation", "active exploitation"])
@pytest.mark.parametrize("negative", ["", "not ", "never "])
@pytest.mark.parametrize(
    "tail,qualified",
    [
        ("", False),
        (" yesterday", False),
        (" in June", False),
        (" as investigators confirmed yesterday", False),
        (" if reports are accurate", True),
    ],
)
def test_complete_observation(auxiliary, nominal, negative, tail, qualified):
    text = f"{A} {auxiliary} {negative}seen {nominal}{tail}."
    assessment = assess_exploitation([article(text)], [A])
    assert not assessment.unsupported
    assert assessment.status == ("unknown" if negative or qualified else "observed")
    assert all(not c.assertion_projection.excludes for c in assessment.relations)


@pytest.mark.parametrize("nominal", ["exploitation", "active exploitation"])
@pytest.mark.parametrize(
    "operator",
    [
        "may have seen",
        "might have seen",
        "could have seen",
        "would have seen",
        "will have seen",
        "can have seen",
        "sees",
        "saw",
        "is seeing",
        "has been seeing",
        "has not not seen",
        "has never not seen",
        "not has seen",
        "has seen not",
        "has recently seen",
        "has currently seen",
    ],
)
def test_unapproved_observation_operator(operator, nominal):
    result = assess_exploitation([article(f"{A} {operator} {nominal}.")], [A])
    assert result.unsupported


@pytest.mark.parametrize(
    "operand",
    [
        "",
        "attacks",
        "weaponization",
        "limited, targeted exploitation",
        "active exploits",
        "active exploitation and unknown activity",
        "exploitation today",
        "exploitation now",
        "exploitation tomorrow",
        "exploitation under unexplained conditions",
        f"exploitation of {B}",
    ],
)
def test_reserved_operand_stays_required(operand):
    text = f"{A} has seen {operand}."
    clauses = parse_assertions(text)
    assert clauses[0].cves == (A,) or B in clauses[0].cves
    assert clauses[0].unsupported
    assert assess_exploitation([article(text)], [A]).unsupported
    with pytest.raises(EvidenceError) as error:
        compile_finding_records(catalog_for(text), [A])
    assert error.value.code == "unsupported_evidence_relation"
    assert error.value.field == "Exploitation Status"


@pytest.mark.parametrize("nominal", ["exploitation", "active exploitation"])
@pytest.mark.parametrize("negative", ["", "not ", "never "])
def test_current_positive_and_sibling_keep_their_owners(nominal, negative):
    text = f"{A} has {negative}seen {nominal} and {B} is actively exploited."
    expected = "unknown" if negative else "observed"
    assert assess_exploitation([article(text)], [A]).status == expected
    sibling = assess_exploitation([article(text)], [B])
    assert not sibling.unsupported and sibling.status == "active"
    same = assess_exploitation(
        [article(f"{A} has {negative}seen {nominal}. {A} is actively exploited.")], [A]
    )
    assert not same.unsupported and same.status == "active"
    separate = assess_exploitation(
        [
            article(
                f"{A} has {negative}seen {nominal}.", link="https://example.test/a"
            ),
            article(f"{B} is actively exploited.", link="https://example.test/b"),
        ],
        [A],
    )
    assert not separate.unsupported and separate.status == expected


def test_invalid_nominal_cannot_swallow_later_finite():
    clauses = parse_assertions(
        f"{A} has seen limited, targeted exploitation and {B} is actively exploited."
    )
    assert len(clauses) == 2
    assert clauses[0].cves == (A,) and clauses[0].unsupported
    assert clauses[1].cves == (B,) and clauses[1].assertion_status == "active"


@pytest.mark.parametrize("nominal", ["exploitation", "active exploitation"])
def test_literal_observation_spans_and_validation(nominal):
    (clause,) = parse_assertions(f"{A} has not seen {nominal} yesterday.")
    observation = getattr(clause, "observation", None)
    assert observation is not None
    assert observation.supported
    assert observation.text[slice(*observation.auxiliary_span)] == "has"
    assert observation.text[slice(*observation.negative_span)] == "not"
    assert observation.text[slice(*observation.predicate_span)] == "seen"
    assert observation.text[slice(*observation.nominal_span)] == nominal
    assert observation.text[slice(*observation.event_span)] == "exploitation"
    assert clause.assertion_status == "unknown"
    bad = replace(observation, event_span=observation.predicate_span)
    assert not bad.supported
    assert replace(clause, observation=bad).assertion_status is None


@pytest.mark.parametrize(
    "subject", ["It", "They", "Researchers", "The vendor", "Attackers"]
)
def test_unknown_observer_is_not_a_vulnerability(subject):
    assert assess_exploitation(
        [article(f"{subject} has seen exploitation of {A}.")], [A]
    ).unsupported

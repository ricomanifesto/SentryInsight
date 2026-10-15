"""Invalid ownership, head/span and inherited-coordinate controls."""

from dataclasses import replace
import pytest
from src.core.assertion_predicates import OPERATOR_PRODUCTIONS, bind_predicate
from src.core.assertions import parse_assertions
from src.core.assertion_qualifiers import assertion_scope
from src.core.relations import AssertionScope, ScopeTerm, ScopeOperator, OwnedClause
from src.core.finding_evidence import assess_exploitation
from test_owned_relation_contract import article

A = "CVE-2026-1234"
B = "CVE-2026-5678"


def item(text, literal, kind, target):
    start = text.index(literal)
    return ScopeOperator(literal, start, start + len(literal), kind, target)


def scope(text="is not known to be actively exploited"):
    start = text.index("actively")
    return AssertionScope(
        text,
        (ScopeTerm("actively", start, start + 8, "activity", "event"),),
        (
            item(text, "not", "negation", "knowledge"),
            item(text, "known", "knowledge", "event"),
        ),
        "current",
    )


def projection(s, polarity="affirmative"):
    return OwnedClause(
        kind="assertion", tense="current", polarity=polarity, scopes=(s,)
    ).assertion_projection


def test_exact_eight_knowledge_heads_stay_in_bounded_productions():
    assert len(OPERATOR_PRODUCTIONS) == 74
    marked = [
        r
        for r in OPERATOR_PRODUCTIONS
        if getattr(r, "knowledge_head", None) is not None
    ]
    assert len(marked) == 8
    assert all(
        r.knowledge_head == 1 and r.operators[1:] == ("known", "to", "be")
        for r in marked
    )


@pytest.mark.parametrize(
    "mutation",
    [
        "missing-head",
        "duplicate-head",
        "wrong-head-text",
        "wrong-head-target",
        "wrong-head-kind",
        "bad-head-span",
        "event-negation-before-head",
        "knowledge-negation-after-head",
        "knowledge-modifier-after-head",
        "event-modifier-before-head",
        "unknown-negation-target",
        "unknown-modifier-owner",
        "overlapping-head-negation",
    ],
)
def test_invalid_head_owner_and_span_states_are_unsupported(mutation):
    s = scope()
    neg, head = s.operators
    if mutation == "missing-head":
        s = replace(s, operators=(neg,))
    elif mutation == "duplicate-head":
        s = replace(s, operators=(neg, head, head))
    elif mutation == "wrong-head-text":
        s = replace(s, operators=(neg, item(s.text, "is", "knowledge", "event")))
    elif mutation == "wrong-head-target":
        s = replace(s, operators=(neg, replace(head, target="knowledge")))
    elif mutation == "wrong-head-kind":
        s = replace(s, operators=(neg, replace(head, kind="event")))
    elif mutation == "bad-head-span":
        s = replace(s, operators=(neg, replace(head, start=head.start + 1)))
    elif mutation == "event-negation-before-head":
        s = replace(s, operators=(replace(neg, target="event"), head))
    elif mutation == "knowledge-negation-after-head":
        s = scope("is known to not be actively exploited")
    elif mutation == "knowledge-modifier-after-head":
        s = replace(s, terms=(replace(s.terms[0], owner="knowledge"),))
    elif mutation == "event-modifier-before-head":
        text = "is actively not known to be exploited"
        s = AssertionScope(
            text,
            (ScopeTerm("actively", 3, 11, "activity", "event"),),
            (
                item(text, "not", "negation", "knowledge"),
                item(text, "known", "knowledge", "event"),
            ),
            "current",
        )
    elif mutation == "unknown-negation-target":
        s = replace(s, operators=(replace(neg, target="unclassified"), head))
    elif mutation == "unknown-modifier-owner":
        s = replace(s, terms=(replace(s.terms[0], owner="unclassified"),))
    elif mutation == "overlapping-head-negation":
        s = replace(
            s,
            operators=(
                neg,
                replace(head, start=neg.start, text=s.text[neg.start : head.end]),
            ),
        )
    assert not s.supported
    assert projection(s).status is None


@pytest.mark.parametrize(
    "text,negative",
    [
        ("is not known to be actively exploited", "knowledge"),
        ("is known not to be actively exploited", "event"),
        ("is known to not be actively exploited", "event"),
        ("is known to be not actively exploited", "event"),
        ("was never known to be exploited", "knowledge"),
    ],
)
def test_event_compatibility_polarity_is_derived_from_the_bound_owner(text, negative):
    f = bind_predicate(text, voice="vulnerability")
    assert f.supported
    assert f.polarity == ("negative" if negative == "event" else "affirmative")
    heads = [o for o in f.scope.operators if o.kind == "knowledge"]
    assert len(heads) == 1
    neg = next(o for o in f.scope.operators if o.kind == "negation")
    assert (neg.target == "knowledge") == (negative == "knowledge")
    assert all(
        f.scope.text[x.start : x.end] == x.text
        for x in (*f.scope.operators, *f.scope.terms)
    )


@pytest.mark.parametrize("modifier", ["actively", "currently", "widely", "likely"])
@pytest.mark.parametrize("position", ["knowledge", "event"])
def test_modifier_owner_is_positioned_relative_to_the_matched_head(modifier, position):
    text = (
        f"is {modifier} not known to be exploited"
        if position == "knowledge"
        else f"is not known to be {modifier} exploited"
    )
    f = bind_predicate(text, voice="vulnerability")
    assert f.supported
    term = next(t for t in f.scope.terms if t.text == modifier)
    assert term.owner == position
    p = projection(f.scope)
    assert p.status == "unknown" and not p.excludes


@pytest.mark.parametrize(
    "text",
    [
        f"{A} is not known to be exploited and weaponized.",
        f"{A} is not known to be not only exploited but weaponized.",
    ],
)
def test_inherited_knowledge_scope_keeps_original_local_coordinates(text):
    clauses = parse_assertions(text)
    assert len(clauses) == 2
    first = next(
        s
        for s in clauses[0].scopes
        if any(o.target == "knowledge" for o in s.operators)
    )
    inherited = next(
        s
        for s in clauses[1].scopes
        if any(o.target == "knowledge" for o in s.operators)
    )
    assert inherited.text == first.text and inherited.text != clauses[1].text
    assert all(o in first.operators for o in inherited.operators)
    assert any(o.kind == "knowledge" for o in inherited.operators)
    assert any(
        o.kind == "negation" and o.target == "knowledge" for o in inherited.operators
    )
    for clause in clauses:
        assert clause.status == "unknown" and not clause.unsupported
        assert all(
            s.text[o.start : o.end] == o.text
            for s in clause.scopes
            for o in (*s.operators, *s.terms)
        )


@pytest.mark.parametrize(
    "tail,expected",
    [
        (f"{A} is actively exploited.", "active"),
        (f"{A} was exploited yesterday.", "observed"),
        (f"{B} is actively exploited.", "active"),
    ],
)
def test_an_independent_finite_does_not_receive_negative_knowledge(tail, expected):
    clauses = assess_exploitation(
        [article(f"{A} is not known to be exploited. {tail}")], [A, B]
    ).relations
    assert clauses[0].status == "unknown" and clauses[-1].status == expected
    assert not any(
        o.target == "knowledge" for s in clauses[-1].scopes for o in s.operators
    )


@pytest.mark.parametrize(
    "text,excludes",
    [
        ("is currently known not to be exploited", ()),
        ("is known not to be currently exploited", ("active",)),
        ("is not known to be currently exploited", ()),
    ],
)
def test_current_exclusion_requires_an_event_owned_denial(text, excludes):
    clause = parse_assertions(f"{A} {text}.")[0]
    assert not clause.unsupported and clause.status == "unknown"
    assert clause.assertion_projection.excludes == excludes


@pytest.mark.parametrize(
    "text",
    [
        "is not known not to be exploited",
        "is never known to not be exploited",
        "is not not known to be exploited",
        "is known known to be exploited",
    ],
)
def test_repeated_scope_or_operator_stacks_stay_unsupported(text):
    assert not bind_predicate(text, voice="vulnerability").supported


def test_scope_composition_cannot_repair_an_invalid_negation_owner():
    text = "is known not to be exploited"
    operators = (
        item(text, "known", "knowledge", "event"),
        item(text, "not", "negation", "unclassified"),
    )
    bound = assertion_scope(text, operators=operators, event_tense="current")
    assert not bound.supported
    assert projection(bound).status is None


@pytest.mark.parametrize(
    "tail,cve,expected,inherits_knowledge",
    [
        ("is actively exploited", A, "active", False),
        (f"{B} is actively exploited", B, "active", False),
        ("was exploited yesterday", A, "observed", False),
        ("weaponized", A, "unknown", True),
    ],
)
def test_correlative_knowledge_scope_stops_at_independent_finite_or_subject(
    tail, cve, expected, inherits_knowledge
):
    text = f"{A} is not known to be not only exploited but {tail}."
    result = assess_exploitation([article(text)], [cve])
    assert result.status == expected and not result.unsupported
    assert result.relations[-1].knowledge_negative is inherits_knowledge

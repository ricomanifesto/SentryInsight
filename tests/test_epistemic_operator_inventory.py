"""Finite operator admission and ownership contract, including every prefix gap."""

from dataclasses import asdict
import hashlib
import json

import pytest

from src.core.assertion_predicates import OPERATOR_PRODUCTIONS, bind_predicate
from src.core.relations import OwnedClause

MODIFIERS = (
    "actively",
    "also",
    "currently",
    "extensively",
    "first",
    "likely",
    "newly",
    "now",
    "observed",
    "possibly",
    "potentially",
    "probably",
    "publicly",
    "recently",
    "still",
    "successfully",
    "unlikely",
    "widely",
    "yet",
)
POSSIBLE = {"likely", "possibly", "potentially", "probably", "unlikely"}


def test_existing_complete_productions_are_the_frozen_admission_boundary():
    signature = [
        {key: value for key, value in asdict(rule).items() if key != "knowledge_head"}
        for rule in OPERATOR_PRODUCTIONS
    ]
    assert len(signature) == 67
    assert sum(len(rule.events) for rule in OPERATOR_PRODUCTIONS) == 110
    assert (
        hashlib.sha256(json.dumps(signature, sort_keys=True).encode()).hexdigest()
        == "8d33a42eafaa88ba6ce3d546cd4c91cd10e37f0372d840d260494ed6ed2df460"
    )


def positions(rule, event):
    gaps = range(len(rule.operators) + 1)
    yield []
    for gap in gaps:
        for word in ("not", "never", *MODIFIERS):
            yield [(gap, [word])]
        for negation in ("not", "never"):
            for modifier in MODIFIERS:
                yield [(gap, [negation, modifier])]
                yield [(gap, [modifier, negation])]
    if "known" in rule.operators:
        for negation_gap in gaps:
            for modifier_gap in gaps:
                if negation_gap != modifier_gap:
                    for negation in ("not", "never"):
                        for modifier in MODIFIERS:
                            yield [
                                (negation_gap, [negation]),
                                (modifier_gap, [modifier]),
                            ]
    if event == rule.events[0]:
        for left in gaps:
            for right in range(left, len(rule.operators) + 1):
                for first, second in (
                    ("not", "not"),
                    ("not", "never"),
                    ("never", "not"),
                    ("never", "never"),
                ):
                    yield (
                        [(left, [first, second])]
                        if left == right
                        else [(left, [first]), (right, [second])]
                    )


def expected_meaning(rule, event, insertions):
    """Independent meaning contract; it never invokes the production projection."""
    inserted = dict(insertions)
    sequence = []
    for gap in range(len(rule.operators) + 1):
        sequence.extend((word, gap, True) for word in inserted.get(gap, []))
        if gap < len(rule.operators):
            sequence.append((rule.operators[gap], gap, False))
    negatives = [
        (i, gap)
        for i, (word, gap, added) in enumerate(sequence)
        if added and word in {"not", "never"}
    ]
    modifiers = [
        (i, word, gap)
        for i, (word, gap, added) in enumerate(sequence)
        if added and word not in {"not", "never"}
    ]
    boundary = rule.operators.index("known") if "known" in rule.operators else None

    def owner(gap):
        return "knowledge" if boundary is not None and gap <= boundary else "event"

    knowledge_negative = any(owner(gap) == "knowledge" for _, gap in negatives)
    event_negative = any(owner(gap) == "event" for _, gap in negatives)
    possible = bool(rule.modal) or any(word in POSSIBLE for _, word, _ in modifiers)
    supported = not (
        len(negatives) > 1
        or (negatives and not rule.allows_negation)
        or any(word == "observed" for _, word, _ in modifiers)
        or (
            rule.tense == "past"
            and any(word in {"now", "currently"} for _, word, _ in modifiers)
        )
        or (rule.tense == "unspecified" and not (negatives or possible))
    )
    restrictions = [
        (word, owner(gap))
        for i, word, gap in modifiers
        if not (word == "also" and negatives and i < min(n[0] for n in negatives))
    ]
    if event == "under":
        restrictions.append(("actively", "event"))
    if not supported:
        status = None
    elif knowledge_negative:
        status = "unknown"
    elif possible:
        status = "unknown" if event_negative else "potential"
    elif event_negative:
        status = "unknown" if restrictions else "not_observed"
    else:
        status = (
            "active"
            if rule.tense == "current"
            else "observed" if rule.tense == "past" else None
        )
    excludes = (
        ("active",)
        if (
            supported
            and event_negative
            and not knowledge_negative
            and not possible
            and rule.tense == "current"
            and restrictions
            and all(
                word in {"actively", "currently", "now"} and role == "event"
                for word, role in restrictions
            )
        )
        else ()
    )
    return (
        supported,
        status,
        excludes,
        [owner(gap) for _, gap in negatives],
        [owner(gap) for _, _, gap in modifiers],
    )


def predicate(rule, event, insertions):
    tokens = list(rule.operators)
    for gap, words in sorted(insertions, reverse=True):
        tokens[gap:gap] = words
    tail = " active exploitation" if event == "under" else ""
    if rule.voice == "actor":
        tail += " CVE-2026-1234"
    return " ".join([*tokens, event]) + tail


@pytest.mark.parametrize("rule", OPERATOR_PRODUCTIONS)
def test_all_existing_negation_modifier_positions_keep_their_owner(rule):
    for event in rule.events:
        for insertions in positions(rule, event):
            text = predicate(rule, event, insertions)
            expected = expected_meaning(rule, event, insertions)
            frame = bind_predicate(text, voice=rule.voice)
            clause = OwnedClause(
                kind=frame.kind,
                modal=frame.modal,
                polarity=frame.polarity,
                tense=frame.tense,
                scopes=(frame.scope,),
                temporal=frame.temporal,
                unsupported=not frame.supported,
            )
            projection = clause.assertion_projection
            negatives = [
                o.target for o in frame.scope.operators if o.kind == "negation"
            ]
            actual = (
                frame.supported,
                projection.status,
                projection.excludes,
                [
                    "event" if target in {"event", "qualified_event"} else target
                    for target in negatives
                ],
                [term.owner for term in frame.scope.terms[: len(expected[-1])]],
            )
            assert actual == expected, (text, expected, actual)
            assert all(
                frame.scope.text[item.start : item.end] == item.text
                for item in (*frame.scope.terms, *frame.scope.operators)
            )
            if "known" in rule.operators:
                heads = [o for o in frame.scope.operators if o.kind == "knowledge"]
                assert (
                    len(heads) == 1
                    and heads[0].text == "known"
                    and heads[0].target == "event"
                )


@pytest.mark.parametrize("rule", OPERATOR_PRODUCTIONS)
def test_correlative_markers_and_unrecognized_stacks_preserve_admission(rule):
    for event in rule.events:
        for gap in range(len(rule.operators) + 1):
            for word in ("only", "just", "merely", "simply"):
                text = predicate(rule, event, [(gap, ["not", word])])
                frame = bind_predicate(text, voice=rule.voice)
                assert frame.supported == (
                    rule.tense != "unspecified" or bool(rule.modal)
                ), text
                assert frame.polarity == "affirmative", text
        for prefix in ("will", rule.operators[0] if rule.operators else "known"):
            text = predicate(rule, event, [(0, [prefix])])
            assert not bind_predicate(text, voice=rule.voice).supported, text

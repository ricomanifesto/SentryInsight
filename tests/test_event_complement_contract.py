"""Independent operator/qualification matrix and exact lexical boundaries."""

import re
import pytest
from src.core.assertion_predicates import bind_predicate
from src.core.relations import OwnedClause
from src.core.exploitation_contract import (
    EXPLOITATION_RELEVANCE_PATTERN,
    NEGATED_EXPLOITATION_PATTERN,
    has_required_event,
)


def event_cases():
    # Explicit existing operators; expectations do not consume parser tables.
    operators = [
        (x, t, "")
        for x, t in [
            ("is", "current"),
            ("are", "current"),
            ("was", "past"),
            ("were", "past"),
            ("has been", "unspecified"),
            ("have been", "unspecified"),
            ("had been", "past"),
        ]
    ]
    operators += [
        (f"{m} {c}", "unspecified", "possible")
        for m in ("may", "might", "could", "would")
        for c in ("be", "have been")
    ]
    operators += [
        (f"{f} known to be", t, "")
        for f, t in [
            ("is", "current"),
            ("are", "current"),
            ("was", "past"),
            ("were", "past"),
        ]
    ]
    mods = (
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
    possible = {"likely", "possibly", "potentially", "probably", "unlikely"}
    for operator, tense, modal in operators:
        words = operator.split()
        head = words.index("known") if "known" in words else None
        gaps = range(len(words) + 1)
        insertions = [[]]
        for gap in gaps:
            insertions.extend([[(gap, [word])] for word in ("not", "never", *mods)])
            for neg in ("not", "never"):
                for mod in mods:
                    insertions.extend([[(gap, [neg, mod])], [(gap, [mod, neg])]])
        if head is not None:
            for ng in gaps:
                for mg in gaps:
                    if ng != mg:
                        insertions.extend(
                            [
                                [(ng, [n]), (mg, [m])]
                                for n in ("not", "never")
                                for m in mods
                            ]
                        )
        for left in gaps:
            for right in range(left, len(words) + 1):
                for n, m in [
                    ("not", "not"),
                    ("not", "never"),
                    ("never", "not"),
                    ("never", "never"),
                ]:
                    insertions.append(
                        [(left, [n, m])]
                        if left == right
                        else [(left, [n]), (right, [m])]
                    )
        for complement in (
            "attack",
            "active exploitation",
            "limited, targeted exploitation",
        ):
            for added in insertions:
                seq = []
                bygap = dict(added)
                for gap in gaps:
                    seq.extend((word, gap, True) for word in bygap.get(gap, []))
                    if gap < len(words):
                        seq.append((words[gap], gap, False))
                negs = [
                    (i, g)
                    for i, (w, g, a) in enumerate(seq)
                    if a and w in {"not", "never"}
                ]
                terms = [
                    (i, w, g)
                    for i, (w, g, a) in enumerate(seq)
                    if a and w not in {"not", "never"}
                ]

                def owner(g):
                    return "knowledge" if head is not None and g <= head else "event"

                kn = any(owner(g) == "knowledge" for _, g in negs)
                en = any(owner(g) == "event" for _, g in negs)
                possibility = bool(modal) or any(w in possible for _, w, _ in terms)
                supported = not (
                    len(negs) > 1
                    or any(w == "observed" for _, w, _ in terms)
                    or (
                        tense == "past"
                        and any(w in {"now", "currently"} for _, w, _ in terms)
                    )
                    or (
                        tense == "unspecified"
                        and not (negs or possibility)
                        and operator not in {"has been", "have been"}
                    )
                )
                restrictions = [
                    (w, owner(g))
                    for i, w, g in terms
                    if not (w == "also" and negs and i < min(n[0] for n in negs))
                ]
                restrictions.append(
                    (
                        (
                            "activity"
                            if complement != "limited, targeted exploitation"
                            else "degree"
                        ),
                        "event",
                    )
                )
                status = (
                    None
                    if not supported
                    else (
                        "unknown"
                        if kn or en
                        else (
                            "potential"
                            if possibility
                            else "active" if tense == "current" else "observed"
                        )
                    )
                )
                excludes = (
                    ["active"]
                    if supported
                    and en
                    and not kn
                    and not possibility
                    and tense == "current"
                    and all(
                        w in {"activity", "actively", "currently", "now"}
                        and o == "event"
                        for w, o in restrictions
                    )
                    else []
                )
                yield (
                    {
                        "text": " ".join(w for w, _, _ in seq) + " under " + complement,
                        "operator": operator,
                        "complement": complement,
                        "expected": {
                            "kind": "assertion",
                            "supported": supported,
                            "status": status,
                            "excludes": excludes,
                        },
                        "negation_owners": [owner(g) for _, g in negs],
                        "modifier_owners": [owner(g) for _, _, g in terms],
                    }
                )


POSITIVE_PATTERN = "\\b(?:active(?:ly)? exploit(?:s|ed|ing|ation)?|exploit(?:s|ed|ing|ation)?|in the wild|zero[\\s-]?day|0day|weaponiz(?:ed|ation)|under attack|attackers? (?:are )?exploit(?:s|ed|ing)?|backdoor|malware|threat actor|campaign)\\b"
NEGATIVE_PATTERN = "\\b(?:no evidence(?:\\s+(?:of|that))?|not\\s+(?:actively\\s+|being\\s+)?(?=exploit)|without\\s+(?:evidence|signs?|reports?)(?:\\s+of)?|has not been|have not been|not known to be|not reported to be|not observed to be|not detected as|no signs? of|no reports? of)\\b.{0,120}\\b(?:exploit(?:ed|ing|ation)?|in the wild|weaponiz(?:ed|ation)|under attack)\\b"


@pytest.mark.parametrize(
    "complement", ["attack", "active exploitation", "limited, targeted exploitation"]
)
def test_complete_operator_and_modifier_matrix(complement):
    count = 0
    for row in event_cases():
        if row["complement"] != complement:
            continue
        count += 1
        frame = bind_predicate(row["text"], voice="vulnerability")
        clause = OwnedClause(
            kind=frame.kind,
            modal=frame.modal,
            polarity=frame.polarity,
            tense=frame.tense,
            aspect=frame.aspect,
            scopes=(frame.scope,),
            temporal=frame.temporal,
            unsupported=not frame.supported,
        )
        projection = clause.assertion_projection
        assert {
            "kind": frame.kind,
            "supported": frame.supported,
            "status": projection.status,
            "excludes": list(projection.excludes),
        } == row["expected"], row
        event = frame.event_binding
        assert event is not None and event.descriptor is not None
        assert event.kind == "complete"
        assert frame.text[slice(*event.head_span)] == "under"
        assert frame.text[slice(*event.complement_span)] == complement
        qualifier = frame.text[slice(*event.qualifier_span)]
        assert qualifier == (
            "attack"
            if complement == "attack"
            else (
                "active" if complement == "active exploitation" else "limited, targeted"
            )
        )
        assert all(
            frame.scope.text[t.start : t.end] == t.text
            for t in (*frame.scope.terms, *frame.scope.operators)
        )
    assert count == 9980


def test_selector_patterns_retain_exact_order_boundaries_and_flags():
    assert EXPLOITATION_RELEVANCE_PATTERN.pattern == POSITIVE_PATTERN
    assert NEGATED_EXPLOITATION_PATTERN.pattern == NEGATIVE_PATTERN
    assert EXPLOITATION_RELEVANCE_PATTERN.flags == re.compile("", re.I).flags
    assert NEGATED_EXPLOITATION_PATTERN.flags == re.compile("", re.I | re.S).flags


@pytest.mark.parametrize(
    "text,kind",
    [
        ("is under attack", "complete"),
        ("will be under attack", "complete"),
        ("is under attack tomorrow", "required"),
        ("is under attack CVE-2026-1234", "required"),
        ("is under attacks", "context"),
        ("is under review", "context"),
        ("is under repair", "context"),
    ],
)
def test_complement_classification_is_distinct_from_operator_admission(text, kind):
    frame = bind_predicate(text, voice="vulnerability")
    assert frame.event_binding.kind == kind
    assert frame.supported == (kind == "context" or text == "is under attack")
    assert has_required_event(text) == (kind != "context")


@pytest.mark.parametrize("operator", ["is", "was", "may be", "is known to be"])
@pytest.mark.parametrize("context", ["affected", "patched", "disclosed"])
@pytest.mark.parametrize(
    "complement", ["attack", "active exploitation", "limited, targeted exploitation"]
)
def test_context_verb_cannot_consume_a_required_event(operator, context, complement):
    text = f"{operator} {context} under {complement}"
    frame = bind_predicate(text, voice="vulnerability")
    assert frame.event_binding.kind == "required"
    assert frame.kind == "assertion"
    assert not frame.supported

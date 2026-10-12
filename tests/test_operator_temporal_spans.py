"""Freeze complete operator forms and owned temporal spans before implementation."""

import pytest
from src.core.assertion_predicates import bind_predicate
from src.core.assertion_qualifiers import bind_qualifiers
from test_assertion_subject_contract import rejected

A = "CVE-2026-1234"


@pytest.mark.parametrize(
    "text,state",
    [
        ("is under active exploitation", "active"),
        ("may be under active exploitation", "potential"),
        ("had been under active exploitation", "observed"),
        ("may not be under active exploitation", "unknown"),
        ("may have been under active exploitation", "potential"),
        ("is known to be under active exploitation", "active"),
        ("may under active exploitation", None),
        ("has begun under active exploitation", None),
        ("may be under active exploitation by unexplained means", None),
        ("may be under active exploitation tomorrow", None),
    ],
)
def test_existing_nominal_complement_uses_complete_operator_production(text, state):
    from src.core.assertions import parse_assertions

    source = f"{A} {text}."
    relations = parse_assertions(source)
    assert relations
    if state is None:
        assert any(r.unsupported for r in relations)
    else:
        assert not any(r.unsupported for r in relations)
        assert [r.assertion_status for r in relations] == [state]
        assert [r.text for r in relations] == [source]


@pytest.mark.parametrize(
    "voice,text,supported",
    [
        ("actor", f"are exploiting {A}", True),
        ("vulnerability", "is exploited", True),
        ("actor", f"are exploited {A}", False),
        ("vulnerability", "is exploiting", False),
        ("actor", f"were exploiting {A}", True),
        ("vulnerability", "was being exploited", True),
        ("vulnerability", "was being exploit", False),
        ("actor", f"had been exploiting {A}", True),
        ("vulnerability", "had been exploited", True),
        ("actor", f"had been exploited {A}", False),
        ("actor", f"may exploit {A}", True),
        ("vulnerability", "may be exploited", True),
        ("actor", f"may be exploiting {A}", True),
        ("vulnerability", "may have been exploited", True),
        ("vulnerability", "may exploited", False),
        ("actor", f"may have been exploit {A}", False),
        ("vulnerability", "is known to be exploited", True),
        ("actor", f"are known to be exploiting {A}", True),
        ("vulnerability", "is known to be exploiting", False),
        ("actor", f"have begun exploited {A}", False),
        ("vulnerability", "has begun exploited", False),
        (
            "vulnerability",
            "has begun to be exploited and consider attacking systems",
            False,
        ),
    ],
)
def test_existing_operator_family_owns_grammatical_voice_event(voice, text, supported):
    assert bind_predicate(text, voice=voice).supported is supported


@pytest.mark.parametrize(
    "voice,text,operator,event,target",
    [
        (
            "vulnerability",
            "has begun to be actively exploited yesterday",
            "has begun to be actively",
            "exploited",
            "",
        ),
        (
            "vulnerability",
            "had begun being exploited yesterday",
            "had begun being",
            "exploited",
            "",
        ),
        (
            "actor",
            f"have begun actively exploiting {A} yesterday",
            "have begun actively",
            "exploiting",
            A,
        ),
        (
            "actor",
            f"had begun to actively exploit {A} yesterday",
            "had begun to actively",
            "exploit",
            A,
        ),
    ],
)
def test_initiation_frame_preserves_exact_nonoverlapping_spans(
    voice, text, operator, event, target
):
    f = bind_predicate(text, voice=voice)
    assert f.supported and f.tense == "past" and f.aspect == "initiation"
    assert text[slice(*f.operator_span)] == operator
    assert text[slice(*f.event_span)] == event
    assert f.target.text == target
    assert text[slice(*f.adjunct_span)] == "yesterday"
    assert all(text[q.start : q.end] == q.text for q in f.qualifiers)
    assert (
        f.operator_span[1]
        <= f.event_span[0]
        <= f.event_span[1]
        <= f.target.start
        <= f.target.end
        <= f.adjunct_span[0]
    )


@pytest.mark.parametrize(
    "text,owner,direction",
    [
        ("yesterday", "event", "past"),
        ("last week", "event", "past"),
        ("tomorrow", "event", "future"),
        ("next Tuesday afternoon", "event", "future"),
        ("now", "event", "current"),
        ("today", "event", "window"),
        ("as was confirmed yesterday", "reporter", "past"),
        ("as is confirmed today", "reporter", "window"),
        ("as was confirmed next week", "reporter", "future"),
    ],
)
def test_temporal_annotation_is_owned_and_preserves_whole_span(text, owner, direction):
    bound = bind_qualifiers(text)
    assert bound.complete and len(bound.spans) == 1
    q = bound.spans[0]
    assert q.text == text and text[q.start : q.end] == text
    assert q.temporal.owner == owner and q.temporal.direction == direction


@pytest.mark.parametrize(
    "text",
    [
        f"{A} exploitation was observed tomorrow.",
        f"{A} exploitation has not been observed tomorrow.",
        f"No evidence of {A} being exploited tomorrow.",
        f"The actor gained access by exploiting a vulnerability ({A}) tomorrow.",
        f"The actor gained access by exploiting a vulnerability ({A}) now.",
        f"{A} is exploited as was confirmed next week.",
    ],
)
def test_every_owned_assertion_consumer_preserves_future_rejection(
    monkeypatch, tmp_path, text
):
    rejected(monkeypatch, tmp_path, text)

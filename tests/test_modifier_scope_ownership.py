"""Ordered scope, ownership, inheritance and finite modifier inventory."""

import pytest
from src.core.assertions import parse_assertions
from src.core.assertion_predicates import bind_predicate
from src.core.finding_evidence import assess_exploitation
from test_owned_relation_contract import article

A = "CVE-2026-1234"
B = "CVE-2026-5678"


# Explicit finite controls settle the elided adversative disposition.
@pytest.mark.parametrize(
    "tail,expected",
    [
        ("weaponized in the wild", "unknown"),
        ("was weaponized in the wild", "observed"),
        ("is now weaponized in the wild", "active"),
    ],
)
def test_elided_adversative_time(tail, expected):
    a = assess_exploitation(
        [article(f"{A} was not actively exploited, but {tail}.")], [A]
    )
    assert not a.unsupported and a.status == expected
    assert not a.conflicting and not a.negative


DENIALS = [
    ("is not actively exploited", True),
    ("is not exploited now", True),
    ("is currently not exploited", True),
    ("is not currently exploited", True),
    ("is currently not widely exploited", False),
    ("is not currently widely exploited", False),
    ("is not widely currently exploited", False),
    ("is not actively widely exploited", False),
    ("is not actively successfully exploited", False),
    ("is not publicly currently exploited", False),
    ("is not currently exploited often", False),
    ("is not actively exploited abroad", False),
    ("was not actively exploited", False),
    ("is not exploited", False),
    ("may not be actively exploited", False),
]


@pytest.mark.parametrize("predicate,exclude", DENIALS)
def test_exact_current_exclusion(predicate, exclude):
    r = parse_assertions(f"{A} {predicate}.")[0]
    assert not r.unsupported
    assert r.assertion_projection.excludes == (("active",) if exclude else ())
    assert r.status == (
        "not_observed" if predicate == "is not exploited" else "unknown"
    )


@pytest.mark.parametrize(
    "wrapper",
    [
        "There is no evidence that {}.",
        "The vendor has not found evidence that {}.",
        "It is possible that {}.",
        "If reports are accurate, {}.",
        "{} if reports are accurate.",
        "The vendor denied that it has found evidence that {}.",
    ],
)
def test_qualified_absence_never_excludes(wrapper):
    r = parse_assertions(wrapper.format(f"{A} is actively exploited"))[0]
    assert not r.unsupported and not r.assertion_projection.excludes


@pytest.mark.parametrize("predicate,exclude", DENIALS)
@pytest.mark.parametrize("reverse", [False, True])
def test_same_cve_across_sources(predicate, exclude, reverse):
    xs = [
        article(f"{A} is exploited.", link="https://example.test/positive"),
        article(f"{A} {predicate}.", link="https://example.test/qualified"),
    ]
    if reverse:
        xs.reverse()
    a = assess_exploitation(xs, [A])
    assert not a.unsupported
    assert a.status == (
        "unknown" if exclude or predicate == "is not exploited" else "active"
    )
    assert a.conflicting == (exclude or predicate == "is not exploited")
    assert {r.source_text for r in a.relations} == {x["content"] for x in xs}


@pytest.mark.parametrize(
    "text,status,conflict",
    [
        (
            f"{A} and {B} were exploited.\n\n{A} and {B} are not actively exploited.",
            "observed",
            False,
        ),
        (
            f"{A} and {B} are exploited.\n\n{A} and {B} are not actively exploited.",
            "unknown",
            True,
        ),
        (
            f"{A} was exploited.\n\n{A} and {B} are not actively exploited.",
            "unknown",
            False,
        ),
        (f"{A} is exploited.\n\n{B} is not actively exploited.", "unknown", False),
        (
            f"{A} and {B} are exploited.\n\n{A} and {B} are not currently widely exploited.",
            "active",
            False,
        ),
    ],
)
def test_joint_coverage(text, status, conflict):
    a = assess_exploitation([article(text)], [A, B])
    assert not a.unsupported
    assert a.status == status and a.conflicting == conflict


PREFIX = [
    "actively",
    "also",
    "currently",
    "extensively",
    "first",
    "likely",
    "never",
    "newly",
    "not",
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
]


@pytest.mark.parametrize("word", PREFIX)
def test_prefix_inventory_preserves_exact_terms(word):
    text = f"is {word} exploited"
    f = bind_predicate(text, voice="vulnerability")
    s = f.scope
    assert s.text == text
    tokens = [*s.terms, *s.operators]
    assert any(t.text == word and s.text[t.start : t.end] == word for t in tokens)
    assert f.supported == (word != "observed")


TAILS = [
    ("as investigators confirmed yesterday", "reporter"),
    ("the vendor said on June 4", "reporter"),
    ("last year", "event"),
    ("in June", "event"),
    ("for two years", "event"),
    ("over the weekend", "event"),
    ("after public disclosure", "event"),
    ("after it was publicly disclosed", "event"),
    ("after the vendor had issued an update", "event"),
    ("because a patch was unavailable", "event"),
    ("often", "event"),
    ("widely", "event"),
    ("in the wild", "event"),
    ("in Example Platform", "event"),
    ("against Example's own cloud service", "event"),
    ("as a zero-day", "event"),
    ("for the gateway", "event"),
    ("to gain privileges", "event"),
    ("to run arbitrary code with root privileges on Example systems", "event"),
    ("to install custom malware on vulnerable Example appliances", "event"),
    ("by attackers", "event"),
]


@pytest.mark.parametrize("tail,owner", TAILS)
def test_all_tail_productions_retain_owner_and_span(tail, owner):
    text = "was exploited " + tail
    f = bind_predicate(text, voice="vulnerability")
    assert f.supported
    terms = [t for t in f.scope.terms if t.text == tail]
    assert len(terms) == 1 and terms[0].owner == owner
    t = terms[0]
    assert f.scope.text[t.start : t.end] == tail


@pytest.mark.parametrize(
    "text,expected",
    [
        (
            f"{A} is not widely exploited and weaponized in the wild.",
            ["unknown", "unknown"],
        ),
        (
            f"{A} is not widely exploited and is weaponized in the wild.",
            ["unknown", "active"],
        ),
        (
            f"{A} is not only widely exploited but weaponized in the wild.",
            ["active", "active"],
        ),
    ],
)
def test_scope_inheritance(text, expected):
    rs = parse_assertions(text)
    assert [r.status for r in rs] == expected
    if " and weaponized" in text:
        assert rs[0].scopes[0] in rs[1].scopes
    elif " and is" in text:
        assert rs[0].scopes[0] not in rs[1].scopes
    for r in rs:
        for s in r.scopes:
            assert all(
                s.text[t.start : t.end] == t.text for t in [*s.terms, *s.operators]
            )


@pytest.mark.parametrize(
    "text,term,owner",
    [
        (f"Active exploitation of {A} has not been observed.", "Active", "event"),
        (f"Exploitation of {A} has not been observed widely.", "widely", "evidence"),
        (
            f"There is no evidence of {A} being exploited extensively.",
            "extensively",
            "event",
        ),
        (
            f"The vendor has not found evidence that {A} is widely exploited.",
            "widely",
            "event",
        ),
        (
            f"Example Group has not widely gained access by exploiting a vulnerability ({A}).",
            "widely",
            "event",
        ),
        (
            "The advisory lists two known flaws that it says were not successfully exploited.",
            "successfully",
            "event",
        ),
    ],
)
def test_nonverbal_adapters_preserve_qualified_owner(text, term, owner):
    r = parse_assertions(text)[0]
    assert not r.unsupported and r.status == "unknown"
    assert any(t.text == term and t.owner == owner for s in r.scopes for t in s.terms)
    assert not r.assertion_projection.excludes


@pytest.mark.parametrize(
    "text",
    [
        f"There is no evidence that {A} is actively exploited.",
        f"There is no evidence of {A} being exploited actively.",
    ],
)
def test_absence_operator_retains_exact_original_span(text):
    r = parse_assertions(text)[0]
    ops = [(s, o) for s in r.scopes for o in s.operators if o.kind == "absence"]
    assert len(ops) == 1
    s, o = ops[0]
    assert s.text[o.start : o.end] == o.text and "no evidence" in o.text

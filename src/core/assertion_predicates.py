"""One finite verbal frame owns operators, event, target and residual spans."""

from dataclasses import dataclass, replace
import re

from .cve import extract_cve_ids
from .assertion_bindings import CVE_LIST as CVE_LIST, TargetBinding, bind_target
from .assertion_qualifiers import QualifierSpan, bind_qualifiers

POSSIBILITY_WORDS = ("potentially", "likely", "possibly", "probably", "unlikely")
TOPIC = re.compile(r"\b(?:exploit\w*|weaponiz\w*)\b", re.I)
BOUNDARY = re.compile(
    r"([;,]\s*(?:and|but|while|whereas)\b|[;,]|\b(?:and|but|while|whereas)\b)", re.I
)
CONDITION = re.compile(r"\b(?:if|unless)\b", re.I)
REQUIRED_ADJUNCT = re.compile(
    r"\b(?:if|unless|when|until|once|although|though|only|provided|depending)\b", re.I
)
PREDICATE_MODIFIERS = frozenset(POSSIBILITY_WORDS) | {
    "also",
    "currently",
    "now",
    "still",
    "not",
    "never",
    "actively",
    "newly",
    "recently",
    "widely",
    "publicly",
    "successfully",
    "extensively",
}
FINITE_PREDICATE_HEADS = frozenset(
    {
        "is",
        "are",
        "was",
        "were",
        "has",
        "have",
        "had",
        "may",
        "might",
        "could",
        "can",
        "will",
        "would",
    }
)
# Complete auxiliary productions have explicit semantics. Perfect evidence
# without an owned qualification is deliberately unresolved; unknown chains
# never acquire a state from an incidental auxiliary elsewhere in the prefix.
AUXILIARY_STATES = {
    **{(word,): "current" for word in ("is", "are")},
    **{(word, "being"): "current" for word in ("is", "are")},
    **{(word,): "past" for word in ("was", "were")},
    **{(word, "being"): "past" for word in ("was", "were")},
    ("had", "been"): "past",
    ("has", "been"): "unspecified",
    ("have", "been"): "unspecified",
    ("have", "begun"): "past",
    ("has", "begun"): "past",
    ("had", "begun"): "past",
    **{
        (word, *tail): "possible"
        for word in ("may", "might", "could", "would")
        for tail in ((), ("be",), ("have", "been"))
    },
    **{
        (word, "known", "to", "be"): state
        for word, state in (
            ("is", "current"),
            ("are", "current"),
            ("was", "past"),
            ("were", "past"),
        )
    },
}

PARTICIPIAL_PREDICATE_HEADS = frozenset(
    {
        "exploited",
        "weaponized",
        "affected",
        "vulnerable",
        "exploitable",
    }
)
PREDICATE_HEADS = (
    FINITE_PREDICATE_HEADS | PARTICIPIAL_PREDICATE_HEADS | {"be", "been", "being"}
)


@dataclass(frozen=True)
class PredicateFrame:
    text: str
    end: int
    operator_span: tuple[int, int]
    event_span: tuple[int, int]
    target: TargetBinding
    adjunct_span: tuple[int, int]
    qualifiers: tuple[QualifierSpan, ...]
    verb: str
    kind: str
    tense: str
    aspect: str
    finite: bool
    modal: str
    polarity: str
    supported: bool
    starts_relation: bool
    inherits_subject: bool
    requires_inheritance: bool = False
    correlative: tuple[str, str] | None = None


CONTINUATION = {"continue": "current", "continues": "current", "continued": "past"}
EVENTS = frozenset({"exploit", "exploited", "exploiting", "weaponized"})
CONTEXT = frozenset(
    {
        "affected",
        "vulnerable",
        "exploitable",
        "allows",
        "allow",
        "permits",
        "permit",
        "patched",
        "disclosed",
    }
)
AUXILIARY_WORDS = FINITE_PREDICATE_HEADS | {
    "be",
    "been",
    "being",
    "begun",
    "known",
    "to",
}
PREFIX_WORDS = PREDICATE_MODIFIERS | AUXILIARY_WORDS | {"yet", "observed", "first"}


def bind_predicate(
    text: str, *, voice: str = "unscoped", modal: str = "", negative: bool = False
) -> PredicateFrame:
    """Return one complete frame or an explicit unsupported required frame.

    Coordination consumes this result too. It never has its own operator list
    or lexical scan. A recognized start is not a promise of a supported state.
    """
    end = len(text.rstrip(" .!?"))
    tokens = list(re.finditer(r"\S+", text[:end]))
    words = [token.group().casefold() for token in tokens]
    i, finite, correlative = 0, False, None
    tense, aspect, auxiliaries = "unspecified", "simple", []
    supported = True
    initial = words[0] if words else ""
    # This owner interprets exploitation predicates, not arbitrary prose that
    # happens to contain an aspect verb (e.g. "continue to be safe to use").
    continuation = initial in CONTINUATION and bool(TOPIC.search(text))
    if continuation:
        aspect, tense, finite = "continuative", CONTINUATION[initial], True
        i = 1
        if i < len(words) and words[i] == "to":
            i += 1
        else:
            supported = False
        passive = i < len(words) and words[i] == "be"
        if passive:
            i += 1
        supported &= voice != "actor" if passive else voice == "actor"
        while i < len(words) and words[i] in PREDICATE_MODIFIERS:
            if words[i] in {"not", "never"}:
                negative = True
            elif words[i] in POSSIBILITY_WORDS:
                modal = modal or "possible"
            i += 1
        supported &= not negative
        expected_event = "exploited" if passive else "exploit"
    else:
        while i < len(words) and words[i] in PREFIX_WORDS:
            word = words[i]
            i += 1
            if word in AUXILIARY_WORDS:
                auxiliaries.append(word)
            if (
                word == "not"
                and i < len(words)
                and words[i] in {"only", "just", "merely", "simply"}
            ):
                i += 1
                correlative = (modal, "negative" if negative else "affirmative")
            elif word in {"not", "never"}:
                negative = True
            elif word in POSSIBILITY_WORDS or word in {
                "may",
                "might",
                "could",
                "would",
            }:
                modal = modal or "possible"
            finite |= word in FINITE_PREDICATE_HEADS
        state = AUXILIARY_STATES.get(tuple(auxiliaries))
        if state == "possible":
            modal = modal or "possible"
        elif state:
            tense = state
    event_start = tokens[i].start() if i < len(tokens) else end
    event_end = tokens[i].end() if i < len(tokens) else end
    verb = words[i] if i < len(words) else ""
    argument_start = tokens[i + 1].start() if i + 1 < len(tokens) else end
    argument = text[argument_start:end]
    target = TargetBinding("", argument_start, argument_start)
    if voice == "actor":
        target = bind_target(text[:end], argument_start, implicit=True) or target
        if target.kind != "empty":
            argument_start = target.end
            while argument_start < end and text[argument_start].isspace():
                argument_start += 1
            argument = text[argument_start:end]
        if not continuation:
            if verb == "exploited" and not finite:
                tense = "past"
            elif verb == "exploit" and not auxiliaries:
                tense = "current"
    if (
        not continuation
        and not auxiliaries
        and verb == "weaponized"
        and re.fullmatch(r"in (?:the wild|attacks)", argument, re.I)
    ):
        tense = "current"
    qualifiers = bind_qualifiers(argument, complement=verb)
    known = verb in EVENTS
    kind = "assertion" if known or TOPIC.search(text) else "context"
    if continuation:
        supported &= verb == expected_event and qualifiers.complete
        supported &= voice != "actor" or target.kind != "empty"
    elif verb == "under" and re.fullmatch(
        r"(?:limited, targeted|active) exploitation", argument, re.I
    ):
        verb, kind = "exploitation", "assertion"
        supported &= AUXILIARY_STATES.get(tuple(auxiliaries)) is not None
    elif verb == "exploitable":
        supported &= not argument and tuple(auxiliaries) in {
            ("is",),
            ("are",),
            ("was",),
            ("were",),
        }
        kind, modal = ("context" if supported else "assertion"), "capability"
    else:
        supported &= not (
            known and auxiliaries and AUXILIARY_STATES.get(tuple(auxiliaries)) is None
        )
        supported &= not (known and not qualifiers.complete)
        supported &= not (not known and verb not in CONTEXT and TOPIC.search(text))
    # Target identities are never borrowed from an adjunct or another object.
    if extract_cve_ids(argument):
        supported = False
    requires_inheritance = bool(
        supported
        and known
        and not finite
        and tense == "unspecified"
        and not modal
        and not negative
    )
    if kind == "assertion" and not (modal or negative or tense in {"current", "past"}):
        supported = False
    # The same recognized frame supplies all verbal boundary decisions. An
    # adjective followed by a noun cannot inherit the preceding CVE subject.
    inherits = (
        (finite or verb in PREDICATE_HEADS or initial in {"be", "been", "being"})
        and (verb not in PARTICIPIAL_PREDICATE_HEADS or qualifiers.complete)
        and (not continuation or verb == expected_event)
    )
    starts = inherits or (continuation and bool(TOPIC.search(text)))
    return PredicateFrame(
        text=text,
        end=len(text),
        operator_span=(0, len(text[:event_start].rstrip())),
        event_span=(event_start, event_end),
        target=target,
        adjunct_span=(argument_start, end),
        qualifiers=tuple(
            replace(
                span, start=span.start + argument_start, end=span.end + argument_start
            )
            for span in qualifiers.spans
        ),
        verb=verb,
        kind=kind,
        tense=tense,
        aspect=aspect,
        finite=finite,
        modal=modal,
        polarity="negative" if negative else "affirmative",
        supported=bool(supported),
        starts_relation=bool(starts),
        inherits_subject=bool(inherits),
        requires_inheritance=requires_inheritance,
        correlative=correlative,
    )

"""One finite verbal frame owns operators, event, target and residual spans."""

from dataclasses import dataclass, replace
import re

from .cve import extract_cve_ids
from .assertion_bindings import CVE_LIST as CVE_LIST, TargetBinding, bind_target
from .assertion_qualifiers import QualifierSpan, bind_qualifiers
from .relations import temporal_compatible

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


@dataclass(frozen=True)
class OperatorProduction:
    operators: tuple[str, ...]
    voice: str
    events: tuple[str, ...]
    tense: str
    aspect: str = "simple"
    modal: str = ""
    allows_negation: bool = True


# One production owns the entire operator AND grammatical event complement.
# Coordination consumes the resulting frame; it has no independent grammar.
OPERATOR_PRODUCTIONS = (
    OperatorProduction((), "actor", ("exploit",), "current"),
    OperatorProduction((), "actor", ("exploited",), "past"),
    OperatorProduction((), "vulnerability", ("exploited", "weaponized"), "unspecified"),
    *(
        OperatorProduction((word,), voice, events, tense)
        for word, tense in (
            ("is", "current"),
            ("are", "current"),
            ("was", "past"),
            ("were", "past"),
        )
        for voice, events in (
            ("actor", ("exploiting",)),
            ("vulnerability", ("exploited", "weaponized", "under")),
        )
    ),
    *(
        OperatorProduction(
            (word, "being"), "vulnerability", ("exploited", "weaponized"), tense
        )
        for word, tense in (
            ("is", "current"),
            ("are", "current"),
            ("was", "past"),
            ("were", "past"),
        )
    ),
    *(
        OperatorProduction((word, "been"), voice, events, tense)
        for word, tense in (
            ("has", "unspecified"),
            ("have", "unspecified"),
            ("had", "past"),
        )
        for voice, events in (
            ("actor", ("exploiting",)),
            ("vulnerability", ("exploited", "weaponized", "under")),
        )
    ),
    *(
        OperatorProduction(
            (word, "begun", *complement),
            voice,
            events,
            "past",
            "initiation",
            allows_negation=False,
        )
        for word in ("has", "have", "had")
        for complement, voice, events in (
            ((), "actor", ("exploiting",)),
            (("to",), "actor", ("exploit",)),
            (("to", "be"), "vulnerability", ("exploited",)),
            (("being",), "vulnerability", ("exploited",)),
        )
    ),
    *(
        OperatorProduction(
            (word, *complement), voice, events, "unspecified", modal="possible"
        )
        for word in ("may", "might", "could", "would")
        for complement, voice, events in (
            ((), "actor", ("exploit",)),
            (("be",), "actor", ("exploiting",)),
            (("be",), "vulnerability", ("exploited", "weaponized", "under")),
            (("have", "been"), "actor", ("exploiting",)),
            (("have", "been"), "vulnerability", ("exploited", "weaponized", "under")),
        )
    ),
    *(
        OperatorProduction((word, "known", "to", "be"), voice, events, tense)
        for word, tense in (
            ("is", "current"),
            ("are", "current"),
            ("was", "past"),
            ("were", "past"),
        )
        for voice, events in (
            ("actor", ("exploiting",)),
            ("vulnerability", ("exploited", "weaponized", "under")),
        )
    ),
    *(
        OperatorProduction(
            (word, "to", *complement),
            voice,
            events,
            tense,
            "continuative",
            allows_negation=False,
        )
        for word, tense in (
            ("continue", "current"),
            ("continues", "current"),
            ("continued", "past"),
        )
        for complement, voice, events in (
            ((), "actor", ("exploit",)),
            (("be",), "vulnerability", ("exploited",)),
        )
    ),
)


def operator_production(operators, voice, event):
    return next(
        (
            rule
            for rule in OPERATOR_PRODUCTIONS
            if rule.operators == tuple(operators)
            and rule.voice == ("vulnerability" if voice == "unscoped" else voice)
            and event in rule.events
        ),
        None,
    )


def operator_tense(operators):
    """Closed non-event compositions reuse their already bound operator."""
    if not operators:
        return "unspecified"
    return next(
        (
            rule.tense
            for rule in OPERATOR_PRODUCTIONS
            if rule.operators == tuple(operators)
        ),
        "unspecified",
    )


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


ASPECT_HEADS = frozenset(
    rule.operators[0] for rule in OPERATOR_PRODUCTIONS if rule.aspect == "continuative"
)
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
AUXILIARY_WORDS = (
    FINITE_PREDICATE_HEADS
    | ASPECT_HEADS
    | {
        "be",
        "been",
        "being",
        "begun",
        "known",
        "to",
    }
)
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
    correlative_operator_count = 0
    tense, aspect, auxiliaries = "unspecified", "simple", []
    supported = True
    initial = words[0] if words else ""
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
            correlative_operator_count = len(auxiliaries)
        elif word in {"not", "never"}:
            negative = True
        elif word in POSSIBILITY_WORDS:
            modal = modal or "possible"
        finite |= word in FINITE_PREDICATE_HEADS or word in ASPECT_HEADS
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
    rule = operator_production(auxiliaries, voice, verb)
    governing = rule
    if rule:
        tense, aspect = rule.tense, rule.aspect
        modal = modal or rule.modal
        supported &= rule.allows_negation or not negative
    else:
        tense = operator_tense(auxiliaries)
        if verb in CONTEXT:
            # The same recognized operator can qualify a context clause that
            # supplies an explicitly coordinated event's modal scope.
            context_rule = (
                next(
                    (
                        item
                        for item in OPERATOR_PRODUCTIONS
                        if item.operators == tuple(auxiliaries)
                    ),
                    None,
                )
                if auxiliaries
                else None
            )
            if context_rule:
                governing = context_rule
                modal = modal or context_rule.modal
    if correlative and correlative_operator_count and governing and governing.modal:
        # A governing operator before the correlative boundary qualifies both
        # predicates. A modifier inside its first branch does not move scope.
        correlative = (correlative[0] or governing.modal, correlative[1])
    if (
        not auxiliaries
        and verb == "weaponized"
        and re.fullmatch(r"in (?:the wild|attacks)", argument, re.I)
    ):
        tense = "current"
    qualifiers = bind_qualifiers(argument, complement=verb)
    known = verb in EVENTS
    kind = "assertion" if known or TOPIC.search(text) else "context"
    if initial in ASPECT_HEADS and rule is None and kind == "context":
        # An aspect word in unrelated prose is not an exploitation relation.
        # Required malformed exploitation still advertises its boundary.
        finite = False
    if verb == "under" and re.fullmatch(
        r"(?:limited, targeted|active) exploitation", argument, re.I
    ):
        verb, kind = "exploitation", "assertion"
        supported &= rule is not None
    elif verb == "exploitable":
        supported &= not argument and tuple(auxiliaries) in {
            ("is",),
            ("are",),
            ("was",),
            ("were",),
        }
        kind, modal = ("context" if supported else "assertion"), "capability"
    else:
        supported &= not (known and rule is None)
        supported &= not (known and not qualifiers.complete)
        supported &= not (not known and verb not in CONTEXT and TOPIC.search(text))
    if kind == "assertion":
        supported &= temporal_compatible(
            tuple(q.temporal for q in qualifiers.spans if q.temporal), tense
        )
    if known and voice == "actor":
        supported &= target.kind != "empty"
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
        finite or verb in PREDICATE_HEADS or initial in {"be", "been", "being"}
    ) and (verb not in PARTICIPIAL_PREDICATE_HEADS or qualifiers.complete)
    inherits &= initial not in ASPECT_HEADS or rule is not None
    starts = inherits or (initial in ASPECT_HEADS and bool(TOPIC.search(text)))
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

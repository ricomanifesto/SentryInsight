"""One finite verbal frame owns operators, event, target and residual spans."""

from dataclasses import dataclass, replace
import re

from .cve import extract_cve_ids
from .exploitation_contract import (
    EventBinding,
    TOPIC as TOPIC,
    bind_event,
    has_required_event,
)
from .assertion_bindings import CVE_LIST as CVE_LIST, TargetBinding, bind_target
from .assertion_qualifiers import (
    QualifierSpan,
    TIME_DIRECTIONS,
    assertion_scope,
    bind_qualifiers,
    modifier_term,
    qualifier_terms,
)
from .relations import (
    AssertionScope,
    ObservationConstruction,
    ScopeOperator,
    ScopeTerm,
    TemporalConstraint,
    temporal_compatible,
)

POSSIBILITY_WORDS = ("potentially", "likely", "possibly", "probably", "unlikely")
BOUNDARY = re.compile(
    r"([;,]\s*(?:and|but|while|whereas)\b|[;,]|\b(?:and|but|while|whereas)\b)", re.I
)
CONDITION = re.compile(r"\b(?:only\s+if|if|unless)\b", re.I)
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
    knowledge_head: int | None = None


# These established non-perfect constructions retain their bounded policies.
# Perfect auxiliaries compose with morphological complements below.
_NONPERFECT_PRODUCTIONS = (
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
        )
    ),
    *(
        OperatorProduction(
            (word, "known", "to", "be"), voice, events, tense, knowledge_head=1
        )
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


def _perfect_operator(operators, voice):
    """Bind finite reference time, perfect aspect and a voice-owned complement.

    Modal -> have -> participle and finite-have -> participle share the same
    transition. Been introduces an existing passive/state or progressive
    complement; it never licenses an arbitrary following verb.
    """
    words = tuple(operators)
    modal = ""
    if words and words[0] in {"may", "might", "could", "would"}:
        modal, words = "possible", words[1:]
        if not words or words[0] != "have":
            return None
    if not words or words[0] not in {"has", "have", "had"}:
        return None
    tense = "unspecified" if modal else "past" if words[0] == "had" else "current"
    complement = words[1:]
    if not complement and voice == "actor":
        events, aspect = ("exploited",), "perfect"
    elif complement == ("been",):
        if voice == "actor":
            events, aspect = ("exploiting",), "perfect_progressive"
        elif voice == "vulnerability":
            events, aspect = ("exploited", "weaponized", "under"), "perfect"
        else:
            return None
    else:
        return None
    return OperatorProduction(tuple(operators), voice, events, tense, aspect, modal)


# Exhaustive conformance inventory, derived from the same bounded transition.
# Recognition does not search this inventory for perfect operator strings.
OPERATOR_PRODUCTIONS = _NONPERFECT_PRODUCTIONS + tuple(
    rule
    for finite in (("has",), ("have",), ("had",))
    + tuple((modal, "have") for modal in ("may", "might", "could", "would"))
    for complement, voice in (
        ((), "actor"),
        (("been",), "actor"),
        (("been",), "vulnerability"),
    )
    if (rule := _perfect_operator((*finite, *complement), voice)) is not None
)


def operator_production(operators, voice, event):
    voice = "vulnerability" if voice == "unscoped" else voice
    if perfect := _perfect_operator(operators, voice):
        return perfect if event in perfect.events else None
    return next(
        (
            rule
            for rule in _NONPERFECT_PRODUCTIONS
            if rule.operators == tuple(operators)
            and rule.voice == voice
            and event in rule.events
        ),
        None,
    )


def operator_tense(operators):
    """Closed non-event compositions reuse their already bound operator."""
    if not operators:
        return "unspecified"
    if perfect := _perfect_operator(operators, "actor"):
        return perfect.tense
    return next(
        (
            rule.tense
            for rule in _NONPERFECT_PRODUCTIONS
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
    operators: tuple[str, ...] = ()
    scope: AssertionScope = AssertionScope("")
    temporal: tuple[TemporalConstraint, ...] = ()
    event_binding: EventBinding | None = None
    observation: ObservationConstruction | None = None

    @property
    def capability(self):
        """A simple modal passive is distinct from a possible past event."""
        return (
            self.supported
            and self.kind == "assertion"
            and self.modal == "possible"
            and self.aspect == "simple"
            and len(self.operators) == 2
            and self.operators[-1] == "be"
            and self.verb == "exploited"
        )


ASPECT_HEADS = frozenset(
    rule.operators[0] for rule in OPERATOR_PRODUCTIONS if rule.aspect == "continuative"
)
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


def _observation_frame(text, voice, modal, negative):
    """Reserve a perfect-seen operand before admitting its complete grammar."""
    start = re.match(
        r"(?P<aux>has|have|had)\b(?P<middle>(?:\s+[A-Za-z]+)*?)"
        r"\s+(?P<predicate>seen)\b",
        text,
        re.I,
    )
    if start is None:
        return None
    neg = re.fullmatch(r"\s*(not|never)\s*", start["middle"], re.I)
    neg_span = (
        (start.start("middle") + neg.start(1), start.start("middle") + neg.end(1))
        if neg
        else None
    )
    nominal = re.match(
        r"\s+(?P<nominal>(?:(?P<activity>active)\s+)?(?P<event>exploitation))"
        r"(?=$|[\s,.!?])",
        text[start.end() :],
        re.I,
    )

    def span(name):
        if nominal is None or nominal.start(name) < 0:
            return (start.end(), start.end())
        return (start.end() + nominal.start(name), start.end() + nominal.end(name))

    observation = ObservationConstruction(
        text,
        start.span("aux"),
        start.span("predicate"),
        span("nominal"),
        span("event"),
        neg_span,
        span("activity") if nominal and nominal["activity"] else None,
    )
    end = len(text.rstrip(" .!?"))
    tail_start = span("nominal")[1]
    qualifiers = bind_qualifiers(text[tail_start:end])
    temporal = tuple(q.temporal for q in qualifiers.spans if q.temporal)
    terms = list(qualifier_terms(text, qualifiers.spans, offset=tail_start))
    if observation.activity_span:
        left, right = observation.activity_span
        terms.append(ScopeTerm(text[left:right], left, right, "activity"))
    operators = (
        (ScopeOperator(text[slice(*neg_span)], *neg_span, "negation", "event"),)
        if neg_span
        else ()
    )
    scope = assertion_scope(text, terms, operators, event_tense="past")
    supported = bool(
        observation.supported
        and voice in {"vulnerability", "unscoped"}
        and not modal
        and not negative
        and qualifiers.complete
        and all(q.kind in {"temporal", "reporter"} for q in qualifiers.spans)
        and all(
            t.owner == "reporter" or t.direction in {"past", "context"}
            for t in temporal
        )
        and temporal_compatible(temporal, "past")
        and scope.supported
        and not extract_cve_ids(text[tail_start:])
    )
    return PredicateFrame(
        text=text,
        end=len(text),
        operator_span=(0, start.start("predicate")),
        event_span=span("event"),
        target=TargetBinding("", tail_start, tail_start),
        adjunct_span=(tail_start, end),
        qualifiers=tuple(
            replace(q, start=q.start + tail_start, end=q.end + tail_start)
            for q in qualifiers.spans
        ),
        verb="exploitation",
        kind="assertion",
        tense="past",
        aspect="perfect-observation",
        finite=True,
        modal=modal,
        polarity=observation.polarity,
        supported=supported,
        starts_relation=True,
        inherits_subject=True,
        operators=(start["aux"].casefold(),),
        scope=scope,
        temporal=temporal,
        observation=observation,
    )


def bind_predicate(
    text: str, *, voice: str = "unscoped", modal: str = "", negative: bool = False
) -> PredicateFrame:
    """Return one complete frame or an explicit unsupported required frame.

    Coordination consumes this result too. It never has its own operator list
    or lexical scan. A recognized start is not a promise of a supported state.
    """
    if observation := _observation_frame(text, voice, modal, negative):
        return observation
    end = len(text.rstrip(" .!?"))
    tokens = list(re.finditer(r"\S+", text[:end]))
    words = [token.group().casefold() for token in tokens]
    i, finite, correlative = 0, False, None
    correlative_operator_count = 0
    tense, aspect, auxiliaries = "unspecified", "simple", []
    auxiliary_spans = []
    inherited_negative = negative
    supported = True
    terms, scope_operators, prefix_time = [], [], []
    initial = words[0] if words else ""
    while i < len(words) and words[i] in PREFIX_WORDS:
        word = words[i]
        token = tokens[i]
        i += 1
        if word in AUXILIARY_WORDS:
            auxiliaries.append(word)
            auxiliary_spans.append((token.start(), token.end()))
        if (
            word == "not"
            and i < len(words)
            and words[i] in {"only", "just", "merely", "simply"}
        ):
            scope_operators.append(
                ScopeOperator(
                    text[token.start() : tokens[i].end()],
                    token.start(),
                    tokens[i].end(),
                    "correlative",
                    "coordination",
                )
            )
            i += 1
            correlative = (modal, "negative" if negative else "affirmative")
            correlative_operator_count = len(auxiliaries)
        elif word in {"not", "never"}:
            negative = True
            scope_operators.append(
                ScopeOperator(
                    token.group(), token.start(), token.end(), "negation", "event"
                )
            )
        elif word in POSSIBILITY_WORDS:
            modal = modal or "possible"
        if word not in AUXILIARY_WORDS and word not in {"not", "never"}:
            terms.append(modifier_term(text, token.start(), token.end()))
            if word in TIME_DIRECTIONS:
                prefix_time.append(
                    TemporalConstraint("event", TIME_DIRECTIONS[word], token.group())
                )
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
    if governing and governing.knowledge_head is not None:
        head_start, head_end = auxiliary_spans[governing.knowledge_head]
        # The matched complete production owns this boundary. Negation and
        # modifiers before its head qualify knowledge, not the embedded event.
        scope_operators = [
            (
                replace(o, target="knowledge")
                if o.kind == "negation" and o.end <= head_start
                else o
            )
            for o in scope_operators
        ]
        terms = [
            replace(term, owner="knowledge") if term.end <= head_start else term
            for term in terms
        ]
        scope_operators.append(
            ScopeOperator(
                text[head_start:head_end], head_start, head_end, "knowledge", "event"
            )
        )
        scope_operators.sort(key=lambda operator: operator.start)
        negative = inherited_negative or any(
            o.kind == "negation" and o.target == "event" for o in scope_operators
        )
        if correlative:
            boundary = next(
                o.start for o in reversed(scope_operators) if o.kind == "correlative"
            )
            correlative = (
                correlative[0],
                (
                    "negative"
                    if inherited_negative
                    or any(
                        o.kind == "negation"
                        and o.target == "event"
                        and o.end <= boundary
                        for o in scope_operators
                    )
                    else "affirmative"
                ),
            )
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
    event = bind_event(text, (event_start, event_end), (argument_start, end))
    if event.descriptor and event.descriptor.complement:
        # Exact nominal morphology owns its punctuation and intrinsic qualifier;
        # the ordinary qualifier owner consumes any following temporal/role tail.
        argument_start = event.complement_span[1]
        while argument_start < end and text[argument_start].isspace():
            argument_start += 1
        argument = text[argument_start:end]
    qualifiers = bind_qualifiers(argument, complement=verb)
    known = event.descriptor is not None
    kind = "context" if event.kind == "context" else "assertion"
    if initial in ASPECT_HEADS and rule is None and kind == "context":
        # An aspect word in unrelated prose is not an exploitation relation.
        # Required malformed exploitation still advertises its boundary.
        finite = False
    if event.descriptor and event.descriptor.complement:
        start, stop = event.qualifier_span
        terms.append(
            ScopeTerm(text[start:stop], start, stop, event.descriptor.qualifier_kind)
        )
        verb = "exploitation"
        supported &= rule is not None and qualifiers.complete
        if qualifiers.complete and temporal_compatible(
            tuple(q.temporal for q in qualifiers.spans if q.temporal), tense, aspect
        ):
            event = replace(event, kind="complete")
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
        # A context verb cannot consume a required event elsewhere in its
        # argument. Recognition without a bound complement is never admission.
        supported &= event.kind != "required"
    temporal = tuple(prefix_time) + tuple(
        q.temporal for q in qualifiers.spans if q.temporal
    )
    scope = assertion_scope(
        text,
        (*terms, *qualifier_terms(text, qualifiers.spans, offset=argument_start)),
        scope_operators,
        event_tense=tense,
    )
    if kind == "assertion":
        supported &= scope.supported and temporal_compatible(temporal, tense, aspect)
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
    starts = inherits or (initial in ASPECT_HEADS and has_required_event(text))
    return PredicateFrame(
        operators=tuple(auxiliaries),
        scope=scope,
        temporal=temporal,
        text=text,
        end=len(text),
        operator_span=(0, len(text[:event_start].rstrip())),
        event_span=(event_start, event_end),
        event_binding=event,
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

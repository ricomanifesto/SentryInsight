"""One finite verbal frame owns operators, event, target and residual spans."""

from dataclasses import dataclass, replace
import re

from .cve import extract_cve_ids
from .exploitation_contract import (
    EventBinding,
    TOPIC as TOPIC,
    bind_event,
    has_required_event,
    event_forms,
    requires_attack_context,
)
from .assertion_bindings import (
    CVE_LIST as CVE_LIST,
    SubjectBinding,
    TargetBinding,
    bind_target,
)
from .assertion_qualifiers import (
    EPISTEMIC_MODIFIERS,
    REPORTED_MODIFIERS,
    REPORTED_PATTERN,
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

BOUNDARY = re.compile(
    r"([;,]\s*(?:and|but|while|whereas)\b|[;,]|\b(?:and|but|while|whereas)\b)", re.I
)
CONDITION = re.compile(r"\b(?:only\s+if|if|unless)\b", re.I)
REQUIRED_ADJUNCT = re.compile(
    r"\b(?:if|unless|when|until|once|although|though|only|provided|depending)\b", re.I
)
PREDICATE_MODIFIERS = frozenset(EPISTEMIC_MODIFIERS) | {
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
        "do",
        "does",
        "did",
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


DO_SUPPORT = {
    "do": ("current", "plural"),
    "does": ("current", "singular"),
    "did": ("past", None),
}
OBSERVATION_FINITE = {
    "has": ("current", "singular"),
    "have": ("current", "plural"),
    "had": ("past", None),
}


# These established non-perfect constructions retain their bounded policies.
# Perfect auxiliaries compose with morphological complements below.
_NONPERFECT_PRODUCTIONS = (
    OperatorProduction(
        (), "actor", event_forms(("finite_present", "finite_present_3sg")), "current"
    ),
    OperatorProduction((), "actor", event_forms("past"), "past"),
    OperatorProduction(
        (),
        "vulnerability",
        event_forms("participle", ("exploit", "weaponize", "use")),
        "unspecified",
    ),
    *(
        OperatorProduction((word,), voice, events, tense)
        for word, tense in (
            ("is", "current"),
            ("are", "current"),
            ("was", "past"),
            ("were", "past"),
        )
        for voice, events in (
            ("actor", event_forms("progressive")),
            (
                "vulnerability",
                event_forms(
                    ("participle", "state"), ("exploit", "weaponize", "under", "use")
                ),
            ),
        )
    ),
    *(
        OperatorProduction(
            (word, "being"),
            "vulnerability",
            event_forms("participle", ("exploit", "weaponize", "use")),
            tense,
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
            ((), "actor", event_forms("progressive")),
            (("to",), "actor", event_forms("base")),
            (("to", "be"), "vulnerability", event_forms("participle")),
            (("being",), "vulnerability", event_forms("participle")),
        )
    ),
    *(
        OperatorProduction(
            (word, *complement), voice, events, "unspecified", modal="possible"
        )
        for word in ("may", "might", "could", "would")
        for complement, voice, events in (
            ((), "actor", event_forms("base")),
            (("be",), "actor", event_forms("progressive")),
            (
                ("be",),
                "vulnerability",
                event_forms(
                    ("participle", "state"), ("exploit", "weaponize", "under", "use")
                ),
            ),
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
            ("actor", event_forms("progressive")),
            (
                "vulnerability",
                event_forms(
                    ("participle", "state"), ("exploit", "weaponize", "under", "use")
                ),
            ),
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
            ((), "actor", event_forms("base")),
            (("be",), "vulnerability", event_forms("participle")),
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
        events, aspect = event_forms("participle"), "perfect"
    elif complement == ("been",):
        if voice == "actor":
            events, aspect = event_forms("progressive"), "perfect_progressive"
        elif voice == "vulnerability":
            events, aspect = (
                event_forms(
                    ("participle", "state"), ("exploit", "weaponize", "under", "use")
                ),
                "perfect",
            )
        else:
            return None
    else:
        return None
    return OperatorProduction(tuple(operators), voice, events, tense, aspect, modal)


_DO_PRODUCTIONS = tuple(
    OperatorProduction((word,), "actor", event_forms("base"), tense)
    for word, (tense, _) in DO_SUPPORT.items()
)

# Exhaustive conformance inventory, derived from the same bounded transition.
# Recognition does not search this inventory for perfect operator strings.
OPERATOR_PRODUCTIONS = (
    _NONPERFECT_PRODUCTIONS
    + tuple(
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
    + _DO_PRODUCTIONS
)


def operator_production(operators, voice, event):
    voice = "vulnerability" if voice == "unscoped" else voice
    if perfect := _perfect_operator(operators, voice):
        return perfect if event in perfect.events else None
    return next(
        (
            rule
            for rule in (*_NONPERFECT_PRODUCTIONS, *_DO_PRODUCTIONS)
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
            for rule in (*_NONPERFECT_PRODUCTIONS, *_DO_PRODUCTIONS)
            if rule.operators == tuple(operators)
        ),
        "unspecified",
    )


PARTICIPIAL_PREDICATE_HEADS = frozenset(
    {
        "exploited",
        "used",
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
class FiniteOperatorBinding:
    """A literal finite chain owns agreement and its complement requirement."""

    text: str
    spans: tuple[tuple[int, int], ...]
    construction: str
    subject: SubjectBinding | None
    production: OperatorProduction | None
    negations: tuple[tuple[int, int], ...] = ()

    @property
    def words(self):
        return tuple(self.text[start:end].casefold() for start, end in self.spans)

    @property
    def required_slot(self):
        if self.construction == "observed_passive":
            return "participle"
        return "base" if self.words and self.words[0] in DO_SUPPORT else None

    @property
    def supported(self):
        rule = self.production
        if (
            rule is None
            or self.words != rule.operators
            or any(not 0 <= start < end <= len(self.text) for start, end in self.spans)
            or any(
                left[1] >= right[0] for left, right in zip(self.spans, self.spans[1:])
            )
        ):
            return False
        if self.construction == "observed_passive":
            agreement = OBSERVATION_FINITE.get(self.words[0], (None, None))[1]
            return bool(
                self.subject
                and self.subject.kind == "vulnerability"
                and self.subject.number
                and (agreement is None or self.subject.number == agreement)
            )
        if self.words and self.words[0] in DO_SUPPORT:
            agreement = DO_SUPPORT[self.words[0]][1]
            return bool(
                self.subject
                and self.subject.kind == "actor"
                and self.subject.number
                and (agreement is None or self.subject.number == agreement)
                and len(self.negations) <= 1
                and all(start > self.spans[0][1] for start, _ in self.negations)
            )
        return True


def bind_operator(
    text,
    *,
    spans,
    subject,
    construction="event",
    voice="unscoped",
    event="",
    negations=(),
):
    words = tuple(text[start:end].casefold() for start, end in spans)
    if construction == "observed_passive":
        rule = (
            OperatorProduction(
                words,
                "vulnerability",
                ("observed",),
                OBSERVATION_FINITE[words[0]][0],
                "perfect",
            )
            if len(words) == 2 and words[0] in OBSERVATION_FINITE and words[1] == "been"
            else None
        )
    else:
        rule = operator_production(words, voice, event)
    return FiniteOperatorBinding(
        text, tuple(spans), construction, subject, rule, tuple(negations)
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
    operator_binding: FiniteOperatorBinding | None = None

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
        rf"(?:{REPORTED_PATTERN}\s+)*(?P<aux>has|have|had)\b(?P<middle>(?:\s+[A-Za-z]+)*?)"
        r"\s+(?P<predicate>seen)\b",
        text,
        re.I,
    )
    if start is None:
        return None
    tokens = list(re.finditer(r"\S+", text[: start.start("predicate")]))
    negatives = [
        token for token in tokens if token.group().casefold() in {"not", "never"}
    ]
    neg_span = negatives[0].span() if len(negatives) == 1 else None
    modifiers = tuple(
        modifier_term(text, *token.span(), owner="evidence")
        for token in tokens
        if token.group().casefold() in REPORTED_MODIFIERS
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
        modifiers,
    )
    end = len(text.rstrip(" .!?"))
    tail_start = span("nominal")[1]
    qualifiers = bind_qualifiers(text[tail_start:end])
    temporal = tuple(q.temporal for q in qualifiers.spans if q.temporal)
    terms = [*modifiers, *qualifier_terms(text, qualifiers.spans, offset=tail_start)]
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


def _position_qualifiers(text, qualifiers, offset, event):
    positioned = []
    for span in qualifiers:
        context = span.attack_context
        if context:
            quantity = context.cardinality
            context = replace(
                context,
                text=text,
                start=context.start + offset,
                end=context.end + offset,
                relation_span=tuple(x + offset for x in context.relation_span),
                head_span=tuple(x + offset for x in context.head_span),
                cardinality=(
                    replace(
                        quantity,
                        start=quantity.start + offset,
                        end=quantity.end + offset,
                    )
                    if quantity
                    else None
                ),
            )
            if event.attack_context is span.attack_context:
                event = replace(event, attack_context=context)
        positioned.append(
            replace(
                span,
                start=span.start + offset,
                end=span.end + offset,
                attack_context=context,
            )
        )
    return tuple(positioned), event


def _passive_observation_frame(text, voice, modal, negative, subject):
    """Bind observation and event as separate, literal propositions."""
    end = len(text.rstrip(" .!?"))
    tokens = list(re.finditer(r"\S+", text[:end]))
    words = [token.group().casefold() for token in tokens]
    # The envelope advertises ownership only; every component is validated below.
    outer_words = (
        set(OBSERVATION_FINITE) | {"been", "not", "never"} | REPORTED_MODIFIERS
    )
    i = 0
    while i < len(words) and words[i] in outer_words:
        i += 1
    if i == len(words) or words[i] != "observed":
        return None
    predicate = tokens[i].span()
    auxiliary = [
        t.span()
        for t in tokens[:i]
        if t.group().casefold() in OBSERVATION_FINITE or t.group().casefold() == "been"
    ]
    if tuple(text[slice(*s)].casefold() for s in auxiliary) not in {
        (finite, "been") for finite in OBSERVATION_FINITE
    }:
        return None
    outer_terms = tuple(
        modifier_term(text, *t.span(), owner="evidence")
        for t in tokens[:i]
        if t.group().casefold() in REPORTED_MODIFIERS
    )
    outer_negations = tuple(
        ScopeOperator(t.group(), *t.span(), "negation", "event")
        for t in tokens[:i]
        if t.group().casefold() in {"not", "never"}
    )
    operator = bind_operator(
        text,
        spans=auxiliary,
        subject=subject,
        construction="observed_passive",
        negations=[(o.start, o.end) for o in outer_negations],
    )
    outer = assertion_scope(
        text,
        outer_terms,
        outer_negations,
        event_tense=operator.production.tense if operator.production else "unspecified",
    )
    i += 1
    inner_terms, inner_negations, complement = [], [], []
    while i < len(words) and words[i] in (
        {"to", "be", "not", "never"} | REPORTED_MODIFIERS
    ):
        token, word = tokens[i], words[i]
        if word in {"to", "be"}:
            complement.append(token.span())
        elif word in {"not", "never"}:
            inner_negations.append(
                ScopeOperator(token.group(), *token.span(), "negation", "event")
            )
        else:
            inner_terms.append(modifier_term(text, *token.span()))
        i += 1
    event_span = tokens[i].span() if i < len(tokens) else (end, end)
    if not complement or text[slice(*complement[0])].casefold() != "to":
        # A rejected legacy modifier such as "has been observed exploited"
        # remains with its original frame; only an infinitive advertises this
        # new observation operand.
        return None
    verb = words[i] if i < len(words) else ""
    tail_start = tokens[i + 1].start() if i + 1 < len(tokens) else end
    qualifiers = bind_qualifiers(text[tail_start:end], complement=verb)
    context = next(
        (q.attack_context for q in qualifiers.spans if q.attack_context), None
    )
    event = bind_event(text, event_span, (tail_start, end), attack_context=context)
    # Ordinary use remains non-exploitation context, including inside an envelope.
    if event.kind == "context":
        return None
    positioned, event = _position_qualifiers(text, qualifiers.spans, tail_start, event)
    inner = assertion_scope(
        text,
        (*inner_terms, *qualifier_terms(text, qualifiers.spans, offset=tail_start)),
        inner_negations,
        event_tense="past",
    )
    observation = ObservationConstruction(
        text,
        auxiliary[0],
        predicate,
        None,
        event_span,
        (
            (outer_negations[0].start, outer_negations[0].end)
            if len(outer_negations) == 1
            else None
        ),
        modifiers=outer_terms,
        construction="observed_passive",
        finite_binding=operator,
        event_binding=event,
        complement_spans=tuple(complement),
        observation_scope=outer,
        event_scope=inner,
    )
    temporal = tuple(q.temporal for q in qualifiers.spans if q.temporal)
    supported = bool(
        observation.supported
        and voice == "vulnerability"
        and not modal
        and not negative
        and qualifiers.complete
        and temporal_compatible(temporal, "past")
        and all(
            t.owner == "reporter" or t.direction in {"past", "context"}
            for t in temporal
        )
        and not extract_cve_ids(text[tail_start:])
    )
    return PredicateFrame(
        text=text,
        end=len(text),
        operator_span=(0, predicate[0]),
        event_span=event_span,
        target=TargetBinding("", tail_start, tail_start),
        adjunct_span=(tail_start, end),
        qualifiers=positioned,
        verb=verb,
        kind="assertion",
        tense="past",
        aspect="perfect-observation",
        finite=True,
        modal=modal,
        polarity="negative" if inner_negations else "affirmative",
        supported=supported,
        starts_relation=True,
        inherits_subject=True,
        operators=operator.words,
        scope=inner,
        temporal=temporal,
        event_binding=event,
        observation=observation,
        operator_binding=operator,
    )


def bind_predicate(
    text: str,
    *,
    voice: str = "unscoped",
    modal: str = "",
    negative: bool = False,
    subject: SubjectBinding | None = None,
) -> PredicateFrame:
    """Return one complete frame or an explicit unsupported required frame.

    Coordination consumes this result too. It never has its own operator list
    or lexical scan. A recognized start is not a promise of a supported state.
    """
    if observation := _observation_frame(text, voice, modal, negative):
        return observation
    if observation := _passive_observation_frame(text, voice, modal, negative, subject):
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
        elif EPISTEMIC_MODIFIERS.get(word) == "epistemic":
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
    operator = bind_operator(
        text,
        spans=auxiliary_spans,
        subject=subject,
        voice=voice,
        event=verb,
        negations=[(o.start, o.end) for o in scope_operators if o.kind == "negation"],
    )
    rule = operator.production
    governing = rule
    if rule:
        tense, aspect = rule.tense, rule.aspect
        modal = modal or rule.modal
        supported &= rule.allows_negation or not negative
        supported &= operator.supported
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
    if requires_attack_context(verb):
        attack_context = next(
            (q.attack_context for q in qualifiers.spans if q.attack_context), None
        )
        event = bind_event(
            text,
            (event_start, event_end),
            (argument_start, end),
            attack_context=attack_context,
            unowned_infinitive=(
                voice == "unscoped"
                and tuple(auxiliaries) == ("to",)
                and not has_required_event(text)
            ),
        )
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
    if operator.words and operator.words[0] in DO_SUPPORT and tense == "past":
        supported &= all(
            t.owner == "reporter" or t.direction in {"past", "context"}
            for t in temporal[len(prefix_time) :]
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
    if event.descriptor and event.descriptor.singular_actor:
        supported &= bool(
            subject and subject.kind == "actor" and subject.number == "singular"
        )
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
    positioned_qualifiers, event = _position_qualifiers(
        text, qualifiers.spans, argument_start, event
    )
    return PredicateFrame(
        operator_binding=operator,
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
        qualifiers=tuple(positioned_qualifiers),
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

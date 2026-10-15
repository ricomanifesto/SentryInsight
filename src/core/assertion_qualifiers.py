"""Closed, completely consumed qualifier spans; no exploitation projection.

Conditions and independent clauses remain with condition_boundaries. A known
role or preposition cannot consume an unknown subordinate proposition.
"""

from dataclasses import dataclass
import re

from .assertion_bindings import (
    CVE_LIST,
    REPORTER_SUBJECT,
    bind_subject,
    PRODUCT_NOMINAL,
)
from .assertion_bindings import NAME as NAME
from .cve import extract_cve_ids
from .relations import (
    AttackCardinality,
    AttackContext,
    AssertionScope,
    ScopeOperator,
    ScopeTerm,
    TemporalConstraint,
    TemporalDirection,
)

# Classification of the already accepted modifier vocabulary. Recognition
# remains with each existing finite production, not this semantic mapping.
MODIFIER_KINDS = {
    "actively": "activity",
    "active": "activity",
    "widely": "degree",
    "extensively": "degree",
    "currently": "current_time",
    "now": "current_time",
    "still": "time",
    "newly": "time",
    "recently": "time",
    "yet": "time",
    "first": "order",
    "publicly": "disclosure",
    "successfully": "outcome",
    "also": "addition",
    "potentially": "epistemic",
    "likely": "epistemic",
    "possibly": "epistemic",
    "probably": "epistemic",
    "unlikely": "epistemic",
    "potential": "epistemic",
    "possible": "epistemic",
    "observed": "unclassified",
}


def modifier_term(text, start, end, *, owner="event"):
    value = text[start:end]
    return ScopeTerm(value, start, end, MODIFIER_KINDS[value.casefold()], owner)


def qualifier_terms(text, spans, *, offset=0, owner="event"):
    """Transfer complete owned qualifier spans without re-parsing their prose."""
    result = []
    for span in spans:
        if context := span.attack_context:
            result.append(
                ScopeTerm(
                    span.text, span.start + offset, span.end + offset, "domain", owner
                )
            )
            if quantity := context.cardinality:
                result.append(
                    ScopeTerm(
                        quantity.text,
                        quantity.start + offset,
                        quantity.end + offset,
                        "cardinality",
                        owner,
                    )
                )
            continue
        value = span.text.casefold()
        kind = MODIFIER_KINDS.get(value, span.kind)
        if span.temporal and span.temporal.direction == "current":
            kind = "current_time"
        if value in {"in the wild", "in attacks", "in prior reporting"}:
            kind = "domain"
        result.append(
            ScopeTerm(
                span.text,
                span.start + offset,
                span.end + offset,
                kind,
                "reporter" if span.kind == "reporter" else owner,
            )
        )
    return tuple(result)


def assertion_scope(text, terms=(), operators=(), *, event_tense="unspecified"):
    """Bind negation to the parsed proposition, preserving each local span."""
    scope = AssertionScope(text, tuple(terms), tuple(operators), event_tense)
    target = "qualified_event" if scope.restrictions else "event"
    return AssertionScope(
        text,
        scope.terms,
        tuple(
            (
                ScopeOperator(o.text, o.start, o.end, o.kind, target)
                if o.kind == "negation" and o.target in {"event", "qualified_event"}
                else o
            )
            for o in scope.operators
        ),
        event_tense,
    )


# The existing temporal owner, now shared by all assertion-tail consumers.
TIME_UNIT = r"(?:second|minute|hour|day|week|fortnight|month|quarter|year|weekend|night|morning|afternoon|evening)s?"
WEEKDAY = r"(?:monday|tuesday|wednesday|thursday|friday|saturday|sunday)(?: (?:morning|afternoon|evening|night))?"
QUANTITY = r"(?:\d+|one|two|three|four|five|six|seven|eight|nine|ten|several|many|multiple|numerous|a|an|(?:hundreds|thousands|millions|dozens) of)"
NOMINAL_TIME = (
    rf"(?:(?:the )?(?P<time_relation>last|next|previous|following|this|that|every|each|all) (?:{QUANTITY} )?(?:{TIME_UNIT}|{WEEKDAY})"
    rf"|{QUANTITY} {TIME_UNIT}|{WEEKDAY}"
    rf"|(?:(?:more|less|fewer) than |at (?:least|most) |up to )?{QUANTITY} (?:times|occasions))"
)
MONTH = r"(?:January|February|March|April|May|June|July|August|September|October|November|December)"
DATE = rf"(?:{MONTH}(?: \d{{1,2}})?|{NOMINAL_TIME}|(?P<relative_day>today|yesterday))"


@dataclass(frozen=True)
class QualifierSpan:
    kind: str
    text: str
    start: int
    end: int
    subject: str = ""
    predicate: str = ""
    object_text: str = ""
    cves: tuple[str, ...] = ()
    temporal: TemporalConstraint | None = None
    attack_context: AttackContext | None = None


@dataclass(frozen=True)
class QualifierBinding:
    text: str
    spans: tuple[QualifierSpan, ...]
    end: int

    @property
    def complete(self):
        return self.end == len(self.text)

    @property
    def residual(self):
        return self.text[self.end :]


def _production(pattern, *, flags=re.I):
    return re.compile("(?:" + pattern.replace(" ", r"\s+") + r")(?=$|[\s,.!?])", flags)


ATTACK_CONTEXT = _production(
    r"(?P<relation>in) (?:(?P<quantity>\S+) )?(?P<head>attacks?)"
)


# Each production binds a role and its entire finite or nominal argument.
# These are grammatical participant slots, never source/provider strings.
REPORTERS = (
    _production(
        rf"as (?P<subject>was|is|investigators|researchers|the vendor) "
        rf"(?P<predicate>confirmed|confirm|observed|observe|detected|detect)"
        rf"(?: (?P<object>{DATE}))?"
    ),
    _production(
        rf"(?P<subject>{REPORTER_SUBJECT}) (?P<predicate>said) on (?P<object>{DATE})",
        flags=0,
    ),
)
PRODUCTIONS = (
    *(("reporter", production) for production in REPORTERS),
    ("temporal", _production(rf"{NOMINAL_TIME}")),
    ("temporal", _production(rf"(?:in|on) {DATE}")),
    ("temporal", _production(rf"for (?:{QUANTITY} )?{TIME_UNIT}")),
    ("temporal", _production(r"over the weekend|at the time of publication")),
    (
        "temporal",
        _production(r"(?:after|before) (?P<object>public disclosure|a patch)"),
    ),
    (
        "temporal",
        _production(
            r"(?:after|before) (?P<subject>it|patches) (?P<predicate>(?:was|were) (?:publicly )?(?:disclosed|released))"
        ),
    ),
    (
        "temporal",
        _production(
            r"(?:after|before) (?P<subject>the vendor) (?P<predicate>had issued) (?P<object>an update)"
        ),
    ),
    (
        "causal",
        _production(r"because (?P<subject>a patch) (?P<predicate>was unavailable)"),
    ),
    (
        "temporal",
        _production(
            r"(?P<time_adverb>currently|now|still|recently|today|yesterday|tomorrow|tonight|earlier|later|again|already|often|sometimes|always|ever|soon|twice|ago|overnight)"
        ),
    ),
    (
        "context",
        _production(
            r"worldwide|abroad|overseas|here|there|actively|newly|widely|publicly|successfully|extensively"
        ),
    ),
    (
        "context",
        _production(
            r"in (?P<object>the wild|prior reporting)|across (?P<region>countries)"
        ),
    ),
    ("context", _production(rf"(?i:in) (?P<object>{NAME} Platform)", flags=0)),
    (
        "context",
        _production(rf"(?i:against) (?P<object>{NAME}'s own cloud service)", flags=0),
    ),
    ("role", _production(r"as (?P<object>a zero-day)")),
    ("identity", _production(rf"for (?P<object>{CVE_LIST}|the gateway)")),
    ("purpose", _production(r"to (?P<predicate>gain) (?P<object>privileges)")),
    (
        "purpose",
        _production(
            rf"to (?P<predicate>run) (?P<object>arbitrary code)"
            rf"(?: with (?P<privilege>root privileges))?"
            rf"(?: on (?P<target>{PRODUCT_NOMINAL}))?",
            flags=0,
        ),
    ),
    (
        "purpose",
        _production(
            rf"to (?P<predicate>install) (?P<object>custom malware) on (?P<target>vulnerable {NAME} appliances)",
            flags=0,
        ),
    ),
)


COMPLEMENTS = {"vulnerable": _production(r"to (?P<object>attack)")}


# Direction belongs to a captured temporal production, never a substring in
# arbitrary evidence. Calendar/frequency/duration contexts do not invent dates.
TIME_DIRECTIONS: dict[str, TemporalDirection] = {
    "last": "past",
    "previous": "past",
    "yesterday": "past",
    "earlier": "past",
    "ago": "past",
    "next": "future",
    "tomorrow": "future",
    "now": "current",
    "currently": "current",
    "today": "window",
    "this": "window",
    "recently": "window",
    "following": "relative",
    "later": "relative",
    "soon": "relative",
    "tonight": "relative",
    "that": "relative",
    "every": "context",
    "each": "context",
    "all": "context",
    "still": "context",
    "again": "context",
    "already": "context",
    "often": "context",
    "sometimes": "context",
    "always": "context",
    "ever": "context",
    "twice": "context",
    "overnight": "context",
}


def _temporal_constraint(kind, match):
    if kind not in {"temporal", "reporter"}:
        return None
    fields = match.groupdict()
    marker = next(
        (
            fields.get(key)
            for key in ("time_relation", "relative_day", "time_adverb")
            if fields.get(key)
        ),
        "",
    )
    direction = TIME_DIRECTIONS[marker.casefold()] if marker else "context"
    reporter_tense = "unspecified"
    if kind == "reporter":
        finite = fields.get("subject", "").casefold()
        predicate = fields.get("predicate", "").casefold()
        reporter_tense = (
            "past"
            if finite == "was"
            else (
                "current"
                if finite == "is"
                else (
                    "past"
                    if predicate in {"confirmed", "observed", "detected", "said"}
                    else "current"
                )
            )
        )
    return TemporalConstraint(
        "reporter" if kind == "reporter" else "event",
        direction,
        match.group(),
        reporter_tense,
    )


def bind_qualifiers(text: str, *, complement: str = "") -> QualifierBinding:
    """Consume exact closed spans; leave every unknown suffix for rejection."""
    spans = []
    cursor = 0
    while cursor < len(text):
        start = cursor
        while start < len(text) and text[start].isspace():
            start += 1
        if start == len(text) or re.fullmatch(r"[.!?]+", text[start:]):
            return QualifierBinding(text, tuple(spans), len(text))
        if spans and text[start] == ",":
            start += 1
            while start < len(text) and text[start].isspace():
                start += 1
        if match := ATTACK_CONTEXT.match(text, start):
            quantity = (
                AttackCardinality(
                    text=match["quantity"],
                    start=match.start("quantity"),
                    end=match.end("quantity"),
                    kind=(
                        "plurality"
                        if match["quantity"].casefold() in {"multiple", "several"}
                        else "exact_positive"
                    ),
                )
                if match["quantity"]
                else None
            )
            context = AttackContext(
                text,
                start,
                match.end(),
                match.span("relation"),
                match.span("head"),
                quantity,
            )
            if not context.supported:
                return QualifierBinding(text, tuple(spans), start)
            spans.append(
                QualifierSpan(
                    "context",
                    match.group(),
                    start,
                    match.end(),
                    object_text=match["head"],
                    attack_context=context,
                )
            )
            cursor = match.end()
            continue
        if text[start : start + 3].casefold() == "by ":
            actor = bind_subject(text[start + 3 :] + " ")
            if actor and actor.kind == "actor":
                end = start + 3 + len(actor.text)
                spans.append(
                    QualifierSpan("agent", text[start:end], start, end, actor.text)
                )
                cursor = end
                continue
        productions = (
            (("context", COMPLEMENTS[complement]),) if complement in COMPLEMENTS else ()
        ) + PRODUCTIONS
        for kind, production in productions:
            match = production.match(text, start)
            if match:
                fields = match.groupdict()
                spans.append(
                    QualifierSpan(
                        kind,
                        match.group(),
                        start,
                        match.end(),
                        fields.get("subject") or "",
                        fields.get("predicate") or "",
                        fields.get("object") or "",
                        tuple(extract_cve_ids(match.group())),
                        _temporal_constraint(kind, match),
                    )
                )
                cursor = match.end()
                break
        else:
            return QualifierBinding(text, tuple(spans), start)
    return QualifierBinding(text, tuple(spans), cursor)


def detach_reporting(text: str):
    """The same reporter production owns an exact terminal attribution."""
    for production in REPORTERS:
        for match in production.finditer(text):
            if match.start() and not text[match.start() - 1].isspace():
                continue
            binding = bind_qualifiers(text[match.start() :])
            if binding.complete and all(
                span.kind == "reporter" for span in binding.spans
            ):
                return text[: match.start()].rstrip(" ,"), binding.spans
    return text, ()

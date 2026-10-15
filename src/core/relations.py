"""Owned semantic relations shared by assertion and directive projections.

Recognition returns a relation or an explicit unsupported result. Qualifiers
belong to a parsed predicate; projections never search its source text again.
"""

from dataclasses import dataclass, replace
from typing import TYPE_CHECKING, Literal

from .assertion_bindings import SubjectBinding

if TYPE_CHECKING:
    from .recommendations import DirectiveFrame

# Columns are event current / past / unspecified, never reporter tense. A
# negative evidence operator applied to a qualified or negative event does not
# establish non-observation of exploitation.
_ASSERTION_PROJECTION = {
    (False, "affirmative", ""): ("active", "observed", None),
    (False, "negative", ""): ("not_observed",) * 3,
    (False, "affirmative", "possible"): ("potential",) * 3,
    (False, "negative", "possible"): ("unknown",) * 3,
    (True, "affirmative", ""): ("not_observed",) * 3,
    (True, "negative", ""): ("unknown",) * 3,
    (True, "affirmative", "possible"): ("unknown",) * 3,
    (True, "negative", "possible"): ("unknown",) * 3,
}
_EVENT_TENSES = ("current", "past", "unspecified")


@dataclass(frozen=True)
class ScopeTerm:
    """A positioned modifier belongs to one parsed proposition."""

    text: str
    start: int
    end: int
    kind: str
    owner: str = "event"


@dataclass(frozen=True)
class ScopeOperator:
    text: str
    start: int
    end: int
    kind: str
    target: str


@dataclass(frozen=True)
class AttackCardinality:
    text: str
    start: int
    end: int
    kind: Literal["plurality", "exact_positive"]

    @property
    def supported(self):
        if self.kind == "plurality":
            return self.text.casefold() in {"multiple", "several"}
        return bool(
            self.kind == "exact_positive"
            and self.text.isascii()
            and self.text.isdecimal()
            and not self.text.startswith("0")
        )


@dataclass(frozen=True)
class AttackContext:
    """One positioned attack relation, shared by qualifier and event binding."""

    text: str
    start: int
    end: int
    relation_span: tuple[int, int]
    head_span: tuple[int, int]
    cardinality: AttackCardinality | None = None

    @property
    def supported(self):
        relation = self.text[slice(*self.relation_span)].casefold()
        head = self.text[slice(*self.head_span)].casefold()
        if not (
            0 <= self.start < self.end <= len(self.text)
            and self.start == self.relation_span[0]
            and self.relation_span[1] < self.head_span[0]
            and self.head_span[1] == self.end
            and relation == "in"
        ):
            return False
        if quantity := self.cardinality:
            return bool(
                quantity.supported
                and self.relation_span[1] < quantity.start < quantity.end
                and quantity.end < self.head_span[0]
                and self.text[quantity.start : quantity.end] == quantity.text
                and head == ("attack" if quantity.text == "1" else "attacks")
            )
        return head == "attacks"


@dataclass(frozen=True)
class AssertionScope:
    """Local text keeps spans valid through wrappers and inherited relations."""

    text: str
    terms: tuple[ScopeTerm, ...] = ()
    operators: tuple[ScopeOperator, ...] = ()
    event_tense: str = "unspecified"

    @property
    def knowledge_negative(self):
        return any(
            o.kind == "negation" and o.target == "knowledge" for o in self.operators
        )

    @property
    def restrictions(self):
        negatives = [o.start for o in self.operators if o.kind == "negation"]
        return tuple(
            term
            for term in self.terms
            if term.owner != "reporter" and term.kind not in {"domain", "identity"}
            # "also not" adds a denied proposition; "not also" denies an
            # additional proposition. Their order is part of the binding.
            and not (
                term.kind == "addition" and negatives and term.end <= min(negatives)
            )
        )

    @property
    def supported(self):
        heads = [o for o in self.operators if o.kind == "knowledge"]
        if len(heads) > 1:
            return False
        if heads:
            head = heads[0]
            if head.text.casefold() != "known" or head.target != "event":
                return False
            for operator in self.operators:
                if operator.kind != "negation":
                    continue
                if operator.target == "knowledge":
                    if operator.end > head.start:
                        return False
                elif operator.target in {"event", "qualified_event"}:
                    if operator.start < head.end:
                        return False
                else:
                    return False
            for term in self.terms:
                if term.owner == "knowledge":
                    if term.end > head.start:
                        return False
                elif term.owner == "event":
                    if term.start < head.end:
                        return False
                elif term.owner != "reporter":
                    return False
        elif self.knowledge_negative or any(
            term.owner == "knowledge" for term in self.terms
        ):
            return False
        return (
            all(
                0 <= item.start < item.end <= len(self.text)
                and self.text[item.start : item.end] == item.text
                for item in (*self.terms, *self.operators)
            )
            and all(term.kind != "unclassified" for term in self.terms)
            and sum(term.kind == "reported" for term in self.terms) <= 1
            and sum(o.kind == "negation" for o in self.operators) <= 1
            and self.event_tense in _EVENT_TENSES
        )


@dataclass(frozen=True)
class AssertionProjection:
    status: str | None
    excludes: tuple[str, ...] = ()
    qualified_denial: bool = False


TemporalDirection = Literal[
    "past", "current", "window", "future", "context", "relative"
]


@dataclass(frozen=True)
class TemporalConstraint:
    """A parsed time relation belongs to its event or reporting predicate."""

    owner: Literal["event", "reporter"]
    direction: TemporalDirection
    text: str
    reporter_tense: str = "unspecified"


def temporal_compatible(constraints, event_tense, aspect="simple"):
    """Validate owned temporal meaning without guessing a new event state."""
    event_directions = set()
    for constraint in constraints:
        if constraint.owner not in {"event", "reporter"}:
            return False
        direction = constraint.direction
        if direction not in {"past", "current", "window", "context"}:
            # Future facts and unresolved relative anchors are outside this
            # finite contract, even under negative or qualified evidence.
            return False
        tense = (
            event_tense if constraint.owner == "event" else constraint.reporter_tense
        )
        if tense not in _EVENT_TENSES:
            return False
        if (direction, tense) in {("past", "current"), ("current", "past")} and not (
            constraint.owner == "event"
            and aspect in {"perfect", "perfect_progressive"}
            and (direction, tense) == ("past", "current")
        ):
            return False
        if constraint.owner == "event":
            event_directions.add(direction)
    return not {"past", "current"}.issubset(event_directions)


@dataclass(frozen=True)
class EvidenceReporter:
    """The reporting operator does not lend its tense to its embedded event."""

    subject: str
    finite: str
    polarity: Literal["affirmative", "negative"]
    qualification: str = ""
    as_of: str = ""


@dataclass(frozen=True)
class EvidenceOperation:
    """A nominal evidence predicate is not an exploitation-event predicate."""

    predicate: str
    auxiliary: str
    polarity: str
    text: str
    auxiliary_span: tuple[int, int]
    predicate_span: tuple[int, int]
    temporal: tuple[TemporalConstraint, ...] = ()
    absence: bool = False
    auxiliary_spans: tuple[tuple[int, int], ...] = ()

    @property
    def supported(self):
        return (
            self.predicate in {"confirmed", "observed", "detected"}
            and self.auxiliary in {"", "is", "was", "has been", "has not been"}
            and self.polarity in {"affirmative", "negative"}
            and self.polarity
            == ("negative" if self.auxiliary == "has not been" else "affirmative")
            and (
                " ".join(
                    self.text[start:end].lower() for start, end in self.auxiliary_spans
                )
                if self.auxiliary_spans
                else self.text[slice(*self.auxiliary_span)].lower()
            )
            == self.auxiliary
            and all(
                self.auxiliary_span[0] <= start < end <= self.auxiliary_span[1]
                for start, end in self.auxiliary_spans
            )
            and all(
                left[1] < right[0]
                for left, right in zip(self.auxiliary_spans, self.auxiliary_spans[1:])
            )
            and self.text[slice(*self.predicate_span)].lower() == self.predicate
            and temporal_compatible(self.temporal, self.tense)
        )

    @property
    def tense(self):
        return (
            "current"
            if self.auxiliary == "is"
            else (
                "past"
                if self.auxiliary in {"was", "has been", "has not been"}
                else "unspecified"
            )
        )


_NOMINAL_PROJECTION = {
    ("confirmed", "affirmative"): "observed",
    ("confirmed", "negative"): "unknown",
    ("observed", "affirmative"): "observed",
    ("observed", "negative"): "not_observed",
    ("detected", "affirmative"): "observed",
    ("detected", "negative"): "not_observed",
}


@dataclass(frozen=True)
class ObservationConstruction:
    """A perfect experiential observation owns its event nominal and polarity.

    Spans address the literal predicate text, independent of later source or
    coordination wrappers. Its reference point never establishes current activity.
    """

    text: str
    auxiliary_span: tuple[int, int]
    predicate_span: tuple[int, int]
    nominal_span: tuple[int, int]
    event_span: tuple[int, int]
    negative_span: tuple[int, int] | None = None
    activity_span: tuple[int, int] | None = None
    modifiers: tuple[ScopeTerm, ...] = ()

    @property
    def polarity(self):
        return "negative" if self.negative_span else "affirmative"

    @property
    def supported(self):
        spans = [self.auxiliary_span]
        if self.negative_span:
            spans.append(self.negative_span)
        spans.append(self.predicate_span)
        if self.activity_span:
            spans.append(self.activity_span)
        spans.append(self.event_span)
        if any(not 0 <= start < end <= len(self.text) for start, end in spans):
            return False
        spans.extend((term.start, term.end) for term in self.modifiers)
        spans.sort()
        return (
            spans[0][0] == 0
            and self.text[slice(*self.auxiliary_span)].casefold()
            in {"has", "have", "had"}
            and self.text[slice(*self.predicate_span)].casefold() == "seen"
            and self.text[slice(*self.event_span)].casefold() == "exploitation"
            and (
                not self.negative_span
                or self.text[slice(*self.negative_span)].casefold() in {"not", "never"}
                and self.auxiliary_span[1]
                < self.negative_span[0]
                < self.predicate_span[0]
            )
            and AssertionScope(self.text, self.modifiers).supported
            and all(
                term.kind == "reported"
                and term.owner == "evidence"
                and term.end < self.predicate_span[0]
                for term in self.modifiers
            )
            and (
                not self.activity_span
                or self.text[slice(*self.activity_span)].casefold() == "active"
            )
            and self.nominal_span
            == ((self.activity_span or self.event_span)[0], self.event_span[1])
            and all(
                left[1] < right[0] and self.text[left[1] : right[0]].isspace()
                for left, right in zip(spans, spans[1:])
            )
        )


@dataclass(frozen=True)
class ActorParticipation:
    """An admitted subject or event agent, positioned in its literal source."""

    binding: SubjectBinding
    role: Literal["subject", "agent"]
    coordinate_text: str
    nominal_span: tuple[int, int]

    def rebase(self, text: str, offset: int):
        start, end = (value + offset for value in self.nominal_span)
        if not (0 <= start < end <= len(text)) or text[start:end] != self.binding.text:
            raise ValueError("Actor origin must preserve its literal nominal")
        return replace(self, coordinate_text=text, nominal_span=(start, end))


@dataclass(frozen=True)
class AssertionOrigin:
    document_sha256: str
    block_index: int
    sentence_index: int
    clause_index: int


@dataclass(frozen=True)
class OwnedClause:
    text: str = ""
    source_text: str = ""
    cves: tuple[str, ...] = ()
    subject: str = ""
    attribution: str = "unscoped"
    relation: str = "root"
    kind: str = "context"
    context_role: str = ""
    verb: str = ""
    modal: str = ""
    polarity: Literal["affirmative", "negative"] = "affirmative"
    tense: str = "unspecified"
    aspect: str = "simple"
    conditions: tuple[str, ...] = ()
    reporting: tuple[str, ...] = ()
    reporter: EvidenceReporter | None = None
    evidence_operation: EvidenceOperation | None = None
    observation: ObservationConstruction | None = None
    scopes: tuple[AssertionScope, ...] = ()
    temporal: tuple[TemporalConstraint, ...] = ()
    finite: bool = False
    correlative: tuple[str, str] | None = None
    unsupported: bool = False
    object_text: str = ""
    object_role: str | None = None
    object_members: tuple[str, ...] = ()
    object_antecedent: int | None = None
    object_conditions: tuple[str, ...] = ()
    directive_modifiers: tuple[str, ...] = ()
    purposes: tuple[str, ...] = ()
    deadlines: tuple[str, ...] = ()
    reference: bool = False
    argument_relation: str = "direct"
    coordination: str = "initial"
    directive_frame: "DirectiveFrame | None" = None
    actor_participation: ActorParticipation | None = None
    assertion_origin: AssertionOrigin | None = None

    @property
    def knowledge_negative(self):
        return any(scope.knowledge_negative for scope in self.scopes)

    @property
    def reported_proposition(self):
        return any(
            term.kind == "reported" for scope in self.scopes for term in scope.terms
        )

    @property
    def _base_assertion_status(self) -> str | None:
        if self.kind != "assertion" or self.unsupported:
            return None
        # Qualification cannot rescue an unrecognized semantic state. Nominal
        # assertions remain valid without a verbal finite predicate.
        if (
            self.modal not in {"", "possible", "unknown"}
            or self.polarity not in {"affirmative", "negative"}
            or self.tense not in _EVENT_TENSES
            or self.aspect
            not in {
                "simple",
                "perfect",
                "perfect_progressive",
                "initiation",
                "continuative",
                "perfect-observation",
            }
            or not temporal_compatible(self.temporal, self.tense, self.aspect)
            or any(not scope.supported for scope in self.scopes)
            or (self.evidence_operation and not self.evidence_operation.supported)
            or (self.observation and not self.observation.supported)
            or (
                self.reporter
                and self.reporter.polarity not in {"affirmative", "negative"}
            )
        ):
            return None
        if (
            self.knowledge_negative
            or self.reported_proposition
            or self.modal == "unknown"
            or self.conditions
            or (self.reporter and self.reporter.qualification)
        ):
            return "unknown"
        negative_reporter = bool(self.reporter and self.reporter.polarity == "negative")
        if self.aspect in {"perfect", "perfect_progressive"}:
            # Finite present/past is the reference time, not proof that the
            # event is ongoing. Denying progressive activity does not deny
            # every occurrence of that event.
            if self.aspect == "perfect_progressive" and self.polarity == "negative":
                return "unknown"
            return _ASSERTION_PROJECTION[
                (negative_reporter, self.polarity, self.modal)
            ][1]
        if self.observation:
            return (
                "unknown"
                if negative_reporter
                or self.polarity == "negative"
                or self.observation.polarity == "negative"
                or self.modal
                else "observed"
            )
        if operation := self.evidence_operation:
            # Neither an outer denial nor two nested negatives establishes an
            # event. Confirmation absence is weaker than observation absence.
            if negative_reporter or (
                operation.absence and operation.polarity == "negative"
            ):
                return "unknown"
            polarity = "negative" if operation.absence else operation.polarity
            if self.polarity == "negative":
                return "unknown"
            if self.modal == "possible":
                return "potential" if polarity == "affirmative" else "unknown"
            status = _NOMINAL_PROJECTION[operation.predicate, polarity]
            if status == "observed" and self.tense == "current":
                return "active"
            return status
        return _ASSERTION_PROJECTION[negative_reporter, self.polarity, self.modal][
            _EVENT_TENSES.index(self.tense)
        ]

    @property
    def assertion_projection(self) -> AssertionProjection:
        status = self._base_assertion_status
        if status is None:
            return AssertionProjection(None)
        restrictions = tuple(t for s in self.scopes for t in s.restrictions)
        if self.knowledge_negative:
            return AssertionProjection("unknown", qualified_denial=bool(restrictions))
        operators = tuple(o for s in self.scopes for o in s.operators)
        absence = any(o.kind == "absence" for o in operators)
        direct_negative = any(
            o.kind == "negation" and o.target in {"event", "qualified_event"}
            for o in operators
        )
        negative_reporter = bool(self.reporter and self.reporter.polarity == "negative")
        negative_operation = bool(
            self.evidence_operation
            and (
                self.evidence_operation.absence
                or self.evidence_operation.polarity == "negative"
            )
        )
        if absence and direct_negative:
            return AssertionProjection("unknown", qualified_denial=bool(restrictions))
        if restrictions and (
            self.polarity == "negative"
            or negative_reporter
            or negative_operation
            or absence
        ):
            # Only an unqualified factual denial of CURRENT EVENT ACTIVITY
            # excludes active. A current word around a degree, outcome,
            # disclosure, frequency or other restriction cannot do so.
            excludes_current = (
                direct_negative
                and self.polarity == "negative"
                and self.tense == "current"
                and self.aspect not in {"perfect", "perfect_progressive"}
                and not (self.modal or self.conditions or absence)
                and not negative_reporter
                and not self.evidence_operation
                and not (self.reporter and self.reporter.qualification)
                and all(
                    scope.event_tense == "current"
                    for scope in self.scopes
                    if any(o.kind == "negation" for o in scope.operators)
                )
                and all(
                    t.owner == "event" and t.kind in {"activity", "current_time"}
                    for t in restrictions
                )
            )
            return AssertionProjection(
                "unknown",
                ("active",) if excludes_current else (),
                qualified_denial=True,
            )
        return AssertionProjection(status)

    @property
    def assertion_status(self) -> str | None:
        return self.assertion_projection.status

    @property
    def status(self) -> str:
        return self.assertion_status or "unknown"

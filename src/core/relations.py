"""Owned semantic relations shared by assertion and directive projections.

Recognition returns a relation or an explicit unsupported result. Qualifiers
belong to a parsed predicate; projections never search its source text again.
"""

from dataclasses import dataclass
from typing import Literal

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


def temporal_compatible(constraints, event_tense):
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
        if (direction, tense) in {("past", "current"), ("current", "past")}:
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

    @property
    def supported(self):
        return (
            self.predicate in {"confirmed", "observed", "detected"}
            and self.auxiliary in {"", "is", "was", "has been", "has not been"}
            and self.polarity in {"affirmative", "negative"}
            and self.polarity
            == ("negative" if self.auxiliary == "has not been" else "affirmative")
            and self.text[slice(*self.auxiliary_span)].lower() == self.auxiliary
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
    conditions: tuple[str, ...] = ()
    reporting: tuple[str, ...] = ()
    reporter: EvidenceReporter | None = None
    evidence_operation: EvidenceOperation | None = None
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

    @property
    def assertion_status(self) -> str | None:
        if self.kind != "assertion" or self.unsupported:
            return None
        # Qualification cannot rescue an unrecognized semantic state. Nominal
        # assertions remain valid without a verbal finite predicate.
        if (
            self.modal not in {"", "possible", "unknown"}
            or self.polarity not in {"affirmative", "negative"}
            or self.tense not in _EVENT_TENSES
            or not temporal_compatible(self.temporal, self.tense)
            or (self.evidence_operation and not self.evidence_operation.supported)
            or (
                self.reporter
                and self.reporter.polarity not in {"affirmative", "negative"}
            )
        ):
            return None
        if (
            self.modal == "unknown"
            or self.conditions
            or (self.reporter and self.reporter.qualification)
        ):
            return "unknown"
        negative_reporter = bool(self.reporter and self.reporter.polarity == "negative")
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
    def status(self) -> str:
        return self.assertion_status or "unknown"

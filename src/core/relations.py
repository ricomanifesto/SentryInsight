"""Owned semantic relations shared by assertion and directive projections.

Recognition returns a relation or an explicit unsupported result. Qualifiers
belong to a parsed predicate; projections never search its source text again.
"""

from dataclasses import dataclass
from typing import Literal


@dataclass(frozen=True)
class EvidenceReporter:
    """The reporting operator does not lend its tense to its embedded event."""

    subject: str
    finite: str
    polarity: Literal["affirmative", "negative"]
    qualification: str = ""
    as_of: str = ""


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
        if (
            self.modal == "unknown"
            or self.conditions
            or (self.reporter and self.reporter.qualification)
        ):
            return "unknown"
        if self.reporter and self.reporter.polarity == "negative":
            return "not_observed"
        if self.polarity == "negative":
            return "not_observed"
        if self.modal == "possible":
            return "potential"
        return {"past": "observed", "current": "active"}.get(self.tense)

    @property
    def status(self) -> str:
        return self.assertion_status or "unknown"

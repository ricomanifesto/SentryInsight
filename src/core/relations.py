"""Owned semantic relations shared by assertion and directive projections.

Recognition returns a relation or an explicit unsupported result. Qualifiers
belong to a parsed predicate; projections never search its source text again.
"""

from dataclasses import dataclass
from typing import Literal


@dataclass(frozen=True)
class OwnedClause:
    text: str = ""
    source_text: str = ""
    cves: tuple[str, ...] = ()
    subject: str = ""
    attribution: str = "unscoped"
    relation: str = "root"
    kind: str = "context"
    verb: str = ""
    modal: str = ""
    polarity: Literal["affirmative", "negative"] = "affirmative"
    tense: str = "unspecified"
    conditions: tuple[str, ...] = ()
    reporting: tuple[str, ...] = ()
    finite: bool = False
    correlative: tuple[str, str] | None = None
    unsupported: bool = False
    object_text: str = ""
    object_role: str | None = None
    object_members: tuple[str, ...] = ()
    reference: bool = False
    argument_relation: str = "direct"
    coordination: str = "initial"

    @property
    def assertion_status(self) -> str | None:
        if self.kind != "assertion" or self.unsupported:
            return None
        if self.modal == "unknown" or self.conditions:
            return "unknown"
        if self.polarity == "negative":
            return "not_observed"
        if self.modal == "possible":
            return "potential"
        return {"past": "observed", "current": "active"}.get(self.tense)

    @property
    def status(self) -> str:
        return self.assertion_status or "unknown"

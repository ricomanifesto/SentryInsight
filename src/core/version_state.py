"""Canonical affected-version evidence states, independent of source parsing."""

from enum import Enum
import re

ABSENT = "Not stated in supplied sources."
UNRESOLVED = "Unresolved from supplied sources."
STATE_FIELD = "Affected Versions Status"


class VersionEvidenceStatus(str, Enum):
    SUPPORTED = "supported"
    NOT_STATED = "not_stated"
    UNRESOLVED = "unresolved"


def resolved_report_schema(report: str) -> int:
    """Select after grounding; mixed or invalid states still fail artifact checks."""
    return 4 if re.search(r"^- \*\*Affected Versions Status\*\*:", report, re.M) else 3

"""The findings table: one segmentation of a report's finding section.

Reporting-key canonicalization, version-reference resolution, vendor-link and
finding-evidence validation, and key-to-link resolution read the same rows of
the same report text instead of each re-finding the section, the findings and
their fields. A row carries its 1-based index, absolute offsets, fields, CVE
scope, cited keys and digest, so every stage reports a rejected finding with
the same identity. Stages that rewrite findings return new text through
``render``; the next stage reads that text's table.

The grammars are unchanged and intentionally distinct: ``FIELD`` accepts any
whitespace around a field (as finding validation always has), while the
Reporting field is a single line. The published artifact parser keeps its own
closed field grammar.
"""

import hashlib
import re
from dataclasses import dataclass
from functools import cached_property, lru_cache
from typing import Iterable

from .cve import extract_cve_ids

ACTIVE_SECTION_PATTERN = re.compile(
    r"(?P<prefix>^##\s+Active Exploitation Details\s*$\n)"
    r"(?P<section>.*?)(?=^##\s+|\Z)",
    re.MULTILINE | re.DOTALL,
)
FINDING_PATTERN = re.compile(
    r"(?P<heading>^###\s+.+?\s*$\n)(?P<body>.*?)(?=^###\s+|\Z)",
    re.MULTILINE | re.DOTALL,
)
FIELD = re.compile(r"^-\s+\*\*([^*]+)\*\*:\s*(.*?)\s*$", re.MULTILINE)
REPORTING_FIELD_PATTERN = re.compile(
    r"^(?P<prefix>-[ \t]+\*\*Reporting\*\*:[ \t]*)(?P<value>.*?)[ \t]*$",
    re.MULTILINE,
)


@dataclass(frozen=True, eq=False)
class FindingRow:
    """A finding's heading line and body with absolute offsets in the report."""

    index: int
    heading: str
    body: str
    start: int
    body_start: int

    @property
    def end(self) -> int:
        return self.body_start + len(self.body)

    @property
    def text(self) -> str:
        return self.heading + self.body

    @property
    def title(self) -> str:
        return self.heading.removeprefix("###").strip()

    @cached_property
    def pairs(self) -> tuple[tuple[str, str], ...]:
        """Every field in body order, duplicates included."""
        return tuple(FIELD.findall(self.body))

    def fields(self) -> dict[str, str]:
        """A fresh name-to-value map; a repeated name keeps its last value."""
        return dict(self.pairs)

    @cached_property
    def cves(self) -> tuple[str, ...]:
        """CVEs of the CVE IDs field and the heading, in that order."""
        return tuple(
            extract_cve_ids(self.fields().get("CVE IDs", "") + " " + self.heading)
        )

    @cached_property
    def cited_keys(self) -> tuple[str, ...]:
        """The Reporting field split on commas, unvalidated."""
        return tuple(
            key.strip() for key in self.fields().get("Reporting", "").split(",")
        )

    @cached_property
    def reporting_fields(self) -> tuple[re.Match[str], ...]:
        """Single-line Reporting fields with body-relative offsets."""
        return tuple(REPORTING_FIELD_PATTERN.finditer(self.body))

    @cached_property
    def sha256(self) -> str:
        return hashlib.sha256(self.text.encode()).hexdigest()


@dataclass(frozen=True, eq=False)
class ReportFindings:
    """The finding section of one exact report text, or its absence."""

    report: str
    match_start: int
    section_start: int
    section_end: int
    rows: tuple[FindingRow, ...]

    @property
    def has_section(self) -> bool:
        return self.match_start >= 0

    def outside(self) -> str:
        """The report without its finding section heading and body."""
        return self.report[: self.match_start] + self.report[self.section_end :]

    def render(self, replacements: Iterable[tuple[int, int, str]]) -> str:
        """Apply ascending, non-overlapping absolute-offset replacements."""
        report = self.report
        for start, end, value in reversed(list(replacements)):
            report = report[:start] + value + report[end:]
        return report


@lru_cache(maxsize=32)
def report_findings(report: str) -> ReportFindings:
    """The findings table of exact report text, shared by every stage reading it."""
    section = ACTIVE_SECTION_PATTERN.search(report)
    if not section:
        return ReportFindings(report, -1, -1, -1, ())
    base = section.start("section")
    rows = tuple(
        FindingRow(
            index,
            finding["heading"],
            finding["body"],
            base + finding.start(),
            base + finding.start("body"),
        )
        for index, finding in enumerate(FINDING_PATTERN.finditer(section["section"]), 1)
    )
    return ReportFindings(report, section.start(), base, section.end("section"), rows)

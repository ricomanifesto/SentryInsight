"""Conservative recovery and ordering for fresh report severity fields."""

from collections import defaultdict
import re
from typing import Mapping

from .finding_evidence import source_evidence
from .report_findings import report_findings
from .reporting import ReportingSource

_NAMED = r"(?P<severity>critical|high|medium|low)"
_SUBJECT = r"(?:[-*][ \t]+)?(?P<cve>CVE-\d{4}-\d{4,})\b"
_DIRECT_SEVERITY = tuple(
    re.compile(pattern, re.IGNORECASE)
    for pattern in (
        rf"^{_SUBJECT}\s+(?:(?:is|was)\s+)?"
        rf"(?:rated\s+|classified\s+as\s+|has\s+(?:a\s+)?severity\s+of\s+)"
        rf"{_NAMED}\b",
        rf"^{_SUBJECT}(?:\s*,\s*|\s+(?:is|was)\s+)(?:a\s+)?"
        rf"{_NAMED}(?:[- ]severity)?\s+(?:security\s+)?"
        rf"(?:vulnerability|flaw|issue)\b",
        rf"^{_SUBJECT}\s*\(\s*{_NAMED}(?:\s+severity)?\s*\)",
    )
)
_UNCERTAIN = re.compile(
    r"\b(?:not|never|no|if|may|might|could|would|disputed|"
    r"unconfirmed|previously|initially|formerly|downgraded|upgraded)\b",
    re.IGNORECASE,
)
_NAMED_VALUE = re.compile(r"\b(?:critical|high|medium|low)\b", re.IGNORECASE)
_STARTS_WITH_CVE = re.compile(rf"^{_SUBJECT}", re.IGNORECASE)
_SEVERITY_FIELD = re.compile(
    r"^-[ \t]+\*\*Severity\*\*:[ \t]*(?P<value>[^\r\n]*?)[ \t]*$",
    re.MULTILINE,
)
_CRITICAL_CLAIM = re.compile(
    r"\bcritical(?:[- ]severity)?\s+(?:security\s+)?(?:vulnerabilit\w+|flaws?)\b",
    re.IGNORECASE,
)


def restore_source_severity(
    report: str, catalog: Mapping[str, ReportingSource]
) -> tuple[str, int]:
    """Fill Unknown only from an exact, unambiguous singleton CVE attribution.

    There must be one unanimous named value across eligible evidence and at
    least one cited source with that value. No title-based, score-only or
    adjacent-issue inference. Known labels and evidence-free Unknowns are not
    rewritten. The caller still runs all acceptance checks after this step.
    """
    table = report_findings(report)
    pending = []
    for row in table.rows:
        fields = list(_SEVERITY_FIELD.finditer(row.body))
        if (
            len(row.cves) == 1
            and len(fields) == 1
            and fields[0]["value"].casefold() == "unknown"
        ):
            pending.append((row, fields[0]))
    if not pending:
        return report, 0

    wanted = {row.cves[0] for row, _ in pending}
    evidence: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
    uncertain = set()
    for source in catalog.values():
        source_body = source_evidence(source.content)
        if not source_body.cve_set & wanted:
            continue
        for sentence, ids in source_body.sentences:
            if len(ids) != 1 or not ids <= wanted:
                continue
            labels = {label.lower() for label in _NAMED_VALUE.findall(sentence)}
            if not labels or not _STARTS_WITH_CVE.match(sentence):
                continue
            cve = next(iter(ids))
            if _UNCERTAIN.search(sentence):
                # An exact-scope negation or qualifier is not positive support
                # and must not be overridden by a different cited source.
                uncertain.add(cve)
                continue
            if any(pattern.match(sentence) for pattern in _DIRECT_SEVERITY):
                # Additional named values in an explicit rating statement are
                # ambiguity, not corroboration of its first value.
                for label in labels:
                    evidence[cve][label].add(source.key)
    edits = []
    for row, field in pending:
        values = evidence.get(row.cves[0], {})
        if len(values) == 1 and row.cves[0] not in uncertain:
            severity, keys = next(iter(values.items()))
            if keys.intersection(row.cited_keys):
                edits.append(
                    (
                        row.body_start + field.start("value"),
                        row.body_start + field.end("value"),
                        severity,
                    )
                )
    return table.render(edits), len(edits)


def critical_first(report: str) -> str:
    """Stably partition the already-validated finding blocks, preserving slugs."""
    table = report_findings(report)
    if len(table.rows) < 2:
        return report
    critical = [
        row
        for row in table.rows
        if row.fields().get("Severity", "").lower() == "critical"
    ]
    critical_set = set(critical)
    ordered = critical + [row for row in table.rows if row not in critical_set]
    if tuple(ordered) == table.rows:
        return report

    start, end = table.rows[0].start, table.rows[-1].end
    row_text = table.rows[-1].text
    trailing = row_text[len(row_text.rstrip("\r\n")) :]
    newline = "\r\n" if "\r\n" in table.rows[0].heading else "\n"
    body = (newline * 2).join(row.text.rstrip("\r\n") for row in ordered)
    return report[:start] + body + trailing + report[end:]


def has_critical_claim_without_known_severity(report: str) -> bool:
    """An advisory cue only, never evidence from which to assign a label."""
    rows = report_findings(report).rows
    return (
        bool(rows)
        and all(row.fields().get("Severity", "").lower() == "unknown" for row in rows)
        and _CRITICAL_CLAIM.search(report) is not None
    )

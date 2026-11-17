"""Lossless consolidation of repeated findings, never article-based grouping."""

import re
from typing import Mapping

from .finding_evidence import ABSENT, source_evidence
from .report_findings import FIELD, FindingRow, report_findings
from .reporting import ReportingSource

CHAIN = re.compile(r"\b(?:exploit(?:ation)? chain|chained together)\b", re.I)
CHAIN_BOUNDARY = re.compile(
    r"\b(?:not|never|no|cannot|can't|without|neither|unrelated|separate|independent)\b",
    re.I,
)
IDENTITY_FIELDS = {"CVE IDs", "Reporting", "Vendor Links"}
CVE = re.compile(
    r"\bCVE-\d{4}-\d{4,}\b(?:\s*(?:[,/&]|\band\b|\bor\b)\s*CVE-\d{4}-\d{4,}\b)*",
    re.I,
)


def _signature(row: FindingRow) -> tuple[str, str] | None:
    if not row.cves or len(row.pairs) != len(row.fields()):
        return None
    title = CVE.sub("", row.title)
    title = re.sub(r"[\s(),/]+", " ", title).strip()
    body = FIELD.sub(
        lambda match: "" if match[1] in IDENTITY_FIELDS else match[0], row.body
    ).strip()
    return title, body


def _same_issue(
    group: list[FindingRow],
    other: list[FindingRow],
    catalog: Mapping[str, ReportingSource],
) -> bool:
    row = other[0]
    if _signature(row) is None or _signature(group[0]) != _signature(row):
        return False
    existing = set.union(*(set(member.cves) for member in group))
    incoming = set.union(*(set(member.cves) for member in other))
    if incoming <= existing or existing <= incoming:
        return True
    cves = existing | incoming
    shared_keys = set.union(*(set(member.cited_keys) for member in group)) & set.union(
        *(set(member.cited_keys) for member in other)
    )
    # Co-mention, the same product and joint version attribution are insufficient.
    # Require one shared cited source to explicitly name this exact chain.
    return any(
        ids == cves and CHAIN.search(sentence) and not CHAIN_BOUNDARY.search(sentence)
        for key in shared_keys
        if key in catalog
        for sentence, ids in source_evidence(catalog[key].content).sentences
    )


def _merged(group: list[FindingRow]) -> str:
    cves = list(dict.fromkeys(cve for row in group for cve in row.cves))
    keys = list(dict.fromkeys(key for row in group for key in row.cited_keys))
    links = list(
        dict.fromkeys(
            link.strip()
            for row in group
            for link in row.fields().get("Vendor Links", ABSENT).split(";")
            if link.strip() and link.strip() != ABSENT
        )
    )
    values = {
        "CVE IDs": ", ".join(cves),
        "Reporting": ", ".join(keys),
        "Vendor Links": "; ".join(links) or ABSENT,
    }
    first = group[0]
    body = FIELD.sub(
        lambda match: (
            f"- **{match[1]}**: {values[match[1]]}\n"
            if match[1] in values
            else match[0]
        ),
        first.body,
    )
    return first.heading + body.rstrip() + "\n\n"


def group_related_findings(report: str, catalog: Mapping[str, ReportingSource]) -> str:
    """Preserve all prose/details; only union identities of exact repeated rows.

    Run after version-reference rendering and before final evidence validation.
    Different qualifiers, status, recommendations or narrative prevent merging.
    No-CVE findings have no shared vulnerability identity and remain separate.
    """
    table = report_findings(report)
    groups = [[row] for row in table.rows]
    # A later chain article can connect a previously separate follow-up. Reach
    # a fixed point so input order cannot leave that follow-up as a duplicate.
    changed = True
    while changed:
        changed = False
        for index, group in enumerate(groups):
            for other_index in range(index + 1, len(groups)):
                if _same_issue(group, groups[other_index], catalog):
                    group.extend(groups.pop(other_index))
                    group.sort(key=lambda row: row.start)
                    changed = True
                    break
            if changed:
                break
    replacements = []
    for group in groups:
        if len(group) > 1:
            replacements.append((group[0].start, group[0].end, _merged(group)))
            replacements.extend((row.start, row.end, "") for row in group[1:])
    return table.render(sorted(replacements))

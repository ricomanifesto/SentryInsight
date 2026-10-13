"""Exact field scoring independent of the production evidence recognizer.

These checks cover the fields named in the answer key, not arbitrary report prose.
An all-pass result is a candidate for semantic review, never a factual certificate.
"""

import re

from markdown_it import MarkdownIt

from src.core.reporting import reporting_key

from .dataset import SourceCase

FIELDS = {
    "exploitation_status": ("Exploitation Status", "status"),
    "affected_versions": ("Affected Versions", "affected_versions"),
    "exceptions": ("Exceptions", "exceptions"),
    "recommendations": ("Recommended Actions", "recommended_actions"),
    "vendor_links": ("Vendor Links", "vendor_links"),
}
CVE = re.compile(r"\bCVE-\d{4}-\d{4,}\b", re.IGNORECASE)


def normalize(value: str, *, terminal_period: bool = True) -> str:
    value = " ".join(value.split())
    return value.removesuffix(".") if terminal_period else value


def grade_report(case: SourceCase, report: str) -> dict[str, bool]:
    checks = dict.fromkeys(
        ["well_formed", "finding_coverage", "cve_ownership", "citations", *FIELDS],
        False,
    )
    sections = re.findall(
        r"^## Active Exploitation Details\s*\n(.*?)(?=^## |\Z)",
        report,
        re.MULTILINE | re.DOTALL,
    )
    if len(sections) != 1:
        return checks
    blocks = re.findall(
        r"^### (.*?)\n(.*?)(?=^### |\Z)",
        sections[0],
        re.MULTILINE | re.DOTALL,
    )
    findings = {}
    tokens = list(MarkdownIt("commonmark").parse(report))
    hidden_structure = False
    while tokens:
        token = tokens.pop()
        hidden_structure |= token.type in {
            "fence",
            "code_block",
            "html_block",
            "html_inline",
        }
        tokens.extend(token.children or [])
    well_formed = bool(blocks) and not hidden_structure
    for title, body in blocks:
        pairs = re.findall(r"^- \*\*([^*]+)\*\*:[ \t]*([^\n]*)", body, re.MULTILINE)
        fields = dict(pairs)
        previous_label = None
        for line in body.splitlines():
            match = re.match(r"^- \*\*([^*]+)\*\*:", line)
            if match:
                previous_label = match[1]
            elif line.strip() and previous_label in {
                label for label, _ in FIELDS.values()
            } | {"CVE IDs", "Reporting"}:
                # Required fields have a single-line contract. Never silently
                # discard a continuation that could reverse the first line.
                well_formed = False
        ids = CVE.findall(fields.get("CVE IDs", ""))
        required = {label for label, _ in FIELDS.values()} | {
            "CVE IDs",
            "Reporting",
            "Description",
            "Severity",
            "Action",
        }
        if (
            len(fields) != len(pairs)
            or not required <= fields.keys()
            or not fields.get("Description", "").strip()
            or fields.get("Severity")
            not in {"critical", "high", "medium", "low", "unknown"}
            or fields.get("Action")
            not in {"patch", "mitigate", "investigate", "monitor", "none"}
            or len(ids) != 1
            or ids[0] in findings
            or set(CVE.findall(title)) - set(ids)
            or fields.get("CVE IDs", "").strip() != ids[0]
        ):
            well_formed = False
            continue
        findings[ids[0]] = fields
    expected_ids = {finding.cve for finding in case.expected.findings}
    checks["well_formed"] = well_formed
    checks["finding_coverage"] = set(findings) == expected_ids
    checks["cve_ownership"] = set(CVE.findall(report)) == expected_ids
    if not well_formed or not checks["finding_coverage"]:
        return checks
    checks["citations"] = True
    for metric in FIELDS:
        checks[metric] = True
    for expected in case.expected.findings:
        actual = findings[expected.cve]
        for metric, (label, attr) in FIELDS.items():
            text_phrase = metric not in {"vendor_links", "exploitation_status"}
            checks[metric] &= normalize(
                actual[label], terminal_period=text_phrase
            ) == normalize(getattr(expected, attr), terminal_period=text_phrase)
        keys = [part.strip() for part in actual["Reporting"].split(",")]
        expected_keys = {
            reporting_key(case.articles[i].link) for i in expected.source_indices
        }
        checks["citations"] &= (
            len(keys) == len(set(keys)) and set(keys) == expected_keys
        )
    return checks

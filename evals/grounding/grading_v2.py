"""Versioned field grading; narrative correctness always needs separate review."""

import re
from typing import Literal

from .dataset import Record, SourceCase
from .grading import CVE, FIELDS, GRADER_METRICS, grade_report

GRADER_VERSION = "grounding-fields-v2"
DEPENDENT_FIELDS = {"citations", *FIELDS}


class Check(Record):
    state: Literal["pass", "fail", "not_evaluated"]
    reason: str


class ReportGrade(Record):
    checks: dict[str, Check]
    narrative_review: Check
    additional_narrative_cves: list[str]

    @property
    def field_pass(self) -> bool:
        return all(check.state == "pass" for check in self.checks.values())


def grade_report_v2(case: SourceCase, report: str) -> ReportGrade:
    # V1 stays byte-for-byte reproducible. V2 reuses its structure and exact-value
    # checks, with one deliberately narrow display-label normalization.
    normalized = re.sub(
        r"(?m)^(- \*\*Affected Versions\*\*:[ \t]*)Affected versions:[ \t]*",
        r"\1",
        report,
        flags=re.IGNORECASE,
    )
    raw = grade_report(case, normalized)
    checks = {
        key: Check(
            state="pass" if value else "fail",
            reason=(
                "Matches the field contract."
                if value
                else "Does not match the field contract; review value and field role."
            ),
        )
        for key, value in raw.items()
    }
    owned_cves: set[str] = set()
    if not raw["well_formed"]:
        for key in GRADER_METRICS:
            if key != "well_formed":
                checks[key] = Check(
                    state="not_evaluated", reason="Required finding structure failed."
                )
    else:
        section = re.findall(
            r"^## Active Exploitation Details\s*\n(.*?)(?=^## |\Z)",
            normalized,
            re.MULTILINE | re.DOTALL,
        )[0]
        ownership_ok = True
        for title, body in re.findall(
            r"^### (.*?)\n(.*?)(?=^### |\Z)", section, re.MULTILINE | re.DOTALL
        ):
            fields = dict(
                re.findall(r"^- \*\*([^*]+)\*\*:[ \t]*([^\n]*)", body, re.MULTILINE)
            )
            # Titles and structured fields must stay with their own finding.
            # Executive-summary/other prose is handled by narrative review.
            cves = set(CVE.findall("\n".join([title, *fields.values()])))
            owned_cves.update(cves)
            ownership_ok &= cves == {fields["CVE IDs"].strip()}
        checks["cve_ownership"] = Check(
            state="pass" if ownership_ok else "fail",
            reason="CVE identity is checked within each finding's title and fields.",
        )
        if not raw["finding_coverage"]:
            for key in DEPENDENT_FIELDS:
                checks[key] = Check(
                    state="not_evaluated", reason="Expected finding coverage failed."
                )
    return ReportGrade(
        checks=checks,
        narrative_review=Check(
            state="not_evaluated",
            reason="Review all narrative claims against sources; field pass is not factual certification.",
        ),
        additional_narrative_cves=sorted(
            set(CVE.findall(report))
            - owned_cves
            - {finding.cve for finding in case.expected.findings}
        ),
    )

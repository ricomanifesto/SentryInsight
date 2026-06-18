"""Validation rules for generated exploitation reports."""

from dataclasses import dataclass
from typing import Iterable, List

REQUIRED_SECTIONS = (
    "# Exploitation Report",
    "## Active Exploitation Details",
    "## Affected Systems and Products",
    "## Attack Vectors and Techniques",
    "## Threat Actor Activities",
)

ERROR_MARKERS = (
    "# Error",
    "Error code:",
    "Error Generating Exploitation Report",
    "Invalid Model",
    "credit balance is too low",
    "authentication_error",
    "not_found_error",
    "rate_limit_error",
    "overloaded_error",
)


@dataclass(frozen=True)
class ReportValidationIssue:
    code: str
    message: str


def validate_report_content(markdown: str) -> List[ReportValidationIssue]:
    """Return validation issues that should block publishing."""
    issues: List[ReportValidationIssue] = []
    content = markdown.strip()

    if not content:
        return [
            ReportValidationIssue(
                code="empty_report",
                message="Report is empty.",
            )
        ]

    normalized_content = content.casefold()
    for marker in ERROR_MARKERS:
        if marker.casefold() in normalized_content:
            issues.append(
                ReportValidationIssue(
                    code="error_marker",
                    message=f"Report contains blocked error marker: {marker}",
                )
            )

    for section in REQUIRED_SECTIONS:
        if section not in content:
            issues.append(
                ReportValidationIssue(
                    code="missing_section",
                    message=f"Report is missing required section: {section}",
                )
            )

    return issues


def format_report_validation_issues(
    issues: Iterable[ReportValidationIssue],
) -> str:
    """Format validation issues for logs and CLI output."""
    return "\n".join(f"- {issue.code}: {issue.message}" for issue in issues)

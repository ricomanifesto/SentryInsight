"""A rejected report keeps a bounded reason a repair can act on.

The reason names the failed check, field and finding, plus categorical
expected/observed values. It never carries text, CVEs, URLs or hashes.
"""

import json

import pytest

from src.core.finding_evidence import EvidenceError
from src.core.validation_diagnostics import sanitize_diagnostic, validation_diagnostic

PRIVATE = "PRIVATE-MARKER https://private.example/secret"


def evidence(code, field, expected, observed, index=2):
    error = EvidenceError(
        PRIVATE, code=code, field=field, expected=expected, observed=observed
    )
    error.finding_index = index
    error.cves = (PRIVATE,)
    error.finding_sha256 = PRIVATE
    return error


def test_grounding_rejection_keeps_categorical_expected_and_observed():
    diagnostic = validation_diagnostic(
        "finding_evidence",
        evidence(
            "unsupported_exploitation_status",
            "Exploitation Status",
            "unknown",
            "observed",
        ),
    )
    assert diagnostic["codes"] == ["unsupported_exploitation_status"]
    assert diagnostic["field"] == "Exploitation Status"
    assert diagnostic["finding_index"] == 2
    assert diagnostic["expected"] == "unknown"
    assert diagnostic["observed"] == "observed"
    assert PRIVATE not in json.dumps(diagnostic)


@pytest.mark.parametrize(
    ("expected", "observed", "safe"),
    [
        (True, False, (True, False)),
        (3, 1_000_001, (3, "invalid")),
        (PRIVATE, "not_observed", ("invalid", "not_observed")),
        (None, None, (None, None)),
    ],
)
def test_expected_and_observed_are_bounded(expected, observed, safe):
    diagnostic = validation_diagnostic(
        "finding_evidence",
        evidence(
            "affected_version_not_grounded", "Affected Versions", expected, observed
        ),
    )
    assert (diagnostic["expected"], diagnostic["observed"]) == safe
    assert PRIVATE not in json.dumps(diagnostic)


def test_unknown_codes_never_carry_values():
    diagnostic = validation_diagnostic(
        "finding_evidence", evidence("looks_like_a_secret", PRIVATE, "unknown", True)
    )
    assert diagnostic["expected"] is None and diagnostic["observed"] is None


def test_sanitizer_reapplies_the_same_bounds_to_untrusted_input():
    hostile = {
        "stage": "finding_evidence",
        "codes": ["affected_version_not_grounded", PRIVATE],
        "field": "Affected Versions",
        "finding_index": 1,
        "expected": PRIVATE,
        "observed": {"nested": PRIVATE},
        "extra": PRIVATE,
    }
    clean = sanitize_diagnostic(hostile)
    assert set(clean) == {
        "schema_version",
        "stage",
        "codes",
        "field",
        "finding_index",
        "issues_truncated",
        "expected",
        "observed",
    }
    assert clean["expected"] == "invalid" and clean["observed"] == "invalid"
    assert PRIVATE not in json.dumps(clean)


@pytest.mark.parametrize(
    ("markdown", "reason"),
    [
        ("- **Unclosed label", "invalid_bold_label"),
        ("- ** **:", "invalid_bold_label"),
        ("- **FishMonger**", "missing_bold_label_description"),
        ("- **FishMonger**: &mdash;", "missing_bold_label_description"),
    ],
)
def test_markdown_rejection_keeps_reason_line_and_bounded_excerpt(markdown, reason):
    from src.core.report_validation import validate_report_content
    from src.core.reviewed_report import ReviewedReportValidationError

    report = "\n\n" + markdown
    error = ReviewedReportValidationError(validate_report_content(report))
    diagnostic = validation_diagnostic("report_content", error)
    assert diagnostic["markdown_reason"] == reason
    assert diagnostic["markdown_line"] == 3
    assert diagnostic["markdown_excerpt"] == markdown
    assert sanitize_diagnostic(diagnostic) == diagnostic


def test_markdown_excerpt_is_capped_and_single_line_in_diagnostics():
    from src.core.report_validation import (
        ReportValidationIssue,
        validate_report_content,
    )
    from src.core.reviewed_report import ReviewedReportValidationError

    long_line = "- **" + ("X" * 260) + "**:"
    error = ReviewedReportValidationError(validate_report_content(long_line))
    diagnostic = validation_diagnostic("report_content", error)
    assert diagnostic["markdown_line"] == 1
    assert len(diagnostic["markdown_excerpt"]) == 200
    assert diagnostic["markdown_excerpt"].endswith("...")
    assert sanitize_diagnostic(diagnostic) == diagnostic

    multiline = ReviewedReportValidationError(
        [
            ReportValidationIssue(
                "malformed_markdown",
                PRIVATE,
                "missing_bold_label_description",
                markdown_line=7,
                markdown_excerpt="- **Label**:\t\nAuthorization: Bearer secret",
            )
        ]
    )
    clean = validation_diagnostic("report_content", multiline)
    assert clean["markdown_line"] == 7
    assert clean["markdown_excerpt"] == "- **Label**:"
    assert "Authorization" not in json.dumps(clean)
    assert PRIVATE not in json.dumps(clean)


@pytest.mark.parametrize("reason", [PRIVATE, {"text": PRIVATE}, 1, None])
def test_untrusted_markdown_reason_is_omitted(reason):
    from src.core.report_validation import ReportValidationIssue
    from src.core.reviewed_report import ReviewedReportValidationError

    error = ReviewedReportValidationError(
        [ReportValidationIssue("malformed_markdown", PRIVATE, reason)]
    )
    assert "markdown_reason" not in validation_diagnostic("report_content", error)
    assert "markdown_reason" not in sanitize_diagnostic(
        {"codes": ["malformed_markdown"], "markdown_reason": reason}
    )


@pytest.mark.parametrize("bad_line", [True, False, 0, -1, 1_000_001, "3", 3.5, None])
@pytest.mark.parametrize("bad_excerpt", [None, 123, {"a": 1}, "", "   ", "\nsecond"])
def test_untrusted_markdown_line_and_excerpt_are_omitted(bad_line, bad_excerpt):
    clean = sanitize_diagnostic(
        {
            "codes": ["malformed_markdown"],
            "markdown_reason": "missing_bold_label_description",
            "markdown_line": bad_line,
            "markdown_excerpt": bad_excerpt,
        }
    )
    assert "markdown_line" not in clean
    assert "markdown_excerpt" not in clean


def test_markdown_fields_require_matching_content_code():
    clean = sanitize_diagnostic(
        {
            "codes": ["active_content"],
            "markdown_reason": "invalid_bold_label",
            "markdown_line": 4,
            "markdown_excerpt": "- **Label**:",
        }
    )
    assert "markdown_reason" not in clean
    assert "markdown_line" not in clean
    assert "markdown_excerpt" not in clean


def test_artifact_rejection_retains_allowlisted_reason_field_and_index_only():
    from src.core.report_artifact import ReportArtifactError

    error = ReportArtifactError(
        PRIVATE,
        reason="invalid_triage_value",
        field="Severity",
        finding_index=2,
    )
    diagnostic = validation_diagnostic("report_artifact", error)
    assert diagnostic["codes"] == ["artifact_rejected"]
    assert diagnostic["artifact_reason"] == "invalid_triage_value"
    assert diagnostic["field"] == "Severity"
    assert diagnostic["finding_index"] == 2
    assert sanitize_diagnostic(diagnostic) == diagnostic
    assert PRIVATE not in json.dumps(diagnostic)


@pytest.mark.parametrize("bad_reason", [PRIVATE, {"text": PRIVATE}, 1, None])
def test_untrusted_artifact_reason_is_omitted(bad_reason):
    from src.core.report_artifact import ReportArtifactError

    error = ReportArtifactError(PRIVATE, reason=bad_reason)
    diagnostic = validation_diagnostic("report_artifact", error)
    assert "artifact_reason" not in diagnostic
    assert "artifact_reason" not in sanitize_diagnostic(
        {"codes": ["artifact_rejected"], "artifact_reason": bad_reason}
    )
    assert "artifact_reason" not in sanitize_diagnostic(
        {"codes": ["active_content"], "artifact_reason": "invalid_triage_value"}
    )

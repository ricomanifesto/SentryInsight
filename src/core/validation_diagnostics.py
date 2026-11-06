"""Bounded categories shared by production and unpublished verification; never serialize exceptions."""

from src.core.finding_evidence import EvidenceError
from src.core.report_artifact import ReportArtifactError
from src.core.report_validation import ReportValidationIssue
from src.core.reporting import ReportingGroundingError
from src.core.reviewed_report import (
    ReportingSelectionError,
    ReviewedReportValidationError,
)
from src.core.source_review import SourceReviewError

STAGES = frozenset(
    {
        "candidate_structure",
        "source_review",
        "reporting_identity",
        "version_references",
        "finding_evidence",
        "report_content",
        "source_coverage",
        "report_artifact",
    }
)
FIELDS = frozenset(
    {
        "Affected Versions",
        "Affected Versions Status",
        "Exceptions",
        "Recommended Actions",
        "Vendor Links",
        "Exploitation Status",
        "Reporting",
        "Action",
        "prose",
        "summary",
    }
)
# Explicit allowlists are the disclosure boundary. New validator codes require
# review here; neither code-shaped strings nor exception messages are trusted.
SOURCE_CODES = frozenset("""
    conflicting_source_metadata invalid_review_input_catalog invalid_review_packet
    invalid_review_scope invalid_source_identity invalid_source_metadata
    missing_review_scope missing_source_content review_cohort_incomplete
    review_input_limit_exceeded review_packet_conflict review_packet_path_invalid
    review_packet_permissions_invalid review_packet_persistence_failed
    review_selection_changed_evidence unknown_review_reason invalid_source_coverage
    model_supplied_coverage invalid_review_candidate out_of_scope_candidate_cve
    quarantined_or_unknown_reporting_source review_candidate_missing_findings
    source_review_plan_mismatch source_review_plan_missing source_review_required
    source_review_fingerprint_mismatch
    invalid_reporting_field_count invalid_reporting_source_syntax
    unknown_reporting_source quarantined_reporting_source duplicate_reporting_source
    """.split())
EVIDENCE_CODES = frozenset("""
    finding_evidence_rejected duplicate_version_reference
    invalid_version_evidence_state invalid_version_reference
    invalid_version_reference_field invalid_version_reference_protocol
    invalid_version_reference_source misplaced_version_reference
    missing_finding_section missing_version_references unresolved_version_evidence
    unsupported_version_absence unsupported_version_reference
    version_reference_collision wrapped_version_reference
    action_without_recommendation affected_version_not_grounded
    ambiguous_affected_version_audience ambiguous_affected_version_audience_predicate
    ambiguous_affected_version_clause ambiguous_affected_version_continuation
    ambiguous_affected_version_grouping ambiguous_affected_version_polarity
    ambiguous_affected_version_range_continuation ambiguous_recommendation_scope
    ambiguous_version_cve_attribution detail_not_grounded duplicate_finding_field
    exception_not_grounded invalid_vendor_link missing_affected_version_entries
    missing_conflicting_exploitation_evidence missing_detail_field
    missing_negative_exploitation_evidence missing_retained_source_content
    missing_retained_source_evidence missing_source_details missing_source_exclusions
    missing_source_recommendation non_affected_version_clause
    recommendation_not_grounded unsupported_affected_version_entry
    unsupported_exploitation_status unsupported_finding_exploitation_claim
    unsupported_summary_exploitation_claim unsupported_vendor_link
    """.split())
CONTENT_CODES = frozenset("""
    active_content duplicate_section empty_report error_marker
    executive_summary_readability malformed_markdown missing_expected_cves
    missing_section noncanonical_section_heading removed_source_attribution
    underpopulated_threat_actor_activities virtual_event_promotion
    """.split())
MAX_ISSUES = 8
MAX_FINDING_INDEX = 1_000_000
UNKNOWN_CODE = "unclassified_validation_failure"


def _known(value: object, allowed: frozenset[str], fallback: str) -> str:
    return value if type(value) is str and value in allowed else fallback


EVIDENCE_STATES = frozenset(
    {"active", "observed", "potential", "not_observed", "unknown", "missing"}
)


def _bounded_value(value: object) -> str | int | bool | None:
    """Only categorical states, booleans and bounded counts; never text."""
    if value is None or type(value) is bool:
        return value
    if type(value) is int:
        return value if 0 <= value <= MAX_FINDING_INDEX else "invalid"
    return value if type(value) is str and value in EVIDENCE_STATES else "invalid"


def validation_diagnostic(stage: str, error: Exception) -> dict:
    """Return only fixed labels, bounded integers and a truncation flag.

    Messages, repr/str, traceback, titles, URLs, CVEs, hashes and source/candidate
    text are never read by this formatter. Categories for legacy
    errors without a structured code are less specific than coded rejections.
    """
    codes = [UNKNOWN_CODE]
    field = None
    finding_index = None
    truncated = False
    expected = observed = None
    if isinstance(error, EvidenceError):
        codes = [_known(error.code, EVIDENCE_CODES, UNKNOWN_CODE)]
        field = _known(error.field, FIELDS, "") or None
        index = error.finding_index
        if type(index) is int and 0 <= index <= MAX_FINDING_INDEX:
            finding_index = index
        # A targeted repair needs the categorical mismatch, not any text.
        if codes != [UNKNOWN_CODE]:
            expected = _bounded_value(error.expected)
            observed = _bounded_value(error.observed)
    elif isinstance(error, SourceReviewError):
        codes = [_known(error.code, SOURCE_CODES, UNKNOWN_CODE)]
        if isinstance(error, ReportingSelectionError):
            field = "Reporting"
            index = error.finding_index
            if type(index) is int and 0 <= index <= MAX_FINDING_INDEX:
                finding_index = index
    elif isinstance(error, ReviewedReportValidationError):
        issues = error.issues
        if type(issues) is list and issues:
            truncated = len(issues) > MAX_ISSUES
            codes = list(
                dict.fromkeys(
                    (
                        _known(issue.code, CONTENT_CODES, UNKNOWN_CODE)
                        if type(issue) is ReportValidationIssue
                        else UNKNOWN_CODE
                    )
                    for issue in issues[:MAX_ISSUES]
                )
            )
    elif isinstance(error, ReportingGroundingError):
        codes = ["reporting_identity_rejected"]
    elif isinstance(error, ReportArtifactError):
        codes = ["artifact_rejected"]
    return {
        "schema_version": 1,
        "stage": _known(stage, STAGES, "unknown_validation_stage"),
        "codes": codes,
        "field": field,
        "finding_index": finding_index,
        "issues_truncated": truncated,
        "expected": expected,
        "observed": observed,
    }


WORKFLOW_STAGES = STAGES | {
    "fetch",
    "analysis",
    "report_policy",
    "report_validation",
    "report_output",
    "site_publication",
}
WORKFLOW_CODES = (
    SOURCE_CODES
    | EVIDENCE_CODES
    | CONTENT_CODES
    | {
        "reporting_identity_rejected",
        "artifact_rejected",
        UNKNOWN_CODE,
        "feed_url_missing",
        "feed_fetch_failed",
        "analysis_failed",
        "model_provider_unavailable",
        "model_rate_limited",
        "model_auth_rejected",
        "model_request_failed",
        "model_output_limit_exceeded",
        "input_budget_exceeded",
        "analysis_exception",
        "request_budget_unresolved",
        "model_identity_mismatch",
        "source_review_failed",
        "report_artifact_invalid",
        "report_output_name_invalid",
        "review_packet_write_failed",
        "source_review_fingerprint_mismatch",
        "site_build_failed",
        "publication_failed",
        "publication_recovery_required",
        "publication_rolled_back",
        "invalid_publication_stage",
        "filesystem_error",
        "archive_conflict",
    }
)


def sanitize_diagnostic(value: object) -> dict:
    value = value if type(value) is dict else {}
    raw_codes = value.get("codes")
    codes = raw_codes if type(raw_codes) is list else []
    index = value.get("finding_index")
    return {
        "schema_version": 1,
        "stage": _known(
            value.get("stage"), WORKFLOW_STAGES, "unknown_validation_stage"
        ),
        "codes": list(
            dict.fromkeys(
                _known(code, WORKFLOW_CODES, UNKNOWN_CODE)
                for code in codes[:MAX_ISSUES]
            )
        )
        or [UNKNOWN_CODE],
        "field": _known(value.get("field"), FIELDS, "") or None,
        "finding_index": (
            index if type(index) is int and 0 <= index <= MAX_FINDING_INDEX else None
        ),
        "issues_truncated": len(codes) > MAX_ISSUES
        or value.get("issues_truncated") is True,
        "expected": _bounded_value(value.get("expected")),
        "observed": _bounded_value(value.get("observed")),
    }

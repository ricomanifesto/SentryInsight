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
        "Severity",
        "Exploitation Status",
        "Reporting",
        "CVE IDs",
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
    review_packet_size_limit_exceeded
    review_selection_changed_evidence unknown_review_reason invalid_source_coverage
    model_supplied_coverage invalid_review_candidate out_of_scope_candidate_cve
    quarantined_or_unknown_reporting_source review_candidate_missing_findings
    source_review_plan_mismatch source_review_plan_missing source_review_required
    source_review_fingerprint_mismatch
    invalid_reporting_field_count invalid_reporting_source_syntax
    unknown_reporting_source quarantined_reporting_source duplicate_reporting_source
    """.split())
EVIDENCE_CODES = frozenset("""
    finding_evidence_rejected finding_cve_identity_mismatch duplicate_version_reference
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
    missing_descriptive_finding_title
    """.split())
MARKDOWN_REASONS = frozenset({"invalid_bold_label", "missing_bold_label_description"})
ARTIFACT_REASONS = frozenset(
    {
        "empty_finding_slug",
        "invalid_front_matter",
        "missing_metadata",
        "invalid_metadata",
        "invalid_source_coverage",
        "missing_active_exploitation_section",
        "missing_findings",
        "duplicate_finding_field",
        "missing_required_field",
        "invalid_triage_value",
        "invalid_cve_ids",
        "invalid_reporting_field",
        "invalid_vendor_link",
        "invalid_version_status",
        "duplicate_finding_slug",
        "source_coverage_mismatch",
        "partial_cve_identifier",
    }
)
MAX_MARKDOWN_LINE = 1_000_000
MAX_MARKDOWN_EXCERPT_CHARS = 200
MAX_ISSUES = 8
MAX_FINDING_INDEX = 1_000_000
UNKNOWN_CODE = "unclassified_validation_failure"


def _known(value: object, allowed: frozenset[str], fallback: str) -> str:
    return value if type(value) is str and value in allowed else fallback


def _bounded_positive_int(value: object, maximum: int) -> int | None:
    return value if type(value) is int and 1 <= value <= maximum else None


def _bounded_markdown_excerpt(value: object) -> str | None:
    """Keep a single-line public-report excerpt capped at MAX_MARKDOWN_EXCERPT_CHARS."""
    if type(value) is not str:
        return None
    first_line = value.splitlines()[0] if value.splitlines() else ""
    cleaned = "".join(
        " " if ord(character) < 32 or ord(character) == 127 else character
        for character in first_line
    ).rstrip()
    if not cleaned:
        return None
    if len(cleaned) > MAX_MARKDOWN_EXCERPT_CHARS:
        return cleaned[: MAX_MARKDOWN_EXCERPT_CHARS - 3].rstrip() + "..."
    return cleaned


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
    """Return fixed labels, bounded integers and a truncation flag.

    Messages, repr/str, traceback, headers, credentials and source bodies are
    never read by this formatter. Only ``malformed_markdown`` issues may include
    the offending 1-based line number and a bounded single-line excerpt of that
    public-report line so generation diagnostics identify what tripped the rule.
    """
    codes = [UNKNOWN_CODE]
    field = None
    finding_index = None
    truncated = False
    expected = observed = None
    markdown_reason = None
    markdown_line = None
    markdown_excerpt = None
    artifact_reason = None
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
            for issue in issues[:MAX_ISSUES]:
                if (
                    type(issue) is ReportValidationIssue
                    and issue.code == "malformed_markdown"
                ):
                    markdown_reason = (
                        _known(issue.markdown_reason, MARKDOWN_REASONS, "") or None
                    )
                    markdown_line = _bounded_positive_int(
                        issue.markdown_line, MAX_MARKDOWN_LINE
                    )
                    markdown_excerpt = _bounded_markdown_excerpt(issue.markdown_excerpt)
                    if (
                        markdown_reason
                        or markdown_line is not None
                        or markdown_excerpt is not None
                    ):
                        break
    elif isinstance(error, ReportingGroundingError):
        codes = ["reporting_identity_rejected"]
    elif isinstance(error, ReportArtifactError):
        codes = ["artifact_rejected"]
        artifact_reason = (
            _known(getattr(error, "reason", None), ARTIFACT_REASONS, "") or None
        )
        field = _known(getattr(error, "field", None), FIELDS, "") or None
        finding_index = _bounded_positive_int(
            getattr(error, "finding_index", None), MAX_FINDING_INDEX
        )
    return {
        **({"artifact_reason": artifact_reason} if artifact_reason else {}),
        **({"markdown_reason": markdown_reason} if markdown_reason else {}),
        **({"markdown_line": markdown_line} if markdown_line is not None else {}),
        **(
            {"markdown_excerpt": markdown_excerpt}
            if markdown_excerpt is not None
            else {}
        ),
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
    has_malformed_markdown = "malformed_markdown" in codes[:MAX_ISSUES]
    has_artifact_rejection = any(
        type(code) is str and code in {"artifact_rejected", "report_artifact_invalid"}
        for code in codes[:MAX_ISSUES]
    )
    artifact_reason = (
        _known(value.get("artifact_reason"), ARTIFACT_REASONS, "")
        if has_artifact_rejection
        else ""
    )
    markdown_reason = (
        _known(value.get("markdown_reason"), MARKDOWN_REASONS, "")
        if has_malformed_markdown
        else ""
    )
    markdown_line = (
        _bounded_positive_int(value.get("markdown_line"), MAX_MARKDOWN_LINE)
        if has_malformed_markdown
        else None
    )
    markdown_excerpt = (
        _bounded_markdown_excerpt(value.get("markdown_excerpt"))
        if has_malformed_markdown
        else None
    )
    return {
        **({"artifact_reason": artifact_reason} if artifact_reason else {}),
        **({"markdown_reason": markdown_reason} if markdown_reason else {}),
        **({"markdown_line": markdown_line} if markdown_line is not None else {}),
        **(
            {"markdown_excerpt": markdown_excerpt}
            if markdown_excerpt is not None
            else {}
        ),
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

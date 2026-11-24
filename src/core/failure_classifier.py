"""Single canonical classifier mapping every failure path to a bounded class.

Every failure path (exception types, validation diagnostics, artifact reasons,
provider outcomes, HTTP statuses and request states) maps to exactly one class:

- ``repairable``: a contract, validation or grounding rejection that names a
  rule and, where possible, a finding and field.
- ``transient``: a timeout, 408, 429, 5xx or network error. Transient retries
  remain owned by the model/feed clients.
- ``fail_fast``: auth, quota, configuration, source/reporting identity, site
  safety (active content), integrity, output-token limit, publication/archive
  failure, or any unknown/unclassified failure.

Unknown failures always default to ``fail_fast``.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Literal, Mapping

import httpx

from .attempt_budget import AttemptBudgetError
from .finding_evidence import EvidenceError
from .opencode_client import OpenCodeUnavailable
from .openrouter_client import (
    RETRYABLE_CODES,
    OpenRouterError,
    OpenRouterModelMismatch,
    OpenRouterOutputLimitExceeded,
    OpenRouterUnavailable,
)
from .paid_verification import PaidVerificationError
from .publication_transaction import PublicationError
from .repair_budget import RepairBudgetError
from .report_artifact import ReportArtifactError
from .report_validation import ReportValidationIssue
from .reporting import ReportingGroundingError
from .reviewed_report import ReportingSelectionError, ReviewedReportValidationError
from .source_review import SourceReviewError
from .validation_diagnostics import SOURCE_CODES, UNKNOWN_CODE

FailureClass = Literal["repairable", "transient", "fail_fast"]
RepairScope = Literal["finding", "section", "report", "none"]

# Finding-level contract, validation and grounding rules where regenerating a
# single finding block against its already-cited sources can resolve the fault.
REPAIRABLE_FINDING_RULES: frozenset[str] = frozenset(
    {
        # Version reference protocol / evidence rules (finding-scoped).
        "duplicate_version_reference",
        "invalid_version_evidence_state",
        "invalid_version_reference",
        "invalid_version_reference_field",
        "invalid_version_reference_protocol",
        "invalid_version_reference_source",
        "misplaced_version_reference",
        "missing_version_references",
        "unresolved_version_evidence",
        "unsupported_version_absence",
        "unsupported_version_reference",
        "version_reference_collision",
        "wrapped_version_reference",
        # Finding evidence & grounding rules (finding-scoped).
        "finding_evidence_rejected",
        "action_without_recommendation",
        "affected_version_not_grounded",
        "detail_not_grounded",
        "duplicate_finding_field",
        "exception_not_grounded",
        "invalid_vendor_link",
        "missing_affected_version_entries",
        "missing_conflicting_exploitation_evidence",
        "missing_detail_field",
        "missing_negative_exploitation_evidence",
        "missing_source_details",
        "missing_source_exclusions",
        "missing_source_recommendation",
        "non_affected_version_clause",
        "recommendation_not_grounded",
        "unsupported_affected_version_entry",
        "unsupported_exploitation_status",
        "unsupported_finding_exploitation_claim",
        "unsupported_vendor_link",
        # Finding-scoped content & artifact rules.
        "missing_descriptive_finding_title",
        "invalid_cve_ids",
        "invalid_triage_value",
        "invalid_version_status",
        "missing_required_field",
        "empty_finding_slug",
        "duplicate_finding_slug",
    }
)

# Section-level rules repaired at the smallest enclosing section when possible.
# ``malformed_markdown`` is promoted to finding scope whenever its line lies
# inside a finding block, and stays section-scoped otherwise.
REPAIRABLE_SECTION_RULES: frozenset[str] = frozenset(
    {
        "malformed_markdown",
        "executive_summary_readability",
        "underpopulated_threat_actor_activities",
        "unsupported_summary_exploitation_claim",
        "removed_source_attribution",
    }
)

# Report-level structural/coverage rules with no smaller repairable unit.
REPAIRABLE_REPORT_RULES: frozenset[str] = frozenset(
    {
        "duplicate_section",
        "missing_section",
        "noncanonical_section_heading",
        "missing_expected_cves",
        "empty_report",
        "missing_finding_section",
        "missing_active_exploitation_section",
        "missing_findings",
    }
)

REPAIRABLE_RULES: frozenset[str] = (
    REPAIRABLE_FINDING_RULES | REPAIRABLE_SECTION_RULES | REPAIRABLE_REPORT_RULES
)

# Transient transport / provider / rate-limit rules (already retried by client).
TRANSIENT_RULES: frozenset[str] = frozenset(
    {
        "model_provider_unavailable",
        "model_rate_limited",
        "feed_fetch_failed",
    }
)

# Site-safety, identity and integrity rules that always block the entire report
# and are never repaired or dropped.
HARD_BLOCK_RULES: frozenset[str] = SOURCE_CODES | frozenset(
    {
        # Site safety & policy.
        "active_content",
        "virtual_event_promotion",
        "error_marker",
        # Identity & integrity.
        "reporting_identity_rejected",
        "finding_cve_identity_mismatch",
        "partial_cve_identifier",
        "invalid_reporting_field",
        "source_coverage_mismatch",
        "invalid_front_matter",
        "missing_metadata",
        "invalid_metadata",
        "invalid_source_coverage",
    }
)

# Source-side ambiguity/retention rules, auth/quota/config, output-token limit,
# publication/archive/workflow errors and generic failures.
FAIL_FAST_RULES: frozenset[str] = HARD_BLOCK_RULES | frozenset(
    {
        # Auth, quota, model identity, configuration, output limit, budget.
        "model_auth_rejected",
        "model_identity_mismatch",
        "model_output_limit_exceeded",
        "input_budget_exceeded",
        "request_budget_unresolved",
        "feed_url_missing",
        "report_output_name_invalid",
        # Ambiguous or missing retained source evidence (source-side).
        "ambiguous_affected_version_audience",
        "ambiguous_affected_version_audience_predicate",
        "ambiguous_affected_version_clause",
        "ambiguous_affected_version_continuation",
        "ambiguous_affected_version_grouping",
        "ambiguous_affected_version_polarity",
        "ambiguous_affected_version_range_continuation",
        "ambiguous_recommendation_scope",
        "ambiguous_version_cve_attribution",
        "missing_retained_source_content",
        "missing_retained_source_evidence",
        # Publication, archive, review-packet, workflow and generic failures.
        "site_build_failed",
        "publication_failed",
        "publication_recovery_required",
        "publication_rolled_back",
        "invalid_publication_stage",
        "filesystem_error",
        "archive_conflict",
        "review_packet_write_failed",
        "source_review_failed",
        "insufficient_valid_findings",
        "analysis_failed",
        "analysis_exception",
        "model_request_failed",
        "artifact_rejected",
        "report_artifact_invalid",
        UNKNOWN_CODE,
    }
)


@dataclass(frozen=True)
class ClassifiedFailure:
    """Result of classifying a single failure path."""

    failure_class: FailureClass
    rule: str
    scope: RepairScope = "none"
    finding_index: int | None = None
    field: str | None = None
    reason: str = ""

    @property
    def is_hard_block(self) -> bool:
        return self.rule in HARD_BLOCK_RULES


def _rule_scope(rule: str, finding_index: int | None) -> RepairScope:
    if rule == "malformed_markdown":
        return "finding" if finding_index is not None else "section"
    if rule in REPAIRABLE_FINDING_RULES:
        return "finding"
    if rule in REPAIRABLE_SECTION_RULES:
        return "section"
    if rule in REPAIRABLE_REPORT_RULES:
        return "report"
    return "none"


def classify_rule(
    rule: str | None,
    *,
    finding_index: int | None = None,
    field: str | None = None,
) -> ClassifiedFailure:
    """Classify one canonical rule/code string. Unknown rules default to fail_fast."""
    if not isinstance(rule, str) or not rule:
        return ClassifiedFailure(
            failure_class="fail_fast",
            rule=UNKNOWN_CODE,
            scope="none",
            finding_index=finding_index,
            field=field,
            reason="unknown_failure",
        )
    if rule in HARD_BLOCK_RULES:
        return ClassifiedFailure(
            failure_class="fail_fast",
            rule=rule,
            scope="none",
            finding_index=finding_index,
            field=field,
            reason="identity_integrity_or_safety_block",
        )
    if rule in REPAIRABLE_RULES and field == "Reporting":
        # Source/reporting identity is never repaired, whatever the rule.
        return ClassifiedFailure(
            failure_class="fail_fast",
            rule=rule,
            scope="none",
            finding_index=finding_index,
            field=field,
            reason="identity_integrity_or_safety_block",
        )
    if rule in REPAIRABLE_RULES:
        return ClassifiedFailure(
            failure_class="repairable",
            rule=rule,
            scope=_rule_scope(rule, finding_index),
            finding_index=finding_index,
            field=field,
            reason="contract_validation_or_grounding_rejection",
        )
    if rule in TRANSIENT_RULES:
        return ClassifiedFailure(
            failure_class="transient",
            rule=rule,
            scope="none",
            finding_index=finding_index,
            field=field,
            reason="transient_transport_or_provider_error",
        )
    if rule in FAIL_FAST_RULES:
        return ClassifiedFailure(
            failure_class="fail_fast",
            rule=rule,
            scope="none",
            finding_index=finding_index,
            field=field,
            reason="non_repairable_failure",
        )
    return ClassifiedFailure(
        failure_class="fail_fast",
        rule=UNKNOWN_CODE,
        scope="none",
        finding_index=finding_index,
        field=field,
        reason="unknown_failure",
    )


def classify_failure(
    *,
    error: BaseException | None = None,
    diagnostic: Mapping[str, Any] | None = None,
    stage: str | None = None,
    code: str | None = None,
    artifact_reason: str | None = None,
    request_state: str | None = None,
    http_status: int | None = None,
    provider_code: int | None = None,
) -> ClassifiedFailure:
    """Classify an exception, diagnostic dict, rule code, or provider outcome.

    Identity, integrity and site-safety blockers take precedence over any
    co-occurring repairable issue. Unknown failures always map to ``fail_fast``.
    """
    # 1. Inspect explicit exception instances first.
    if error is not None:
        if isinstance(error, OpenRouterOutputLimitExceeded):
            return ClassifiedFailure(
                failure_class="fail_fast",
                rule="model_output_limit_exceeded",
                reason="output_token_limit",
            )
        if isinstance(error, OpenRouterModelMismatch):
            return ClassifiedFailure(
                failure_class="fail_fast",
                rule="model_identity_mismatch",
                reason="model_identity_mismatch",
            )
        if isinstance(error, (AttemptBudgetError, RepairBudgetError)):
            return ClassifiedFailure(
                failure_class="fail_fast",
                rule="request_budget_unresolved",
                reason="request_budget_unresolved",
            )
        if getattr(error, "code", None) == "insufficient_valid_findings":
            return ClassifiedFailure(
                failure_class="fail_fast",
                rule="insufficient_valid_findings",
                reason="non_repairable_failure",
            )
        if isinstance(error, PaidVerificationError):
            return ClassifiedFailure(
                failure_class="fail_fast",
                rule="model_auth_rejected",
                reason="paid_verification_guard",
            )
        if isinstance(error, (OpenRouterUnavailable, OpenCodeUnavailable)):
            return ClassifiedFailure(
                failure_class="transient",
                rule="model_provider_unavailable",
                reason="provider_unavailable",
            )
        if isinstance(error, OpenRouterError):
            status = error.provider_code or error.http_status
            if status in {401, 402, 403}:
                return ClassifiedFailure(
                    failure_class="fail_fast",
                    rule="model_auth_rejected",
                    reason="auth_or_quota_rejected",
                )
            if error.retryable or status in RETRYABLE_CODES:
                rule = (
                    "model_rate_limited"
                    if status == 429
                    else "model_provider_unavailable"
                )
                return ClassifiedFailure(
                    failure_class="transient",
                    rule=rule,
                    reason="transient_provider_status",
                )
            return ClassifiedFailure(
                failure_class="fail_fast",
                rule="model_request_failed",
                reason="permanent_or_uncertain_provider_error",
            )
        if isinstance(
            error,
            (
                httpx.TimeoutException,
                httpx.TransportError,
                ConnectionError,
                TimeoutError,
            ),
        ):
            return ClassifiedFailure(
                failure_class="transient",
                rule="model_provider_unavailable",
                reason="network_or_timeout_error",
            )
        if isinstance(error, ReportingGroundingError):
            return ClassifiedFailure(
                failure_class="fail_fast",
                rule="reporting_identity_rejected",
                field="Reporting",
                reason="identity_integrity_or_safety_block",
            )
        if isinstance(error, ReportingSelectionError):
            return classify_rule(
                error.code, finding_index=error.finding_index, field="Reporting"
            )
        if isinstance(error, SourceReviewError):
            return classify_rule(error.code)
        if isinstance(error, PublicationError):
            return classify_rule(error.code)
        if isinstance(error, EvidenceError):
            finding_index = (
                error.finding_index if isinstance(error.finding_index, int) else None
            )
            return classify_rule(
                error.code, finding_index=finding_index, field=error.field
            )
        if isinstance(error, ReportArtifactError):
            reason = getattr(error, "reason", None)
            field = getattr(error, "field", None)
            finding_index = getattr(error, "finding_index", None)
            idx = finding_index if isinstance(finding_index, int) else None
            if isinstance(reason, str) and reason:
                return classify_rule(reason, finding_index=idx, field=field)
            return ClassifiedFailure(
                failure_class="fail_fast",
                rule="artifact_rejected",
                finding_index=idx,
                field=field,
                reason="unspecified_artifact_rejection",
            )
        if isinstance(error, ReviewedReportValidationError):
            issues = [
                issue
                for issue in (error.issues or [])
                if isinstance(issue, ReportValidationIssue)
            ]
            if not issues:
                return ClassifiedFailure(
                    failure_class="fail_fast",
                    rule=UNKNOWN_CODE,
                    reason="empty_validation_issues",
                )
            # Hard blockers always win over any co-occurring repairable issues.
            for issue in issues:
                if issue.code in HARD_BLOCK_RULES:
                    return classify_rule(issue.code)
            for issue in issues:
                classified = classify_rule(issue.code)
                if classified.failure_class == "repairable":
                    return classified
            return classify_rule(issues[0].code)
        # Any unrecognized exception type fails fast.
        return ClassifiedFailure(
            failure_class="fail_fast",
            rule=UNKNOWN_CODE,
            reason=f"unclassified_exception:{type(error).__name__}",
        )

    # 2. Inspect structured diagnostic payload if provided.
    if diagnostic is not None:
        raw_codes = diagnostic.get("codes")
        codes = (
            [c for c in raw_codes if isinstance(c, str)]
            if isinstance(raw_codes, list)
            else []
        )
        diag_field = diagnostic.get("field")
        field = diag_field if isinstance(diag_field, str) else None
        diag_index = diagnostic.get("finding_index")
        finding_index = diag_index if isinstance(diag_index, int) else None
        diag_artifact_reason = diagnostic.get("artifact_reason")
        if not artifact_reason and isinstance(diag_artifact_reason, str):
            artifact_reason = diag_artifact_reason

        # Hard blockers always take precedence.
        for candidate_code in codes:
            if candidate_code in HARD_BLOCK_RULES:
                return classify_rule(
                    candidate_code, finding_index=finding_index, field=field
                )
        if artifact_reason:
            return classify_rule(
                artifact_reason, finding_index=finding_index, field=field
            )
        for candidate_code in codes:
            if candidate_code in TRANSIENT_RULES:
                return classify_rule(
                    candidate_code, finding_index=finding_index, field=field
                )
        for candidate_code in codes:
            if candidate_code in REPAIRABLE_RULES:
                return classify_rule(
                    candidate_code, finding_index=finding_index, field=field
                )
        if codes:
            return classify_rule(codes[0], finding_index=finding_index, field=field)

    # 3. Direct rule / artifact_reason / provider outcome inputs.
    if artifact_reason:
        return classify_rule(artifact_reason)
    if code:
        return classify_rule(code)

    status = provider_code or http_status
    if status in {401, 402, 403}:
        return ClassifiedFailure(
            failure_class="fail_fast",
            rule="model_auth_rejected",
            reason="auth_or_quota_rejected",
        )
    if status in RETRYABLE_CODES:
        return ClassifiedFailure(
            failure_class="transient",
            rule=(
                "model_rate_limited" if status == 429 else "model_provider_unavailable"
            ),
            reason="transient_http_status",
        )
    if request_state in {"not_sent", "retryable_rejection"}:
        return ClassifiedFailure(
            failure_class="transient",
            rule="model_provider_unavailable",
            reason="transient_request_state",
        )
    if stage in {"source_review", "reporting_identity", "source_coverage"}:
        return ClassifiedFailure(
            failure_class="fail_fast",
            rule=UNKNOWN_CODE,
            reason="identity_integrity_or_safety_block",
        )
    return ClassifiedFailure(
        failure_class="fail_fast",
        rule=UNKNOWN_CODE,
        reason="unknown_failure",
    )

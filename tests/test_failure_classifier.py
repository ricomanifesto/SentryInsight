"""Exhaustive unit tests for the single canonical failure classifier."""

from __future__ import annotations

import httpx
import pytest

from src.core.attempt_budget import AttemptBudgetError
from src.core.failure_classifier import (
    FAIL_FAST_RULES,
    HARD_BLOCK_RULES,
    REPAIRABLE_RULES,
    TRANSIENT_RULES,
    classify_failure,
    classify_rule,
)
from src.core.finding_evidence import EvidenceError
from src.core.opencode_client import OpenCodeUnavailable
from src.core.openrouter_client import (
    OpenRouterError,
    OpenRouterModelMismatch,
    OpenRouterOutputLimitExceeded,
    OpenRouterUnavailable,
)
from src.core.paid_verification import PaidVerificationError
from src.core.publication_transaction import PublicationError
from src.core.repair_budget import RepairBudgetError
from src.core.report_artifact import ReportArtifactError
from src.core.report_repair import InsufficientValidFindingsError
from src.core.report_validation import ReportValidationIssue
from src.core.reporting import ReportingGroundingError
from src.core.reviewed_report import (
    ReportingSelectionError,
    ReviewedReportValidationError,
)
from src.core.source_review import SourceReviewError
from src.core.validation_diagnostics import (
    ARTIFACT_REASONS,
    CONTENT_CODES,
    EVIDENCE_CODES,
    SOURCE_CODES,
    UNKNOWN_CODE,
    WORKFLOW_CODES,
)


def test_rule_sets_are_mutually_disjoint_and_cover_all_allowlisted_codes():
    assert REPAIRABLE_RULES.isdisjoint(TRANSIENT_RULES)
    assert REPAIRABLE_RULES.isdisjoint(FAIL_FAST_RULES)
    assert TRANSIENT_RULES.isdisjoint(FAIL_FAST_RULES)
    assert HARD_BLOCK_RULES <= FAIL_FAST_RULES

    all_mapped = REPAIRABLE_RULES | TRANSIENT_RULES | FAIL_FAST_RULES
    expected_known = (
        SOURCE_CODES
        | EVIDENCE_CODES
        | CONTENT_CODES
        | ARTIFACT_REASONS
        | WORKFLOW_CODES
    )
    unmapped = expected_known - all_mapped
    assert unmapped == set(), f"Unmapped allowlisted codes: {sorted(unmapped)}"


@pytest.mark.parametrize(
    "rule,expected_scope",
    [
        ("invalid_cve_ids", "finding"),
        ("invalid_triage_value", "finding"),
        ("invalid_version_reference_field", "finding"),
        ("unsupported_vendor_link", "finding"),
        ("invalid_vendor_link", "finding"),
        ("missing_descriptive_finding_title", "finding"),
        ("malformed_markdown", "section"),
        ("executive_summary_readability", "section"),
        ("duplicate_section", "report"),
        ("missing_expected_cves", "report"),
    ],
)
def test_repairable_rules_classify_with_expected_scope(rule, expected_scope):
    result = classify_rule(rule)
    assert result.failure_class == "repairable"
    assert result.rule == rule
    assert result.scope == expected_scope
    assert not result.is_hard_block


def test_malformed_markdown_promotes_to_finding_scope_when_finding_index_known():
    result = classify_rule("malformed_markdown", finding_index=2)
    assert result.failure_class == "repairable"
    assert result.scope == "finding"
    assert result.finding_index == 2


@pytest.mark.parametrize(
    "kwargs,expected_rule",
    [
        (
            {"error": OpenRouterUnavailable("timeout")},
            "model_provider_unavailable",
        ),
        (
            {"error": OpenCodeUnavailable("server down")},
            "model_provider_unavailable",
        ),
        (
            {"error": OpenRouterError("rate limited", retryable=True, http_status=429)},
            "model_rate_limited",
        ),
        (
            {
                "error": OpenRouterError(
                    "upstream error", retryable=True, http_status=503
                )
            },
            "model_provider_unavailable",
        ),
        ({"error": httpx.ReadTimeout("timed out")}, "model_provider_unavailable"),
        ({"error": ConnectionError("reset")}, "model_provider_unavailable"),
        ({"http_status": 408}, "model_provider_unavailable"),
        ({"http_status": 429}, "model_rate_limited"),
        ({"http_status": 502}, "model_provider_unavailable"),
        ({"request_state": "retryable_rejection"}, "model_provider_unavailable"),
        ({"code": "feed_fetch_failed"}, "feed_fetch_failed"),
    ],
)
def test_transient_failures_classify_as_transient(kwargs, expected_rule):
    result = classify_failure(**kwargs)
    assert result.failure_class == "transient"
    assert result.rule == expected_rule
    assert result.scope == "none"


@pytest.mark.parametrize(
    "kwargs,expected_rule",
    [
        (
            {"error": OpenRouterOutputLimitExceeded("truncated", http_status=200)},
            "model_output_limit_exceeded",
        ),
        (
            {"error": OpenRouterModelMismatch("wrong model")},
            "model_identity_mismatch",
        ),
        (
            {"error": OpenRouterError("unauthorized", http_status=401)},
            "model_auth_rejected",
        ),
        (
            {"error": OpenRouterError("payment required", provider_code=402)},
            "model_auth_rejected",
        ),
        ({"error": AttemptBudgetError()}, "request_budget_unresolved"),
        ({"error": RepairBudgetError()}, "request_budget_unresolved"),
        (
            {"error": InsufficientValidFindingsError(0, 1)},
            "insufficient_valid_findings",
        ),
        ({"error": PaidVerificationError()}, "model_auth_rejected"),
        ({"error": ReportingGroundingError("bad url")}, "reporting_identity_rejected"),
        (
            {"error": ReportingSelectionError("quarantined_reporting_source", 1)},
            "quarantined_reporting_source",
        ),
        (
            {"error": SourceReviewError("model_supplied_coverage")},
            "model_supplied_coverage",
        ),
        (
            {
                "error": EvidenceError(
                    "cve mismatch",
                    code="finding_cve_identity_mismatch",
                    field="CVE IDs",
                )
            },
            "finding_cve_identity_mismatch",
        ),
        (
            {"error": PublicationError("publication_failed")},
            "publication_failed",
        ),
        (
            {
                "error": ReviewedReportValidationError(
                    [ReportValidationIssue("active_content", "script tag")]
                )
            },
            "active_content",
        ),
        (
            {
                "error": ReviewedReportValidationError(
                    [ReportValidationIssue("virtual_event_promotion", "promo")]
                )
            },
            "virtual_event_promotion",
        ),
        (
            {"error": ReportArtifactError("unspecified")},
            "artifact_rejected",
        ),
        (
            {
                "error": ReportArtifactError(
                    "bad front matter", reason="invalid_front_matter"
                )
            },
            "invalid_front_matter",
        ),
        ({"code": "input_budget_exceeded"}, "input_budget_exceeded"),
        (
            {"code": "ambiguous_affected_version_clause"},
            "ambiguous_affected_version_clause",
        ),
        ({"http_status": 403}, "model_auth_rejected"),
    ],
)
def test_fail_fast_failures_classify_as_fail_fast(kwargs, expected_rule):
    result = classify_failure(**kwargs)
    assert result.failure_class == "fail_fast"
    assert result.rule == expected_rule
    assert result.scope == "none"


def test_unknown_failures_default_to_fail_fast():
    assert (
        classify_failure(error=RuntimeError("unexpected")).failure_class == "fail_fast"
    )
    assert classify_failure(code="brand_new_unmapped_code").failure_class == "fail_fast"
    assert classify_failure(code="brand_new_unmapped_code").rule == UNKNOWN_CODE
    assert classify_failure().failure_class == "fail_fast"
    assert (
        classify_failure(diagnostic={"codes": ["not_a_real_code"]}).failure_class
        == "fail_fast"
    )


def test_hard_blockers_take_precedence_over_repairable_issues():
    mixed_error = ReviewedReportValidationError(
        [
            ReportValidationIssue("malformed_markdown", "bad bullet"),
            ReportValidationIssue("active_content", "script tag"),
        ]
    )
    classified = classify_failure(error=mixed_error)
    assert classified.failure_class == "fail_fast"
    assert classified.rule == "active_content"
    assert classified.is_hard_block

    mixed_diag = {
        "stage": "report_content",
        "codes": ["duplicate_section", "virtual_event_promotion"],
    }
    diag_classified = classify_failure(diagnostic=mixed_diag)
    assert diag_classified.failure_class == "fail_fast"
    assert diag_classified.rule == "virtual_event_promotion"


def test_artifact_error_with_repairable_reason_classifies_as_repairable():
    err = ReportArtifactError(
        "bad cve",
        reason="invalid_cve_ids",
        field="CVE IDs",
        finding_index=3,
    )
    classified = classify_failure(error=err)
    assert classified.failure_class == "repairable"
    assert classified.rule == "invalid_cve_ids"
    assert classified.scope == "finding"
    assert classified.finding_index == 3
    assert classified.field == "CVE IDs"


def test_diagnostic_with_artifact_reason_classifies_correctly():
    diag = {
        "stage": "report_artifact",
        "codes": ["artifact_rejected"],
        "artifact_reason": "invalid_triage_value",
        "field": "Severity",
        "finding_index": 2,
    }
    classified = classify_failure(diagnostic=diag)
    assert classified.failure_class == "repairable"
    assert classified.rule == "invalid_triage_value"
    assert classified.scope == "finding"
    assert classified.finding_index == 2
    assert classified.field == "Severity"


def test_reporting_identity_field_is_never_repairable():
    classified = classify_rule(
        "missing_required_field", finding_index=1, field="Reporting"
    )
    assert classified.failure_class == "fail_fast"
    assert classify_rule("missing_required_field", field="Severity").failure_class == (
        "repairable"
    )


def test_every_classified_rule_is_a_real_diagnostic_code():
    known = (
        SOURCE_CODES
        | EVIDENCE_CODES
        | CONTENT_CODES
        | ARTIFACT_REASONS
        | WORKFLOW_CODES
    )
    invented = (REPAIRABLE_RULES | TRANSIENT_RULES | FAIL_FAST_RULES) - known
    assert invented == set()

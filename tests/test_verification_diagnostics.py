"""Diagnostic disclosure is finite; the real validation decision is unchanged."""

import asyncio
import json

import httpx
import pytest

from scripts.verification_diagnostics import (
    MAX_FINDING_INDEX,
    MAX_ISSUES,
    UNKNOWN_CODE,
    validation_diagnostic,
)
from scripts.verify_report_generation import VerificationClient, verify_articles
from src.core import reviewed_report
from src.core.finding_evidence import EvidenceError
from src.core.report_artifact import ReportArtifactError
from src.core.report_validation import ReportValidationIssue
from src.core.reporting import ReportingGroundingError
from src.core.reviewed_report import ReviewedReportValidationError
from src.core.source_review import PLAN_KEY, SourceReviewError
from test_generation_verification import articles, response
from test_reviewed_report import prepared_result

PRIVATE = "PRIVATE-MARKER https://private.example/secret"


def mutate(result, change):
    if change == "shape":
        result["exploitation_report"] = None
    elif change == "plan":
        result.pop(PLAN_KEY)
    else:
        text = result["exploitation_report"]
        if change == "coverage":
            text += "\n\n## Source Coverage and Review\n" + PRIVATE
        elif change == "section":
            text = text.replace("## Active Exploitation Details", "## Other")
        elif change == "version":
            text = text.replace(
                "**Affected Versions**: Not stated in supplied sources.",
                "**Affected Versions**: " + PRIVATE,
            )
        elif change == "recommendation":
            text = text.replace(
                "**Recommended Actions**: Not stated in supplied sources.",
                "**Recommended Actions**: Install " + PRIVATE,
            )
        elif change == "content":
            text = text.replace("## Threat Actor Activities", "## Other")
        elif change == "artifact":
            text = text.replace("**Severity**: unknown", "**Severity**: urgent")
        result["exploitation_report"] = text
    return result


CASES = [
    ("shape", "candidate_structure", "invalid_review_candidate"),
    ("coverage", "candidate_structure", "model_supplied_coverage"),
    ("plan", "source_review", "source_review_plan_missing"),
    ("section", "reporting_identity", "review_candidate_missing_findings"),
    ("version", "version_references", "invalid_version_reference"),
    ("recommendation", "finding_evidence", "recommendation_not_grounded"),
    ("content", "report_content", "missing_section"),
    ("artifact", "report_artifact", "artifact_rejected"),
]


@pytest.mark.parametrize(("change", "stage", "code"), CASES)
def test_real_rejections_keep_exception_type_and_gain_only_safe_categories(
    change, stage, code
):
    result = mutate(prepared_result(), change)
    with pytest.raises(Exception) as original:
        reviewed_report.resolve_reviewed_analysis(result)
    stages = []
    with pytest.raises(type(original.value)) as observed:
        reviewed_report.resolve_reviewed_analysis(result, on_stage=stages.append)
    assert str(original.value) == str(observed.value)
    diagnostic = validation_diagnostic(stages[-1], observed.value)
    assert diagnostic["stage"] == stage
    assert diagnostic["codes"] == [code]
    assert PRIVATE not in json.dumps(diagnostic)


def test_successful_observation_changes_neither_report_bytes_nor_coverage():
    result = prepared_result()
    normal = reviewed_report.resolve_reviewed_analysis(result)
    stages = []
    observed = reviewed_report.resolve_reviewed_analysis(result, on_stage=stages.append)
    assert observed == normal
    assert stages == [
        "candidate_structure",
        "source_review",
        "reporting_identity",
        "version_references",
        "finding_evidence",
        "reporting_identity",
        "report_content",
        "source_coverage",
        "report_artifact",
    ]


@pytest.mark.parametrize(
    ("function", "stage", "error", "code"),
    [
        (
            "resolve_reporting_keys",
            "reporting_identity",
            ReportingGroundingError(PRIVATE),
            "reporting_identity_rejected",
        ),
        (
            "make_source_coverage",
            "source_coverage",
            SourceReviewError("invalid_source_coverage"),
            "invalid_source_coverage",
        ),
        (
            "parse_report_artifact",
            "report_artifact",
            RuntimeError(PRIVATE),
            UNKNOWN_CODE,
        ),
    ],
)
def test_remaining_boundaries_preserve_failures_and_do_not_guess_messages(
    function, stage, error, code, monkeypatch
):
    def reject(*args, **kwargs):
        raise error

    monkeypatch.setattr(reviewed_report, function, reject)
    stages = []
    with pytest.raises(type(error)) as caught:
        reviewed_report.resolve_reviewed_analysis(
            prepared_result(), on_stage=stages.append
        )
    assert caught.value is error
    diagnostic = validation_diagnostic(stages[-1], error)
    assert diagnostic["stage"] == stage
    assert diagnostic["codes"] == [code]
    assert PRIVATE not in json.dumps(diagnostic)


@pytest.mark.parametrize(
    ("change", "stage", "code"),
    [case for case in CASES if case[0] not in {"shape", "plan"}],
)
def test_real_prompt_receipt_exports_diagnostic_without_answer_or_publication(
    change, stage, code, tmp_path, monkeypatch, caplog, capsys
):
    inputs = articles()
    answer = mutate(prepared_result(inputs), change)["exploitation_report"]
    calls = []

    def provider(request):
        calls.append(request)
        return response(answer)

    monkeypatch.chdir(tmp_path)
    last_good = tmp_path / "index.md"
    last_good.write_text("last-good sentinel")
    receipt = asyncio.run(
        verify_articles(
            inputs,
            client=VerificationClient("test-secret", httpx.MockTransport(provider)),
        )
    )
    assert receipt["outcome"] == "validation_failed"
    assert receipt["attempted"] == len(calls) == 1
    assert receipt["provider"]["http_status"] == 200
    assert receipt["provider"]["finish_reason"] == "stop"
    assert receipt["validation_diagnostic"]["stage"] == stage
    assert receipt["validation_diagnostic"]["codes"] == [code]
    assert receipt["published"] is receipt["production_ready"] is False
    output = json.dumps(receipt) + caplog.text + str(capsys.readouterr())
    assert PRIVATE not in output
    assert "test-secret" not in output
    assert answer not in output
    assert list(tmp_path.iterdir()) == [last_good]
    assert last_good.read_text() == "last-good sentinel"


@pytest.mark.parametrize("index", [True, -1, MAX_FINDING_INDEX + 1, 1.5, "1"])
def test_arbitrary_error_attributes_cannot_expand_disclosure(index):
    error = EvidenceError(
        PRIVATE,
        code="looks_like_a_secret_code",
        field=PRIVATE,
        expected=PRIVATE,
        observed=PRIVATE,
    )
    error.finding_index = index
    error.source_keys = (PRIVATE,)
    error.cves = (PRIVATE,)
    error.finding_sha256 = PRIVATE
    diagnostic = validation_diagnostic(PRIVATE, error)
    assert diagnostic == {
        "schema_version": 1,
        "stage": "unknown_validation_stage",
        "codes": [UNKNOWN_CODE],
        "field": None,
        "finding_index": None,
        "issues_truncated": False,
    }


def test_known_field_and_bounded_finding_index_are_retained():
    error = EvidenceError(PRIVATE, code="detail_not_grounded", field="Exceptions")
    error.finding_index = 3
    diagnostic = validation_diagnostic("finding_evidence", error)
    assert diagnostic["field"] == "Exceptions"
    assert diagnostic["finding_index"] == 3
    assert diagnostic["codes"] == ["detail_not_grounded"]


def test_issue_list_is_bounded_and_unknown_codes_are_not_echoed():
    issues = [
        ReportValidationIssue("missing_section", PRIVATE),
        ReportValidationIssue(PRIVATE, PRIVATE),
        ReportValidationIssue([], PRIVATE),
        PRIVATE,
    ] + [ReportValidationIssue("active_content", PRIVATE)] * 1000
    diagnostic = validation_diagnostic(
        "report_content", ReviewedReportValidationError(issues)
    )
    assert diagnostic["codes"] == ["missing_section", UNKNOWN_CODE, "active_content"]
    assert diagnostic["issues_truncated"] is True
    assert len(diagnostic["codes"]) <= MAX_ISSUES
    assert len(json.dumps(diagnostic)) < 1024
    assert PRIVATE not in json.dumps(diagnostic)


@pytest.mark.parametrize("issues", [[], None, PRIVATE, (PRIVATE,)])
def test_malformed_issue_container_gets_a_fixed_fallback(issues):
    error = ReviewedReportValidationError([])
    error.issues = issues
    assert validation_diagnostic("report_content", error)["codes"] == [UNKNOWN_CODE]


def test_exception_text_and_repr_are_never_inspected():
    class Unprintable(ReportArtifactError):
        def __str__(self):
            raise AssertionError("must not stringify")

        def __repr__(self):
            raise AssertionError("must not repr")

    diagnostic = validation_diagnostic("report_artifact", Unprintable(PRIVATE))
    assert diagnostic["codes"] == ["artifact_rejected"]
    assert PRIVATE not in json.dumps(diagnostic)


def test_source_codes_are_allowlisted_instead_of_trusting_exception_type():
    diagnostic = validation_diagnostic("source_review", SourceReviewError(PRIVATE))
    assert diagnostic["codes"] == [UNKNOWN_CODE]
    assert PRIVATE not in json.dumps(diagnostic)

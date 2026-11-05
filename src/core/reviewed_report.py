"""Strict whole-candidate validation after source review, before coverage rendering."""

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, Mapping

from .article_policy import contains_virtual_event_tag
from .cve import extract_cve_ids
from .finding_evidence import (
    EvidenceError,
    validate_finding_evidence,
    validate_vendor_links,
)
from .report_artifact import DIGEST_ARCHIVE_ROOT, parse_report_artifact
from .reporting import (
    ACTIVE_SECTION_PATTERN,
    FINDING_PATTERN,
    REPORTING_FIELD_PATTERN,
    ReportingGroundingError,
    ReportingSource,
    deserialize_reporting_catalog,
    resolve_reporting_keys,
    serialize_reporting_catalog,
)
from .report_validation import (
    ReportValidationIssue,
    blocking_issues,
    prepare_generated_report,
    validate_report_content,
)
from .source_coverage import (
    coverage_markdown,
    make_source_coverage,
    visible_candidate_text,
)
from .source_review import (
    PLAN_KEY,
    SourceReviewError,
    SourceReviewPlan,
    canonical_json,
    plan_reporting_catalog,
    review_articles,
    validate_review_packet,
)
from .version_references import resolve_analysis_version_references


class ReviewedReportValidationError(ValueError):
    def __init__(self, issues: list[ReportValidationIssue]):
        self.issues = issues
        super().__init__("Report validation failed")


@dataclass(frozen=True)
class ReviewedReport:
    report: str
    coverage: dict[str, Any]
    catalog: dict[str, ReportingSource]
    source: str
    grounded_report: str
    # Bounded reasons for accuracy checks that advisory grounding logged
    # instead of blocking. Empty under strict grounding.
    advisories: tuple[dict, ...] = ()

    @property
    def covered_report(self) -> str:
        return self.report.rstrip() + "\n\n" + coverage_markdown(self.coverage)


def analysis_review_plan(result: Mapping[str, Any]) -> SourceReviewPlan:
    """Host metadata is mandatory; there is no legacy live-generation fallback."""
    if PLAN_KEY not in result or "reporting_metadata_cves" not in result:
        raise SourceReviewError("source_review_plan_missing")
    supplied = validate_review_packet(result[PLAN_KEY])
    metadata = result["reporting_metadata_cves"]
    if not isinstance(metadata, dict):
        raise SourceReviewError("invalid_source_metadata")
    try:
        catalog = deserialize_reporting_catalog(result.get("reporting_sources", []))
    except (ReportingGroundingError, TypeError, KeyError):
        raise SourceReviewError("invalid_review_input_catalog") from None
    plan = plan_reporting_catalog(catalog, metadata)
    if plan.packet != supplied:
        raise SourceReviewError("source_review_plan_mismatch")
    return plan


def _candidate_reporting_keys(report: str) -> list[str]:
    section = ACTIVE_SECTION_PATTERN.search(report)
    if not section:
        raise SourceReviewError("review_candidate_missing_findings")
    keys = set()
    for finding in FINDING_PATTERN.finditer(section.group("section")):
        for field in REPORTING_FIELD_PATTERN.finditer(finding.group("body")):
            keys.update(key.strip() for key in field["value"].split(","))
    if not keys:
        raise SourceReviewError("review_candidate_missing_findings")
    return sorted(keys)


def resolve_reviewed_analysis(
    result: Mapping[str, Any],
    *,
    on_stage: Callable[[str], None] | None = None,
    advisory: bool = False,
) -> ReviewedReport:
    """Validate every finding; optionally observe fixed stage names, never text.

    ``advisory`` keeps site-safety, structure and source-identity checks
    blocking, but records accuracy rejections (unresolvable versions,
    ungrounded finding evidence, out-of-scope CVEs, report-quality issues) as
    bounded reasons in ``advisories`` and publishes the report.
    """
    from .validation_diagnostics import validation_diagnostic

    advisories: list[dict] = []
    current = {"stage": "candidate_structure"}

    def stage(name: str) -> None:
        current["stage"] = name
        if on_stage is not None:
            on_stage(name)

    def advise(error: Exception) -> None:
        advisories.append(validation_diagnostic(current["stage"], error))

    stage("candidate_structure")
    raw = result.get("exploitation_report")
    if not isinstance(raw, str):
        raise SourceReviewError("invalid_review_candidate")
    if contains_virtual_event_tag(raw):
        raise ReviewedReportValidationError(
            [
                ReportValidationIssue(
                    "virtual_event_promotion",
                    "Report contains a blocked [Virtual Event] promotion.",
                )
            ]
        )
    visible_candidate_text(raw, reject_host_namespace=True)
    stage("source_review")
    plan = analysis_review_plan(result)
    if not plan.eligible_keys:
        raise SourceReviewError("source_review_required")
    stage("reporting_identity")
    prepared = prepare_generated_report(raw)
    cited = _candidate_reporting_keys(prepared)
    if not set(cited) <= set(plan.eligible_keys):
        raise SourceReviewError("quarantined_or_unknown_reporting_source")
    eligible_cves = {
        cve
        for row in plan.packet["sources"]
        if row["state"] == "eligible"
        for cve in row["cves"]
    }
    candidate_cves = set(extract_cve_ids(prepared)) | set(
        extract_cve_ids(visible_candidate_text(prepared))
    )
    if not candidate_cves <= eligible_cves:
        if not advisory:
            raise SourceReviewError("out_of_scope_candidate_cve")
        advise(SourceReviewError("out_of_scope_candidate_cve"))
    catalog = plan.eligible_catalog
    stage("version_references")
    canonical = resolve_analysis_version_references(
        {
            **result,
            "exploitation_report": prepared,
            "reporting_sources": serialize_reporting_catalog(catalog),
        },
        on_reject=advise if advisory else None,
    )
    stage("finding_evidence")
    if advisory:
        # Source identity stays blocking even when grounding is advisory.
        validate_vendor_links(canonical, catalog)
    try:
        validate_finding_evidence(canonical, catalog)
    except EvidenceError as exc:
        if not advisory:
            raise
        advise(exc)
    stage("reporting_identity")
    resolved = resolve_reporting_keys(canonical, catalog)
    stage("report_content")
    # Import only the pure prompt helpers at call time; analysis itself imports
    # the source planner. Expected IDs are recomputed, never trusted result data.
    from .analyze import (
        collect_exploitation_relevant_prompt_cves,
        format_article_summary,
    )

    expected_cves = {
        cve
        for article in review_articles(plan)
        for cve in collect_exploitation_relevant_prompt_cves(
            format_article_summary(article)
        )
    }
    issues = validate_report_content(resolved, expected_cves=expected_cves)
    if advisory:
        blocking = blocking_issues(issues)
        if len(blocking) < len(issues):
            advise(
                ReviewedReportValidationError(
                    [issue for issue in issues if issue not in blocking]
                )
            )
        issues = blocking
    if issues:
        raise ReviewedReportValidationError(issues)
    stage("source_coverage")
    coverage = make_source_coverage(plan.packet, cited)
    stage("report_artifact")
    report_date = str(
        result.get("date") or datetime.now(timezone.utc).date().isoformat()
    )
    generated_at = str(
        result.get("generated_at")
        or datetime.now(timezone.utc)
        .isoformat(timespec="seconds")
        .replace("+00:00", "Z")
    )
    source = (
        "---\nschema_version: 5\n"
        f"report_date: {report_date}\ngenerated_at: {generated_at}\n"
        f"digest_issue_url: {DIGEST_ARCHIVE_ROOT}{report_date}/\n"
        f"source_coverage: {canonical_json(coverage)}\n---\n"
        + resolved.lstrip().rstrip()
        + "\n\n"
        + coverage_markdown(coverage)
    )
    parse_report_artifact(source)
    return ReviewedReport(
        resolved, coverage, catalog, source, canonical, tuple(advisories)
    )

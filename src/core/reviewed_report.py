"""Strict whole-candidate validation after source review, before coverage rendering."""

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable, Mapping

from .article_policy import contains_virtual_event_tag
from .cve import extract_cve_ids
from .derivations import derivation_scope
from .finding_evidence import (
    EvidenceError,
    validate_finding_evidence,
    validate_vendor_links,
)
from .report_artifact import DIGEST_ARCHIVE_ROOT, parse_report_artifact
from .reporting import (
    REPORTING_KEY_PATTERN,
    ReportingGroundingError,
    ReportingSource,
    deserialize_reporting_catalog,
    resolve_reporting_keys,
    serialize_reporting_catalog,
)
from .report_findings import report_findings
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
    ADVISORY_POLICY_VERSION,
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


def analysis_review_plan(
    result: Mapping[str, Any], *, advisory: bool = False
) -> SourceReviewPlan:
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
    # An advisory resolver also accepts a strict plan (a subset of what it
    # would admit); a strict resolver never accepts an advisory plan.
    planned_advisory = supplied["policy_version"] == ADVISORY_POLICY_VERSION
    if planned_advisory and not advisory:
        raise SourceReviewError("source_review_plan_mismatch")
    plan = plan_reporting_catalog(catalog, metadata, advisory=planned_advisory)
    if plan.packet != supplied:
        raise SourceReviewError("source_review_plan_mismatch")
    return plan


class ReportingSelectionError(SourceReviewError):
    """A categorical identity rejection with no source or candidate text."""

    def __init__(self, code: str, finding_index: int):
        super().__init__(code)
        self.finding_index = finding_index


def _prepare_reporting_selection(
    report: str, plan: SourceReviewPlan
) -> tuple[str, list[str]]:
    """Canonicalize exact code-wrapped identities, then enforce admission.

    Never infer an identity from URLs, labels, substrings or nearby evidence.
    Every downstream validator receives the same canonical Reporting fields.
    """
    table = report_findings(report)
    if not table.has_section:
        raise SourceReviewError("review_candidate_missing_findings")
    cited: set[str] = set()
    eligible = set(plan.eligible_keys)

    def prepare(row):
        body = row.body
        fields = row.reporting_fields

        def reject(code):
            raise ReportingSelectionError(code, row.index)

        if len(fields) != 1:
            reject("invalid_reporting_field_count")
        field = fields[0]
        keys = []
        for token in field["value"].split(","):
            key = token.strip()
            if key.startswith("`") and key.endswith("`"):
                key = key[1:-1]
            if not REPORTING_KEY_PATTERN.fullmatch(key):
                reject("invalid_reporting_source_syntax")
            if key not in plan.catalog:
                reject("unknown_reporting_source")
            if key not in eligible:
                reject("quarantined_reporting_source")
            if key in keys:
                reject("duplicate_reporting_source")
            keys.append(key)
        cited.update(keys)
        return (
            row.heading
            + body[: field.start("value")]
            + ", ".join(keys)
            + body[field.end("value") :]
        )

    # A list, not a generator: a callback's exception propagates unchanged.
    canonical = table.render([(row.start, row.end, prepare(row)) for row in table.rows])
    if not cited:
        raise SourceReviewError("review_candidate_missing_findings")
    return canonical, sorted(cited)


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
    with derivation_scope():
        return _resolve_reviewed_analysis(result, on_stage=on_stage, advisory=advisory)


def _resolve_reviewed_analysis(
    result: Mapping[str, Any],
    *,
    on_stage: Callable[[str], None] | None,
    advisory: bool,
) -> ReviewedReport:
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
    plan = analysis_review_plan(result, advisory=advisory)
    if not plan.eligible_keys:
        raise SourceReviewError("source_review_required")
    stage("reporting_identity")
    prepared, cited = _prepare_reporting_selection(prepare_generated_report(raw), plan)
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
    issues = validate_report_content(
        resolved, expected_cves=expected_cves, require_descriptive_titles=True
    )
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

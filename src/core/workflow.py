from typing import Dict, Any, NotRequired, TypedDict, cast
from langgraph.graph import START, END, StateGraph
import logfire
import logging
import asyncio
import json
import shutil
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from ..services.fetch import SentryDigestFeedClient
from .analyze import filter_exploitation_articles, analyze_exploitation
from .article_policy import (
    exclude_virtual_event_promotions,
)
from .report_validation import (
    format_report_validation_issues,
)
from .finding_evidence import (
    EvidenceError,
    grounding_failure_diagnostic,
)
from .analysis_errors import ANALYSIS_ERROR_CLASSES
from .observability import (
    ci_attributes,
    model_attributes,
    state_attributes,
    traced_stage,
)
from .report_artifact import ReportArtifactError, parse_report_artifact
from .reporting import (
    ReportingGroundingError,
)
from scripts.build_site import (
    ArchiveConflictError,
    SiteBuildError,
    archive_previous_report,
    build_site,
)
from .content_fingerprint import (
    FINGERPRINT_PATH,
    read_stored_fingerprint,
    write_stored_fingerprint,
)

from .source_review import (
    PLAN_KEY,
    SourceReviewError,
    prepare_source_review,
    write_review_packet,
    digest,
)
from .reviewed_report import resolve_reviewed_analysis, ReviewedReportValidationError
from .publication_transaction import (
    PublicationError,
    ensure_no_pending_publication,
    promote_artifacts,
)

logger = logging.getLogger(__name__)
REPO_ROOT = Path(__file__).resolve().parents[2]


class WorkflowFailure(TypedDict):
    """Bounded failure classification; never carries source or report text."""

    stage: str
    codes: list[str]
    field: NotRequired[str | None]


# Define the state type
class ExploitationAnalysisState(TypedDict):
    articles: list
    filtered_articles: list
    analysis_results: Dict[str, Any]
    config: Dict[str, Any]
    status: str
    report_path: NotRequired[str]
    report_validation_errors: NotRequired[list[str]]
    articles_fingerprint: NotRequired[str]
    failure: NotRequired[WorkflowFailure]
    unresolved_version_count: NotRequired[int]
    source_review_plan: NotRequired[dict]
    report_generated: NotRequired[bool]
    source_review_count: NotRequired[int]


def _record_failure(
    state: ExploitationAnalysisState,
    stage: str,
    codes: list[str],
    field: str | None = None,
) -> None:
    state["failure"] = {"stage": stage, "codes": codes, "field": field}


# Load configuration
def load_config(config_path: str = "config/config.json") -> Dict[str, Any]:
    """Load configuration from JSON file"""
    try:
        with open(config_path, "r") as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Failed to load configuration: {e}")
        return {}


# Define the workflow steps
async def fetch_articles(state: ExploitationAnalysisState) -> ExploitationAnalysisState:
    """Fetch articles from SentryDigest."""
    logger.info("Starting article fetching")

    config = state["config"]
    rss_feed_url = config.get("feed_url", "")

    if not rss_feed_url:
        logger.error("RSS feed URL not configured")
        _record_failure(state, "fetch", ["feed_url_missing"])
        state["status"] = "failed"
        return state

    feed_client = SentryDigestFeedClient(rss_feed_url)
    try:
        articles = await feed_client.fetch_articles()
    except Exception as e:
        logger.error(f"Error in RSS feed: {e}")
        _record_failure(state, "fetch", ["feed_fetch_failed"])
        state["status"] = "failed"
        return state

    state["articles"] = exclude_virtual_event_promotions(articles)
    logger.info(f"Fetched {len(state['articles'])} eligible articles")

    return state


async def enrich_articles(
    state: ExploitationAnalysisState,
) -> ExploitationAnalysisState:
    """Enrich articles with full content."""
    logger.info("Enriching articles")

    articles = exclude_virtual_event_promotions(state["articles"])
    feed_client = SentryDigestFeedClient(state["config"].get("feed_url", ""))
    enriched_articles = await feed_client.enrich_article_content(articles)

    state["articles"] = exclude_virtual_event_promotions(enriched_articles)

    return state


def _fingerprint_path_for(output_path: str) -> str:
    """Resolve the fingerprint file alongside the report's output path."""
    return str(Path(output_path).parent / Path(FINGERPRINT_PATH).name)


async def filter_articles(
    state: ExploitationAnalysisState,
) -> ExploitationAnalysisState:
    """Filter articles for exploitation content"""
    logger.info("Starting article filtering")

    articles = exclude_virtual_event_promotions(state["articles"])
    state["articles"] = articles
    filtered = exclude_virtual_event_promotions(filter_exploitation_articles(articles))

    state["filtered_articles"] = filtered

    state["report_generated"] = False
    output_path = state["config"].get("output_path", "index.md")
    root = Path(output_path).parent
    try:
        ensure_no_pending_publication(root)
        if filtered:
            plan = prepare_source_review(filtered)
            write_review_packet(plan.packet, root / ".sentryinsight-review")
            state["source_review_plan"] = plan.packet
            fingerprint = digest(
                {"generation_schema": 5, "plan_id": plan.packet["plan_id"]}
            )
            state["articles_fingerprint"] = fingerprint
            if not plan.eligible_keys:
                state["status"] = "review_required"
            elif fingerprint == read_stored_fingerprint(
                _fingerprint_path_for(output_path)
            ):
                logger.info("Source review plan is unchanged; skipping analysis")
                state["status"] = "completed_unchanged"
    except (SourceReviewError, PublicationError, OSError) as exc:
        code = (
            exc.code
            if isinstance(exc, (SourceReviewError, PublicationError))
            else "review_packet_write_failed"
        )
        _record_failure(state, "source_review", [code])
        state["status"] = "failed"

    return state


async def analyze_articles(
    state: ExploitationAnalysisState,
) -> ExploitationAnalysisState:
    """Analyze articles for exploitation content"""
    logger.info("Starting article analysis")

    filtered_articles = exclude_virtual_event_promotions(state["filtered_articles"])
    state["filtered_articles"] = filtered_articles
    config = state["config"]

    if not filtered_articles:
        logger.warning("No exploitation-related articles found to analyze")
        state["analysis_results"] = {
            "skipped": True,
            "skip_reason": "No eligible exploitation-related articles found.",
            "exploitation_report": "",
            "date": datetime.now(timezone.utc).date().isoformat(),
            "analyzed_article_count": 0,
        }
        state["status"] = "completed_with_warnings"
        return state

    # Analyze the filtered articles
    analysis_results = await analyze_exploitation(filtered_articles, config)
    state["analysis_results"] = analysis_results
    if analysis_results.get("skipped"):
        logger.warning(f"Analysis skipped: {analysis_results['skip_reason']}")
        state["status"] = (
            "review_required"
            if analysis_results.get("skip_reason") == "source_review_required"
            else "completed_with_warnings"
        )
        return state
    if analysis_results.get("error"):
        logger.error(f"Analysis failed: {analysis_results['error']}")
        codes = ["analysis_failed"]
        error_class = analysis_results.get("error_class")
        if isinstance(error_class, str) and error_class in ANALYSIS_ERROR_CLASSES:
            codes.append(error_class)
        _record_failure(state, "analysis", codes)
        state["status"] = "failed"
        return state

    logger.info("Completed article analysis")
    return state


async def generate_report(
    state: ExploitationAnalysisState,
) -> ExploitationAnalysisState:
    """Generate the exploitation report"""
    if state.get("status") in {"failed", "review_required", "completed_unchanged"}:
        return state
    state["report_generated"] = False

    logger.info("Generating exploitation report")

    analysis_results = state["analysis_results"]
    config = state["config"]

    if not analysis_results:
        logger.warning("No analysis results to generate report")
        state["status"] = "completed_with_warnings"
        return state
    if analysis_results.get("skipped"):
        logger.warning(f"Skipping report generation: {analysis_results['skip_reason']}")
        state["status"] = "completed_with_warnings"
        return state

    report = analysis_results.get("exploitation_report", "")
    reporting_catalog = {}
    try:
        # Bind this result to the complete inputs retained by this actual run.
        if PLAN_KEY not in state:
            raise SourceReviewError("source_review_plan_missing")
        plan = prepare_source_review(state["filtered_articles"])
        if (
            state[PLAN_KEY] != plan.packet
            or analysis_results.get(PLAN_KEY) != plan.packet
        ):
            raise SourceReviewError("source_review_plan_mismatch")
        fingerprint = digest(
            {"generation_schema": 5, "plan_id": plan.packet["plan_id"]}
        )
        if state.get("articles_fingerprint") != fingerprint:
            raise SourceReviewError("source_review_fingerprint_mismatch")
        root = Path(config.get("output_path", "index.md")).parent
        ensure_no_pending_publication(root)
        write_review_packet(plan.packet, root / ".sentryinsight-review")
        reporting_catalog = plan.eligible_catalog
        candidate = resolve_reviewed_analysis(analysis_results)
        report_source = candidate.source
        artifact = parse_report_artifact(report_source)
    except (SourceReviewError, PublicationError, OSError) as exc:
        code = (
            exc.code
            if isinstance(exc, (SourceReviewError, PublicationError))
            else "review_packet_write_failed"
        )
        _record_failure(state, "source_review", [code])
        state["report_validation_errors"] = [code]
        state["status"] = "failed"
        return state
    except ReviewedReportValidationError as exc:
        logger.error(
            "Report validation failed:\n%s", format_report_validation_issues(exc.issues)
        )
        state["report_validation_errors"] = [issue.message for issue in exc.issues]
        stage = (
            "report_policy"
            if any(issue.code == "virtual_event_promotion" for issue in exc.issues)
            else "report_validation"
        )
        _record_failure(
            state, stage, list(dict.fromkeys(issue.code for issue in exc.issues))
        )
        state["status"] = "failed"
        return state
    except (ReportingGroundingError, EvidenceError) as exc:
        diagnostic = grounding_failure_diagnostic(report, reporting_catalog, exc)
        logger.error("Report grounding failed: %s", json.dumps(diagnostic))
        state["report_validation_errors"] = [str(exc)]
        _record_failure(
            state, diagnostic["stage"], [diagnostic["code"]], diagnostic["field"]
        )
        state["status"] = "failed"
        return state
    except ReportArtifactError:
        state["report_validation_errors"] = ["report_artifact_invalid"]
        _record_failure(state, "report_artifact", ["report_artifact_invalid"])
        state["status"] = "failed"
        return state

    output_path = config.get("output_path", "index.md")
    output_file = Path(output_path)
    if output_file.name != "index.md":
        logger.error("The canonical report output must be named index.md")
        state["report_validation_errors"] = [
            "The canonical report output must be named index.md"
        ]
        _record_failure(state, "report_output", ["report_output_name_invalid"])
        state["status"] = "failed"
        return state

    # Build the complete next public tree before replacing any current files.
    # Git commits publish the resulting paths together, while this staging step
    # prevents validation or renderer failures from splitting local state.
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            staged_root = Path(temp_dir) / "site"
            staged_reports = staged_root / "reports"
            staged_reports.mkdir(parents=True)

            current_reports = output_file.parent / "reports"
            if current_reports.exists():
                for archived_path in current_reports.glob("????-??-??.md"):
                    shutil.copy2(archived_path, staged_reports / archived_path.name)

            if output_file.exists():
                archive_previous_report(
                    current_source=output_file.read_text(),
                    next_report=artifact,
                    reports_path=staged_reports,
                )

            staged_report = staged_root / "index.md"
            staged_report.write_text(report_source)
            build_site(
                report_path=staged_report,
                output_path=staged_root,
                template_path=REPO_ROOT / "site",
            )

            write_stored_fingerprint(
                fingerprint, str(staged_root / Path(FINGERPRINT_PATH).name)
            )
            promotion_status = promote_artifacts(staged_root, output_file.parent)
            if promotion_status == "publication_cleanup_pending":
                logger.warning(
                    "Publication completed; local recovery cleanup is required before another generation"
                )
    except (ArchiveConflictError, SiteBuildError, PublicationError, OSError) as exc:
        code = _publication_failure_code(exc)
        logger.error("Static report publication failed: %s", code)
        state["report_validation_errors"] = [code]
        _record_failure(state, "site_publication", [code])
        state["status"] = "failed"
        return state

    state["report_generated"] = True
    state["source_review_count"] = sum(
        row["state"] != "eligible" for row in plan.packet["sources"]
    )

    state["report_path"] = output_path
    state["unresolved_version_count"] = artifact.unresolved_version_count
    if artifact.unresolved_version_count:
        logger.info(
            "Report includes %d finding(s) with unresolved affected-version evidence",
            artifact.unresolved_version_count,
        )
    return state


def _publication_failure_code(exc: Exception) -> str:
    if isinstance(exc, PublicationError):
        return exc.code
    if isinstance(exc, ArchiveConflictError):
        return "archive_conflict"
    if isinstance(exc, SiteBuildError):
        return "site_build_failed"
    return "filesystem_error"


async def publish_results(
    state: ExploitationAnalysisState,
) -> ExploitationAnalysisState:
    """Publish results to GitHub Pages or local file"""
    logger.info("Publishing results")

    if state.get("status") in {"failed", "review_required", "completed_unchanged"}:
        logger.info("Skipping publishing for terminal workflow status")
        return state

    analysis_results = state["analysis_results"]

    if not analysis_results:
        logger.warning("No analysis results to publish")
        state["status"] = "completed_with_warnings"
        return state
    if analysis_results.get("skipped"):
        logger.warning(f"Skipping publishing: {analysis_results['skip_reason']}")
        state["status"] = "completed_with_warnings"
        return state

    if not state.get("report_path"):
        logger.warning("No validated static report artifacts were produced")
        state["status"] = "completed_with_warnings"
        return state

    logger.info("Validated static report artifacts are ready for GitHub Pages")
    state["status"] = (
        "completed_with_review" if state.get("source_review_count") else "completed"
    )

    return state


def should_end(state: ExploitationAnalysisState) -> str:
    """Determine if workflow should end."""
    if state.get("status") == "failed":
        return "error"
    elif state.get("status") in {"completed_unchanged", "review_required"}:
        return "unchanged"
    elif not state.get("filtered_articles"):
        return "no_articles"
    else:
        return "continue"


# Define workflow graph
def create_exploitation_analysis_graph() -> Any:
    """Create the exploitation analysis workflow graph"""
    workflow: Any = StateGraph(cast(Any, ExploitationAnalysisState))

    # Add nodes; each stage records one span with bounded state attributes.
    workflow.add_node("fetch_articles", traced_stage("fetch", fetch_articles))
    workflow.add_node("enrich_articles", traced_stage("enrich", enrich_articles))
    workflow.add_node("filter_articles", traced_stage("filter", filter_articles))
    workflow.add_node("analyze_articles", traced_stage("analyze", analyze_articles))
    workflow.add_node("generate_report", traced_stage("generate", generate_report))
    workflow.add_node("publish_results", traced_stage("publish", publish_results))

    # Define edges
    workflow.add_edge(START, "fetch_articles")
    workflow.add_edge("fetch_articles", "enrich_articles")
    workflow.add_edge("enrich_articles", "filter_articles")
    workflow.add_conditional_edges(
        "analyze_articles",
        lambda state: "error" if state.get("status") == "failed" else "continue",
        {"error": END, "continue": "generate_report"},
    )
    workflow.add_edge("generate_report", "publish_results")
    workflow.add_edge("publish_results", END)

    # Add conditional edges
    workflow.add_conditional_edges(
        "filter_articles",
        should_end,
        {
            "error": END,
            "unchanged": END,
            "no_articles": "generate_report",
            "continue": "analyze_articles",
        },
    )

    # Compile the graph
    return workflow.compile()


# Main function to run the workflow
async def run_exploitation_analysis():
    """Run the exploitation analysis workflow"""
    logger.info("Starting exploitation analysis workflow")

    with logfire.span(
        "sentryinsight report run", _span_name="sentryinsight.run"
    ) as span:
        span.set_attributes(ci_attributes())
        # Load configuration
        config = load_config()

        if not config:
            logger.error("Failed to load configuration, exiting")
            span.set_attributes(
                {
                    "workflow.status": "failed",
                    "failure.stage": "config",
                    "failure.codes": ["config_unavailable"],
                }
            )
            return None

        span.set_attributes(model_attributes(config))

        # Initialize state
        initial_state = {
            "articles": [],
            "filtered_articles": [],
            "analysis_results": {},
            "config": config,
            "status": "started",
        }

        # Create the graph
        graph = create_exploitation_analysis_graph()

        # Run the graph
        try:
            final_state = await graph.ainvoke(initial_state)
        except Exception as e:
            logger.error(f"Error during workflow execution: {e}")
            span.set_attributes(
                {"workflow.status": "failed", "error.type": type(e).__qualname__}
            )
            span.set_level("error")
            return None

        span.set_attributes(state_attributes(final_state))
        if final_state.get("status") == "failed":
            logger.error("Workflow failed")
        else:
            logger.info("Workflow completed successfully")
        return final_state


# For direct execution
if __name__ == "__main__":
    asyncio.run(run_exploitation_analysis())

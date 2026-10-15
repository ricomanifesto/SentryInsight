from typing import Dict, Any, NotRequired, TypedDict, cast
from langgraph.graph import START, END, StateGraph
import logfire
import logging
import asyncio
import json
from datetime import datetime, timezone
from pathlib import Path

from ..services.fetch import SentryDigestFeedClient
from .analyze import filter_exploitation_articles, analyze_exploitation
from .article_policy import (
    contains_virtual_event_tag,
    exclude_virtual_event_promotions,
)
from .report_validation import (
    format_report_validation_issues,
    remove_source_attribution_section,
    split_overlong_executive_summary,
    validate_report_content,
)
from .finding_evidence import (
    EvidenceError,
    grounding_failure_diagnostic,
    validate_finding_evidence,
)
from .observability import model_attributes, state_attributes, traced_stage
from .report_artifact import ReportArtifactError, parse_report_artifact
from .reporting import (
    ReportingContentError,
    ReportingGroundingError,
    deserialize_reporting_catalog,
    resolve_reporting_keys,
)
from scripts.build_site import (
    ArchiveConflictError,
    SiteBuildError,
    build_site,
)
from .content_fingerprint import (
    compute_articles_fingerprint,
)
from .publication import (
    PublicationError,
    publish_report_artifacts,
    read_publication_fingerprint,
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
    publication_cleanup_pending: NotRequired[bool]


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


async def filter_articles(
    state: ExploitationAnalysisState,
) -> ExploitationAnalysisState:
    """Filter articles for exploitation content"""
    logger.info("Starting article filtering")

    articles = exclude_virtual_event_promotions(state["articles"])
    state["articles"] = articles
    filtered = exclude_virtual_event_promotions(filter_exploitation_articles(articles))

    state["filtered_articles"] = filtered

    if filtered:
        output_path = state["config"].get("output_path", "index.md")
        try:
            fingerprint = compute_articles_fingerprint(filtered)
        except ReportingContentError:
            logger.error("Generation evidence failed: invalid_retained_source")
            state["analysis_results"] = {
                "error": "invalid_retained_source",
                "exploitation_report": "",
                "reporting_sources": [],
                "date": datetime.now(timezone.utc).date().isoformat(),
                "analyzed_article_count": len(filtered),
            }
            state["status"] = "failed"
            return state
        try:
            previous_fingerprint = read_publication_fingerprint(
                Path(output_path).parent
            )
        except OSError as exc:
            logger.error("Publication recovery before analysis failed: %s", exc)
            _record_failure(state, "site_publication", [_publication_failure_code(exc)])
            state["status"] = "failed"
            return state
        state["articles_fingerprint"] = fingerprint
        if fingerprint == previous_fingerprint:
            logger.info(
                "Source article set is unchanged since the last report — "
                "skipping analysis to avoid redundant API usage"
            )
            state["status"] = "completed_unchanged"

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
        state["status"] = "completed_with_warnings"
        return state
    if analysis_results.get("error"):
        logger.error(f"Analysis failed: {analysis_results['error']}")
        _record_failure(state, "analysis", ["analysis_failed"])
        state["status"] = "failed"
        return state

    logger.info("Completed article analysis")
    return state


async def generate_report(
    state: ExploitationAnalysisState,
) -> ExploitationAnalysisState:
    """Generate the exploitation report"""
    if state.get("status") == "failed":
        return state

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

    # Extract the exploitation report
    exploitation_report = analysis_results.get(
        "exploitation_report", "# No Exploitation Report Generated"
    )
    # Normalization must not erase a promotion's only tag and publish its body.
    if contains_virtual_event_tag(exploitation_report):
        state["report_validation_errors"] = [
            "Report contains a blocked [Virtual Event] promotion."
        ]
        _record_failure(state, "report_policy", ["virtual_event_promotion"])
        state["status"] = "failed"
        return state

    # Since the exploitation_report already contains the full formatted report,
    # we should use it directly instead of the template
    report = remove_source_attribution_section(exploitation_report)
    normalized_report = split_overlong_executive_summary(report)
    if normalized_report != report:
        logger.info(
            "Split an overlong Executive Summary at a sentence boundary before validation"
        )
    report = normalized_report
    reporting_catalog = {}
    try:
        reporting_catalog = deserialize_reporting_catalog(
            analysis_results.get("reporting_sources", [])
        )
        validate_finding_evidence(report, reporting_catalog)
        report = resolve_reporting_keys(report, reporting_catalog)
    except (ReportingGroundingError, EvidenceError) as exc:
        diagnostic = grounding_failure_diagnostic(report, reporting_catalog, exc)
        logger.error("Report grounding failed: %s", json.dumps(diagnostic))
        state["report_validation_errors"] = [str(exc)]
        _record_failure(
            state, diagnostic["stage"], [diagnostic["code"]], diagnostic["field"]
        )
        state["status"] = "failed"
        return state
    validation_issues = validate_report_content(
        report,
        expected_cves=analysis_results.get("cves_identified"),
    )
    if validation_issues:
        logger.error(
            "Report validation failed:\n%s",
            format_report_validation_issues(validation_issues),
        )
        state["report_validation_errors"] = [
            issue.message for issue in validation_issues
        ]
        _record_failure(
            state,
            "report_validation",
            list(dict.fromkeys(issue.code for issue in validation_issues)),
        )
        state["status"] = "failed"
        return state

    report_date = str(
        analysis_results.get("date") or datetime.now(timezone.utc).date().isoformat()
    )
    generated_at = str(
        analysis_results.get("generated_at")
        or datetime.now(timezone.utc)
        .isoformat(timespec="seconds")
        .replace("+00:00", "Z")
    )
    report_source = (
        "---\n"
        "schema_version: 3\n"
        f"report_date: {report_date}\n"
        f"generated_at: {generated_at}\n"
        "digest_issue_url: https://ricomanifesto.github.io/"
        f"SentryDigest/archive/{report_date}/\n"
        "---\n"
        f"{report.lstrip()}"
    )
    try:
        artifact = parse_report_artifact(report_source)
    except ReportArtifactError as exc:
        logger.error("Report artifact validation failed: %s", exc)
        state["report_validation_errors"] = [str(exc)]
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

    try:
        cleanup_pending = publish_report_artifacts(
            artifact,
            report_source,
            output_file.parent,
            state.get("articles_fingerprint"),
            REPO_ROOT / "site",
            builder=build_site,
        )
    except (ArchiveConflictError, SiteBuildError, OSError) as exc:
        logger.error("Static report publication failed: %s", exc)
        state["report_validation_errors"] = [str(exc)]
        _record_failure(state, "site_publication", [_publication_failure_code(exc)])
        state["status"] = "failed"
        return state

    if cleanup_pending:
        state["publication_cleanup_pending"] = True
    state["report_path"] = output_path
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

    if state.get("status") == "failed":
        logger.warning("Skipping publishing because workflow status is failed")
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
    state["status"] = "completed"

    return state


def should_end(state: ExploitationAnalysisState) -> str:
    """Determine if workflow should end."""
    if state.get("status") == "failed":
        return "error"
    elif state.get("status") == "completed_unchanged":
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

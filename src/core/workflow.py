from typing import Dict, Any, NotRequired, TypedDict, cast
from langgraph.graph import START, END, StateGraph
import logging
import asyncio
import json
import shutil
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from ..services.fetch import SentryDigestFeedClient
from .analyze import filter_exploitation_articles, analyze_exploitation
from .report_validation import (
    format_report_validation_issues,
    remove_source_attribution_section,
    validate_report_content,
)
from .report_artifact import ReportArtifactError, parse_report_artifact
from scripts.build_site import (
    ArchiveConflictError,
    SiteBuildError,
    archive_previous_report,
    build_site,
)
from .content_fingerprint import (
    FINGERPRINT_PATH,
    compute_articles_fingerprint,
    read_stored_fingerprint,
    write_stored_fingerprint,
)

logger = logging.getLogger(__name__)
REPO_ROOT = Path(__file__).resolve().parents[2]


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
        state["status"] = "failed"
        return state

    feed_client = SentryDigestFeedClient(rss_feed_url)
    try:
        articles = await feed_client.fetch_articles()
    except Exception as e:
        logger.error(f"Error in RSS feed: {e}")
        state["status"] = "failed"
        return state

    state["articles"] = articles
    logger.info(f"Fetched {len(articles)} articles")

    return state


async def enrich_articles(
    state: ExploitationAnalysisState,
) -> ExploitationAnalysisState:
    """Enrich articles with full content."""
    logger.info("Enriching articles")

    articles = state["articles"]
    feed_client = SentryDigestFeedClient(state["config"].get("feed_url", ""))
    enriched_articles = await feed_client.enrich_article_content(articles)

    state["articles"] = enriched_articles

    return state


def _fingerprint_path_for(output_path: str) -> str:
    """Resolve the fingerprint file alongside the report's output path."""
    return str(Path(output_path).parent / Path(FINGERPRINT_PATH).name)


async def filter_articles(
    state: ExploitationAnalysisState,
) -> ExploitationAnalysisState:
    """Filter articles for exploitation content"""
    logger.info("Starting article filtering")

    articles = state["articles"]
    filtered = filter_exploitation_articles(articles)

    state["filtered_articles"] = filtered

    if filtered:
        output_path = state["config"].get("output_path", "index.md")
        fingerprint = compute_articles_fingerprint(filtered)
        previous_fingerprint = read_stored_fingerprint(
            _fingerprint_path_for(output_path)
        )
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

    filtered_articles = state["filtered_articles"]
    config = state["config"]

    if not filtered_articles:
        logger.warning("No exploitation-related articles found to analyze")
        state["analysis_results"] = {
            "exploitation_report": "# No Exploitation Content Found\n\nNo articles with exploitation-related content were found in the current dataset.",
            "date": datetime.now(timezone.utc).date().isoformat(),
            "analyzed_article_count": 0,
        }
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
        state["status"] = "failed"

    logger.info("Completed article analysis")
    return state


async def generate_report(
    state: ExploitationAnalysisState,
) -> ExploitationAnalysisState:
    """Generate the exploitation report"""
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

    # Since the exploitation_report already contains the full formatted report,
    # we should use it directly instead of the template
    report = remove_source_attribution_section(exploitation_report)
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
        "schema_version: 1\n"
        f"report_date: {report_date}\n"
        f"generated_at: {generated_at}\n"
        "---\n"
        f"{report.lstrip()}"
    )
    try:
        artifact = parse_report_artifact(report_source)
    except ReportArtifactError as exc:
        logger.error("Report artifact validation failed: %s", exc)
        state["report_validation_errors"] = [str(exc)]
        state["status"] = "failed"
        return state

    output_path = config.get("output_path", "index.md")
    output_file = Path(output_path)
    if output_file.name != "index.md":
        logger.error("The canonical report output must be named index.md")
        state["report_validation_errors"] = [
            "The canonical report output must be named index.md"
        ]
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

            staged_files = sorted(
                (path for path in staged_root.rglob("*") if path.is_file()),
                key=lambda path: (
                    path.relative_to(staged_root) == Path("index.html"),
                    path.as_posix(),
                ),
            )
            for staged_path in staged_files:
                relative_path = staged_path.relative_to(staged_root)
                destination = output_file.parent / relative_path
                destination.parent.mkdir(parents=True, exist_ok=True)
                temporary_destination = destination.with_name(
                    f".{destination.name}.sentryinsight.tmp"
                )
                try:
                    shutil.copy2(staged_path, temporary_destination)
                    temporary_destination.replace(destination)
                finally:
                    temporary_destination.unlink(missing_ok=True)
    except (ArchiveConflictError, SiteBuildError, OSError) as exc:
        logger.error("Static report publication failed: %s", exc)
        state["report_validation_errors"] = [str(exc)]
        state["status"] = "failed"
        return state

    if state.get("articles_fingerprint"):
        write_stored_fingerprint(
            state["articles_fingerprint"], _fingerprint_path_for(output_path)
        )

    state["report_path"] = output_path
    return state


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

    # Add nodes
    workflow.add_node("fetch_articles", fetch_articles)
    workflow.add_node("enrich_articles", enrich_articles)
    workflow.add_node("filter_articles", filter_articles)
    workflow.add_node("analyze_articles", analyze_articles)
    workflow.add_node("generate_report", generate_report)
    workflow.add_node("publish_results", publish_results)

    # Define edges
    workflow.add_edge(START, "fetch_articles")
    workflow.add_edge("fetch_articles", "enrich_articles")
    workflow.add_edge("enrich_articles", "filter_articles")
    workflow.add_edge("analyze_articles", "generate_report")
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

    # Load configuration
    config = load_config()

    if not config:
        logger.error("Failed to load configuration, exiting")
        return None

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
        logger.info("Workflow completed successfully")
        return final_state
    except Exception as e:
        logger.error(f"Error during workflow execution: {e}")
        return None


# For direct execution
if __name__ == "__main__":
    asyncio.run(run_exploitation_analysis())

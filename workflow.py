from typing import Dict, Any, TypedDict, List, Callable, Awaitable
from langgraph.graph import START, END, StateGraph
import yaml
import logging
import asyncio
import os
from datetime import datetime
from pathlib import Path

from fetch import SentryDigestFetcher
from analyze import filter_exploitation_articles, analyze_exploitation
from publish import publish_to_github_pages

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Define the state type
class ExploitationAnalysisState(TypedDict):
    articles: list
    filtered_articles: list
    analysis_results: Dict[str, Any]
    config: Dict[str, Any]
    status: str

# Load configuration
def load_config(config_path: str = "config.yaml") -> Dict[str, Any]:
    """Load configuration from YAML file"""
    try:
        with open(config_path, "r") as f:
            return yaml.safe_load(f)
    except Exception as e:
        logger.error(f"Failed to load configuration: {e}")
        return {}

# Define the workflow steps
async def fetch_articles(state: ExploitationAnalysisState) -> ExploitationAnalysisState:
    """Fetch articles from SentryDigest"""
    logger.info("Starting article fetching")
    
    config = state["config"]
    rss_feed_url = config.get("sentrydigest_url", "")
    
    if not rss_feed_url:
        logger.error("RSS feed URL not configured")
        state["status"] = "failed"
        return state
    
    fetcher = SentryDigestFetcher(rss_feed_url)
    articles = await fetcher.fetch_articles()
    
    # Enrich articles with content if available
    articles = await fetcher.enrich_article_content(articles)
    
    state["articles"] = articles
    logger.info(f"Fetched and enriched {len(articles)} articles")
    
    return state

async def filter_articles(state: ExploitationAnalysisState) -> ExploitationAnalysisState:
    """Filter articles for exploitation content"""
    logger.info("Starting article filtering")
    
    articles = state["articles"]
    filtered = filter_exploitation_articles(articles)
    
    state["filtered_articles"] = filtered
    
    return state

async def analyze_articles(state: ExploitationAnalysisState) -> ExploitationAnalysisState:
    """Analyze articles for exploitation content"""
    logger.info("Starting article analysis")
    
    filtered_articles = state["filtered_articles"]
    config = state["config"]
    
    if not filtered_articles:
        logger.warning("No exploitation-related articles found to analyze")
        state["analysis_results"] = {
            "exploitation_report": "# No Exploitation Content Found\n\nNo articles with exploitation-related content were found in the current dataset.",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "analyzed_article_count": 0
        }
        return state
    
    # Analyze the filtered articles
    analysis_results = await analyze_exploitation(filtered_articles, config)
    state["analysis_results"] = analysis_results
    
    logger.info("Completed article analysis")
    return state

async def publish_results(state: ExploitationAnalysisState) -> ExploitationAnalysisState:
    """Publish results to GitHub Pages"""
    logger.info("Starting results publishing")
    
    analysis_results = state["analysis_results"]
    config = state["config"]
    
    if not analysis_results:
        logger.warning("No analysis results to publish")
        state["status"] = "completed_with_warnings"
        return state
    
    # Get GitHub Pages config
    github_pages_config = config.get("github_pages", {})
    
    # Publish to GitHub Pages if enabled
    if github_pages_config.get("enabled", False):
        success = await publish_to_github_pages(analysis_results, github_pages_config)
        
        if success:
            logger.info("Successfully published to GitHub Pages")
            state["status"] = "completed"
        else:
            logger.warning("Failed to publish to GitHub Pages")
            state["status"] = "completed_with_warnings"
    else:
        logger.info("GitHub Pages publishing is disabled")
        
        # Create output directory if it doesn't exist
        output_path = config.get("output_path", "./analysis")
        os.makedirs(output_path, exist_ok=True)
        
        # Write report to file
        report_path = os.path.join(output_path, f"exploitation-report-{analysis_results.get('date', datetime.now().strftime('%Y-%m-%d'))}.md")
        with open(report_path, "w") as f:
            f.write(analysis_results.get("exploitation_report", "# No Report Generated"))
            
        logger.info(f"Analysis report saved to {report_path}")
        state["status"] = "completed"
    
    return state

# Define workflow graph
def create_exploitation_analysis_graph() -> StateGraph:
    """Create the exploitation analysis workflow graph"""
    workflow = StateGraph(ExploitationAnalysisState)
    
    # Add nodes
    workflow.add_node("fetch_articles", fetch_articles)
    workflow.add_node("filter_articles", filter_articles)
    workflow.add_node("analyze_articles", analyze_articles)
    workflow.add_node("publish_results", publish_results)
    
    # Define edges
    workflow.add_edge(START, "fetch_articles")
    workflow.add_edge("fetch_articles", "filter_articles")
    workflow.add_edge("filter_articles", "analyze_articles")
    workflow.add_edge("analyze_articles", "publish_results")
    workflow.add_edge("publish_results", END)
    
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
        "status": "started"
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

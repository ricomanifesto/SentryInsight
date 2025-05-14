from typing import Dict, Any, TypedDict
from langgraph.graph import START, END, StateGraph
import yaml
import logging
import asyncio
import os
from datetime import datetime

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
        logger.error(f"Error loading configuration: {e}")
        return {}

# Node functions
async def fetch_articles(state: ExploitationAnalysisState) -> ExploitationAnalysisState:
    """Fetch articles from SentryDigest"""
    logger.info("Starting article fetching")
    
    config = state["config"]
    rss_url = config.get("sentrydigest_url", "")
    
    # Initialize fetcher
    fetcher = SentryDigestFetcher(rss_url)
    
    # Fetch articles
    articles = await fetcher.fetch_articles()
    
    # Enrich articles with content
    enriched_articles = await fetcher.enrich_article_content(articles)
    
    logger.info(f"Fetched and enriched {len(enriched_articles)} articles")
    
    return {
        **state,
        "articles": enriched_articles,
        "status": "articles_fetched"
    }

async def filter_articles(state: ExploitationAnalysisState) -> ExploitationAnalysisState:
    """Filter articles for exploitation content"""
    logger.info("Starting article filtering")
    
    articles = state["articles"]
    
    # Filter articles
    filtered_articles = await filter_exploitation_articles(articles)
    
    logger.info(f"Filtered {len(articles)} articles to {len(filtered_articles)} exploitation-related articles")
    
    return {
        **state,
        "filtered_articles": filtered_articles,
        "status": "articles_filtered"
    }

async def analyze_articles(state: ExploitationAnalysisState) -> ExploitationAnalysisState:
    """Analyze exploitation articles"""
    logger.info("Starting exploitation analysis")
    
    filtered_articles = state["filtered_articles"]
    config = state["config"]
    model_config = config.get("model", {})
    
    # Analyze articles
    analysis_results = await analyze_exploitation(filtered_articles, model_config)
    
    logger.info("Completed exploitation analysis")
    
    return {
        **state,
        "analysis_results": analysis_results,
        "status": "analysis_complete"
    }

async def publish_results(state: ExploitationAnalysisState) -> ExploitationAnalysisState:
    """Publish analysis results"""
    logger.info("Starting results publishing")
    
    analysis_results = state["analysis_results"]
    config = state["config"]
    github_pages_config = config.get("github_pages", {})
    
    # Publish results
    success = await publish_to_github_pages(analysis_results, github_pages_config)
    
    logger.info(f"Publishing {'succeeded' if success else 'failed'}")
    
    return {
        **state,
        "status": "published" if success else "publish_failed"
    }

# Create the graph
def create_exploitation_analysis_graph():
    """Create the workflow graph for exploitation analysis"""
    builder = StateGraph(ExploitationAnalysisState)
    
    # Add nodes
    builder.add_node("fetch_articles", fetch_articles)
    builder.add_node("filter_articles", filter_articles)
    builder.add_node("analyze_articles", analyze_articles)
    builder.add_node("publish_results", publish_results)
    
    # Add edges
    builder.add_edge(START, "fetch_articles")
    builder.add_edge("fetch_articles", "filter_articles")
    builder.add_edge("filter_articles", "analyze_articles")
    builder.add_edge("analyze_articles", "publish_results")
    builder.add_edge("publish_results", END)
    
    # Compile the graph
    return builder.compile()

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
        async for event in graph.astream_events(initial_state):
            state = event.data
            current_node = state.get("current_node", "")
            if current_node:
                logger.info(f"Completed node: {current_node}")
    except Exception as e:
        logger.error(f"Error during workflow execution: {e}")
        return None
    
    logger.info("Exploitation analysis workflow completed successfully")
    return state

# For direct execution
if __name__ == "__main__":
    asyncio.run(run_exploitation_analysis())

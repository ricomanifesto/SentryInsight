"""MCP RSS feed parser for SentryDigest."""

import asyncio
import logging
from typing import Dict, Any, List, Optional

from mcp.server.fastmcp import FastMCP
from ..core.tools import RSSTools

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize FastMCP server for RSS operations only
rss_mcp = FastMCP("sentrydigest-rss")

# Initialize tools
rss_tools = RSSTools()

@rss_mcp.tool()
async def fetch_rss_feed(feed_url: str) -> Dict[str, Any]:
    """Fetch an RSS feed and return the parsed content.
    
    Args:
        feed_url: URL of the RSS feed to fetch
    """
    logger.info(f"Fetching RSS feed from {feed_url}")
    try:
        feed_data = await rss_tools.fetch_rss_feed(feed_url)
        return feed_data
    except Exception as e:
        logger.error(f"Error fetching RSS feed: {e}")
        return {"error": str(e), "entries": []}

@rss_mcp.tool()
async def enrich_rss_articles(articles: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Enrich RSS articles with full content.
    
    Args:
        articles: List of article dictionaries to enrich
    """
    logger.info(f"Enriching {len(articles)} articles concurrently")
    try:
        enrichment_tasks = [rss_tools.enrich_article_content(article) for article in articles]
        enriched_articles = await asyncio.gather(*enrichment_tasks, return_exceptions=True)
        
        result_articles = []
        for i, result in enumerate(enriched_articles):
            if isinstance(result, Exception):
                logger.error(f"Error enriching article {i}: {result}")
                result_articles.append(articles[i])
            else:
                result_articles.append(result)
        
        return result_articles
    except Exception as e:
        logger.error(f"Error enriching articles: {e}")
        return articles  # Return original articles if enrichment fails

# Export the MCP application
mcp_app = rss_mcp  
"""RSS Feed parsing tools for MCP architecture."""

import logging
import feedparser
import httpx
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class RSSTools:
    """Tools for working with RSS feeds in MCP architecture."""
    
    def __init__(self):
        """Initialize the RSS tools."""
        self.client = httpx.AsyncClient(follow_redirects=True, timeout=30.0)
    
    async def fetch_rss_feed(self, feed_url: str) -> Dict[str, Any]:
        """
        Fetch and parse an RSS feed.
        
        Args:
            feed_url: The URL of the RSS feed
            
        Returns:
            Parsed feed data
        """
        try:
            logger.info(f"Fetching RSS feed from {feed_url}")
            response = await self.client.get(feed_url)
            response.raise_for_status()
            
            # Parse the feed
            feed = feedparser.parse(response.text)
            
            return {
                "title": feed.feed.get("title", "Unknown Feed"),
                "description": feed.feed.get("description", ""),
                "link": feed.feed.get("link", ""),
                "last_updated": feed.feed.get("updated", ""),
                "entry_count": len(feed.entries),
                "entries": feed.entries
            }
        except Exception as e:
            logger.error(f"Error fetching RSS feed: {e}")
            return {
                "error": str(e),
                "entries": []
            }
    
    async def enrich_article_content(self, article: Dict[str, Any]) -> Dict[str, Any]:
        """
        Fetch and add full content for an article.
        
        Args:
            article: Article dictionary with at least a link
            
        Returns:
            Enriched article with full content
        """
        try:
            logger.info(f"Enriching article: {article.get('title', '')}")
            
            # Skip if the article already has content
            if "content" in article and article["content"]:
                return article
            
            # Combine title and summary for basic content
            full_content = article.get("title", "") + "\n"
            
            # Add summary if available
            if "summary" in article and article["summary"]:
                full_content += article["summary"] + "\n"
            
            # Fetch full content if link exists
            if "link" in article and article["link"]:
                timeout = httpx.Timeout(10.0, connect=5.0)
                async with httpx.AsyncClient(timeout=timeout, follow_redirects=True) as client:
                    response = await client.get(article["link"])
                    
                    if response.status_code == 200:
                        # Add full article content
                        full_content += "\n\n" + response.text
            
            # Update article with content
            article["content"] = full_content
            return article
            
        except Exception as e:
            logger.error(f"Error enriching article: {e}")
            article["content"] = article.get("title", "") + "\n" + article.get("summary", "")
            article["error"] = str(e)
            return article
            
    def extract_basic_fields(self, entry: Dict[str, Any]) -> Dict[str, Any]:
        """
        Extract core fields from a feedparser entry.
        
        Args:
            entry: A feedparser entry
            
        Returns:
            Dictionary with extracted fields
        """
        return {
            "title": entry.get("title", ""),
            "link": entry.get("link", ""),
            "summary": entry.get("description", ""),
            "published": entry.get("published", ""),
            "source": entry.get("dc_source", entry.get("source", {}).get("title", "Unknown Source")),
            "date": entry.get("dc_date", entry.get("published_parsed", "")),
            "content": entry.get("content", [{}])[0].get("value", "") if entry.get("content") else "",
        } 
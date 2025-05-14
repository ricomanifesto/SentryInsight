import logging
import asyncio
import re
import html
from typing import List, Dict, Any
import httpx
import feedparser
from datetime import datetime
from urllib.parse import urlparse

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SentryDigestFetcher:
    """
    Class for fetching articles from SentryDigest RSS feed
    """
    
    def __init__(self, feed_url: str):
        """
        Initialize the fetcher with the feed URL
        
        Args:
            feed_url: URL of the SentryDigest RSS feed
        """
        self.feed_url = feed_url
        self.client = httpx.AsyncClient(follow_redirects=True, timeout=30.0)
    
    async def fetch_articles(self) -> List[Dict[str, Any]]:
        """
        Fetch articles from SentryDigest RSS feed
        
        Returns:
            List of articles with basic metadata
        """
        logger.info(f"Fetching articles from {self.feed_url}")
        
        try:
            # Fetch the feed
            response = await self.client.get(self.feed_url)
            response.raise_for_status()
            
            # Use feedparser to parse the feed
            feed = feedparser.parse(response.text)
            
            # Extract articles
            articles = []
            for entry in feed.entries:
                # Basic article info
                article = {
                    "title": entry.title,
                    "link": entry.link,
                    "summary": entry.description,
                    "published": entry.get("published", ""),
                    "source": entry.get("dc_source", "Unknown Source"),
                    "date": entry.get("dc_date", datetime.now().strftime("%Y-%m-%d")),
                    "content": entry.get("content", ""),
                }
                articles.append(article)
            
            logger.info(f"Extracted {len(articles)} articles from feed")
            return articles
            
        except Exception as e:
            logger.error(f"Error fetching articles: {e}")
            raise
    
    async def enrich_article_content(self, articles: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Enrich articles with full content
        
        Args:
            articles: List of article dictionaries
            
        Returns:
            Enriched list of articles with full content
        """
        logger.info(f"Enriching {len(articles)} articles with content")
        
        # List to store enriched articles
        enriched_articles = []
        
        # Process each article
        for article in articles:
            logger.info(f"Enriching article: {article.get('title', '')}")
            
            # Skip if the article already has content
            if "content" in article and article["content"]:
                enriched_articles.append(article)
                continue
            
            # Combine title and summary for basic content
            full_content = article.get("title", "") + "\n"
            
            # Add summary if available
            if "summary" in article and article["summary"]:
                full_content += article["summary"] + "\n"
            
            # Use async fetch for full article content
            try:
                timeout = httpx.Timeout(10.0, connect=5.0)
                async with httpx.AsyncClient(timeout=timeout, follow_redirects=True) as client:
                    logger.info(f"Fetching full content for: {article.get('link', '')}")
                    response = await client.get(article.get("link", ""))
                    
                    if response.status_code == 200:
                        # Add full article content
                        article["content"] = full_content + "\n\n" + response.text
                    else:
                        # Use what we have if we can't fetch the full article
                        logger.warning(f"Could not fetch full content: {response.status_code}")
                        article["content"] = full_content
            except Exception as e:
                logger.warning(f"Error fetching full content: {e}")
                # Fall back to summary if error occurs
                article["content"] = full_content
            
            enriched_articles.append(article)
        
        logger.info(f"Enriched {len(enriched_articles)} articles with content")
        return enriched_articles

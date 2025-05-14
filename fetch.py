import httpx
import feedparser
import logging
from typing import List, Dict, Any
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SentryDigestFetcher:
    """
    RSS feed fetcher for SentryDigest, focused on exploitation content
    """
    
    def __init__(self, rss_feed_url: str):
        """Initialize with the URL of the SentryDigest RSS feed"""
        self.rss_feed_url = rss_feed_url
        logger.info(f"Initialized SentryDigestFetcher with RSS feed URL: {rss_feed_url}")
        
    async def fetch_articles(self) -> List[Dict[str, Any]]:
        """
        Extract articles from the SentryDigest RSS feed
        
        Returns:
            List of article dictionaries with title, link, source, published date, and description
        """
        logger.info(f"Fetching articles from RSS feed: {self.rss_feed_url}")
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(self.rss_feed_url, timeout=30.0)
                response.raise_for_status()
                feed_content = response.text
                
                # Parse the RSS feed
                feed = feedparser.parse(feed_content)
                
                if not feed.entries:
                    logger.warning("No entries found in the RSS feed")
                    return []
                
                # Convert feedparser entries to our format
                articles = []
                for entry in feed.entries:
                    article = {
                        "title": entry.get("title", ""),
                        "link": entry.get("link", ""),
                        "published": entry.get("published", ""),
                        "summary": entry.get("summary", ""),
                        "content": entry.get("content", [{}])[0].get("value", "") if "content" in entry else "",
                        "source": "SentryDigest"
                    }
                    articles.append(article)
                
                logger.info(f"Successfully fetched {len(articles)} articles")
                return articles
                
        except Exception as e:
            logger.error(f"Error fetching articles: {e}")
            return []
    
    async def enrich_article_content(self, articles: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Enriches articles with full content if available by fetching the article URLs
        
        Args:
            articles: List of article dictionaries
            
        Returns:
            Enriched article dictionaries
        """
        logger.info(f"Enriching content for {len(articles)} articles")
        
        enriched_articles = []
        async with httpx.AsyncClient() as client:
            for article in articles:
                try:
                    # Only fetch if we don't already have content
                    if not article.get("content") and article.get("link"):
                        logger.info(f"Fetching content for: {article['title']}")
                        response = await client.get(article["link"], timeout=30.0)
                        if response.status_code == 200:
                            # Just use the HTML as the content for now - we'll let the AI extract what it needs
                            article["content"] = response.text
                            logger.info(f"Successfully enriched content for: {article['title']}")
                except Exception as e:
                    logger.warning(f"Failed to enrich article {article.get('title', 'Unknown')}: {e}")
                
                enriched_articles.append(article)
                
        return enriched_articles

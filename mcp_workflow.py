"""MCP (Model Context Protocol) workflow for cybersecurity exploitation analysis."""

import os
import logging
import json
from typing import Dict, Any, List, Optional

# Import the MCP server framework
from mcp.server.fastmcp import FastMCP

# Import existing tools - still useful
from tools import RSSTools
from fetch import SentryDigestFetcher
from entities import extract_cve_ids, extract_cvss_scores

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize FastMCP server
mcp = FastMCP("sentry-digest-mcp")

# Initialize tools
rss_tools = RSSTools()

def load_config() -> Dict[str, Any]:
    """Load configuration from JSON file."""
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    try:
        with open(config_path, "r") as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Error loading config: {e}")
        return {}

@mcp.tool()
async def fetch_sentrydigest_feed(feed_url: Optional[str] = None) -> str:
    """Fetch the SentryDigest RSS feed.
    
    Args:
        feed_url: Optional URL override for the RSS feed
    """
    config = load_config()
    if not feed_url:
        feed_url = config.get("feed_url", "https://ricomanifesto.github.io/SentryDigest/feed.xml")
    
    logger.info(f"Fetching SentryDigest feed from {feed_url}")
    try:
        feed_data = await rss_tools.fetch_rss_feed(feed_url)
        article_count = len(feed_data.get("entries", []))
        
        # Return a summary of what was fetched
        return f"Successfully fetched {article_count} articles from SentryDigest feed at {feed_url}"
    except Exception as e:
        error_msg = f"Error fetching feed: {str(e)}"
        logger.error(error_msg)
        return error_msg

@mcp.tool()
async def get_latest_articles(feed_url: Optional[str] = None, count: int = 10) -> str:
    """Get the latest articles from SentryDigest feed.
    
    Args:
        feed_url: Optional URL override for the RSS feed
        count: Number of articles to return
    """
    config = load_config()
    if not feed_url:
        feed_url = config.get("feed_url", "https://ricomanifesto.github.io/SentryDigest/feed.xml")
    
    logger.info(f"Getting latest {count} articles from {feed_url}")
    try:
        # Fetch the feed
        feed_data = await rss_tools.fetch_rss_feed(feed_url)
        
        # Extract articles
        articles = []
        for entry in feed_data.get("entries", []):
            article = rss_tools.extract_basic_fields(entry)
            articles.append(article)
        
        # Limit to requested count
        articles = articles[:min(count, len(articles))]
        
        if not articles:
            return "No articles found in the feed."
        
        # Format the articles
        formatted_articles = []
        for article in articles:
            formatted = f"TITLE: {article.get('title', '')}\n"
            formatted += f"SOURCE: {article.get('source', '')}\n"
            formatted += f"DATE: {article.get('date', '')}\n"
            formatted += f"LINK: {article.get('link', '')}\n"
            formatted += f"SUMMARY: {article.get('summary', '')}\n"
            formatted_articles.append(formatted)
        
        return "\n---\n".join(formatted_articles)
    except Exception as e:
        error_msg = f"Error fetching articles: {str(e)}"
        logger.error(error_msg)
        return error_msg

@mcp.tool()
async def enrich_article(article_url: str) -> str:
    """Fetch the full content of an article.
    
    Args:
        article_url: URL of the article to enrich
    """
    logger.info(f"Enriching article at {article_url}")
    try:
        # Create a basic article dict with the URL
        article = {"link": article_url}
        
        # Use the existing tool to enrich the article
        enriched = await rss_tools.enrich_article_content(article)
        
        # Return the enriched content
        if "content" in enriched and enriched["content"]:
            return f"Article content from {article_url}:\n\n{enriched['content']}"
        else:
            return f"Could not fetch content for {article_url}"
    except Exception as e:
        error_msg = f"Error enriching article: {str(e)}"
        logger.error(error_msg)
        return error_msg

@mcp.tool()
async def detect_exploitation_content(text: str) -> str:
    """Analyze text for exploitation-related content.
    
    Args:
        text: Text content to analyze
    """
    logger.info("Analyzing text for exploitation content")
    try:
        # Extract CVEs - using existing tools
        cves = extract_cve_ids(text)
        
        # Extract CVSS scores
        cvss_scores = extract_cvss_scores(text)
        
        # Look for exploitation keywords
        exploitation_keywords = [
            "exploit", "vulnerability", "zero-day", "0day", "patch", "RCE",
            "arbitrary code", "authentication bypass", "privilege escalation"
        ]
        
        found_keywords = []
        for keyword in exploitation_keywords:
            if keyword.lower() in text.lower():
                found_keywords.append(keyword)
        
        # Format the results
        result = "Exploitation Content Analysis:\n\n"
        
        if cves:
            result += f"CVEs detected: {', '.join(cves)}\n\n"
        else:
            result += "No CVEs detected.\n\n"
        
        if cvss_scores:
            result += "CVSS Scores:\n"
            for score in cvss_scores:
                result += f"- Score: {score.get('score')}, Severity: {score.get('severity')}\n"
            result += "\n"
        
        if found_keywords:
            result += f"Exploitation keywords detected: {', '.join(found_keywords)}\n\n"
            result += "This content likely contains exploitation-related information."
        else:
            result += "No exploitation keywords detected. This content may not be related to security exploitations."
        
        return result
    except Exception as e:
        error_msg = f"Error analyzing text: {str(e)}"
        logger.error(error_msg)
        return error_msg

@mcp.tool()
async def generate_exploitation_report(articles_json: str) -> str:
    """Generate an exploitation report from articles.
    
    Args:
        articles_json: JSON string containing articles to analyze
    """
    logger.info("Generating exploitation report")
    try:
        # Parse the JSON input
        articles = json.loads(articles_json)
        
        # Load the report template
        template_path = os.path.join(os.path.dirname(__file__), "templates", "exploitation_report.md")
        with open(template_path, "r") as f:
            template = f.read()
        
        # Initialize the AI model
        from analyze import analyze_exploitation
        config = load_config()
        
        # Generate the analysis result
        analysis_result = await analyze_exploitation(articles, config)
        
        # Extract the exploitation report
        exploitation_report = analysis_result.get("exploitation_report", "No exploitation report generated.")
        
        # Parse the report into sections
        sections = {
            "exploitation_summary": exploitation_report,
            "exploitation_details": "",
            "affected_systems": "",
            "attack_vectors": "",
            "threat_actors": ""
        }
        
        # Look for section headers in the report
        if "# Executive Summary" in exploitation_report:
            parts = exploitation_report.split("# Executive Summary", 1)
            sections["exploitation_summary"] = parts[1].split("#", 1)[0].strip()
        
        if "# Exploitation Details" in exploitation_report or "# Active Exploitation" in exploitation_report:
            marker = "# Exploitation Details" if "# Exploitation Details" in exploitation_report else "# Active Exploitation"
            parts = exploitation_report.split(marker, 1)
            sections["exploitation_details"] = parts[1].split("#", 1)[0].strip() if len(parts) > 1 else ""
        
        if "# Affected Systems" in exploitation_report:
            parts = exploitation_report.split("# Affected Systems", 1)
            sections["affected_systems"] = parts[1].split("#", 1)[0].strip() if len(parts) > 1 else ""
        
        if "# Attack Vectors" in exploitation_report:
            parts = exploitation_report.split("# Attack Vectors", 1)
            sections["attack_vectors"] = parts[1].split("#", 1)[0].strip() if len(parts) > 1 else ""
        
        if "# Threat Actors" in exploitation_report:
            parts = exploitation_report.split("# Threat Actors", 1)
            sections["threat_actors"] = parts[1].split("#", 1)[0].strip() if len(parts) > 1 else ""
        
        # Generate the final report
        report = template
        for key, value in sections.items():
            placeholder = f"{{{{ {key} }}}}"
            report = report.replace(placeholder, value)
        
        # Save the report to disk
        output_path = config.get("output_path", "index.md")
        with open(output_path, "w") as f:
            f.write(report)
        
        return f"Exploitation report generated and saved to {output_path}"
    except Exception as e:
        error_msg = f"Error generating report: {str(e)}"
        logger.error(error_msg)
        return error_msg

@mcp.tool()
async def get_exploitation_articles(feed_url: Optional[str] = None, count: int = 30) -> str:
    """Get articles with exploitation-related content.
    
    Args:
        feed_url: Optional URL override for the RSS feed
        count: Maximum number of articles to return
    """
    config = load_config()
    if not feed_url:
        feed_url = config.get("feed_url", "https://ricomanifesto.github.io/SentryDigest/feed.xml")
    
    logger.info(f"Getting exploitation articles from {feed_url}")
    try:
        # Initialize the fetcher
        fetcher = SentryDigestFetcher(feed_url)
        
        # Fetch articles
        all_articles = await fetcher.fetch_articles()
        
        # Enrich with content
        enriched_articles = await fetcher.enrich_article_content(all_articles)
        
        # Filter for exploitation content
        from entities import analyze_article_exploitation
        
        exploitation_articles = []
        for article in enriched_articles:
            analysis = analyze_article_exploitation(article)
            if analysis.get("has_exploitation_content", False):
                exploitation_articles.append(article)
                if len(exploitation_articles) >= count:
                    break
        
        if not exploitation_articles:
            return "No exploitation-related articles found."
        
        # Format the articles
        formatted_articles = []
        for article in exploitation_articles:
            formatted = f"TITLE: {article.get('title', '')}\n"
            formatted += f"SOURCE: {article.get('source', '')}\n"
            formatted += f"LINK: {article.get('link', '')}\n"
            formatted += f"CVEs: {', '.join(analyze_article_exploitation(article).get('cves', []))}\n"
            formatted += f"SUMMARY: {article.get('summary', '')}\n"
            formatted_articles.append(formatted)
        
        return "\n---\n".join(formatted_articles)
    except Exception as e:
        error_msg = f"Error getting exploitation articles: {str(e)}"
        logger.error(error_msg)
        return error_msg

# Export the compiled MCP application
mcp_app = mcp 
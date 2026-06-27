import logging
import os
from typing import List, Dict, Any
from datetime import datetime

import tiktoken

from .model_config import resolve_model, validate_model
from .opencode_client import OpenCodeClient, OpenCodeUnavailable, parse_model_selection
from .entities import extract_cve_ids
from .source_attribution import (
    clean_article_source,
    collect_source_attribution_entries,
)

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Initialize tokenizer for token counting
tokenizer = tiktoken.get_encoding("cl100k_base")


def load_template() -> str:
    """Load the report template"""
    template_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "..",
        "docs",
        "templates",
        "exploitation_report.md",
    )
    try:
        with open(template_path, "r") as f:
            return f.read()
    except Exception as e:
        logger.error(f"Error loading template: {e}")
        return """# Exploitation Report

{{ exploitation_summary }}

## Affected Systems

{{ affected_systems }}

## Attack Vectors

{{ attack_vectors }}

## Mitigation

{{ mitigation }}
"""


def filter_exploitation_articles(
    articles: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    """
    Filter articles to only include those with exploitation-related content

    Args:
        articles: List of article dictionaries

    Returns:
        Filtered list of articles with exploitation content
    """
    logger.info(f"Filtering {len(articles)} articles for exploitation content")

    # Pass all articles to the AI for analysis
    # This gives the AI more context to work with
    return articles


def format_article_summary(article: Dict[str, Any]) -> str:
    def clean_text(value: Any, default: str = "") -> str:
        if value is None:
            return default
        return str(value).strip()

    title = clean_text(article.get("title"), "Untitled article") or "Untitled article"
    source = clean_article_source(article.get("source"))
    link = clean_text(article.get("link"))
    content = clean_text(
        article.get("content", article.get("summary")),
        "No content available",
    )

    metadata = []
    if source:
        metadata.append(f"Source: {source}")
    if link:
        metadata.append(f"URL: {link}")
    if article_cves := collect_structured_cves(article):
        metadata.append(f"CVEs: {', '.join(article_cves)}")

    heading = f"**{title}**"
    if metadata:
        heading = f"{heading} ({'; '.join(metadata)})"

    return f"{heading}\n\n{content[:500]}...\n\n"


def collect_structured_cves(article: Dict[str, Any]) -> list[str]:
    """Collect CVE IDs from structured article metadata."""
    cves: list[str] = []
    cves.extend(str(cve).strip() for cve in article.get("cves", []) if str(cve).strip())
    cves.extend(extract_cve_ids("\n".join(cves)))

    seen: set[str] = set()
    unique_cves: list[str] = []
    for cve in cves:
        normalized_cve = cve.upper()
        if normalized_cve in seen:
            continue
        seen.add(normalized_cve)
        unique_cves.append(normalized_cve)

    return unique_cves


def collect_prompt_cves(article_summary: str) -> list[str]:
    """Collect CVE IDs from the exact article text sent to the model."""
    return [cve.upper() for cve in extract_cve_ids(article_summary)]


async def analyze_exploitation(
    articles: List[Dict[str, Any]], config: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Analyze exploitation-related articles

    Args:
        articles: List of article dictionaries with exploitation content
        config: Configuration dictionary

    Returns:
        Exploitation analysis report
    """
    logger.info(f"Analyzing exploitation in {len(articles)} articles")

    # Initialize the AI model through OpenCode.
    model_name = resolve_model(config)
    max_tokens = int(config.get("analysis", {}).get("max_tokens", 4000))
    try:
        validate_model(model_name)
        model_selection = parse_model_selection(model_name)
    except ValueError as e:
        logger.error(f"Invalid model configuration: {e}")
        return {
            "exploitation_report": f"# Error: Invalid Model\n\n{str(e)}",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "error": str(e),
        }

    # Prepare all article summaries
    all_article_summaries = []
    all_cves = set()
    all_systems = set()
    all_attack_vectors = set()

    for article in articles:
        article_summary = format_article_summary(article)
        all_article_summaries.append(article_summary)

        # Extract CVEs from the same text the model sees.
        for cve in collect_prompt_cves(article_summary):
            all_cves.add(cve)
        if "affected_systems" in article:
            for system in article.get("affected_systems", []):
                all_systems.add(system)
        if "attack_vectors" in article:
            for vector in article.get("attack_vectors", []):
                all_attack_vectors.add(vector)

    # Create a comprehensive prompt for exploitation analysis
    prompt = f"""
You're a cybersecurity expert specializing in vulnerability and exploitation analysis. Analyze the following security news articles to generate a comprehensive report on active exploitation.

Generate a report following this EXACT structure with professional markdown formatting:

# Exploitation Report

## Executive Summary

[Write two to three concise executive-readable paragraphs covering the most critical exploitation activity. Do not emit one long block of text. Only mention CVE IDs if they are explicitly provided in the articles. Do not mention when CVE IDs are missing or unavailable.]

## Active Exploitation Details

[For each actively exploited vulnerability, create a well-formatted subsection:

### Vulnerability Name
- **Description**: Detailed description of the vulnerability
- **Impact**: What attackers can achieve
- **Status**: Current exploitation status and patch availability
- **CVE ID**: [Only include this line if a CVE ID is mentioned in the articles]
]

## Affected Systems and Products

[Create a well-formatted bullet list:
- **Product/System Name**: Specific details about affected versions or components
- **Platform**: Description of affected platforms or environments
]

## Attack Vectors and Techniques

[Use clear formatting for attack methods:
- **Technique Name**: Description of how the attack works
- **Vector**: Specific attack vector details
]

## Threat Actor Activities

[Organize threat actor information clearly:
- **Actor/Group**: Activities and targeting details
- **Campaign**: Operation descriptions and impacts
]

## Source Attribution

[List the source articles used for this report:
- **Article Title**: Source name - URL
Only use source names and URLs provided in the article metadata. Do not invent
or infer sources.]

Formatting requirements:
- Use proper markdown with **bold** for emphasis
- Create clear bullet points with good spacing
- Use ### for subsections within main sections
- Include the ## Executive Summary section and split it into multiple paragraphs
- Write professional, well-structured content
- Only mention CVE IDs when they are actually provided in the source articles
- Include every CVE ID extracted from the article metadata when it is relevant to exploitation details
- Do NOT mention missing or unavailable CVE information
- Include the Source Attribution section when article source metadata or URLs are available
- Do not leave Threat Actor Activities as a single stale-looking item when broader actor or campaign activity appears elsewhere in the report; include the relevant actor, campaign, or unknown-operator roll-ups grounded in the articles

Focus specifically on:
- Zero-day vulnerabilities being actively exploited
- Recently patched vulnerabilities that were exploited
- New attack vectors and techniques
- Critical vulnerabilities with high impact
- Notable threat actors and their activities

Here are the articles:

{"".join(all_article_summaries)}

Generate a well-formatted exploitation report following the structure above. Be comprehensive but only include CVE IDs when they are explicitly mentioned in the articles.
"""

    # Estimate token count for logging
    estimated_tokens = len(tokenizer.encode(prompt))
    logger.info(f"Estimated token count for analysis prompt: {estimated_tokens}")

    # Call the AI model
    try:
        client = OpenCodeClient(timeout=max(120.0, float(max_tokens) / 20))
        exploitation_report = await client.generate(
            system_prompt="You are a cybersecurity threat hunter specializing in vulnerability exploitation analysis. Your task is to create a comprehensive report on current exploit activity based on recent security articles. Be extremely thorough in identifying ALL exploited vulnerabilities mentioned in the articles, including zero-days, active exploits, and recently patched vulnerabilities that were exploited in the wild.",
            user_prompt=prompt,
            model=model_selection,
            title="SentryInsight exploitation report",
        )

        source_attribution_entries = collect_source_attribution_entries(articles)
        return {
            "exploitation_report": exploitation_report,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "analyzed_article_count": len(articles),
            "cves_identified": list(all_cves),
            "source_attribution_required": bool(source_attribution_entries),
            "source_attribution_entries": source_attribution_entries,
        }
    except OpenCodeUnavailable as e:
        logger.warning(f"Skipping exploitation analysis: {e}")
        return {
            "exploitation_report": "",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "analyzed_article_count": len(articles),
            "cves_identified": list(all_cves),
            "skipped": True,
            "skip_reason": str(e),
        }
    except Exception as e:
        logger.error(f"Error during exploitation analysis: {e}")
        return {
            "exploitation_report": f"# Error Generating Exploitation Report\n\nAn error occurred during analysis: {str(e)}\n\n## Partial Data\n\nCVEs identified: {', '.join(all_cves) if all_cves else 'None'}\n\nAffected systems: {', '.join(all_systems) if all_systems else 'None'}",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "error": str(e),
        }


def analyze_article_exploitation(article: Dict[str, Any]) -> Dict[str, Any]:
    """
    Analyze exploitation content in an article

    Args:
        article: Article dictionary

    Returns:
        Dictionary with exploitation details
    """
    # We'll skip the detailed article analysis and rely on the AI for comprehensive analysis
    return {
        "has_exploitation_content": True,  # Consider all articles potentially relevant
        "cves": [],
        "cvss_scores": [],
        "exploitation_details": {
            "exploitation_status": "Unknown",
            "affected_systems": [],
            "attack_vectors": [],
        },
    }

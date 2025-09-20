import logging
import os
import re
import json
from typing import List, Dict, Any
from datetime import datetime

import tiktoken
from langchain_anthropic import ChatAnthropic
from langchain.schema import HumanMessage, SystemMessage

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize tokenizer for token counting
tokenizer = tiktoken.get_encoding("cl100k_base")

def load_template() -> str:
    """Load the report template"""
    template_path = os.path.join(os.path.dirname(__file__), "..", "..", "docs", "templates", "exploitation_report.md")
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

def filter_exploitation_articles(articles: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
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

async def analyze_exploitation(articles: List[Dict[str, Any]], config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Analyze exploitation-related articles
    
    Args:
        articles: List of article dictionaries with exploitation content
        config: Configuration dictionary
        
    Returns:
        Exploitation analysis report
    """
    logger.info(f"Analyzing exploitation in {len(articles)} articles")
    
    # Get the template
    template = load_template()
    
    # Initialize the AI model (Anthropic Claude)
    api_key = os.getenv("ANTHROPIC_API_KEY")
    model_name = config.get("analysis", {}).get("model", "claude-sonnet-4-20250514")
    max_tokens = config.get("analysis", {}).get("max_tokens", 4000)
    
    if not api_key:
        logger.error("No Anthropic API key provided")
        return {
            "exploitation_report": "# Error: No Anthropic API Key\n\nPlease set the ANTHROPIC_API_KEY environment variable.",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "error": "No API key"
        }

    model = ChatAnthropic(
        api_key=api_key,
        model=model_name,
        max_tokens=max_tokens
    )
    
    # Prepare all article summaries
    all_article_summaries = []
    all_cves = set()
    all_systems = set()
    all_attack_vectors = set()
    
    for article in articles:
        # Get article metadata
        title = article.get("title", "")
        source = article.get("source", "")
        link = article.get("link", "")
        
        # Get article content or summary
        content = article.get("content", article.get("summary", "No content available"))
        
        # Create summary
        summary = f"**{title}** (Source: {source})\n\nURL: {link}\n\n{content[:500]}...\n\n"
        all_article_summaries.append(summary)
        
        # Extract CVEs and affected systems
        if "cves" in article:
            for cve in article.get("cves", []):
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

[Write a comprehensive summary paragraph of the most critical exploitation activity. Only mention CVE IDs if they are explicitly provided in the articles. Do not mention when CVE IDs are missing or unavailable.]

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

Formatting requirements:
- Use proper markdown with **bold** for emphasis
- Create clear bullet points with good spacing
- Use ### for subsections within main sections
- Write professional, well-structured content
- Only mention CVE IDs when they are actually provided in the source articles
- Do NOT mention missing or unavailable CVE information

Focus specifically on:
- Zero-day vulnerabilities being actively exploited
- Recently patched vulnerabilities that were exploited
- New attack vectors and techniques
- Critical vulnerabilities with high impact
- Notable threat actors and their activities

Here are the articles:

{''.join(all_article_summaries)}

Generate a well-formatted exploitation report following the structure above. Be comprehensive but only include CVE IDs when they are explicitly mentioned in the articles.
"""
    
    # Estimate token count for logging
    estimated_tokens = len(tokenizer.encode(prompt))
    logger.info(f"Estimated token count for analysis prompt: {estimated_tokens}")
    
    # Call the AI model
    try:
        messages = [
            SystemMessage(content="You are a cybersecurity threat hunter specializing in vulnerability exploitation analysis. Your task is to create a comprehensive report on current exploit activity based on recent security articles. Be extremely thorough in identifying ALL exploited vulnerabilities mentioned in the articles, including zero-days, active exploits, and recently patched vulnerabilities that were exploited in the wild."),
            HumanMessage(content=prompt)
        ]
        
        response = await model.ainvoke(messages)
        
        # Extract the exploitation report
        exploitation_report = response.content
        
        return {
            "exploitation_report": exploitation_report,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "analyzed_article_count": len(articles),
            "cves_identified": list(all_cves)
        }
    except Exception as e:
        logger.error(f"Error during exploitation analysis: {e}")
        return {
            "exploitation_report": f"# Error Generating Exploitation Report\n\nAn error occurred during analysis: {str(e)}\n\n## Partial Data\n\nCVEs identified: {', '.join(all_cves) if all_cves else 'None'}\n\nAffected systems: {', '.join(all_systems) if all_systems else 'None'}",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "error": str(e)
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
            "attack_vectors": []
        }
    }

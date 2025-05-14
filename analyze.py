import logging
import yaml
from typing import List, Dict, Any
from datetime import datetime
from pathlib import Path

from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI

from entities import analyze_article_exploitation

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load exploitation report template
def load_template() -> str:
    """Load the exploitation report template"""
    template_path = Path(__file__).parent / "templates" / "exploitation-report.md"
    try:
        with open(template_path, "r") as f:
            return f.read()
    except FileNotFoundError:
        logger.warning(f"Template file not found at {template_path}, using default template")
        return """# Exploitation Intelligence Report

## Key Vulnerability Statistics
- **Total Vulnerabilities Analyzed:** [Number]
- **Critical Severity Count:** [Number]
- **Zero-Day Count:** [Number]
- **Most Affected System:** [System Name]

## Critical Vulnerabilities

### [CVE ID or Name]
- **Severity:** [CVSS Score/Severity Level]
- **Exploitation Status:** [Actively Exploited/PoC Available/Not Observed]
- **Affected Systems:** [List of affected systems]
- **Description:** [Brief description of the vulnerability]
- **Technical Details:** [Technical explanation of exploitation]
- **Attack Vectors:** [How attackers are exploiting this vulnerability]

## Mitigation Recommendations
1. [Specific recommendation]
2. [Specific recommendation]
3. [Specific recommendation]

## Exploitation Forecast
- [Expected progression of exploitation attempts]
- [Prediction for zero-day discoveries]
"""

async def filter_exploitation_articles(articles: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Filter articles to identify those related to exploitation
    
    Args:
        articles: List of article dictionaries
        
    Returns:
        Filtered list of exploitation-related articles
    """
    logger.info(f"Filtering {len(articles)} articles for exploitation content")
    
    exploitation_articles = []
    for article in articles:
        # Analyze article for exploitation content
        analysis = analyze_article_exploitation(article)
        
        # If article has exploitation content, add it to the filtered list
        if analysis.get("has_exploitation_content", False):
            # Add the analysis to the article
            article["exploitation_analysis"] = analysis
            exploitation_articles.append(article)
    
    logger.info(f"Found {len(exploitation_articles)} articles with exploitation content")
    return exploitation_articles

async def analyze_exploitation(
    articles: List[Dict[str, Any]], 
    model_config: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Analyze exploitation articles and generate a report
    
    Args:
        articles: List of exploitation-related article dictionaries
        model_config: Configuration for the language model
        
    Returns:
        Dictionary containing the exploitation report
    """
    logger.info(f"Analyzing {len(articles)} exploitation articles")
    
    # Initialize the language model
    model = ChatOpenAI(
        model=model_config.get("name", "gpt-4-turbo"),
        temperature=model_config.get("temperature", 0.2)
    )
    
    # Load the template
    template = load_template()
    
    # Extract CVE details from all articles
    cve_details = []
    for article in articles:
        analysis = article.get("exploitation_analysis", {})
        
        # Extract CVEs
        for cve in analysis.get("cves", []):
            cve_details.append({
                "cve_id": cve,
                "article_title": article.get("title", ""),
                "article_link": article.get("link", ""),
                "cvss_scores": analysis.get("cvss_scores", []),
                "exploitation_status": analysis.get("exploitation_details", {}).get("exploitation_status"),
                "affected_systems": analysis.get("exploitation_details", {}).get("affected_systems", []),
                "attack_vectors": analysis.get("exploitation_details", {}).get("attack_vectors", [])
            })
    
    # Prepare the prompt for the AI
    prompt = f"""You are a cybersecurity threat hunter focused on vulnerability exploitation analysis.
    
Analyze the following exploitation-related articles and create a comprehensive exploitation intelligence report.

## Articles
{[{'title': a.get('title', ''), 'link': a.get('link', ''), 'content': a.get('content', '')[:500] + '...' if len(a.get('content', '')) > 500 else a.get('content', '')} for a in articles]}

## Extracted CVEs and Exploitation Details
{cve_details}

## Instructions
1. Focus on active exploitations and zero-days
2. Prioritize critical and high severity vulnerabilities
3. Provide technical details about exploit methods
4. Include mitigation recommendations
5. Forecast future exploitation trends

Format your report according to this template:
{template}

Make sure to:
- Include actual CVE IDs where available
- Link vulnerabilities to affected systems
- Provide CVSS scores when mentioned
- Highlight if exploits are being actively used in the wild
- List specific mitigation steps
"""
    
    # Call the AI model
    messages = [
        SystemMessage(content="You are a cybersecurity threat hunter specializing in vulnerability exploitation analysis."),
        HumanMessage(content=prompt)
    ]
    
    response = await model.ainvoke(messages)
    
    # Extract the exploitation report
    exploitation_report = response.content
    
    return {
        "exploitation_report": exploitation_report,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

"""MCP (Model-Channel-Protocol) workflow for cybersecurity exploitation analysis."""

import os
import logging
from typing import Dict, Any, List, Annotated, TypedDict
import json

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.tools import tool
from langgraph.graph import StateGraph, START, END

from tools import RSSTools

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize tools
rss_tools = RSSTools()

# Define state schema
class WorkflowState(TypedDict):
    """State for the MCP workflow."""
    feed_data: Dict
    articles: List[Dict]
    enriched_articles: List[Dict]
    exploitation_relevant: List[Dict]
    analysis_result: Dict
    report: str
    errors: List[str]
    status: str

# Define node functions
async def fetch_feed(state: WorkflowState) -> WorkflowState:
    """Fetch the RSS feed."""
    logger.info("Fetching RSS feed")
    try:
        config_path = os.path.join(os.path.dirname(__file__), "config.json")
        with open(config_path, "r") as f:
            config = json.load(f)
        
        feed_url = config.get("feed_url", "https://ricomanifesto.github.io/SentryDigest/feed.xml")
        feed_data = await rss_tools.fetch_rss_feed(feed_url)
        
        # Extract articles
        articles = []
        for entry in feed_data.get("entries", []):
            article = rss_tools.extract_basic_fields(entry)
            articles.append(article)
        
        return {
            **state, 
            "feed_data": feed_data,
            "articles": articles,
            "status": "feed_fetched"
        }
    except Exception as e:
        logger.error(f"Error fetching feed: {e}")
        return {**state, "errors": state.get("errors", []) + [f"Feed fetch error: {str(e)}"], "status": "error"}

async def enrich_articles(state: WorkflowState) -> WorkflowState:
    """Enrich articles with full content."""
    logger.info(f"Enriching {len(state.get('articles', []))} articles with content")
    try:
        enriched_articles = []
        for article in state.get("articles", []):
            enriched = await rss_tools.enrich_article_content(article)
            enriched_articles.append(enriched)
        
        return {
            **state, 
            "enriched_articles": enriched_articles,
            "status": "articles_enriched"
        }
    except Exception as e:
        logger.error(f"Error enriching articles: {e}")
        return {**state, "errors": state.get("errors", []) + [f"Enrichment error: {str(e)}"], "status": "error"}

def filter_exploitation_articles(state: WorkflowState) -> WorkflowState:
    """Filter articles relevant to exploitation."""
    logger.info("Filtering articles for exploitation content")
    try:
        # Initialize AI model
        config_path = os.path.join(os.path.dirname(__file__), "config.json")
        with open(config_path, "r") as f:
            config = json.load(f)
        
        model_name = config.get("analysis", {}).get("model", "gpt-4o")
        temperature = config.get("analysis", {}).get("temperature", 0.1)
        
        model = ChatOpenAI(model=model_name, temperature=temperature)
        
        # Prepare articles for filtering
        articles = state.get("enriched_articles", [])
        
        # Create a system prompt
        system_prompt = """
        You're a cybersecurity expert analyzing news for exploitation information.
        For each article, determine if it contains information about:
        1. Zero-day vulnerabilities
        2. Active exploitation of vulnerabilities
        3. New attack vectors
        4. Critical patches
        5. Threat actor activities specifically related to exploits
        
        Respond with YES if the article contains exploitation-related content, or NO if it doesn't.
        """
        
        # Filter articles
        exploitation_relevant = []
        for article in articles:
            title = article.get("title", "")
            summary = article.get("summary", "")
            content = article.get("content", "")
            
            # Combine title and summary for shorter analysis
            analysis_text = f"TITLE: {title}\n\nSUMMARY: {summary}"
            
            # Create messages
            messages = [
                SystemMessage(content=system_prompt),
                HumanMessage(content=f"Does this article contain information about vulnerability exploitation?\n\n{analysis_text}")
            ]
            
            # Get response
            response = model.invoke(messages)
            
            # If relevant, add to filtered list
            if "YES" in response.content.upper():
                exploitation_relevant.append(article)
        
        logger.info(f"Filtered {len(exploitation_relevant)} exploitation-relevant articles")
        
        return {
            **state, 
            "exploitation_relevant": exploitation_relevant,
            "status": "articles_filtered"
        }
    except Exception as e:
        logger.error(f"Error filtering articles: {e}")
        return {**state, "errors": state.get("errors", []) + [f"Filtering error: {str(e)}"], "status": "error"}

async def analyze_exploitation(state: WorkflowState) -> WorkflowState:
    """Perform in-depth exploitation analysis."""
    logger.info("Analyzing exploitation content")
    try:
        # Initialize model
        config_path = os.path.join(os.path.dirname(__file__), "config.json")
        with open(config_path, "r") as f:
            config = json.load(f)
        
        model_name = config.get("analysis", {}).get("model", "gpt-4o")
        temperature = config.get("analysis", {}).get("temperature", 0.1)
        
        model = ChatOpenAI(model=model_name, temperature=temperature)
        
        # Get relevant articles
        articles = state.get("exploitation_relevant", [])
        
        if not articles:
            return {
                **state, 
                "analysis_result": {"message": "No exploitation-relevant articles found"},
                "status": "no_relevant_articles"
            }
        
        # Prepare system prompt with specific section headers
        system_prompt = """
        You're a cybersecurity expert specialized in vulnerability exploitation. 
        Analyze the provided cybersecurity news articles and create a comprehensive exploitation report.
        
        Focus especially on:
        1. Zero-day vulnerabilities being actively exploited
        2. Recently patched vulnerabilities that were exploited
        3. New attack vectors and techniques
        4. Critical vulnerabilities with high impact
        5. Notable threat actors and their activities
        
        Format your report using these EXACT section headers:
        # Executive Summary
        (Brief summary of the most critical findings)
        
        # Exploitation Details
        (Information about active exploits, zero-days, etc.)
        
        # Affected Systems
        (Products, vendors, and systems affected)
        
        # Attack Vectors
        (How the attacks are carried out, technical details)
        
        # Threat Actors
        (Information about threat actors if available)
        
        Be thorough, technical, and precise. This report will be used by security teams to prioritize their response.
        """
        
        # Prepare article data
        article_data = "\n\n".join([
            f"TITLE: {article.get('title', '')}\n"
            f"SOURCE: {article.get('source', '')}\n"
            f"DATE: {article.get('date', '')}\n"
            f"SUMMARY: {article.get('summary', '')}"
            for article in articles
        ])
        
        # Create messages
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=f"Generate an exploitation report based on these cybersecurity news articles:\n\n{article_data}")
        ]
        
        # Get response
        response = model.invoke(messages)
        
        analysis_result = {
            "exploitation_report": response.content,
            "analyzed_article_count": len(articles),
            "sources": list(set(article.get("source", "") for article in articles)),
        }
        
        return {
            **state, 
            "analysis_result": analysis_result,
            "status": "analysis_complete"
        }
    except Exception as e:
        logger.error(f"Error analyzing exploitation: {e}")
        return {**state, "errors": state.get("errors", []) + [f"Analysis error: {str(e)}"], "status": "error"}

def generate_report(state: WorkflowState) -> WorkflowState:
    """Generate the final markdown report."""
    logger.info("Generating final report")
    try:
        analysis = state.get("analysis_result", {})
        exploitation_report = analysis.get("exploitation_report", "No exploitation report generated")
        
        # Load template if available
        template_path = os.path.join(os.path.dirname(__file__), "templates", "exploitation_report.md")
        try:
            with open(template_path, "r") as f:
                template = f.read()
        except:
            template = "# SentryDigest Exploitation Report\n\n{{ exploitation_summary }}"
        
        # Extract sections from AI report
        # We'll use a simple approach: the entire report becomes the exploitation_summary
        # and we'll extract other sections if they exist using headings as markers
        
        sections = {
            "exploitation_summary": exploitation_report,
            "exploitation_details": "",
            "affected_systems": "",
            "attack_vectors": "",
            "mitigation": "",
            "threat_actors": ""
        }
        
        # Look for common section headers in the AI output
        if "# Executive Summary" in exploitation_report:
            parts = exploitation_report.split("# Executive Summary", 1)
            sections["exploitation_summary"] = "# Executive Summary" + parts[1].split("#", 1)[0]
        
        if "# Exploitation Details" in exploitation_report or "# Active Exploitation" in exploitation_report:
            marker = "# Exploitation Details" if "# Exploitation Details" in exploitation_report else "# Active Exploitation"
            parts = exploitation_report.split(marker, 1)
            sections["exploitation_details"] = parts[1].split("#", 1)[0] if len(parts) > 1 else ""
            
        if "# Affected Systems" in exploitation_report or "# Vulnerable Systems" in exploitation_report:
            marker = "# Affected Systems" if "# Affected Systems" in exploitation_report else "# Vulnerable Systems"
            parts = exploitation_report.split(marker, 1)
            sections["affected_systems"] = parts[1].split("#", 1)[0] if len(parts) > 1 else ""
            
        if "# Attack Vectors" in exploitation_report:
            parts = exploitation_report.split("# Attack Vectors", 1)
            sections["attack_vectors"] = parts[1].split("#", 1)[0] if len(parts) > 1 else ""
            
        if "# Mitigation" in exploitation_report or "# Recommendations" in exploitation_report:
            marker = "# Mitigation" if "# Mitigation" in exploitation_report else "# Recommendations"
            parts = exploitation_report.split(marker, 1)
            sections["mitigation"] = parts[1].split("#", 1)[0] if len(parts) > 1 else ""
            
        if "# Threat Actor" in exploitation_report:
            parts = exploitation_report.split("# Threat Actor", 1)
            sections["threat_actors"] = parts[1].split("#", 1)[0] if len(parts) > 1 else ""
        
        # Generate report from template by replacing all placeholders
        report = template
        for key, value in sections.items():
            placeholder = f"{{{{ {key} }}}}"
            report = report.replace(placeholder, value.strip())
        
        # If no sections were populated, use the full report as exploitation_summary
        if report.find("{{") != -1:
            # There are still unpopulated variables
            report = f"# SentryDigest Exploitation Report\n\n{exploitation_report}"
        
        return {
            **state, 
            "report": report,
            "status": "report_generated"
        }
    except Exception as e:
        logger.error(f"Error generating report: {e}")
        return {**state, "errors": state.get("errors", []) + [f"Report generation error: {str(e)}"], "status": "error"}

def save_report(state: WorkflowState) -> WorkflowState:
    """Save the report to a file."""
    logger.info("Saving report to file")
    try:
        # Load configuration
        config_path = os.path.join(os.path.dirname(__file__), "config.json")
        with open(config_path, "r") as f:
            config = json.load(f)
        
        output_path = config.get("output_path", "index.md")
        
        # Write report to file
        with open(output_path, "w") as f:
            f.write(state.get("report", "Error generating report"))
        
        return {
            **state, 
            "status": "complete"
        }
    except Exception as e:
        logger.error(f"Error saving report: {e}")
        return {**state, "errors": state.get("errors", []) + [f"Save error: {str(e)}"], "status": "error"}

def should_end(state: WorkflowState) -> str:
    """Determine if workflow should end."""
    if state.get("status") == "error":
        return "error"
    elif state.get("status") == "no_relevant_articles":
        return "no_articles"
    elif state.get("status") == "complete":
        return "success"
    else:
        return "continue"

# Create workflow graph
def create_workflow() -> StateGraph:
    """Create the MCP workflow graph."""
    # Initialize workflow
    workflow = StateGraph(WorkflowState)
    
    # Define nodes
    workflow.add_node("fetch_feed", fetch_feed)
    workflow.add_node("enrich_articles", enrich_articles)
    workflow.add_node("filter_articles", filter_exploitation_articles)
    workflow.add_node("analyze_exploitation", analyze_exploitation)
    workflow.add_node("generate_report", generate_report)
    workflow.add_node("save_report", save_report)
    
    # Define edges
    workflow.add_edge(START, "fetch_feed")
    workflow.add_edge("fetch_feed", "enrich_articles")
    workflow.add_edge("enrich_articles", "filter_articles")
    workflow.add_edge("filter_articles", "analyze_exploitation")
    workflow.add_edge("analyze_exploitation", "generate_report")
    workflow.add_edge("generate_report", "save_report")
    workflow.add_edge("save_report", END)
    
    # Add conditional edges
    workflow.add_conditional_edges(
        "analyze_exploitation",
        should_end,
        {
            "error": END,
            "no_articles": "generate_report",
            "continue": "generate_report"
        }
    )
    
    return workflow

# Export the compiled workflow
workflow = create_workflow().compile()

async def run_exploitation_analysis():
    """Run the exploitation analysis workflow."""
    logger.info("Starting exploitation analysis workflow")
    
    # Initialize state
    initial_state = {
        "feed_data": {},
        "articles": [],
        "enriched_articles": [],
        "exploitation_relevant": [],
        "analysis_result": {},
        "report": "",
        "errors": [],
        "status": "started"
    }
    
    # Run the workflow without using MemoryCheckpoint
    try:
        # Using workflow directly without checkpoint
        result = await workflow.ainvoke(initial_state)
        logger.info(f"Workflow completed with status: {result.get('status')}")
        return result
    except Exception as e:
        logger.error(f"Workflow error: {e}")
        return {
            **initial_state,
            "errors": [f"Workflow error: {str(e)}"],
            "status": "error"
        } 
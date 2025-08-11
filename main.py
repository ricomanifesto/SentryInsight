"""SentryDigest Exploitation Report Generator using LangGraph workflow with MCP RSS tools."""

import os
import asyncio
import logging
import json
import threading
from datetime import datetime

# Initialize environment variables
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Anthropic API key should be set via environment variable ANTHROPIC_API_KEY

# Import the LangGraph workflow
from src.core.workflow import run_exploitation_analysis

# Import MCP server for RSS operations
from src.services.rss_mcp import mcp_app

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("exploitation-analysis.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def run_mcp_server():
    """Run the MCP server in a separate thread."""
    logger.info("Starting RSS MCP Server")
    mcp_app.run(transport="stdio")

async def main():
    """Main function to run the LangGraph workflow."""
    logger.info("Starting SentryDigest Exploitation Report Generator with LangGraph workflow")
    
    try:
        # Run the LangGraph workflow
        result = await run_exploitation_analysis()
        
        if not result or result.get("status") == "failed":
            logger.error("Errors occurred during analysis")
        else:
            logger.info("Analysis completed successfully")
            
    except Exception as e:
        logger.error(f"Error in main function: {e}")

if __name__ == "__main__":
    # Start MCP server in a separate thread if needed
    # Uncomment the following lines if you need the MCP server running:
    # mcp_thread = threading.Thread(target=run_mcp_server, daemon=True)
    # mcp_thread.start()
    
    # Run the main workflow
    asyncio.run(main())

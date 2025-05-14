"""SentryDigest Exploitation Report Generator using Model Context Protocol."""

import os
import asyncio
import logging

# Initialize environment variables
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Import the Model Context Protocol server
from mcp_workflow import mcp_app

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

if __name__ == "__main__":
    # Run the MCP server
    logger.info("Starting SentryDigest MCP Server")
    mcp_app.run(transport="stdio")  # You can also use "http" for a web server

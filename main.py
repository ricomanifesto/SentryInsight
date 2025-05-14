"""SentryDigest Exploitation Report Generator using MCP architecture."""

import os
import asyncio
import logging
import json
from datetime import datetime

# Initialize environment variables
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Import the MCP workflow
from mcp_workflow import run_exploitation_analysis

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

async def main():
    """Main function to run the application using MCP architecture."""
    logger.info("Starting SentryDigest Exploitation Report Generator with MCP architecture")
    
    try:
        # Run the MCP workflow
        result = await run_exploitation_analysis()
        
        if result.get("status") == "error":
            logger.error(f"Errors occurred during analysis: {result.get('errors')}")
        else:
            logger.info(f"Analysis completed successfully. Report saved.")
            
    except Exception as e:
        logger.error(f"Error in main function: {e}")

if __name__ == "__main__":
    # Run the main function
    asyncio.run(main())

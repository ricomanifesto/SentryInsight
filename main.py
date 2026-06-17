"""SentryDigest Exploitation Report Generator using LangGraph workflow with MCP RSS tools."""

import asyncio
import logging

# Initialize environment variables
try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

# OpenCode should be running with access to the configured model provider.

# Import the LangGraph workflow
from src.core.workflow import run_exploitation_analysis

# Import MCP server for RSS operations
from src.services.rss_mcp import mcp_app

logger = logging.getLogger(__name__)


def configure_logging():
    """Configure logging when the executable entrypoint runs."""
    root_logger = logging.getLogger()
    if root_logger.handlers:
        return

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("exploitation-analysis.log"),
            logging.StreamHandler(),
        ],
    )


def run_mcp_server():
    """Run the MCP server in a separate thread."""
    configure_logging()
    logger.info("Starting RSS MCP Server")
    mcp_app.run(transport="stdio")


async def main():
    """Main function to run the LangGraph workflow."""
    configure_logging()
    logger.info(
        "Starting SentryDigest Exploitation Report Generator with LangGraph workflow"
    )

    try:
        # Run the LangGraph workflow
        result = await run_exploitation_analysis()

        if not result or result.get("status") == "failed":
            logger.error("Errors occurred during analysis")
            raise SystemExit(1)
        else:
            logger.info("Analysis completed successfully")

    except Exception as e:
        logger.error(f"Error in main function: {e}")
        raise SystemExit(1)


if __name__ == "__main__":
    # Run the main workflow
    asyncio.run(main())

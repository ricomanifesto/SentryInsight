"""Run the SentryInsight exploitation-report workflow."""

import asyncio
import logging
import os
from pathlib import Path

# Initialize environment variables
try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

from src.core.observability import configure_observability
from src.core.workflow import run_exploitation_analysis
from src.core.review_delivery import write_run_outcome

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


async def main():
    """Main function to run the LangGraph workflow."""
    configure_logging()
    configure_observability()
    logger.info("Starting SentryInsight exploitation report generation")

    result = None
    # A fixed failure receipt exists even if execution stops before a valid plan.
    write_run_outcome(None, Path("."))
    try:
        result = await run_exploitation_analysis()

        if not result or result.get("status") == "failed":
            logger.error("Errors occurred during analysis")
            raise SystemExit(1)
        else:
            logger.info("Analysis completed successfully")

    except Exception as e:
        logger.error(f"Error in main function: {e}")
        raise SystemExit(1)
    finally:
        root = Path(
            (result or {}).get("config", {}).get("output_path", "index.md")
        ).parent
        outcome = write_run_outcome(result, root)
        if output_path := os.getenv("GITHUB_OUTPUT"):
            with open(output_path, "a") as stream:
                stream.write(
                    "report_generated="
                    + str(outcome["report_generated"]).lower()
                    + "\n"
                )


if __name__ == "__main__":
    asyncio.run(main())

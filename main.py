#!/usr/bin/env python3
import os
import sys
import argparse
import asyncio
import logging
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Import the workflow
from workflow import run_exploitation_analysis

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("exploitation-analysis.log")
    ]
)
logger = logging.getLogger(__name__)

async def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='SentryInsight - Exploitation Intelligence Analyzer')
    parser.add_argument('--config', type=str, default='config.yaml', help='Path to configuration file')
    args = parser.parse_args()
    
    logger.info(f"Starting SentryInsight Exploitation Intelligence Analyzer")
    logger.info(f"Using configuration file: {args.config}")
    
    try:
        # Run the exploitation analysis workflow
        final_state = await run_exploitation_analysis()
        
        if final_state:
            logger.info(f"Analysis completed with status: {final_state.get('status', 'unknown')}")
            logger.info(f"Analyzed {len(final_state.get('articles', []))} articles")
            logger.info(f"Found {len(final_state.get('filtered_articles', []))} exploitation-related articles")
        else:
            logger.error("Analysis failed to complete")
            sys.exit(1)
            
    except Exception as e:
        logger.error(f"Error running analysis: {e}")
        sys.exit(1)
    
    logger.info("Exploitation Intelligence Analysis completed successfully")

if __name__ == "__main__":
    asyncio.run(main())

import os
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, Any

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def publish_to_github_pages(
    analysis_results: Dict[str, Any],
    github_pages_config: Dict[str, Any]
) -> bool:
    """
    Publish analysis results to GitHub Pages
    
    Args:
        analysis_results: Dictionary containing analysis results
        github_pages_config: Configuration for GitHub Pages
        
    Returns:
        True if publishing was successful, False otherwise
    """
    if not github_pages_config.get("enabled", False):
        logger.info("GitHub Pages publishing is disabled")
        return False
    
    try:
        # Get the GitHub Pages repository directory
        repo_dir = github_pages_config.get("repo_directory", "./docs")
        repo_path = Path(repo_dir)
        
        # Create directory if it doesn't exist
        repo_path.mkdir(parents=True, exist_ok=True)
        
        # Extract the exploitation report and date
        exploitation_report = analysis_results.get("exploitation_report", "No exploitation report available.")
        report_date = analysis_results.get("date", datetime.now().strftime("%Y-%m-%d"))
        
        # Create the main index.html file
        index_path = repo_path / "index.md"
        with open(index_path, "w") as f:
            f.write("---\n")
            f.write("layout: default\n")
            f.write(f"title: Exploitation Intelligence Report - {report_date}\n")
            f.write("---\n\n")
            f.write(exploitation_report)
        
        # Create the navigation file
        nav_path = repo_path / "navigation.md"
        with open(nav_path, "w") as f:
            f.write("---\n")
            f.write("layout: default\n")
            f.write("title: Navigation\n")
            f.write("---\n\n")
            f.write("# SentryInsight Reports\n\n")
            f.write("## Available Reports\n\n")
            f.write("- [Exploitation Intelligence Report](./index.html)\n")
            f.write(f"\n\nLast updated: {datetime.now().strftime('%B %d, %Y at %H:%M:%S')}\n")
        
        # Create _config.yml if it doesn't exist
        config_path = repo_path / "_config.yml"
        if not config_path.exists():
            with open(config_path, "w") as f:
                f.write("theme: jekyll-theme-cayman\n")
                f.write("title: SentryInsight\n")
                f.write("description: Exploitation Intelligence Reports\n")
        
        logger.info(f"Successfully published to GitHub Pages directory: {repo_dir}")
        return True
        
    except Exception as e:
        logger.error(f"Error publishing to GitHub Pages: {e}")
        return False

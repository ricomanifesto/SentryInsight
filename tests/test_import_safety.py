import subprocess
import sys


def test_library_imports_do_not_configure_application_logging():
    script = """
import logging

root_logger = logging.getLogger()
root_logger.handlers.clear()

import src.core.analyze
import src.core.report_artifact
import src.core.workflow
import src.services.fetch

if root_logger.handlers:
    raise SystemExit(f"library imports configured {len(root_logger.handlers)} root handler(s)")
"""

    result = subprocess.run(
        [sys.executable, "-c", script],
        capture_output=True,
        check=False,
        text=True,
    )

    assert result.returncode == 0, result.stderr

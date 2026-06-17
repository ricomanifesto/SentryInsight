#!/usr/bin/env python3
"""Validate generated report markdown before publishing."""

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from src.core.report_validation import (
    format_report_validation_issues,
    validate_report_content,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate generated exploitation report markdown."
    )
    parser.add_argument(
        "report_path",
        nargs="?",
        default="index.md",
        help="Path to the generated markdown report.",
    )
    args = parser.parse_args()

    report_path = Path(args.report_path)
    if not report_path.exists():
        print(f"Report does not exist: {report_path}")
        return 1

    issues = validate_report_content(report_path.read_text())
    if issues:
        print("Report content validation failed:")
        print(format_report_validation_issues(issues))
        return 1

    print(f"Report content validation passed: {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Validate generated report markdown before publishing."""

# ruff: noqa: E402

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
    parser.add_argument(
        "--require-source-attribution",
        action="store_true",
        help="Fail unless the report contains the expected Source Attribution rows.",
    )
    parser.add_argument(
        "--source-attribution-entry",
        action="append",
        default=[],
        help="Expected canonical Source Attribution row. May be repeated.",
    )
    args = parser.parse_args()

    report_path = Path(args.report_path)
    if not report_path.exists():
        print(f"Report does not exist: {report_path}")
        return 1

    issues = validate_report_content(
        report_path.read_text(),
        require_source_attribution=args.require_source_attribution,
        source_attribution_entries=(
            args.source_attribution_entry if args.source_attribution_entry else None
        ),
    )
    if issues:
        print("Report content validation failed:")
        print(format_report_validation_issues(issues))
        return 1

    print(f"Report content validation passed: {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

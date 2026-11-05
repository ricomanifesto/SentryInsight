#!/usr/bin/env python3
"""Validate generated report markdown before publishing."""

# ruff: noqa: E402

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from src.core.report_validation import (
    blocking_issues,
    format_report_validation_issues,
    validate_report_content,
)


def advisory_grounding(config_path: Path) -> bool:
    """The repository configuration selects advisory or strict grounding."""
    try:
        config = json.loads(config_path.read_text())
    except (OSError, ValueError):
        return False
    analysis = config.get("analysis") if isinstance(config, dict) else None
    return isinstance(analysis, dict) and analysis.get("grounding") == "advisory"


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
        "--expected-cve",
        action="append",
        default=[],
        help="Expected CVE ID that must appear in the report. May be repeated.",
    )
    parser.add_argument(
        "--config",
        default=str(REPO_ROOT / "config/config.json"),
        help="Configuration that selects advisory or strict grounding.",
    )
    args = parser.parse_args()

    report_path = Path(args.report_path)
    if not report_path.exists():
        print(f"Report does not exist: {report_path}")
        return 1

    issues = validate_report_content(
        report_path.read_text(),
        expected_cves=args.expected_cve if args.expected_cve else None,
    )
    if advisory_grounding(Path(args.config)):
        blocking = blocking_issues(issues)
        advisory = [issue for issue in issues if issue not in blocking]
        if advisory:
            print("Report content advisories (not blocking):")
            print(format_report_validation_issues(advisory))
        issues = blocking
    if issues:
        print("Report content validation failed:")
        print(format_report_validation_issues(issues))
        return 1

    print(f"Report content validation passed: {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Offline source review metadata tools; no provider calls or source approvals."""

import argparse
from collections import Counter
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.core.review_delivery import (
    package_review,
    read_review_packet,
    write_run_outcome,
)
from src.core.source_review import (
    PLAN_KEY,
    SourceReviewError,
    prepare_source_review,
    write_review_packet,
)
from src.core.publication_transaction import PublicationError, recover_publication


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    preflight = commands.add_parser(
        "preflight", help="Plan a complete normalized article JSON list offline"
    )
    preflight.add_argument("input", type=Path)
    preflight.add_argument("--root", type=Path, required=True)
    inspect = commands.add_parser(
        "inspect", help="Print validated metadata dispositions only"
    )
    inspect.add_argument("packet", type=Path)
    package = commands.add_parser(
        "package", help="Create a strict metadata-only review artifact"
    )
    package.add_argument("--root", type=Path, default=Path("."))
    package.add_argument("--output", type=Path, required=True)
    recover = commands.add_parser(
        "recover", help="Explicitly restore prior local publication artifacts"
    )
    recover.add_argument("--root", type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.command == "preflight":
            write_run_outcome(None, args.root)
            plan = prepare_source_review(json.loads(args.input.read_text()))
            write_review_packet(plan.packet, args.root / ".sentryinsight-review")
            write_run_outcome(
                {
                    PLAN_KEY: plan.packet,
                    "status": (
                        "review_required"
                        if len(plan.eligible_keys) != len(plan.catalog)
                        else "completed_with_warnings"
                    ),
                },
                args.root,
            )
            print(
                json.dumps(
                    {
                        "plan_id": plan.packet["plan_id"],
                        "source_counts": dict(
                            Counter(row["state"] for row in plan.packet["sources"])
                        ),
                    },
                    sort_keys=True,
                )
            )
        elif args.command == "inspect":
            print(json.dumps(read_review_packet(args.packet), indent=2, sort_keys=True))
        elif args.command == "package":
            outcome = package_review(args.root, args.output)
            print(json.dumps(outcome, sort_keys=True))
        else:
            recover_publication(args.root)
            print("publication_recovered")
        return 0
    except (SourceReviewError, PublicationError, OSError, ValueError, TypeError):
        print("source_review_operation_failed", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

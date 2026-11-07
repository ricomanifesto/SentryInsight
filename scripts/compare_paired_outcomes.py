#!/usr/bin/env python3
"""Print the paired validity comparison for a benchmark runs file.

The file holds ``{"runs": [...]}`` where each run has ``date`` (the feed),
``mode`` (the arm), ``outcome`` and ``failure_codes``. Only counts, the test
result and failure codes are printed; report hashes and text are never read.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.core.paired_outcomes import (  # noqa: E402
    DEFAULT_ALPHA,
    PairedOutcomeError,
    compare_paired_outcomes,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("runs", type=Path)
    parser.add_argument("--baseline", default="off")
    parser.add_argument("--treatment", default="enabled")
    parser.add_argument("--alpha", type=float, default=DEFAULT_ALPHA)
    args = parser.parse_args(argv)
    try:
        data = json.loads(args.runs.read_text(encoding="utf-8"))
        runs = data["runs"] if isinstance(data, dict) else data
        result = compare_paired_outcomes(
            runs, baseline=args.baseline, treatment=args.treatment, alpha=args.alpha
        )
    except (OSError, ValueError, KeyError, TypeError, PairedOutcomeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

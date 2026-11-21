"""Manual paid readiness entry point: one first attempt, one receipt line.

Run only from a manual dispatch with the readiness flag, the pinned fact
manifest digest and fresh billing evidence. Prints one bounded categorical
receipt as JSON. A rendered candidate lands only in the fresh --output
directory outside the repository; nothing is promoted, uploaded, recorded in
history or published, and no log file is written.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.core.paid_readiness import run_paid_readiness  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        required=True,
        help="absolute, not yet existing directory outside the repository",
    )
    arguments = parser.parse_args(argv)
    receipt = asyncio.run(
        run_paid_readiness(environ=dict(os.environ), output=Path(arguments.output))
    )
    sys.stdout.write(json.dumps(receipt, sort_keys=True, separators=(",", ":")) + "\n")
    return 0 if receipt["outcome"] == "rendered" else 1


if __name__ == "__main__":
    raise SystemExit(main())

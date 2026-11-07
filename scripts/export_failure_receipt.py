#!/usr/bin/env python3
"""Export a validated private receipt, never arbitrary logs or model output."""

import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.core.failure_receipt import read_receipt, write_receipt
from src.core import exploitation_triage


def export_triage(source: Path, output: Path) -> None:
    """Copy a validated triage receipt; an absent receipt means triage was off."""
    if not source.exists() and not source.is_symlink():
        return
    try:
        if output.exists() or output.is_symlink():
            raise ValueError()
        exploitation_triage.write_receipt(
            output, exploitation_triage.read_receipt(source)
        )
    except Exception:
        print("Triage receipt export refused; no triage artifact produced.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("source", "output"):
        parser.add_argument(f"--{name}", required=True, type=Path)
    parser.add_argument("--triage-source", type=Path)
    parser.add_argument("--triage-output", type=Path)
    options = parser.parse_args()
    if (options.triage_source is None) != (options.triage_output is None):
        parser.error("--triage-source and --triage-output are used together")
    try:
        if options.output.exists() or options.output.is_symlink():
            raise ValueError()
        receipt = read_receipt(options.source)
        write_receipt(options.output, receipt)
    except Exception:
        print("Failure receipt export refused; no diagnostic artifact produced.")
        return 1
    if options.triage_source is not None:
        export_triage(options.triage_source, options.triage_output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

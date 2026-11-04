#!/usr/bin/env python3
"""Export a validated private receipt, never arbitrary logs or model output."""

import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.core.failure_receipt import read_receipt, write_receipt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("source", "output"):
        parser.add_argument(f"--{name}", required=True, type=Path)
    options = parser.parse_args()
    try:
        if options.output.exists() or options.output.is_symlink():
            raise ValueError()
        receipt = read_receipt(options.source)
        write_receipt(options.output, receipt)
    except Exception:
        print("Failure receipt export refused; no diagnostic artifact produced.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Apply reviewed, fingerprint-bound corrections without calling a model."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def apply_correction(source: str, correction: dict) -> str:
    fingerprint = hashlib.sha256(source.encode()).hexdigest()
    if fingerprint == correction.get("corrected_sha256"):
        return source
    if fingerprint != correction["source_sha256"]:
        # Verify idempotence by reconstructing the exact authorized original.
        restored = source
        for item in reversed(correction["replacements"]):
            if restored.count(item["after"]) != 1:
                raise ValueError("Report fingerprint does not match correction")
            restored = restored.replace(item["after"], item["before"], 1)
        if hashlib.sha256(restored.encode()).hexdigest() == correction["source_sha256"]:
            return source
        raise ValueError("Report fingerprint does not match correction")
    result = source
    for item in correction["replacements"]:
        if not item["before"] or result.count(item["before"]) != 1:
            raise ValueError("Each correction must match exactly once")
        result = result.replace(item["before"], item["after"], 1)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("correction", type=Path)
    parser.add_argument("--report", type=Path, default=Path("index.md"))
    args = parser.parse_args()
    source = args.report.read_text()
    corrected = apply_correction(source, json.loads(args.correction.read_text()))
    # A correction is source-only; use build_site and the normal validation gate
    # before committing its public projections.
    if corrected != source:
        args.report.write_text(corrected)


if __name__ == "__main__":
    main()

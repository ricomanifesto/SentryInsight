#!/usr/bin/env python3
"""Fold exported triage receipts into a ledger and print bounds and a verdict.

Reads only local files: receipt JSON, published reports and optional plan.
Makes no network or model calls and prints counts, never article text.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.core import triage_accumulator as acc  # noqa: E402
from src.core.report_artifact import (  # noqa: E402
    ReportArtifactError,
    parse_report_artifact,
)


def receipt_paths(sources: list[Path]) -> list[Path]:
    paths: list[Path] = []
    for source in sources:
        if source.is_dir():
            paths.extend(sorted(source.rglob("*.json")))
        elif source.is_file():
            paths.append(source)
        else:
            raise acc.TriageAccumulatorError(f"Receipt path not found: {source}")
    return paths


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise acc.TriageAccumulatorError(f"Unreadable JSON: {path}") from exc


def published_hashes_from_reports(root: Path) -> set[str]:
    """Hash every Reporting link in the current and archived reports.

    ``current-findings.json`` carries CVE identifiers and counts but no links,
    so the current report's links are read from ``index.md``.
    """
    hashes: set[str] = set()
    for path in [root / "index.md", *sorted((root / "reports").glob("*.md"))]:
        if not path.is_file():
            continue
        try:
            artifact = parse_report_artifact(path.read_text(encoding="utf-8"))
        except ReportArtifactError as exc:
            raise acc.TriageAccumulatorError(f"Unparseable report: {path}") from exc
        for finding in artifact.findings:
            for reference in finding.reporting:
                digest = acc.published_url_sha256(reference.url)
                if digest is not None:
                    hashes.add(digest)
    return hashes


def write_ledger(path: Path, ledger: dict[str, Any], *, replace: bool) -> None:
    data = (json.dumps(ledger, sort_keys=True, indent=2) + "\n").encode("utf-8")
    if not replace:
        with path.open("xb") as stream:
            stream.write(data)
        return
    descriptor, temporary = tempfile.mkstemp(prefix=".triage-ledger-", dir=path.parent)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(data)
        os.replace(temporary, path)
    finally:
        Path(temporary).unlink(missing_ok=True)


def summary(joined: dict[str, Any], result: dict[str, Any]) -> dict[str, Any]:
    counts = {
        key: joined[key]
        for key in (
            "runs_decided",
            "runs_legacy_full",
            "runs_shadow",
            "runs_enabled",
            "positions_decided",
            "positions_unhashed",
            "positions_legacy_full",
            "unique_decided",
            "would_drop",
            "conflicting",
            "published",
            "published_unmatched",
            "cited",
            "cited_and_dropped",
        )
    }
    return {"counts": counts, "bounds": result}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipts", type=Path, nargs="+", required=True)
    parser.add_argument(
        "--published",
        type=Path,
        help="JSON list of published URL hashes (default: derive from reports)",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root holding index.md and reports/",
    )
    parser.add_argument("--plan", type=Path)
    parser.add_argument("--ledger", type=Path)
    parser.add_argument(
        "--update",
        action="store_true",
        help="Fold new receipts into an existing --ledger",
    )
    options = parser.parse_args(argv)
    if options.update and options.ledger is None:
        parser.error("--update requires --ledger")

    try:
        previous = None
        if options.ledger is not None and options.ledger.exists():
            if not options.update:
                raise acc.TriageAccumulatorError(
                    f"Ledger exists; pass --update to fold into it: {options.ledger}"
                )
            previous = acc.validate_ledger(load_json(options.ledger))
        receipts = [load_json(path) for path in receipt_paths(options.receipts)]
        ledger = acc.fold_receipts(receipts, previous)

        if options.published is not None:
            published = load_json(options.published)
            if not isinstance(published, list):
                raise acc.TriageAccumulatorError("--published must be a JSON list")
        else:
            published = sorted(published_hashes_from_reports(options.root))
        joined = acc.join_must_keep(ledger, published)
        plan = load_json(options.plan) if options.plan is not None else None
        result = acc.bounds(joined, plan)

        if options.ledger is not None:
            write_ledger(options.ledger, ledger, replace=previous is not None)
    except (acc.TriageAccumulatorError, FileExistsError) as exc:
        print(f"accumulate_triage: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(summary(joined, result), sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

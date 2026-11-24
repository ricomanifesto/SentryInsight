#!/usr/bin/env python3
"""Export a validated private receipt, never arbitrary logs or model output."""

import argparse
import os
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.core.failure_receipt import read_receipt, write_receipt
from src.core import exploitation_triage


def format_attempts_summary(receipt: dict) -> str:
    """Format bounded attempt and degradation lines for the GitHub step summary."""
    attempts = receipt.get("attempts") or []
    dropped = receipt.get("dropped_findings") or []
    if not attempts and not dropped:
        return ""
    lines = ["### Generation Attempts", ""]
    if attempts:
        lines.extend(
            [
                "| Attempt | Kind | Class | Rule | Finding | Field | Outcome |",
                "| --- | --- | --- | --- | --- | --- | --- |",
            ]
        )
        for item in attempts:
            lines.append(
                f"| {item['attempt']} | `{item['kind']}` | "
                f"`{item['failure_class'] or '-'}` | `{item['rule'] or '-'}` | "
                f"{item['finding_index'] if item['finding_index'] is not None else '-'} | "
                f"`{item['field'] or '-'}` | `{item['outcome']}` |"
            )
    if dropped:
        lines.extend(["", "#### Degraded Findings Omitted", ""])
        for entry in dropped:
            field_part = f" on `{entry['field']}`" if entry.get("field") else ""
            lines.append(
                f"- Finding #{entry['finding_index']}: `{entry['rule']}`{field_part} "
                f"after {entry['repair_attempts']} repair attempt(s)"
            )
    return "\n".join(lines) + "\n"


def append_step_summary(receipt: dict) -> None:
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY", "").strip()
    if not summary_path:
        return
    markdown = format_attempts_summary(receipt)
    if not markdown:
        return
    target = Path(summary_path)
    if target.is_symlink():
        return
    with target.open("a", encoding="utf-8") as stream:
        stream.write("\n" + markdown)


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
        append_step_summary(receipt)
    except Exception:
        print("Failure receipt export refused; no diagnostic artifact produced.")
        return 1
    if options.triage_source is not None:
        export_triage(options.triage_source, options.triage_output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

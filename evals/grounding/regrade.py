"""Regrade a completed saved v1 run without models, gate execution or export."""

import os

# CLI use is local-only, including when telemetry environment variables exist.
if __name__ == "__main__":
    os.environ["OTEL_SDK_DISABLED"] = "true"
    os.environ["LOGFIRE_SEND_TO_LOGFIRE"] = "false"
    os.environ["LANGSMITH_TRACING"] = "false"
    os.environ["LANGCHAIN_TRACING_V2"] = "false"

import argparse  # noqa: E402
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

from .dataset import digest, load_cases
from .grading import GRADER_METRICS, grade_report
from .grading_v2 import Check, GRADER_VERSION, ReportGrade, grade_report_v2

ROOT = Path(__file__).resolve().parents[2]
INPUT_FILES = ("manifest.json", "graded.json", "trials.jsonl")
TRIAL_FIELDS = {
    "trial_id",
    "case",
    "variant",
    "repetition",
    "error_type",
    "duration_seconds",
    "input_sha256",
    "report",
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def grader_snapshot() -> dict[str, str]:
    paths = [ROOT / "pyproject.toml", ROOT / "uv.lock"]
    for directory in ("src", "evals"):
        paths.extend((ROOT / directory).rglob("*.py"))
    paths.extend((ROOT / "evals/grounding/data").glob("*.json"))
    return {str(p.relative_to(ROOT)): sha256(p.read_bytes()) for p in sorted(paths)}


def indexed(rows: list[dict]) -> dict[str, dict]:
    result = {row["trial_id"]: row for row in rows}
    if len(result) != len(rows):
        raise ValueError("Duplicate trial identity")
    return result


def summarize(rows: list[dict]) -> dict:
    return {
        "planned": len(rows),
        "execution_errors": sum(bool(row["original"]["error_type"]) for row in rows),
        "field_pass_trials": sum(row["field_pass"] for row in rows),
        "narrative_review_required": sum(
            not row["original"]["error_type"] for row in rows
        ),
        "checks": {
            name: {
                **{
                    state: sum(
                        row["grade"]["checks"][name]["state"] == state for row in rows
                    )
                    for state in ("pass", "fail", "not_evaluated")
                },
                "planned": len(rows),
            }
            for name in GRADER_METRICS
        },
    }


def regrade_saved_run(saved: Path, output: Path) -> dict:
    saved, output = saved.resolve(), output.resolve()
    if output.exists():
        raise FileExistsError(output)
    if output.is_relative_to(saved):
        raise ValueError("Regrade output must be outside the original run")
    inputs = {name: (saved / name).read_bytes() for name in INPUT_FILES}
    manifest = json.loads(inputs["manifest.json"])
    rows = json.loads(inputs["graded.json"])
    trials = [json.loads(line) for line in inputs["trials.jsonl"].splitlines()]
    snapshot = grader_snapshot()
    if manifest.get("complete") is not True or manifest.get("schema_version") != 1:
        raise ValueError("Require a completed schema-v1 run")
    # The frozen source, gold and v1 grading contract must still be reproducible.
    for name in (
        "evals/grounding/data/sources.json",
        "evals/grounding/data/answers.json",
        "evals/grounding/dataset.py",
        "evals/grounding/grading.py",
    ):
        if manifest["source_files"].get(name) != snapshot[name]:
            raise ValueError(f"Frozen source mismatch: {name}")
    by_id, raw_by_id = indexed(rows), indexed(trials)
    plan = manifest["trial_ids"]
    if (
        len(set(plan)) != len(plan)
        or manifest["planned"] != len(plan)
        or set(plan) != set(by_id)
        or set(plan) != set(raw_by_id)
        or not plan
    ):
        raise ValueError("Incomplete or inconsistent trial plan")
    cases = {case.name: case for case in load_cases()}
    selected = list(dict.fromkeys(by_id[trial_id]["case"] for trial_id in plan))
    if set(selected) - cases.keys():
        raise ValueError("Unknown source case")
    if (
        digest([cases[name].model_dump() for name in selected])
        != manifest["dataset_sha256"]
    ):
        raise ValueError("Dataset digest mismatch")
    grades: list[dict] = []
    for trial_id in plan:
        row, raw = by_id[trial_id], raw_by_id[trial_id]
        case = cases[row["case"]]
        if set(raw) != TRIAL_FIELDS or any(
            row[key] != raw[key] for key in TRIAL_FIELDS
        ):
            raise ValueError("Saved grade and raw trial disagree")
        if row["variant"] not in {"baseline", "checklist"} or row[
            "repetition"
        ] not in range(1, 4):
            raise ValueError("Invalid trial configuration")
        task_input = case.task_input(row["variant"], row["repetition"])
        if (
            trial_id != f"{case.name}/{row['variant']}/{row['repetition']}"
            or row["input_sha256"] != digest(task_input.model_dump())
            or row["split"] != case.split
        ):
            raise ValueError("Trial identity or input digest mismatch")
        if row["error_type"]:
            if row["checks"] is not None or row["gate"] is not None or row["report"]:
                raise ValueError("Execution error has incompatible report or grades")
            skipped = Check(
                state="not_evaluated", reason="Model execution failed in original run."
            )
            grade = ReportGrade(
                checks={name: skipped for name in GRADER_METRICS},
                narrative_review=skipped,
                additional_narrative_cves=[],
            )
        else:
            if not isinstance(row["report"], str) or not row["report"].strip():
                raise ValueError("Missing successful report")
            if row["checks"] != grade_report(case, row["report"]):
                raise ValueError("Original v1 grades are not reproducible")
            grade = grade_report_v2(case, row["report"])
        grades.append(
            {
                "trial_id": trial_id,
                "original": row,
                "report_sha256": sha256(row["report"].encode()),
                "grade": grade.model_dump(),
                "field_pass": grade.field_pass,
            }
        )
    summary = {
        **summarize(grades),
        "by_variant": {
            variant: summarize(
                [row for row in grades if row["original"]["variant"] == variant]
            )
            for variant in sorted({row["original"]["variant"] for row in grades})
        },
        "limitations": [
            "Regrading existing outputs is not a new model experiment or production validation.",
            "Field scores do not grade narrative correctness; all prose requires source review.",
            "Previously inspected holdouts are development evidence for subsequent tuning.",
            "Original production-gate receipts are retained, not rerun or independently certified.",
        ],
    }
    receipt = {
        "schema_version": 2,
        "grader_version": GRADER_VERSION,
        "started_at": datetime.now(timezone.utc).isoformat(),
        "input_files": {name: sha256(data) for name, data in inputs.items()},
        "grader_files": snapshot,
        "original_commit": manifest["commit"],
        "planned": len(plan),
        "model_calls": 0,
        "telemetry_export": False,
        "complete": False,
    }
    output.mkdir(parents=True, exist_ok=False)

    def write(name, data):
        (output / name).write_text(json.dumps(data, indent=2) + "\n")

    write("manifest.json", receipt)
    write("graded.json", grades)
    write("summary.json", summary)
    if grader_snapshot() != snapshot or any(
        (saved / name).read_bytes() != data for name, data in inputs.items()
    ):
        raise RuntimeError("Source or input changed; regrade remains incomplete")
    receipt["complete"] = True
    receipt["finished_at"] = datetime.now(timezone.utc).isoformat()
    write("manifest.json", receipt)
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(regrade_saved_run(args.input, args.output), indent=2))


if __name__ == "__main__":
    main()

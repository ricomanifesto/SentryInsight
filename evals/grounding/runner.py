"""Local Pydantic Evals execution with complete trial accounting."""

import asyncio
import hashlib
import platform
from datetime import datetime, timezone
from importlib.metadata import version
import json
import subprocess
import time
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Awaitable, Callable

from pydantic_evals import Case, Dataset
from pydantic_evals.evaluators import Evaluator, EvaluatorContext

from src.core.analyze import (
    collect_exploitation_relevant_prompt_cves,
    format_article_summary,
)
from src.core.article_policy import contains_virtual_event_tag
from src.core.finding_evidence import EvidenceError, validate_finding_evidence
from src.core.report_artifact import ReportArtifactError, parse_report_artifact
from src.core.report_validation import (
    remove_source_attribution_section,
    split_overlong_executive_summary,
    validate_report_content,
)
from src.core.reporting import (
    ReportingGroundingError,
    build_reporting_catalog,
    resolve_reporting_keys,
)

from .dataset import SourceCase, TaskInput, digest
from .grading import grade_report

ROOT = Path(__file__).resolve().parents[2]


def source_snapshot() -> dict[str, str]:
    files = [ROOT / "pyproject.toml", ROOT / "uv.lock"]
    for directory in ("src", "evals"):
        files.extend((ROOT / directory).rglob("*.py"))
    files.extend((ROOT / "evals/grounding/data").glob("*.json"))
    return {
        str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(files)
    }


Task = Callable[[TaskInput], Awaitable[str]]


@dataclass
class TrialOutput:
    report: str = ""
    error_type: str | None = None


def gate_result(inputs: TaskInput, report: str) -> dict[str, Any]:
    """Replay validation stages only; never write or publish a product report."""
    articles = [a.model_dump() for a in inputs.articles]
    catalog = build_reporting_catalog(articles)
    expected_cves = {
        cve
        for article in articles
        for cve in collect_exploitation_relevant_prompt_cves(
            format_article_summary(article)
        )
    }
    if contains_virtual_event_tag(report):
        return {"passed": False, "code": "virtual_event_promotion"}
    report = split_overlong_executive_summary(remove_source_attribution_section(report))
    try:
        validate_finding_evidence(report, catalog)
        resolved = resolve_reporting_keys(report, catalog)
    except (EvidenceError, ReportingGroundingError) as exc:
        return {"passed": False, "code": getattr(exc, "code", "reporting_identity")}
    issues = validate_report_content(resolved, expected_cves=expected_cves)
    if issues:
        return {"passed": False, "code": issues[0].code}
    header = (
        "---\nschema_version: 3\nreport_date: 2026-01-01\n"
        "generated_at: 2026-01-01T00:00:00Z\n"
        "digest_issue_url: https://ricomanifesto.github.io/"
        "SentryDigest/archive/2026-01-01/\n---\n"
    )
    try:
        parse_report_artifact(header + resolved)
    except ReportArtifactError:
        return {"passed": False, "code": "artifact_invalid"}
    return {"passed": True, "code": None}


@dataclass
class FieldChecks(Evaluator[TaskInput, TrialOutput, SourceCase]):
    def evaluate(self, ctx: EvaluatorContext[TaskInput, TrialOutput, SourceCase]):
        if ctx.output.error_type:
            return {"execution_ok": False}
        assert ctx.metadata is not None
        return {"execution_ok": True, **grade_report(ctx.metadata, ctx.output.report)}


async def run_evaluation(
    cases: list[SourceCase],
    *,
    task: Task,
    output: Path,
    repetitions: int = 3,
    concurrency: int = 2,
    variants: tuple[str, ...] = ("baseline", "checklist"),
    provenance: dict[str, Any] | None = None,
) -> dict[str, Any]:
    if not cases or not 1 <= repetitions <= 3 or not 1 <= concurrency <= 2:
        raise ValueError("Require cases, 1-3 repetitions, and 1-2 concurrent trials")
    if not variants or len(set(variants)) != len(variants):
        raise ValueError("Require unique variants")
    plan = [
        Case(
            name=f"{case.name}/{variant}/{rep}",
            inputs=case.task_input(variant, rep),
            metadata=case,
        )
        for rep in range(1, repetitions + 1)
        for case in cases
        for variant in variants
    ]
    output.mkdir(parents=True, exist_ok=False)
    commit = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()
    dirty = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()
    snapshot = source_snapshot()
    manifest = {
        "started_at": datetime.now(timezone.utc).isoformat(),
        "working_tree_dirty": bool(dirty),
        "source_files": snapshot,
        "python_version": platform.python_version(),
        "dependencies": {
            name: version(name) for name in ("pydantic-evals", "pydantic", "httpx")
        },
        "schema_version": 1,
        "planned": len(plan),
        "commit": commit,
        "dataset_sha256": digest([case.model_dump() for case in cases]),
        "trial_ids": [case.name for case in plan],
        "repetitions": repetitions,
        "concurrency": concurrency,
        "provenance": provenance or {},
        "complete": False,
    }
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    recorded: dict[str, dict[str, Any]] = {}

    async def guarded(inputs: TaskInput) -> TrialOutput:
        started = time.monotonic()
        trial_id = f"{inputs.name}/{inputs.variant}/{inputs.repetition}"
        try:
            report = await asyncio.wait_for(task(inputs), timeout=240)
            if not isinstance(report, str) or not report.strip():
                raise ValueError("Empty or invalid report")
            result = TrialOutput(report=report)
        except Exception as exc:
            # Never record transport exception messages, URLs, or credentials.
            result = TrialOutput(error_type=type(exc).__name__)
        recorded[trial_id] = {
            "trial_id": trial_id,
            "case": inputs.name,
            "variant": inputs.variant,
            "repetition": inputs.repetition,
            "error_type": result.error_type,
            "duration_seconds": round(time.monotonic() - started, 4),
            "input_sha256": digest(inputs.model_dump()),
            "report": result.report,
        }
        # Persist immediately so interruption cannot erase completed work.
        with (output / "trials.jsonl").open("a") as stream:
            stream.write(json.dumps(recorded[trial_id], sort_keys=True) + "\n")
        return result

    dataset = Dataset(
        name="sentryinsight-grounding-v1",
        cases=plan,
        evaluators=[FieldChecks()],
    )
    evaluated = await dataset.evaluate(
        guarded,
        max_concurrency=concurrency,
        progress=False,
    )
    if evaluated.failures or evaluated.report_evaluator_failures:
        raise RuntimeError("Evaluation framework failed; manifest remains incomplete")
    by_name = {case.name: case for case in cases}
    rows = []
    for trial in evaluated.cases:
        if trial.evaluator_failures:
            raise RuntimeError("Grading failed; manifest remains incomplete")
        row = recorded[trial.name]
        case = by_name[row["case"]]
        row["split"] = case.split
        row["checks"] = None
        row["gate"] = None
        if not row["error_type"]:
            row["checks"] = grade_report(case, row["report"])
            row["gate"] = gate_result(trial.inputs, row["report"])
        rows.append(row)
    if len(rows) != len(plan) or len(recorded) != len(plan):
        raise RuntimeError("Missing trial results; manifest remains incomplete")

    def summarize(selected):
        completed = [row for row in selected if not row["error_type"]]
        counters = Counter()
        for row in completed:
            for metric, passed in row["checks"].items():
                counters[metric] += int(passed)
        return {
            "planned": len(selected),
            "recorded": len(selected),
            "completed": len(completed),
            "execution_errors": len(selected) - len(completed),
            "field_pass_trials": sum(all(row["checks"].values()) for row in completed),
            "field_checks": {
                key: {
                    "passed": value,
                    "evaluated": len(completed),
                    "planned": len(selected),
                }
                for key, value in sorted(counters.items())
            },
            "gate_acceptance_disagreements": sum(
                row["gate"]["passed"] and not all(row["checks"].values())
                for row in completed
            ),
            "gate_rejection_disagreements": sum(
                not row["gate"]["passed"] and all(row["checks"].values())
                for row in completed
            ),
        }

    summary = {
        **summarize(rows),
        "by_variant_and_split": {
            f"{variant}/{split}": summarize(
                [
                    row
                    for row in rows
                    if row["variant"] == variant and row["split"] == split
                ]
            )
            for variant in variants
            for split in sorted({case.split for case in cases})
        },
        "limitations": [
            "Synthetic fixtures; review status is recorded in the dataset.",
            "Exact field checks do not establish correctness of arbitrary prose.",
            "Rejection candidates require manual review; gate replay does not publish.",
            "Repeated trials are not independent source cases or population estimates.",
        ],
    }
    (output / "graded.json").write_text(json.dumps(rows, indent=2) + "\n")
    (output / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    if source_snapshot() != snapshot:
        raise RuntimeError(
            "Source changed during evaluation; manifest remains incomplete"
        )
    manifest["finished_at"] = datetime.now(timezone.utc).isoformat()
    manifest["complete"] = True
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    return summary

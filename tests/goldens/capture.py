"""Frozen derivation goldens for behavior-preserving refactors.

The committed ``derivations.json`` holds SHA-256 digests of the review packet,
plan identity and generation prompt for every evaluation case under both
review policies, the resolved report and parsed artifact (or failure stage and
code) for each case's reference report, and the parsed artifact of each frozen
archived report. The frozen archive set is the names already in the golden:
normal generation keeps adding dated reports under ``reports/``, and those new
files are not fixtures. Regenerate only for an intended contract change:

    PYTHONPATH=.:tests uv run --frozen python -B tests/goldens/capture.py --write

``--write`` keeps the frozen archive set; ``--refreeze-archives`` replaces it
with every report currently under ``reports/``.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[2]
GOLDEN = Path(__file__).with_name("derivations.json")
sys.path[:0] = [str(ROOT), str(ROOT / "tests")]

from evals.grounding.dataset import load_cases  # noqa: E402
from goldens.trace_plugin import _plain  # noqa: E402
from review_fixtures import reviewed_analysis  # noqa: E402
from src.core.exploitation_prompt import build_exploitation_prompt  # noqa: E402
from src.core.report_artifact import parse_report_artifact  # noqa: E402
from src.core.reporting import serialize_reporting_catalog  # noqa: E402
from src.core.reviewed_report import resolve_reviewed_analysis  # noqa: E402
from src.core.source_review import packet_bytes, prepare_source_review  # noqa: E402


def sha256(value: str | bytes) -> str:
    data = value.encode() if isinstance(value, str) else value
    return hashlib.sha256(data).hexdigest()


def artifact_digest(source: str) -> str:
    return sha256(
        json.dumps(_plain(parse_report_artifact(source)), sort_keys=True, default=repr)
    )


def _resolution(result: dict[str, Any], *, advisory: bool) -> dict[str, Any]:
    stages: list[str] = []
    try:
        candidate = resolve_reviewed_analysis(
            result, on_stage=stages.append, advisory=advisory
        )
    except Exception as exc:  # the failure stage and code are the golden
        return {
            "stage": stages[-1] if stages else None,
            "error": type(exc).__name__,
            "code": getattr(exc, "code", None),
        }
    return {
        "source_sha256": sha256(candidate.source),
        "artifact_sha256": artifact_digest(candidate.source),
        "advisories": len(candidate.advisories),
    }


def capture_archives(reports: Path, names: Iterable[str]) -> dict[str, Any]:
    """Digest each named archived report; a missing frozen archive is an error."""
    return {
        name: {
            "markdown_sha256": sha256((reports / name).read_bytes()),
            "artifact_sha256": artifact_digest((reports / name).read_text()),
        }
        for name in sorted(names)
    }


def capture(archive_names: Iterable[str] | None = None) -> dict[str, Any]:
    """Capture every golden; ``archive_names`` None means every current report."""
    cases: dict[str, Any] = {}
    prompts: list[str] = []
    for case in load_cases():
        articles = [article.model_dump() for article in case.articles]
        entry: dict[str, Any] = {}
        for policy, advisory in (("strict", False), ("advisory", True)):
            plan = prepare_source_review(articles, advisory=advisory)
            prompt = build_exploitation_prompt(plan) if plan.eligible_keys else ""
            prompts.append(prompt)
            entry[policy] = {
                "plan_id": plan.packet["plan_id"],
                "packet_sha256": sha256(packet_bytes(plan.packet)),
                "prompt_sha256": sha256(prompt),
            }
        result, _ = reviewed_analysis(
            {
                "exploitation_report": case.reference_report,
                "reporting_sources": serialize_reporting_catalog(
                    prepare_source_review(articles).catalog
                ),
                "date": "2026-11-07",
                "generated_at": "2026-11-07T12:00:00Z",
            }
        )
        entry["reference_report"] = {
            "strict": _resolution(result, advisory=False),
            "advisory": _resolution(result, advisory=True),
        }
        cases[case.name] = entry
    reports = ROOT / "reports"
    if archive_names is None:
        archive_names = [path.name for path in reports.glob("*.md")]
    archive = capture_archives(reports, archive_names)
    return {
        "eval_cases": cases,
        "eval_prompt_set_sha256": sha256("".join(map(sha256, prompts))),
        "archived_reports": archive,
    }


if __name__ == "__main__":
    frozen = None
    if "--refreeze-archives" not in sys.argv and GOLDEN.exists():
        frozen = json.loads(GOLDEN.read_text())["archived_reports"]
    data = json.dumps(capture(frozen), indent=2, sort_keys=True) + "\n"
    if "--write" in sys.argv:
        GOLDEN.write_text(data)
    else:
        sys.stdout.write(data)

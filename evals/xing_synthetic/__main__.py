"""Explicit CLI: public tokenizer setup, offline calibration, or guarded live run."""

import os

# Before application imports in the isolated CLI, including calibration.
# Importing testable guards must not mutate another caller's environment.
if __name__ == "__main__":
    os.environ["OTEL_SDK_DISABLED"] = "true"
    os.environ["LOGFIRE_SEND_TO_LOGFIRE"] = "false"
    os.environ["LANGSMITH_TRACING"] = "false"
    os.environ["LANGCHAIN_TRACING_V2"] = "false"

import argparse  # noqa: E402
import asyncio  # noqa: E402
import hashlib  # noqa: E402
import json  # noqa: E402
import logging  # noqa: E402
from pathlib import Path  # noqa: E402
import re  # noqa: E402
import subprocess  # noqa: E402
import urllib.request  # noqa: E402
from typing import Any  # noqa: E402

from .fixtures import evaluate, prepare_cases, reference_report  # noqa: E402
from .policy import PilotError, TOKENIZER_SHA, TOKENIZER_URL, TokenBudget  # noqa: E402
from .runner import run_cases  # noqa: E402

REPO = Path(__file__).resolve().parents[2]


def download_tokenizer(path: Path) -> None:
    if os.getenv("OPENROUTER_API_KEY"):
        raise PilotError("secret_in_setup_step")
    if path.exists():
        TokenBudget(path)
        return
    # This fixed public download has no authentication. Only a checked data
    # asset is parsed; no remote Python/transformers trust_remote_code is used.
    with urllib.request.urlopen(TOKENIZER_URL, timeout=60) as response:
        data = response.read(4 * 1024 * 1024)
    if hashlib.sha256(data).hexdigest() != TOKENIZER_SHA:
        raise PilotError("tokenizer_identity")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as stream:
        stream.write(data)


def check_live_environment(expected_sha: str, output: Path) -> None:
    expected = {
        "GITHUB_ACTIONS": "true",
        "GITHUB_REPOSITORY": "ricomanifesto/SentryInsight",
        "GITHUB_EVENT_NAME": "workflow_dispatch",
        "GITHUB_REF": "refs/heads/main",
        "GITHUB_RUN_ATTEMPT": "1",
    }
    if any(os.getenv(k) != value for k, value in expected.items()):
        raise PilotError("execution_context")
    if not re.fullmatch(r"[0-9a-f]{40}", expected_sha):
        raise PilotError("candidate_identity")
    head = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=REPO, text=True
    ).strip()
    dirty = subprocess.check_output(
        ["git", "status", "--porcelain"], cwd=REPO, text=True
    )
    if head != expected_sha or dirty:
        raise PilotError("candidate_identity")
    temp = os.getenv("RUNNER_TEMP")
    if not temp or not output.resolve().is_relative_to(Path(temp).resolve()):
        raise PilotError("output_location")
    if output.resolve().is_relative_to(REPO.resolve()):
        raise PilotError("production_output_location")
    if os.getenv("SENTRYINSIGHT_MODEL"):
        raise PilotError("model_override")


async def execute(args) -> dict:
    if args.mode == "tokenizer":
        download_tokenizer(args.tokenizer)
        return {"tokenizer_sha256": TOKENIZER_SHA, "model_requests": 0}
    if args.mode == "run":
        if not args.live or args.output is None:
            raise PilotError("live_authorization_missing")
        check_live_environment(args.expected_commit or "", args.output)
    elif args.live or args.review_outputs or os.getenv("OPENROUTER_API_KEY"):
        raise PilotError("invalid_offline_mode")
    cases = await prepare_cases(TokenBudget(args.tokenizer))
    if args.mode == "calibrate":
        rows: list[dict[str, Any]] = []
        for case in cases:
            _, checks = evaluate(case, reference_report(case))
            rows.append(
                {
                    "case": case.name,
                    "checks": checks,
                    "input_tokens_with_framing_reserve": case.input_tokens_with_reserve,
                    "request_sha256": case.request_sha256,
                }
            )
        if not all(all(row["checks"].values()) for row in rows):
            raise PilotError("calibration_failed")
        return {"mode": "offline_calibration", "model_requests": 0, "trials": rows}
    return await run_cases(
        cases,
        secret=os.getenv("OPENROUTER_API_KEY", ""),
        output=args.output,
        candidate_sha=args.expected_commit,
        review_outputs=args.review_outputs,
    )


def main() -> int:
    # Suppress provider/application logs only in this isolated CLI process.
    # Importing environment guards in tests must not change global logging.
    logging.disable(logging.CRITICAL)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("tokenizer", "calibrate", "run"))
    parser.add_argument("--tokenizer", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--expected-commit")
    parser.add_argument("--live", action="store_true")
    parser.add_argument("--review-outputs", action="store_true")
    try:
        result = asyncio.run(execute(parser.parse_args()))
        print(json.dumps(result, allow_nan=False))
        return 0 if result.get("complete", True) else 2
    except Exception:
        # Detailed raw exceptions may contain paths, data or transport context.
        print(json.dumps({"outcome": "preflight_failed", "complete": False}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

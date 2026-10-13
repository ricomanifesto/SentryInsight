"""Run in a fresh, uninstrumented process. No telemetry configuration or export."""

# Set before importing the application or evaluation SDK.
import os

os.environ["OTEL_SDK_DISABLED"] = "true"
os.environ["LOGFIRE_SEND_TO_LOGFIRE"] = "false"
os.environ["LANGSMITH_TRACING"] = "false"
os.environ["LANGCHAIN_TRACING_V2"] = "false"

import argparse  # noqa: E402
import asyncio  # noqa: E402
import json  # noqa: E402
from pathlib import Path  # noqa: E402

from .dataset import load_cases  # noqa: E402
from .runner import run_evaluation  # noqa: E402


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["calibrate", "run"])
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--split", choices=["development", "holdout", "all"], default="development"
    )
    parser.add_argument("--limit", type=int)
    parser.add_argument("--repetitions", type=int, default=1)
    parser.add_argument("--concurrency", type=int, default=2)
    parser.add_argument("--model")
    parser.add_argument(
        "--live", action="store_true", help="Permit the named free model calls"
    )
    args = parser.parse_args()
    cases = [c for c in load_cases() if args.split == "all" or c.split == args.split]
    if args.limit is not None:
        if args.limit < 1:
            parser.error("--limit must be positive")
        cases = cases[: args.limit]
    if args.mode == "calibrate":

        async def task(inputs):
            return next(
                case.reference_report for case in cases if case.name == inputs.name
            )

        variants = ("baseline",)
        provenance = {"mode": "calibration_fixture_replay", "model_calls": 0}
    else:
        if not args.live or not args.model:
            parser.error(
                "Model runs require --live and --model; no implicit provider calls"
            )
        from .model_task import ModelTask

        task = ModelTask(
            model=args.model,
            receipts=args.output / "model-receipts.jsonl",
            max_requests=len(cases) * 2 * args.repetitions,
        )
        variants = ("baseline", "checklist")
        provenance = {"mode": "model", "model": args.model, "price_ceiling_usd": 0}
    summary = asyncio.run(
        run_evaluation(
            cases,
            task=task,
            output=args.output,
            repetitions=args.repetitions,
            concurrency=args.concurrency,
            variants=variants,
            provenance=provenance,
        )
    )
    print(json.dumps(summary, indent=2))
    return 2 if summary["execution_errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())

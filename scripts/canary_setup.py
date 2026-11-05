#!/usr/bin/env python3
"""Consume the same fixed setup clock; the artifact gate never sends a model."""

import asyncio
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.canary_deadline import CONTEXT, clock_path, load_clock  # noqa: E402


async def prepare_setup():
    from scripts.execute_full_feed_canary import DATE, worker

    context = {name: os.environ.get(name, "") for name in CONTEXT}
    budget = load_clock(clock_path(), context, DATE)
    value = await worker(
        {
            "mode": "setup",
            "feed_file": str(clock_path().parent / "sentry-canary-feed.xml"),
        },
        budget.phase("setup"),
    )
    if value != {"calibration_passed": True}:
        raise ValueError("Closed setup refused")
    budget.before_reserve()


def artifact_gate():
    from scripts.execute_full_feed_canary import DATE

    context = {name: os.environ.get(name, "") for name in CONTEXT}
    budget = load_clock(clock_path(), context, DATE)
    budget.gate(60)
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as stream:
            stream.write("retain=true\n")


def main():
    try:
        if sys.argv[1:] == ["--artifact-gate"]:
            artifact_gate()
        elif not sys.argv[1:]:
            asyncio.run(prepare_setup())
        else:
            raise ValueError("Closed setup refused")
    except BaseException:
        print('{"setup":"refused"}')
        return 1
    print('{"setup":"verified"}')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

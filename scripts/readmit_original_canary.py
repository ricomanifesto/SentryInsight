#!/usr/bin/env python3
"""Bounded NO-MODEL operator wrapper; no provider secret is read or inherited."""

import argparse
import asyncio
import json
import os
import re
from pathlib import Path
import shutil
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.canary_deadline import CONTEXT, PhaseDeadline  # noqa: E402
from scripts.canary_process import run_private  # noqa: E402


async def run(args):
    from scripts.rehearse_full_feed_canary import environment, decode_response

    if (
        os.environ.get("RUNNER_DEBUG") == "1"
        or os.environ.get("ACTIONS_STEP_DEBUG", "").casefold() == "true"
    ):
        raise ValueError("Original readmission refused")

    node = shutil.which("node")
    if node is None:
        raise ValueError("Original readmission refused")
    child = environment()
    child["GIT_ALLOW_PROTOCOL"] = "https"
    child.update({key: os.environ.get(key, "") for key in CONTEXT})
    raw = await run_private(
        [
            node,
            str(ROOT / "scripts/readmit_original_canary.cjs"),
            "--expected-commit",
            args.expected_commit,
            "--expected-readmission",
            args.expected_readmission,
            "--readmit-original",
        ],
        b"",
        PhaseDeadline(time.monotonic_ns() + 90_000_000_000),
        env=child,
        cwd=ROOT,
        limit=2048,
    )
    value = decode_response(raw)
    if (
        type(value) is not dict
        or set(value)
        != {
            "outcome",
            "originalRun",
            "priorHistorySha256",
            "recordsSha256",
            "priorTip",
            "committedTip",
        }
        or value["outcome"] != "readmitted"
        or value["originalRun"] != "42022367409"
        or value["priorTip"] != "b1d9eedc0d54eacad63fb86e9d24e495a0bdee27"
        or any(
            type(value[key]) is not str
            or re.fullmatch("[a-f0-9]{64}", value[key]) is None
            for key in ("priorHistorySha256", "recordsSha256")
        )
        or type(value["committedTip"]) is not str
        or re.fullmatch("[a-f0-9]{40}", value["committedTip"]) is None
    ):
        raise ValueError("Original readmission refused")
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--expected-commit", required=True)
    parser.add_argument("--expected-readmission", required=True)
    args = parser.parse_args()
    try:
        value = asyncio.run(run(args))
    except BaseException:
        print('{"outcome":"readmission_held_or_unknown"}')
        return 1
    print(json.dumps(value, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""One anonymous fixed public run read; no key, admission or model operation."""

import asyncio
import http.client
import json
import os
from pathlib import Path
import ssl
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.canary_deadline import (  # noqa: E402
    CONTEXT,
    PhaseDeadline,
    anchor_run,
    clock_path,
    context_identity,
    save_clock,
    strict_json,
)
from scripts.canary_process import run_private  # noqa: E402


def public_run(context):
    context_identity(context)
    connection = http.client.HTTPSConnection(
        "api.github.com", timeout=15, context=ssl.create_default_context()
    )
    try:
        connection.request(
            "GET",
            "/repos/ricomanifesto/SentryInsight/actions/runs/"
            + context["GITHUB_RUN_ID"],
            headers={
                "Accept": "application/vnd.github+json",
                "Accept-Encoding": "identity",
                "User-Agent": "SentryInsight-closed-clock",
            },
        )
        response = connection.getresponse()
        if response.status != 200 or response.getheader("Content-Encoding") not in (
            None,
            "identity",
        ):
            raise ValueError("Closed clock refused")
        raw = response.read(131073)
        if len(raw) > 131072:
            raise ValueError("Closed clock refused")
        value = strict_json(raw)
        return {
            key: value.get(key)
            for key in (
                "id",
                "repository",
                "actor",
                "event",
                "head_sha",
                "head_branch",
                "workflow_id",
                "run_attempt",
                "status",
                "created_at",
            )
        }
    finally:
        connection.close()


async def establish():
    context = {key: os.environ.get(key, "") for key in CONTEXT}
    context_identity(context)
    raw = await run_private(
        [
            sys.executable,
            "-I",
            "-B",
            str(Path(__file__).resolve()),
            "--public-read-worker",
        ],
        json.dumps(context).encode(),
        PhaseDeadline(time.monotonic_ns() + 20_000_000_000),
        env={"PATH": os.defpath},
        cwd=ROOT,
        limit=131072,
    )
    from scripts.execute_full_feed_canary import DATE

    value = anchor_run(json.loads(raw), context, DATE)
    value.before_reserve()
    save_clock(clock_path(), value)


def main():
    try:
        if sys.argv[1:] == ["--public-read-worker"]:
            raw = sys.stdin.buffer.read(8193)
            if len(raw) > 8192:
                raise ValueError("Closed clock refused")
            print(json.dumps(public_run(strict_json(raw))))
        elif not sys.argv[1:]:
            asyncio.run(establish())
        else:
            raise ValueError("Closed clock refused")
    except BaseException:
        print('{"clock":"refused"}')
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Fixed closed host operations; private input/output pipes, never a live model."""

import asyncio
import base64
import json
import logging
import os
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


def packed(value):
    return {
        "pack": base64.b64encode(value.pack).decode(),
        "wire": base64.b64encode(value.wire).decode(),
        "metadata": value.metadata,
    }


def unpacked(value):
    from scripts.prepare_full_feed_canary import Prepared, require

    require(type(value) is dict and set(value) == {"pack", "wire", "metadata"})
    return Prepared(
        base64.b64decode(value["pack"], validate=True),
        base64.b64decode(value["wire"], validate=True),
        value["metadata"],
    )


async def act(value):
    from scripts.execute_full_feed_canary import Authority, promote_report, source_fence
    from scripts.prepare_full_feed_canary import (
        _prepare_owned,
        capture_environment,
        prepare,
        require,
    )
    from scripts.rehearse_full_feed_canary import ReplayPermit

    mode = value["mode"]
    if mode == "setup":
        require(set(value) == {"mode", "feed_file"})
        import httpx
        import tiktoken
        from scripts.prepare_full_feed_canary import FEED_URL, verify_feed
        from scripts.execute_full_feed_canary import bounded_get
        from scripts.rehearse_full_feed_canary import rehearse

        async with httpx.AsyncClient(
            trust_env=False, follow_redirects=False, timeout=15
        ) as client:
            feed = await bounded_get(client, FEED_URL)
        verify_feed(feed)
        Path(value["feed_file"]).write_bytes(feed)
        tiktoken.get_encoding("cl100k_base")
        result = await rehearse(
            feed, Path(value["feed_file"]).parent / "sentry-calibration"
        )
        require(result.get("host_validated") is True)
        return {"calibration_passed": True}
    if mode == "emit":
        require(set(value) == {"mode", "receipt", "result"})
        path = Path(value["receipt"])
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value["result"], sort_keys=True) + "\n")
        return {"recorded": True}
    if mode == "cleanup":
        require(set(value) == {"mode", "scratch"})
        path = Path(value["scratch"])
        require(
            path.is_absolute()
            and path.name.startswith("closed-sentry-canary-")
            and not path.is_symlink()
        )
        shutil.rmtree(path)
        return {"removed": True}
    if mode == "prepare":
        require(set(value) == {"mode", "feed", "scratch"})
        return packed(
            await prepare(
                base64.b64decode(value["feed"], validate=True), Path(value["scratch"])
            )
        )
    if mode == "replay":
        require(
            set(value)
            == {"mode", "feed", "output", "scratch", "response", "prepared", "permit"}
        )
        from scripts.rehearse_report_offline import (
            public_snapshot,
            compare_pages_package,
        )

        output, scratch = Path(value["output"]), Path(value["scratch"])
        output.mkdir()
        for relative in public_snapshot(ROOT):
            target = output / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / relative, target)
        with capture_environment(Path(os.environ["TIKTOKEN_CACHE_DIR"])):
            result = await _prepare_owned(
                base64.b64decode(value["feed"], validate=True),
                output,
                replay=base64.b64decode(value["response"], validate=True),
                expected=unpacked(value["prepared"]),
                attempt_budget=ReplayPermit(value["permit"]),
            )
            require(type(result) is dict)
            if result["host_validated"]:
                compare_pages_package(output, scratch)
        return result
    require(mode in {"source_fence", "publish"})
    require(
        set(value)
        == (
            {"mode", "approved"}
            if mode == "source_fence"
            else {"mode", "approved", "output", "scratch"}
        )
    )
    approved = Authority(**value["approved"])
    if mode == "source_fence":
        source_fence(approved)
        return {"verified": True}
    return {
        "commit": promote_report(
            Path(value["output"]), approved, Path(value["scratch"])
        )
    }


def main():
    logging.disable(logging.CRITICAL)
    try:
        from scripts.rehearse_full_feed_canary import decode_response

        raw = sys.stdin.buffer.read(8 * 1024 * 1024 + 1)
        if len(raw) > 8 * 1024 * 1024:
            raise ValueError("Closed worker refused")
        result = asyncio.run(act(decode_response(raw)))
        sys.stdout.write(json.dumps({"ok": result}, separators=(",", ":")))
    except BaseException:
        sys.stdout.write('{"error":"host_worker_refused"}')
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

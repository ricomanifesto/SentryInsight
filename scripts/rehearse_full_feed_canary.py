#!/usr/bin/env python3
"""Closed one-send full-feed rehearsal. There is deliberately no live mode."""

import argparse
import asyncio
from datetime import datetime, timezone
from decimal import Decimal, ROUND_CEILING
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.prepare_full_feed_canary import (  # noqa: E402
    Prepared,
    _prepare_owned,
    canonical,
    capture_environment,
    prepare,
    require,
)

DATE = "2026-11-05"
MODEL = "moonshotai/kimi-k3.1-pro"


def environment():
    """No credential, Python startup, proxy, exporter or Git auth inheritance."""
    return {
        "PATH": "/usr/bin:/bin:/opt/homebrew/bin",
        "GIT_CONFIG_GLOBAL": "/dev/null",
        "GIT_CONFIG_SYSTEM": "/dev/null",
        "GIT_ALLOW_PROTOCOL": "file",
        "GIT_TERMINAL_PROMPT": "0",
        "GIT_AUTHOR_NAME": "Offline Fixture",
        "GIT_AUTHOR_EMAIL": "offline@example.invalid",
        "GIT_COMMITTER_NAME": "Offline Fixture",
        "GIT_COMMITTER_EMAIL": "offline@example.invalid",
    }


class BudgetOwner:
    """A single process owns handles across real local-file Git CAS transitions."""

    def __init__(self, directory):
        node = shutil.which("node", path=environment()["PATH"])
        if node is None:
            raise ValueError("Closed canary refused")
        self.process = subprocess.Popen(
            [node, str(ROOT / "scripts/full_feed_canary_budget.cjs"), str(directory)],
            env=environment(),
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
        )
        self.blocked = False

    async def exchange(self, value):
        require(not self.blocked)
        try:
            if self.process.stdin is None or self.process.stdout is None:
                raise ValueError("Closed canary refused")
            self.process.stdin.write(canonical(value) + b"\n")
            self.process.stdin.flush()
            raw = await asyncio.wait_for(
                asyncio.to_thread(self.process.stdout.readline, 8193), 20
            )
            require(0 < len(raw) <= 8192 and raw.endswith(b"\n"))
            result = json.loads(raw)
            require(type(result) is dict and set(result) == {"ok"})
            return result["ok"]
        except BaseException:
            self.blocked = True
            raise ValueError("Closed canary refused") from None

    def close(self):
        if self.process.stdin is not None:
            self.process.stdin.close()
        try:
            self.process.wait(timeout=2)
        except subprocess.TimeoutExpired:
            self.process.kill()
            self.process.wait(timeout=2)
        if self.process.stdout is not None:
            self.process.stdout.close()


class ReplayPermit:
    """Reattach the one acknowledged token for offline replay, never issue one."""

    def __init__(self, value):
        require(
            type(value) is dict
            and set(value) == {"token", "attempt", "limit", "request_sha256"}
        )
        require(value["attempt"] == value["limit"] == 1)
        self.value = value
        self.used = False
        self.disposition = None

    async def reserve(self, request_sha256, limit):
        require(
            not self.used
            and limit == 1
            and request_sha256 == self.value["request_sha256"]
        )
        self.used = True
        return dict(self.value)

    async def finish(self, reservation, disposition, *, retry_after=0):
        require(
            self.used
            and reservation == self.value
            and self.disposition is None
            and retry_after == 0
        )
        self.disposition = disposition


def calibration(prepared):
    """Host-only positive control, never part of messages sent to the model."""
    pack = json.loads(prepared.pack)
    from src.core.analyze import prepare_source_review

    plan = prepare_source_review(pack["articles"])
    eligible = [row for row in plan.packet["sources"] if row["state"] == "eligible"]
    row = next(row for row in eligible if row["key"] == "source-b8bdafeefd72")
    cves = sorted({cve for row in eligible for cve in row["cves"]})
    return (
        "# Exploitation Report\n\n## Executive Summary\n\n"
        "The supplied feed reports that Zyxel patched a zero-day vulnerability. "
        "Other supplied reporting mentions "
        + (", ".join(cves) or "no CVE IDs")
        + ".\n\n"
        "## Active Exploitation Details\n\n### Zyxel GS1900 network switches\n"
        "- **Description**: A zero-day vulnerability in Zyxel network switches.\n"
        "- **Severity**: unknown\n- **Exploitation Status**: unknown\n- **Action**: monitor\n"
        "- **Reporting**: " + row["key"] + "\n"
        "- **Affected Versions**: Not stated in supplied sources.\n"
        "- **Exceptions**: Not stated in supplied sources.\n"
        "- **Recommended Actions**: Not stated in supplied sources.\n"
        "- **Vendor Links**: Not stated in supplied sources.\n\n"
        "## Affected Systems and Products\n\nZyxel GS1900 network switches.\n\n"
        "## Attack Vectors and Techniques\n\nNot stated in supplied sources.\n\n"
        "## Threat Actor Activities\n\nNot stated in supplied sources.\n"
    )


def complete_body(answer):
    return canonical(
        {
            "model": MODEL,
            "provider": "Moonshot AI",
            "service_tier": None,
            "choices": [{"finish_reason": "stop", "message": {"content": answer}}],
            "usage": {
                "prompt_tokens": 12000,
                "completion_tokens": 2000,
                "total_tokens": 14000,
                "completion_tokens_details": {"reasoning_tokens": 100},
                "cost": 0.044,
            },
        }
    )


def financial_receipt(raw):
    from src.core.model_route import validate_completion

    body = json.loads(raw, parse_float=Decimal)
    # Actual host validator receives ordinary decoded JSON separately below.
    validate_completion(json.loads(raw), MODEL, 32000)
    require(body.get("provider") in (None, "Moonshot AI"))
    usage = body["usage"]
    require(
        set(("prompt_tokens", "completion_tokens", "total_tokens", "cost"))
        <= set(usage)
    )
    cost = usage["cost"]
    require(type(cost) in (int, Decimal) and not isinstance(cost, bool))
    require(Decimal(cost).is_finite() and 0 <= cost <= Decimal("2.417152"))
    units = int((Decimal(cost) * 1000000).to_integral_value(rounding=ROUND_CEILING))
    prompt, completion, total = (
        usage[name] for name in ("prompt_tokens", "completion_tokens", "total_tokens")
    )
    reasoning = usage.get("completion_tokens_details", {}).get("reasoning_tokens")
    require(type(reasoning) is int and 0 <= reasoning <= completion)
    require(total == prompt + completion and units <= prompt * 2 + completion * 10)
    require(prompt <= 1048576 and completion <= 32000)
    return {
        "model": MODEL,
        "provider": body.get("provider"),
        "serviceTier": body.get("service_tier"),
        "promptTokens": prompt,
        "completionTokens": completion,
        "reasoningTokens": reasoning,
        "totalTokens": total,
        "costMicrousd": units,
        "costCoverage": "unknown",
    }


async def rehearse(raw, root, *, scenario="success", now=None):
    """All outbound responses are local synthetic calibration; no key is read."""
    require(
        scenario
        in {
            "success",
            "invalid_grounding",
            "missing_cost",
            "empty",
            "transport_unknown",
        }
    )
    root = Path(root).resolve()
    root.mkdir(parents=True, exist_ok=True)
    require(shutil.disk_usage(root).free >= 1024**3)
    instant = now or datetime.now(timezone.utc)
    require(instant.tzinfo is not None and instant.date().isoformat() == DATE)
    cache = Path(os.environ["TIKTOKEN_CACHE_DIR"])
    prepared = await prepare(raw, root / "capture")
    require(isinstance(prepared, Prepared))
    revision = (
        subprocess.run(
            ["/usr/bin/git", "rev-parse", "HEAD"],
            cwd=ROOT,
            env=environment(),
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            check=True,
            timeout=5,
        )
        .stdout.decode()
        .strip()
    )
    output = root / "artifacts"
    output.mkdir()
    from scripts.rehearse_report_offline import public_snapshot, compare_pages_package

    for relative in public_snapshot(ROOT):
        target = output / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / relative, target)
    before = public_snapshot(output)
    owner = BudgetOwner(root / "financial")
    physical_posts = 0
    receipt = None
    host = {"host_validated": False, "host_replay_requests": 0, "status": "failed"}
    package = None
    refused = None
    phase = "financial_begin"
    try:
        permit = await owner.exchange(
            {
                "operation": "begin",
                "revision": revision,
                "sourceSha256": prepared.metadata["source_pack_sha256"],
                "requestSha256": prepared.metadata["canonical_request_sha256"],
                "now": instant.isoformat(timespec="milliseconds").replace(
                    "+00:00", "Z"
                ),
            }
        )
        replay_permit = ReplayPermit(permit)
        with capture_environment(cache):
            import httpx

            answer = calibration(prepared)
            if scenario == "invalid_grounding":
                answer = answer.replace("source-b8bdafeefd72", "source-000000000000")
            if scenario == "empty":
                answer = ""
            response_body = complete_body(answer)
            if scenario == "missing_cost":
                value = json.loads(response_body)
                value["usage"].pop("cost")
                response_body = canonical(value)

            def mock_sender(request):
                nonlocal physical_posts
                require(physical_posts == 0 and bytes(request.content) == prepared.wire)
                require(
                    request.method == "POST"
                    and str(request.url)
                    == "https://openrouter.ai/api/v1/chat/completions"
                )
                outbound = "\n".join(
                    row["content"] for row in json.loads(request.content)["messages"]
                )
                require(not answer or answer not in outbound)
                physical_posts += 1
                if scenario == "transport_unknown":
                    raise httpx.ReadTimeout("Synthetic canary failure")

                class Body(httpx.AsyncByteStream):
                    async def __aiter__(self):
                        yield response_body

                return httpx.Response(200, stream=Body())

            # The closed current entry accepts ONLY this owned MockTransport.
            # A future real sender requires a separate exact release/admission gate.
            async with httpx.AsyncClient(
                transport=httpx.MockTransport(mock_sender),
                trust_env=False,
                follow_redirects=False,
                timeout=10,
            ) as client:
                phase = "mock_send"
                require((now or datetime.now(timezone.utc)).date().isoformat() == DATE)
                async with client.stream(
                    "POST",
                    "https://openrouter.ai/api/v1/chat/completions",
                    content=prepared.wire,
                    headers={
                        "Authorization": "Bearer offline-synthetic-key",
                        "Content-Type": "application/json",
                        "Accept-Encoding": "identity",
                    },
                ) as response:
                    require(
                        response.status_code == 200
                        and response.headers.get("content-encoding")
                        in (None, "identity")
                    )
                    chunks = bytearray()
                    async with asyncio.timeout(10):
                        async for chunk in response.aiter_raw():
                            require(len(chunks) + len(chunk) <= 2 * 1024 * 1024)
                            chunks.extend(chunk)
                    received = bytes(chunks)
            phase = "accounting"
            receipt = financial_receipt(received)
            phase = "host_replay"
            host = await _prepare_owned(
                raw,
                output,
                replay=received,
                expected=prepared,
                attempt_budget=replay_permit,
            )
            require(type(host) is dict)
            if host["host_validated"]:
                phase = "package"
                package = compare_pages_package(output, root)
            else:
                refused = "host_validation_refused"
    except BaseException:
        refused = "closed_check_refused"
    finally:
        try:
            finish = await owner.exchange({"operation": "finish", "receipt": receipt})
        finally:
            owner.close()
    after = public_snapshot(output)
    if not host["host_validated"]:
        require(after == before)
    coverage = None
    timestamp = None
    if host["host_validated"]:
        from src.core.report_artifact import parse_report_artifact

        artifact = parse_report_artifact((output / "index.md").read_text())
        if artifact.source_coverage is None:
            raise ValueError("Closed canary refused")
        coverage = artifact.source_coverage["counts"]
        require(artifact.generated_at <= datetime.now(timezone.utc))
        require(
            artifact.generated_at.date().isoformat() == DATE
            and artifact.report_date.isoformat() == DATE
        )
        timestamp = artifact.generated_at.isoformat()
    return {
        "schema_version": 1,
        "offline_only": True,
        "production_ready": False,
        "activation": "synthetic_only",
        "ledger": "disposable_local_file_remote",
        "code_commit": revision,
        "source": prepared.metadata,
        "mock_physical_posts": physical_posts,
        "host_replay_requests": host["host_replay_requests"],
        "host_validated": host["host_validated"],
        "host_diagnostic": host.get("diagnostic"),
        "scratch_promoted": after != before,
        "coverage_counts": coverage,
        "pages_package": package,
        "last_good_preserved": after == before,
        "published": False,
        "output_fate": "scratch_only_then_discard",
        "refusal": refused,
        "failure_phase": phase if refused else None,
        "generated_at": timestamp,
        **finish,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline-only", action="store_true", required=True)
    parser.add_argument("--feed-file", type=Path, required=True)
    args = parser.parse_args()
    try:
        with tempfile.TemporaryDirectory(
            prefix="sentry-full-feed-rehearsal-"
        ) as directory:
            result = asyncio.run(rehearse(args.feed_file.read_bytes(), Path(directory)))
        print(json.dumps(result, sort_keys=True))
    except BaseException:
        print('{"outcome":"refused","published":false,"external_requests":0}')
        raise SystemExit(1) from None


if __name__ == "__main__":
    main()

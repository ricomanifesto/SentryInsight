#!/usr/bin/env python3
"""Calibrate a fixed synthetic case; optionally make one unpublished trial call."""

# The command may run directly from any working directory.
# ruff: noqa: E402

import argparse
import asyncio
import hashlib
import json
import logging
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import httpx

from scripts.verify_report_generation import (
    MODEL_ID,
    MAX_OUTPUT_TOKENS,
    VerificationClient,
    verify_articles,
)

CASE = ROOT / "evals/nemotron_verification/case.json"
CASE_SHA256 = "2d8c314d1a5c5b6234ad8a0f7be2bb4c93668385c8135381d7c9aded83b02040"
TOKENIZER_URL = (
    "https://openaipublic.blob.core.windows.net/encodings/cl100k_base.tiktoken"
)
TOKENIZER_SHA256 = "223921b76ee99bde995b7ff738513eef100fb51d18c93597a113bcffe865b2a7"
ENDPOINT = "https://openrouter.ai/api/v1/chat/completions"
BASE_POLICY = {
    "allow_fallbacks": False,
    "max_price": {"prompt": 0, "completion": 0, "request": 0, "image": 0},
}
POLICY = {**BASE_POLICY, "only": ["nvidia"]}
MAX_SYNTHETIC_INPUT_TOKENS = 16_000


def digest(value):
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_case():
    raw = CASE.read_bytes()
    if hashlib.sha256(raw).hexdigest() != CASE_SHA256:
        raise ValueError("Synthetic fixture changed")
    return json.loads(raw)


def require_tokenizer_cache():
    # Validation never fetches data implicitly. The credential-free setup step
    # downloads this one public file through tiktoken's own hash verification.
    cache = os.environ.get("TIKTOKEN_CACHE_DIR")
    if not cache:
        raise ValueError("Explicit tokenizer cache required")
    path = Path(cache) / hashlib.sha1(TOKENIZER_URL.encode()).hexdigest()
    if hashlib.sha256(path.read_bytes()).hexdigest() != TOKENIZER_SHA256:
        raise ValueError("Tokenizer hash mismatch")


class NvidiaBoundary(httpx.AsyncBaseTransport):
    """Constrain the existing client at its sole outbound request boundary."""

    def __init__(self, inner, expected_request_sha256=None):
        self.inner = inner
        self.expected_request_sha256 = expected_request_sha256
        self.attempted = 0
        self.request_sha256 = None
        self.input_tokens_with_reserve = None

    async def handle_async_request(self, request):
        if self.attempted or request.method != "POST" or str(request.url) != ENDPOINT:
            raise ValueError("Request boundary refused")
        payload = json.loads(request.content)
        if (
            set(payload) != {"model", "max_tokens", "provider", "messages"}
            or payload["model"] != MODEL_ID
            or payload["max_tokens"] != MAX_OUTPUT_TOKENS
            or payload["provider"] != BASE_POLICY
        ):
            raise ValueError("Request policy changed")
        payload["provider"] = POLICY
        from src.core.analyze import tokenizer

        self.input_tokens_with_reserve = (
            sum(len(tokenizer.encode(item["content"])) for item in payload["messages"])
            + 256
        )
        self.request_sha256 = digest(payload)
        if self.input_tokens_with_reserve > MAX_SYNTHETIC_INPUT_TOKENS or (
            self.expected_request_sha256 is not None
            and self.request_sha256 != self.expected_request_sha256
        ):
            raise ValueError("Unapproved prompt")
        # Rebuild Content-Length after adding the recipient pin. Header values
        # (including Authorization) are never included in receipts or hashes.
        bounded = httpx.Request(
            "POST",
            ENDPOINT,
            headers={k: v for k, v in request.headers.items() if k != "content-length"},
            json=payload,
            extensions=request.extensions,
        )
        self.attempted = 1  # A transport failure is still a consumed attempt.
        return await self.inner.handle_async_request(bounded)

    async def aclose(self):
        await self.inner.aclose()


async def calibrate():
    require_tokenizer_cache()
    case = load_case()
    captured = []

    def respond(request):
        captured.append(json.loads(request.content))
        return httpx.Response(
            200,
            json={
                "model": MODEL_ID,
                "choices": [
                    {
                        "finish_reason": "stop",
                        "message": {"content": case["calibration_response"]},
                    }
                ],
            },
        )

    boundary = NvidiaBoundary(httpx.MockTransport(respond))
    receipt = await verify_articles(
        case["articles"], client=VerificationClient("synthetic-key", boundary)
    )
    if (
        receipt["outcome"] != "validation_passed"
        or receipt["source_counts"] != {"eligible": 1, "review_required": 1}
        or len(captured) != 1
        or "example.test/advisories/withheld" in json.dumps(captured)
    ):
        raise ValueError("Calibration failed")
    return {
        "schema_version": 1,
        "case_sha256": CASE_SHA256,
        "input_sha256": digest(case["articles"]),
        "request_sha256": boundary.request_sha256,
        "requested_model": MODEL_ID,
        "recipient": "NVIDIA via OpenRouter",
        "provider_policy": POLICY,
        "input_tokens_with_reserve": boundary.input_tokens_with_reserve,
        "max_output_tokens": MAX_OUTPUT_TOKENS,
        "source_plan_id": receipt["source_plan_id"],
        "source_counts": receipt["source_counts"],
        "calibration_passed": True,
        "live_attempted": 0,
        "published": False,
        "human_review": "not_performed",
        "production_ready": False,
    }


def require_live_context(expected_commit, output):
    if not expected_commit or not re.fullmatch(r"[0-9a-f]{40}", expected_commit):
        raise ValueError("Exact approved commit required")
    expected = {
        "GITHUB_REPOSITORY": "ricomanifesto/SentryInsight",
        "GITHUB_REF": "refs/heads/main",
        "GITHUB_SHA": expected_commit,
        "GITHUB_EVENT_NAME": "workflow_dispatch",
        "GITHUB_RUN_ATTEMPT": "1",
    }
    if any(os.environ.get(name) != value for name, value in expected.items()):
        raise ValueError("Unapproved execution context")
    actual = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
    ).strip()
    if actual != expected_commit:
        raise ValueError("Checkout changed")
    if subprocess.check_output(
        ["git", "status", "--porcelain"], cwd=ROOT, text=True
    ).strip():
        raise ValueError("Checkout is not clean")
    directory = Path(os.environ["RUNNER_TEMP"]).resolve() / "nemotron-verification"
    if output.resolve() != directory / "live.json" or output.exists():
        raise ValueError("Unsafe or previously used receipt path")


async def run_trial(calibration, api_key, *, inner=None):
    boundary = NvidiaBoundary(
        (
            inner
            if inner is not None
            else httpx.AsyncHTTPTransport(retries=0, trust_env=False)
        ),
        calibration["request_sha256"],
    )
    try:
        receipt = await verify_articles(
            load_case()["articles"], client=VerificationClient(api_key, boundary)
        )
    except Exception:
        receipt = {"outcome": "verification_failed"}
    return {
        **calibration,
        "live_attempted": boundary.attempted,
        "result": receipt,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--live", action="store_true")
    parser.add_argument("--expected-commit")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    logging.disable(logging.CRITICAL)
    for name, value in {
        "OTEL_SDK_DISABLED": "true",
        "LOGFIRE_SEND_TO_LOGFIRE": "false",
        "LANGSMITH_TRACING": "false",
        "LANGCHAIN_TRACING_V2": "false",
    }.items():
        os.environ[name] = value
    try:
        if args.live:
            require_live_context(args.expected_commit, args.output)
        calibration = asyncio.run(calibrate())
        receipt = calibration
        if args.live:
            key = os.environ.get("OPENROUTER_API_KEY", "").strip()
            if not key:
                raise ValueError("Missing credential")
            receipt = asyncio.run(run_trial(calibration, key))
        args.output.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
        with args.output.open("x") as stream:
            os.chmod(args.output, 0o600)
            stream.write(json.dumps(receipt, sort_keys=True) + "\n")
        success = not args.live or receipt["result"]["outcome"] == "validation_passed"
        print("Verification passed." if success else "Verification failed; no retry.")
        return 0 if success else 1
    except Exception:
        # No exception text, source body, answer or credential reaches Actions.
        print("Verification preparation failed; do not retry uncertain attempts.")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

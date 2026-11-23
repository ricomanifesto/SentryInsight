#!/usr/bin/env python3
"""Preflight normalized public articles; optionally verify one unpublished report.

The default is offline. --run sends eligible source evidence to the configured
free Nemotron endpoint once. Answers stay in memory and are never exported.
This command has no generation-workflow, publication or scheduling operations.
"""

import argparse
import asyncio
from collections import Counter
import hashlib
import json
import logging
import math
import os
from pathlib import Path
import sys
import tempfile
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import httpx

from src.core.openrouter_client import OpenRouterClient, OpenRouterError
from src.core.opencode_client import ModelSelection
from src.core.reviewed_report import resolve_reviewed_analysis
from src.core.source_review import prepare_source_review
from scripts.verification_diagnostics import validation_diagnostic

MODEL = "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free"
MODEL_ID = MODEL.removeprefix("openrouter/")
MAX_INPUT_BYTES = 2_000_000
MAX_INPUT_TOKENS = 200_000
MAX_OUTPUT_TOKENS = 32_000


class VerificationClient(OpenRouterClient):
    """Use the normal client with a single-request and exact-model boundary."""

    def __init__(self, api_key: str, transport=None):
        super().__init__(
            api_key=api_key,
            max_tokens=MAX_OUTPUT_TOKENS,
            timeout=1800,
            max_attempts=1,
            transport=transport,
        )
        self.attempted = 0
        self.metadata: dict[str, Any] = {}

    async def generate(
        self,
        *,
        system_prompt: str,
        user_prompt: str,
        model: ModelSelection | None = None,
        title: str = "Report generation",
    ) -> str:
        if (
            self.attempted
            or model is None
            or model.provider_id != "openrouter"
            or model.model_id != MODEL_ID
        ):
            raise OpenRouterError("Verification request boundary refused")
        self.attempted = 1
        return await super().generate(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            model=model,
            title=title,
        )

    def _response_text(self, response: httpx.Response) -> str:
        self.metadata["http_status"] = response.status_code
        text = super()._response_text(response)
        payload = response.json()
        if payload.get("model") != MODEL_ID:
            raise OpenRouterError("Verification model identity refused")
        choices = payload.get("choices")
        if (
            not isinstance(choices, list)
            or len(choices) != 1
            or choices[0].get("finish_reason") != "stop"
        ):
            raise OpenRouterError("Verification completion not established")
        self.metadata["finish_reason"] = "stop"
        usage = payload.get("usage")
        if isinstance(usage, dict):
            self.metadata["usage"] = {
                key: value
                for key in (
                    "prompt_tokens",
                    "completion_tokens",
                    "total_tokens",
                    "cost",
                )
                if type(value := usage.get(key)) in (int, float)
                and math.isfinite(value)
                and 0 <= value <= 2**63
            }
        return text


async def verify_articles(
    articles: list[dict[str, Any]], *, client: VerificationClient | None = None
) -> dict[str, Any]:
    """Return bounded evidence, without invoking the production artifact writer."""
    if not isinstance(articles, list) or not 1 <= len(articles) <= 512:
        raise ValueError("Expected 1 to 512 normalized public articles")
    plan = prepare_source_review(articles)
    receipt: dict[str, Any] = {
        "schema_version": 1,
        "requested_model": MODEL_ID,
        "max_input_tokens": MAX_INPUT_TOKENS,
        "max_output_tokens": MAX_OUTPUT_TOKENS,
        "source_plan_id": plan.packet["plan_id"],
        "source_counts": dict(Counter(row["state"] for row in plan.packet["sources"])),
        "attempted": 0,
        "outcome": "preflight_only",
        "published": False,
        "human_review": "not_performed",
        "production_ready": False,
    }
    if not plan.eligible_keys:
        receipt["outcome"] = "review_required"
        return receipt
    if client is None:
        return receipt
    # Offline preflight and --help must not load/download tokenizer data.
    from src.core.analyze import analyze_exploitation

    # The analyzer persists only its normal source-review metadata here. The
    # temporary directory is removed on every ordinary exit; no report is saved.
    with tempfile.TemporaryDirectory(prefix="sentryinsight-verification-") as directory:
        config = {
            "output_path": str(Path(directory) / "index.md"),
            "analysis": {
                "model": MODEL,
                "max_input_tokens": MAX_INPUT_TOKENS,
                "max_tokens": MAX_OUTPUT_TOKENS,
            },
        }
        result = await analyze_exploitation(articles, config, model_client=client)
        receipt["attempted"] = client.attempted
        receipt["provider"] = client.metadata
        if result.get("error") or result.get("skipped"):
            receipt["outcome"] = "analysis_failed"
            return receipt
        validation_stage = "unknown_validation_stage"

        def observe_stage(stage: str) -> None:
            nonlocal validation_stage
            validation_stage = stage

        try:
            candidate = resolve_reviewed_analysis(result, on_stage=observe_stage)
        except Exception as error:
            # Exceptions can contain source or generated text. Never export them.
            receipt["outcome"] = "validation_failed"
            receipt["validation_diagnostic"] = validation_diagnostic(
                validation_stage, error
            )
            return receipt
        receipt["outcome"] = "validation_passed"
        receipt["report_sha256"] = hashlib.sha256(candidate.source.encode()).hexdigest()
        receipt["coverage_counts"] = candidate.coverage["counts"]
        return receipt


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "articles", type=Path, help="Normalized public article JSON list"
    )
    parser.add_argument(
        "--run", action="store_true", help="Make at most one model request"
    )
    args = parser.parse_args()
    # Do not configure tracing, load .env files or print generated/source text.
    logging.disable(logging.CRITICAL)
    try:
        with args.articles.open("rb") as stream:
            raw = stream.read(MAX_INPUT_BYTES + 1)
        if len(raw) > MAX_INPUT_BYTES:
            raise ValueError("Input size exceeded")
        articles = json.loads(raw)
        client = None
        if args.run:
            key = os.environ.get("OPENROUTER_API_KEY", "").strip()
            if not key:
                raise ValueError("Missing provider credential")
            client = VerificationClient(key)
        receipt = asyncio.run(verify_articles(articles, client=client))
        receipt["input_sha256"] = hashlib.sha256(raw).hexdigest()
        print(json.dumps(receipt, sort_keys=True))
        return 0 if receipt["outcome"] in {"preflight_only", "validation_passed"} else 1
    except Exception:
        print('{"outcome":"verification_failed","published":false}', file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

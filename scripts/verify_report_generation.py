#!/usr/bin/env python3
"""Preflight normalized public articles; optionally verify one unpublished report.

The default is offline. --run sends eligible source evidence to the configured
free Nemotron endpoint once. Answers stay in memory and are never exported.
This command has no generation-workflow, publication or scheduling operations.

``--profile recovery`` is an opt-in profile for the exact free
nvidia/nemotron-3.5-super-vl:free route with a 32,000 output cap and an 8,000
reasoning budget. Before anything is sent, the outgoing request must carry
exactly that envelope: require_parameters, four zero price ceilings and no
fallbacks. It makes at most one request, never retries, and accepts only the
exact model, a natural stop, cost exactly zero and bounded usage.
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
from typing import Any, cast

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import httpx

from src.core.openrouter_client import (
    OPENROUTER_BASE_URL,
    REASONING_MAX_TOKENS,
    OpenRouterClient,
    OpenRouterError,
)
from src.core.opencode_client import ModelSelection
from src.core.reviewed_report import resolve_reviewed_analysis
from src.core.source_review import prepare_source_review
from scripts.verification_diagnostics import validation_diagnostic

MODEL = "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free"
MODEL_ID = MODEL.removeprefix("openrouter/")
MAX_INPUT_BYTES = 2_000_000
MAX_INPUT_TOKENS = 200_000
MAX_OUTPUT_TOKENS = 32_000
RECOVERY_MODEL = "openrouter/nvidia/nemotron-3.5-super-vl:free"
RECOVERY_MODEL_ID = RECOVERY_MODEL.removeprefix("openrouter/")
RECOVERY_REASONING_MAX_TOKENS = 8_000
RECOVERY_ENDPOINT = OPENROUTER_BASE_URL + "/chat/completions"
RECOVERY_PROVIDER_POLICY = {
    "allow_fallbacks": False,
    "max_price": {"prompt": 0, "completion": 0, "request": 0, "image": 0},
    "require_parameters": True,
}
REFUSALS = frozenset(
    {
        "capability_policy_not_established",
        "request_envelope_refused",
        "http_status_not_ok",
        "usage_missing",
        "cost_not_zero",
        "completion_usage_invalid",
        "reasoning_usage_invalid",
    }
)


def _canonical(value: Any) -> str:
    # JSON distinguishes true from 1 and 0 from false, unlike ``==``.
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def _exact_message(message: object, role: str) -> bool:
    """One message object with exactly a role and nonempty string content."""
    if type(message) is not dict:
        return False
    # The exact-type check above proves a plain dict; name its shape for typing.
    fields = cast(dict[str, object], message)
    content = fields.get("content")
    return (
        set(fields) == {"role", "content"}
        and fields.get("role") == role
        and type(content) is str
        and content != ""
    )


def recovery_envelope_established(payload: Any) -> bool:
    """True only for the exact recovery route, cap and capability policy."""
    if type(payload) is not dict or set(payload) != {
        "model",
        "max_tokens",
        "messages",
        "provider",
        "reasoning",
    }:
        return False
    messages = payload["messages"]
    return (
        payload["model"] == RECOVERY_MODEL_ID
        and type(payload["max_tokens"]) is int
        and payload["max_tokens"] == MAX_OUTPUT_TOKENS
        and _canonical(payload["reasoning"])
        == _canonical({"max_tokens": RECOVERY_REASONING_MAX_TOKENS})
        and _canonical(payload["provider"]) == _canonical(RECOVERY_PROVIDER_POLICY)
        and type(messages) is list
        and len(messages) == 2
        and all(
            _exact_message(message, role)
            for message, role in zip(messages, ("system", "user"))
        )
    )


class VerificationClient(OpenRouterClient):
    """Use the normal client with a single-request and exact-model boundary."""

    model_id = MODEL_ID

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
            or model.model_id != self.model_id
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
        if payload.get("model") != self.model_id:
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


class _RecoveryEnvelopeTransport(httpx.AsyncBaseTransport):
    """Check the exact outgoing request before it can leave; send at most once."""

    def __init__(self, inner: httpx.AsyncBaseTransport, client: "RecoveryClient"):
        self.inner = inner
        self.client = client
        self.sent = 0

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        try:
            payload = json.loads(request.content)
        except (ValueError, TypeError):
            payload = None
        if (
            self.sent
            or request.method != "POST"
            or str(request.url) != RECOVERY_ENDPOINT
            or not recovery_envelope_established(payload)
        ):
            self.client.refuse("request_envelope_refused", request_state="not_sent")
        self.sent += 1
        return await self.inner.handle_async_request(request)

    async def aclose(self) -> None:
        await self.inner.aclose()


class RecoveryClient(VerificationClient):
    """Opt-in recovery profile: exact free route, bounded reasoning, one send."""

    model_id = RECOVERY_MODEL_ID

    def __init__(self, api_key: str, transport=None):
        self.guard = _RecoveryEnvelopeTransport(
            transport if transport is not None else httpx.AsyncHTTPTransport(), self
        )
        super().__init__(api_key, transport=self.guard)
        if self.verification is not None:
            raise OpenRouterError("Recovery profile refuses paid verification")
        if RECOVERY_REASONING_MAX_TOKENS != REASONING_MAX_TOKENS:
            raise OpenRouterError("Recovery reasoning budget does not match client")

    @property
    def sent(self) -> int:
        return self.guard.sent

    def refuse(self, refusal: str, request_state: str = "permanent_rejection"):
        self.metadata["refusal"] = refusal if refusal in REFUSALS else "refused"
        raise OpenRouterError(
            "Recovery verification refused", request_state=request_state
        )

    def _payload(self, system_prompt, user_prompt, model_id):
        payload = super()._payload(system_prompt, user_prompt, model_id)
        # Before reservation and before any send: the exact policy or nothing.
        if self.verification is not None or not recovery_envelope_established(payload):
            self.refuse("capability_policy_not_established", request_state="not_sent")
        return payload

    def _response_text(self, response: httpx.Response) -> str:
        # Error statuses keep the client's own classification; any other
        # success status than exactly 200 is refused before reading content.
        if response.is_success and response.status_code != 200:
            self.metadata["http_status"] = response.status_code
            self.refuse("http_status_not_ok")
        text = super()._response_text(response)
        usage = response.json().get("usage")
        if type(usage) is not dict:
            self.refuse("usage_missing")
        cost = usage.get("cost")
        if type(cost) not in (int, float) or not math.isfinite(cost) or cost != 0:
            self.refuse("cost_not_zero")
        completion = usage.get("completion_tokens")
        # Strictly below the cap: a natural stop at exactly the cap is not
        # distinguishable from truncation and is refused.
        if type(completion) is not int or not 0 < completion < MAX_OUTPUT_TOKENS:
            self.refuse("completion_usage_invalid")
        details = usage.get("completion_tokens_details")
        counts = [
            value
            for value in (
                details.get("reasoning_tokens") if type(details) is dict else None,
                usage.get("reasoning_tokens"),
            )
            if value is not None
        ]
        if (
            not counts
            or len(set(map(_canonical, counts))) != 1
            or type(counts[0]) is not int
            or not 0 <= counts[0] <= RECOVERY_REASONING_MAX_TOKENS
            or counts[0] > completion
        ):
            self.refuse("reasoning_usage_invalid")
        self.metadata["usage"] = {
            **self.metadata.get("usage", {}),
            "cost": cost,
            "completion_tokens": completion,
            "reasoning_tokens": counts[0],
        }
        return text


PROFILES = {
    "default": (MODEL, None),
    "recovery": (RECOVERY_MODEL, RECOVERY_REASONING_MAX_TOKENS),
}


async def verify_articles(
    articles: list[dict[str, Any]],
    *,
    client: VerificationClient | None = None,
    profile: str | None = None,
) -> dict[str, Any]:
    """Return bounded evidence, without invoking the production artifact writer."""
    if not isinstance(articles, list) or not 1 <= len(articles) <= 512:
        raise ValueError("Expected 1 to 512 normalized public articles")
    if profile is None:
        profile = "recovery" if isinstance(client, RecoveryClient) else "default"
    if profile not in PROFILES or (
        client is not None
        and isinstance(client, RecoveryClient) != (profile == "recovery")
    ):
        raise ValueError("Verification profile and client disagree")
    model, reasoning_budget = PROFILES[profile]
    plan = prepare_source_review(articles)
    receipt: dict[str, Any] = {
        "schema_version": 1,
        "requested_model": model.removeprefix("openrouter/"),
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
    if reasoning_budget is not None:
        receipt.update(
            profile=profile, reasoning_max_tokens=reasoning_budget, requests_sent=0
        )
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
                "model": model,
                "max_input_tokens": MAX_INPUT_TOKENS,
                "max_tokens": MAX_OUTPUT_TOKENS,
            },
        }
        result = await analyze_exploitation(articles, config, model_client=client)
        receipt["attempted"] = client.attempted
        receipt["provider"] = client.metadata
        if isinstance(client, RecoveryClient):
            receipt["requests_sent"] = client.sent
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
    parser.add_argument(
        "--profile",
        choices=sorted(PROFILES),
        default="default",
        help="recovery: exact free nemotron-3.5 route with bounded reasoning",
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
            client = (
                RecoveryClient(key)
                if args.profile == "recovery"
                else VerificationClient(key)
            )
        receipt = asyncio.run(
            verify_articles(articles, client=client, profile=args.profile)
        )
        receipt["input_sha256"] = hashlib.sha256(raw).hexdigest()
        print(json.dumps(receipt, sort_keys=True))
        return 0 if receipt["outcome"] in {"preflight_only", "validation_passed"} else 1
    except Exception:
        print('{"outcome":"verification_failed","published":false}', file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

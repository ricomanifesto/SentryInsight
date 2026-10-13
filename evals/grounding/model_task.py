"""Model-backed evaluation through the real report prompt, with zero-price routing."""

import json
import os
from pathlib import Path
from typing import Any

import httpx

from src.core.analyze import analyze_exploitation
from src.core.opencode_client import ModelSelection

from .dataset import TaskInput, digest

CHECKLIST = (
    "\nBefore writing, verify each CVE separately against every supplied source. "
    "Keep predicted likelihood, hypothetical conditions, qualified denials, "
    "and conflicting assertions separate from observed exploitation. "
    "Check the ownership and full wording of each version, exception and "
    "recommendation. A fixed version does not establish an affected range. "
    "Check that summary prose agrees with the finding status."
)


class ModelRunError(RuntimeError):
    """Sanitized model execution failure."""


class FreeModelClient:
    def __init__(
        self,
        *,
        api_key: str,
        variant: str,
        max_tokens: int,
        transport: httpx.AsyncBaseTransport | None = None,
    ):
        self.api_key = api_key
        self.variant = variant
        self.max_tokens = max_tokens
        self.transport = transport
        self.receipt: dict[str, Any] = {}

    async def generate(
        self,
        *,
        system_prompt: str,
        user_prompt: str,
        model: ModelSelection | None = None,
        title: str = "Report generation",
    ) -> str:
        if (
            model is None
            or model.provider_id != "openrouter"
            or not model.model_id.endswith(":free")
        ):
            raise ModelRunError("Only explicit free OpenRouter models are supported")
        if self.variant == "checklist":
            system_prompt += CHECKLIST
        payload = {
            "model": model.model_id,
            "max_tokens": self.max_tokens,
            "temperature": 1,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "provider": {
                "allow_fallbacks": False,
                "max_price": {"prompt": 0, "completion": 0, "request": 0, "image": 0},
            },
        }
        self.receipt = {
            "request_sha256": digest(payload),
            "requested_model": model.model_id,
            "provider_policy": payload["provider"],
            "max_tokens": self.max_tokens,
            "temperature": 1,
            "checklist_sha256": digest(CHECKLIST),
            "attempts": 1,
        }
        try:
            async with httpx.AsyncClient(
                timeout=180,
                transport=self.transport,
                follow_redirects=False,
            ) as client:
                response = await client.post(
                    "https://openrouter.ai/api/v1/chat/completions",
                    headers={"Authorization": f"Bearer {self.api_key}"},
                    json=payload,
                )
            self.receipt["http_status"] = response.status_code
            if response.status_code != 200:
                raise ModelRunError("Provider did not return a completion")
            data = response.json()
            usage = data.get("usage") or {}
            self.receipt.update(
                {
                    "response_id": data.get("id"),
                    "reported_model": data.get("model"),
                    "provider": data.get("provider"),
                    "usage": {
                        key: usage.get(key)
                        for key in (
                            "prompt_tokens",
                            "completion_tokens",
                            "total_tokens",
                            "cost",
                        )
                    },
                }
            )
            choice = data["choices"][0]
            self.receipt["finish_reason"] = choice.get("finish_reason")
            if choice.get("finish_reason") != "stop":
                raise ModelRunError("Incomplete generation")
            content = choice["message"]["content"]
            if not isinstance(content, str) or not content.strip():
                raise ModelRunError("Empty completion")
            return content
        except (httpx.HTTPError, KeyError, IndexError, TypeError, ValueError):
            raise ModelRunError("Invalid or unavailable completion") from None


class ModelTask:
    def __init__(
        self, *, model: str, receipts: Path, max_requests: int, max_tokens=8000
    ):
        if not model.startswith("openrouter/") or not model.endswith(":free"):
            raise ValueError("This pilot permits only explicit free OpenRouter routes")
        if os.getenv("SENTRYINSIGHT_MODEL", "").strip():
            raise ValueError(
                "Unset SENTRYINSIGHT_MODEL; the CLI model must be authoritative"
            )
        self.api_key = os.getenv("OPENROUTER_API_KEY", "").strip()
        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY is required")
        self.model = model
        self.receipts = receipts
        self.max_requests = max_requests
        self.max_tokens = max_tokens
        self.requests = 0

    async def __call__(self, inputs: TaskInput) -> str:
        if self.requests >= self.max_requests:
            raise ModelRunError("Request limit reached")
        self.requests += 1  # No await before reservation; at most one call per trial.
        client = FreeModelClient(
            api_key=self.api_key,
            variant=inputs.variant,
            max_tokens=self.max_tokens,
        )
        try:
            result = await analyze_exploitation(
                [article.model_dump() for article in inputs.articles],
                {"analysis": {"model": self.model, "max_tokens": self.max_tokens}},
                model_client=client,
            )
            if result.get("error") or result.get("skipped"):
                raise ModelRunError("Report generation did not complete")
            return result["exploitation_report"]
        finally:
            self.receipts.parent.mkdir(parents=True, exist_ok=True)
            with self.receipts.open("a") as stream:
                stream.write(
                    json.dumps(
                        {
                            "trial_id": f"{inputs.name}/{inputs.variant}/{inputs.repetition}",
                            **client.receipt,
                        }
                    )
                    + "\n"
                )

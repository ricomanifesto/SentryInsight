"""Direct OpenRouter chat-completions client for report generation.

Used when an ``OPENROUTER_API_KEY`` is configured (for example in CI) so report
generation does not depend on a locally running OpenCode gateway. Exposes the
same ``generate`` contract as :class:`~src.core.opencode_client.OpenCodeClient`.
"""

from __future__ import annotations

from typing import Any

import httpx

from .opencode_client import ModelSelection

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
OPENROUTER_API_KEY_ENV_VAR = "OPENROUTER_API_KEY"


class OpenRouterError(RuntimeError):
    """Raised when OpenRouter cannot return usable model output."""


class OpenRouterUnavailable(OpenRouterError):
    """Raised when the OpenRouter API cannot be reached."""


class OpenRouterClient:
    """Small async client for OpenRouter chat completions."""

    def __init__(
        self,
        *,
        api_key: str,
        max_tokens: int = 4000,
        base_url: str = OPENROUTER_BASE_URL,
        timeout: float = 120.0,
        transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        self.api_key = api_key
        self.max_tokens = max_tokens
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.transport = transport

    async def generate(
        self,
        *,
        system_prompt: str,
        user_prompt: str,
        model: ModelSelection | None = None,
        title: str = "Report generation",
    ) -> str:
        """Generate text through the OpenRouter chat completions API."""
        if model is None or model.provider_id != "openrouter":
            raise OpenRouterError("OpenRouter calls require an openrouter/* model")

        try:
            async with httpx.AsyncClient(
                base_url=self.base_url,
                timeout=self.timeout,
                transport=self.transport,
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                    "X-Title": title,
                },
            ) as client:
                response = await client.post(
                    "/chat/completions",
                    json={
                        "model": model.model_id,
                        "max_tokens": self.max_tokens,
                        "messages": [
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": user_prompt},
                        ],
                    },
                )
        except httpx.TransportError as e:
            # Keep the message generic so connection details never leak.
            raise OpenRouterUnavailable("OpenRouter API unavailable") from e

        self._raise_for_status(response)
        return self._extract_text(response.json())

    def _raise_for_status(self, response: httpx.Response) -> None:
        if response.is_success:
            return
        # Surface only the status code; the body may echo prompt content.
        raise OpenRouterError(
            f"OpenRouter chat completion failed: HTTP {response.status_code}"
        )

    def _extract_text(self, payload: dict[str, Any]) -> str:
        choices = payload.get("choices")
        if not isinstance(choices, list):
            raise OpenRouterError("OpenRouter response did not include choices")

        text_parts: list[str] = []
        for choice in choices:
            if not isinstance(choice, dict):
                continue
            message = choice.get("message")
            if isinstance(message, dict):
                content = message.get("content")
                if isinstance(content, str) and content.strip():
                    text_parts.append(content)

        if text_parts:
            return "\n".join(text_parts)

        raise OpenRouterError("OpenRouter response did not include text output")

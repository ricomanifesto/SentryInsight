"""Direct OpenRouter chat-completions client for report generation.

Used when an ``OPENROUTER_API_KEY`` is configured (for example in CI) so report
generation does not depend on a locally running OpenCode gateway. Exposes the
same ``generate`` contract as :class:`~src.core.opencode_client.OpenCodeClient`.
"""

from __future__ import annotations

import asyncio
import logging
import math
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from typing import Any

import httpx

from .opencode_client import ModelSelection

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
OPENROUTER_API_KEY_ENV_VAR = "OPENROUTER_API_KEY"
MAX_ATTEMPTS = 3
MAX_RETRY_DELAY = 30.0
RETRYABLE_CODES = {408, 429, 500, 502, 503, 504}
logger = logging.getLogger(__name__)


class OpenRouterError(RuntimeError):
    """Raised when OpenRouter cannot return usable model output."""

    def __init__(self, message: str, *, retryable: bool = False) -> None:
        super().__init__(message)
        self.retryable = retryable


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
            for attempt in range(1, MAX_ATTEMPTS + 1):
                response = None
                try:
                    try:
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
                    except httpx.TransportError as exc:
                        # Local protocol/configuration errors are not transient.
                        # Suppress the original exception, which may contain secrets.
                        raise OpenRouterUnavailable(
                            "OpenRouter API unavailable",
                            retryable=isinstance(
                                exc,
                                (
                                    httpx.NetworkError,
                                    httpx.TimeoutException,
                                    httpx.RemoteProtocolError,
                                ),
                            ),
                        ) from None
                    return self._response_text(response)
                except OpenRouterError as exc:
                    delay = self._retry_delay(response, attempt)
                    if (
                        not exc.retryable
                        or attempt == MAX_ATTEMPTS
                        or delay > MAX_RETRY_DELAY
                    ):
                        logger.error(
                            "OpenRouter attempt %d/%d failed: %s; stopping",
                            attempt,
                            MAX_ATTEMPTS,
                            exc,
                        )
                        raise
                    logger.warning(
                        "OpenRouter attempt %d/%d failed: %s; retrying in %.1fs",
                        attempt,
                        MAX_ATTEMPTS,
                        exc,
                        delay,
                    )
                    await asyncio.sleep(delay)

        raise AssertionError("OpenRouter retry loop exhausted without a result")

    @staticmethod
    def _retry_delay(response: httpx.Response | None, attempt: int) -> float:
        """Honor Retry-After; the caller stops if the wait exceeds our budget."""
        backoff = float(2 ** (attempt - 1))
        value = response.headers.get("Retry-After") if response is not None else None
        if not value:
            return backoff
        try:
            delay = float(value)
        except ValueError:
            try:
                retry_at = parsedate_to_datetime(value)
                delay = (retry_at - datetime.now(timezone.utc)).total_seconds()
            except (ValueError, TypeError, OverflowError):
                return backoff
        if math.isnan(delay) or delay < 0:
            return backoff
        return max(backoff, delay)

    def _response_text(self, response: httpx.Response) -> str:
        try:
            payload = response.json()
        except ValueError:
            payload = None

        has_error = isinstance(payload, dict) and "error" in payload
        provider_code = None
        if has_error and isinstance(payload["error"], dict):
            code = payload["error"].get("code")
            # Arbitrary messages, metadata and string codes can echo requests.
            if (
                isinstance(code, str)
                and code.isascii()
                and code.isdigit()
                and len(code) == 3
            ):
                code = int(code)
            if type(code) is int and 100 <= code <= 599:
                provider_code = code

        if not response.is_success or has_error:
            message = f"OpenRouter chat completion failed: HTTP {response.status_code}"
            retryable = response.status_code in RETRYABLE_CODES
            if has_error:
                message += f"; provider_code={provider_code or 'unknown'}"
                # Known provider codes classify HTTP 200 errors too. If no code
                # is supplied, retain the HTTP status as the only safe evidence.
                if provider_code is not None:
                    retryable = (
                        response.is_success or retryable
                    ) and provider_code in RETRYABLE_CODES
            raise OpenRouterError(message, retryable=retryable)

        if not isinstance(payload, dict):
            raise OpenRouterError(
                f"OpenRouter response was not a JSON object (HTTP {response.status_code})",
                retryable=True,
            )
        try:
            return self._extract_text(payload)
        except OpenRouterError as exc:
            raise OpenRouterError(
                f"{exc} (HTTP {response.status_code})", retryable=exc.retryable
            ) from None

    def _extract_text(self, payload: dict[str, Any]) -> str:
        choices = payload.get("choices")
        if not isinstance(choices, list) or not choices:
            raise OpenRouterError(
                "OpenRouter response did not include choices", retryable=True
            )

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

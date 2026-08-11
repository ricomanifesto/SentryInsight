"""OpenAI Responses API client for report generation."""

from __future__ import annotations

from typing import Any

import openai
from openai import AsyncOpenAI
from openai.types.shared_params.reasoning import Reasoning
from openai.types.shared_params.reasoning_effort import ReasoningEffort


class OpenAIError(RuntimeError):
    """Raised when OpenAI cannot return usable model output."""


class OpenAIUnavailable(OpenAIError):
    """Raised when the OpenAI API cannot be reached."""


class OpenAIClient:
    """Small async client for the OpenAI Responses API."""

    def __init__(
        self,
        *,
        max_output_tokens: int = 16_000,
        reasoning_effort: ReasoningEffort = "xhigh",
        api_key: str | None = None,
        timeout: float = 120.0,
        sdk_client: Any | None = None,
    ) -> None:
        self.max_output_tokens = max_output_tokens
        self.reasoning_effort = reasoning_effort
        if sdk_client is None:
            if not api_key or not api_key.strip():
                raise OpenAIError("OPENAI_API_KEY is required for model generation")
            sdk_client = AsyncOpenAI(api_key=api_key, timeout=timeout)
        self._sdk_client = sdk_client

    async def generate(
        self,
        *,
        system_prompt: str,
        user_prompt: str,
        model: str,
        title: str = "Report generation",
    ) -> str:
        """Generate text through the OpenAI Responses API."""
        if not model.strip():
            raise OpenAIError("OpenAI model ID is required")

        reasoning: Reasoning = {"effort": self.reasoning_effort}
        try:
            response = await self._sdk_client.responses.create(
                model=model,
                instructions=system_prompt,
                input=user_prompt,
                max_output_tokens=self.max_output_tokens,
                reasoning=reasoning,
                metadata={"request_title": title},
            )
        except openai.APIConnectionError as error:
            raise OpenAIUnavailable("OpenAI API unavailable") from error
        except openai.APIStatusError as error:
            raise OpenAIError(
                f"OpenAI response failed: HTTP {error.status_code}"
            ) from error
        except openai.APIError as error:
            raise OpenAIError("OpenAI request failed") from error

        text = str(getattr(response, "output_text", "") or "").strip()
        if text:
            return text
        raise OpenAIError("OpenAI response did not include text output")

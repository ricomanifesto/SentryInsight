"""Build the OpenAI model client used for report generation."""

from __future__ import annotations

import os
from typing import cast

from openai.types.shared_params.reasoning_effort import ReasoningEffort

from .openai_client import OpenAIClient

OPENAI_API_KEY_ENV_VAR = "OPENAI_API_KEY"
OPENAI_REASONING_EFFORT_ENV_VAR = "OPENAI_REASONING_EFFORT"
DEFAULT_REASONING_EFFORT = "xhigh"
VALID_REASONING_EFFORTS = frozenset(
    {"none", "minimal", "low", "medium", "high", "xhigh", "max"}
)


def build_model_client(*, timeout: float, max_tokens: int) -> OpenAIClient:
    """Return the configured OpenAI Responses API client."""
    api_key = os.getenv(OPENAI_API_KEY_ENV_VAR, "").strip()
    if not api_key:
        raise ValueError("OPENAI_API_KEY is required for model generation")
    raw_reasoning_effort = os.getenv(
        OPENAI_REASONING_EFFORT_ENV_VAR, DEFAULT_REASONING_EFFORT
    ).strip()
    if raw_reasoning_effort not in VALID_REASONING_EFFORTS:
        raise ValueError(
            "OPENAI_REASONING_EFFORT must be one of: "
            + ", ".join(sorted(VALID_REASONING_EFFORTS))
        )
    reasoning_effort = cast(ReasoningEffort, raw_reasoning_effort)
    return OpenAIClient(
        api_key=api_key,
        max_output_tokens=max_tokens,
        reasoning_effort=reasoning_effort,
        timeout=timeout,
    )

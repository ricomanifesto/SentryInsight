"""Select the model client used for report generation.

Prefer a direct OpenRouter client when an API key is configured, so the
pipeline can run without a locally hosted OpenCode gateway (for example in CI).
Otherwise fall back to OpenCode for local development. Both clients expose the
same ``generate`` contract.
"""

from __future__ import annotations

import os

from .opencode_client import OpenCodeClient
from .openrouter_client import OPENROUTER_API_KEY_ENV_VAR, OpenRouterClient


def build_model_client(
    *, timeout: float, max_tokens: int
) -> OpenCodeClient | OpenRouterClient:
    """Return the model client selected by the environment.

    Uses OpenRouter directly when ``OPENROUTER_API_KEY`` is set; otherwise uses
    a local OpenCode server.
    """
    api_key = os.getenv(OPENROUTER_API_KEY_ENV_VAR, "").strip()
    if api_key:
        return OpenRouterClient(api_key=api_key, max_tokens=max_tokens, timeout=timeout)
    return OpenCodeClient(timeout=timeout)

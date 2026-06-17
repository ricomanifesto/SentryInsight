"""Anthropic model configuration helpers."""

import os
import re
from typing import Any, Dict

DEFAULT_ANTHROPIC_MODEL = "claude-sonnet-4-6"
MODEL_ENV_VAR = "SENTRYINSIGHT_ANTHROPIC_MODEL"

_MODEL_ID_PATTERN = re.compile(r"^claude-[a-z0-9]+(?:-[a-z0-9]+)*$")
_KNOWN_UNAVAILABLE_MODELS = {
    "claude-sonnet-4-20250514",
}


def resolve_anthropic_model(config: Dict[str, Any]) -> str:
    """Resolve the Anthropic model from env, config, or the project default."""
    env_model = os.getenv(MODEL_ENV_VAR, "").strip()
    if env_model:
        return env_model

    configured_model = config.get("analysis", {}).get("model", "").strip()
    return configured_model or DEFAULT_ANTHROPIC_MODEL


def validate_anthropic_model(model_name: str) -> None:
    """Raise ValueError when the configured model is known-bad or malformed."""
    if not model_name:
        raise ValueError("Anthropic model is empty")

    if model_name in _KNOWN_UNAVAILABLE_MODELS:
        raise ValueError(
            f"Anthropic model {model_name!r} is known to return 404; "
            f"use {DEFAULT_ANTHROPIC_MODEL!r} or set {MODEL_ENV_VAR}."
        )

    if not _MODEL_ID_PATTERN.match(model_name):
        raise ValueError(
            f"Anthropic model {model_name!r} is not a valid Claude API model ID"
        )

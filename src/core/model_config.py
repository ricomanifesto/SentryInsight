"""Model configuration helpers."""

import os
import re
from typing import Any, Dict

DEFAULT_MODEL = "anthropic/claude-sonnet-4-6"
MODEL_ENV_VAR = "SENTRYINSIGHT_MODEL"

_MODEL_ID_PATTERN = re.compile(
    r"^[a-z][a-z0-9_-]*/[a-z][a-z0-9._-]*(?:-[a-z0-9._-]+)*$"
)
_KNOWN_UNAVAILABLE_MODELS = {
    "claude-sonnet-4-20250514",
}


def resolve_model(config: Dict[str, Any]) -> str:
    """Resolve the model from env, config, or the project default."""
    env_model = os.getenv(MODEL_ENV_VAR, "").strip()
    if env_model:
        return env_model

    configured_model = config.get("analysis", {}).get("model", "").strip()
    return configured_model or DEFAULT_MODEL


def validate_model(model_name: str) -> None:
    """Raise ValueError when the configured model is known-bad or malformed."""
    if not model_name:
        raise ValueError("Model is empty")

    model_id = model_name.split("/", 1)[-1]
    if model_id in _KNOWN_UNAVAILABLE_MODELS:
        raise ValueError(
            f"Model {model_name!r} is known to return 404; "
            f"use a current model or set {MODEL_ENV_VAR}."
        )

    if not _MODEL_ID_PATTERN.match(model_name):
        raise ValueError(f"Model {model_name!r} is not a valid provider/model ID")

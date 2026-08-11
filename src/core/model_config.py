"""Model configuration helpers."""

import os
import re
from typing import Any, Dict

DEFAULT_MODEL = "gpt-5.6-sol"
MODEL_ENV_VAR = "SENTRYINSIGHT_MODEL"

_MODEL_ID_PATTERN = re.compile(r"^[a-z0-9][a-z0-9._:-]*$")


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

    if not _MODEL_ID_PATTERN.match(model_name):
        raise ValueError(f"Model {model_name!r} is not a valid OpenAI model ID")

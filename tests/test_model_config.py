import os
import unittest
from unittest.mock import patch

from src.core.model_config import (
    DEFAULT_ANTHROPIC_MODEL,
    MODEL_ENV_VAR,
    resolve_anthropic_model,
    validate_anthropic_model,
)


class ModelConfigTests(unittest.TestCase):
    def test_resolves_model_from_config(self):
        config = {"analysis": {"model": "claude-sonnet-4-6"}}

        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(resolve_anthropic_model(config), "claude-sonnet-4-6")

    def test_env_override_wins(self):
        config = {"analysis": {"model": "claude-haiku-4-5"}}

        with patch.dict(os.environ, {MODEL_ENV_VAR: "claude-opus-4-8"}):
            self.assertEqual(resolve_anthropic_model(config), "claude-opus-4-8")

    def test_empty_config_uses_default(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(resolve_anthropic_model({}), DEFAULT_ANTHROPIC_MODEL)

    def test_rejects_known_unavailable_model(self):
        with self.assertRaises(ValueError):
            validate_anthropic_model("claude-sonnet-4-20250514")

    def test_accepts_current_dateless_model(self):
        validate_anthropic_model("claude-sonnet-4-6")


if __name__ == "__main__":
    unittest.main()

import os
import unittest
from unittest.mock import patch

from src.core.model_config import (
    DEFAULT_MODEL,
    MODEL_ENV_VAR,
    resolve_model,
    validate_model,
)
from src.core.opencode_client import parse_model_selection


class ModelConfigTests(unittest.TestCase):
    def test_resolves_model_from_config(self):
        config = {"analysis": {"model": "anthropic/claude-sonnet-4-6"}}

        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(resolve_model(config), "anthropic/claude-sonnet-4-6")

    def test_env_override_wins(self):
        config = {"analysis": {"model": "anthropic/claude-haiku-4-5"}}

        with patch.dict(os.environ, {MODEL_ENV_VAR: "openai/gpt-5"}):
            self.assertEqual(resolve_model(config), "openai/gpt-5")

    def test_empty_config_uses_default(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(resolve_model({}), DEFAULT_MODEL)

    def test_rejects_known_unavailable_model(self):
        with self.assertRaises(ValueError):
            validate_model("anthropic/claude-sonnet-4-20250514")

    def test_accepts_provider_model(self):
        validate_model("openai/gpt-5")

    def test_rejects_bare_provider_model(self):
        with self.assertRaises(ValueError):
            validate_model("claude-sonnet-4-6")

    def test_parses_explicit_provider_model(self):
        model = parse_model_selection("anthropic/claude-sonnet-4-6")

        self.assertEqual(model.provider_id, "anthropic")
        self.assertEqual(model.model_id, "claude-sonnet-4-6")


if __name__ == "__main__":
    unittest.main()

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
    def test_default_model_uses_free_openrouter_report_model(self):
        self.assertEqual(
            DEFAULT_MODEL,
            "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free",
        )

    def test_resolves_model_from_config(self):
        config = {
            "analysis": {"model": "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free"}
        }

        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(
                resolve_model(config),
                "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free",
            )

    def test_env_override_wins(self):
        config = {
            "analysis": {"model": "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free"}
        }

        with patch.dict(
            os.environ, {MODEL_ENV_VAR: "openrouter/nex-agi/nex-n2-pro:free"}
        ):
            self.assertEqual(
                resolve_model(config), "openrouter/nex-agi/nex-n2-pro:free"
            )

    def test_empty_config_uses_default(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(resolve_model({}), DEFAULT_MODEL)

    def test_rejects_known_unavailable_model(self):
        with self.assertRaises(ValueError):
            validate_model("anthropic/claude-sonnet-4-20250514")

    def test_accepts_provider_model(self):
        validate_model("openrouter/nex-agi/nex-n2-pro:free")

    def test_accepts_openrouter_nested_model_id(self):
        validate_model("openrouter/nvidia/nemotron-3-ultra-550b-a55b:free")

    def test_rejects_bare_provider_model(self):
        with self.assertRaises(ValueError):
            validate_model("claude-sonnet-4-6")

    def test_parses_explicit_provider_model(self):
        model = parse_model_selection(
            "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free"
        )

        self.assertEqual(model.provider_id, "openrouter")
        self.assertEqual(model.model_id, "nvidia/nemotron-3-ultra-550b-a55b:free")


if __name__ == "__main__":
    unittest.main()

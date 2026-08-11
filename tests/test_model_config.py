import os
import unittest
from unittest.mock import patch

from src.core.model_config import (
    DEFAULT_MODEL,
    MODEL_ENV_VAR,
    resolve_model,
    validate_model,
)


class ModelConfigTests(unittest.TestCase):
    def test_default_model_uses_gpt_5_6_sol(self):
        self.assertEqual(DEFAULT_MODEL, "gpt-5.6-sol")

    def test_resolves_model_from_config(self):
        config = {"analysis": {"model": "gpt-5.6-sol"}}

        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(
                resolve_model(config),
                "gpt-5.6-sol",
            )

    def test_env_override_wins(self):
        config = {"analysis": {"model": "gpt-5.6-sol"}}

        with patch.dict(os.environ, {MODEL_ENV_VAR: "gpt-5.6-sol-2026-08-01"}):
            self.assertEqual(resolve_model(config), "gpt-5.6-sol-2026-08-01")

    def test_empty_config_uses_default(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(resolve_model({}), DEFAULT_MODEL)

    def test_accepts_openai_model(self):
        validate_model("gpt-5.6-sol")

    def test_rejects_provider_qualified_model(self):
        with self.assertRaisesRegex(ValueError, "OpenAI model ID"):
            validate_model("provider/model")


if __name__ == "__main__":
    unittest.main()

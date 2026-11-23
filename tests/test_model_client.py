import os
import unittest
from unittest import mock

from src.core.model_client import build_model_client
from src.core.opencode_client import OpenCodeClient
from src.core.openrouter_client import OpenRouterClient


class BuildModelClientTests(unittest.TestCase):
    def test_uses_openrouter_when_api_key_present(self):
        with mock.patch.dict(
            os.environ, {"OPENROUTER_API_KEY": "test-key"}, clear=False
        ):
            client = build_model_client(timeout=120.0, max_tokens=4000)

        self.assertIsInstance(client, OpenRouterClient)
        self.assertEqual(client.api_key, "test-key")
        self.assertEqual(client.max_tokens, 4000)
        self.assertIsNone(client.recovery_max_tokens)
        self.assertIsNone(client.reasoning_max_tokens)
        self.assertIsNone(client.total_timeout)
        self.assertFalse(client.output_limit_recovery)

    def test_forwards_recovery_and_timeout_options_to_openrouter(self):
        with mock.patch.dict(
            os.environ, {"OPENROUTER_API_KEY": "test-key"}, clear=False
        ):
            client = build_model_client(
                timeout=1800.0,
                max_tokens=96000,
                recovery_max_tokens=131072,
                total_timeout=3600.0,
                output_limit_recovery=True,
            )

        self.assertIsInstance(client, OpenRouterClient)
        self.assertEqual(client.max_tokens, 96000)
        self.assertEqual(client.recovery_max_tokens, 131072)
        self.assertIsNone(client.reasoning_max_tokens)
        self.assertEqual(client.total_timeout, 3600.0)
        self.assertTrue(client.output_limit_recovery)

    def test_falls_back_to_opencode_without_api_key(self):
        with mock.patch.dict(os.environ, {"OPENROUTER_API_KEY": ""}, clear=False):
            client = build_model_client(timeout=120.0, max_tokens=4000)

        self.assertIsInstance(client, OpenCodeClient)

    def test_blank_api_key_falls_back_to_opencode(self):
        with mock.patch.dict(os.environ, {"OPENROUTER_API_KEY": "   "}, clear=False):
            client = build_model_client(timeout=120.0, max_tokens=4000)

        self.assertIsInstance(client, OpenCodeClient)


if __name__ == "__main__":
    unittest.main()

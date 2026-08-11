import os
import unittest
from unittest import mock

from src.core.model_client import build_model_client
from src.core.openai_client import OpenAIClient


class BuildModelClientTests(unittest.TestCase):
    def test_uses_openai_when_api_key_present(self):
        with mock.patch.dict(
            os.environ,
            {"OPENAI_API_KEY": "test-key", "OPENAI_REASONING_EFFORT": "xhigh"},
            clear=False,
        ):
            client = build_model_client(timeout=120.0, max_tokens=4000)

        self.assertIsInstance(client, OpenAIClient)
        self.assertEqual(client.max_output_tokens, 4000)
        self.assertEqual(client.reasoning_effort, "xhigh")

    def test_requires_openai_api_key(self):
        with mock.patch.dict(os.environ, {"OPENAI_API_KEY": ""}, clear=False):
            with self.assertRaisesRegex(ValueError, "OPENAI_API_KEY"):
                build_model_client(timeout=120.0, max_tokens=4000)

    def test_rejects_unknown_reasoning_effort(self):
        with mock.patch.dict(
            os.environ,
            {"OPENAI_API_KEY": "test-key", "OPENAI_REASONING_EFFORT": "extreme"},
            clear=False,
        ):
            with self.assertRaisesRegex(ValueError, "OPENAI_REASONING_EFFORT"):
                build_model_client(timeout=120.0, max_tokens=4000)


if __name__ == "__main__":
    unittest.main()

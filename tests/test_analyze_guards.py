import asyncio
import importlib
import os
import sys
import types
import unittest
from unittest.mock import patch


def import_analyze_with_stubs():
    sys.modules.pop("src.core.analyze", None)

    tiktoken_module = types.ModuleType("tiktoken")
    tiktoken_module.get_encoding = lambda _name: types.SimpleNamespace(
        encode=lambda value: value.split()
    )

    anthropic_module = types.ModuleType("langchain_anthropic")

    class ChatAnthropic:
        def __init__(self, **_kwargs):
            raise AssertionError("ChatAnthropic should not be constructed")

    anthropic_module.ChatAnthropic = ChatAnthropic

    messages_module = types.ModuleType("langchain_core.messages")
    messages_module.HumanMessage = lambda content: types.SimpleNamespace(
        content=content
    )
    messages_module.SystemMessage = lambda content: types.SimpleNamespace(
        content=content
    )

    with patch.dict(
        sys.modules,
        {
            "tiktoken": tiktoken_module,
            "langchain_anthropic": anthropic_module,
            "langchain_core.messages": messages_module,
        },
    ):
        return importlib.import_module("src.core.analyze")


class AnalyzeGuardTests(unittest.TestCase):
    def test_invalid_model_returns_error_before_external_call(self):
        analyze = import_analyze_with_stubs()

        with patch.dict(os.environ, {"ANTHROPIC_API_KEY": "test-key"}):
            result = asyncio.run(
                analyze.analyze_exploitation(
                    articles=[],
                    config={
                        "analysis": {
                            "model": "claude-sonnet-4-20250514",
                        }
                    },
                )
            )

        self.assertIn("error", result)
        self.assertIn("known to return 404", result["error"])
        self.assertIn("# Error: Invalid Anthropic Model", result["exploitation_report"])

    def test_missing_api_key_returns_error_without_external_call(self):
        analyze = import_analyze_with_stubs()

        with patch.dict(os.environ, {}, clear=True):
            result = asyncio.run(
                analyze.analyze_exploitation(
                    articles=[],
                    config={"analysis": {"model": "claude-sonnet-4-6"}},
                )
            )

        self.assertEqual(result["error"], "No API key")
        self.assertIn("No Anthropic API Key", result["exploitation_report"])


if __name__ == "__main__":
    unittest.main()

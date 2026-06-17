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

    with patch.dict(
        sys.modules,
        {
            "tiktoken": tiktoken_module,
        },
    ):
        return importlib.import_module("src.core.analyze")


class AnalyzeGuardTests(unittest.TestCase):
    def test_invalid_model_returns_error_before_external_call(self):
        analyze = import_analyze_with_stubs()

        with patch.dict(os.environ, {}, clear=True):
            result = asyncio.run(
                analyze.analyze_exploitation(
                    articles=[],
                    config={
                        "analysis": {
                            "model": "anthropic/claude-sonnet-4-20250514",
                        }
                    },
                )
            )

        self.assertIn("error", result)
        self.assertIn("known to return 404", result["error"])
        self.assertIn("# Error: Invalid Model", result["exploitation_report"])

    def test_generates_report_through_opencode_without_provider_api_key(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenCodeClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **kwargs):
                self.kwargs = kwargs
                assert kwargs["model"].provider_id == "anthropic"
                assert kwargs["model"].model_id == "claude-sonnet-4-6"
                return "# Exploitation Report\n\nGenerated through OpenCode."

        analyze.OpenCodeClient = FakeOpenCodeClient

        with patch.dict(os.environ, {}, clear=True):
            result = asyncio.run(
                analyze.analyze_exploitation(
                    articles=[],
                    config={"analysis": {"model": "anthropic/claude-sonnet-4-6"}},
                )
            )

        self.assertNotIn("error", result)
        self.assertIn("Generated through OpenCode", result["exploitation_report"])


if __name__ == "__main__":
    unittest.main()

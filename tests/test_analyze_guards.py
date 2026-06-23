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
                assert kwargs["model"].provider_id == "openrouter"
                assert (
                    kwargs["model"].model_id == "nvidia/nemotron-3-ultra-550b-a55b:free"
                )
                return "# Exploitation Report\n\nGenerated through OpenCode."

        analyze.OpenCodeClient = FakeOpenCodeClient

        with patch.dict(os.environ, {}, clear=True):
            result = asyncio.run(
                analyze.analyze_exploitation(
                    articles=[],
                    config={
                        "analysis": {
                            "model": "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free"
                        }
                    },
                )
            )

        self.assertNotIn("error", result)
        self.assertIn("Generated through OpenCode", result["exploitation_report"])

    def test_unavailable_opencode_server_returns_skip_result(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenCodeClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **_kwargs):
                raise analyze.OpenCodeUnavailable("OpenCode server unavailable")

        analyze.OpenCodeClient = FakeOpenCodeClient

        with patch.dict(os.environ, {}, clear=True):
            result = asyncio.run(
                analyze.analyze_exploitation(
                    articles=[],
                    config={
                        "analysis": {
                            "model": "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free"
                        }
                    },
                )
            )

        self.assertTrue(result["skipped"])
        self.assertEqual(result["skip_reason"], "OpenCode server unavailable")
        self.assertNotIn("error", result)

    def test_article_prompt_omits_empty_source_and_url_fields(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenCodeClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **kwargs):
                user_prompt = kwargs["user_prompt"]
                self.__class__.user_prompt = user_prompt
                return "# Exploitation Report\n\nGenerated through OpenCode."

        analyze.OpenCodeClient = FakeOpenCodeClient

        with patch.dict(os.environ, {}, clear=True):
            asyncio.run(
                analyze.analyze_exploitation(
                    articles=[
                        {
                            "title": None,
                            "source": None,
                            "link": None,
                            "summary": "Summary only",
                        }
                    ],
                    config={
                        "analysis": {
                            "model": "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free"
                        }
                    },
                )
            )

        self.assertIn("**Untitled article**", FakeOpenCodeClient.user_prompt)
        self.assertIn("Summary only...", FakeOpenCodeClient.user_prompt)
        self.assertNotIn("(Source: )", FakeOpenCodeClient.user_prompt)
        self.assertNotIn("URL: \n", FakeOpenCodeClient.user_prompt)

    def test_prompt_requires_source_attribution_from_article_metadata(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenCodeClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **kwargs):
                self.__class__.user_prompt = kwargs["user_prompt"]
                return "# Exploitation Report\n\nGenerated through OpenCode."

        analyze.OpenCodeClient = FakeOpenCodeClient

        with patch.dict(os.environ, {}, clear=True):
            asyncio.run(
                analyze.analyze_exploitation(
                    articles=[
                        {
                            "title": "Example exploitation report",
                            "source": "Example Source",
                            "link": "https://example.test/report",
                            "summary": "Summary only",
                        }
                    ],
                    config={
                        "analysis": {
                            "model": "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free"
                        }
                    },
                )
            )

        self.assertIn("## Source Attribution", FakeOpenCodeClient.user_prompt)
        self.assertIn(
            "Only use source names and URLs provided",
            FakeOpenCodeClient.user_prompt,
        )
        self.assertIn("Example exploitation report", FakeOpenCodeClient.user_prompt)
        self.assertIn("Example Source", FakeOpenCodeClient.user_prompt)
        self.assertIn("https://example.test/report", FakeOpenCodeClient.user_prompt)

    def test_analysis_result_carries_canonical_source_attribution_entries(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenCodeClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **_kwargs):
                return "# Exploitation Report\n\nGenerated through OpenCode."

        analyze.OpenCodeClient = FakeOpenCodeClient

        with patch.dict(os.environ, {}, clear=True):
            result = asyncio.run(
                analyze.analyze_exploitation(
                    articles=[
                        {
                            "title": "Example exploitation report",
                            "source": "Example Source",
                            "link": "https://example.test/report",
                            "summary": "Summary only",
                        },
                        {
                            "title": "Source-only exploitation report",
                            "source": "Example Source",
                            "summary": "Summary only",
                        },
                    ],
                    config={
                        "analysis": {
                            "model": "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free"
                        }
                    },
                )
            )

        self.assertTrue(result["source_attribution_required"])
        self.assertEqual(
            result["source_attribution_entries"],
            [
                "- **Example exploitation report**: Example Source - https://example.test/report",
                "- **Source-only exploitation report**: Example Source",
            ],
        )
        self.assertNotIn("source_attribution_requirements", result)


if __name__ == "__main__":
    unittest.main()

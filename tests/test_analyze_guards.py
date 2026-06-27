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

    opencode_client_module = types.ModuleType("src.core.opencode_client")

    class OpenCodeUnavailable(RuntimeError):
        pass

    class OpenCodeClient:
        pass

    def parse_model_selection(model_name):
        provider_id, model_id = model_name.split("/", 1)
        return types.SimpleNamespace(provider_id=provider_id, model_id=model_id)

    opencode_client_module.OpenCodeClient = OpenCodeClient
    opencode_client_module.OpenCodeUnavailable = OpenCodeUnavailable
    opencode_client_module.parse_model_selection = parse_model_selection

    with patch.dict(
        sys.modules,
        {
            "src.core.opencode_client": opencode_client_module,
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

    def test_analysis_result_extracts_cves_from_article_text(self):
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
                            "title": "Vendor patch for CVE-2026-1111",
                            "summary": "Summary text is not used when content is present.",
                            "content": "Exploitation observed for CVE 2026 2222. "
                            + ("padding " * 80)
                            + "Late content mentions CVE-2026-4444.",
                            "link": "https://example.test/CVE-2026-3333",
                            "cves": ["CVE-2026-5555"],
                        }
                    ],
                    config={
                        "analysis": {
                            "model": "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free"
                        }
                    },
                )
            )

        self.assertEqual(
            sorted(result["cves_identified"]),
            [
                "CVE-2026-1111",
                "CVE-2026-2222",
                "CVE-2026-3333",
                "CVE-2026-5555",
            ],
        )
        self.assertNotIn("CVE-2026-4444", result["cves_identified"])

    def test_analysis_result_ignores_patch_only_cves_for_expected_coverage(self):
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
                            "title": "Vendor patch for CVE-2026-1111",
                            "summary": "Maintenance update available for administrators.",
                            "link": "https://example.test/CVE-2026-1111",
                        },
                        {
                            "title": "Patch fixes RCE in CVE-2026-3333",
                            "summary": "Remote code execution issue fixed in a routine update.",
                            "link": "https://example.test/CVE-2026-3333",
                        },
                        {
                            "title": "Active exploitation of CVE-2026-2222",
                            "summary": "Attackers are exploiting the issue in the wild.",
                            "link": "https://example.test/CVE-2026-2222",
                        },
                    ],
                    config={
                        "analysis": {
                            "model": "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free"
                        }
                    },
                )
            )

        self.assertEqual(result["cves_identified"], ["CVE-2026-2222"])

    def test_analysis_result_ignores_negated_exploitation_cves(self):
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
                            "title": "CVE-2026-1111 advisory",
                            "summary": "No evidence that CVE-2026-1111 has been exploited in the wild.",
                            "link": "https://example.test/CVE-2026-1111",
                        },
                        {
                            "title": "Active exploitation of CVE-2026-2222",
                            "summary": "Attackers are exploiting CVE-2026-2222 in the wild.",
                            "link": "https://example.test/CVE-2026-2222",
                        },
                    ],
                    config={
                        "analysis": {
                            "model": "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free"
                        }
                    },
                )
            )

        self.assertEqual(result["cves_identified"], ["CVE-2026-2222"])

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

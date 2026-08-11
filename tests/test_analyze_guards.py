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

    openai_client_module = types.ModuleType("src.core.openai_client")

    class OpenAIUnavailable(RuntimeError):
        pass

    class OpenAIClient:
        pass

    openai_client_module.OpenAIClient = OpenAIClient
    openai_client_module.OpenAIUnavailable = OpenAIUnavailable

    with patch.dict(
        sys.modules,
        {
            "src.core.openai_client": openai_client_module,
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
                            "model": "provider/model",
                        }
                    },
                )
            )

        self.assertIn("error", result)
        self.assertIn("OpenAI model ID", result["error"])
        self.assertIn("# Error: Invalid Model", result["exploitation_report"])

    def test_generates_report_through_openai(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenAIClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **kwargs):
                self.kwargs = kwargs
                assert kwargs["model"] == "gpt-5.6-sol"
                return "# Exploitation Report\n\nGenerated through OpenAI."

        analyze.build_model_client = lambda **kwargs: FakeOpenAIClient(**kwargs)

        with patch.dict(os.environ, {}, clear=True):
            result = asyncio.run(
                analyze.analyze_exploitation(
                    articles=[],
                    config={"analysis": {"model": "gpt-5.6-sol"}},
                )
            )

        self.assertNotIn("error", result)
        self.assertIn("Generated through OpenAI", result["exploitation_report"])

    def test_unavailable_openai_api_returns_skip_result(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenAIClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **_kwargs):
                raise analyze.OpenAIUnavailable("OpenAI API unavailable")

        analyze.build_model_client = lambda **kwargs: FakeOpenAIClient(**kwargs)

        with patch.dict(os.environ, {}, clear=True):
            result = asyncio.run(
                analyze.analyze_exploitation(
                    articles=[],
                    config={"analysis": {"model": "gpt-5.6-sol"}},
                )
            )

        self.assertTrue(result["skipped"])
        self.assertEqual(result["skip_reason"], "OpenAI API unavailable")
        self.assertNotIn("error", result)

    def test_article_prompt_omits_empty_source_and_url_fields(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenAIClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **kwargs):
                user_prompt = kwargs["user_prompt"]
                self.__class__.user_prompt = user_prompt
                return "# Exploitation Report\n\nGenerated through OpenAI."

        analyze.build_model_client = lambda **kwargs: FakeOpenAIClient(**kwargs)

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
                    config={"analysis": {"model": "gpt-5.6-sol"}},
                )
            )

        self.assertIn("**Untitled article**", FakeOpenAIClient.user_prompt)
        self.assertIn("Summary only...", FakeOpenAIClient.user_prompt)
        self.assertNotIn("(Source: )", FakeOpenAIClient.user_prompt)
        self.assertNotIn("URL: \n", FakeOpenAIClient.user_prompt)

    def test_analysis_result_extracts_cves_from_article_text(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenAIClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **_kwargs):
                return "# Exploitation Report\n\nGenerated through OpenAI."

        analyze.build_model_client = lambda **kwargs: FakeOpenAIClient(**kwargs)

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
                    config={"analysis": {"model": "gpt-5.6-sol"}},
                )
            )

        self.assertEqual(
            sorted(result["cves_identified"]),
            [
                "CVE-2026-2222",
                "CVE-2026-5555",
            ],
        )
        self.assertNotIn("CVE-2026-4444", result["cves_identified"])

    def test_analysis_result_ignores_patch_only_cves_for_expected_coverage(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenAIClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **_kwargs):
                return "# Exploitation Report\n\nGenerated through OpenAI."

        analyze.build_model_client = lambda **kwargs: FakeOpenAIClient(**kwargs)

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
                    config={"analysis": {"model": "gpt-5.6-sol"}},
                )
            )

        self.assertEqual(result["cves_identified"], ["CVE-2026-2222"])

    def test_analysis_result_ignores_negated_exploitation_cves(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenAIClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **_kwargs):
                return "# Exploitation Report\n\nGenerated through OpenAI."

        analyze.build_model_client = lambda **kwargs: FakeOpenAIClient(**kwargs)

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
                    config={"analysis": {"model": "gpt-5.6-sol"}},
                )
            )

        self.assertEqual(result["cves_identified"], ["CVE-2026-2222"])

    def test_analysis_result_keeps_exploited_cve_near_unrelated_negation(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenAIClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **_kwargs):
                return "# Exploitation Report\n\nGenerated through OpenAI."

        analyze.build_model_client = lambda **kwargs: FakeOpenAIClient(**kwargs)

        with patch.dict(os.environ, {}, clear=True):
            result = asyncio.run(
                analyze.analyze_exploitation(
                    articles=[
                        {
                            "title": "Active exploitation of CVE-2026-1111",
                            "summary": (
                                "Attackers are exploiting CVE-2026-1111 in the wild. "
                                "No evidence that CVE-2026-2222 has been exploited."
                            ),
                            "link": "https://example.test/report",
                        }
                    ],
                    config={"analysis": {"model": "gpt-5.6-sol"}},
                )
            )

        self.assertEqual(result["cves_identified"], ["CVE-2026-1111"])

    def test_analysis_result_keeps_unpatched_exploited_cve(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenAIClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **_kwargs):
                return "# Exploitation Report\n\nGenerated through OpenAI."

        analyze.build_model_client = lambda **kwargs: FakeOpenAIClient(**kwargs)

        with patch.dict(os.environ, {}, clear=True):
            result = asyncio.run(
                analyze.analyze_exploitation(
                    articles=[
                        {
                            "title": "Vendor zero-day under attack",
                            "summary": (
                                "CVE-2026-1111 is not yet patched and is being "
                                "exploited in the wild."
                            ),
                            "link": "https://example.test/report",
                        }
                    ],
                    config={"analysis": {"model": "gpt-5.6-sol"}},
                )
            )

        self.assertEqual(result["cves_identified"], ["CVE-2026-1111"])

    def test_analysis_result_includes_present_tense_exploit_cve(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenAIClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **_kwargs):
                return "# Exploitation Report\n\nGenerated through OpenAI."

        analyze.build_model_client = lambda **kwargs: FakeOpenAIClient(**kwargs)

        with patch.dict(os.environ, {}, clear=True):
            result = asyncio.run(
                analyze.analyze_exploitation(
                    articles=[
                        {
                            "title": "Attackers exploit vendor service",
                            "summary": "Attackers exploit CVE-2026-1111 to gain access.",
                            "link": "https://example.test/report",
                        }
                    ],
                    config={"analysis": {"model": "gpt-5.6-sol"}},
                )
            )

        self.assertEqual(result["cves_identified"], ["CVE-2026-1111"])

    def test_analysis_result_keeps_unauthenticated_exploited_cve(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenAIClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **_kwargs):
                return "# Exploitation Report\n\nGenerated through OpenAI."

        analyze.build_model_client = lambda **kwargs: FakeOpenAIClient(**kwargs)

        with patch.dict(os.environ, {}, clear=True):
            result = asyncio.run(
                analyze.analyze_exploitation(
                    articles=[
                        {
                            "title": "Unauthenticated zero-day exploited",
                            "summary": (
                                "Without authentication, attackers are exploiting "
                                "CVE-2026-1111 in the wild."
                            ),
                            "link": "https://example.test/report",
                        }
                    ],
                    config={"analysis": {"model": "gpt-5.6-sol"}},
                )
            )

        self.assertEqual(result["cves_identified"], ["CVE-2026-1111"])

    def test_analysis_result_ignores_directly_negated_cve_exploitation(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenAIClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **_kwargs):
                return "# Exploitation Report\n\nGenerated through OpenAI."

        analyze.build_model_client = lambda **kwargs: FakeOpenAIClient(**kwargs)

        with patch.dict(os.environ, {}, clear=True):
            result = asyncio.run(
                analyze.analyze_exploitation(
                    articles=[
                        {
                            "title": "Vendor advisory",
                            "summary": "CVE-2026-1111 is not exploited in the wild.",
                            "link": "https://example.test/report",
                        }
                    ],
                    config={"analysis": {"model": "gpt-5.6-sol"}},
                )
            )

        self.assertEqual(result["cves_identified"], [])

    def test_analysis_result_ignores_without_evidence_cve_exploitation(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenAIClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **_kwargs):
                return "# Exploitation Report\n\nGenerated through OpenAI."

        analyze.build_model_client = lambda **kwargs: FakeOpenAIClient(**kwargs)

        with patch.dict(os.environ, {}, clear=True):
            result = asyncio.run(
                analyze.analyze_exploitation(
                    articles=[
                        {
                            "title": "Vendor advisory",
                            "summary": (
                                "CVE-2026-1111 was disclosed without evidence of "
                                "exploitation in the wild."
                            ),
                            "link": "https://example.test/report",
                        }
                    ],
                    config={"analysis": {"model": "gpt-5.6-sol"}},
                )
            )

        self.assertEqual(result["cves_identified"], [])

    def test_analysis_result_includes_metadata_cve_for_exploited_article(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenAIClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **_kwargs):
                return "# Exploitation Report\n\nGenerated through OpenAI."

        analyze.build_model_client = lambda **kwargs: FakeOpenAIClient(**kwargs)

        with patch.dict(os.environ, {}, clear=True):
            result = asyncio.run(
                analyze.analyze_exploitation(
                    articles=[
                        {
                            "title": "Vendor product exploited in the wild",
                            "summary": "Attackers are exploiting the product.",
                            "link": "https://example.test/advisory",
                            "cves": ["CVE-2026-1111"],
                        }
                    ],
                    config={"analysis": {"model": "gpt-5.6-sol"}},
                )
            )

        self.assertEqual(result["cves_identified"], ["CVE-2026-1111"])

    def test_analysis_result_includes_url_cve_for_exploited_article(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenAIClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **_kwargs):
                return "# Exploitation Report\n\nGenerated through OpenAI."

        analyze.build_model_client = lambda **kwargs: FakeOpenAIClient(**kwargs)

        with patch.dict(os.environ, {}, clear=True):
            result = asyncio.run(
                analyze.analyze_exploitation(
                    articles=[
                        {
                            "title": "Vendor product exploited in the wild",
                            "summary": "Attackers are exploiting the product.",
                            "link": "https://example.test/CVE-2026-1111",
                        }
                    ],
                    config={"analysis": {"model": "gpt-5.6-sol"}},
                )
            )

        self.assertEqual(result["cves_identified"], ["CVE-2026-1111"])

    def test_analysis_result_does_not_require_all_mixed_metadata_cves(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenAIClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **_kwargs):
                return "# Exploitation Report\n\nGenerated through OpenAI."

        analyze.build_model_client = lambda **kwargs: FakeOpenAIClient(**kwargs)

        with patch.dict(os.environ, {}, clear=True):
            result = asyncio.run(
                analyze.analyze_exploitation(
                    articles=[
                        {
                            "title": "Vendor advisory with active exploitation",
                            "summary": (
                                "Attackers are exploiting CVE-2026-1111 in the wild. "
                                "No evidence that CVE-2026-2222 has been exploited."
                            ),
                            "link": "https://example.test/advisory",
                            "cves": ["CVE-2026-1111", "CVE-2026-2222"],
                        }
                    ],
                    config={"analysis": {"model": "gpt-5.6-sol"}},
                )
            )

        self.assertEqual(result["cves_identified"], ["CVE-2026-1111"])

    def test_analysis_result_filters_negated_metadata_cves_individually(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenAIClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **_kwargs):
                return "# Exploitation Report\n\nGenerated through OpenAI."

        analyze.build_model_client = lambda **kwargs: FakeOpenAIClient(**kwargs)

        with patch.dict(os.environ, {}, clear=True):
            result = asyncio.run(
                analyze.analyze_exploitation(
                    articles=[
                        {
                            "title": "Two zero-days exploited in the wild",
                            "summary": (
                                "Attackers are exploiting one listed issue. "
                                "No evidence that CVE-2026-2222 has been exploited."
                            ),
                            "link": "https://example.test/advisory",
                            "cves": ["CVE-2026-1111", "CVE-2026-2222"],
                        }
                    ],
                    config={"analysis": {"model": "gpt-5.6-sol"}},
                )
            )

        self.assertEqual(result["cves_identified"], ["CVE-2026-1111"])

    def test_analysis_result_includes_multi_metadata_cves_when_none_negated(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenAIClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **_kwargs):
                return "# Exploitation Report\n\nGenerated through OpenAI."

        analyze.build_model_client = lambda **kwargs: FakeOpenAIClient(**kwargs)

        with patch.dict(os.environ, {}, clear=True):
            result = asyncio.run(
                analyze.analyze_exploitation(
                    articles=[
                        {
                            "title": "Two zero-days exploited in the wild",
                            "summary": "Attackers are exploiting both issues.",
                            "link": "https://example.test/advisory",
                            "cves": ["CVE-2026-1111", "CVE-2026-2222"],
                        }
                    ],
                    config={"analysis": {"model": "gpt-5.6-sol"}},
                )
            )

        self.assertEqual(
            sorted(result["cves_identified"]),
            ["CVE-2026-1111", "CVE-2026-2222"],
        )

    def test_prompt_requires_source_attribution_from_article_metadata(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenAIClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **kwargs):
                self.__class__.user_prompt = kwargs["user_prompt"]
                return "# Exploitation Report\n\nGenerated through OpenAI."

        analyze.build_model_client = lambda **kwargs: FakeOpenAIClient(**kwargs)

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
                    config={"analysis": {"model": "gpt-5.6-sol"}},
                )
            )

        self.assertIn("## Source Attribution", FakeOpenAIClient.user_prompt)
        self.assertIn(
            "Only use source names and URLs provided",
            FakeOpenAIClient.user_prompt,
        )
        self.assertIn("Example exploitation report", FakeOpenAIClient.user_prompt)
        self.assertIn("Example Source", FakeOpenAIClient.user_prompt)
        self.assertIn("https://example.test/report", FakeOpenAIClient.user_prompt)

    def test_analysis_result_carries_canonical_source_attribution_entries(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenAIClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **_kwargs):
                return "# Exploitation Report\n\nGenerated through OpenAI."

        analyze.build_model_client = lambda **kwargs: FakeOpenAIClient(**kwargs)

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
                    config={"analysis": {"model": "gpt-5.6-sol"}},
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

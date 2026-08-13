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

    class ModelSelection:
        def __init__(self, provider_id="", model_id=""):
            self.provider_id = provider_id
            self.model_id = model_id

    def parse_model_selection(model_name):
        provider_id, model_id = model_name.split("/", 1)
        return types.SimpleNamespace(provider_id=provider_id, model_id=model_id)

    opencode_client_module.OpenCodeClient = OpenCodeClient
    opencode_client_module.OpenCodeUnavailable = OpenCodeUnavailable
    opencode_client_module.ModelSelection = ModelSelection
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

        analyze.build_model_client = lambda **kwargs: FakeOpenCodeClient(**kwargs)

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

        analyze.build_model_client = lambda **kwargs: FakeOpenCodeClient(**kwargs)

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

        analyze.build_model_client = lambda **kwargs: FakeOpenCodeClient(**kwargs)

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
        self.assertIn("Summary only", FakeOpenCodeClient.user_prompt)
        self.assertNotIn("Summary only...", FakeOpenCodeClient.user_prompt)
        self.assertNotIn("(Source: )", FakeOpenCodeClient.user_prompt)
        self.assertNotIn("URL: \n", FakeOpenCodeClient.user_prompt)

    def test_article_summary_omits_unknown_source_sentinel(self):
        analyze = import_analyze_with_stubs()

        summary = analyze.format_article_summary(
            {
                "title": "Example report",
                "source": " Unknown\n Source ",
                "summary": "Summary only",
            }
        )

        self.assertNotIn("Source:", summary)

    def test_article_summary_collapses_source_whitespace(self):
        analyze = import_analyze_with_stubs()

        summary = analyze.format_article_summary(
            {
                "title": "Example report",
                "source": "Example\n Research\tTeam",
                "summary": "Summary only",
            }
        )

        self.assertIn("Source: Example Research Team", summary)

    def test_analysis_result_extracts_cves_from_article_text(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenCodeClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **_kwargs):
                return "# Exploitation Report\n\nGenerated through OpenCode."

        analyze.build_model_client = lambda **kwargs: FakeOpenCodeClient(**kwargs)

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
                "CVE-2026-2222",
                "CVE-2026-5555",
            ],
        )
        self.assertNotIn("CVE-2026-4444", result["cves_identified"])

    def test_structured_cves_omit_truncated_identifiers(self):
        analyze = import_analyze_with_stubs()

        self.assertEqual(
            analyze.collect_structured_cves(
                {
                    "cves": [
                        "CVE-2026-593...",
                        "CVE-2026-59310",
                        "CVE-2026-59310",
                    ]
                }
            ),
            ["CVE-2026-59310"],
        )
        self.assertEqual(analyze.collect_structured_cves({"cves": None}), [])

    def test_prompt_includes_source_derived_cve_metadata(self):
        analyze = import_analyze_with_stubs()

        article_summary = analyze.format_article_summary(
            {
                "title": "VMware issue exploited in the wild",
                "summary": "The RSS value ends at CVE-2026-593...",
                "content": "Attackers gained access through the vulnerable service.",
                "cves": ["CVE-2026-59310"],
            }
        )

        self.assertIn("CVEs: CVE-2026-59310", article_summary)
        self.assertNotIn("CVEs: CVE-2026-593...", article_summary)

    def test_analysis_result_ignores_patch_only_cves_for_expected_coverage(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenCodeClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **_kwargs):
                return "# Exploitation Report\n\nGenerated through OpenCode."

        analyze.build_model_client = lambda **kwargs: FakeOpenCodeClient(**kwargs)

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

        analyze.build_model_client = lambda **kwargs: FakeOpenCodeClient(**kwargs)

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

    def test_analysis_result_ignores_unconfirmed_source_metadata_cve(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenCodeClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **_kwargs):
                return "# Exploitation Report\n\nGenerated through OpenCode."

        analyze.build_model_client = lambda **kwargs: FakeOpenCodeClient(**kwargs)

        with patch.dict(os.environ, {}, clear=True):
            result = asyncio.run(
                analyze.analyze_exploitation(
                    articles=[
                        {
                            "title": "Vendor activity under investigation",
                            "summary": (
                                "Scanning is indicative of potential exploitation "
                                "efforts targeting CVE-2026-1111."
                            ),
                            "link": "https://example.test/report",
                            "cves": ["CVE-2026-1111"],
                        }
                    ],
                    config={
                        "analysis": {
                            "model": "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free"
                        }
                    },
                )
            )

        self.assertEqual(result["cves_identified"], [])

    def test_cve_context_includes_following_exploitation_sentence(self):
        analyze = import_analyze_with_stubs()
        article_summary = (
            "**Vendor advisory** (CVEs: CVE-2026-1234)\n\n"
            "CVE-2026-1234 allows remote code execution. "
            "Attackers are actively exploiting this flaw."
        )

        self.assertEqual(
            analyze.collect_exploitation_relevant_prompt_cves(article_summary),
            ["CVE-2026-1234"],
        )

    def test_cve_context_includes_referential_preceding_exploitation_sentence(self):
        analyze = import_analyze_with_stubs()
        article_summary = (
            "**Vendor advisory** (CVEs: CVE-2026-1234)\n\n"
            "Attackers are actively exploiting a flaw in Product X. "
            "The flaw is tracked as CVE-2026-1234."
        )

        self.assertEqual(
            analyze.collect_exploitation_relevant_prompt_cves(article_summary),
            ["CVE-2026-1234"],
        )

    def test_modal_capability_does_not_mask_confirmed_exploitation_clause(self):
        analyze = import_analyze_with_stubs()
        article_summary = (
            "The flaw can allow remote code execution, and attackers are actively "
            "exploiting CVE-2026-1234."
        )

        self.assertEqual(
            analyze.collect_exploitation_relevant_prompt_cves(article_summary),
            ["CVE-2026-1234"],
        )

    def test_hypothetical_exploit_clause_does_not_mask_confirmed_clause(self):
        analyze = import_analyze_with_stubs()
        article_summary = (
            "The flaw could be exploited to gain access, but attackers are actively "
            "exploiting CVE-2026-1234."
        )

        self.assertEqual(
            analyze.collect_exploitation_relevant_prompt_cves(article_summary),
            ["CVE-2026-1234"],
        )

    def test_adversative_without_comma_still_separates_confirmed_clause(self):
        analyze = import_analyze_with_stubs()
        article_summary = (
            "The flaw could be exploited to gain access but attackers are actively "
            "exploiting CVE-2026-1234."
        )

        self.assertEqual(
            analyze.collect_exploitation_relevant_prompt_cves(article_summary),
            ["CVE-2026-1234"],
        )

    def test_unpunctuated_and_separates_actor_led_exploitation_clause(self):
        analyze = import_analyze_with_stubs()
        article_summary = (
            "CVE-2026-1111 is not exploited and attackers actively exploit "
            "CVE-2026-2222."
        )

        self.assertEqual(
            analyze.collect_exploitation_relevant_prompt_cves(article_summary),
            ["CVE-2026-2222"],
        )

    def test_short_prompt_content_does_not_make_final_cve_look_truncated(self):
        analyze = import_analyze_with_stubs()
        article_summary = analyze.format_article_summary(
            {
                "title": "Active exploitation",
                "content": (
                    "Attackers actively exploit CVE-2026-1111 and CVE-2026-2222"
                ),
                "cves": ["CVE-2026-1111", "CVE-2026-2222"],
            }
        )

        self.assertEqual(
            analyze.collect_exploitation_relevant_prompt_cves(article_summary),
            ["CVE-2026-1111", "CVE-2026-2222"],
        )

    def test_exploitation_capability_wording_is_not_confirmed_activity(self):
        analyze = import_analyze_with_stubs()
        for article_summary in (
            "Exploitation of CVE-2026-1234 can lead to remote code execution.",
            "Successful exploitation of CVE-2026-1234 would allow remote code execution.",
        ):
            with self.subTest(article_summary=article_summary):
                self.assertEqual(
                    analyze.collect_exploitation_relevant_prompt_cves(article_summary),
                    [],
                )

    def test_no_known_exploitation_wording_is_negated(self):
        analyze = import_analyze_with_stubs()
        article_summary = "There is no known exploitation of CVE-2026-1234."

        self.assertEqual(
            analyze.collect_exploitation_relevant_prompt_cves(article_summary),
            [],
        )

    def test_exploitation_before_negation_wording_is_negated(self):
        analyze = import_analyze_with_stubs()

        for article_summary in (
            "Exploitation has not been observed for CVE-2026-1234.",
            "No exploitation of CVE-2026-1234 has been observed.",
        ):
            with self.subTest(article_summary=article_summary):
                self.assertEqual(
                    analyze.collect_exploitation_relevant_prompt_cves(article_summary),
                    [],
                )

    def test_not_known_to_have_been_exploited_wording_is_negated(self):
        analyze = import_analyze_with_stubs()
        article_summary = "CVE-2026-1111 is not known to have been exploited."

        self.assertEqual(
            analyze.collect_exploitation_relevant_prompt_cves(article_summary),
            [],
        )

    def test_adverbial_exploitation_negations_are_excluded(self):
        analyze = import_analyze_with_stubs()

        for article_summary in (
            "CVE-2026-1234 is not currently being exploited.",
            "CVE-2026-1234 is not yet exploited.",
            "CVE-2026-1234 is not actively being exploited.",
            "CVE-2026-1234 has not yet been exploited.",
            "CVE-2026-1234 is not being actively exploited.",
        ):
            with self.subTest(article_summary=article_summary):
                self.assertEqual(
                    analyze.collect_exploitation_relevant_prompt_cves(article_summary),
                    [],
                )

    def test_ceased_exploitation_wording_is_excluded(self):
        analyze = import_analyze_with_stubs()

        for article_summary in (
            "CVE-2026-1234 is no longer actively exploited.",
            "CVE-2026-1234 is no longer being exploited.",
        ):
            with self.subTest(article_summary=article_summary):
                self.assertEqual(
                    analyze.collect_exploitation_relevant_prompt_cves(article_summary),
                    [],
                )

    def test_explicit_impossibility_wording_is_excluded(self):
        analyze = import_analyze_with_stubs()

        for article_summary in (
            "CVE-2026-1234 cannot be exploited remotely.",
            "CVE-2026-1234 can't be exploited remotely.",
            "CVE-2026-1234 could not be exploited in testing.",
            "CVE-2026-1234 is unable to be exploited remotely.",
            "CVE-2026-1234 is not possible to exploit remotely.",
            "CVE-2026-1234 is impossible to exploit remotely.",
        ):
            with self.subTest(article_summary=article_summary):
                self.assertEqual(
                    analyze.collect_exploitation_relevant_prompt_cves(article_summary),
                    [],
                )

    def test_contrastive_while_keeps_confirmed_cve_separate_from_negation(self):
        analyze = import_analyze_with_stubs()
        article_summary = (
            "CVE-2026-1111 is actively exploited, while CVE-2026-2222 is not "
            "exploited."
        )

        self.assertEqual(
            analyze.collect_exploitation_relevant_prompt_cves(article_summary),
            ["CVE-2026-1111"],
        )

    def test_contrastive_not_cve_shorthand_excludes_the_second_cve(self):
        analyze = import_analyze_with_stubs()
        article_summary = "Only CVE-2026-1111 is actively exploited, not CVE-2026-2222."

        self.assertEqual(
            analyze.collect_exploitation_relevant_prompt_cves(article_summary),
            ["CVE-2026-1111"],
        )

    def test_body_level_cve_label_remains_available_for_context_analysis(self):
        analyze = import_analyze_with_stubs()
        article_summary = (
            "**Vendor advisory** (Source: Vendor)\n\n"
            "Affected CVEs: CVE-2026-1111 and CVE-2026-2222 are actively exploited."
        )

        self.assertEqual(
            analyze.collect_exploitation_relevant_prompt_cves(article_summary),
            ["CVE-2026-1111", "CVE-2026-2222"],
        )

    def test_coordinated_cve_subjects_share_exploitation_predicate(self):
        analyze = import_analyze_with_stubs()

        for article_summary, expected_cves in (
            (
                "CVE-2026-1111, and CVE-2026-2222 are actively exploited.",
                ["CVE-2026-1111", "CVE-2026-2222"],
            ),
            (
                "CVE-2026-1111, CVE-2026-2222, and CVE-2026-3333 are "
                "actively exploited.",
                ["CVE-2026-1111", "CVE-2026-2222", "CVE-2026-3333"],
            ),
        ):
            with self.subTest(article_summary=article_summary):
                self.assertEqual(
                    analyze.collect_exploitation_relevant_prompt_cves(article_summary),
                    expected_cves,
                )

    def test_neither_nor_cve_subjects_are_negated(self):
        analyze = import_analyze_with_stubs()
        article_summary = (
            "Neither CVE-2026-1111 nor CVE-2026-2222 is actively exploited."
        )

        self.assertEqual(
            analyze.collect_exploitation_relevant_prompt_cves(article_summary),
            [],
        )

    def test_later_referential_exploitation_overrides_earlier_negative_state(self):
        analyze = import_analyze_with_stubs()
        article_summary = (
            "**Vendor advisory** (CVEs: CVE-2026-1234)\n\n"
            "CVE-2026-1234 was not exploited previously. "
            "It is now actively exploited in the wild."
        )

        self.assertEqual(
            analyze.collect_exploitation_relevant_prompt_cves(article_summary),
            ["CVE-2026-1234"],
        )

    def test_referential_exploitation_skips_intervening_neutral_sentence(self):
        analyze = import_analyze_with_stubs()
        article_summary = (
            "**Vendor advisory** (CVEs: CVE-2026-1234)\n\n"
            "CVE-2026-1234 affects Product X. A patch is available. "
            "Attackers are actively exploiting the vulnerability."
        )

        self.assertEqual(
            analyze.collect_exploitation_relevant_prompt_cves(article_summary),
            ["CVE-2026-1234"],
        )

    def test_referential_negation_skips_intervening_neutral_sentence(self):
        analyze = import_analyze_with_stubs()
        article_summary = (
            "**Vendor advisory** (CVEs: CVE-2026-1234)\n\n"
            "CVE-2026-1234 affects Product X. A patch is available. "
            "The vulnerability is not currently being exploited."
        )

        self.assertEqual(
            analyze.collect_exploitation_relevant_prompt_cves(article_summary),
            [],
        )

    def test_referential_scan_stops_at_new_unnamed_vulnerability(self):
        analyze = import_analyze_with_stubs()
        article_summary = (
            "**Vendor advisory** (CVEs: CVE-2026-1234)\n\n"
            "CVE-2026-1234 affects Product X. A separate vulnerability was "
            "disclosed. It is actively exploited."
        )

        self.assertEqual(
            analyze.collect_exploitation_relevant_prompt_cves(article_summary),
            [],
        )

    def test_demonstrative_new_vulnerability_still_refers_to_prior_cve(self):
        analyze = import_analyze_with_stubs()
        article_summary = (
            "**Vendor advisory** (CVEs: CVE-2026-1234)\n\n"
            "CVE-2026-1234 was disclosed. This new vulnerability is actively "
            "exploited."
        )

        self.assertEqual(
            analyze.collect_exploitation_relevant_prompt_cves(article_summary),
            ["CVE-2026-1234"],
        )

    def test_plural_reference_promotes_coordinated_cves(self):
        analyze = import_analyze_with_stubs()
        article_summary = (
            "**Vendor advisory** (CVEs: CVE-2026-1111, CVE-2026-2222)\n\n"
            "CVE-2026-1111 and CVE-2026-2222 affect Product X. "
            "They are actively exploited."
        )

        self.assertEqual(
            analyze.collect_exploitation_relevant_prompt_cves(article_summary),
            ["CVE-2026-1111", "CVE-2026-2222"],
        )

    def test_modal_malware_impact_is_not_confirmed_exploitation(self):
        analyze = import_analyze_with_stubs()
        article_summary = "CVE-2026-1234 could allow malware installation."

        self.assertEqual(
            analyze.collect_exploitation_relevant_prompt_cves(article_summary),
            [],
        )

    def test_confirmed_exploitation_survives_modal_malware_impact(self):
        analyze = import_analyze_with_stubs()
        article_summary = (
            "CVE-2026-1234 is actively exploited and could allow malware installation."
        )

        self.assertEqual(
            analyze.collect_exploitation_relevant_prompt_cves(article_summary),
            ["CVE-2026-1234"],
        )

    def test_cve_led_coordinating_clause_keeps_confirmed_cve_separate(self):
        analyze = import_analyze_with_stubs()
        article_summary = (
            "CVE-2026-1111 is actively exploited and CVE-2026-2222 is not exploited."
        )

        self.assertEqual(
            analyze.collect_exploitation_relevant_prompt_cves(article_summary),
            ["CVE-2026-1111"],
        )

    def test_multiline_title_keeps_generated_cve_metadata_parseable(self):
        analyze = import_analyze_with_stubs()
        article_summary = analyze.format_article_summary(
            {
                "title": "Vendor\nAdvisory",
                "content": "Attackers actively exploit the flaw.",
                "cves": ["CVE-2026-1234"],
            }
        )

        self.assertIn("**Vendor Advisory**", article_summary)
        self.assertEqual(
            analyze.collect_exploitation_relevant_prompt_cves(article_summary),
            ["CVE-2026-1234"],
        )

    def test_negated_grouped_quantifier_does_not_promote_all_metadata_cves(self):
        analyze = import_analyze_with_stubs()
        article_summary = (
            "**Vendor advisory** (CVEs: CVE-2026-1111, CVE-2026-2222)\n\n"
            "Not all vulnerabilities are actively exploited."
        )

        self.assertEqual(
            analyze.collect_exploitation_relevant_prompt_cves(article_summary),
            [],
        )

    def test_referential_and_clause_overrides_earlier_negative_state(self):
        analyze = import_analyze_with_stubs()
        article_summary = (
            "CVE-2026-1234 was not exploited previously and it is now actively "
            "exploited in the wild."
        )

        self.assertEqual(
            analyze.collect_exploitation_relevant_prompt_cves(article_summary),
            ["CVE-2026-1234"],
        )

    def test_never_exploited_wording_is_negated(self):
        analyze = import_analyze_with_stubs()
        article_summary = "CVE-2026-1234 has never been exploited."

        self.assertEqual(
            analyze.collect_exploitation_relevant_prompt_cves(article_summary),
            [],
        )

    def test_punctuation_splits_positive_cve_clause_from_prior_negation(self):
        analyze = import_analyze_with_stubs()
        article_summary = (
            "No vulnerabilities were exploited previously; "
            "CVE-2026-1111 is now actively exploited."
        )

        self.assertEqual(
            analyze.collect_exploitation_relevant_prompt_cves(article_summary),
            ["CVE-2026-1111"],
        )

    def test_decimal_version_does_not_split_cve_from_exploitation_context(self):
        analyze = import_analyze_with_stubs()
        article_summary = "CVE-2026-1234 affects Product 1.2 and is actively exploited."

        self.assertEqual(
            analyze.collect_exploitation_relevant_prompt_cves(article_summary),
            ["CVE-2026-1234"],
        )

    def test_following_referential_negation_cancels_zero_day_label(self):
        analyze = import_analyze_with_stubs()
        article_summary = (
            "CVE-2026-1234 is a zero-day vulnerability, but it has not been exploited."
        )

        self.assertEqual(
            analyze.collect_exploitation_relevant_prompt_cves(article_summary),
            [],
        )

    def test_plural_reference_promotes_all_metadata_cves(self):
        analyze = import_analyze_with_stubs()

        for body in (
            "Both are actively exploited in the wild.",
            "The vulnerabilities are actively exploited in the wild.",
        ):
            with self.subTest(body=body):
                article_summary = (
                    "**Vendor advisory** "
                    "(CVEs: CVE-2026-1111, CVE-2026-2222)\n\n" + body
                )
                self.assertEqual(
                    analyze.collect_exploitation_relevant_prompt_cves(article_summary),
                    ["CVE-2026-1111", "CVE-2026-2222"],
                )

    def test_proof_of_concept_exploit_is_not_confirmed_activity(self):
        analyze = import_analyze_with_stubs()

        for article_summary in (
            "A proof-of-concept exploit for CVE-2026-1234 is publicly available.",
            "A PoC exploit for CVE-2026-1234 is available.",
        ):
            with self.subTest(article_summary=article_summary):
                self.assertEqual(
                    analyze.collect_exploitation_relevant_prompt_cves(article_summary),
                    [],
                )

    def test_probabilistic_exploitation_is_not_confirmed_activity(self):
        analyze = import_analyze_with_stubs()

        for article_summary in (
            "Exploitation of CVE-2026-1234 is likely.",
            "Exploitation of CVE-2026-1234 is suspected.",
            "Exploitation of CVE-2026-1234 remains unconfirmed.",
        ):
            with self.subTest(article_summary=article_summary):
                self.assertEqual(
                    analyze.collect_exploitation_relevant_prompt_cves(article_summary),
                    [],
                )

    def test_interrogative_exploitation_headline_is_not_confirmed_activity(self):
        analyze = import_analyze_with_stubs()
        article_summary = (
            "**Is CVE-2026-1234 actively exploited?**\n\n"
            "There is no evidence of exploitation in the wild."
        )

        self.assertEqual(
            analyze.collect_exploitation_relevant_prompt_cves(article_summary),
            [],
        )

    def test_preverbal_uncertainty_is_not_confirmed_activity(self):
        analyze = import_analyze_with_stubs()

        for article_summary in (
            "CVE-2026-1234 is suspected to be exploited.",
            "CVE-2026-1234 is believed to be exploited.",
            "CVE-2026-1234 is reported to be exploited.",
        ):
            with self.subTest(article_summary=article_summary):
                self.assertEqual(
                    analyze.collect_exploitation_relevant_prompt_cves(article_summary),
                    [],
                )

    def test_contextual_cve_match_rejects_unicode_ellipsis(self):
        analyze = import_analyze_with_stubs()
        article_summary = "Attackers actively exploit CVE-2026-1234… in the wild."

        self.assertEqual(
            analyze.collect_exploitation_relevant_prompt_cves(article_summary),
            [],
        )

    def test_month_name_does_not_make_confirmed_exploitation_unconfirmed(self):
        analyze = import_analyze_with_stubs()
        article_summary = "The May campaign exploited CVE-2026-1234."

        self.assertEqual(
            analyze.collect_exploitation_relevant_prompt_cves(article_summary),
            ["CVE-2026-1234"],
        )

    def test_following_sentence_does_not_transfer_another_cve_exploitation(self):
        analyze = import_analyze_with_stubs()
        article_summary = (
            "**Vendor advisory** (CVEs: CVE-2026-1111, CVE-2026-2222)\n\n"
            "CVE-2026-1111 allows remote code execution. "
            "Attackers are exploiting CVE-2026-2222."
        )

        self.assertEqual(
            analyze.collect_exploitation_relevant_prompt_cves(article_summary),
            ["CVE-2026-2222"],
        )

    def test_contrasted_cves_are_evaluated_in_their_own_clauses(self):
        analyze = import_analyze_with_stubs()
        article_summary = (
            "**Vendor advisory** (CVEs: CVE-2026-1111, CVE-2026-2222)\n\n"
            "CVE-2026-1111 is not being exploited, but attackers are actively "
            "exploiting CVE-2026-2222."
        )

        self.assertEqual(
            analyze.collect_exploitation_relevant_prompt_cves(article_summary),
            ["CVE-2026-2222"],
        )

    def test_grouped_exploitation_preserves_contextual_and_contextless_cves(self):
        analyze = import_analyze_with_stubs()
        article_summary = (
            "**Vendor advisory** (CVEs: CVE-2026-1111, CVE-2026-2222)\n\n"
            "CVE-2026-1111 allows remote code execution. "
            "Both vulnerabilities are actively exploited."
        )

        self.assertEqual(
            analyze.collect_exploitation_relevant_prompt_cves(article_summary),
            ["CVE-2026-1111", "CVE-2026-2222"],
        )

    def test_grouped_cve_wording_preserves_all_metadata_cves(self):
        analyze = import_analyze_with_stubs()
        article_summary = (
            "**Vendor advisory** (CVEs: CVE-2026-1111, CVE-2026-2222)\n\n"
            "Both CVEs are actively exploited."
        )

        self.assertEqual(
            analyze.collect_exploitation_relevant_prompt_cves(article_summary),
            ["CVE-2026-1111", "CVE-2026-2222"],
        )

    def test_unrelated_grouped_patch_sentence_does_not_promote_all_cves(self):
        analyze = import_analyze_with_stubs()
        article_summary = (
            "**Vendor advisory** (CVEs: CVE-2026-1111, CVE-2026-2222)\n\n"
            "CVE-2026-1111 and CVE-2026-2222 affect the product. "
            "Both vulnerabilities are patched. "
            "Attackers actively exploit CVE-2026-1111."
        )

        self.assertEqual(
            analyze.collect_exploitation_relevant_prompt_cves(article_summary),
            ["CVE-2026-1111"],
        )

    def test_analysis_result_keeps_exploited_cve_near_unrelated_negation(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenCodeClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **_kwargs):
                return "# Exploitation Report\n\nGenerated through OpenCode."

        analyze.build_model_client = lambda **kwargs: FakeOpenCodeClient(**kwargs)

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
                    config={
                        "analysis": {
                            "model": "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free"
                        }
                    },
                )
            )

        self.assertEqual(result["cves_identified"], ["CVE-2026-1111"])

    def test_analysis_result_keeps_unpatched_exploited_cve(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenCodeClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **_kwargs):
                return "# Exploitation Report\n\nGenerated through OpenCode."

        analyze.build_model_client = lambda **kwargs: FakeOpenCodeClient(**kwargs)

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
                    config={
                        "analysis": {
                            "model": "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free"
                        }
                    },
                )
            )

        self.assertEqual(result["cves_identified"], ["CVE-2026-1111"])

    def test_analysis_result_includes_present_tense_exploit_cve(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenCodeClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **_kwargs):
                return "# Exploitation Report\n\nGenerated through OpenCode."

        analyze.build_model_client = lambda **kwargs: FakeOpenCodeClient(**kwargs)

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
                    config={
                        "analysis": {
                            "model": "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free"
                        }
                    },
                )
            )

        self.assertEqual(result["cves_identified"], ["CVE-2026-1111"])

    def test_analysis_result_keeps_unauthenticated_exploited_cve(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenCodeClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **_kwargs):
                return "# Exploitation Report\n\nGenerated through OpenCode."

        analyze.build_model_client = lambda **kwargs: FakeOpenCodeClient(**kwargs)

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
                    config={
                        "analysis": {
                            "model": "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free"
                        }
                    },
                )
            )

        self.assertEqual(result["cves_identified"], ["CVE-2026-1111"])

    def test_analysis_result_ignores_directly_negated_cve_exploitation(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenCodeClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **_kwargs):
                return "# Exploitation Report\n\nGenerated through OpenCode."

        analyze.build_model_client = lambda **kwargs: FakeOpenCodeClient(**kwargs)

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
                    config={
                        "analysis": {
                            "model": "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free"
                        }
                    },
                )
            )

        self.assertEqual(result["cves_identified"], [])

    def test_analysis_result_ignores_without_evidence_cve_exploitation(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenCodeClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **_kwargs):
                return "# Exploitation Report\n\nGenerated through OpenCode."

        analyze.build_model_client = lambda **kwargs: FakeOpenCodeClient(**kwargs)

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
                    config={
                        "analysis": {
                            "model": "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free"
                        }
                    },
                )
            )

        self.assertEqual(result["cves_identified"], [])

    def test_analysis_result_includes_metadata_cve_for_exploited_article(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenCodeClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **_kwargs):
                return "# Exploitation Report\n\nGenerated through OpenCode."

        analyze.build_model_client = lambda **kwargs: FakeOpenCodeClient(**kwargs)

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
                    config={
                        "analysis": {
                            "model": "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free"
                        }
                    },
                )
            )

        self.assertEqual(result["cves_identified"], ["CVE-2026-1111"])

    def test_analysis_result_includes_url_cve_for_exploited_article(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenCodeClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **_kwargs):
                return "# Exploitation Report\n\nGenerated through OpenCode."

        analyze.build_model_client = lambda **kwargs: FakeOpenCodeClient(**kwargs)

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
                    config={
                        "analysis": {
                            "model": "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free"
                        }
                    },
                )
            )

        self.assertEqual(result["cves_identified"], ["CVE-2026-1111"])

    def test_analysis_result_does_not_require_all_mixed_metadata_cves(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenCodeClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **_kwargs):
                return "# Exploitation Report\n\nGenerated through OpenCode."

        analyze.build_model_client = lambda **kwargs: FakeOpenCodeClient(**kwargs)

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
                    config={
                        "analysis": {
                            "model": "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free"
                        }
                    },
                )
            )

        self.assertEqual(result["cves_identified"], ["CVE-2026-1111"])

    def test_analysis_result_filters_negated_metadata_cves_individually(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenCodeClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **_kwargs):
                return "# Exploitation Report\n\nGenerated through OpenCode."

        analyze.build_model_client = lambda **kwargs: FakeOpenCodeClient(**kwargs)

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
                    config={
                        "analysis": {
                            "model": "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free"
                        }
                    },
                )
            )

        self.assertEqual(result["cves_identified"], ["CVE-2026-1111"])

    def test_analysis_result_includes_multi_metadata_cves_when_none_negated(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenCodeClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **_kwargs):
                return "# Exploitation Report\n\nGenerated through OpenCode."

        analyze.build_model_client = lambda **kwargs: FakeOpenCodeClient(**kwargs)

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
                    config={
                        "analysis": {
                            "model": "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free"
                        }
                    },
                )
            )

        self.assertEqual(
            sorted(result["cves_identified"]),
            ["CVE-2026-1111", "CVE-2026-2222"],
        )

    def test_prompt_does_not_request_source_attribution(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenCodeClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **kwargs):
                self.__class__.user_prompt = kwargs["user_prompt"]
                return "# Exploitation Report\n\nGenerated through OpenCode."

        analyze.build_model_client = lambda **kwargs: FakeOpenCodeClient(**kwargs)

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

        self.assertNotIn("## Source Attribution", FakeOpenCodeClient.user_prompt)
        self.assertNotIn("Source Attribution section", FakeOpenCodeClient.user_prompt)
        self.assertIn("Example exploitation report", FakeOpenCodeClient.user_prompt)
        self.assertIn("Example Source", FakeOpenCodeClient.user_prompt)
        self.assertIn("https://example.test/report", FakeOpenCodeClient.user_prompt)

    def test_analysis_result_omits_source_attribution_contract(self):
        analyze = import_analyze_with_stubs()

        class FakeOpenCodeClient:
            def __init__(self, **_kwargs):
                pass

            async def generate(self, **_kwargs):
                return "# Exploitation Report\n\nGenerated through OpenCode."

        analyze.build_model_client = lambda **kwargs: FakeOpenCodeClient(**kwargs)

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

        self.assertNotIn("source_attribution_required", result)
        self.assertNotIn("source_attribution_entries", result)
        self.assertNotIn("source_attribution_requirements", result)


if __name__ == "__main__":
    unittest.main()

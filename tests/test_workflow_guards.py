import asyncio
import importlib
import os
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import AsyncMock, patch

import pytest


def import_workflow_with_stubs(analysis_result=None):
    sys.modules.pop("src.core.workflow", None)

    graph_module = types.ModuleType("langgraph.graph")
    graph_module.START = "START"
    graph_module.END = "END"

    class StateGraph:
        def __init__(self, *_args, **_kwargs):
            pass

        def add_node(self, *_args, **_kwargs):
            pass

        def add_edge(self, *_args, **_kwargs):
            pass

        def add_conditional_edges(self, *_args, **_kwargs):
            pass

        def compile(self):
            return self

    graph_module.StateGraph = StateGraph

    langgraph_module = types.ModuleType("langgraph")
    langgraph_module.graph = graph_module

    fetch_module = types.ModuleType("src.services.fetch")

    class FakeSentryDigestFeedClient:
        def __init__(self, *_args, **_kwargs):
            pass

        async def fetch_articles(self):
            return []

        async def enrich_article_content(self, articles):
            return articles

    fetch_module.SentryDigestFeedClient = FakeSentryDigestFeedClient

    analyze_module = types.ModuleType("src.core.analyze")
    analyze_module.filter_exploitation_articles = lambda articles: articles

    async def analyze_exploitation(_articles, _config):
        return analysis_result or {}

    analyze_module.analyze_exploitation = analyze_exploitation

    with patch.dict(
        sys.modules,
        {
            "langgraph": langgraph_module,
            "langgraph.graph": graph_module,
            "src.services.fetch": fetch_module,
            "src.core.analyze": analyze_module,
        },
    ):
        return importlib.import_module("src.core.workflow")


@pytest.mark.parametrize(
    "analysis_error",
    [
        "OpenRouter response did not include choices (HTTP 200)",
        "OpenRouter provider error: HTTP 200; provider_code=503",
    ],
)
def test_real_graph_stops_after_failed_analysis(
    analysis_error, monkeypatch, tmp_path, caplog
):
    from langgraph.graph import END, START, StateGraph

    workflow = import_workflow_with_stubs(
        analysis_result={
            "error": analysis_error,
            "exploitation_report": "# Error Generating Exploitation Report",
        }
    )
    monkeypatch.setattr(workflow, "StateGraph", StateGraph)
    monkeypatch.setattr(workflow, "START", START)
    monkeypatch.setattr(workflow, "END", END)
    articles = [{"title": "New exploitation story", "link": "https://example.test/new"}]
    monkeypatch.setattr(
        workflow,
        "SentryDigestFeedClient",
        lambda *_args: types.SimpleNamespace(
            fetch_articles=AsyncMock(return_value=articles),
            enrich_article_content=AsyncMock(return_value=articles),
        ),
    )
    output = tmp_path / "index.md"
    output.write_text("Last valid report")
    fingerprint = tmp_path / ".sentryinsight-articles-fingerprint"
    fingerprint.write_text("last-valid-fingerprint\n")
    monkeypatch.setattr(
        workflow,
        "load_config",
        lambda: {"feed_url": "test", "output_path": str(output)},
    )
    generate = AsyncMock(wraps=workflow.generate_report)
    publish = AsyncMock(wraps=workflow.publish_results)
    monkeypatch.setattr(workflow, "generate_report", generate)
    monkeypatch.setattr(workflow, "publish_results", publish)

    with caplog.at_level("INFO", logger="src.core.workflow"):
        result = asyncio.run(workflow.run_exploitation_analysis())

    assert result["status"] == "failed"
    assert result["analysis_results"]["error"] == analysis_error
    generate.assert_not_awaited()
    publish.assert_not_awaited()
    assert output.read_text() == "Last valid report"
    assert fingerprint.read_text() == "last-valid-fingerprint\n"
    assert not (tmp_path / "reports").exists()
    assert "report_validation_errors" not in result
    assert "Workflow completed successfully" not in caplog.text
    assert "Completed article analysis" not in caplog.text
    assert "Workflow failed" in caplog.text


def test_failed_state_does_not_enter_report_validation(monkeypatch):
    workflow = import_workflow_with_stubs()
    state = {
        "status": "failed",
        "analysis_results": {"error": "original provider error"},
        "config": {},
    }
    resolve = unittest.mock.Mock(side_effect=AssertionError("must not validate"))
    monkeypatch.setattr(workflow, "resolve_reporting_keys", resolve)

    result = asyncio.run(workflow.generate_report(state))

    assert result["status"] == "failed"
    assert result["analysis_results"]["error"] == "original provider error"
    assert "report_validation_errors" not in result
    resolve.assert_not_called()


class WorkflowGuardTests(unittest.TestCase):
    def test_analysis_error_marks_state_failed(self):
        workflow = import_workflow_with_stubs(analysis_result={"error": "bad model"})
        state = {
            "filtered_articles": [{"title": "Example"}],
            "analysis_results": {},
            "config": {},
            "status": "started",
        }

        result = asyncio.run(workflow.analyze_articles(state))

        self.assertEqual(result["status"], "failed")
        self.assertEqual(result["analysis_results"]["error"], "bad model")

    def test_invalid_report_does_not_write_output_file(self):
        workflow = import_workflow_with_stubs()

        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "index.md"
            state = {
                "analysis_results": {
                    "exploitation_report": (
                        "# Error Generating Exploitation Report\n\nError code: 404"
                    )
                },
                "config": {"output_path": str(output_path)},
                "status": "started",
            }

            result = asyncio.run(workflow.generate_report(state))

            self.assertEqual(result["status"], "failed")
            self.assertIn("report_validation_errors", result)
            self.assertFalse(output_path.exists())

    def test_skipped_analysis_does_not_write_output_file(self):
        workflow = import_workflow_with_stubs()

        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "index.md"
            state = {
                "analysis_results": {
                    "skipped": True,
                    "skip_reason": "OpenCode server unavailable",
                    "exploitation_report": "",
                },
                "config": {"output_path": str(output_path)},
                "status": "started",
            }

            result = asyncio.run(workflow.generate_report(state))

            self.assertEqual(result["status"], "completed_with_warnings")
            self.assertFalse(output_path.exists())

    def test_source_attribution_is_removed_before_writing_output_file(self):
        workflow = import_workflow_with_stubs()

        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "index.md"
            state = {
                "analysis_results": {
                    "exploitation_report": """# Exploitation Report

## Executive Summary

Recent exploitation activity is concentrated in edge systems.

## Active Exploitation Details

### Example Vulnerability (CVE-2026-1234)
- **Description**: Attackers are exploiting a vulnerable service.
- **Impact**: Remote access.
- **Status**: Active exploitation observed.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: source-1e8f5cb3245d
- **Affected Versions**: Not stated in supplied sources.
- **Exceptions**: Not stated in supplied sources.
- **Recommended Actions**: CVE-2026-1234 is actively exploited in the wild. Install the update.
- **Vendor Links**: Not stated in supplied sources.

## Affected Systems and Products

- **Example Product**: Affected versions are exposed.

## Attack Vectors and Techniques

- **Internet-facing service**: Attackers send crafted requests.

## Threat Actor Activities

- **Unknown actor**: Opportunistic exploitation.

## Source Attribution

- **Example report**: Example Source - https://example.test/report
""",
                    "source_attribution_required": True,
                    "source_attribution_entries": [
                        "- **Example report**: Example Source - https://example.test/report"
                    ],
                    "reporting_sources": [
                        {
                            "key": "source-1e8f5cb3245d",
                            "publisher": "Example Source",
                            "title": "Example report",
                            "url": "https://example.test/report",
                            "content": "CVE-2026-1234 is actively exploited in the wild. Install the update.",
                        }
                    ],
                },
                "config": {"output_path": str(output_path)},
                "status": "started",
            }

            result = asyncio.run(workflow.generate_report(state))

            self.assertNotEqual(result["status"], "failed")
            self.assertNotIn("report_validation_errors", result)
            self.assertTrue(output_path.exists())
            self.assertNotIn("## Source Attribution", output_path.read_text())
            self.assertIn("report_date:", output_path.read_text())
            self.assertIn("generated_at:", output_path.read_text())
            self.assertIn("schema_version: 3", output_path.read_text())
            self.assertIn("digest_issue_url:", output_path.read_text())
            self.assertIn("**Reporting**:", output_path.read_text())
            self.assertTrue((Path(tmpdir) / "index.html").exists())
            self.assertTrue((Path(tmpdir) / "reports" / "index.json").exists())

    def test_overlong_summary_is_split_before_report_validation(self):
        workflow = import_workflow_with_stubs()
        summary_sentences = [
            "Attackers are exploiting multiple exposed systems across sectors.",
            "Credential theft and remote code execution remain the dominant risks.",
            "Supply chain compromise is expanding across developer ecosystems.",
            "Security teams should prioritize patching and credential rotation.",
            "Defenders should monitor for follow-on access attempts.",
        ]

        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "index.md"
            state = {
                "analysis_results": {
                    "exploitation_report": f"""# Exploitation Report

## Executive Summary

{" ".join(summary_sentences)}

## Active Exploitation Details

### Example Vulnerability (CVE-2026-1234)
- **Description**: Attackers are exploiting a vulnerable service.
- **Impact**: Remote access.
- **Status**: Active exploitation observed.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: source-1e8f5cb3245d
- **Affected Versions**: Not stated in supplied sources.
- **Exceptions**: Not stated in supplied sources.
- **Recommended Actions**: CVE-2026-1234 is actively exploited in the wild. Install the update.
- **Vendor Links**: Not stated in supplied sources.

## Affected Systems and Products

- **Example Product**: Affected versions are exposed.

## Attack Vectors and Techniques

- **Internet-facing service**: Attackers send crafted requests.

## Threat Actor Activities

- **Unknown actor**: Opportunistic exploitation.
""",
                    "reporting_sources": [
                        {
                            "key": "source-1e8f5cb3245d",
                            "publisher": "Example Source",
                            "title": "Example report",
                            "url": "https://example.test/report",
                            "content": "CVE-2026-1234 is actively exploited in the wild. Install the update.",
                        }
                    ],
                },
                "config": {"output_path": str(output_path)},
                "status": "started",
            }

            result = asyncio.run(workflow.generate_report(state))

            self.assertNotEqual(result["status"], "failed")
            written_report = output_path.read_text()
            summary_body = written_report.split("## Executive Summary", 1)[1].split(
                "## Active Exploitation Details", 1
            )[0]
            self.assertEqual(
                len([part for part in summary_body.split("\n\n") if part.strip()]), 2
            )
            for sentence in summary_sentences:
                self.assertIn(sentence, summary_body)

    def test_missing_expected_cve_does_not_write_output_file(self):
        workflow = import_workflow_with_stubs()

        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "index.md"
            state = {
                "analysis_results": {
                    "exploitation_report": """# Exploitation Report

## Executive Summary

Recent exploitation activity is concentrated in edge systems.

## Active Exploitation Details

### Example Vulnerability (CVE-2026-1234)
- **Description**: Attackers are exploiting a vulnerable service.
- **Impact**: Remote access.
- **Status**: Active exploitation observed.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: source-1e8f5cb3245d
- **Affected Versions**: Not stated in supplied sources.
- **Exceptions**: Not stated in supplied sources.
- **Recommended Actions**: Install the update.
- **Vendor Links**: Not stated in supplied sources.

## Affected Systems and Products

- **Example Product**: Affected versions are exposed.

## Attack Vectors and Techniques

- **Internet-facing service**: Attackers send crafted requests.

## Threat Actor Activities

- **Unknown actor**: Opportunistic exploitation.
""",
                    "cves_identified": ["CVE-2026-1111"],
                },
                "config": {"output_path": str(output_path)},
                "status": "started",
            }

            result = asyncio.run(workflow.generate_report(state))

            self.assertEqual(result["status"], "failed")
            self.assertIn("report_validation_errors", result)
            self.assertFalse(output_path.exists())

    def test_static_build_failure_preserves_current_report_and_archive(self):
        workflow = import_workflow_with_stubs()

        current_report = """---
schema_version: 1
report_date: 2026-08-12
generated_at: 2026-08-12T13:21:22Z
---
# Exploitation Report

## Executive Summary

The existing report remains current.

## Active Exploitation Details

### Existing Vulnerability
- **Description**: Existing report content.
- **Impact**: Existing impact.
- **Status**: Existing status.
- **Severity**: high
- **Exploitation Status**: observed
- **Action**: monitor

## Affected Systems and Products

- **Example Product**: Existing scope.

## Attack Vectors and Techniques

- **Internet-facing service**: Existing vector.

## Threat Actor Activities

- **Unknown actor**: Existing activity.
"""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "index.md"
            output_path.write_text(current_report)
            state = {
                "analysis_results": {
                    "date": "2026-08-13",
                    "generated_at": "2026-08-13T13:21:22Z",
                    "exploitation_report": """# Exploitation Report

## Executive Summary

The next report should not be partially published.

## Active Exploitation Details

### Next Vulnerability
- **Description**: Next report content.
- **Impact**: Next impact.
- **Status**: Next status.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch

## Affected Systems and Products

- **Example Product**: Next scope.

## Attack Vectors and Techniques

- **Internet-facing service**: Next vector.

## Threat Actor Activities

- **Unknown actor**: Next activity.
""",
                },
                "config": {"output_path": str(output_path)},
                "status": "started",
            }

            with patch.object(
                workflow,
                "build_site",
                side_effect=workflow.SiteBuildError("late build failure"),
            ):
                result = asyncio.run(workflow.generate_report(state))

            self.assertEqual(result["status"], "failed")
            self.assertEqual(output_path.read_text(), current_report)
            self.assertFalse((Path(tmpdir) / "reports").exists())

    def test_failed_state_skips_publish(self):
        workflow = import_workflow_with_stubs()
        state = {
            "analysis_results": {"exploitation_report": "# Exploitation Report"},
            "config": {"github_pages": {"enabled": True}},
            "status": "failed",
        }

        result = asyncio.run(workflow.publish_results(state))

        self.assertIs(result, state)

    def test_filter_articles_skips_analysis_when_article_set_unchanged(self):
        from src.core.content_fingerprint import (
            compute_articles_fingerprint,
            write_stored_fingerprint,
        )

        workflow = import_workflow_with_stubs()

        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "index.md"
            articles = [{"title": "Same story", "link": "https://example.com/a"}]
            write_stored_fingerprint(
                compute_articles_fingerprint(articles),
                str(Path(tmpdir) / ".sentryinsight-articles-fingerprint"),
            )

            state = {
                "articles": articles,
                "config": {"output_path": str(output_path)},
                "status": "started",
            }

            result = asyncio.run(workflow.filter_articles(state))

            self.assertEqual(result["status"], "completed_unchanged")
            self.assertEqual(workflow.should_end(result), "unchanged")

    def test_filter_articles_continues_when_article_set_is_new(self):
        workflow = import_workflow_with_stubs()

        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "index.md"
            articles = [{"title": "New story", "link": "https://example.com/new"}]

            state = {
                "articles": articles,
                "config": {"output_path": str(output_path)},
                "status": "started",
            }

            result = asyncio.run(workflow.filter_articles(state))

            self.assertNotEqual(result.get("status"), "completed_unchanged")
            self.assertEqual(workflow.should_end(result), "continue")
            self.assertIn("articles_fingerprint", result)

    def test_generate_report_persists_fingerprint_for_next_run(self):
        from src.core.content_fingerprint import read_stored_fingerprint

        workflow = import_workflow_with_stubs()

        # Run from an isolated cwd so the default canonical path is disposable.
        original_cwd = Path.cwd()
        with tempfile.TemporaryDirectory() as tmpdir:
            os.chdir(tmpdir)
            try:
                state = {
                    "analysis_results": {
                        "exploitation_report": """# Exploitation Report

## Executive Summary

Recent exploitation activity is concentrated in edge systems.

## Active Exploitation Details

### Example Vulnerability (CVE-2026-1234)
- **Description**: Attackers are exploiting a vulnerable service.
- **Impact**: Remote access.
- **Status**: Active exploitation observed.
- **Severity**: high
- **Exploitation Status**: active
- **Action**: patch
- **Reporting**: source-1e8f5cb3245d
- **Affected Versions**: Not stated in supplied sources.
- **Exceptions**: Not stated in supplied sources.
- **Recommended Actions**: CVE-2026-1234 is actively exploited in the wild. Install the update.
- **Vendor Links**: Not stated in supplied sources.

## Affected Systems and Products

- **Example Product**: Affected versions are exposed.

## Attack Vectors and Techniques

- **Internet-facing service**: Attackers send crafted requests.

## Threat Actor Activities

- **Unknown actor**: Opportunistic exploitation.
""",
                        "reporting_sources": [
                            {
                                "key": "source-1e8f5cb3245d",
                                "publisher": "Example Source",
                                "title": "Example report",
                                "url": "https://example.test/report",
                                "content": "CVE-2026-1234 is actively exploited in the wild. Install the update.",
                            }
                        ],
                    },
                    "articles_fingerprint": "test-fingerprint-value",
                    "config": {"output_path": "index.md"},
                    "status": "started",
                }

                result = asyncio.run(workflow.generate_report(state))

                self.assertEqual(result["status"], "started")
                fingerprint_path = Path(".sentryinsight-articles-fingerprint")
                self.assertTrue(fingerprint_path.exists())
                self.assertEqual(
                    read_stored_fingerprint(str(fingerprint_path)),
                    "test-fingerprint-value",
                )
            finally:
                os.chdir(original_cwd)

    def test_skipped_analysis_skips_publish(self):
        workflow = import_workflow_with_stubs()
        state = {
            "analysis_results": {
                "skipped": True,
                "skip_reason": "OpenCode server unavailable",
                "exploitation_report": "",
            },
            "config": {"github_pages": {"enabled": True}},
            "status": "completed_with_warnings",
        }

        result = asyncio.run(workflow.publish_results(state))

        self.assertIs(result, state)
        self.assertEqual(result["status"], "completed_with_warnings")


if __name__ == "__main__":
    unittest.main()

import asyncio
import importlib
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import patch


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

    publish_module = types.ModuleType("src.services.publish")

    async def publish_to_github_pages(_analysis_results, _github_pages_config):
        raise AssertionError("publish should not run for failed state")

    publish_module.publish_to_github_pages = publish_to_github_pages

    audio_module = types.ModuleType("src.services.audio")

    async def generate_executive_summary_audio(_report, _output_path):
        raise AssertionError("audio generation should not run for failed state")

    audio_module.generate_executive_summary_audio = generate_executive_summary_audio

    with patch.dict(
        sys.modules,
        {
            "langgraph": langgraph_module,
            "langgraph.graph": graph_module,
            "src.services.fetch": fetch_module,
            "src.core.analyze": analyze_module,
            "src.services.publish": publish_module,
            "src.services.audio": audio_module,
        },
    ):
        return importlib.import_module("src.core.workflow")


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

    def test_missing_required_source_attribution_does_not_write_output_file(self):
        workflow = import_workflow_with_stubs()

        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "index.md"
            state = {
                "analysis_results": {
                    "exploitation_report": """# Exploitation Report

Recent exploitation activity is concentrated in edge systems.

## Active Exploitation Details

### Example Vulnerability
- **Description**: Attackers are exploiting a vulnerable service.
- **Impact**: Remote access.
- **Status**: Active exploitation observed.

## Affected Systems and Products

- **Example Product**: Affected versions are exposed.

## Attack Vectors and Techniques

- **Internet-facing service**: Attackers send crafted requests.

## Threat Actor Activities

- **Unknown actor**: Opportunistic exploitation.
""",
                    "source_attribution_required": True,
                },
                "config": {"output_path": str(output_path)},
                "status": "started",
            }

            result = asyncio.run(workflow.generate_report(state))

            self.assertEqual(result["status"], "failed")
            self.assertIn("report_validation_errors", result)
            self.assertFalse(output_path.exists())

    def test_failed_state_skips_audio_generation(self):
        workflow = import_workflow_with_stubs()
        state = {
            "analysis_results": {"exploitation_report": "# Exploitation Report"},
            "status": "failed",
        }

        result = asyncio.run(workflow.generate_audio(state))

        self.assertIs(result, state)

    def test_failed_state_skips_publish(self):
        workflow = import_workflow_with_stubs()
        state = {
            "analysis_results": {"exploitation_report": "# Exploitation Report"},
            "config": {"github_pages": {"enabled": True}},
            "status": "failed",
        }

        result = asyncio.run(workflow.publish_results(state))

        self.assertIs(result, state)

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

"""Exercise real analysis, graph, publication gates and static artifacts offline."""

import asyncio
import json
from types import SimpleNamespace
from unittest.mock import AsyncMock

import pytest

from test_analyze_guards import import_analyze_with_stubs, reference_plan_from_prompt
from test_workflow_guards import import_workflow_with_stubs

REPRESENTATIVE_ARTICLES = [
    {
        "title": "Example Gateway security advisory",
        "source": "Example publisher",
        "link": "https://example.test/gateway",
        "content_kind": "article",
        "content": (
            "## CVE-2026-1234\n\nCVE-2026-1234 is a critical vulnerability in Example Gateway, with a CVSS score of 9.8.\n\n"
            "CVE-2026-1234 exploitation has not been observed.\n\n"
            "Example Gateway on Windows permits server-side request forgery that could expose internal data.\n\n"
            "Researchers link a potential campaign targeting CVE-2026-1234 to Example Group.\n\n"
            "Affected versions: Example Gateway 2.3 (Windows only).\n\n"
            "Hosted users need no action.\n\n"
            "Customers should install the patch. Restart the service only after backing up the configuration.\n\nSee the vendor security advisory for details."
        ),
        "source_links": ["https://vendor.example/security/advisories/gateway"],
        "source_link_contexts": [
            dict(
                url="https://vendor.example/security/advisories/gateway",
                label="vendor security advisory",
                context="See the vendor security advisory for details.",
            )
        ],
    },
    {
        "title": "Example Storage exploitation advisory",
        "source": "Another publisher",
        "link": "https://example.test/storage",
        "content_kind": "article",
        "content": (
            "## CVE-2026-5678\n\nCVE-2026-5678 is actively exploited. Its CVSS score is 7.5.\n\n"
            "The Example Storage server has a buffer overflow that could allow remote code execution.\n\n"
            "Researchers attribute attacks exploiting CVE-2026-5678 to Example Operator.\n\n"
            "Affected versions: Example Storage 4.5 and earlier.\n\n"
            "Users should apply the update.\n\nSee the vendor security advisory for details."
        ),
        "source_links": ["https://vendor.example/security/advisories/storage"],
        "source_link_contexts": [
            dict(
                url="https://vendor.example/security/advisories/storage",
                label="vendor security advisory",
                context="See the vendor security advisory for details.",
            )
        ],
    },
]


def run_real_pipeline(
    monkeypatch,
    output_path,
    *,
    mutation=None,
    articles=None,
    select_plan=None,
    expect_model_call=True,
):
    from langgraph.graph import END, START, StateGraph

    analyze = import_analyze_with_stubs()

    def response(**kwargs):
        raw = (select_plan or reference_plan_from_prompt)(**kwargs)
        if mutation is None:
            return raw
        plan = json.loads(raw)
        if mutation == "badge":
            plan["findings"][0]["status"] = "active"
        elif mutation == "prose":
            plan["summary"] = "Attackers are exploiting every vulnerability."
        elif mutation == "omit":
            plan["findings"].pop()
        else:
            plan["findings"][0]["excerpts"] = plan["findings"][1]["excerpts"]
        return json.dumps(plan)

    client = SimpleNamespace(generate=AsyncMock(side_effect=response))
    monkeypatch.setattr(analyze, "build_model_client", lambda **_: client)
    workflow = import_workflow_with_stubs()
    monkeypatch.setattr(workflow, "StateGraph", StateGraph)
    monkeypatch.setattr(workflow, "START", START)
    monkeypatch.setattr(workflow, "END", END)
    monkeypatch.setattr(workflow, "analyze_exploitation", analyze.analyze_exploitation)
    monkeypatch.setattr(
        workflow,
        "SentryDigestFeedClient",
        lambda *_: SimpleNamespace(
            fetch_articles=AsyncMock(
                return_value=(
                    articles if articles is not None else REPRESENTATIVE_ARTICLES
                )
            ),
            enrich_article_content=AsyncMock(
                return_value=(
                    articles if articles is not None else REPRESENTATIVE_ARTICLES
                )
            ),
        ),
    )
    monkeypatch.setattr(
        workflow,
        "load_config",
        lambda: {
            "feed_url": "https://example.test/feed",
            "output_path": str(output_path),
        },
    )
    result = asyncio.run(workflow.run_exploitation_analysis())
    assert client.generate.await_count == int(expect_model_call)
    return result


def test_real_pipeline_publishes_useful_complete_artifacts(monkeypatch, tmp_path):
    output = tmp_path / "index.md"
    result = run_real_pipeline(monkeypatch, output)
    assert result["status"] == "completed", result
    text = output.read_text()
    assert "**Severity**: critical" in text
    assert "**Severity**: high" in text
    assert "**Exploitation Status**: not_observed" in text
    assert "**Exploitation Status**: active" in text
    assert "Hosted users need no action." in text
    assert "only after backing up the configuration" in text
    assert "https://vendor.example/security/advisories/gateway" in text
    assert "Example Group" in text.split("## Threat Actor Activities", 1)[1]
    assert (
        "remote code execution" in text.split("## Attack Vectors and Techniques", 1)[1]
    )
    assert (tmp_path / "index.html").is_file()
    artifact = json.loads((tmp_path / "current-findings.json").read_text())
    assert artifact["finding_count"] == 2
    assert set(artifact["cve_ids"]) == {"CVE-2026-1234", "CVE-2026-5678"}
    assert (tmp_path / ".sentryinsight-articles-fingerprint").read_text().strip()


@pytest.mark.parametrize("mutation", ["badge", "prose", "omit", "cross_scope"])
def test_invalid_plan_preserves_previous_report_and_fingerprint(
    monkeypatch, tmp_path, mutation
):
    output = tmp_path / "index.md"
    output.write_text("Previous validated report")
    fingerprint = tmp_path / ".sentryinsight-articles-fingerprint"
    fingerprint.write_text("previous-inputs\n")
    result = run_real_pipeline(monkeypatch, output, mutation=mutation)
    assert result["status"] == "failed"
    assert result["analysis_results"]["error"] == "invalid_generation_plan"
    assert output.read_text() == "Previous validated report"
    assert fingerprint.read_text() == "previous-inputs\n"
    assert not (tmp_path / "index.html").exists()
    assert not (tmp_path / "current-findings.json").exists()


@pytest.mark.parametrize(
    "metadata",
    [
        {"cves": ["CVE-2026-1234"]},
        {"title": "Active exploitation of CVE-2026-1234"},
        {"link": "https://example.test/CVE-2026-1234"},
    ],
)
def test_real_pipeline_retains_metadata_only_cves_without_claiming_confirmation(
    monkeypatch, tmp_path, metadata
):
    article = dict(
        title="Gateway exploitation",
        source="Publisher",
        link="https://example.test/story",
        content="Attackers are exploiting the gateway.",
        content_kind="article",
    )
    article.update(metadata)
    result = run_real_pipeline(monkeypatch, tmp_path / "index.md", articles=[article])
    assert result["status"] == "completed", result
    artifact = json.loads((tmp_path / "current-findings.json").read_text())
    assert artifact["cve_ids"] == ["CVE-2026-1234"]
    report = (tmp_path / "index.md").read_text()
    assert "**Exploitation Status**: unknown" in report
    assert "metadata" in report

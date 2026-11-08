"""A full offline replay derives detail context and scopes a bounded number of times.

Source review runs at filter, analysis and generation time, and publication
validation checks every finding's version scope. Within one run scope these
must reuse derivations of identical content instead of recomputing them once
per stage or once per finding.
"""

import asyncio
import importlib
from unittest.mock import AsyncMock

import pytest

from evals.grounding.dataset import ABSENT
from src.core import finding_evidence, version_references
from src.core.derivations import derivation_scope
from src.core.reporting import build_reporting_catalog, reporting_key
from src.core.version_references import build_version_reference_context

MAX_DERIVATIONS = 4


def _article(index: int) -> dict:
    cve = f"CVE-2026-{41100 + index}"
    return {
        "title": f"Synthetic advisory {index}",
        "source": "Fictional Security Bulletin",
        "link": f"https://example.test/advisories/replay-{index:02d}",
        "content": (
            f"{cve} is actively exploited.\n\n"
            f"Affected versions: Example Gateway 1.{index}.\n\n"
            "Customers should install the patch."
        ),
        "content_kind": "article",
        "source_links": [f"https://vendor.example.test/advisories/{41100 + index}"],
    }


def _report(articles: list[dict]) -> str:
    """A complete reference-protocol report citing every article once."""
    scopes = {
        tuple(scope["cves"]): scope
        for scope in build_version_reference_context(build_reporting_catalog(articles))
    }
    blocks = [
        "# Exploitation Report\n\n## Executive Summary\n\n"
        "The supplied advisories describe the findings below.\n\n"
        "Review the source-specific status and details before acting.\n\n"
        "## Active Exploitation Details\n"
    ]
    for index, article in enumerate(articles):
        cve = f"CVE-2026-{41100 + index}"
        references = "; ".join(item["id"] for item in scopes[(cve,)]["constraints"])
        blocks.append(
            f"### Example vulnerability ({cve})\n"
            "- **Description**: A vulnerability described by the supplied source.\n"
            "- **Severity**: unknown\n"
            "- **Exploitation Status**: active\n"
            "- **Action**: patch\n"
            f"- **CVE IDs**: {cve}\n"
            f"- **Reporting**: {reporting_key(article['link'])}\n"
            f"- **Affected Versions**: {references}\n"
            f"- **Exceptions**: {ABSENT}\n"
            "- **Recommended Actions**: Customers should install the patch.\n"
            f"- **Vendor Links**: {article['source_links'][0]}\n"
        )
    blocks.extend(
        f"## {title}\n\n{ABSENT}\n"
        for title in (
            "Affected Systems and Products",
            "Attack Vectors and Techniques",
            "Threat Actor Activities",
        )
    )
    return "\n".join(blocks)


def _replay(tmp_path, monkeypatch, findings: int) -> dict[str, int]:
    import src.core.analyze as analyze
    import src.core.workflow as workflow

    analyze, workflow = importlib.reload(analyze), importlib.reload(workflow)
    articles = [_article(index) for index in range(findings)]
    report = _report(articles)
    monkeypatch.setattr(workflow, "filter_exploitation_articles", lambda items: items)
    client = AsyncMock()
    client.generate.return_value = report
    real_analyze = workflow.analyze_exploitation

    async def analyze_with_client(items, config):
        return await real_analyze(items, config, model_client=client)

    monkeypatch.setattr(workflow, "analyze_exploitation", analyze_with_client)

    counts = {"detail_context": 0, "scopes": 0}
    for module, name, counter in (
        (finding_evidence, "_derive_finding_detail_context", "detail_context"),
        (version_references, "_derive_scopes", "scopes"),
    ):
        original = getattr(module, name)

        def counted(*args, _original=original, _counter=counter, **kwargs):
            counts[_counter] += 1
            return _original(*args, **kwargs)

        monkeypatch.setattr(module, name, counted)

    state = {
        "articles": articles,
        "filtered_articles": articles,
        "analysis_results": {},
        "status": "started",
        "config": {"output_path": str(tmp_path / "index.md")},
    }

    async def run(state):
        # The same single run scope that ``run_exploitation_analysis`` opens.
        with derivation_scope():
            state = await workflow.filter_articles(state)
            state = await workflow.analyze_articles(state)
            return await workflow.generate_report(state)

    result = asyncio.run(run(state))
    assert result.get("report_generated") is True, result.get("failure")
    client.generate.assert_awaited_once()
    return counts


@pytest.mark.parametrize("findings", [2, 8])
def test_full_replay_derives_detail_context_and_scopes_a_bounded_number_of_times(
    tmp_path, monkeypatch, findings
):
    counts = _replay(tmp_path, monkeypatch, findings)
    assert counts["detail_context"] <= MAX_DERIVATIONS, counts
    assert counts["scopes"] <= MAX_DERIVATIONS, counts


def test_derivations_are_not_shared_outside_a_scope():
    articles = [_article(0)]
    catalog = build_reporting_catalog(articles)
    first = finding_evidence.build_finding_detail_context(catalog)
    first[0]["spans"].clear()
    assert finding_evidence.build_finding_detail_context(catalog)[0]["spans"]


def test_scoped_results_never_alias_the_cached_value():
    catalog = build_reporting_catalog([_article(0)])
    with derivation_scope():
        first = finding_evidence.build_finding_detail_context(catalog)
        expected = repr(first)
        first[0]["spans"][0]["text"] = "mutated"
        first[0]["cves"].append("CVE-2026-0000")
        first[0]["exploitation"]["status"] = "mutated"
        first.clear()
        assert repr(finding_evidence.build_finding_detail_context(catalog)) == expected
        scopes = version_references._scopes(catalog)
        scopes.clear()
        assert version_references._scopes(catalog)


def test_changed_content_is_a_different_derivation():
    original, changed = _article(0), _article(0)
    changed["content"] = changed["content"].replace("1.0", "1.9")
    with derivation_scope():
        before = version_references._scopes(build_reporting_catalog([original]))
        after = version_references._scopes(build_reporting_catalog([changed]))
    assert before[0].constraints != after[0].constraints

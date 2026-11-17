"""Required finding identities cannot be replaced by narrative CVE mentions."""

import asyncio

import pytest

from src.core.report_artifact import parse_report_artifact
from src.core.reporting import reporting_key
from src.core.reviewed_report import resolve_reviewed_analysis
from src.core.source_review import (
    PLAN_KEY,
    digest,
    prepare_source_review,
    review_articles,
)
from test_reviewed_report import prepared_result
from test_report_artifact import REPORT
from test_unresolved_versions import raw_report
from test_version_references import ABSENT, source
from test_workflow_guards import import_workflow_with_stubs

CVE = "CVE-2026-1234"


@pytest.mark.parametrize("advisory", [False, True])
@pytest.mark.parametrize("narrative_mention", [False, True])
def test_missing_required_cve_preserves_report_and_fingerprint(
    advisory, narrative_mention, tmp_path
):
    articles = [
        source("A service advisory.", "primary"),
        source(f"Attackers are actively exploiting {CVE}.", "required"),
    ]
    plan = prepare_source_review(articles, advisory=advisory)
    result = prepared_result(articles)
    result[PLAN_KEY] = plan.packet
    result["exploitation_report"] = raw_report(
        [reporting_key(articles[0]["link"])], ABSENT
    )
    if narrative_mention:
        result[
            "exploitation_report"
        ] += f"\n\n{CVE} is discussed elsewhere in this report.\n"
    output = tmp_path / "index.md"
    html = tmp_path / "index.html"
    fingerprint = tmp_path / ".sentryinsight-articles-fingerprint"
    originals = {
        output: REPORT,
        html: "<h1>LAST VALID REPORT</h1>",
        fingerprint: "LAST VALID FINGERPRINT",
    }
    for path, text in originals.items():
        path.write_text(text)
    state = {
        "analysis_results": result,
        "filtered_articles": review_articles(plan, eligible_only=False),
        PLAN_KEY: plan.packet,
        "articles_fingerprint": digest(
            {"generation_schema": 5, "plan_id": plan.packet["plan_id"]}
        ),
        "config": {
            "output_path": str(output),
            "analysis": {"grounding": "advisory" if advisory else "strict"},
        },
        "status": "started",
    }
    workflow = import_workflow_with_stubs()
    failed = asyncio.run(workflow.generate_report(state))
    assert failed["status"] == "failed"
    assert failed["failure"]["codes"] == ["missing_expected_cves"]
    assert failed["report_generated"] is False
    for path, text in originals.items():
        assert path.read_text() == text
    assert not (tmp_path / "reports").exists()


@pytest.mark.parametrize("advisory", [False, True])
@pytest.mark.parametrize(
    "content",
    [
        "A campaign used stolen credentials. No vulnerability is identified.",
        f"There is no evidence of exploitation of {CVE}.",
        f"A credential attack.\n\nFor background, {CVE} was exploited earlier.",
    ],
)
def test_sources_without_required_cves_allow_non_cve_findings(advisory, content):
    articles = [source("A credential attack.", "primary"), source(content, "context")]
    result = prepared_result(articles)
    result[PLAN_KEY] = prepare_source_review(articles, advisory=advisory).packet
    result["exploitation_report"] = raw_report(
        [reporting_key(articles[0]["link"])], ABSENT
    )
    candidate = resolve_reviewed_analysis(result, advisory=advisory)
    [finding] = parse_report_artifact(candidate.source).findings
    assert finding.cve_ids == ()
    assert candidate.coverage["counts"]["cited_sources"] == 1

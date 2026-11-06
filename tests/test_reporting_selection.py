"""Synthetic identity failures, without model requests or historical output."""

import asyncio
import json

import pytest

from src.core.reporting import reporting_key
from src.core.reviewed_report import resolve_reviewed_analysis
from src.core.source_review import PLAN_KEY, SourceReviewError
from src.core.validation_diagnostics import sanitize_diagnostic, validation_diagnostic
from test_reviewed_report import prepared_result
from test_unresolved_versions import raw_report
from test_version_references import ABSENT, source


@pytest.mark.parametrize("advisory", [False, True])
def test_exact_code_wrapped_keys_preserve_the_same_validated_report(advisory):
    result = prepared_result([source("An independent advisory.", "good")])
    expected = resolve_reviewed_analysis(result, advisory=advisory)
    key = result["reporting_sources"][0]["key"]
    result["exploitation_report"] = result["exploitation_report"].replace(
        "**Reporting**: " + key, "**Reporting**: `" + key + "`"
    )
    actual = resolve_reviewed_analysis(result, advisory=advisory)
    assert actual.source == expected.source
    assert actual.advisories == expected.advisories


@pytest.mark.parametrize("advisory", [False, True])
@pytest.mark.parametrize(
    "value,code",
    [
        ("source-000000000000", "unknown_reporting_source"),
        ("`source-000000000000`", "unknown_reporting_source"),
        ("held", "quarantined_reporting_source"),
        ("`held`", "quarantined_reporting_source"),
        ("https://private.example/secret", "invalid_reporting_source_syntax"),
        ("{key},", "invalid_reporting_source_syntax"),
        ("{key}; {key}", "invalid_reporting_source_syntax"),
        ("[trusted]({key})", "invalid_reporting_source_syntax"),
        ("{key} extra", "invalid_reporting_source_syntax"),
        ("`{key}", "invalid_reporting_source_syntax"),
        ("{key}, `{key}`", "duplicate_reporting_source"),
        ("", "invalid_reporting_source_syntax"),
    ],
)
def test_rejections_have_safe_actionable_categories(value, code, advisory):
    result = prepared_result(
        [source("An advisory.", "good"), source("Affected versions:", "held")]
    )
    key = reporting_key("https://example.test/good")
    held = reporting_key("https://example.test/held")
    value = value.format(key=key).replace("held", held)
    result["exploitation_report"] = raw_report([value], ABSENT)
    with pytest.raises(SourceReviewError) as caught:
        resolve_reviewed_analysis(result, advisory=advisory)
    diagnostic = validation_diagnostic("reporting_identity", caught.value)
    assert diagnostic["codes"] == [code]
    assert diagnostic["finding_index"] == 1
    assert diagnostic["field"] == "Reporting"
    assert sanitize_diagnostic(diagnostic) == diagnostic
    serialized = json.dumps(diagnostic)
    assert key not in serialized and held not in serialized
    assert "private.example" not in serialized


@pytest.mark.parametrize("duplicate", [False, True])
def test_each_finding_requires_exactly_one_reporting_field(duplicate):
    result = prepared_result()
    key = next(
        r["key"] for r in result[PLAN_KEY]["sources"] if r["state"] == "eligible"
    )
    line = "- **Reporting**: " + key
    result["exploitation_report"] = result["exploitation_report"].replace(
        line, line + "\n" + line if duplicate else ""
    )
    with pytest.raises(SourceReviewError) as caught:
        resolve_reviewed_analysis(result)
    diagnostic = validation_diagnostic("reporting_identity", caught.value)
    assert diagnostic["codes"] == ["invalid_reporting_field_count"]
    assert diagnostic["finding_index"] == 1


def test_later_finding_failure_is_not_hidden_by_valid_earlier_citation():
    result = prepared_result([source("An advisory.", "good")])
    report = result["exploitation_report"]
    finding = report.split("## Active Exploitation Details\n")[1].split("\n## ")[0]
    key = result["reporting_sources"][0]["key"]
    rejected = finding.replace(key, "source-000000000000")
    result["exploitation_report"] = report.replace(finding, finding + rejected)
    with pytest.raises(SourceReviewError) as caught:
        resolve_reviewed_analysis(result)
    diagnostic = validation_diagnostic("reporting_identity", caught.value)
    assert diagnostic["codes"] == ["unknown_reporting_source"]
    assert diagnostic["finding_index"] == 2


def test_multiple_wrapped_keys_preserve_order_and_coverage():
    result = prepared_result(
        [source("An advisory.", "one"), source("An advisory.", "two")]
    )
    expected = resolve_reviewed_analysis(result)
    for item in result["reporting_sources"]:
        key = item["key"]
        result["exploitation_report"] = result["exploitation_report"].replace(
            key, "`" + key + "`"
        )
    actual = resolve_reviewed_analysis(result)
    assert actual.source == expected.source
    assert actual.coverage["counts"]["cited_sources"] == 2


def test_prompt_ends_with_exact_admitted_source_contract(tmp_path):
    from test_review_pipeline import load_modules

    analyze, _ = load_modules()

    class Client:
        calls = 0

        async def generate(self, **kwargs):
            self.calls += 1
            self.prompt = kwargs["user_prompt"]
            return "candidate"

    client = Client()
    articles = [source("An advisory.", "good"), source("Affected versions:", "held")]
    result = asyncio.run(
        analyze.analyze_exploitation(
            articles,
            {"output_path": str(tmp_path / "index.md"), "analysis": {}},
            model_client=client,
        )
    )
    assert "error" not in result
    assert client.calls == 1
    contract = client.prompt.split("BEGIN REPORTING SOURCE CONTRACT\n")[1].split(
        "\nEND REPORTING SOURCE CONTRACT"
    )[0]
    assert json.loads(contract) == [reporting_key(articles[0]["link"])]
    assert reporting_key(articles[1]["link"]) not in client.prompt
    assert "Affected versions:" not in client.prompt
    assert "plain keys" in client.prompt


def test_identity_failure_preserves_last_good_tree_and_reports_actual_stage(
    tmp_path, monkeypatch
):
    from test_review_pipeline import load_modules, state_for

    _, workflow = load_modules()
    articles = [source("An advisory.", "good")]
    monkeypatch.setattr(workflow, "filter_exploitation_articles", lambda items: items)
    files = {
        "index.md": "last good report",
        "index.html": "last good site",
        ".sentryinsight-articles-fingerprint": "last good fingerprint",
        "reports/2026-11-01.md": "historical report",
    }
    for name, text in files.items():
        path = tmp_path / name
        path.parent.mkdir(exist_ok=True)
        path.write_text(text)
    state = asyncio.run(workflow.filter_articles(state_for(tmp_path, articles)))
    state["analysis_results"] = prepared_result(articles)
    state["analysis_results"]["exploitation_report"] = raw_report(
        ["source-000000000000"], ABSENT
    )
    result = asyncio.run(workflow.generate_report(state))
    assert result["status"] == "failed"
    assert result["report_generated"] is False
    assert result["failure"]["stage"] == "reporting_identity"
    assert result["failure_diagnostic"]["codes"] == ["unknown_reporting_source"]
    assert result["failure_diagnostic"]["finding_index"] == 1
    assert {name: (tmp_path / name).read_text() for name in files} == files

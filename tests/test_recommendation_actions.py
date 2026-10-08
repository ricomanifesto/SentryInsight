"""Complete source directives own action badges, including their qualifications."""

import json

import pytest

from src.core.finding_evidence import recommendation_action
from src.core.report_artifact import Action, parse_report_artifact
from test_finding_generation import CVE, catalog_for, render
from test_finding_generation_pipeline import run_real_pipeline

DIRECTIVES = [
    ("install the patch", "patch"),
    ("apply the updates", "patch"),
    ("upgrade the appliance", "patch"),
    ("apply the workaround", "mitigate"),
    ("mitigate the vulnerability", "mitigate"),
    ("review the logs for indicators of compromise", "investigate"),
    ("investigate suspicious activity", "investigate"),
    ("monitor logs", "monitor"),
    ("monitor vendor advisories", "monitor"),
    ("consult the advisory", "none"),
    ("contact support", "none"),
]


@pytest.mark.parametrize(("directive", "action"), DIRECTIVES)
@pytest.mark.parametrize(
    "form", ["Users are advised to {}.", "Users should {}.", "{}."]
)
def test_all_supported_actions_survive_collection_rendering_and_validation(
    directive, action, form
):
    advice = form.format(directive).capitalize()
    _, report = render(catalog_for(f"## {CVE}\n\n{advice}"))
    assert f"**Action**: {action}" in report
    assert f"**Recommended Actions**: {advice}" in report
    if action != "none":
        assert "**Action Context**" not in report


@pytest.mark.parametrize(("directive", "action"), DIRECTIVES)
@pytest.mark.parametrize(
    "form",
    [
        "Users should not {}.",
        "Users are not advised to {}.",
        "Do not {}.",
        "Users should {} only if the appliance is exposed.",
        "Users should {}. Do not do so until access is approved.",
    ],
)
def test_qualified_actions_keep_complete_guidance_without_unconditional_badge(
    directive, action, form
):
    advice = form.format(directive)
    _, report = render(catalog_for(f"## {CVE}\n\n{advice}"))
    assert "**Action**: none" in report
    assert f"**Recommended Actions**: {advice}" in report


@pytest.mark.parametrize(
    "advice",
    [
        "Users previously monitored logs.",
        "Should users monitor logs?",
        "Users are advised to review the advisory, which mentions logs.",
        "Users are advised to apply the workaround before installing the patch.",
    ],
)
def test_background_words_do_not_select_an_unrelated_action(advice):
    expected = "mitigate" if "workaround" in advice else "none"
    assert recommendation_action([advice]) == expected


def test_action_contract_covers_the_published_enum():
    assert {action for _, action in DIRECTIVES} == {action.value for action in Action}


@pytest.mark.parametrize(("directive", "action"), DIRECTIVES)
def test_real_pipeline_serializes_source_owned_action(
    monkeypatch, tmp_path, directive, action
):
    advice = f"Users are advised to {directive}."
    article = dict(
        title="Example advisory",
        source="Publisher",
        link="https://example.test/advisory",
        content=f"## {CVE}\n\n{CVE} exploitation has not been observed.\n\n{advice}",
        content_kind="article",
    )
    result = run_real_pipeline(monkeypatch, tmp_path / "index.md", articles=[article])
    assert result["status"] == "completed", result
    manifest = json.loads((tmp_path / "current-findings.json").read_text())
    assert manifest["finding_count"] == 1
    artifact = parse_report_artifact((tmp_path / "index.md").read_text())
    assert artifact.findings[0].action.value == action
    assert artifact.findings[0].recommended_actions == advice
    assert f'"action":"{action}"' in (tmp_path / "index.html").read_text()

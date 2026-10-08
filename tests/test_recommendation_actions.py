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


@pytest.mark.parametrize(
    "audience",
    [
        "Users of affected systems",
        "Customers running version 2.0",
        "Administrators of the affected appliances",
        "Users on version 2.0",
    ],
)
@pytest.mark.parametrize(
    ("modal", "action"),
    [
        ("should", "patch"),
        ("are advised to", "patch"),
        ("should not", "none"),
    ],
)
def test_bounded_audience_noun_qualifiers_keep_direct_modal_ownership(
    audience, modal, action
):
    advice = f"{audience} {modal} install the patch."
    _, report = render(catalog_for(f"## {CVE}\n\n{advice}"))
    assert f"**Action**: {action}" in report
    assert f"**Recommended Actions**: {advice}" in report


@pytest.mark.parametrize(
    "narrative",
    [
        "Patch Tuesday updates addressed 50 flaws.",
        "Update 1.2 fixes the vulnerability.",
        "Monitor logs indicate that the service restarted.",
        "Patch systems are available for download.",
        "Patch Tuesday updates will fail if the service is running.",
        "Update 1.2 does not fix the vulnerability.",
        "Patch systems with updates addressed 50 flaws.",
        "When asked why anyone should believe the interviewee, the reporter questioned the story.",
    ],
)
def test_descriptive_nouns_never_become_recommendations(narrative):
    _, report = render(catalog_for(f"## {CVE}\n\n{narrative}"))
    assert "**Action**: none" in report
    assert "**Recommended Actions**: Not stated in supplied sources." in report


@pytest.mark.parametrize(
    ("advice", "action"),
    [
        ("Users should monitor logs and install the update.", "patch"),
        ("Users should investigate suspicious activity and patch systems.", "patch"),
        ("Users should install the update and monitor logs.", "patch"),
        ("Monitor logs and apply the workaround.", "mitigate"),
        (
            "Users should monitor logs, review indicators of compromise, and apply the patch.",
            "patch",
        ),
        ("Users should monitor logs and not install the update.", "monitor"),
        (
            "Users should monitor logs and install the update only if exposed.",
            "monitor",
        ),
        ("Users should monitor logs or install the update.", "none"),
        ("Users should monitor logs and consider installing an update.", "none"),
        ("Monitor logs and consider installing an update.", "none"),
        ("Users should monitor logs and traffic.", "monitor"),
    ],
)
def test_coordinated_directives_preserve_structure_before_badge_priority(
    advice, action
):
    _, report = render(catalog_for(f"## {CVE}\n\n{advice}"))
    assert f"**Action**: {action}" in report
    assert f"**Recommended Actions**: {advice}" in report


def test_actions_follow_singleton_and_shared_cve_ownership():
    other = "CVE-2026-5678"
    records, _ = render(
        catalog_for(
            f"## {CVE}\n\nUsers should monitor logs.\n\n"
            f"## {other}\n\nUsers should apply the update."
        )
    )
    assert {record.cves: dict(record.fields)["Action"] for record in records} == {
        (CVE,): "monitor",
        (other,): "patch",
    }
    records, report = render(
        catalog_for(
            f"For {CVE} and {other}, users should monitor logs and install the update."
        )
    )
    assert len(records) == 1
    assert set(records[0].cves) == {CVE, other}
    assert "**Action**: patch" in report


@pytest.mark.parametrize(
    ("advice", "action"),
    [
        ("Users should monitor logs and install the update.", "patch"),
        ("Users should monitor logs and not install the update.", "monitor"),
        (
            "Users should monitor logs and install the update only if exposed.",
            "monitor",
        ),
        ("Users should monitor logs or install the update.", "none"),
        ("Monitor logs and consider installing an update.", "none"),
        ("Users deny that they should install the patch.", "none"),
        ("Users are unsure whether they should install the patch.", "none"),
    ],
)
def test_real_pipeline_keeps_qualified_and_coordinated_guidance(
    monkeypatch, tmp_path, advice, action
):
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[
            dict(
                title="Example advisory",
                source="Publisher",
                link="https://example.test/advisory",
                content=f"## {CVE}\n\n{CVE} exploitation status is unknown.\n\n{advice}",
                content_kind="article",
            )
        ],
    )
    assert result["status"] == "completed", result
    artifact = parse_report_artifact((tmp_path / "index.md").read_text())
    assert artifact.findings[0].action.value == action
    assert artifact.findings[0].recommended_actions == advice


def test_parsed_directive_retains_modality_polarity_conditions_and_coordination():
    from src.core.recommendations import parse_recommendation

    text = "Users should monitor logs and not install the update until verification completes."
    directive = parse_recommendation(text)
    assert directive is not None
    assert directive.source_text == text
    assert directive.modality == "advice"
    assert [(clause.verb, clause.polarity) for clause in directive.clauses] == [
        ("monitor", "affirmative"),
        ("install", "negative"),
    ]
    assert directive.clauses[0].conditions == ()
    assert directive.clauses[1].conditions == ("until verification completes",)


@pytest.mark.parametrize(
    ("advice", "with_patch"),
    [
        ("Users deny that they should install the patch.", "none"),
        ("Users are unsure whether they should install the patch.", "none"),
        ("Users say that operators should monitor logs.", "patch"),
        ("Users wonder if they should apply the workaround.", "patch"),
        ("Users question whether investigators are advised to review logs.", "patch"),
        ("Users with an unclassified relation should install the patch.", "none"),
        (
            "Users of systems if they are unsure whether they should install the patch.",
            "none",
        ),
        ("Users of systems when they deny that they should install the patch.", "none"),
    ],
)
def test_intervening_relations_cannot_establish_advice_ownership(advice, with_patch):
    for prefix in ("", "Users should install the patch. "):
        source = prefix + advice
        _, report = render(catalog_for(f"## {CVE}\n\n{source}"))
        assert f"**Action**: {with_patch if prefix else 'none'}" in report
        assert f"**Recommended Actions**: {source}" in report


@pytest.mark.parametrize(
    ("guidance", "action"),
    [
        (
            "Users should install the patch. Users should monitor logs if suspicious activity occurs.",
            "patch",
        ),
        ("Users should install the patch. Users should not monitor logs.", "patch"),
        ("Users should install the patch. Users should apply no workaround.", "patch"),
        (
            "Users should install the patch. Users should consult the advisory. Do not do so until access is approved.",
            "patch",
        ),
        (
            "Users should monitor logs. Users should install the patch if exposed.",
            "monitor",
        ),
        ("Users should install the patch. Users should not install the patch.", "none"),
        (
            "Users should install the patch. Users should install the patch only if exposed.",
            "none",
        ),
        (
            "Users should monitor vendor advisories. Users should not monitor logs.",
            "monitor",
        ),
        (
            "Users should monitor logs. Users should not monitor logs from the gateway.",
            "none",
        ),
        ("Users should monitor logs. Users should monitor no logs.", "none"),
        (
            "Users should monitor logs. Users should not monitor logs and traffic.",
            "none",
        ),
        (
            "Users should monitor logs and traffic. Users should not monitor logs.",
            "monitor",
        ),
        (
            "Users should install the patch. Users should monitor logs. Do not do so until access is approved.",
            "patch",
        ),
        (
            "Users should install the patch. Do not do so until access is approved.",
            "none",
        ),
        (
            "Users should install the patch.\n\nDo not do so until access is approved.",
            "none",
        ),
        (
            "Users should install the patch. If exposed, users should monitor logs.",
            "patch",
        ),
        (
            "Users should install the patch. If exposed, users should install the patch.",
            "none",
        ),
    ],
)
def test_directive_qualification_ownership_in_real_pipeline(
    monkeypatch, tmp_path, guidance, action
):
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[
            dict(
                title="Example advisory",
                source="Publisher",
                link="https://example.test/advisory",
                content=f"## {CVE}\n\n{CVE} exploitation status is unknown.\n\n{guidance}",
                content_kind="article",
            )
        ],
    )
    assert result["status"] == "completed", result
    artifact = parse_report_artifact((tmp_path / "index.md").read_text())
    assert artifact.findings[0].action.value == action
    for block in guidance.split("\n\n"):
        assert block in artifact.findings[0].recommended_actions


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

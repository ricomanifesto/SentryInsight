"""Finite object/modifier ownership oracle, frozen before implementation.

Exactly one terminal immediately/as-soon-as-possible modifier follows a complete
existing argument. Conditions and clause boundaries keep their existing owners.
Unknown residuals fail closed; recognition never strips arbitrary adverbs.
"""

import json

import pytest

from src.core.finding_evidence import recommendation_action
from src.core.recommendations import parse_recommendation
from src.core.report_artifact import parse_report_artifact
from test_finding_generation_pipeline import run_real_pipeline
from test_owned_relation_contract import article

CVE = "CVE-2026-1234"
MODIFIERS = ["immediately", "as soon as possible"]


def pipeline(monkeypatch, tmp_path, guidance, action=None):
    previous = {
        "index.md": b"Previous report",
        "index.html": b"Previous site",
        "current-findings.json": b'{"previous":true}',
        ".sentryinsight-articles-fingerprint": b"previous-inputs\n",
    }
    if action is None:
        for name, data in previous.items():
            (tmp_path / name).write_bytes(data)
    source = f"## {CVE}\n\n{CVE} exploitation status is unknown.\n\n{guidance}"
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[article(source)],
        expect_model_call=action is not None,
    )
    if action is None:
        assert result["status"] == "failed", result
        assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
        assert all(
            (tmp_path / name).read_bytes() == data for name, data in previous.items()
        )
    else:
        assert result["status"] == "completed", result
        (finding,) = parse_report_artifact((tmp_path / "index.md").read_text()).findings
        assert finding.action.value == action
        assert finding.recommended_actions == guidance
        saved = json.loads((tmp_path / "current-findings.json").read_text())
        assert saved["finding_count"] == 1


@pytest.mark.parametrize("modifier", MODIFIERS)
@pytest.mark.parametrize(
    "instruction,objects,action",
    [
        ("install the patch", ("patch",), "patch"),
        ("upgrade to version 2.0", ("release",), "patch"),
        ("upgrade the appliance to version 2.0", ("system",), "patch"),
        ("apply the patch and the workaround", ("patch", "mitigation"), "patch"),
        ("apply the workaround", ("mitigation",), "mitigate"),
        ("investigate suspicious activity", ("evidence",), "investigate"),
        ("monitor logs and traffic", ("evidence", "monitoring"), "monitor"),
        ("restart the service", ("service",), "none"),
    ],
)
@pytest.mark.parametrize("form", ["affirmative", "negative", "conditional"])
def test_terminal_modifier_is_owned_separately_from_complete_argument(
    monkeypatch, tmp_path, modifier, instruction, objects, action, form
):
    guidance = (
        "Users should "
        + ("not " if form == "negative" else "")
        + instruction
        + " "
        + modifier
        + (", if needed" if form == "conditional" else "")
        + "."
    )
    parsed = parse_recommendation(guidance)
    assert parsed is not None and not parsed.ambiguous
    assert parsed.source_text == guidance and len(parsed.clauses) == 1
    (clause,) = parsed.clauses
    assert clause.object_members == objects
    assert clause.directive_modifiers == (modifier,)
    assert modifier not in clause.object_text
    assert clause.polarity == ("negative" if form == "negative" else "affirmative")
    assert clause.conditions == (("if needed",) if form == "conditional" else ())
    expected = action if form == "affirmative" else "none"
    assert recommendation_action([guidance]) == expected
    pipeline(monkeypatch, tmp_path, guidance, expected)


@pytest.mark.parametrize("modifier", MODIFIERS)
@pytest.mark.parametrize("connector", [" and ", ", and ", ", but ", " then ", "; "])
@pytest.mark.parametrize("reverse", [False, True])
def test_modifier_and_condition_do_not_cross_independent_directives(
    monkeypatch, tmp_path, modifier, connector, reverse
):
    clauses = [
        f"Users should install the patch {modifier}",
        "Users should monitor logs, if needed",
    ]
    if reverse:
        clauses.reverse()
    guidance = connector.join(clauses) + "."
    parsed = parse_recommendation(guidance)
    assert parsed is not None and not parsed.ambiguous
    assert len(parsed.clauses) == 2
    patch = next(c for c in parsed.clauses if c.verb == "install")
    monitor = next(c for c in parsed.clauses if c.verb == "monitor")
    assert patch.directive_modifiers == (modifier,) and not patch.conditions
    assert monitor.directive_modifiers == () and monitor.conditions == ("if needed",)
    pipeline(monkeypatch, tmp_path, guidance, "patch")


@pytest.mark.parametrize("modifier", MODIFIERS)
@pytest.mark.parametrize(
    "form,action",
    [
        ("Users should install the patch, {}.", "patch"),
        ("Install the patch {}.", "patch"),
        ("If needed, users should install the patch {}.", "none"),
        ("Users should not install the patch {} but monitor logs.", "monitor"),
        ("Users should install the patch {} but must not install the patch.", "none"),
        ("Users should install the patch {} or apply the workaround.", "none"),
        ("Users should install the patch {} and apply the workaround.", "patch"),
        ("Users should install the patch if needed {}.", "none"),
    ],
)
def test_modifier_keeps_polarity_conditions_conflicts_and_alternatives(
    monkeypatch, tmp_path, modifier, form, action
):
    pipeline(monkeypatch, tmp_path, form.format(modifier), action)


@pytest.mark.parametrize("modifier", MODIFIERS)
@pytest.mark.parametrize(
    "form",
    [
        "Users should install the report {}.",
        "Users should update the advisory {}.",
        "Users should install the patch {} and consider installing an update.",
        "Users should install the patch {} and assess whether to upgrade the system.",
        "Users should install the patch {} while considering whether to act.",
        "Users should apply the patch {} and the workaround.",
        "Users should apply the patch and the workaround {} and the update.",
        "Users should install the patch {} {}.",
        "Users of systems {} should install the patch.",
        "Users of systems claim that they should install the patch {}.",
        "Users should install the patch {} if needed and consider an update.",
    ],
)
def test_modifier_does_not_hide_unknown_target_bridge_or_residual_advice(
    monkeypatch, tmp_path, modifier, form
):
    pipeline(monkeypatch, tmp_path, form.format(modifier, modifier))


@pytest.mark.parametrize(
    "tail",
    [
        "quietly",
        "eventually",
        "conditionally",
        "as circumstances permit",
        "with urgency",
    ],
)
def test_unknown_modifier_is_terminal_before_transport(monkeypatch, tmp_path, tail):
    pipeline(monkeypatch, tmp_path, f"Users should install the patch {tail}.")

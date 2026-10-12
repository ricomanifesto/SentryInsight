"""Direct and reported advice share one finite operator contract."""

import pytest

from src.core.recommendations import parse_recommendation
from test_directive_modifier_contract import pipeline

FORMS = [("advised", "advise"), ("recommended", "recommend"), ("urged", "urge")]


def guidance(voice, participle, root, modifier, form, instruction="install the patch"):
    intensity = modifier + " " if modifier else ""
    prohibition = "not " if form == "prohibited" else ""
    condition = ", if needed" if form == "conditional" else ""
    if voice == "direct":
        prefix = "Users are " + ("not " if form == "negated" else "")
        prefix += intensity + participle + " " + prohibition + "to "
    else:
        finite = (
            "did not " + intensity + root
            if form == "negated"
            else intensity + participle
        )
        prefix = "The vendor " + finite + " users " + prohibition + "to "
    return prefix + instruction + condition + "."


@pytest.mark.parametrize("voice", ["direct", "reported"])
@pytest.mark.parametrize("participle,root", FORMS)
@pytest.mark.parametrize(
    "form", ["affirmative", "prohibited", "negated", "conditional"]
)
def test_shared_operator_keeps_polarity_and_complete_pipeline_guidance(
    monkeypatch, tmp_path, voice, participle, root, form
):
    for modifier in ("", "strongly"):
        text = guidance(voice, participle, root, modifier, form)
        parsed = parse_recommendation(text)
        assert parsed is not None and not parsed.ambiguous
        assert parsed.source_text == text and len(parsed.clauses) == 1
        (clause,) = parsed.clauses
        assert clause.verb == "install" and clause.object_members == ("patch",)
        assert clause.polarity == (
            "negative"
            if form == "prohibited" or voice == "direct" and form == "negated"
            else "affirmative"
        )
        assert clause.conditions == (("if needed",) if form == "conditional" else ())
        if voice == "reported":
            assert clause.reporter and clause.reporter.subject == "The vendor"
            assert clause.reporter.polarity == (
                "negative" if form == "negated" else "affirmative"
            )
            assert ("strongly" in clause.reporter.finite) == bool(modifier)
        else:
            assert clause.reporter is None
        assert ("strongly" in clause.modal) == bool(modifier)
        target = tmp_path / (modifier or "ordinary")
        target.mkdir()
        pipeline(
            monkeypatch, target, text, "patch" if form == "affirmative" else "none"
        )


@pytest.mark.parametrize("voice", ["direct", "reported"])
@pytest.mark.parametrize(
    "instruction,action",
    [
        ("upgrade to version 2.0", "patch"),
        ("upgrade the appliance to version 2.0", "patch"),
        ("apply the patch and the workaround", "patch"),
        ("install the patch immediately and monitor logs, if needed", "patch"),
        ("monitor logs, if needed, but install the patch", "patch"),
        ("not install the patch but monitor logs", "monitor"),
    ],
)
def test_operator_leaves_targets_coordination_and_qualifiers_with_existing_owners(
    monkeypatch, tmp_path, voice, instruction, action
):
    text = guidance(voice, "advised", "advise", "strongly", "affirmative", instruction)
    pipeline(monkeypatch, tmp_path, text, action)


@pytest.mark.parametrize(
    "text,action",
    [
        (
            "Users of affected systems are strongly advised to install the patch.",
            "patch",
        ),
        (
            "Customers running version 2.0 are strongly advised not to install the patch.",
            "none",
        ),
        ("If needed, users are strongly advised to install the patch.", "none"),
        (
            "The vendor strongly advised affected customers to install the patch.",
            "patch",
        ),
        (
            "If needed, the vendor strongly advised affected customers to install the patch.",
            "none",
        ),
        ("Users are strongly encouraged to install the patch.", "patch"),
        (
            '"Users are strongly advised to install the patch," the company said.',
            "patch",
        ),
    ],
)
def test_supported_audience_and_reporting_boundaries_survive_intensification(
    monkeypatch, tmp_path, text, action
):
    pipeline(monkeypatch, tmp_path, text, action)


@pytest.mark.parametrize("voice", ["direct", "reported"])
@pytest.mark.parametrize(
    "modifier", ["strongly strongly", "extremely", "allegedly", "unexpectedly"]
)
def test_unknown_or_repeated_intensifier_preserves_all_prior_artifacts(
    monkeypatch, tmp_path, voice, modifier
):
    pipeline(
        monkeypatch,
        tmp_path,
        guidance(voice, "advised", "advise", modifier, "affirmative"),
    )


@pytest.mark.parametrize(
    "text",
    [
        "Users strongly are advised to install the patch.",
        "Users are advised strongly to install the patch.",
        "Users are strongly advised to install the patch with unspecified requirements.",
        "The vendor strongly advised users to install the patch with unspecified requirements.",
        "Users are strongly advised to install the patch and unidentified predicates apply.",
        "The vendor strongly advised users to install the patch and unidentified predicates apply.",
        "Users through an unknown relation are strongly advised to install the patch.",
        "The vendor allegedly strongly advised users to install the patch.",
        "The vendor strongly encouraged users to install the patch.",
    ],
)
def test_operator_cannot_swallow_unknown_bridges_or_residual_advice(
    monkeypatch, tmp_path, text
):
    pipeline(monkeypatch, tmp_path, text)

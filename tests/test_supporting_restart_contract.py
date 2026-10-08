"""Supporting operational advice retains ownership without a primary-action badge.

Finite targets: existing system nouns and service(s). Existing directive modal,
polarity, conditions and coordination apply. Retained temporal context includes
afterward and during recovery; arbitrary target tails stay unsupported.
"""

import pytest

from src.core.finding_evidence import recommendation_action
from src.core.recommendations import parse_recommendation
from src.core.report_artifact import parse_report_artifact
from test_finding_generation_pipeline import run_real_pipeline
from test_owned_relation_contract import article
from test_relation_totality_contract import assert_preserved_unsupported

CVE = "CVE-2026-1234"


@pytest.mark.parametrize("target", ["the service", "the system", "affected systems"])
@pytest.mark.parametrize(
    "form,negative,qualified",
    [
        ("Restart {}.", False, False),
        ("Users should restart {}.", False, False),
        ("Do not restart {}.", True, False),
        ("Users are not advised to restart {}.", True, False),
        ("Restart {} only after backing up the configuration.", False, True),
        ("If exposed, restart {}.", False, True),
        ("Restart {} afterward.", False, False),
        ("Never restart {} during recovery.", True, False),
    ],
)
def test_restart_has_complete_supporting_relation(target, form, negative, qualified):
    text = form.format(target)
    directive = parse_recommendation(text)
    assert directive is not None and not directive.ambiguous
    assert directive.source_text == text
    assert len(directive.clauses) == 1
    clause = directive.clauses[0]
    assert clause.verb == "restart" and not clause.unsupported
    assert clause.object_members
    assert clause.polarity == ("negative" if negative else "affirmative")
    assert bool(clause.conditions or directive.conditions) is qualified
    assert recommendation_action([text]) == "none"


@pytest.mark.parametrize(
    "restart",
    [
        "Restart the service.",
        "Restart the service only after backing up the configuration.",
        "Do not restart the service.",
        "Never restart the service during recovery.",
    ],
)
@pytest.mark.parametrize(
    "primary,action",
    [
        ("", "none"),
        ("Users should install the patch.", "patch"),
        ("Users should monitor logs.", "monitor"),
    ],
)
@pytest.mark.parametrize("reverse", [False, True])
def test_supporting_restart_pipeline_preserves_primary_priority_and_truthful_label(
    monkeypatch, tmp_path, restart, primary, action, reverse
):
    parts = [p for p in (primary, restart) if p]
    guidance = " ".join(reversed(parts) if reverse else parts)
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[
            article(f"## {CVE}\n\n{CVE} exploitation status is unknown.\n\n{guidance}")
        ],
    )
    assert result["status"] == "completed", result
    report = (tmp_path / "index.md").read_text()
    finding = parse_report_artifact(report).findings[0]
    assert finding.action.value == action
    assert finding.recommended_actions == guidance
    html = (tmp_path / "index.html").read_text()
    assert "No action listed" not in html
    if action == "none":
        assert "Action not classified" in html
        assert 'data-action="none"' in html


@pytest.mark.parametrize(
    "guidance",
    [
        "Users should restart the advisory.",
        "Restart the vendor.",
        "Users with an unclassified relation should restart the service.",
        "Restart the service with an unclassified setting.",
        "Users should restart.",
    ],
)
def test_unknown_restart_ownership_remains_unsupported(monkeypatch, tmp_path, guidance):
    assert_preserved_unsupported(
        monkeypatch,
        tmp_path,
        f"## {CVE}\n\n{CVE} exploitation status is unknown.\n\n{guidance}",
    )


def test_restart_continuation_cannot_rebind_an_earlier_primary_action():
    guidance = "Users should install the patch. Restart the service. Do not do so."
    assert recommendation_action([guidance]) == "patch"

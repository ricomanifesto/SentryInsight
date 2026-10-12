"""Urgency support cannot turn a discarded audience into an imperative.

These cases preserve the existing complete logical-block ownership contract;
they add no supported audience grammar or assertion sentence productions.
"""

import pytest

from src.core.finding_evidence import recommendation_action
from src.core.report_artifact import parse_report_artifact
from test_directive_modifier_contract import pipeline
from test_finding_generation_pipeline import run_real_pipeline
from test_owned_relation_contract import article


@pytest.mark.parametrize("audience", ["U.S. customers", "U.K. users"])
@pytest.mark.parametrize("separator", [" ", "\n"])
@pytest.mark.parametrize("modifier", ["immediately", "as soon as possible"])
def test_unsupported_audience_stays_owned_across_soft_wraps(
    monkeypatch, tmp_path, audience, separator, modifier
):
    guidance = f"{audience} should{separator}install the patch {modifier}."
    assert recommendation_action([guidance]) == "none"
    pipeline(monkeypatch, tmp_path, guidance)


@pytest.mark.parametrize("separator", [" ", "\n"])
@pytest.mark.parametrize(
    "guidance,action",
    [
        ("Users should{}install the patch immediately.", "patch"),
        ("Users should not{}install the patch immediately.", "none"),
        (
            "Users are unsure whether they should{}install the patch immediately.",
            "none",
        ),
        ("Install{}the patch immediately.", "patch"),
        ("Users should install the patch.{}Monitor logs as soon as possible.", "patch"),
    ],
)
def test_logical_guidance_keeps_its_existing_modality_and_sentence_boundaries(
    monkeypatch, tmp_path, separator, guidance, action
):
    text = guidance.format(separator)
    assert recommendation_action([text]) == action
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[
            article(
                f"## CVE-2026-1234\n\nCVE-2026-1234 exploitation status is unknown.\n\n{text}"
            )
        ],
    )
    assert result["status"] == "completed", result
    (finding,) = parse_report_artifact((tmp_path / "index.md").read_text()).findings
    assert finding.action.value == action
    assert finding.recommended_actions == " ".join(text.split())

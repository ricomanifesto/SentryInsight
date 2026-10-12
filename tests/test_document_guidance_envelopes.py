"""Source reporting/context boundaries do not discard guidance or polarity."""

import pytest

from src.core.finding_evidence import recommendation_action
from test_composed_document_pipeline_contract import article
from test_finding_generation_pipeline import run_real_pipeline


@pytest.mark.parametrize(
    "text,action",
    [
        ('"Users should install the patch," the company said.', "patch"),
        ('"Users should not install the patch," the company said.', "none"),
        ('"Users should install the patch only if exposed," the company said.', "none"),
        (
            '"There is no action you need to take on your account," Example says in its message to customers.',
            "none",
        ),
        (
            "As of October 5, 2026, all the extensions have been removed. Users who have installed the extensions and entered a recovery phrase into the fake interfaces should assume compromise, create a new wallet from a clean system, and move their assets.",
            "none",
        ),
    ],
)
def test_complete_guidance_envelope_reaches_real_pipeline(
    monkeypatch, tmp_path, text, action
):
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[
            article(
                f"<h2>CVE-2026-1234</h2><p>CVE-2026-1234 exploitation status is unknown.</p><p>{text}</p>"
            )
        ],
    )
    assert result["status"] == "completed", result
    report = (tmp_path / "index.md").read_text()
    assert text in report and f"**Action**: {action}" in report


@pytest.mark.parametrize(
    "text",
    [
        '"Users should install the patch," unknown structures claim a conclusion.',
        '"Users should install the patch," the company might say.',
        'Unclassified prefix. "Users should install the patch," the company said.',
    ],
)
def test_unknown_envelope_does_not_promote_its_quoted_directive(
    monkeypatch, tmp_path, text
):
    paths = [
        tmp_path / name
        for name in (
            "index.md",
            "index.html",
            "current-findings.json",
            ".sentryinsight-articles-fingerprint",
        )
    ]
    for path in paths:
        path.write_bytes(b"Prior validated artifact")
    result = run_real_pipeline(
        monkeypatch,
        paths[0],
        articles=[
            article(
                f"<h2>CVE-2026-1234</h2><p>CVE-2026-1234 exploitation status is unknown.</p><p>{text}</p>"
            )
        ],
        expect_model_call=False,
    )
    assert (
        result["status"] == "failed"
        and result["analysis_results"]["error"] == "unsupported_evidence_relation"
    )
    assert all(path.read_bytes() == b"Prior validated artifact" for path in paths)


@pytest.mark.parametrize(
    "modifier", ["possibly", "allegedly", "unlikely", "hypothetically", "unpredictably"]
)
def test_unknown_directive_modifier_cannot_be_stripped_by_word_suffix(
    monkeypatch, tmp_path, modifier
):
    test_unknown_envelope_does_not_promote_its_quoted_directive(
        monkeypatch, tmp_path, f"Users should {modifier} install the patch."
    )


def test_supported_initial_urgency_is_retained_as_owned_modifier():
    from src.core.recommendations import parse_recommendation

    parsed = parse_recommendation("Users should immediately install the patch.")
    assert parsed and not parsed.ambiguous
    assert parsed.clauses[0].directive_modifiers == ("immediately",)
    assert (
        recommendation_action(["Users should immediately install the patch."])
        == "patch"
    )

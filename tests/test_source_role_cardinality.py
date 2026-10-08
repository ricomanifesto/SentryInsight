"""Source roles and directive references are nonexclusive, ordered ownership."""

import pytest

from src.core.report_artifact import parse_report_artifact
from test_finding_generation_pipeline import run_real_pipeline


@pytest.mark.parametrize("quantifier", ["the", "all", "any", "each", "every"])
@pytest.mark.parametrize("separator", [". ", "; "])
@pytest.mark.parametrize("joint", [False, True])
@pytest.mark.parametrize("advice_first", [False, True])
@pytest.mark.parametrize(
    ("guidance", "action"),
    [
        (
            "{audience} should install the patch; administrators should do so immediately.",
            "patch",
        ),
        ("{audience} should install the patch and do so immediately.", "patch"),
        (
            "{audience} should install the patch; administrators should not do so until access is approved.",
            "none",
        ),
        (
            "{audience} should install the patch and not do so until access is approved.",
            "none",
        ),
        (
            "{audience} should install the patch; administrators should do so only if exposed.",
            "none",
        ),
        (
            "Administrators should do so immediately; {audience} should install the patch.",
            "patch",
        ),
        (
            "Administrators should not do so until access is approved; {audience} should install the patch.",
            "none",
        ),
        (
            "{audience} should monitor logs; administrators should not do so; users should install the patch.",
            "patch",
        ),
        (
            "{audience} should not install the patch; administrators should do so immediately.",
            "none",
        ),
    ],
)
def test_mixed_roles_and_reference_ownership_through_real_pipeline(
    monkeypatch, tmp_path, quantifier, separator, joint, advice_first, guidance, action
):
    cves = "CVE-2026-1234 and CVE-2026-5678" if joint else "CVE-2026-1234"
    detail = (
        f"{cves} exploitation status is unknown. "
        f"{cves} allows remote code execution on the gateway."
    )
    noun = "system" if quantifier in {"each", "every"} else "systems"
    advice = guidance.format(audience=f"Users of {quantifier} affected {noun}")
    ordered = [advice, detail] if advice_first else [detail, advice]
    paragraph = separator.join(part.rstrip(".") for part in ordered) + "."
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[
            dict(
                title="Example security advisory",
                source="Publisher",
                link="https://example.test/cardinality",
                content_kind="article",
                content=f"## {cves}\n\n{paragraph}",
            )
        ],
    )
    assert result["status"] == "completed", result
    report = (tmp_path / "index.md").read_text()
    artifact = parse_report_artifact(report)
    assert len(artifact.findings) == 1
    finding = artifact.findings[0]
    assert finding.action.value == action
    assert paragraph in finding.recommended_actions
    assert f"**Description**: {paragraph}" in report
    assert f"**Impact**: {paragraph}" in report
    assert paragraph in report.split("## Attack Vectors and Techniques", 1)[1]


@pytest.mark.parametrize("quantifier", ["all", "any", "each", "every", "no"])
def test_nominal_quantifiers_preserve_negative_and_conditional_guidance(quantifier):
    from src.core.finding_evidence import recommendation_action

    audience = f"Users of {quantifier} affected systems"
    assert (
        recommendation_action([f"{audience} should not install the patch."]) == "none"
    )
    assert (
        recommendation_action([f"{audience} should install the patch only if exposed."])
        == "none"
    )
    if quantifier == "no":
        assert (
            recommendation_action([f"{audience} should install the patch."]) == "none"
        )


@pytest.mark.parametrize(
    "guidance",
    [
        "Users should install the patch; only if exposed.",
        "Users should install the patch. A different operation follows. Do not do so.",
        "Users should install the patch; a different operation follows; do not do so.",
    ],
)
def test_continuation_limits_preserve_unresolved_qualifications(guidance):
    from src.core.finding_evidence import recommendation_action

    assert recommendation_action([guidance]) == "none"


@pytest.mark.parametrize("condition", ["If", "Unless", "When", "Until"])
def test_leading_condition_owns_explicit_clause_instead_of_prior_directive(condition):
    from src.core.finding_evidence import recommendation_action

    guidance = f"Users should install the patch; {condition} exposed, users should monitor logs."
    assert recommendation_action([guidance]) == "patch"

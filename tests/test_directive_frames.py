"""Independent acceptance for bounded verb arguments and conjunction semantics."""

import pytest

from src.core.finding_evidence import recommendation_action
from src.core.report_artifact import parse_report_artifact
from test_finding_generation_pipeline import run_real_pipeline


def pipeline_action(monkeypatch, tmp_path, guidance, *, unsupported=False):
    paragraph = (
        "CVE-2026-1234 exploitation status is unknown. "
        f"CVE-2026-1234 allows remote code execution on the gateway. {guidance}"
    )
    previous = {
        "index.md": b"Previous validated report",
        "index.html": b"Previous site",
        "current-findings.json": b'{"previous":true}',
    }
    if unsupported:
        for name, content in previous.items():
            (tmp_path / name).write_bytes(content)
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[
            dict(
                title="Example security advisory",
                source="Publisher",
                link="https://example.test/frames",
                content_kind="article",
                content=paragraph,
            )
        ],
        expect_model_call=not unsupported,
    )
    if unsupported:
        assert result["status"] == "failed", result
        assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
        assert all(
            (tmp_path / name).read_bytes() == content
            for name, content in previous.items()
        )
        return None
    assert result["status"] == "completed", result
    finding = parse_report_artifact((tmp_path / "index.md").read_text()).findings[0]
    assert paragraph in finding.recommended_actions
    return finding.action.value


@pytest.mark.parametrize(
    ("instruction", "action"),
    [
        ("install the patch", "patch"),
        ("apply the update", "patch"),
        ("patch systems", "patch"),
        ("upgrade the appliance", "patch"),
        ("upgrade to version 2.0", "patch"),
        ("upgrade the appliance to version 2.0", "patch"),
        ("update to version 2.0", "patch"),
        ("update software to version 2.0", "patch"),
        ("apply the workaround", "mitigate"),
        ("apply the patch and the workaround", "patch"),
        ("apply the patch or the workaround", "none"),
        ("mitigate the vulnerability", "mitigate"),
        ("review logs", "investigate"),
        ("investigate suspicious activity", "investigate"),
        ("monitor vendor advisories", "monitor"),
        ("consult the advisory", "none"),
        ("contact support", "none"),
        ("review the advisory", "none"),
        ("update the advisory", "none"),
        ("upgrade to the vendor", "none"),
        ("upgrade the appliance to the advisory", "none"),
    ],
)
@pytest.mark.parametrize(
    "form",
    ["Users should {}.", "Users should not {}.", "Users should {} only if exposed."],
)
def test_bounded_frames_keep_action_polarity_and_conditions(
    monkeypatch, tmp_path, instruction, action, form
):
    expected = action if form == "Users should {}." else "none"
    guidance = form.format(instruction)
    # These original negative argument cases still cannot project an action.
    # The stricter publication contract also rejects their unclassified frame.
    if instruction in {
        "update the advisory",
        "upgrade to the vendor",
        "upgrade the appliance to the advisory",
    }:
        assert recommendation_action([guidance]) == expected == "none"
        assert (
            pipeline_action(monkeypatch, tmp_path, guidance, unsupported=True) is None
        )
    else:
        assert pipeline_action(monkeypatch, tmp_path, guidance) == expected


@pytest.mark.parametrize(
    "destination",
    [
        "upgrade to version 2.0",
        "upgrade the appliance to version 2.0",
        "install the patch",
    ],
)
@pytest.mark.parametrize("connector", ["and", ", and", "but", ", but", "then", "or"])
@pytest.mark.parametrize("reverse", [False, True])
def test_argument_frames_and_conjunction_ownership_cross_product(
    monkeypatch, tmp_path, destination, connector, reverse
):
    clauses = [
        f"Users should {destination}",
        "administrators should monitor logs if suspicious activity occurs",
    ]
    if reverse:
        clauses.reverse()
    guidance = f" {connector} ".join(clauses) + "."
    expected = "none" if connector == "or" else "patch"
    assert pipeline_action(monkeypatch, tmp_path, guidance) == expected


@pytest.mark.parametrize(
    ("guidance", "action"),
    [
        ("Users should not install the patch and monitor logs.", "none"),
        ("Users should not install the patch, and monitor logs.", "none"),
        ("Users should not install the patch but monitor logs.", "monitor"),
        ("Users should not install the patch, but monitor logs.", "monitor"),
        ("Users should install the patch, but not monitor logs.", "patch"),
        ("Users should monitor logs but not install the patch.", "monitor"),
        (
            "Users should not install the patch and administrators should monitor logs.",
            "monitor",
        ),
        (
            "Users should install the patch but administrators should not install it.",
            "none",
        ),
        (
            "Users should upgrade to version 2.0; do not do so until access is approved.",
            "none",
        ),
        (
            "Users should install the patch only if exposed but not monitor logs and apply the workaround.",
            "none",
        ),
        (
            "Users should not install the patch but monitor logs and apply the workaround.",
            "mitigate",
        ),
        (
            "Users should not install the patch and administrators should monitor logs and apply the workaround.",
            "mitigate",
        ),
    ],
)
def test_conjunction_polarity_and_reference_boundaries(
    monkeypatch, tmp_path, guidance, action
):
    assert pipeline_action(monkeypatch, tmp_path, guidance) == action

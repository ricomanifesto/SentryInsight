"""Destination rows and CVE owners retain their existing document boundaries."""

import httpx
import pytest
from src.core.finding_evidence import EvidenceError
from src.core.reporting import build_reporting_catalog
from src.core.finding_generation import compile_finding_records
from src.core.report_artifact import parse_report_artifact
from test_composed_document_pipeline_contract import article
from test_finding_generation import CVE, OTHER, render, catalog_for
from test_finding_generation_pipeline import run_real_pipeline

BASE = f"<h2>{CVE}</h2><p>{CVE} exploitation status is unknown.</p>"
INTRO = "<p>Example advised customers to upgrade vulnerable Example appliances to:</p>"


@pytest.mark.parametrize("target", ["the latest release", "the latest version"])
@pytest.mark.parametrize("negative,action", [("", "patch"), ("not ", "none")])
def test_owned_destination_rows_keep_literal_generic_identity(target, negative, action):
    html = (
        BASE
        + f"<p>Example advised customers {negative}to upgrade vulnerable Example appliances to:</p><ul><li>{target}</li></ul>"
    )
    records = compile_finding_records(build_reporting_catalog([article(html)]))
    fields = dict(records[0].fields)
    assert fields["Action"] == action and target in fields["Recommended Actions"]
    assert fields["Affected Versions"] == "Not stated in supplied sources."


@pytest.mark.parametrize(
    "html",
    [
        BASE + INTRO + "<h2>Different product</h2><ul><li>the latest release</li></ul>",
        BASE
        + INTRO
        + "<p>Unclassified intervening advice.</p><ul><li>the latest release</li></ul>",
        BASE
        + "<p>The issue impacts the following versions -</p><ul><li>the latest version</li></ul><p>Users should install the patch.</p>",
        BASE
        + "<p>Example shared the following detailed guidance on the required actions by Example version:</p><ul><li>the latest release: Install the patch.</li></ul>",
    ],
)
def test_generic_destination_cannot_supply_other_document_roles(html):
    with pytest.raises(EvidenceError):
        compile_finding_records(build_reporting_catalog([article(html)]))


@pytest.mark.parametrize(
    "text,expected",
    [
        (
            f"## {CVE}\n\nUsers should update to the latest release.\n\n## {OTHER}\n\nUsers should monitor logs.",
            {(CVE,): "patch", (OTHER,): "monitor"},
        ),
        (
            f"For {CVE} and {OTHER}, users should update to the latest version.",
            {(CVE, OTHER): "patch"},
        ),
        (
            f"## {CVE}\n\nUsers should not update to the latest release.\n\n## {OTHER}\n\nUsers should monitor logs.",
            {(CVE,): "none", (OTHER,): "monitor"},
        ),
    ],
)
def test_generic_targets_keep_singleton_joint_and_sibling_ownership(text, expected):
    records, _ = render(catalog_for(text))
    assert {
        record.cves: dict(record.fields)["Action"] for record in records
    } == expected


@pytest.mark.parametrize(
    "guidance,unsupported",
    [
        ("Users should update to the latest release.", False),
        ("Users should update to the latest version.", False),
        ("Users should update to the latest stable release.", True),
        ("The latest version should have been installed.", True),
    ],
)
def test_real_graph_publishes_owned_targets_and_preserves_artifacts_on_unknowns(
    monkeypatch, tmp_path, guidance, unsupported
):
    previous = {
        "index.md": b"previous report\n",
        "index.html": b"previous html\n",
        "current-findings.json": b'{"previous":true}\n',
        ".sentryinsight-articles-fingerprint": b"previous fingerprint\n",
    }
    if unsupported:
        for name, data in previous.items():
            (tmp_path / name).write_bytes(data)

    def forbidden(*args, **kwargs):
        raise AssertionError("Real model/HTTP transport is forbidden")

    monkeypatch.setattr(httpx.Client, "send", forbidden)
    monkeypatch.setattr(httpx.AsyncClient, "send", forbidden)
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[
            dict(
                title="Example advisory",
                source="Publisher",
                link="https://example.test/release-target",
                content_kind="article",
                content=f"## {CVE}\n\n{CVE} exploitation status is unknown. {CVE} allows remote code execution on the gateway. {guidance}",
            )
        ],
        expect_model_call=not unsupported,
    )
    if unsupported:
        assert result["status"] == "failed"
        assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
        assert all(
            (tmp_path / name).read_bytes() == data for name, data in previous.items()
        )
        return
    assert result["status"] == "completed", result
    finding = parse_report_artifact((tmp_path / "index.md").read_text()).findings[0]
    assert finding.action.value == "patch" and guidance in finding.recommended_actions
    assert finding.affected_versions == "Not stated in supplied sources."
    assert all((tmp_path / name).exists() for name in previous)

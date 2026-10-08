"""Strict publication outcomes for legacy unclassified-guidance expectations.

These are unchanged legacy source forms, not additions to the accepted grammar.
Their grounding/truncation/role checks remain in test_finding_evidence; source
qualification must not create an action, and failure preserves every artifact.
"""

import pytest

from src.core.finding_evidence import recommendation_action
from test_finding_generation_pipeline import run_real_pipeline
from test_owned_relation_contract import article

CVE = "CVE-2026-1234"


@pytest.mark.parametrize(
    "guidance",
    [
        "Do not install the update on hosted systems.",
        "Customers should not apply the patch on hosted systems.",
        "Never restart the service during recovery.",
        "Don't install the update on hosted systems.",
        "Install the update.\n\nDo not install the update on hosted systems.",
        "U.S. customers should install\nthe update immediately.",
        "- U.S. customers should install\n  the update immediately.",
        "Customers of Example Server 2.3 should install Example Server 2019 Cumulative Update 16.",
        "Customers of Example Server 2.3 should install\nExample Server 2019 Cumulative Update 16.",
    ],
)
def test_unclassified_guidance_cannot_publish_or_destroy_prior_artifacts(
    monkeypatch, tmp_path, guidance
):
    assert recommendation_action(guidance.split("\n\n")) == "none"
    previous = {
        "index.md": b"Previous validated report",
        "index.html": b"Previous site",
        "current-findings.json": b'{"previous":true}',
    }
    for name, content in previous.items():
        (tmp_path / name).write_bytes(content)
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[
            article(f"## {CVE}\n\n{CVE} exploitation status is unknown.\n\n{guidance}")
        ],
        expect_model_call=False,
    )
    assert result["status"] == "failed", result
    assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
    assert all(
        (tmp_path / name).read_bytes() == content for name, content in previous.items()
    )


def test_unclassified_html_wrapped_guidance_keeps_prior_artifacts(
    monkeypatch, tmp_path
):
    previous = {
        "index.md": b"Previous validated report",
        "index.html": b"Previous site",
        "current-findings.json": b'{"previous":true}',
    }
    for name, content in previous.items():
        (tmp_path / name).write_bytes(content)
    content = f"<h2>{CVE}</h2><p>{CVE} exploitation status is unknown.</p><p>U.S. customers should install<br>the update immediately.</p>"
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[article(content)],
        expect_model_call=False,
    )
    assert result["status"] == "failed", result
    assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
    assert all(
        (tmp_path / name).read_bytes() == content for name, content in previous.items()
    )

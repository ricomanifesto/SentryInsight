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

# One preservation case for each explicitly reconciled legacy expectation.
RECONCILED_GUIDANCE = [
    (
        "exception-advice",
        "Hosted users need no action, but administrators should install the update.",
    ),
    ("avoid-prohibition", "Avoid the unstable release and do not install the update."),
    ("no-need", "There is no need to install the update on hosted systems."),
    ("vendor-negative", "The vendor does not recommend that you install the update."),
    ("cannot", "Customers cannot install the update on hosted systems."),
    ("unable", "Customers are unable to install the update on hosted systems."),
    ("forbidden", "Customers are forbidden to install the update on hosted systems."),
    ("only", "Only install the update after backing up the database."),
    ("wrapped-audience", "U.S. customers should\ninstall the update immediately."),
    ("nested-markdown", "- Do not:\n  - install the update\n    on hosted systems."),
    (
        "nested-html",
        "<ul><li>Do not:<ul><li>install the update on hosted systems</li></ul></li></ul>",
    ),
    (
        "heading-html",
        "<ul><li>Do not:<h3>Hosted systems</h3><ul><li><p>install the update on hosted systems</p></li></ul></li></ul>",
    ),
    (
        "restart-html",
        "<ul><li>Do not:<ul><li>install the update on hosted systems</li><li>restart the service</li></ul></li></ul>",
    ),
    ("br-html", "<ul><li>Do not:<br>install the update on hosted systems.</li></ul>"),
    (
        "double-br-html",
        "<ul><li>Do not:<br><br>install the update on hosted systems.</li></ul>",
    ),
    (
        "spaced-br-html",
        "<ul><li>Do not:<br> \n<br>install the update on hosted systems.</li></ul>",
    ),
]


@pytest.mark.parametrize(
    "case,guidance", RECONCILED_GUIDANCE, ids=[row[0] for row in RECONCILED_GUIDANCE]
)
def test_reconciled_unsupported_form_preserves_all_previous_artifacts(
    monkeypatch, tmp_path, case, guidance
):
    previous = {
        "index.md": b"Previous validated report",
        "index.html": b"Previous site",
        "current-findings.json": b'{"previous":true}',
        ".sentryinsight-articles-fingerprint": b"previous-input-fingerprint",
    }
    for name, content in previous.items():
        (tmp_path / name).write_bytes(content)
    source = (
        f"<h2>{CVE}</h2><p>{CVE} exploitation status is unknown.</p>{guidance}"
        if case.endswith("html")
        else f"## {CVE}\n\n{CVE} exploitation status is unknown.\n\n{guidance}"
    )
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[article(source)],
        expect_model_call=False,
    )
    assert result["status"] == "failed", result
    assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
    assert all(
        (tmp_path / name).read_bytes() == content for name, content in previous.items()
    )


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
    supporting_restart = guidance == "Never restart the service during recovery."
    previous = {
        "index.md": b"Previous validated report",
        "index.html": b"Previous site",
        "current-findings.json": b'{"previous":true}',
    }
    if not supporting_restart:
        for name, content in previous.items():
            (tmp_path / name).write_bytes(content)
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[
            article(f"## {CVE}\n\n{CVE} exploitation status is unknown.\n\n{guidance}")
        ],
        expect_model_call=supporting_restart,
    )
    if supporting_restart:
        assert result["status"] == "completed", result
        report = (tmp_path / "index.md").read_text()
        assert guidance in report and "**Action**: none" in report
        return
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

"""Inventoried guidance roles: typed targets, attribution, purpose and reference."""

import pytest

from src.core.finding_evidence import collect_finding_details
from src.core.reporting import build_reporting_catalog
from test_composed_document_pipeline_contract import article
from test_finding_generation_pipeline import run_real_pipeline

GUIDANCE = [
    (
        'It also added that devices on unsupported versions of Example "will lose access to Example Update services and won\'t receive any updates as a result" and recommended "upgrading to a supported version of Example client or server."',
        "patch",
    ),
    (
        "Example advised IT administrators to identify all devices running older or unsupported Example versions before the Example Update certificate rotation in 2027.",
        "none",
    ),
    (
        '"And if you do need to act on older device populations, there\'s still time! Review, update, and plan upgrades for unsupported versions before the May 2027 or June 2027 certificate expiration dates," it added.',
        "none",
    ),
    (
        "Example recommends upgrading NX-OS releases to a fixed version, as can be identified through the vendor’s Software Checker tool.",
        "patch",
    ),
    (
        "The company recommends disabling FEATURE, API, or MPLS OAM features if not needed, to eliminate the attack vector.",
        "none",
    ),
    (
        "Example researchers recommend that users verify the repository’s owner. Furthermore, the source for installing AI skills and MCP servers should be official registries or vendor repositories.",
        "none",
    ),
    (
        '"Customers need to upgrade these Example instances to the recommended Example versions to address the vulnerability."',
        "patch",
    ),
]


@pytest.mark.parametrize("guidance,action", GUIDANCE)
def test_inventoried_complete_guidance_has_owned_relations_and_output(
    monkeypatch, tmp_path, guidance, action
):
    item = article(
        f"<h2>CVE-2026-1234</h2><p>CVE-2026-1234 exploitation status is unknown.</p><p>{guidance}</p>"
    )
    details = collect_finding_details(
        list(build_reporting_catalog([item]).values()), ["CVE-2026-1234"]
    )
    assert details.recommendation_blocks and all(
        not getattr(d, "ambiguous", False)
        for b in details.recommendation_blocks
        for d in b.directives
    )
    result = run_real_pipeline(monkeypatch, tmp_path / "index.md", articles=[item])
    assert result["status"] == "completed", result
    report = (tmp_path / "index.md").read_text()
    assert guidance in report and f"**Action**: {action}" in report


def test_adjacent_audience_reference_keeps_complete_primary_and_supporting_guidance(
    monkeypatch, tmp_path
):
    earlier = GUIDANCE[1][0]
    later = "They should also deploy monthly Example updates on all supported devices to keep them up to date and create an upgrade plan for unsupported devices before May and June 2027."
    item = article(
        f"<p>Exploitation status is unknown.</p><p>{earlier}</p><p>{later}</p>"
    )
    result = run_real_pipeline(monkeypatch, tmp_path / "index.md", articles=[item])
    assert result["status"] == "completed", result
    report = (tmp_path / "index.md").read_text()
    assert earlier in report and later in report and "**Action**: patch" in report


@pytest.mark.parametrize(
    "prefix",
    [
        "",
        "<p>Users should install the patch.</p><h2>Another story</h2>",
        "<p>Users should install the patch.</p><p>Unrelated context intervenes.</p>",
    ],
)
def test_missing_or_expired_audience_reference_preserves_all_artifacts(
    monkeypatch, tmp_path, prefix
):
    text = "They should install the patch."
    paths = [
        tmp_path / n
        for n in (
            "index.md",
            "index.html",
            "current-findings.json",
            ".sentryinsight-articles-fingerprint",
        )
    ]
    for p in paths:
        p.write_bytes(b"Prior validated artifact")
    result = run_real_pipeline(
        monkeypatch,
        paths[0],
        articles=[
            article(
                "<p>Exploitation status is unknown.</p>" + prefix + f"<p>{text}</p>"
            )
        ],
        expect_model_call=False,
    )
    assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
    assert all(p.read_bytes() == b"Prior validated artifact" for p in paths)


@pytest.mark.parametrize(
    "text",
    [
        "Example advised IT administrators to identify devices for an unclassified purpose.",
        "Example recommends disabling unclassified things if not needed.",
        "Example researchers recommend that users verify unclassified ownership.",
        "Users should install a patch as can be imagined through unknown assertions.",
    ],
)
def test_unknown_arguments_and_reporting_residuals_still_reject(
    monkeypatch, tmp_path, text
):
    paths = [
        tmp_path / n
        for n in (
            "index.md",
            "index.html",
            "current-findings.json",
            ".sentryinsight-articles-fingerprint",
        )
    ]
    for p in paths:
        p.write_bytes(b"Prior validated artifact")
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
    assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
    assert all(p.read_bytes() == b"Prior validated artifact" for p in paths)

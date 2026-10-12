"""Independently expected event/guidance families and atomic failure behavior."""

from dataclasses import asdict

import pytest

from src.core.report_artifact import parse_report_artifact
from src.services.article_content import extract_article_content
from test_finding_generation_pipeline import run_real_pipeline


def article(text):
    result = extract_article_content(
        f"<article>{text}</article>", "https://example.test/advisory"
    )
    return dict(
        title="Security report",
        source="Publisher",
        link="https://example.test/advisory",
        content=result.text,
        content_kind="article",
        source_blocks=[asdict(b) for b in result.blocks],
    )


EVENTS = [
    (
        "The research contest concluded, with researchers collecting $120,000 in rewards after exploiting 12 zero-day flaws.",
        "observed",
    ),
    (
        "In total, today security researchers exploited 12 zero-days for $120,000 in cash on the final day of the contest.",
        "observed",
    ),
    (
        "Analysis of these incidents shows that attackers are probing websites and APIs for access-control weaknesses, and exploiting known vulnerabilities.",
        "active",
    ),
    (
        "A file upload vulnerability has been weaponized to compromise three servers by adding a new account, using it to upload web shells, and ultimately stealing payment data.",
        "observed",
    ),
    (
        "The exposed infrastructure contained 17 named post-exploitation tools, including credential-dumping scripts and file-transfer tooling.",
        "unknown",
    ),
    (
        "The agent maps unfamiliar login surfaces, discovers security weaknesses, and generates purpose-built automation to exploit them.",
        "unknown",
    ),
    (
        "The competition identifies zero-day flaws before attackers exploit them in the wild.",
        "unknown",
    ),
    (
        "During the first breach, the attacker drained $1.4 million by exploiting a flaw in its smart contract code to issue withdrawal commands, which forced the exchange to pay rewards.",
        "observed",
    ),
    (
        "Three weeks later, the attacker hit the exchange again, exploiting a separate coding error that allowed him to withdraw its assets.",
        "observed",
    ),
]


@pytest.mark.parametrize("text,status", EVENTS)
def test_composed_events_survive_real_compile_render_validation(
    monkeypatch, tmp_path, text, status
):
    result = run_real_pipeline(
        monkeypatch, tmp_path / "index.md", articles=[article(f"<p>{text}</p>")]
    )
    assert result["status"] == "completed", result
    (finding,) = parse_report_artifact((tmp_path / "index.md").read_text()).findings
    assert finding.exploitation_status.value == status
    assert text in (tmp_path / "index.md").read_text()


# Full targets/purposes are semantic requirements, not a verb-to-badge list.
GUIDANCE = [
    (
        "To ensure devices keep receiving updates, admins and users must upgrade to a supported version of Example OS before the certificates expire in May 2027.",
        "patch",
    ),
    (
        "Vendors must patch zero-days disclosed during the research competition within 90 days before researchers publicly share details.",
        "patch",
    ),
    (
        "If malware execution is suspected, users should treat the incident as a potential account compromise, revoke active sessions and access tokens, and move to passkeys.",
        "none",
    ),
    (
        "Users who have installed the extensions and entered a recovery phrase into the fake interfaces should assume compromise, create a new wallet from a clean system, and move their assets.",
        "none",
    ),
    (
        "To counter the threat associated with malicious extensions, users are advised to review the browser extensions installed in their environment, and remove those that are no longer needed.",
        "none",
    ),
    (
        "Organizations are recommended to audit extensions within managed environments, adopt runtime monitoring approaches, and deploy extension monitoring technologies to detect suspicious activity.",
        "none",
    ),
    ("Revoke all active user sessions.", "none"),
    ("Review API keys and delete any you do not recognize.", "none"),
    ("Review administrator accounts for unexpected changes.", "none"),
    ("Rotate the credentials for every connected database.", "none"),
    ("Review data warehouse logs for signs of unauthorized access.", "investigate"),
    (
        "Turn off unused services and ports, such as remote access and file sharing.",
        "none",
    ),
    ("Sanitize user input in web applications to block XSS.", "none"),
    ("Require multifactor authentication, especially for webmail and VPNs.", "none"),
    ("Watch for unexpected directory replication.", "none"),
    (
        "Check cloud accounts for connected applications that can read files and email.",
        "none",
    ),
    ("Replace products that no longer get updates.", "none"),
]


@pytest.mark.parametrize("text,action", GUIDANCE)
def test_complete_typed_guidance_survives_real_pipeline(
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
    (finding,) = parse_report_artifact((tmp_path / "index.md").read_text()).findings
    assert finding.action.value == action
    assert text in finding.recommended_actions


@pytest.mark.parametrize(
    "text",
    [
        "The vendor seemingly verifies that attackers have almost begun unclassified exploitation of CVE-2026-1234.",
        "The vendor has not found evidence that attackers are exploiting CVE-2026-1234, and reports conclusively warrant another interpretation.",
        "Users should revoke mystery artifacts.",
        "Users should rotate the credentials unpredictably.",
        "Unknown audiences claim that users should create a new wallet.",
    ],
)
def test_unknown_required_relations_stop_before_transport_and_preserve_artifacts(
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
        path.write_bytes(b"Previously validated bytes\n")
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
    assert result["status"] == "failed"
    assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
    assert all(path.read_bytes() == b"Previously validated bytes\n" for path in paths)

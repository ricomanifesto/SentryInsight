"""Required capability qualifications cannot depend on optional plan excerpts."""

import pytest

from src.core.assertions import parse_assertions
from src.core.finding_evidence import EvidenceError, validate_finding_evidence
from src.core.finding_generation import _finding, compile_finding_records
from src.core.reporting import build_reporting_catalog
from test_composed_document_pipeline_contract import article
from test_document_capability_observation import body, CVE, OTHER
from test_finding_generation_pipeline import run_real_pipeline

QUALIFICATIONS = [
    f"Leveraging the {CVE} flaw also requires either Segment Routing over IPv6 (SRv6) or Network Virtualization (NV) Overlay to be enabled.",
    '"NV Overlay also requires a VXLAN Ethernet VPN (EVPN) VXLAN Network Identifier (VNI) mapped to a Network Virtualization Endpoint (NVE) interface with at least one peer VXLAN Tunnel Endpoint (VTEP) learned (for example, BGP EVPN or an ingress-replication static peer)," reads Example\'s advisory.',
    f"In the case of {CVE}, MPLS OAM must be explicitly activated, as it is disabled by default. Example 9000 switches with Silicon One ASICs do not support the feature and are unaffected by this flaw.",
    "Example also provides temporary Live Protect shields for all two flaws, which is a protection system for switches that cannot yet be upgraded and rebooted.",
    f"{CVE}: Insufficient input validation; it can be exploited through a crafted HTTP request sent to the Example API, a feature that is disabled by default.",
]


@pytest.mark.parametrize("text", QUALIFICATIONS)
def test_complete_qualified_context_is_mandatory_and_does_not_change_observation(
    monkeypatch, tmp_path, text
):
    item = article(body(text))
    catalog = build_reporting_catalog([item])
    (record,) = compile_finding_records(catalog, [CVE, OTHER])
    fields = dict(record.fields)
    assert text in fields["Source Constraints"]
    assert fields["Exploitation Status"] == "not_observed"
    report = "## Active Exploitation Details\n\n" + _finding(record)
    validate_finding_evidence(report, catalog)
    with pytest.raises(EvidenceError) as caught:
        validate_finding_evidence(report.replace(text, text[:-2]), catalog)
    assert caught.value.code == "source_constraints_not_grounded"
    result = run_real_pipeline(monkeypatch, tmp_path / "index.md", articles=[item])
    assert result["status"] == "completed", result
    rendered = (tmp_path / "index.md").read_text()
    assert text in next(
        line for line in rendered.splitlines() if "**Source Constraints**:" in line
    )


@pytest.mark.parametrize("text", QUALIFICATIONS[:4])
def test_unknown_required_qualification_residual_cannot_disappear(
    monkeypatch, tmp_path, text
):
    # Add an independent unclassified relation within the recognized family.
    changed = text[:-1] + " and unspecified assumptions apply."
    names = (
        "index.md",
        "index.html",
        "current-findings.json",
        ".sentryinsight-articles-fingerprint",
    )
    for name in names:
        (tmp_path / name).write_bytes(b"Previous validated artifact")
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[article(body(changed))],
        expect_model_call=False,
    )
    assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
    assert all(
        (tmp_path / name).read_bytes() == b"Previous validated artifact"
        for name in names
    )


def test_other_explicit_cve_requirement_does_not_inherit_the_group():
    text = QUALIFICATIONS[0].replace(CVE, "CVE-2026-9999")
    catalog = build_reporting_catalog([article(body(text))])
    from src.core.finding_evidence import (
        collect_finding_details,
        source_constraint_text,
    )

    details = collect_finding_details(list(catalog.values()), [CVE, OTHER])
    assert text not in source_constraint_text(details)


@pytest.mark.parametrize("text", QUALIFICATIONS[:2])
def test_feature_requirement_is_context_not_current_or_historical_activity(text):
    clauses = parse_assertions(text)
    assert clauses and all(
        c.kind == "context" and c.modal == "capability" and not c.unsupported
        for c in clauses
    )
    assert all(c.assertion_status is None for c in clauses)


@pytest.mark.parametrize(
    "text",
    [
        QUALIFICATIONS[0].replace("requires either", "does not require either"),
        QUALIFICATIONS[1].replace("also requires a", "also does not require a"),
        QUALIFICATIONS[2].replace("must be explicitly", "must not be explicitly"),
    ],
)
def test_negative_requirement_retains_polarity_and_complete_source(
    monkeypatch, tmp_path, text
):
    clauses = parse_assertions(text)
    assert all(c.polarity == "negative" for c in clauses)
    test_complete_qualified_context_is_mandatory_and_does_not_change_observation(
        monkeypatch, tmp_path, text
    )

"""Offline contracts for explicit uncertainty, never inferred absence."""

import hashlib

import pytest

from src.core.finding_evidence import ABSENT, EvidenceError, validate_finding_evidence
from src.core.reporting import build_reporting_catalog, resolve_reporting_keys
from src.core.version_references import (
    build_version_reference_context,
    resolve_version_references,
)
from src.core.report_artifact import ReportArtifactError, parse_report_artifact
from test_version_references import source

UNRESOLVED = "Unresolved from supplied sources."
NARRATIVE = (
    "When investigators disrupted the Moonbot 3.1 botnet in July 2025, "
    "the more than 12 million devices involved were uncertified."
)


def raw_report(keys, value):
    return f"""# Exploitation Report

## Executive Summary

The supplied reporting describes a campaign. Exploitation status is unknown.

Review the source details before choosing a response.

## Active Exploitation Details

### Synthetic campaign
- **Description**: A campaign described by the supplied reporting.
- **Severity**: unknown
- **Exploitation Status**: unknown
- **Action**: monitor
- **Reporting**: {', '.join(keys)}
- **Affected Versions**: {value}
- **Exceptions**: {ABSENT}
- **Recommended Actions**: {ABSENT}
- **Vendor Links**: {ABSENT}

## Affected Systems and Products

- Review the reporting for system details.

## Attack Vectors and Techniques

- Review the reporting for technique details.

## Threat Actor Activities

- The reported campaign requires further investigation.
- Review the supplied reporting before assigning an actor.
"""


def artifact_text(report, catalog, version=4):
    return (
        f"---\nschema_version: {version}\nreport_date: 2026-11-02\n"
        "generated_at: 2026-11-02T12:00:00Z\n"
        "digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-11-02/\n"
        "---\n" + resolve_reporting_keys(report, catalog)
    )


def unresolved_catalog():
    return build_reporting_catalog([source(NARRATIVE)])


def unresolved_refs(catalog):
    return [
        ref
        for scope in build_version_reference_context(catalog)
        for ref in scope["unresolved_references"]
    ]


def test_uncertainty_requires_a_source_bound_reference_and_remains_explicit():
    catalog = unresolved_catalog()
    [scope] = build_version_reference_context(catalog)
    assert scope["state"] == "unresolved"
    assert scope["absence_allowed"] is False
    assert scope["unresolved_allowed"] is True
    [ref] = scope["unresolved_references"]
    assert ref["source_key"] in catalog
    assert ref["content_sha256"] == hashlib.sha256(NARRATIVE.encode()).hexdigest()
    assert ref["span_sha256"] == hashlib.sha256(NARRATIVE.encode()).hexdigest()
    assert ref["reason"] == "unclassified_numeric_prose"
    rendered = resolve_version_references(raw_report(catalog, ref["id"]), catalog)
    assert f"**Affected Versions**: {UNRESOLVED}" in rendered
    assert "**Affected Versions Status**: unresolved" in rendered
    assert ref["id"] not in rendered
    validate_finding_evidence(rendered, catalog)
    artifact = parse_report_artifact(artifact_text(rendered, catalog))
    assert artifact.schema_version == 4
    assert artifact.findings[0].affected_versions_status.value == "unresolved"


@pytest.mark.parametrize(
    "value", [ABSENT, UNRESOLVED, "Unknown", "Not applicable.", "Gateway 3.1"]
)
def test_unresolved_source_never_authorizes_absence_or_free_text(value):
    catalog = unresolved_catalog()
    with pytest.raises(EvidenceError):
        resolve_version_references(raw_report(catalog, value), catalog)


@pytest.mark.parametrize(
    "content",
    [
        "CVE-2026-1234 is described.\n\n" + NARRATIVE,
        NARRATIVE + "\n\nAffected versions: Gateway 7 (Windows only)",
        NARRATIVE + "\n\nAffected versions:",
        NARRATIVE + "\n\nGateway 7 is vulnerable.",
        NARRATIVE + "\n\nUsers of Gateway 7 are affected.",
        NARRATIVE + "\n\nAffected versions: users of Gateway 7 are not affected",
        NARRATIVE
        + "\n\nAffected versions: Gateway 7\n\nAffected versions: users of Gateway 7 are not affected",
        NARRATIVE + "\n\nGateway 8.1",
    ],
)
def test_hard_evidence_failures_do_not_offer_an_unresolved_fallback(content):
    catalog = build_reporting_catalog([source(content)])
    assert all(
        not s["unresolved_allowed"] for s in build_version_reference_context(catalog)
    )
    ref = unresolved_refs(unresolved_catalog())[0]["id"]
    with pytest.raises(EvidenceError):
        resolve_version_references(raw_report(catalog, ref), catalog)


def test_stale_uncited_forged_duplicate_and_partial_uncertainty_refs_fail():
    original = unresolved_catalog()
    [reference] = unresolved_refs(original)
    changed = build_reporting_catalog([source(NARRATIVE + "\nA later note.")])
    with pytest.raises(EvidenceError):
        resolve_version_references(raw_report(changed, reference["id"]), changed)
    both = build_reporting_catalog([source(NARRATIVE), source(NARRATIVE, "two")])
    refs = unresolved_refs(both)
    for values in [
        reference["id"],
        reference["id"] + "; " + reference["id"],
        "unresolved-version-" + "a" * 32,
    ]:
        with pytest.raises(EvidenceError):
            resolve_version_references(raw_report(both, values), both)
    with pytest.raises(EvidenceError):
        resolve_version_references(raw_report([list(both)[0]], refs[1]["id"]), both)
    rendered = resolve_version_references(
        raw_report(both, "; ".join(r["id"] for r in refs)), both
    )
    validate_finding_evidence(rendered, both)


def test_host_state_cannot_be_supplied_or_forged_in_canonical_output():
    catalog = unresolved_catalog()
    ref = unresolved_refs(catalog)[0]["id"]
    raw = raw_report(catalog, ref)
    with pytest.raises(EvidenceError):
        resolve_version_references(
            raw.replace(ref, ref + "\n- **Affected Versions Status**: unresolved"),
            catalog,
        )
    rendered = resolve_version_references(raw, catalog)
    for forged in [
        rendered.replace(UNRESOLVED, ABSENT),
        rendered.replace("Status**: unresolved", "Status**: not_stated"),
    ]:
        with pytest.raises(EvidenceError):
            validate_finding_evidence(forged, catalog)
    unrelated = build_reporting_catalog([source("A campaign was reported.")])
    with pytest.raises(EvidenceError):
        validate_finding_evidence(rendered, unrelated)


def test_schema_four_requires_state_and_keeps_legacy_contract_distinct():
    catalog = unresolved_catalog()
    ref = unresolved_refs(catalog)[0]["id"]
    rendered = resolve_version_references(raw_report(catalog, ref), catalog)
    with pytest.raises(ReportArtifactError):
        parse_report_artifact(artifact_text(rendered, catalog, version=3))
    with pytest.raises(ReportArtifactError):
        parse_report_artifact(
            artifact_text(
                rendered.replace("- **Affected Versions Status**: unresolved\n", ""),
                catalog,
            )
        )
    with pytest.raises(ReportArtifactError):
        parse_report_artifact(
            artifact_text(rendered.replace(UNRESOLVED, ABSENT), catalog)
        )


def test_new_state_is_visible_in_rendering_and_embedded_metadata(tmp_path):
    import json
    import re
    from test_site_builder import build_fixture

    catalog = unresolved_catalog()
    ref = unresolved_refs(catalog)[0]["id"]
    rendered = resolve_version_references(raw_report(catalog, ref), catalog)
    root = build_fixture(tmp_path, artifact_text(rendered, catalog))
    html = (root / "index.html").read_text()
    assert "Affected versions unresolved" in html
    assert "Review the linked reporting" in html
    assert "1 finding has unresolved affected-version evidence" in html
    assert "https://example.test/one" in html
    metadata = json.loads(
        re.search(
            r'<script id="report-metadata" type="application/json">(.*?)</script>',
            html,
            re.S,
        )[1]
    )
    assert metadata["schema_version"] == 4
    assert metadata["unresolved_version_count"] == 1
    assert metadata["findings"][0]["affected_versions_status"] == "unresolved"


@pytest.mark.parametrize(
    "content",
    [
        "Android 8.1 botnet infections were confirmed on televisions running that operating system.",
        "The Android 8.1 botnet comprises televisions running that operating system.",
        "The Gateway firmware shipped with the Moonbot 3.1 botnet in July 2025 is targeted.",
        "Gateway firmware released in July 2025 is targeted.",
    ],
)
def test_ambiguous_names_and_dates_never_become_absence(content):
    catalog = build_reporting_catalog([source(content)])
    [scope] = build_version_reference_context(catalog)
    assert scope["absence_allowed"] is False
    with pytest.raises(EvidenceError):
        resolve_version_references(raw_report(catalog, ABSENT), catalog)
    if scope["unresolved_allowed"]:
        refs = "; ".join(ref["id"] for ref in scope["unresolved_references"])
        rendered = resolve_version_references(raw_report(catalog, refs), catalog)
        assert f"**Affected Versions**: {UNRESOLVED}" in rendered
        validate_finding_evidence(rendered, catalog)
    else:
        assert scope["blocked"] is True


@pytest.mark.parametrize(
    "old,new",
    [
        ("Status**: unknown", "Status**: active"),
        (f"Exceptions**: {ABSENT}", "Exceptions**: Gateway 2.0 is unaffected"),
        (f"Recommended Actions**: {ABSENT}", "Recommended Actions**: Upgrade Gateway"),
        (
            f"Vendor Links**: {ABSENT}",
            "Vendor Links**: https://vendor.example/advisory",
        ),
        ("### Synthetic campaign", "### Synthetic campaign CVE-2026-1234"),
    ],
)
def test_unresolved_state_does_not_bypass_other_evidence_checks(old, new):
    catalog = unresolved_catalog()
    ref = unresolved_refs(catalog)[0]["id"]
    rendered = resolve_version_references(raw_report(catalog, ref), catalog)
    with pytest.raises(EvidenceError):
        validate_finding_evidence(rendered.replace(old, new), catalog)


@pytest.mark.parametrize(
    "content",
    [
        "Gateway 8.1 (users who are administrators)",
        "Gateway 8.1; Gateway 8.2 (users who are administrators)",
        "Gateway 8.1 (May 2025)",
        "Gateway 8.1 (June 2025)",
        "Gateway 8.1; Gateway 8.2 (May 2025)",
        "Gateway 8.1, and older (May 2025)",
        "Gateway 8.1 May 2025",
        "Gateway 8.1 June 2025",
        "Gateway 8.1 [users who are administrators (May 2025)]",
        "Gateway 8.1 for users who are administrators",
        "Gateway 8.1 that is installed on televisions",
        "Gateway 8.1 (users who are administrators]",
        "Gateway 8.1; devices were uncertified.",
        "Gateway 8.1; 12 devices were uncertified.",
        "Gateway 8.1; devices were uncertified in July 2025.",
        "Gateway 8.1 where administrators are present",
        "Gateway 8.1 when administrators are present",
        "Gateway 8.1 if administrators are present",
        "Gateway 8.1, 12 devices were uncertified.",
        "Gateway 8.1 and 12 devices were uncertified.",
        "Gateway 8.1 or 12 devices were uncertified.",
        "Gateway 8.1 | 12 devices were uncertified.",
        "Gateway 8.1 — 12 devices were uncertified.",
        "Gateway 8.1: 12 devices were uncertified.",
        "When investigators disrupted Moonbot 3.1, Gateway 8.1, 12 devices were uncertified.",
    ],
)
def test_release_rows_and_qualifiers_cannot_establish_unresolved_prose(content):
    catalog = build_reporting_catalog([source(content)])
    [scope] = build_version_reference_context(catalog)
    assert scope["blocked"] is True
    assert scope["unresolved_allowed"] is False
    assert scope["absence_allowed"] is False
    for value in (ABSENT, "unresolved-version-" + "a" * 32):
        with pytest.raises(EvidenceError):
            resolve_version_references(raw_report(catalog, value), catalog)

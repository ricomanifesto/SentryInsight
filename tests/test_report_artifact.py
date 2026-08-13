from __future__ import annotations

import pytest

from src.core.report_artifact import (
    Action,
    ExploitationStatus,
    ReportArtifactError,
    Severity,
    parse_report_artifact,
)

REPORT = """---
schema_version: 1
report_date: 2026-08-13
generated_at: 2026-08-13T13:21:22Z
---
# Exploitation Report

## Executive Summary

Attackers are exploiting an exposed service.

## Active Exploitation Details

### Example vulnerability (CVE-2026-1234)
- **Description**: Attackers can execute code remotely.
- **Impact**: Full service compromise.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-1234, CVE-2026-12345678

### Vulnerability without an assigned CVE
- **Description**: A public proof of concept bypasses a local control.
- **Impact**: Local privilege escalation.
- **Severity**: high
- **Exploitation Status**: potential
- **Action**: investigate

## Affected Systems and Products

- **Example Product**: Supported versions are affected.

## Attack Vectors and Techniques

- **Crafted request**: Attackers send a request to the exposed service.

## Threat Actor Activities

- **Unknown actor**: Opportunistic exploitation.
"""


def test_parse_report_artifact_owns_date_and_structured_finding_metadata():
    artifact = parse_report_artifact(REPORT)

    assert artifact.schema_version == 1
    assert artifact.report_date.isoformat() == "2026-08-13"
    assert artifact.generated_at.isoformat() == "2026-08-13T13:21:22+00:00"
    assert artifact.body.startswith("# Exploitation Report")
    assert len(artifact.findings) == 2

    finding = artifact.findings[0]
    assert finding.title == "Example vulnerability (CVE-2026-1234)"
    assert finding.slug == "example-vulnerability-cve-2026-1234"
    assert finding.severity is Severity.CRITICAL
    assert finding.exploitation_status is ExploitationStatus.ACTIVE
    assert finding.action is Action.PATCH
    assert finding.cve_ids == ("CVE-2026-1234", "CVE-2026-12345678")

    no_cve_finding = artifact.findings[1]
    assert no_cve_finding.cve_ids == ()
    assert no_cve_finding.severity is Severity.HIGH
    assert no_cve_finding.exploitation_status is ExploitationStatus.POTENTIAL
    assert no_cve_finding.action is Action.INVESTIGATE


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("Severity", "urgent"),
        ("Exploitation Status", "probably active"),
        ("Action", "patch immediately"),
    ],
)
def test_parse_report_artifact_rejects_unknown_triage_values(field, value):
    malformed = REPORT.replace(f"**{field}**: critical", f"**{field}**: {value}")
    if malformed == REPORT:
        malformed = REPORT.replace(f"**{field}**: active", f"**{field}**: {value}")
    if malformed == REPORT:
        malformed = REPORT.replace(f"**{field}**: patch", f"**{field}**: {value}")

    with pytest.raises(ReportArtifactError, match=field):
        parse_report_artifact(malformed)


@pytest.mark.parametrize(
    "cve_field",
    [
        "CVE-2026-593...",
        "CVE-2026-593…",
        "CVE ID assigned but not specified in source article",
        "Not yet assigned / CVE pending",
        "CVE-2026-123",
    ],
)
def test_parse_report_artifact_rejects_partial_or_placeholder_cve_fields(cve_field):
    malformed = REPORT.replace(
        "CVE-2026-1234, CVE-2026-12345678",
        cve_field,
    )

    with pytest.raises(ReportArtifactError, match="CVE IDs"):
        parse_report_artifact(malformed)


def test_parse_report_artifact_accepts_official_variable_length_cve_ids():
    artifact = parse_report_artifact(
        REPORT.replace("CVE-2026-12345678", "CVE-2026-123456789")
    )

    assert artifact.findings[0].cve_ids[-1] == "CVE-2026-123456789"


@pytest.mark.parametrize(
    "partial",
    ["CVE-2026-", "CVE-2026-593...", "CVE-2026-593…", "CVE-2026-593"],
)
def test_parse_report_artifact_rejects_partial_cves_outside_cve_fields(partial):
    malformed = REPORT.replace(
        "Example vulnerability (CVE-2026-1234)",
        f"Example vulnerability ({partial})",
    )

    with pytest.raises(ReportArtifactError, match="partial CVE"):
        parse_report_artifact(malformed)


@pytest.mark.parametrize("field", ["Severity", "Exploitation Status", "Action"])
def test_parse_report_artifact_requires_each_triage_dimension(field):
    lines = [line for line in REPORT.splitlines() if f"**{field}**:" not in line]

    with pytest.raises(ReportArtifactError, match=field):
        parse_report_artifact("\n".join(lines))


@pytest.mark.parametrize("metadata", ["report_date", "generated_at"])
def test_parse_report_artifact_requires_explicit_time_metadata(metadata):
    malformed = "\n".join(
        line for line in REPORT.splitlines() if not line.startswith(f"{metadata}:")
    )

    with pytest.raises(ReportArtifactError, match=metadata):
        parse_report_artifact(malformed)

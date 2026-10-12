"""Heading-bound rollups cannot borrow a different finding's identity/state."""

import pytest

from src.core.finding_evidence import EvidenceError, validate_finding_evidence
from test_finding_generation import catalog_for, render


@pytest.mark.parametrize(
    "claim",
    [
        "CVE-2026-5678 is actively exploited.",
        "CVE-2026-5678 was exploited yesterday.",
    ],
)
def test_active_owner_cannot_license_a_foreign_unknown_rollup_claim(claim):
    catalog = catalog_for(
        "CVE-2026-1234 is actively exploited.",
        "CVE-2026-5678 exploitation status is unknown.",
    )
    records, report = render(catalog)
    validate_finding_evidence(report, catalog)
    damaged = report + "\n- **CVE-2026-1234**: " + claim + "\n"
    with pytest.raises(EvidenceError):
        validate_finding_evidence(damaged, catalog)


def test_owned_negative_row_cannot_be_promoted_by_an_active_heading():
    catalog = catalog_for(
        "CVE-2026-1234 is actively exploited.",
        "CVE-2026-5678 exploitation has not been observed.",
    )
    _, report = render(catalog)
    damaged = report + "\n- **CVE-2026-5678**: CVE-2026-5678 is actively exploited.\n"
    with pytest.raises(EvidenceError):
        validate_finding_evidence(damaged, catalog)

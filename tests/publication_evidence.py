"""Capture actual pre-resolution output for meaningful publication mutations."""

from src.core import finding_generation
from src.core.finding_evidence import validate_finding_evidence
from src.core.report_validation import (
    remove_source_attribution_section,
    split_overlong_executive_summary,
)
from src.core.reporting import resolve_reporting_keys


def capture_generated_evidence(monkeypatch):
    captured = []

    def validate(report, catalog):
        result = validate_finding_evidence(report, catalog)
        if report.startswith("# Exploitation Report\n"):
            captured.append((report, catalog))
        return result

    monkeypatch.setattr(finding_generation, "validate_finding_evidence", validate)

    def published_baseline(published, expected_catalog):
        assert len(captured) == 1
        generated, catalog = captured[0]
        assert catalog == expected_catalog
        baseline = split_overlong_executive_summary(
            remove_source_attribution_section(generated)
        )
        # Validate the actual generated source-key input, not reconstructed
        # citations. Its resolved bytes must match the published report body.
        validate_finding_evidence(baseline, catalog)
        _, separator, body = published.partition("\n---\n")
        assert separator
        assert resolve_reporting_keys(baseline, catalog).lstrip() == body
        return baseline

    return published_baseline

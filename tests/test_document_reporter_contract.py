"""Finite reporting predicates own absence, time and explicit local references."""

import pytest

from src.core.finding_evidence import assess_exploitation, source_evidence_text
from test_source_document_contract import source


@pytest.mark.parametrize(
    "text",
    [
        '"As of the publication of the bulletin, Example is not aware of any unmitigated exploits of this vulnerability."',
        "There is no evidence that the issue has been exploited in the wild.",
    ],
)
def test_reporter_absence_resolves_local_reference_without_borrowing_older_cve(text):
    item = source(
        f"<article><p>Tracked as CVE-2026-1234, this flaw allows data access.</p><p>{text}</p><p>CVE-2026-5678 was exploited last year.</p></article>"
    )
    result = assess_exploitation([item], ["CVE-2026-1234"])
    assert result.status == "not_observed" and not result.unsupported
    assert text in source_evidence_text([item], ["CVE-2026-1234"])


def test_shared_research_discovery_does_not_supply_event_tense_to_reporter_absence():
    text = "All three vulnerabilities were discovered during internal security testing, and Example said it was unaware of public announcements or malicious exploitation at the time of publishing the advisories."
    item = source(
        "<article><p>All three vulnerabilities require a feature to be active:</p><ul><li>CVE-2026-1234: Gateway flaw.</li><li>CVE-2026-5678 and CVE-2026-9012: Gateway flaws.</li></ul><p>"
        + text
        + "</p></article>"
    )
    result = assess_exploitation(
        [item], ["CVE-2026-1234", "CVE-2026-5678", "CVE-2026-9012"]
    )
    assert result.status == "not_observed" and not result.unsupported
    assert text in source_evidence_text([item], ["CVE-2026-1234"])
    assert any(c.reporter and c.reporter.as_of for c in result.relations)


@pytest.mark.parametrize(
    "sentence",
    [
        "The vendor will not be aware of exploitation of CVE-2026-1234.",
        "The vendor is not aware of evidence seemingly claiming exploitation of CVE-2026-1234.",
        "The vendor is not aware of any unmitigated exploits of CVE-2026-1234, and unseen predicates warrant certainty.",
    ],
)
def test_unknown_reporting_operator_or_residual_stays_unsupported(sentence):
    item = source(f"<article><p>{sentence}</p></article>")
    assert assess_exploitation([item], ["CVE-2026-1234"]).unsupported

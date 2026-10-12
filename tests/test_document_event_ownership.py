"""The frozen composed families retain finite event and descriptive roles."""

import pytest

from src.core.assertions import parse_assertions
from src.core.finding_evidence import assess_exploitation
from test_source_document_contract import source


@pytest.mark.parametrize(
    "sentence,state",
    [
        (
            "The third pattern is exploitation of CVE-2026-1234, an SQL injection flaw in Example, an open-source BI tool that companies connect to their databases.",
            "unknown",
        ),
        (
            "Example said a third party exploited CVE-2026-1234 in its Gateway and had access from August 12 to September 7.",
            "observed",
        ),
        (
            "More recently, in September, it released security updates for two more actively exploited Gateway RCE zero-days (CVE-2026-1234 and CVE-2026-5678) that let attackers deploy custom web shells and tunneling malware, steal credentials, gain root access, and spread into victims' internal networks.",
            "observed",
        ),
    ],
)
def test_composed_event_cannot_borrow_current_tense_from_nominal_words(sentence, state):
    item = source(f"<article><p>{sentence}</p></article>")
    from src.core.cve import extract_cve_ids

    assessment = assess_exploitation([item], extract_cve_ids(sentence))
    assert assessment.status == state and not assessment.unsupported


@pytest.mark.parametrize(
    "text",
    [
        "CVE-2026-1234: Insufficient input validation; it can be exploited through a crafted HTTP request sent to the API, a feature that is disabled by default.",
        "CVE-2026-1234: Improper validation of MPLS echo-request packets allows exploitation through a crafted request sent to an affected device’s IP address.",
        "CVE-2026-1234, CVE-2026-5678, and CVE-2026-9012: Improper validation of IP traffic can be exploited through crafted packets sent to an IP interface; all three require Feature Mode to be enabled.",
    ],
)
def test_finite_capability_frames_are_context_not_activity(text):
    clauses = parse_assertions(text)
    assert clauses and not any(c.unsupported for c in clauses)
    assert all(c.kind == "context" and c.modal == "capability" for c in clauses)


@pytest.mark.parametrize(
    "sentence",
    [
        "Example will say a third party is exploiting CVE-2026-1234 in its Gateway and had access from August 12 to September 7.",
        "The third pattern is exploitation of CVE-2026-1234, and attackers will be exploiting it.",
        "CVE-2026-1234: Insufficient input validation; it can be exploited through an unclassified bridge and hidden predicates prove activity.",
    ],
)
def test_unconsumed_composition_remains_unsupported(sentence):
    assert any(c.unsupported for c in parse_assertions(sentence))


def test_reported_patch_capability_does_not_become_an_observed_event():
    sentence = "Earlier this month, Example issued emergency updates to address a Gateway denial-of-service zero-day flaw (CVE-2026-1234) that researchers and admins later said could also be exploited to gain remote code execution."
    parsed = parse_assertions(sentence)
    assert parsed and all(
        c.kind == "context" and c.modal == "capability" and not c.unsupported
        for c in parsed
    )


def test_named_catalog_membership_is_retained_context_not_current_exploitation():
    sentence = "The U.S. Cybersecurity and Infrastructure Security Agency (CISA) added CVE-2026-1234 to its Known Exploited Vulnerabilities catalog on August 11."
    item = source(f"<article><p>{sentence}</p></article>")
    result = assess_exploitation([item], ["CVE-2026-1234"])
    assert result.status == "unknown" and not result.unsupported


def test_rendered_complete_joint_identity_can_own_its_cardinality_reference():
    from src.core.finding_evidence import _rendered_statements

    text = "CVE-2026-1234, CVE-2026-5678, CVE-2026-9012\n\nAll three vulnerabilities were discovered during internal security testing, and Example said it was unaware of public announcements or malicious exploitation at the time of publishing the advisories."
    clauses = _rendered_statements(text)
    assert clauses and all(
        c.status == "not_observed" and not c.unsupported for c in clauses
    )
    assert all(
        set(c.cves) == {"CVE-2026-1234", "CVE-2026-5678", "CVE-2026-9012"}
        for c in clauses
    )

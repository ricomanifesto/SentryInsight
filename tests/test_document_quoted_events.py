"""Quoted events retain reporting operators and complete purpose/tool roles."""

import pytest

from src.core.finding_evidence import assess_exploitation
from test_source_document_contract import source


@pytest.mark.parametrize(
    "text,status",
    [
        ('"Attackers were exploiting CVE-2026-1234," the company says.', "observed"),
        (
            '"Attackers are not exploiting CVE-2026-1234," the company said.',
            "not_observed",
        ),
        ('"Attackers may be exploiting CVE-2026-1234," the company said.', "potential"),
    ],
)
def test_quoted_event_tense_and_polarity_do_not_come_from_reporting_operator(
    text, status
):
    item = source(f"<article><p>{text}</p></article>")
    result = assess_exploitation([item], ["CVE-2026-1234"])
    assert result.status == status and not result.unsupported
    assert any(clause.reporter for clause in result.relations)


@pytest.mark.parametrize(
    "text",
    [
        "These state-sponsored hackers continue to aggressively target and access networks and systems throughout the world in an effort to identify and steal files and otherwise exploit victims' vulnerabilities.",
        "A second Example Tech tool is ExampleTool, which allegedly enabled the exploitation of computer networks through spear-phishing attacks and the deployment of follow-on payloads.",
        "Malicious cyber actors are using automated scanning, alongside large-scale botnets and manual exploitation techniques to compromise and steal confidential data.",
    ],
)
def test_purpose_and_technique_relations_do_not_confirm_exploitation(text):
    item = source(f'<article><p>"{text.rstrip(".")}," the company said.</p></article>')
    result = assess_exploitation([item], [])
    assert result.status == "unknown" and not result.unsupported


def test_unknown_quote_attribution_cannot_be_discarded():
    item = source(
        '<article><p>"Attackers are exploiting CVE-2026-1234," unknown structures imply certainty.</p></article>'
    )
    assert assess_exploitation([item], ["CVE-2026-1234"]).unsupported


@pytest.mark.parametrize(
    "attribution",
    [
        "said U.S. Attorney Example Person for the Western District of Example",
        "the U.K. National Security Centre (NSC) said",
    ],
)
def test_complete_noun_attribution_keeps_initialisms_and_finite_operator(attribution):
    from src.core.source_document import reporting_envelope

    text = f'"Attackers were exploiting CVE-2026-1234," {attribution}.'
    envelope = reporting_envelope(text)
    assert envelope and envelope.body == "Attackers were exploiting CVE-2026-1234"
    result = assess_exploitation(
        [source(f"<article><p>{text}</p></article>")], ["CVE-2026-1234"]
    )
    assert result.status == "observed" and not result.unsupported
    assert text in result.positive

"""Source structure and composed evidence have one complete ownership boundary.

Expected meanings are fixed independently of the parser. These fixtures contain
synthetic products and identities; no retained publisher article is embedded.
"""

from dataclasses import asdict, replace

import pytest

from src.core.finding_evidence import assess_exploitation, source_evidence_text
from src.core.reporting import (
    build_reporting_catalog,
    deserialize_reporting_catalog,
    serialize_reporting_catalog,
)
from src.services.article_content import extract_article_content


def source(markup):
    extracted = extract_article_content(markup, "https://example.test/story")
    return next(
        iter(
            build_reporting_catalog(
                [
                    dict(
                        title="Security report",
                        source="Publisher",
                        link="https://example.test/story",
                        content=extracted.text,
                        content_kind="article",
                        source_blocks=[asdict(block) for block in extracted.blocks],
                    )
                ]
            ).values()
        )
    )


def test_dom_cells_keep_affected_and_fixed_roles_without_changing_text():
    markup = (
        "<article><p>The advisory lists flaws successfully exploited.</p>"
        "<table><tr><th>Flaw</th><th>Product</th><th>Affected Versions</th>"
        "<th>Fixed In</th></tr><tr><td>CVE-2026-1234</td><td>Gateway</td>"
        "<td>2.0 and earlier</td><td>2.1</td></tr></table></article>"
    )
    extracted = extract_article_content(markup, "https://example.test/story")
    assert extracted.text == (
        "The advisory lists flaws successfully exploited.\n\n"
        "FlawProductAffected VersionsFixed In\n\nCVE-2026-1234Gateway2.0 and earlier2.1"
    )
    rows = [block for block in extracted.blocks if block.kind == "table_row"]
    assert len(rows) == 2
    assert rows[0].cells == ("Flaw", "Product", "Affected Versions", "Fixed In")
    assert rows[1].cells == ("CVE-2026-1234", "Gateway", "2.0 and earlier", "2.1")
    assert rows[0].table == rows[1].table
    assert rows[0].header is True and rows[1].header is False
    assert all(extracted.text[b.start : b.end] == b.text for b in extracted.blocks)
    item = source(markup)
    assert deserialize_reporting_catalog(
        serialize_reporting_catalog({item.key: item})
    ) == {item.key: item}


@pytest.mark.parametrize(
    "field,value",
    [("start", 1), ("end", 1), ("text", "Replacement"), ("text_sha256", "0" * 64)],
)
def test_structure_cannot_outlive_its_source_bytes(field, value):
    item = source("<article><p>CVE-2026-1234 is actively exploited.</p></article>")
    records = serialize_reporting_catalog({item.key: item})
    records[0]["blocks"][0][field] = value
    with pytest.raises(ValueError):
        deserialize_reporting_catalog(records)


def test_related_headlines_remain_context_and_cannot_supply_activity():
    item = source(
        "<article><p>CVE-2026-1234 exploitation has not been observed.</p>"
        "<h3>Related Articles:</h3><p>CVE-2026-1234 is actively exploited.</p></article>"
    )
    assessment = assess_exploitation([item], ["CVE-2026-1234"])
    assert assessment.status == "not_observed" and not assessment.conflicting
    assert "is actively exploited" in item.content
    assert "is actively exploited" not in source_evidence_text(
        [item], ["CVE-2026-1234"]
    )


@pytest.mark.parametrize(
    "sentence,status",
    [
        (
            "The vendor has not found evidence that attackers have begun exploiting CVE-2026-1234 in the wild.",
            "not_observed",
        ),
        (
            "The vendor had not found evidence that attackers were exploiting CVE-2026-1234 at the time of publication.",
            "unknown",
        ),
        (
            "The vendor has found evidence that attackers were exploiting CVE-2026-1234 last year.",
            "observed",
        ),
        (
            "The vendor has found evidence that attackers are exploiting CVE-2026-1234 in the wild.",
            "active",
        ),
        (
            "It is unclear whether the vendor has found evidence that attackers are exploiting CVE-2026-1234.",
            "unknown",
        ),
        (
            "If reports are accurate, the vendor has not found evidence that attackers are exploiting CVE-2026-1234.",
            "unknown",
        ),
        (
            "The vendor denied that it has found evidence that attackers are exploiting CVE-2026-1234.",
            "unknown",
        ),
        (
            "The vendor has not found no evidence that attackers are exploiting CVE-2026-1234.",
            "unknown",
        ),
    ],
)
def test_reporter_operator_and_event_have_separate_owned_states(sentence, status):
    item = source(f"<article><p>{sentence}</p></article>")
    result = assess_exploitation([item], ["CVE-2026-1234"])
    assert result.status == status
    assert not result.unsupported
    assert sentence in source_evidence_text([item], ["CVE-2026-1234"])


def test_explicit_other_cve_contrast_does_not_inherit_reporter_absence():
    text = (
        "While the vendor has not found evidence that attackers have begun exploiting CVE-2026-1234 in the wild, "
        "attackers are exploiting CVE-2026-5678."
    )
    item = source(f"<article><p>{text}</p></article>")
    assert assess_exploitation([item], ["CVE-2026-1234"]).status == "not_observed"
    assert assess_exploitation([item], ["CVE-2026-5678"]).status == "active"
    assert text in source_evidence_text([item], ["CVE-2026-1234"])


@pytest.mark.parametrize("separator", ["-", " "])
def test_identity_owner_protects_complete_joint_list(separator):
    text = (
        "Three vulnerabilities in Gateway appliances "
        f"(CVE{separator}2026-1234, CVE{separator}2026-5678, and CVE{separator}2026-9012) "
        "have come under active exploitation in the wild."
    )
    item = source(f"<article><p>{text}</p></article>")
    result = assess_exploitation(
        [item], ["CVE-2026-1234", "CVE-2026-5678", "CVE-2026-9012"]
    )
    assert result.status == "observed" and not result.unsupported
    assert any(
        set(c.cves) == {"CVE-2026-1234", "CVE-2026-5678", "CVE-2026-9012"}
        for c in result.relations
    )


def test_quoted_possible_event_keeps_local_identity_and_modal():
    text = (
        "Separately, the vendor in September patched a modem flaw, CVE-2026-1234, "
        'that it said: "may be under limited, targeted exploitation."'
    )
    item = source(f"<article><p>{text}</p></article>")
    result = assess_exploitation([item], ["CVE-2026-1234"])
    assert result.status == "potential" and not result.unsupported
    assert text in source_evidence_text([item], ["CVE-2026-1234"])


def test_source_local_empty_scope_never_borrows_another_source_event():
    negative = source(
        "<article><p>The vendor has not found evidence that attackers are exploiting the appliance.</p></article>"
    )
    positive = replace(
        source("<article><p>Attackers are exploiting the appliance.</p></article>"),
        key="another",
        url="https://other.test/story",
    )
    assert assess_exploitation([negative], []).status == "not_observed"
    assert assess_exploitation([positive], []).status == "active"
    with pytest.raises(ValueError):
        assess_exploitation([negative, positive], [])

"""Literal patch provenance and complete, source-owned severity properties."""

import json
from pathlib import Path

import pytest

from src.core.finding_evidence import EvidenceError, recommendation_action
from src.core.finding_generation import compile_finding_records
from src.core.recommendations import parse_recommendation
from src.core.severity import rating_relation, project_ratings
from test_finding_generation import catalog_for

A = "CVE-2026-1234"
B = "CVE-2026-5678"
CASES = json.loads(
    (Path(__file__).parent / "fixtures/patch_severity_contract.json").read_text()
)


@pytest.mark.parametrize("row", CASES["patch"], ids=lambda r: r["id"])
def test_patch_contract(row):
    directive = parse_recommendation(row["text"])
    supported = bool(
        directive
        and not directive.ambiguous
        and not any(c.unsupported for c in directive.clauses)
    )
    assert supported == row["expected_supported"]
    if supported:
        assert recommendation_action([row["text"]]) == row["expected_action"]
        for clause in directive.clauses:
            target = clause.directive_frame.target_binding
            if not target or not target.direct:
                continue
            nominal = target.direct
            for member in nominal.members:
                literal = nominal.text[slice(*member.span)]
                if "vendor " in literal.lower():
                    assert member.role == "patch" and member.release is None
                    assert member.provenance.text.lower() == "vendor"
                    assert (
                        nominal.text[slice(*member.provenance.span)]
                        == member.provenance.text
                    )
                    assert nominal.text[slice(*member.head_span)].lower() in {
                        "patch",
                        "patches",
                        "update",
                        "updates",
                        "hotfix",
                        "hotfixes",
                        "fix",
                        "fixes",
                    }


@pytest.mark.parametrize("row", CASES["severity"], ids=lambda r: r["id"])
def test_severity_contract(row):
    text = row["text"]
    block = "Literal source prefix. " + text
    relation = rating_relation(
        text,
        source_url="https://example.test/rating",
        cves=row["scope"],
        source_block=block,
    )
    result = project_ratings([relation] if relation else [])
    assert result.value == row["expected_value"]
    assert (relation is not None) == row["expected_retained"]
    assert bool(relation and relation.complete) == row["expected_complete"]
    if relation:
        assert result.context == (text,)
        assert block[relation.start : relation.end] == text
        assert relation.source_url == "https://example.test/rating"
    if row["expected_complete"] and text.startswith(("CVE-", "The ")):
        prop = relation.property
        assert prop is not None
        assert text[slice(*prop.band_span)].lower() == result.value
        assert text[slice(*prop.finite_span)].lower() in {"is", "was", "are", "were"}
        subject = text[slice(*prop.subject_span)]
        if subject.startswith("The severity"):
            assert text[slice(*prop.property_span)] in {"severity", "severity rating"}
        else:
            assert prop.property_span is None
        assert set(relation.cves) == set(row["scope"])


@pytest.mark.parametrize("row", CASES["composition"], ids=lambda r: r["id"])
def test_compiled_patch_and_severity_ownership(row):
    records = compile_finding_records(
        catalog_for(*row["sources"]), row["required_cves"]
    )
    expected = row["expected"]
    fields = [dict(record.fields) for record in records]
    assert records
    if "severity" in expected:
        assert all(f["Severity"] == expected["severity"] for f in fields)
    if "severity_by_cve" in expected:
        assert {
            cve: dict(r.fields)["Severity"] for r in records for cve in r.cves
        } == expected["severity_by_cve"]
    if "severity_values" in expected:
        assert sorted(f["Severity"] for f in fields) == sorted(
            expected["severity_values"]
        )
    for text in expected.get("context_includes", []):
        assert any(text in f["Severity Context"] for f in fields)
    for text in expected.get("context_excludes", []):
        assert all(text not in f["Severity Context"] for f in fields)
    if "scope" in expected:
        assert len(records) == 1 and set(records[0].cves) == set(expected["scope"])
    if "action" in expected:
        assert all(f["Action"] == expected["action"] for f in fields)
    if "guidance" in expected:
        assert any(expected["guidance"] in f["Recommended Actions"] for f in fields)
    if "affected_versions" in expected:
        assert all(
            f["Affected Versions"] == expected["affected_versions"] for f in fields
        )
    if "vendor_links" in expected:
        assert all(not r.links for r in records)


@pytest.mark.parametrize(
    "rating,selected",
    [
        (f"{A} is critical.", True),
        ("The severity is high.", True),
        (f"{A} is medium.", False),
        (f"{A} is not critical.", False),
        ("The service is critical.", False),
        ("It is critical.", False),
    ],
)
def test_owned_property_uses_existing_impact_selection_policy(rating, selected):
    catalog = catalog_for(
        f"## {A}\n\n{A} allows remote code execution on the gateway.\n\n{rating}"
    )
    if selected:
        assert compile_finding_records(catalog, relevance=lambda text: False)
    else:
        with pytest.raises(EvidenceError) as failure:
            compile_finding_records(catalog, relevance=lambda text: False)
        assert failure.value.code == "empty_generation_evidence"


def test_foreign_property_cannot_supply_selection_severity():
    catalog = catalog_for(
        f"## {A}\n\n{A} allows remote code execution on the gateway.\n\n"
        f"## {B}\n\n{B} is critical."
    )
    with pytest.raises(EvidenceError) as failure:
        compile_finding_records(catalog, relevance=lambda text: False)
    assert failure.value.code == "empty_generation_evidence"

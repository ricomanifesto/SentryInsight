"""Frozen finite subject language and original-source participation ownership."""

import hashlib
import json
from pathlib import Path

import pytest

from src.core.assertions import parse_assertions
from src.core.cve import extract_cve_ids
from src.core.finding_evidence import (
    EvidenceError,
    assess_exploitation,
    owned_actor_blocks,
    source_assertions,
)
from src.core.finding_generation import compile_finding_records
from src.core.source_document import SourceDocument, SourceSpan, source_document
from test_finding_generation import catalog_for

FROZEN = json.loads(
    (Path(__file__).parent / "fixtures/actor_subject_contract.json").read_text()
)
A = "CVE-2026-1234"


def test_legacy_role_lexicon_is_byte_identical():
    source = Path("src/core/finding_generation.py").read_text()
    literal = source.split("EXCERPT_ROLES = ", 1)[1].split(
        "\n\n\ndef _excerpt_roles", 1
    )[0]
    assert (
        hashlib.sha256(literal.encode()).hexdigest()
        == FROZEN["legacy_role_source_sha256"]
    )


@pytest.mark.parametrize("subject", FROZEN["old_subject_forms"])
def test_old_subject_forms_keep_their_owned_meaning(subject):
    (clause,) = parse_assertions(f"{subject} are actively exploiting {A}.")
    assert not clause.unsupported and clause.status == "active"
    assert clause.subject == subject and clause.cves == (A,)


@pytest.mark.parametrize("case", FROZEN["cases"], ids=lambda c: c["id"])
def test_frozen_lexical_semantics_and_complete_source(case):
    expected = case["expected"]
    texts = case.get("sources", [case["text"]])
    catalog = catalog_for(*texts)
    sources = tuple(catalog.values())
    clauses = [clause for source in sources for clause in source_assertions(source)]
    if expected.get("unsupported"):
        with pytest.raises(EvidenceError) as error:
            compile_finding_records(catalog)
        assert error.value.code == expected["error"]
        assert all(
            clause.actor_participation is None
            for clause in clauses
            if clause.unsupported
        )
        return
    assert not any(clause.unsupported for clause in clauses)
    for cve, status in {
        **expected.get("states", {}),
        **expected.get("independent_states", {}),
        **expected.get("singleton_statuses", {}),
    }.items():
        assessment = assess_exploitation(sources, [cve])
        assert assessment.status == status and not assessment.unsupported
    if "joint_cves" in expected:
        assessment = assess_exploitation(sources, expected["joint_cves"])
        assert (
            assessment.status == expected["joint_status"] and not assessment.unsupported
        )
    if "status" in expected:
        scope = expected.get(
            "cves", [A] if any(extract_cve_ids(text) for text in texts) else []
        )
        assessment = assess_exploitation(sources, scope)
        assert assessment.status == expected["status"] and not assessment.unsupported
    if "subject" in expected:
        assert any(clause.subject == expected["subject"] for clause in clauses)
    if "agent" in expected:
        assert any(
            clause.actor_participation
            and clause.actor_participation.role == "agent"
            and clause.actor_participation.binding.text == expected["agent"]
            for clause in clauses
        )
    if expected.get("reporter_negative"):
        assert any(
            clause.reporter and clause.reporter.polarity == "negative"
            for clause in clauses
        )
    if "reporter" in expected:
        assert any(
            clause.reporter and clause.reporter.subject == expected["reporter"]
            for clause in clauses
        )
    if (
        expected.get("actor_participation") is False
        or expected.get("actor_exploitation_participation") is False
    ):
        assert not any(clause.actor_participation for clause in clauses)
    if expected.get("required_finding") is False:
        return
    records = compile_finding_records(catalog)
    if "source_only_findings" in expected:
        assert len(records) == expected["source_only_findings"]
        assert [record.status for record in records] == expected["statuses"]
        assert all(not record.cves for record in records)
    if "action" in expected:
        assert all(
            dict(record.fields)["Action"] == expected["action"] for record in records
        )
    if "severity" in expected:
        assert all(
            dict(record.fields)["Severity"] == expected["severity"]
            for record in records
        )
    if expected.get("actor_rollup"):
        excerpts = [excerpt for record in records for excerpt in record.excerpts]
        if expected["actor_rollup"] is True:
            assert excerpts
        assert all("actors" in excerpt.roles for excerpt in excerpts)
        assert all(excerpt.text in texts for excerpt in excerpts)


def typed_sources(case, monkeypatch):
    catalog = catalog_for(*(source["text"] for source in case["sources"]))
    aliases = dict(zip((source["id"] for source in case["sources"]), catalog.values()))
    documents = {}
    for item in case["sources"]:
        if "document_context" not in item and "span_role" not in item:
            continue
        context = item.get("document_context", {})
        text = item["text"]
        documents[aliases[item["id"]].key] = SourceDocument(
            text,
            (
                SourceSpan(
                    0,
                    len(text),
                    text,
                    role=item.get("span_role", "body"),
                    section=tuple(context.get("section_cves", ())),
                    reference=tuple(context.get("reference_cves", ())),
                    reference_kind=context.get("reference_kind", ""),
                    reference_valid=context.get("reference_valid", True),
                ),
            ),
        )

    def document_for(source):
        key = getattr(source, "key", None)
        return documents[key] if key in documents else source_document(source)

    monkeypatch.setattr("src.core.finding_evidence.source_document", document_for)
    monkeypatch.setattr("src.core.finding_generation.source_document", document_for)
    return catalog, aliases


@pytest.mark.parametrize("case", FROZEN["typed_cases"], ids=lambda c: c["id"])
def test_frozen_original_actor_coordinates_and_scope_joins(case, monkeypatch):
    catalog, aliases = typed_sources(case, monkeypatch)
    actual = []
    for alias, source in aliases.items():
        for clause in source_assertions(source):
            participant = clause.actor_participation
            if participant is None:
                continue
            origin = clause.assertion_origin
            assert origin and not clause.unsupported
            assert (
                participant.coordinate_text[slice(*participant.nominal_span)]
                == participant.binding.text
            )
            actual.append(
                {
                    "role": participant.role,
                    "binding_kind": participant.binding.kind,
                    "literal_nominal": participant.binding.text,
                    "origin": {
                        "source_id": alias,
                        "document_sha256": origin.document_sha256,
                        "block_index": origin.block_index,
                        "sentence_index": origin.sentence_index,
                        "coordinate_text": participant.coordinate_text,
                        "nominal_span": list(participant.nominal_span),
                    },
                    "applies_to": {
                        "clause_index": origin.clause_index,
                        "cves": list(clause.cves),
                    },
                    "malicious_identity_inferred": False,
                    "status_strengthened": False,
                }
            )
    assert (actual or None) == case["expected_actor_participation"]
    if case.get("expected_unsupported"):
        assert any(
            clause.unsupported
            for source in aliases.values()
            for clause in source_assertions(source)
        )
        return
    for cve, status in case.get("states", {}).items():
        assert assess_exploitation(tuple(aliases.values()), [cve]).status == status
    if "expected_status" in case:
        cves = sorted(
            {
                cve
                for source in case["sources"]
                for cve in extract_cve_ids(source["text"])
            }
        )
        assert (
            assess_exploitation(tuple(aliases.values()), cves).status
            == case["expected_status"]
        )
    if extra := case.get("additional_clause"):
        clause = source_assertions(next(iter(aliases.values())))[extra["clause_index"]]
        assert list(clause.cves) == extra["inherited_cves"]
        assert clause.actor_participation is None
    for join in case.get("allowed_joins", []):
        source = aliases[join["source_id"]]
        blocks = owned_actor_blocks([source], join["finding_cves"])
        assert blocks and all(block.source_key == source.key for block in blocks)
    for join in case.get("forbidden_joins", []):
        assert not owned_actor_blocks(
            [aliases[join["source_id"]]], join["finding_cves"]
        )
    for alias in case.get("forbidden_sources", []):
        assert not owned_actor_blocks([aliases[alias]], [A])
    if case.get("extra_roles"):
        records = compile_finding_records(catalog)
        excerpts = [excerpt for record in records for excerpt in record.excerpts]
        assert excerpts and all("actors" in excerpt.roles for excerpt in excerpts)
        assert all(
            excerpt.text in [source["text"] for source in case["sources"]]
            for excerpt in excerpts
        )

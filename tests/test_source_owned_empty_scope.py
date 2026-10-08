"""Frozen source-owned empty scope; no new assertion/directive productions.

An empty CVE finding is one retained source, not a catalog-wide wildcard.
All expectations use existing parsed productions; unsupported arguments and
auxiliaries stay rejected. Source-owned summary rows use the finding's gate.
"""

import json

import pytest

from src.core.finding_evidence import (
    EvidenceError,
    assess_exploitation,
    build_finding_detail_context,
    source_assertions,
    source_evidence_text,
    validate_finding_evidence,
)
from src.core.finding_generation import compile_finding_records
from src.core.report_artifact import parse_report_artifact
from src.core.reporting import build_reporting_catalog
from test_finding_generation import catalog_for, render
from test_finding_generation_pipeline import run_real_pipeline
from test_owned_relation_contract import article

CVE = "CVE-2026-1234"
POSITIVE = "Attackers are actively exploiting the gateway."
NEGATIVE = "There is no evidence of exploitation."
STATES = [
    (POSITIVE, "active"),
    ("Attackers exploited the gateway.", "observed"),
    (NEGATIVE, "not_observed"),
    ("Potential exploitation was observed.", "potential"),
    ("Exploitation status is unknown.", "unknown"),
    (f"{POSITIVE} {NEGATIVE}", "unknown"),
    (f"{NEGATIVE} {POSITIVE}", "unknown"),
]


@pytest.mark.parametrize("text,status", STATES)
def test_source_owned_assessment_keeps_all_supported_relations(text, status):
    source = next(iter(catalog_for(text).values()))
    parsed = source_assertions(source)
    assert parsed and not any(clause.unsupported for clause in parsed)
    result = assess_exploitation([source], ())
    assert result.status == status
    assert result.relations == parsed
    assert result.conflicting is (POSITIVE in text and NEGATIVE in text)
    context = source_evidence_text([source], ())
    assert all(clause.source_text in context for clause in parsed)
    assert source.url in context


@pytest.mark.parametrize("text,status", STATES)
def test_source_owned_compile_render_and_real_pipeline(
    monkeypatch, tmp_path, text, status
):
    records, report = render(catalog_for(text))
    assert len(records) == 1 and records[0].cves == () and records[0].status == status
    sentences = [clause.source_text for clause in source_assertions(article(text))]
    assert all(sentence in report for sentence in sentences)
    evidence = dict(records[0].fields)["Source Evidence"]
    assert [evidence.index(sentence) for sentence in sentences] == sorted(
        evidence.index(sentence) for sentence in sentences
    )
    result = run_real_pipeline(
        monkeypatch, tmp_path / "index.md", articles=[article(text)]
    )
    assert result["status"] == "completed", result
    saved = (tmp_path / "index.md").read_text()
    (finding,) = parse_report_artifact(saved).findings
    assert finding.cve_ids == () and finding.exploitation_status.value == status
    assert all(sentence in saved for sentence in sentences)
    assert "Source Evidence" in (tmp_path / "index.html").read_text()
    assert json.loads((tmp_path / "current-findings.json").read_text())["cve_ids"] == []


@pytest.mark.parametrize("reverse", [False, True])
def test_independent_sources_do_not_share_empty_assessment_or_summary_scope(
    monkeypatch, tmp_path, reverse
):
    texts = [POSITIVE, NEGATIVE, f"{CVE} was exploited yesterday."]
    if reverse:
        texts.reverse()
    catalog = catalog_for(*texts)
    expected = {
        source.key: status
        for source, status in zip(
            catalog.values(),
            (
                reversed(["active", "not_observed", "observed"])
                if reverse
                else ["active", "not_observed", "observed"]
            ),
        )
    }
    for item in build_finding_detail_context(catalog):
        assert item["exploitation"]["status"] == expected[item["source_key"]]
    records, report = render(catalog)
    assert len(records) == 3
    for record in records:
        fields = dict(record.fields)
        assert record.status == expected[fields["Reporting"]]
        assert fields["Source Evidence"].count("[Source]") == 1
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[
            article(text, link=f"https://example.test/{index}")
            for index, text in enumerate(texts)
        ],
    )
    assert result["status"] == "completed", result
    assert len(parse_report_artifact((tmp_path / "index.md").read_text()).findings) == 3
    assert "Security reporting" in report


@pytest.mark.parametrize(
    "metadata",
    [
        {"cves": [CVE]},
        {"title": f"{CVE} advisory"},
        {"link": f"https://example.test/{CVE}"},
    ],
)
def test_metadata_identity_cannot_become_empty_scope(metadata):
    catalog = build_reporting_catalog([article(NEGATIVE, **metadata)])
    source = next(iter(catalog.values()))
    assert not assess_exploitation([source], ()).relations
    assert not source_evidence_text([source], ())
    records = compile_finding_records(catalog)
    assert [record.cves for record in records] == [(CVE,)]
    assert records[0].status == "unknown"


def test_empty_scope_cannot_select_cve_owned_claims_or_combine_sources():
    catalog = catalog_for(f"{CVE} was exploited yesterday.", POSITIVE, NEGATIVE)
    sources = list(catalog.values())
    assert not assess_exploitation(sources[:1], ()).relations
    assert not source_evidence_text(sources[:1], ())
    for consumer in (assess_exploitation, source_evidence_text):
        with pytest.raises(EvidenceError) as caught:
            consumer(sources[1:], ())
        assert caught.value.code == "ambiguous_source_scope"


@pytest.mark.parametrize(
    "mutation",
    [
        "omit",
        "truncate",
        "polarity",
        "source_url",
        "reporting",
        "combine",
        "cve_source",
        "badge",
        "narrative",
        "summary",
        "summary_owner",
        "summary_unowned",
    ],
)
def test_empty_scope_tampering_cannot_change_evidence_or_attribution(mutation):
    catalog = catalog_for(
        f"{POSITIVE} {NEGATIVE}", POSITIVE, f"{CVE} was exploited yesterday."
    )
    records, report = render(catalog)
    conflict = next(record for record in records if record.status == "unknown")
    positive = next(record for record in records if record.status == "active")
    fields = dict(conflict.fields)
    line = f'- **Source Evidence**: {fields["Source Evidence"]}'
    if mutation == "omit":
        damaged = report.replace(line, "")
    elif mutation in {"truncate", "polarity", "source_url"}:
        replacements = {
            "truncate": (NEGATIVE, ""),
            "polarity": ("no evidence", "evidence"),
            "source_url": ("advisory/0", "advisory/1"),
        }
        old, new = replacements[mutation]
        damaged = report.replace(line, line.replace(old, new))
    elif mutation in {"reporting", "combine", "cve_source"}:
        key = fields["Reporting"]
        other = (
            dict(positive.fields)["Reporting"]
            if mutation != "cve_source"
            else dict(records[0].fields)["Reporting"]
        )
        replacement = f"{key}, {other}" if mutation == "combine" else other
        damaged = report.replace(
            f"**Reporting**: {key}", f"**Reporting**: {replacement}"
        )
    elif mutation == "badge":
        damaged = report.replace(
            "**Exploitation Status**: unknown", "**Exploitation Status**: active"
        )
    elif mutation == "narrative":
        damaged = report.replace(
            f"### {conflict.heading}\n", f"### {conflict.heading}\n\n{POSITIVE}\n"
        )
    elif mutation == "summary_owner":
        damaged = report.replace(
            f"- **{positive.heading}**: {positive.state_prose}",
            f"- **{conflict.heading}**: {positive.state_prose}",
        )
    else:
        claim = (
            f"- **{conflict.heading}**: {POSITIVE}"
            if mutation == "summary"
            else POSITIVE
        )
        damaged = report.replace(
            "## Executive Summary\n", f"## Executive Summary\n\n{claim}\n"
        )
    assert damaged != report
    with pytest.raises(EvidenceError):
        validate_finding_evidence(damaged, catalog)


@pytest.mark.parametrize(
    "text",
    [
        "Attackers can be exploiting the gateway.",
        "Attackers will be exploiting the gateway.",
        "Attackers are actively exploiting the gateway in the wild.",
    ],
)
def test_unsupported_empty_scope_preserves_all_previous_artifacts(
    monkeypatch, tmp_path, text
):
    previous = {
        "index.md": b"Previous report",
        "index.html": b"Previous page",
        "current-findings.json": b'{"previous":true}',
        ".sentryinsight-articles-fingerprint": b"prior-fingerprint\n",
    }
    for name, content in previous.items():
        (tmp_path / name).write_bytes(content)
    assessment = assess_exploitation([article(text)], ())
    assert assessment.unsupported and assessment.status == "unknown"
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[article(text)],
        expect_model_call=False,
    )
    assert result["status"] == "failed"
    assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
    assert all(
        (tmp_path / name).read_bytes() == content for name, content in previous.items()
    )


@pytest.mark.parametrize("location", ["summary", "finding"])
def test_source_owned_summary_is_not_a_wildcard_for_foreign_cve_claims(location):
    catalog = catalog_for(POSITIVE, f"{CVE} is not exploited now.")
    records, report = render(catalog)
    active = next(record for record in records if not record.cves)
    if location == "summary":
        damaged = report.replace(
            f"- **{active.heading}**: {active.state_prose}",
            f"- **{active.heading}**: {CVE} is actively exploited.",
        )
    else:
        damaged = report.replace(
            f"### {active.heading}\n",
            f"### {active.heading}\n\n{CVE} is actively exploited.\n",
        )
    with pytest.raises(EvidenceError):
        validate_finding_evidence(damaged, catalog)

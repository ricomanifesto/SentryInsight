"""Owned relations survive presentation without becoming aggregate claims.

No assertion or directive grammar extension: all predicates here are already
supported. Exact source context is mandatory for conflicts and mixed ownership;
its source/wording cannot be changed, truncated, hidden, or used as a new badge.
"""

import json
import re

import pytest

from src.core.finding_evidence import (
    EvidenceError,
    grounding_failure_diagnostic,
    validate_finding_evidence,
)
from src.core.report_artifact import parse_report_artifact
from test_finding_generation import catalog_for, render
from test_finding_generation_pipeline import run_real_pipeline
from test_owned_relation_contract import article

CVE = "CVE-2026-1234"
OTHER = "CVE-2026-5678"


def evidence_lines(report):
    return [
        line
        for line in report.splitlines()
        if line.startswith("- **Source Evidence**:")
    ]


@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("independent", [False, True])
@pytest.mark.parametrize(
    "positive",
    [
        f"Attackers gained access by exploiting a vulnerability ({CVE})",
        f"{CVE} is actively exploited",
    ],
)
def test_complete_context_and_exact_independent_coverage_in_real_pipeline(
    monkeypatch, tmp_path, reverse, independent, positive
):
    negative = f"{OTHER if independent else CVE} is not exploited now"
    source = (
        ", but ".join(
            reversed([positive, negative]) if reverse else [positive, negative]
        )
        + "."
    )
    result = run_real_pipeline(
        monkeypatch, tmp_path / "index.md", articles=[article(source)]
    )
    assert result["status"] == "completed", result
    report = (tmp_path / "index.md").read_text()
    artifact = parse_report_artifact(report)
    expected = {(CVE,): "unknown"}
    if independent:
        expected = {
            (CVE,): "observed" if "gained access" in positive else "active",
            (OTHER,): "not_observed",
        }
    assert {
        f.cve_ids: f.exploitation_status.value for f in artifact.findings
    } == expected
    assert len(artifact.findings) == len(expected)
    serialized = json.loads((tmp_path / "current-findings.json").read_text())
    assert serialized["finding_count"] == len(expected)
    assert set(serialized["cve_ids"]) == {cve for ids in expected for cve in ids}
    lines = evidence_lines(report)
    assert len(lines) == len(expected) and all(source in line for line in lines)
    assert all("https://example.test/owned" in line for line in lines)
    html = (tmp_path / "index.html").read_text()
    assert "Source Evidence" in html
    if not independent:
        assert (
            "conflicting" in report
            and "combined exploitation status is unknown" in report
        )
    elif "gained access" in positive:
        assert "Current exploitation activity is not established" in report


@pytest.mark.parametrize(
    "mutation",
    [
        "omit",
        "truncate",
        "reverse_polarity",
        "foreign",
        "source",
        "badge",
        "narrative",
        "summary",
    ],
)
def test_attributed_context_cannot_bypass_whole_finding_or_summary_gates(mutation):
    positive = f"Attackers gained access by exploiting a vulnerability ({CVE})"
    negative = f"{CVE} is not exploited now"
    source = f"{positive}, but {negative}."
    catalog = catalog_for(source)
    _, report = render(catalog)
    line = evidence_lines(report)[0]
    if mutation == "omit":
        damaged = report.replace(line, "")
    elif mutation == "truncate":
        damaged = report.replace(line, line.replace(f", but {negative}", ""))
    elif mutation == "reverse_polarity":
        damaged = report.replace(line, line.replace("is not exploited", "is exploited"))
    elif mutation == "foreign":
        damaged = report.replace(line, line.replace(CVE, OTHER))
    elif mutation == "source":
        damaged = report.replace(
            line,
            line.replace(
                "https://example.test/advisory/0", "https://foreign.test/invented"
            ),
        )
    elif mutation == "badge":
        damaged = report.replace(
            "**Exploitation Status**: unknown", "**Exploitation Status**: active"
        )
    elif mutation == "narrative":
        damaged = report.replace("**Description**:", f"**Description**: {positive}. ")
    else:
        damaged = report.replace(
            "## Executive Summary\n",
            f"## Executive Summary\n\n{CVE} is actively exploited.\n",
        )
    assert damaged != report
    with pytest.raises(EvidenceError):
        validate_finding_evidence(damaged, catalog)


def test_context_is_complete_even_when_more_than_three_source_sentences_are_owned():
    texts = [
        f"{CVE} was exploited {when}."
        for when in ["yesterday", "two years ago", "in June", "last week"]
    ]
    texts.append(f"{CVE} is not exploited now.")
    catalog = catalog_for(*texts)
    _, report = render(catalog)
    context = evidence_lines(report)[0]
    assert all(text in context for text in texts)
    assert "conflicting" in report and "**Exploitation Status**: unknown" in report


def test_genuinely_joint_ownership_stays_one_finding_with_complete_conflicting_sources():
    positive = f"{CVE} and {OTHER} were exploited in attacks."
    negative = f"{CVE} and {OTHER} are not exploited now."
    records, report = render(catalog_for(positive, negative))
    assert len(records) == 1 and records[0].cves == (CVE, OTHER)
    assert records[0].status == "unknown"
    assert len(evidence_lines(report)) == 1
    assert (
        positive in evidence_lines(report)[0] and negative in evidence_lines(report)[0]
    )
    assert not re.search(rf"^### {CVE}$|^### {OTHER}$", report, re.M)


@pytest.mark.parametrize("reverse", [False, True])
def test_single_and_joint_predicates_in_one_sentence_do_not_collapse_ownership(
    monkeypatch, tmp_path, reverse
):
    clauses = [
        f"{CVE} was exploited yesterday",
        f"{CVE} and {OTHER} are not exploited now",
    ]
    source = ", but ".join(reversed(clauses) if reverse else clauses) + "."
    result = run_real_pipeline(
        monkeypatch, tmp_path / "index.md", articles=[article(source)]
    )
    assert result["status"] == "completed", result
    report = (tmp_path / "index.md").read_text()
    findings = parse_report_artifact(report).findings
    assert len(findings) == 1 and findings[0].cve_ids == (CVE, OTHER)
    assert findings[0].exploitation_status.value == "unknown"
    assert source in evidence_lines(report)[0] and "conflicting" in report


def test_incomplete_context_diagnostic_never_discloses_source_text_or_url():
    source = f"{CVE} was exploited yesterday, but {CVE} is not exploited now."
    catalog = catalog_for(source)
    _, report = render(catalog)
    damaged = report.replace(evidence_lines(report)[0], "")
    with pytest.raises(EvidenceError) as caught:
        validate_finding_evidence(damaged, catalog)
    diagnostic = grounding_failure_diagnostic(damaged, catalog, caught.value)
    assert diagnostic["code"] == "incomplete_source_evidence"
    assert diagnostic["field"] == "Source Evidence"
    assert diagnostic["expected"] is True and diagnostic["observed"] is False
    assert source not in json.dumps(diagnostic)
    assert "example.test" not in json.dumps(diagnostic)

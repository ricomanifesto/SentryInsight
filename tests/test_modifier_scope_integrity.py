"""Unbound negation and nested evidence absence cannot lose their scope."""

import pytest
import httpx

from src.core.finding_evidence import (
    EvidenceError,
    assess_exploitation,
    validate_finding_evidence,
)
from test_finding_generation import catalog_for, render
from test_finding_generation_pipeline import run_real_pipeline
from test_owned_relation_contract import article

CVE = "CVE-2026-1234"
UNBOUND = [
    f"Example Group has not widely oddly gained access by exploiting a vulnerability ({CVE}).",
    f"Example Group may have not widely oddly gained access by exploiting a vulnerability ({CVE}).",
]


@pytest.fixture(autouse=True)
def no_real_transport(monkeypatch):
    def forbidden(*args, **kwargs):
        raise AssertionError("Real transport forbidden")

    monkeypatch.setattr(httpx.Client, "send", forbidden)
    monkeypatch.setattr(httpx.AsyncClient, "send", forbidden)


@pytest.mark.parametrize("text", UNBOUND)
def test_unclassified_bridge_cannot_erase_intrusion_negation(text):
    assessment = assess_exploitation([article(text)], [CVE])
    assert assessment.unsupported
    assert assessment.status == "unknown"
    assert not assessment.positive


@pytest.mark.parametrize("text", UNBOUND)
def test_unclassified_bridge_preserves_artifacts_before_transport(
    monkeypatch, tmp_path, text
):
    original = {
        name: ("previous " + name).encode()
        for name in (
            "index.md",
            "index.html",
            "current-findings.json",
            ".sentryinsight-articles-fingerprint",
        )
    }
    for name, content in original.items():
        (tmp_path / name).write_bytes(content)
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[article(text)],
        expect_model_call=False,
    )
    assert result["status"] == "failed"
    assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
    assert all(
        (tmp_path / name).read_bytes() == content for name, content in original.items()
    )


@pytest.mark.parametrize(
    "wrapper",
    [
        "There is no evidence that {}.",
        "The vendor has not found evidence that {}.",
    ],
)
def test_nested_absence_retains_complete_qualified_source(wrapper):
    text = wrapper.format(f"{CVE} is not widely exploited")
    catalog = catalog_for(text)
    records, report = render(catalog)
    assert records[0].status == "unknown"
    assert text in report
    line = next(
        line
        for line in report.splitlines()
        if line.startswith("- **Source Evidence**:")
    )
    with pytest.raises(EvidenceError) as caught:
        validate_finding_evidence(report.replace(line, ""), catalog)
    assert caught.value.code == "incomplete_source_evidence"


@pytest.mark.parametrize(
    "prefix,expected", [("", "observed"), ("has not widely ", "unknown")]
)
def test_closed_intrusion_operator_controls(prefix, expected):
    assessment = assess_exploitation(
        [
            article(
                f"Example Group {prefix}gained access by exploiting a vulnerability ({CVE})."
            )
        ],
        [CVE],
    )
    assert not assessment.unsupported
    assert assessment.status == expected

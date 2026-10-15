"""Observe source ownership through compilation, rendering and atomic publication."""

from pathlib import Path

import httpx
import pytest

from publication_evidence import capture_generated_evidence
from src.core.finding_evidence import EvidenceError, validate_finding_evidence
from src.core.report_artifact import parse_report_artifact
from src.core.reporting import build_reporting_catalog
from test_finding_generation_pipeline import run_real_pipeline
from test_owned_relation_contract import article

A = "CVE-2026-1234"


@pytest.mark.parametrize(
    "observation,advice,status,action",
    [
        (
            f"{A} has seen exploitation.",
            "Users should update their systems.",
            "observed",
            "patch",
        ),
        (
            f"{A} have seen active exploitation.",
            "You should patch your systems.",
            "observed",
            "patch",
        ),
        (
            f"{A} had never seen exploitation.",
            "Update your systems.",
            "unknown",
            "patch",
        ),
        (
            f"{A} has not seen active exploitation. {A} is actively exploited.",
            "Users should monitor their systems.",
            "active",
            "monitor",
        ),
        (
            f"{A} has seen exploitation if reports are accurate.",
            "Users should not update their systems.",
            "unknown",
            "none",
        ),
        (
            f"{A} had seen exploitation yesterday.",
            "The vendor urges users to update their systems.",
            "observed",
            "patch",
        ),
        (
            f"{A} has seen active exploitation.",
            "Restart your systems.",
            "observed",
            "none",
        ),
        (
            f"{A} has seen attacks. {A} was exploited yesterday.",
            "Users should update the systems.",
            "unsupported",
            "none",
        ),
        (
            f"{A} has seen limited, targeted exploitation.",
            "Users should update the systems.",
            "unsupported",
            "none",
        ),
        (
            f"{A} has seen exploitation today.",
            "Users should update the systems.",
            "unsupported",
            "none",
        ),
        (
            f"{A} has seen exploitation.",
            "Your systems should be updated.",
            "unsupported",
            "none",
        ),
        (
            f"{A} has seen exploitation.",
            "Users should update Your systems.",
            "unsupported",
            "none",
        ),
        *[
            (
                f"{A} has seen exploitation.",
                f"{first} should update {first_possessive} systems and "
                f"{second} should monitor {second_possessive} systems"
                + (f" and restart {second_possessive} systems" if restart else "")
                + f" and {second_possessive} appliances.",
                "observed",
                "patch",
            )
            for first, first_possessive, second, second_possessive in [
                ("Users", "their", "you", "your"),
                ("You", "your", "users", "their"),
            ]
            for restart in (False, True)
        ],
        *[
            (
                f"{A} has seen exploitation.",
                f"Users should {predicate} {determiner} systems.",
                "unsupported" if determiner == "their" else "observed",
                action,
            )
            for predicate, action in [
                ("review logs on", "investigate"),
                ("rotate credentials for", "none"),
                ("install patches for", "patch"),
            ]
            for determiner in ("their", "the")
        ],
    ],
)
def test_owned_observation_and_directive_publication(
    monkeypatch, tmp_path, observation, advice, status, action
):
    def forbidden(*args, **kwargs):
        raise AssertionError("Real HTTP/model transport forbidden")

    monkeypatch.setattr(httpx.Client, "send", forbidden)
    monkeypatch.setattr(httpx.AsyncClient, "send", forbidden)
    root = Path(__file__).resolve().parents[1]
    previous = {
        name: (root / name).read_bytes()
        for name in (
            "index.md",
            "index.html",
            "current-findings.json",
            ".sentryinsight-articles-fingerprint",
        )
    }
    for name, data in previous.items():
        (tmp_path / name).write_bytes(data)
    source = article(
        f"## {A}\n\n{observation} {A} allows remote code execution on the gateway.\n\n{advice}"
    )
    baseline_for = capture_generated_evidence(monkeypatch)
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[source],
        expect_model_call=status != "unsupported",
    )
    if status == "unsupported":
        assert result["status"] == "failed"
        assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
        assert all(
            (tmp_path / name).read_bytes() == data for name, data in previous.items()
        )
        return
    assert result["status"] == "completed"
    published = (tmp_path / "index.md").read_text()
    (finding,) = parse_report_artifact(published).findings
    assert finding.exploitation_status.value == status
    assert finding.action.value == action
    assert advice in finding.recommended_actions
    catalog = build_reporting_catalog([source])
    baseline = baseline_for(published, catalog)
    evidence = next(
        line
        for line in baseline.splitlines()
        if line.startswith("- **Source Evidence**:")
    )
    guidance = next(
        line
        for line in baseline.splitlines()
        if line.startswith("- **Recommended Actions**:")
    )
    assert all(
        statement.strip() + "." in evidence
        for statement in observation.split(".")
        if statement.strip()
    )
    mutations = [
        (
            baseline.replace(
                evidence, "- **Source Evidence**: incomplete source evidence"
            ),
            "incomplete_source_evidence",
            "Source Evidence",
        ),
        (
            baseline.replace(
                guidance, "- **Recommended Actions**: Users should update the systems."
            ),
            "recommendation_not_grounded",
            "Recommended Actions",
        ),
        (
            baseline.replace(
                f"**Exploitation Status**: {status}",
                "**Exploitation Status**: "
                + ("not_observed" if status == "active" else "active"),
            ),
            "unsupported_exploitation_status",
            "Exploitation Status",
        ),
    ]
    for mutated, code, field in mutations:
        assert mutated != baseline
        with pytest.raises(EvidenceError) as failure:
            validate_finding_evidence(mutated, catalog)
        assert (failure.value.code, failure.value.field) == (code, field)

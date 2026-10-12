"""A prerequisite for exploitation is not an assertion it occurred."""

import pytest
from src.core.assertions import parse_assertions
from test_composed_document_pipeline_contract import article
from test_finding_generation_pipeline import run_real_pipeline


@pytest.mark.parametrize(
    "predicate", ["needs no account", "needs an account", "does not need an account"]
)
def test_account_prerequisite_owns_its_purpose_event(monkeypatch, tmp_path, predicate):
    text = f"An attacker {predicate} to exploit it."
    clauses = parse_assertions(text)
    assert clauses and all(
        c.kind == "context" and c.modal == "capability" and not c.unsupported
        for c in clauses
    )
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[
            article(
                f"<h2>CVE-2026-1234</h2><p>CVE-2026-1234 exploitation status is unknown.</p><p>{text}</p>"
            )
        ],
    )
    assert result["status"] == "completed", result
    report = (tmp_path / "index.md").read_text()
    assert text in report and "**Exploitation Status**: unknown" in report


@pytest.mark.parametrize(
    "tail", ["and unspecified assumptions apply", "with an unclassified purpose"]
)
def test_prerequisite_cannot_swallow_unknown_residual(monkeypatch, tmp_path, tail):
    text = f"An attacker needs no account to exploit CVE-2026-1234 {tail}."
    assert any(c.unsupported for c in parse_assertions(text))
    paths = [
        tmp_path / name
        for name in (
            "index.md",
            "index.html",
            "current-findings.json",
            ".sentryinsight-articles-fingerprint",
        )
    ]
    for path in paths:
        path.write_bytes(b"Prior validated artifact")
    result = run_real_pipeline(
        monkeypatch,
        paths[0],
        articles=[article(f"<h2>CVE-2026-1234</h2><p>{text}</p>")],
        expect_model_call=False,
    )
    assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
    assert all(path.read_bytes() == b"Prior validated artifact" for path in paths)

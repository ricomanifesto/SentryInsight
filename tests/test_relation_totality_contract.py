"""Required relations need a semantic state and complete predicate ownership.

Unsupported forms fail before model transport and preserve every prior artifact.
These cases add no accepted syntax to the bounded assertion/directive grammar.
"""

import json

import pytest

from src.core.finding_evidence import assess_exploitation
from test_finding_generation_pipeline import run_real_pipeline
from test_owned_relation_contract import article

CVE = "CVE-2026-1234"
OTHER = "CVE-2026-5678"
UNSUPPORTED_AUXILIARIES = (
    "has been",
    "have been",
    "can be",
    "will be",
    "can have been",
    "will have been",
    "is will be",
    "was can be",
    "has is",
)


def assert_preserved_unsupported(monkeypatch, tmp_path, content):
    previous = {
        "index.md": b"Previous validated report",
        "index.html": b"Previous site",
        "current-findings.json": b'{"previous":true}',
    }
    for name, data in previous.items():
        (tmp_path / name).write_bytes(data)
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[article(content)],
        expect_model_call=False,
    )
    assert result["status"] == "failed", result
    assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
    assert all(
        (tmp_path / name).read_bytes() == data for name, data in previous.items()
    )


@pytest.mark.parametrize("auxiliary", UNSUPPORTED_AUXILIARIES)
def test_unclassified_auxiliary_has_no_confirmed_state(auxiliary):
    assessment = assess_exploitation([article(f"{CVE} {auxiliary} exploited.")], [CVE])
    assert assessment.status not in {"active", "observed"}
    assert assessment.unsupported
    assert assessment.relations
    assert not any(r.status in {"active", "observed"} for r in assessment.relations)


@pytest.mark.parametrize("auxiliary", UNSUPPORTED_AUXILIARIES)
def test_unclassified_auxiliary_preserves_pipeline_artifacts(
    monkeypatch, tmp_path, auxiliary
):
    assert_preserved_unsupported(monkeypatch, tmp_path, f"{CVE} {auxiliary} exploited.")


@pytest.mark.parametrize(
    "predicate,status",
    [
        ("is actively exploited", "active"),
        ("was exploited yesterday", "observed"),
        ("is not exploited now", "not_observed"),
        ("may have been exploited", "potential"),
    ],
)
def test_supported_predicate_state_remains_owned_in_pipeline(
    monkeypatch, tmp_path, predicate, status
):
    source = f"{CVE} {predicate}."
    assessment = assess_exploitation([article(source)], [CVE])
    assert assessment.status == status and not assessment.unsupported
    result = run_real_pipeline(
        monkeypatch, tmp_path / "index.md", articles=[article(source)]
    )
    assert result["status"] == "completed", result
    assert f"**Exploitation Status**: {status}" in (tmp_path / "index.md").read_text()


@pytest.mark.parametrize(
    "auxiliary,status",
    [
        ("is", "active"),
        ("are", "active"),
        ("is being", "active"),
        ("are being", "active"),
        ("was", "observed"),
        ("were", "observed"),
        ("was being", "observed"),
        ("were being", "observed"),
        ("had been", "observed"),
        ("may be", "potential"),
        ("might be", "potential"),
        ("could be", "potential"),
        ("would be", "potential"),
        ("may have been", "potential"),
        ("might have been", "potential"),
        ("could have been", "potential"),
        ("would have been", "potential"),
    ],
)
def test_finite_auxiliary_acceptance_has_an_explicit_semantic_state(auxiliary, status):
    result = assess_exploitation([article(f"{CVE} {auxiliary} exploited.")], [CVE])
    assert result.status == status and not result.unsupported
    assert len(result.relations) == 1 and result.relations[0].status == status


@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("other_cve", [False, True])
def test_intrusion_cannot_consume_an_independent_negative_predicate(
    monkeypatch, tmp_path, reverse, other_cve
):
    intrusion = f"Attackers gained access by exploiting a vulnerability ({CVE})"
    contrary = f"{OTHER if other_cve else CVE} is not exploited now"
    source = (
        ", but ".join((contrary, intrusion) if reverse else (intrusion, contrary)) + "."
    )
    assessment = assess_exploitation([article(source)], [CVE])
    assert assessment.status == ("observed" if other_cve else "unknown")
    assert assessment.conflicting is (not other_cve)
    assert assessment.positive
    if not other_cve:
        assert assessment.negative
        assert len(assessment.relations) == 2
    other = assess_exploitation([article(source)], [OTHER])
    if other_cve:
        assert other.status == "not_observed" and other.negative
    result = run_real_pipeline(
        monkeypatch, tmp_path / "index.md", articles=[article(source)]
    )
    assert result["status"] == "completed", result
    report = (tmp_path / "index.md").read_text()
    assert source in report
    expected = {CVE, OTHER} if other_cve else {CVE}
    artifact = json.loads((tmp_path / "current-findings.json").read_text())
    assert set(artifact["cve_ids"]) == expected
    if not other_cve:
        assert "conflicting" in report


@pytest.mark.parametrize(
    "tail",
    [
        f"but {CVE} is thought by some analysts to be actively exploited",
        f"and {CVE} will be exploited",
    ],
)
def test_intrusion_cannot_hide_an_unsupported_remaining_predicate(
    monkeypatch, tmp_path, tail
):
    source = f"Attackers gained access by exploiting a vulnerability ({CVE}), {tail}."
    assessment = assess_exploitation([article(source)], [CVE])
    assert assessment.unsupported
    assert_preserved_unsupported(monkeypatch, tmp_path, source)


@pytest.mark.parametrize(
    "guidance",
    [
        "Restart the service.",
        "Restart the service only after backing up the configuration.",
        "Customers should install the patch. Restart the service.",
        "Customers should install the patch. Restart the service only after backing up the configuration.",
    ],
)
def test_explicit_supporting_restart_retains_guidance(monkeypatch, tmp_path, guidance):
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[
            article(f"## {CVE}\n\n{CVE} exploitation status is unknown.\n\n{guidance}")
        ],
    )
    assert result["status"] == "completed", result
    report = (tmp_path / "index.md").read_text()
    assert guidance in report
    expected = "patch" if guidance.startswith("Customers") else "none"
    assert f"**Action**: {expected}" in report


@pytest.mark.parametrize(
    "guidance",
    [
        "For guidance, install the patch.",
        "Administrators intend to install the patch.",
        "Restart the service with an unclassified setting.",
    ],
)
def test_cue_owned_unparsed_guidance_is_terminal_unsupported(
    monkeypatch, tmp_path, guidance
):
    assert_preserved_unsupported(
        monkeypatch,
        tmp_path,
        f"## {CVE}\n\n{CVE} exploitation status is unknown.\n\n{guidance}",
    )

"""Frozen local extension: ownership first; no arbitrary-English expansion.

Joint assertion scopes survive selection, including unsupported and negative
relations. A joint predicate may establish a joint finding, not each singleton.
Descriptive subjects admit a plural vulnerability noun with a parenthesized
CVE pair and a bounded product-name modifier; an optional month/date adjunct
does not own the passive predicate's tense, polarity or modality.

Directive arguments reuse the existing version owner's named cumulative-update
and affected-release identities. Its role regex may not establish advice
modality. Condition-only/prohibited implicit targets are qualified constraints,
never positive badges; unknown audience bridges/arguments remain unsupported.

Expected statuses, counts, scopes and actions are independently specified here.
This file is frozen before production changes for the authorized follow-up.
"""

import json

import pytest

from src.core.finding_evidence import assess_exploitation, recommendation_action
from src.core.finding_generation import compile_finding_records
from test_finding_generation import catalog_for, render
from test_finding_generation_pipeline import run_real_pipeline
from test_owned_relation_contract import article

CVE = "CVE-2026-1234"
OTHER = "CVE-2026-5678"
THIRD = "CVE-2026-9999"
PAIR = (CVE, OTHER)
RELEASE = "Example Server 2019 Cumulative Update 15"


@pytest.mark.parametrize(
    "predicate,status",
    [
        ("are actively exploited", "active"),
        ("were exploited", "observed"),
        ("were not exploited", "not_observed"),
        ("may be exploited", "potential"),
    ],
)
def test_joint_predicate_is_retained_without_singleton_distribution(predicate, status):
    text = f"{CVE} and {OTHER} {predicate} in attacks."
    catalog = catalog_for(text)
    joint = assess_exploitation(list(catalog.values()), PAIR)
    assert joint.status == status
    assert not joint.unsupported
    for cve in PAIR:
        assert assess_exploitation(list(catalog.values()), [cve]).status == "unknown"
    records, report = render(catalog)
    assert len(records) == 1 and records[0].cves == PAIR
    assert records[0].status == status
    assert text in report


@pytest.mark.parametrize("date", ["", "In July, ", "In September, "])
@pytest.mark.parametrize(
    "predicate,status",
    [
        ("were exploited", "observed"),
        ("were not exploited", "not_observed"),
        ("may have been exploited", "potential"),
        ("are actively exploited", "active"),
    ],
)
def test_descriptive_joint_subject_keeps_predicate_meaning_through_pipeline(
    monkeypatch, tmp_path, date, predicate, status
):
    text = (
        f"{date}two ExampleVPN zero-days ({CVE} and {OTHER}) {predicate} "
        "for weeks to install custom malware on vulnerable VPN appliances."
    )
    result = run_real_pipeline(
        monkeypatch, tmp_path / "index.md", articles=[article(text)]
    )
    assert result["status"] == "completed", result
    data = json.loads((tmp_path / "current-findings.json").read_text())
    assert data["finding_count"] == 1 and set(data["cve_ids"]) == set(PAIR)
    report = (tmp_path / "index.md").read_text()
    assert f"**Exploitation Status**: {status}" in report
    assert text in report
    if status == "observed":
        assert "Current exploitation activity is not established" in report


@pytest.mark.parametrize("scope", [(CVE,), (OTHER,), PAIR])
def test_required_unsupported_joint_relation_is_never_lost_before_assessment(scope):
    text = f"{CVE} and {OTHER} are thought by analysts to be exploited."
    result = assess_exploitation([article(text)], scope)
    assert result.unsupported and result.status == "unknown"


@pytest.mark.parametrize("reverse", [False, True])
def test_joint_negative_source_survives_independent_positive_source(reverse):
    positive = f"{CVE} and {OTHER} were exploited in attacks."
    negative = f"{CVE} and {OTHER} were not exploited in attacks."
    texts = [positive, negative]
    if reverse:
        texts.reverse()
    catalog = catalog_for(*texts)
    assessment = assess_exploitation(list(catalog.values()), PAIR)
    assert assessment.conflicting and assessment.positive and assessment.negative
    records, report = render(catalog)
    assert len(records) == 1 and records[0].status == "unknown"
    assert "conflicting" in report and "not been observed" in report


def test_joint_ownership_does_not_consume_other_cve_or_incidental_mentions():
    catalog = catalog_for(
        f"{CVE} and {OTHER} were exploited in attacks.\n\n"
        f"{THIRD} exploitation status is unknown.\n\n"
        f"The researcher discussed {CVE}, {OTHER}, and {THIRD}."
    )
    records = compile_finding_records(catalog)
    assert {record.cves: record.status for record in records} == {
        PAIR: "observed",
        (THIRD,): "unknown",
    }


@pytest.mark.parametrize(
    "text",
    [
        f"{CVE} and {OTHER} are thought by analysts to be exploited.",
        f"Investigators doubt that two ExampleVPN zero-days ({CVE} and {OTHER}) were exploited.",
    ],
)
def test_required_unknown_joint_grammar_preserves_previous_artifacts(
    monkeypatch, tmp_path, text
):
    output = tmp_path / "index.md"
    old = {
        "index.md": b"Previous validated report",
        "index.html": b"Previous site",
        "current-findings.json": b'{"previous":true}',
    }
    for name, content in old.items():
        (tmp_path / name).write_bytes(content)
    result = run_real_pipeline(
        monkeypatch, output, articles=[article(text)], expect_model_call=False
    )
    assert result["status"] == "failed", result
    assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
    assert all(
        (tmp_path / name).read_bytes() == content for name, content in old.items()
    )


@pytest.mark.parametrize("verb", ["install", "apply"])
@pytest.mark.parametrize("separator", [" ", "\n"])
@pytest.mark.parametrize(
    "form,action",
    [
        ("should {}", "patch"),
        ("should not {}", "none"),
        ("should {} only if exposed", "none"),
    ],
)
def test_named_release_argument_uses_version_identity_in_real_pipeline(
    monkeypatch, tmp_path, verb, separator, form, action
):
    guidance = "Customers " + form.format(verb + separator + RELEASE) + "."
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[
            article(f"## {CVE}\n\n{CVE} exploitation status is unknown.\n\n{guidance}")
        ],
    )
    assert result["status"] == "completed", result
    report = (tmp_path / "index.md").read_text()
    assert f"**Action**: {action}" in report
    assert " ".join(guidance.split()) in report
    assert "**Affected Versions**: Not stated in supplied sources." in report


@pytest.mark.parametrize(
    "tail",
    ["for affected versions.", "for affected versions:", "on affected releases."],
)
def test_affected_release_target_preserves_existing_version_owner(
    monkeypatch, tmp_path, tail
):
    guidance = "Customers should install the fix " + tail
    content = f"## {CVE}\n\n{CVE} exploitation status is unknown.\n\n{guidance}\n{RELEASE}\n\n"
    result = run_real_pipeline(
        monkeypatch, tmp_path / "index.md", articles=[article(content)]
    )
    assert result["status"] == "completed", result
    report = (tmp_path / "index.md").read_text()
    assert "**Action**: patch" in report and guidance in report
    assert RELEASE in report


@pytest.mark.parametrize(
    "guidance",
    [
        "Customers should upgrade only if exposed.",
        "Customers should not upgrade.",
        "Do not install.",
        "If exposed, customers should upgrade.",
    ],
)
def test_qualified_implicit_target_is_not_an_unconditional_action(
    monkeypatch, tmp_path, guidance
):
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[
            article(f"## {CVE}\n\n{CVE} exploitation status is unknown.\n\n{guidance}")
        ],
    )
    assert result["status"] == "completed", result
    report = (tmp_path / "index.md").read_text()
    assert "**Action**: none" in report and guidance in report


@pytest.mark.parametrize(
    "guidance",
    [
        "Users should update the advisory.",
        "Users should upgrade to the vendor.",
        "Users should upgrade the appliance to the advisory.",
        "Users should monitor logs and consider installing an update.",
        "Monitor logs and consider installing an update.",
        "Users with an unclassified relation should install the patch.",
        "Users of systems if they are unsure whether they should install the patch.",
        "Users of systems when they deny that they should install the patch.",
        "Customers should upgrade.",
    ],
)
def test_unclassified_required_advice_fails_closed_and_keeps_original_safety(
    monkeypatch, tmp_path, guidance
):
    assert recommendation_action([guidance]) == "none"
    old = {
        "index.md": b"Previous validated report",
        "index.html": b"Previous site",
        "current-findings.json": b'{"previous":true}',
    }
    for name, content in old.items():
        (tmp_path / name).write_bytes(content)
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[
            article(f"## {CVE}\n\n{CVE} exploitation status is unknown.\n\n{guidance}")
        ],
        expect_model_call=False,
    )
    assert result["status"] == "failed", result
    assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
    assert all(
        (tmp_path / name).read_bytes() == content for name, content in old.items()
    )

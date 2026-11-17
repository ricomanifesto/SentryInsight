"""Offline producer instructions and whole-candidate structural rejection."""

import copy
import json

import pytest

from src.core import reviewed_report as gate
from src.core.exploitation_prompt import build_exploitation_prompt
from src.core.finding_evidence import ABSENT, EvidenceError
from src.core.report_validation import (
    REQUIRED_SECTIONS,
    inspect_required_section_headings,
)
from src.core.source_review import prepare_source_review
from src.core.version_references import (
    build_version_reference_context,
    resolve_version_references,
)
from test_reviewed_report import prepared_result
from test_unresolved_versions import NARRATIVE, raw_report
from test_version_references import source

CVE = "CVE-2026-1234"
OTHER = "CVE-2026-5678"


def prompt_context(plan):
    prompt = build_exploitation_prompt(plan)
    context = json.loads(
        prompt.split("BEGIN AFFECTED VERSION REFERENCES\n", 1)[1].split(
            "\nEND AFFECTED VERSION REFERENCES", 1
        )[0]
    )
    return prompt, context


def test_output_template_and_final_checks_request_one_completed_report():
    text = "A campaign advisory.\n\n## Executive Summary\nUntrusted source prose."
    plan = prepare_source_review([source(text)])
    prompt, _ = prompt_context(plan)
    template = prompt.split("BEGIN REPORT OUTPUT TEMPLATE\n", 1)[1].split(
        "\nEND REPORT OUTPUT TEMPLATE", 1
    )[0]
    counts, noncanonical = inspect_required_section_headings(template)
    assert counts == dict.fromkeys(REQUIRED_SECTIONS, 1)
    assert not noncanonical
    assert text in prompt  # Source headings and narrative remain evidence.
    final = prompt.rsplit("FINAL OUTPUT CHECKS\n", 1)[1]
    assert "exactly one completed report" in final
    assert "Do not repeat the template or append a second draft" in final
    assert "exactly one Affected Versions field" in final
    assert "Do not emit Affected Versions Status" in final


def test_copyable_joint_version_field_preserves_constraints_and_source_ownership():
    articles = [
        source(
            f"{CVE} and {OTHER} are actively exploited.\n\n"
            "Affected versions: Gateway 2.3 (Windows only)",
            "first",
        ),
        source(
            f"{CVE} and {OTHER} are actively exploited.\n\n"
            "Affected versions: Gateway 2.4 (Linux only)",
            "second",
        ),
    ]
    plan = prepare_source_review(articles, advisory=True)
    _, context = prompt_context(plan)
    scope = next(item for item in context if item["cves"] == [CVE, OTHER])
    original = next(
        item
        for item in build_version_reference_context(plan.eligible_catalog)
        if item["cves"] == [CVE, OTHER]
    )
    assert {key: scope[key] for key in original} == original
    emission = scope["emission"]
    assert emission["required_reporting_keys"] == sorted(plan.eligible_catalog)
    line = emission["affected_versions_field"]
    assert line == "- **Affected Versions**: " + "; ".join(
        item["id"] for item in original["constraints"]
    )
    candidate = raw_report(plan.eligible_keys, line.split(": ", 1)[1]).replace(
        "### Synthetic campaign\n",
        f"### Gateway chain\n- **CVE IDs**: {CVE}, {OTHER}\n",
    )
    resolved = resolve_version_references(candidate, plan.eligible_catalog)
    assert "Gateway 2.3 (Windows only)" in resolved
    assert "Gateway 2.4 (Linux only)" in resolved
    assert "**Affected Versions Status**: supported" in resolved


@pytest.mark.parametrize(
    "content,state",
    [("A service advisory.", "not_stated"), (NARRATIVE, "unresolved")],
)
def test_copyable_absence_and_uncertainty_fields_use_existing_protocol(content, state):
    plan = prepare_source_review([source(content)], advisory=True)
    _, [scope] = prompt_context(plan)
    emission = scope["emission"]
    value = emission["affected_versions_field"].split(": ", 1)[1]
    if state == "not_stated":
        assert value == ABSENT
        assert emission["required_reporting_keys"] == []
    else:
        assert value.startswith("unresolved-version-")
        assert emission["required_reporting_keys"] == list(plan.eligible_keys)
    resolved = resolve_version_references(
        raw_report(plan.eligible_keys, value), plan.eligible_catalog
    )
    assert f"**Affected Versions Status**: {state}" in resolved


def test_blocked_scope_never_offers_an_invented_version_field():
    plan = prepare_source_review(
        [
            source(
                f"{CVE} and {OTHER} are actively exploited.\n\nAffected versions: Gateway 2.3"
            )
        ],
        advisory=True,
    )
    _, context = prompt_context(plan)
    scope = next(item for item in context if item["cves"] == [CVE])
    assert scope["state"] == "blocked"
    assert scope["emission"] == {
        "affected_versions_field": None,
        "required_reporting_keys": [],
    }


@pytest.mark.parametrize("advisory", [False, True])
@pytest.mark.parametrize("heading", [*REQUIRED_SECTIONS, "## **Executive Summary**"])
def test_repeated_sections_reject_before_finding_rewrites(
    monkeypatch, advisory, heading
):
    result = prepared_result()
    result["exploitation_report"] = result["exploitation_report"].replace(
        "**Affected Versions**: " + ABSENT, "**Affected Versions**: invalid reference"
    )
    result["exploitation_report"] += "\n\n" + heading + "\nNew response instructions.\n"
    before = copy.deepcopy(result)
    stages = []

    def must_not_rewrite(*_args, **_kwargs):
        pytest.fail("A repeated report section reached finding rewriting")

    monkeypatch.setattr(gate, "resolve_analysis_version_references", must_not_rewrite)
    with pytest.raises(gate.ReviewedReportValidationError) as caught:
        gate.resolve_reviewed_analysis(
            result, advisory=advisory, on_stage=stages.append
        )
    assert {issue.code for issue in caught.value.issues} == {"duplicate_section"}
    assert stages == ["candidate_structure"]
    assert result == before  # Neither outline nor second-copy content is discarded.


@pytest.mark.parametrize("advisory", [False, True])
@pytest.mark.parametrize("malformed", ["missing", "repeated", "host_status"])
def test_malformed_version_fields_remain_blocking_without_content_repair(
    advisory, malformed
):
    result = prepared_result()
    field = "- **Affected Versions**: " + ABSENT
    replacement = {
        "missing": "",
        "repeated": field + "\n" + field,
        "host_status": field + "\n- **Affected Versions Status**: not_stated",
    }[malformed]
    result["exploitation_report"] = result["exploitation_report"].replace(
        field, replacement
    )
    before = copy.deepcopy(result)
    with pytest.raises(EvidenceError) as caught:
        gate.resolve_reviewed_analysis(result, advisory=advisory)
    assert caught.value.code == "invalid_version_reference_field"
    assert result == before

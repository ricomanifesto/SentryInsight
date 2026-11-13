"""The prompt offers the explicit unresolved output accepted by advisory mode."""

import json

import pytest

from src.core.exploitation_prompt import build_exploitation_prompt
from src.core.finding_evidence import EvidenceError
from src.core.source_review import prepare_source_review
from src.core.version_references import resolve_version_references
from src.core.version_state import UNRESOLVED
from test_version_references import report, source

CVE = "CVE-2017-16995"


def blocked_article():
    return source(f"{CVE} affects Linux versions 4.4 through unknown.")


def test_strict_holds_soft_blocked_cve_and_keeps_strict_prompt():
    plan = prepare_source_review([blocked_article()])
    assert not plan.eligible_keys
    assert plan.packet["sources"][0]["state"] == "review_required"
    prompt = build_exploitation_prompt(plan)
    assert "A blocked scope remains ineligible" in prompt
    assert "For a retained scope marked blocked" not in prompt
    assert CVE not in prompt


def test_advisory_prompt_offers_explicit_unresolved_for_retained_blocked_cve():
    plan = prepare_source_review([blocked_article()], advisory=True)
    assert plan.eligible_keys
    prompt = build_exploitation_prompt(plan)
    context = json.loads(
        prompt.split("BEGIN AFFECTED VERSION REFERENCES\n", 1)[1].split(
            "\nEND AFFECTED VERSION REFERENCES", 1
        )[0]
    )
    assert context[0]["cves"] == [CVE]
    assert context[0]["blocked"] is True
    assert context[0]["absence_allowed"] is False
    assert f"For a retained scope marked blocked, put exactly {UNRESOLVED}" in prompt
    assert "A blocked scope remains ineligible" not in prompt
    assert "Do not invent IDs or omit the finding" in prompt

    candidate = report(plan.eligible_catalog, UNRESOLVED, cves=CVE, status="unknown")
    errors = []
    resolved = resolve_version_references(
        candidate, plan.eligible_catalog, on_reject=errors.append
    )
    assert [error.code for error in errors] == ["unresolved_version_evidence"]
    assert f"**Affected Versions**: {UNRESOLVED}" in resolved
    assert "**Affected Versions Status**: unresolved" in resolved
    assert CVE in resolved
    with pytest.raises(EvidenceError) as rejected:
        resolve_version_references(candidate, plan.eligible_catalog)
    assert rejected.value.code == "unresolved_version_evidence"


def test_advisory_prompt_never_offers_hard_rejected_source():
    rejected = source("Affected versions:", "hard-rejected")
    plan = prepare_source_review([rejected, blocked_article()], advisory=True)
    row = next(row for row in plan.packet["sources"] if row["url"] == rejected["link"])
    assert row["state"] == "source_rejected"
    prompt = build_exploitation_prompt(plan)
    assert row["key"] not in prompt
    assert rejected["link"] not in prompt

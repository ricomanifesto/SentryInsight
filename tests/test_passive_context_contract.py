"""Complete source-owned directive and context relations preserve their operands."""

import httpx
import pytest
from src.core.assertions import source_qualification
from src.core.recommendations import parse_recommendation
from src.core.finding_evidence import (
    EvidenceError,
    validate_finding_evidence,
    recommendation_action,
)
from src.core.finding_generation import compile_finding_records, _finding
from src.core.reporting import build_reporting_catalog
from src.core.report_artifact import parse_report_artifact
from test_owned_relation_contract import article
from test_directive_modifier_contract import pipeline
from test_finding_generation_pipeline import run_real_pipeline

A = "CVE-2026-1234"
B = "CVE-2026-5678"


@pytest.fixture(autouse=True)
def no_real_transport(monkeypatch):
    def forbidden(*a, **kw):
        raise AssertionError("Real transport forbidden")

    monkeypatch.setattr(httpx.Client, "send", forbidden)
    monkeypatch.setattr(httpx.AsyncClient, "send", forbidden)


SYSTEMS = [
    "Example Gateway appliances",
    "Example ADC and Sample Gateway appliances",
    "Different Server systems",
]
ROLES = [
    "Identity Provider",
    "Service Provider (SP)",
    "Example Assertion Protocol (EAP) Identity Provider (IdP) or Service Provider (SP)",
]


@pytest.mark.parametrize("system", SYSTEMS)
@pytest.mark.parametrize("role", ROLES)
@pytest.mark.parametrize("negative", ["", "not "])
def test_configuration_necessity_is_complete_context(system, role, negative):
    text = f"To be vulnerable, {system} must {negative}be configured as a {role}."
    q = source_qualification(text)
    assert q and not q.unsupported and q.kind == "context" and q.modal == "capability"
    assert q.text == text and q.source_text == text and q.assertion_status is None
    assert q.polarity == ("negative" if negative else "affirmative")
    assert recommendation_action([text]) == "none"


@pytest.mark.parametrize(
    "wrapper", ["{}", "If reports are accurate, {}", '"{}," the company said.']
)
@pytest.mark.parametrize("negative", ["", "not "])
def test_owned_configuration_context_survives_pipeline_and_tampering(
    monkeypatch, tmp_path, wrapper, negative
):
    core = f"To be vulnerable, Example Gateway appliances must {negative}be configured as an Identity Provider"
    text = wrapper.format(core).rstrip(".") + "."
    guidance = "Users should install the patch."
    item = article(
        f"## {A}\n\n{A} exploitation has not been observed.\n\n{text}\n\n{guidance}"
    )
    catalog = build_reporting_catalog([item])
    (record,) = compile_finding_records(catalog, [A])
    fields = dict(record.fields)
    assert text in fields["Source Constraints"]
    assert fields["Recommended Actions"] == guidance and fields["Action"] == "patch"
    assert fields["Exploitation Status"] == "not_observed"
    report = "## Active Exploitation Details\n\n" + _finding(record)
    validate_finding_evidence(report, catalog)
    damaged = report.replace(text, text.replace("configured", "reconfigured"))
    with pytest.raises(EvidenceError):
        validate_finding_evidence(damaged, catalog)
    result = run_real_pipeline(monkeypatch, tmp_path / "index.md", articles=[item])
    assert result["status"] == "completed", result
    assert text in (tmp_path / "index.md").read_text()


@pytest.mark.parametrize("name", ["Example", "Other Campaign"])
@pytest.mark.parametrize("voice", ["active", "passive"])
@pytest.mark.parametrize("qualification", ["affirmative", "negative", "conditional"])
@pytest.mark.parametrize("simply", ["", "simply "])
def test_supporting_interpretation_preserves_full_guidance(
    monkeypatch, tmp_path, name, voice, qualification, simply
):
    target = f"the infrastructure behind {name}"
    negative = "not " if qualification == "negative" else ""
    text = (
        f"Users should {negative}view {target} {simply}as a list of domains to block"
        if voice == "active"
        else f"{target[0].upper()+target[1:]} should {negative}be viewed {simply}as a list of domains to block"
    )
    text += ", if needed." if qualification == "conditional" else "."
    p = parse_recommendation(text)
    assert p and not p.ambiguous and p.source_text == text
    (c,) = p.clauses
    assert c.verb == "view" and c.polarity == (
        "negative" if negative else "affirmative"
    )
    assert c.conditions == (("if needed",) if qualification == "conditional" else ())
    assert c.argument_relation == "classification" and c.object_members == (
        "infrastructure",
    )
    assert recommendation_action([text]) == "none"
    pipeline(monkeypatch, tmp_path, text, "none")


@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("connector", [" and ", "; "])
def test_analytical_instruction_cannot_suppress_separate_patch(
    monkeypatch, tmp_path, reverse, connector
):
    parts = [
        "The infrastructure behind Example should not be viewed simply as a list of domains to block",
        "Users should install the patch",
    ]
    if reverse:
        parts.reverse()
    pipeline(monkeypatch, tmp_path, connector.join(parts) + ".", "patch")


@pytest.mark.parametrize("scope", ["source_only", "joint", "foreign"])
def test_new_guidance_keeps_existing_source_and_identity_owners(
    monkeypatch, tmp_path, scope
):
    text = "The infrastructure behind Example should not be viewed simply as a list of domains to block."
    header = (
        ""
        if scope == "source_only"
        else f"## {A} and {B}\n\n" if scope == "joint" else f"## {A}\n\n"
    )
    event = (
        "Attackers are actively exploiting the gateway."
        if scope == "source_only"
        else (
            f"{A} and {B} exploitation status is unknown."
            if scope == "joint"
            else f"{A} exploitation status is unknown."
        )
    )
    items = [article(header + event + "\n\n" + text)]
    if scope == "foreign":
        items.append(
            article(
                f"## {B}\n\n{B} exploitation status is unknown.\n\nUsers should monitor logs.",
                link="https://example.test/other",
            )
        )
    result = run_real_pipeline(monkeypatch, tmp_path / "index.md", articles=items)
    assert result["status"] == "completed", result
    fs = parse_report_artifact((tmp_path / "index.md").read_text()).findings
    target = next(
        f
        for f in fs
        if f.cve_ids
        == (() if scope == "source_only" else (A, B) if scope == "joint" else (A,))
    )
    assert target.recommended_actions == text and target.action.value == "none"
    if scope == "foreign":
        other = next(f for f in fs if f.cve_ids == (B,))
        assert other.action.value == "monitor" and text not in other.recommended_actions


UNKNOWN = [
    "Example Gateway appliances must be configured as an Identity Provider.",
    "Users should configure Example Gateway appliances as an Identity Provider.",
    "To be vulnerable, unknown arbitrary machines must be configured as an Identity Provider.",
    "To be vulnerable, Example Gateway appliances must be configured as a Domain Controller.",
    "To be vulnerable, Example Gateway appliances must have been configured as an Identity Provider.",
    "To be vulnerable, Example Gateway appliances must be configured as an Identity Provider and unknown assumptions hold.",
    "The infrastructure behind Example should be viewed casually as a list of domains to block.",
    "The infrastructure behind Example should be viewed simply simply as a list of domains to block.",
    "The infrastructure behind Example should have been viewed as a list of domains to block.",
    "The infrastructure behind Example should be viewed as an arbitrary opaque outcome.",
    "The unclassified object should be viewed as a list of domains to block.",
    "The infrastructure behind Example should be viewed as a list of domains to block and unknown statements apply.",
]


@pytest.mark.parametrize("text", UNKNOWN)
def test_unknown_required_context_or_guidance_preserves_all_artifacts(
    monkeypatch, tmp_path, text
):
    pipeline(monkeypatch, tmp_path, text, None)

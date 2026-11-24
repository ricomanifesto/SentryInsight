"""Bounded informed repair: one stubbed model, the real validation pipeline.

Each historical failure signature is reproduced in a draft and driven through
the repair path. The model is a stub; nothing reaches the network.
"""

from __future__ import annotations

import asyncio
import json

import httpx
import pytest

from src.control_plane.projection import projection_request
from src.control_plane.run_snapshot import build_run_snapshot
from src.core import report_repair
from src.core.attempt_budget import AttemptBudgetError
from src.core.exploitation_prompt import (
    ANALYSIS_SYSTEM_PROMPT,
    build_exploitation_prompt,
)
from src.core.failure_receipt import MAX_BYTES, make_receipt, validate_receipt
from src.core.openrouter_client import (
    OpenRouterClient,
    OpenRouterError,
    OpenRouterOutputLimitExceeded,
)
from src.core.repair_budget import (
    AdmissionRepairBudget,
    MemoryRepairBudget,
    RepairBudgetError,
    RepairSlotAttemptBudget,
)
from src.core.report_repair import (
    InsufficientValidFindingsError,
    validate_and_repair_report,
)
from src.core.reporting import reporting_key, serialize_reporting_catalog
from src.core.source_coverage import coverage_markdown, source_disposition
from src.core.source_review import PLAN_KEY, prepare_source_review
from src.core.version_references import PROTOCOL_KEY, PROTOCOL_VERSION
from src.core.version_state import ABSENT
from scripts.export_failure_receipt import format_attempts_summary

MODEL = "openrouter/nvidia/nemotron-3.5-super-vl:free"
ORIGINAL_SHA = "b" * 64
SECRET = "sk-or-secret-marker-0000"


def source(content: str, suffix: str) -> dict:
    return {
        "title": f"Synthetic advisory {suffix}",
        "source": "Synthetic publisher",
        "link": f"https://example.test/{suffix}",
        "content": content,
        "content_kind": "article",
        "source_links": [f"https://vendor.test/{suffix}"],
    }


SOURCES = [
    ("A gateway service advisory names GATEWAY_ONLY_MARKER.", "one"),
    ("A proxy service advisory names PROXY_ONLY_MARKER.", "two"),
    ("A router service advisory names ROUTER_ONLY_MARKER.", "three"),
    ("A switch service advisory names SWITCH_ONLY_MARKER.", "four"),
]
TITLES = ["Gateway campaign", "Proxy campaign", "Router campaign", "Switch campaign"]


def finding(title: str, key: str, **changes: str | None) -> str:
    fields: dict[str, str | None] = {
        "Description": f"A {title.lower()} described by the supplied reporting.",
        "Severity": "unknown",
        "Exploitation Status": "unknown",
        "Action": "monitor",
        "Reporting": key,
        "Affected Versions": ABSENT,
        "Exceptions": ABSENT,
        "Recommended Actions": ABSENT,
        "Vendor Links": ABSENT,
    }
    fields.update(changes)
    lines = "".join(f"- **{k}**: {v}\n" for k, v in fields.items() if v is not None)
    return f"### {title}\n{lines}\n"


def draft(findings: list[str], *, attack: str = "- Review the reporting.") -> str:
    return (
        "# Exploitation Report\n\n## Executive Summary\n\n"
        "The supplied reporting describes campaigns. Exploitation status is unknown.\n\n"
        "Review the source details before choosing a response.\n\n"
        "## Active Exploitation Details\n\n"
        + "".join(findings)
        + "## Affected Systems and Products\n\n"
        "- Review the reporting for system details.\n\n"
        f"## Attack Vectors and Techniques\n\n{attack}\n\n"
        "## Threat Actor Activities\n\n"
        "- The reported campaigns require further investigation.\n"
        "- Review the supplied reporting before assigning an actor.\n"
    )


def world(count: int = 2, contents: list[str] | None = None):
    articles = [
        source(contents[i] if contents else SOURCES[i][0], SOURCES[i][1])
        for i in range(count)
    ]
    plan = prepare_source_review(articles)
    # Keys in input order, so finding N cites source N.
    keys = [reporting_key(article["link"]) for article in articles]
    assert set(keys) == set(plan.eligible_keys)
    results = {
        PLAN_KEY: plan.packet,
        "reporting_sources": serialize_reporting_catalog(plan.catalog),
        "reporting_metadata_cves": {
            row["key"]: row["metadata_cves"] for row in plan.packet["sources"]
        },
        PROTOCOL_KEY: PROTOCOL_VERSION,
        "date": "2026-11-02",
        "generated_at": "2026-11-02T12:00:00Z",
        "request_metadata": {
            "state": "response_received",
            "request_sha256": ORIGINAL_SHA,
        },
        "repair_eligible": True,
    }
    return plan, keys, results


def config(**analysis) -> dict:
    return {
        "analysis": {
            "model": MODEL,
            "max_tokens": 96000,
            "max_input_tokens": 200000,
            **analysis,
        }
    }


class StubModel:
    """Scripted repair responses; records every request it receives."""

    def __init__(self, responses):
        self.responses = list(responses)
        self.calls: list[dict] = []
        self.built: list[dict] = []

    async def generate(self, *, system_prompt, user_prompt, model=None, title=""):
        self.calls.append({"system_prompt": system_prompt, "user_prompt": user_prompt})
        response = (
            self.responses.pop(0) if len(self.responses) > 1 else self.responses[0]
        )
        if isinstance(response, BaseException):
            raise response
        return response


def install(monkeypatch, responses) -> StubModel:
    stub = StubModel(responses)

    def build(**kwargs):
        stub.built.append(kwargs)
        return stub

    monkeypatch.setattr(report_repair, "build_repair_client", build)
    monkeypatch.setenv("OPENROUTER_API_KEY", SECRET)
    return stub


def run(results, report, plan, *, advisory=False, budget=None, **analysis):
    return asyncio.run(
        validate_and_repair_report(
            analysis_results={**results, "exploitation_report": report},
            plan=plan,
            config=config(**analysis),
            advisory=advisory,
            repair_enabled=True,
            repair_budget=budget or MemoryRepairBudget(),
        )
    )


def outcomes(outcome) -> list[tuple]:
    return [
        (line["kind"], line["failure_class"], line["rule"], line["outcome"])
        for line in outcome.attempts
    ]


def two_findings(keys, **changes):
    return draft([finding(TITLES[0], keys[0]), finding(TITLES[1], keys[1], **changes)])


def test_valid_draft_records_one_attempt_and_sends_nothing(monkeypatch):
    plan, keys, results = world()
    stub = install(monkeypatch, ["unused"])
    outcome = run(results, draft([finding(TITLES[0], keys[0])]), plan)
    assert outcome.error is None and outcome.artifact is not None
    assert outcome.attempts == (
        {
            "attempt": 1,
            "kind": "original",
            "failure_class": None,
            "rule": None,
            "finding_index": None,
            "field": None,
            "outcome": "validated",
            "request_sha256": ORIGINAL_SHA,
        },
    )
    assert stub.calls == []


# --- Historical failure signatures (one fixture per logged signature) --------


def test_signature_invalid_version_reference_field_repairs_only_that_finding(
    monkeypatch,
):
    plan, keys, results = world()
    bad = finding(TITLES[1], keys[1]).replace(
        f"- **Affected Versions**: {ABSENT}\n",
        f"- **Affected Versions**: {ABSENT}\n- **Affected Versions**: Proxy 2.1\n",
    )
    stub = install(monkeypatch, [finding(TITLES[1], keys[1])])
    outcome = run(results, draft([finding(TITLES[0], keys[0]), bad]), plan)
    assert outcome.error is None and outcome.dropped_findings == ()
    assert outcomes(outcome) == [
        ("original", "repairable", "invalid_version_reference_field", "rejected"),
        ("repair_finding", "repairable", "invalid_version_reference_field", "repaired"),
    ]
    assert [line["finding_index"] for line in outcome.attempts] == [2, 2]
    [call] = stub.calls
    prompt = call["user_prompt"]
    assert "Rule: invalid_version_reference_field" in prompt
    assert "Field: Affected Versions" in prompt
    assert "- **Affected Versions**: Proxy 2.1" in prompt  # the offending value
    assert "affected_versions_field" in prompt  # fixed valid-value guidance
    # Only the cited source's original material; never another source or a secret.
    assert "PROXY_ONLY_MARKER" in prompt and "GATEWAY_ONLY_MARKER" not in prompt
    assert keys[0] not in prompt and SECRET not in prompt
    assert "Gateway campaign" not in prompt
    repair_sha = outcome.attempts[1]["request_sha256"]
    assert repair_sha and repair_sha != ORIGINAL_SHA


@pytest.mark.parametrize(
    "rule,value",
    [
        ("unsupported_vendor_link", "https://unrelated.example/advisory"),
        ("invalid_vendor_link", "[Advisory](https://vendor.test/two)"),
    ],
)
def test_signature_vendor_link_rejections_repair_the_finding(monkeypatch, rule, value):
    plan, keys, results = world()
    stub = install(monkeypatch, [finding(TITLES[1], keys[1])])
    outcome = run(results, two_findings(keys, **{"Vendor Links": value}), plan)
    assert outcomes(outcome) == [
        ("original", "repairable", rule, "rejected"),
        ("repair_finding", "repairable", rule, "repaired"),
    ]
    assert outcome.attempts[0]["field"] == "Vendor Links"
    prompt = stub.calls[0]["user_prompt"]
    assert value in prompt
    assert "https://vendor.test/two" in prompt
    assert "https://vendor.test/one" not in prompt


def test_signature_malformed_markdown_inside_a_finding_repairs_that_finding(
    monkeypatch,
):
    plan, keys, results = world()
    bad = finding(TITLES[1], keys[1]).replace(
        "- **Severity**", "- **Impact**\n- **Severity**"
    )
    stub = install(monkeypatch, [finding(TITLES[1], keys[1])])
    outcome = run(
        results, draft([finding(TITLES[0], keys[0]), bad]), plan, advisory=True
    )
    assert outcomes(outcome) == [
        ("original", "repairable", "malformed_markdown", "rejected"),
        ("repair_finding", "repairable", "malformed_markdown", "repaired"),
    ]
    assert outcome.attempts[0]["finding_index"] == 2
    assert "- **Impact**" in stub.calls[0]["user_prompt"]


def test_signature_malformed_markdown_outside_findings_repairs_one_section(
    monkeypatch,
):
    plan, keys, results = world()
    fixed = "## Attack Vectors and Techniques\n\n- **Vector**: Review the reporting."
    stub = install(monkeypatch, [fixed])
    report = draft([finding(TITLES[0], keys[0])], attack="- **Vector**")
    outcome = run(results, report, plan, advisory=True)
    assert outcomes(outcome) == [
        ("original", "repairable", "malformed_markdown", "rejected"),
        ("repair_section", "repairable", "malformed_markdown", "repaired"),
    ]
    assert "Section: ## Attack Vectors and Techniques" in stub.calls[0]["user_prompt"]
    assert "- **Vector**: Review the reporting." in outcome.final_report


def _duplicated(report: str) -> str:
    return report.replace(
        "## Affected Systems", "## Executive Summary\n\nAgain.\n\n## Affected Systems"
    )


def test_signature_duplicate_section_regenerates_the_report_once(monkeypatch):
    plan, keys, results = world()
    good = draft([finding(TITLES[0], keys[0])])
    stub = install(monkeypatch, [good])
    outcome = run(results, _duplicated(good), plan, advisory=True)
    assert outcomes(outcome) == [
        ("original", "repairable", "duplicate_section", "rejected"),
        ("repair_report", "repairable", "duplicate_section", "repaired"),
    ]
    [call] = stub.calls
    assert call["system_prompt"] == ANALYSIS_SYSTEM_PROMPT
    assert call["user_prompt"].endswith(build_exploitation_prompt(plan))
    assert "Rule: duplicate_section" in call["user_prompt"]
    assert stub.built[0]["max_tokens"] == 96000


def test_duplicate_section_gets_at_most_one_regeneration(monkeypatch):
    plan, keys, results = world()
    duplicated = _duplicated(draft([finding(TITLES[0], keys[0])]))
    stub = install(monkeypatch, [duplicated])
    outcome = run(results, duplicated, plan, advisory=True)
    assert len(stub.calls) == 1
    assert outcome.error is not None and outcome.artifact is None
    assert outcomes(outcome)[-1] == (
        "repair_report",
        "repairable",
        "duplicate_section",
        "rejected",
    )


def test_signature_missing_expected_cves_regenerates_the_report(monkeypatch):
    cve = "CVE-2026-1234"
    contents = [
        SOURCES[0][0],
        f"Attackers are actively exploiting {cve} in a proxy service.",
    ]
    plan, keys, results = world(2, contents)
    stub = install(monkeypatch, [draft([finding(TITLES[0], keys[0])])])
    outcome = run(results, draft([finding(TITLES[0], keys[0])]), plan)
    assert outcomes(outcome)[0] == (
        "original",
        "repairable",
        "missing_expected_cves",
        "rejected",
    )
    assert outcome.attempts[1]["kind"] == "repair_report"
    assert len(stub.calls) == 1


@pytest.mark.parametrize(
    "rule,field,value",
    [
        ("invalid_cve_ids", "CVE IDs", "Proxy product"),
        ("invalid_triage_value", "Severity", "urgent"),
    ],
)
def test_signature_artifact_reasons_repair_the_named_finding(
    monkeypatch, rule, field, value
):
    plan, keys, results = world()
    stub = install(monkeypatch, [finding(TITLES[1], keys[1])])
    outcome = run(results, two_findings(keys, **{field: value}), plan)
    assert outcomes(outcome) == [
        ("original", "repairable", rule, "rejected"),
        ("repair_finding", "repairable", rule, "repaired"),
    ]
    assert outcome.attempts[0]["field"] == field
    assert outcome.attempts[0]["finding_index"] == 2
    assert f"- **{field}**: {value}" in stub.calls[0]["user_prompt"]


def test_signature_unspecified_artifact_rejection_and_output_limit_fail_fast():
    from src.core.failure_classifier import classify_failure, classify_rule
    from src.core.report_artifact import ReportArtifactError

    unspecified = classify_failure(error=ReportArtifactError("rejected"))
    assert (unspecified.failure_class, unspecified.rule) == (
        "fail_fast",
        "artifact_rejected",
    )
    limit = classify_failure(error=OpenRouterOutputLimitExceeded("limit"))
    assert (limit.failure_class, limit.rule) == (
        "fail_fast",
        "model_output_limit_exceeded",
    )
    identity = classify_rule("reporting_identity_rejected")
    assert identity.failure_class == "fail_fast"


# --- Caps ---------------------------------------------------------------------


def test_finding_gets_three_rounds_then_is_dropped_and_disclosed(monkeypatch):
    plan, keys, results = world()
    still_bad = finding(TITLES[1], keys[1], Severity="urgent")
    stub = install(monkeypatch, [still_bad])
    outcome = run(results, draft([finding(TITLES[0], keys[0]), still_bad]), plan)
    assert len(stub.calls) == 3
    assert outcome.error is None and outcome.candidate is not None
    assert [line["outcome"] for line in outcome.attempts] == [
        "rejected",
        "rejected",
        "rejected",
        "rejected",
        "dropped_and_validated",
    ]
    assert outcome.dropped_findings == (
        {
            "finding_index": 2,
            "rule": "invalid_triage_value",
            "field": "Severity",
            "repair_attempts": 3,
            "source_keys": [keys[1]],
        },
    )
    coverage = outcome.candidate.coverage
    assert coverage["dropped_findings"] == list(outcome.dropped_findings)
    assert coverage["cited_source_keys"] == [keys[0]]
    row = next(r for r in coverage["plan"]["sources"] if r["key"] == keys[1])
    disposition = source_disposition(row, coverage["cited_source_keys"])
    assert disposition == "Eligible input; not represented"
    assert "Degraded publication" in coverage_markdown(coverage)
    assert "Proxy campaign" not in outcome.candidate.report


def test_run_cap_is_six_repair_requests_across_findings(monkeypatch):
    plan, keys, results = world(4)
    bad = [finding(TITLES[i], keys[i], Severity="urgent") for i in (1, 2, 3)]
    stub = install(monkeypatch, [bad[0]])
    budget = MemoryRepairBudget()
    outcome = run(
        results, draft([finding(TITLES[0], keys[0]), *bad]), plan, budget=budget
    )
    assert len(stub.calls) == 6 and budget.slot == 6
    assert [e["repair_attempts"] for e in outcome.dropped_findings] == [3, 3, 0]
    assert [e["finding_index"] for e in outcome.dropped_findings] == [2, 3, 4]
    assert outcome.error is None and outcome.artifact is not None
    assert len(outcome.artifact.findings) == 1


def test_memory_repair_budget_refuses_a_seventh_slot_and_overlap():
    budget = MemoryRepairBudget()

    async def exercise():
        for digit in "123456":
            slot = await budget.reserve(digit * 64)
            with pytest.raises(RepairBudgetError):
                await budget.reserve("9" * 64)
            await budget.finish(slot, "response_received")
        with pytest.raises(RepairBudgetError):
            await budget.reserve("7" * 64)

    asyncio.run(exercise())
    assert [entry["request_sha256"][0] for entry in budget.history] == list("123456")
    with pytest.raises(RepairBudgetError):
        MemoryRepairBudget(max_repairs=7)


def test_transient_repair_failure_spends_one_round_then_retries(monkeypatch):
    plan, keys, results = world()
    transient = OpenRouterError("unavailable", retryable=True, http_status=503)
    stub = install(monkeypatch, [transient, finding(TITLES[1], keys[1])])
    budget = MemoryRepairBudget()
    outcome = run(results, two_findings(keys, Severity="urgent"), plan, budget=budget)
    assert len(stub.calls) == 2 and outcome.error is None
    assert [h["disposition"] for h in budget.history] == [
        "retryable_rejection",
        "response_received",
    ]
    assert outcomes(outcome)[1] == (
        "repair_finding",
        "transient",
        "model_provider_unavailable",
        "repair_request_failed",
    )


def test_fail_fast_repair_failure_stops_repair(monkeypatch):
    plan, keys, results = world()
    stub = install(monkeypatch, [OpenRouterOutputLimitExceeded("limit")])
    outcome = run(results, two_findings(keys, Severity="urgent"), plan)
    assert len(stub.calls) == 1 and outcome.artifact is None
    assert outcomes(outcome)[-1][1:] == (
        "fail_fast",
        "model_output_limit_exceeded",
        "repair_request_failed",
    )


# --- The original episode is never reused ------------------------------------


def test_repair_budget_uses_separate_admission_commands(monkeypatch):
    budget = AdmissionRepairBudget(
        key="run:1", run_id="1", revision="a" * 40, run_attempt="1"
    )
    calls = []

    def invoke(command, arguments):
        calls.append(command)
        if command == "repair-reserve":
            return {
                "slot": 1,
                "max_repairs": 6,
                "request_sha256": "c" * 64,
                "token": "d" * 32,
            }
        return {"recorded": True}

    monkeypatch.setattr(budget, "_invoke", invoke)

    async def exercise():
        slot = await budget.reserve("c" * 64)
        await budget.finish(slot, "response_received")

    asyncio.run(exercise())
    assert calls == ["repair-reserve", "repair-finish"]


def test_openrouter_repair_send_binds_one_slot_to_its_own_digest():
    from src.core.opencode_client import parse_model_selection

    budget = MemoryRepairBudget()
    body = {
        "model": "nvidia/nemotron-3.5-super-vl:free",
        "choices": [{"message": {"content": "### Fixed"}, "finish_reason": "stop"}],
    }
    client = OpenRouterClient(
        api_key="test-key",
        max_tokens=1000,
        max_attempts=1,
        output_limit_recovery=False,
        transport=httpx.MockTransport(lambda request: httpx.Response(200, json=body)),
        attempt_budget=RepairSlotAttemptBudget(budget),
    )
    selection = parse_model_selection(MODEL)

    async def send():
        return await client.generate(
            system_prompt="s", user_prompt="u", model=selection, title="t"
        )

    asyncio.run(send())
    [entry] = budget.history
    assert entry["request_sha256"] == client.last_request["request_sha256"]
    assert entry["request_sha256"] != ORIGINAL_SHA
    assert entry["disposition"] == "response_received"
    # One client, one slot: a second send through the same adapter is refused.
    with pytest.raises(AttemptBudgetError):
        asyncio.run(send())


# --- Safety, identity and integrity always block -----------------------------

UNSAFE = "See [x](javascript:alert(1))."


def test_active_content_blocks_without_repair_or_drop(monkeypatch):
    plan, keys, results = world()
    stub = install(monkeypatch, ["unused"])
    outcome = run(results, two_findings(keys, Description=UNSAFE), plan, advisory=True)
    assert stub.calls == [] and outcome.dropped_findings == ()
    assert outcome.artifact is None
    assert outcomes(outcome)[0][1] == "fail_fast"


def test_unknown_reporting_identity_blocks_without_repair(monkeypatch):
    plan, keys, results = world()
    stub = install(monkeypatch, ["unused"])
    report = draft(
        [finding(TITLES[0], keys[0]), finding(TITLES[1], "source-000000000000")]
    )
    outcome = run(results, report, plan, advisory=True)
    assert stub.calls == [] and outcome.artifact is None
    assert outcomes(outcome) == [
        ("original", "fail_fast", "unknown_reporting_source", "rejected")
    ]


def test_repair_that_introduces_active_content_is_blocked(monkeypatch):
    plan, keys, results = world()
    stub = install(monkeypatch, [finding(TITLES[1], keys[1], Description=UNSAFE)])
    outcome = run(results, two_findings(keys, Severity="urgent"), plan)
    assert len(stub.calls) == 1 and outcome.artifact is None
    assert outcome.dropped_findings == ()
    assert outcome.attempts[-1]["failure_class"] == "fail_fast"


def test_repair_may_not_cite_a_source_the_finding_did_not_cite(monkeypatch):
    plan, keys, results = world()
    widened = finding(TITLES[1], f"{keys[1]}, {keys[0]}")
    stub = install(monkeypatch, [widened, finding(TITLES[1], keys[1])])
    outcome = run(results, two_findings(keys, Severity="urgent"), plan)
    assert len(stub.calls) == 2 and outcome.error is None
    assert [line["outcome"] for line in outcome.attempts[1:]] == [
        "splice_rejected",
        "repaired",
    ]


# --- Degradation and min_findings --------------------------------------------


def test_degradation_below_min_findings_blocks_publication(monkeypatch):
    plan, keys, results = world()
    still_bad = finding(TITLES[1], keys[1], Severity="urgent")
    install(monkeypatch, [still_bad])
    report = draft([finding(TITLES[0], keys[0]), still_bad])
    outcome = run(results, report, plan, min_findings=2)
    assert isinstance(outcome.error, InsufficientValidFindingsError)
    assert (outcome.error.remaining, outcome.error.required) == (1, 2)
    assert outcome.attempts[-1]["outcome"] == "blocked_min_findings"
    assert outcome.attempts[-1]["rule"] == "insufficient_valid_findings"


def test_dropping_the_only_finding_never_publishes_an_empty_report(monkeypatch):
    plan, keys, results = world(1)
    still_bad = finding(TITLES[0], keys[0], Severity="urgent")
    install(monkeypatch, [still_bad])
    outcome = run(results, draft([still_bad]), plan)
    assert isinstance(outcome.error, InsufficientValidFindingsError)
    assert outcome.artifact is None


def test_default_min_findings_is_one_and_invalid_values_fall_back():
    from pathlib import Path

    from src.core.report_repair import resolve_min_findings

    assert resolve_min_findings({}) == 1
    assert resolve_min_findings({"analysis": {"min_findings": 3}}) == 3
    for invalid in (0, -1, "2", 2.0, True, 51):
        assert resolve_min_findings({"analysis": {"min_findings": invalid}}) == 1
    shipped = json.loads(Path("config/config.json").read_text())
    assert shipped["analysis"]["min_findings"] == 1


# --- Paid verification and disabled repair -----------------------------------


def test_paid_verification_disables_repair(monkeypatch):
    plan, keys, results = world()
    stub = install(monkeypatch, [finding(TITLES[1], keys[1])])
    monkeypatch.setattr(report_repair, "active_verification", lambda: object())
    outcome = run(results, two_findings(keys, Severity="urgent"), plan)
    assert stub.calls == [] and outcome.artifact is None
    assert len(outcome.attempts) == 1


def test_repair_client_refuses_paid_verification(monkeypatch):
    from src.core import model_client

    monkeypatch.setattr(model_client, "active_verification", lambda: object())
    with pytest.raises(RepairBudgetError):
        model_client.build_repair_client(
            repair_budget=MemoryRepairBudget(), timeout=10.0, max_tokens=100
        )


def test_repair_disabled_sends_nothing(monkeypatch):
    plan, keys, results = world()
    stub = install(monkeypatch, [finding(TITLES[1], keys[1])])
    outcome = asyncio.run(
        validate_and_repair_report(
            analysis_results={
                **results,
                "exploitation_report": two_findings(keys, Severity="urgent"),
            },
            plan=plan,
            config=config(),
            advisory=False,
            repair_enabled=False,
        )
    )
    assert stub.calls == [] and outcome.artifact is None


# --- Receipts, step summary and report history -------------------------------


def _degraded_outcome(monkeypatch):
    plan, keys, results = world()
    still_bad = finding(TITLES[1], keys[1], Severity="urgent")
    install(monkeypatch, [still_bad])
    return run(results, draft([finding(TITLES[0], keys[0]), still_bad]), plan)


def test_receipt_lines_are_bounded_labels_without_text(monkeypatch):
    outcome = _degraded_outcome(monkeypatch)
    state = {
        "status": "completed",
        "report_generated": True,
        "repair_attempts": list(outcome.attempts),
        "dropped_findings": list(outcome.dropped_findings),
    }
    receipt = make_receipt(state, environ={})
    assert validate_receipt(receipt) == receipt
    assert len(receipt["attempts"]) == 5
    assert set(receipt["attempts"][0]) == {
        "attempt",
        "kind",
        "failure_class",
        "rule",
        "finding_index",
        "field",
        "outcome",
        "request_sha256",
    }
    assert receipt["dropped_findings"] == [
        {
            "finding_index": 2,
            "rule": "invalid_triage_value",
            "field": "Severity",
            "repair_attempts": 3,
        }
    ]
    encoded = json.dumps(receipt)
    for text in (
        "Proxy campaign",
        "PROXY_ONLY_MARKER",
        "urgent",
        SECRET,
        "example.test",
    ):
        assert text not in encoded
    # Extra keys and free text never survive sanitization.
    forged = {**state, "repair_attempts": [{**outcome.attempts[0], "excerpt": "x"}]}
    assert "excerpt" not in json.dumps(make_receipt(forged, environ={}))
    unsafe = {
        **state,
        "repair_attempts": [{**outcome.attempts[0], "rule": "Free text"}],
    }
    assert make_receipt(unsafe, environ={})["attempts"][0]["rule"] is None


def test_receipt_stays_within_its_size_bound_at_maximum_lines():
    line = {
        "attempt": 1,
        "kind": "drop_finding",
        "failure_class": "repairable",
        "rule": "invalid_version_reference_field",
        "finding_index": 999999,
        "field": "Affected Versions Status",
        "outcome": "dropped_revalidation_failed",
        "request_sha256": "f" * 64,
    }
    attempts = [{**line, "attempt": i} for i in range(1, 30)]
    dropped = [
        {
            "finding_index": i,
            "rule": "invalid_version_reference_field",
            "field": "Affected Versions",
            "repair_attempts": 3,
        }
        for i in range(1, 30)
    ]
    receipt = make_receipt(
        {"status": "failed", "repair_attempts": attempts, "dropped_findings": dropped},
        environ={},
    )
    assert len(receipt["attempts"]) == 16 and len(receipt["dropped_findings"]) == 8
    assert len(json.dumps(receipt).encode()) < MAX_BYTES


def test_step_summary_and_history_projection_carry_attempt_lines(monkeypatch):
    outcome = _degraded_outcome(monkeypatch)
    state = {
        "status": "completed",
        "repair_attempts": list(outcome.attempts),
        "dropped_findings": list(outcome.dropped_findings),
    }
    receipt = make_receipt(state, environ={})
    summary = format_attempts_summary(receipt)
    assert (
        "| 2 | `repair_finding` | `repairable` | `invalid_triage_value` | 2 |"
        in summary
    )
    assert "Finding #2: `invalid_triage_value` on `Severity` after 3" in summary
    snapshot = build_run_snapshot(state)
    assert snapshot["attempts"] == receipt["attempts"]
    common = dict(
        pipeline="reports",
        policy_id="production",
        source_revision="actions:1:1",
        snapshot=b"{}",
        files=None,
        execution_id="actions-run-1-1",
        source_commit=None,
        outcome="failed",
        reason="report_validation",
        source_outcomes=None,
    )
    request = projection_request(**common, attempts=snapshot["attempts"])
    assert request["run"]["attempts"] == snapshot["attempts"]
    assert "attempts" not in projection_request(**common)["run"]


# --- Workflow wiring ---------------------------------------------------------


def _workflow_state(tmp_path, monkeypatch, *, eligible: bool):
    from test_review_pipeline import load_modules, state_for

    _, workflow = load_modules()
    articles = [source(SOURCES[i][0], SOURCES[i][1]) for i in range(2)]
    monkeypatch.setattr(workflow, "filter_exploitation_articles", lambda items: items)
    state = asyncio.run(workflow.filter_articles(state_for(tmp_path, articles)))
    state["config"]["analysis"] = {"model": MODEL, "max_tokens": 96000}
    plan, keys, results = world()
    results["exploitation_report"] = two_findings(keys, Severity="urgent")
    if not eligible:
        results.pop("repair_eligible")
    state["analysis_results"] = results
    return workflow, state, keys


def test_workflow_publishes_a_repaired_report_and_records_attempts(
    tmp_path, monkeypatch
):
    workflow, state, keys = _workflow_state(tmp_path, monkeypatch, eligible=True)
    stub = install(monkeypatch, [finding(TITLES[1], keys[1])])
    result = asyncio.run(workflow.generate_report(state))
    assert result["status"] != "failed", result.get("failure")
    assert result["report_generated"] is True
    assert len(stub.calls) == 1
    assert [line["outcome"] for line in result["repair_attempts"]] == [
        "rejected",
        "repaired",
    ]
    receipt = make_receipt(result, environ={})
    assert [line["kind"] for line in receipt["attempts"]] == [
        "original",
        "repair_finding",
    ]


def test_workflow_without_an_eligible_original_request_never_repairs(
    tmp_path, monkeypatch
):
    workflow, state, keys = _workflow_state(tmp_path, monkeypatch, eligible=False)
    stub = install(monkeypatch, [finding(TITLES[1], keys[1])])
    result = asyncio.run(workflow.generate_report(state))
    assert result["status"] == "failed" and stub.calls == []
    assert result["repair_attempts"][0]["outcome"] == "rejected"


def test_unreachable_model_never_causes_a_drop(monkeypatch):
    plan, keys, results = world()
    transient = OpenRouterError("unavailable", retryable=True, http_status=503)
    stub = install(monkeypatch, [transient])
    outcome = run(results, two_findings(keys, Severity="urgent"), plan)
    assert len(stub.calls) == 3
    assert outcome.dropped_findings == () and outcome.artifact is None
    assert outcome.error is not None
    assert not isinstance(outcome.error, InsufficientValidFindingsError)


def test_without_the_production_client_no_repair_is_sent(monkeypatch):
    from src.core import model_client

    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    with pytest.raises(RepairBudgetError):
        model_client.build_repair_client(
            repair_budget=MemoryRepairBudget(), timeout=10.0, max_tokens=100
        )
    plan, keys, results = world()
    outcome = run(results, two_findings(keys, Severity="urgent"), plan)
    assert outcome.artifact is None and outcome.dropped_findings == ()
    assert outcome.attempts[-1]["outcome"] == "budget_refused"

"""Failure/restart oracles use simulated transport, never an inference endpoint."""

import asyncio
from pathlib import Path
import subprocess

import httpx
import pytest

from src.core.attempt_budget import (
    AdmissionAttemptBudget,
    AttemptBudgetError,
    MemoryAttemptBudget,
)
from src.core.failure_receipt import (
    FailureReceiptError,
    finish_receipt,
    make_receipt,
    read_receipt,
    record_request,
    validate_receipt,
    write_receipt,
)
from src.core.openrouter_client import OpenRouterClient, OpenRouterError
from src.core.opencode_client import parse_model_selection
from src.core.retry_policy import retry_decision

MODEL = parse_model_selection("openrouter/nvidia/nemotron-3-ultra-550b-a55b:free")
KWARGS = {
    "model": MODEL,
    "system_prompt": "private-system-marker",
    "user_prompt": "private-input-marker",
}


def success():
    return httpx.Response(
        200,
        json={
            "model": MODEL.model_id,
            "choices": [
                {
                    "finish_reason": "stop",
                    "message": {"content": "private-answer-marker"},
                }
            ],
        },
    )


def rejection(code=503, **extra):
    return httpx.Response(
        code,
        json={"error": {"code": code, "message": "private-provider-marker"}, **extra},
    )


@pytest.mark.parametrize(
    "response",
    [
        httpx.ReadTimeout("private-read-marker"),
        httpx.WriteTimeout("private-write-marker"),
        httpx.RemoteProtocolError("private-protocol-marker"),
        httpx.Response(200, json={}),
        httpx.Response(503),
        rejection(503, usage={"cost": 0}),
        rejection(503, choices=[]),
    ],
)
def test_uncertain_or_conflicting_response_never_replays(response, caplog):
    calls = []
    budget = MemoryAttemptBudget()

    def handler(request):
        calls.append(request)
        if isinstance(response, Exception):
            raise response
        return response

    client = OpenRouterClient(
        api_key="private-key-marker",
        attempt_budget=budget,
        transport=httpx.MockTransport(handler),
    )
    with pytest.raises(OpenRouterError):
        asyncio.run(client.generate(**KWARGS))
    restarted = OpenRouterClient(
        api_key="private-key-marker",
        attempt_budget=budget,
        transport=httpx.MockTransport(handler),
    )
    with pytest.raises(AttemptBudgetError):
        asyncio.run(restarted.generate(**KWARGS))
    assert len(calls) == 1
    assert budget.disposition == "uncertain"
    assert "private-" not in caplog.text


def test_shared_budget_includes_initial_request_and_all_client_retries(monkeypatch):
    calls = []

    async def no_wait(_):
        pass

    monkeypatch.setattr(asyncio, "sleep", no_wait)
    budget = MemoryAttemptBudget()

    def handler(request):
        calls.append(request)
        return rejection()

    client = OpenRouterClient(
        api_key="test", attempt_budget=budget, transport=httpx.MockTransport(handler)
    )
    with pytest.raises(OpenRouterError):
        asyncio.run(client.generate(**KWARGS))
    restarted = OpenRouterClient(
        api_key="test", attempt_budget=budget, transport=httpx.MockTransport(handler)
    )
    with pytest.raises(AttemptBudgetError):
        asyncio.run(restarted.generate(**KWARGS))
    assert len(calls) == 3
    assert client.last_request["attempts"] == 3


@pytest.mark.parametrize("mode", ["reservation", "snapshot", "completion"])
def test_persistence_failure_prevents_or_holds_network_work(mode):
    calls = []

    class BrokenBudget(MemoryAttemptBudget):
        async def reserve(self, request_sha256, limit):
            value = await super().reserve(request_sha256, limit)
            if mode == "reservation":
                raise AttemptBudgetError()
            return value

        async def finish(self, reservation, disposition, **kwargs):
            if mode == "completion":
                raise AttemptBudgetError()
            await super().finish(reservation, disposition, **kwargs)

    def snapshot(_):
        if mode == "snapshot":
            raise FailureReceiptError()

    def handler(request):
        calls.append(request)
        return success()

    budget = BrokenBudget()
    client = OpenRouterClient(
        api_key="test",
        attempt_budget=budget,
        on_request=snapshot,
        transport=httpx.MockTransport(handler),
    )
    with pytest.raises((AttemptBudgetError, FailureReceiptError)):
        asyncio.run(client.generate(**KWARGS))
    assert len(calls) == (1 if mode == "completion" else 0)
    assert budget.disposition == "reserved"
    with pytest.raises(AttemptBudgetError):
        asyncio.run(client.generate(**KWARGS))


def test_cancellation_keeps_request_uncertain():
    def cancel(_):
        raise asyncio.CancelledError()

    budget = MemoryAttemptBudget()
    client = OpenRouterClient(
        api_key="test", attempt_budget=budget, transport=httpx.MockTransport(cancel)
    )
    with pytest.raises(asyncio.CancelledError):
        asyncio.run(client.generate(**KWARGS))
    assert budget.disposition == "uncertain"
    with pytest.raises(AttemptBudgetError):
        asyncio.run(client.generate(**KWARGS))


def test_long_retry_after_does_not_become_immediate_after_restart():
    response = rejection(429)
    response.headers["Retry-After"] = "90"
    budget = MemoryAttemptBudget()
    client = OpenRouterClient(
        api_key="test",
        attempt_budget=budget,
        transport=httpx.MockTransport(lambda _: response),
    )
    with pytest.raises(OpenRouterError):
        asyncio.run(client.generate(**KWARGS))
    assert budget.disposition == "deferred_rejection"
    with pytest.raises(AttemptBudgetError):
        asyncio.run(client.generate(**KWARGS))


def test_admission_bridge_lost_ack_is_not_retried_or_logged(monkeypatch, caplog):
    calls = []

    def lost(*args, **kwargs):
        calls.append((args, kwargs))
        raise subprocess.TimeoutExpired(
            "private-command-marker", 60, output="private-output-marker"
        )

    monkeypatch.setattr(subprocess, "run", lost)
    monkeypatch.setenv("OPENROUTER_API_KEY", "private-key-marker")
    budget = AdmissionAttemptBudget(
        key="run:7", run_id="7", revision="a" * 40, run_attempt="1"
    )
    with pytest.raises(AttemptBudgetError) as error:
        asyncio.run(budget.reserve("b" * 64, 3))
    assert len(calls) == 1 and "OPENROUTER_API_KEY" not in calls[0][1]["env"]
    assert "private-" not in str(error.value) + caplog.text


def request_state(state="response_received"):
    return {
        "state": state,
        "attempts": 1,
        "limit": 3,
        "request_sha256": "b" * 64,
        "http_status": 200,
        "provider_code": None,
        "usage": None,
    }


@pytest.mark.parametrize(
    "stage,code,action",
    [
        ("finding_evidence", "affected_version_not_grounded", "repair_required"),
        ("version_references", "invalid_version_reference", "repair_required"),
        ("report_content", "missing_section", "repair_required"),
        ("analysis", "model_auth_rejected", "repair_required"),
        ("analysis", "model_output_limit_exceeded", "repair_required"),
        ("analysis", "input_budget_exceeded", "repair_required"),
        ("site_publication", "publication_failed", "recover_publication"),
        ("private-stage-marker", "private-code-marker", "reconcile"),
    ],
)
def test_failure_receipt_retains_only_fixed_reason_and_advisory_action(
    tmp_path, stage, code, action
):
    state = {
        "status": "failed",
        "failure": {
            "stage": stage,
            "codes": [code],
            "field": "private-field-marker",
            "message": "private-answer-marker",
            "traceback": "private-secret-marker",
        },
        "analysis_results": {
            "request_metadata": request_state(),
            "exploitation_report": "private-answer-marker",
        },
    }
    path = tmp_path / "receipt.json"
    write_receipt(path, make_receipt(state, environ={}))
    value = read_receipt(path)
    assert value["retry"]["action"] == action
    assert value["request"]["usage"] is None and value["report_generated"] is False
    assert "private-" not in path.read_text()
    assert path.stat().st_mode & 0o777 == 0o600


def test_crash_retains_initial_receipt_and_reserved_snapshot(tmp_path):
    path = tmp_path / "receipt.json"
    write_receipt(path, make_receipt(None, started=True, environ={}))
    record_request(path, request_state("reserved"))
    assert read_receipt(path)["retry"]["action"] == "reconcile"
    finish_receipt(path, None)
    value = read_receipt(path)
    assert value["status"] == "uncertain" and value["request"]["attempts"] == 1
    assert value["retry"]["action"] == "reconcile"


@pytest.mark.parametrize(
    "mutation", ["extra", "bool", "nan", "contradiction", "dynamic_code"]
)
def test_receipt_export_refuses_forged_or_invalid_metadata(mutation):
    receipt = make_receipt({"status": "failed"}, request=request_state(), environ={})
    if mutation == "extra":
        receipt["answer"] = "private-answer-marker"
    elif mutation == "bool":
        receipt["schema_version"] = True
    elif mutation == "nan":
        receipt["request"]["usage"] = {"cost": float("nan")}
    elif mutation == "contradiction":
        receipt["retry"]["action"] = "retry_after"
    else:
        receipt["diagnostic"]["codes"] = ["private-code-marker"]
    with pytest.raises((FailureReceiptError, ValueError)):
        validate_receipt(receipt)


@pytest.mark.parametrize("kind", ["symlink", "large", "permissions"])
def test_read_receipt_refuses_unsafe_files(tmp_path, kind):
    path = tmp_path / "receipt.json"
    write_receipt(path, make_receipt(None, environ={}))
    if kind == "large":
        path.write_bytes(b"x" * 8193)
    elif kind == "permissions":
        path.chmod(0o644)
    else:
        target = tmp_path / "target"
        path.rename(target)
        path.symlink_to(target)
    with pytest.raises(FailureReceiptError):
        read_receipt(path)


@pytest.mark.parametrize("state", [None, {}, [], "private-marker"])
def test_unknown_decision_state_is_never_retried(state):
    assert retry_decision(state, attempts=1, limit=3)["action"] == "reconcile"


def test_workflow_uses_same_admission_and_separate_seven_day_artifact():
    workflow = Path(".github/workflows/generate-report.yml").read_text()
    assert "SENTRYINSIGHT_ATTEMPT_STORE: admission" in workflow
    assert (
        "SENTRYINSIGHT_ADMISSION_KEY: ${{ steps.admission.outputs.admission_key }}"
        in workflow
    )
    assert "scripts/export_failure_receipt.py" in workflow
    artifact = workflow.split(
        "- name: Retain bounded generation diagnostics for seven days", 1
    )[1].split("- name:", 1)[0]
    assert "retention-days: 7" in artifact and "outcome.json" in artifact
    assert "retention-days: 90" in workflow
    assert "readmit" not in artifact


def test_real_validation_failure_reaches_durable_receipt_and_preserves_last_good(
    tmp_path,
):
    from scripts.export_failure_receipt import main as export
    from src.core.source_review import prepare_source_review, digest, PLAN_KEY
    from test_generation_verification import articles
    from test_reviewed_report import prepared_result
    from test_workflow_guards import import_workflow_with_stubs
    from unittest.mock import patch

    inputs = articles()
    plan = prepare_source_review(inputs)
    result = prepared_result(inputs)
    result["exploitation_report"] = result["exploitation_report"].replace(
        "Not stated in supplied sources.", "Gateway before 99.0"
    )
    result["request_metadata"] = request_state()
    last_good = tmp_path / "index.md"
    last_good.write_text("last-good marker")
    state = {
        "status": "analyzed",
        "analysis_results": result,
        "filtered_articles": inputs,
        PLAN_KEY: plan.packet,
        "articles_fingerprint": digest(
            {"generation_schema": 5, "plan_id": plan.packet["plan_id"]}
        ),
        "config": {"output_path": str(last_good)},
    }
    rejected = asyncio.run(import_workflow_with_stubs().generate_report(state))
    assert rejected["status"] == "failed"
    path = tmp_path / "receipt.json"
    write_receipt(path, make_receipt(rejected, environ={}))
    value = read_receipt(path)
    assert value["diagnostic"]["stage"] == "version_references"
    assert value["diagnostic"]["codes"] == ["invalid_version_reference"]
    assert value["retry"]["action"] == "repair_required"
    assert last_good.read_text() == "last-good marker"
    assert "Gateway before" not in path.read_text()
    output = tmp_path / "export" / "outcome.json"
    with patch("sys.argv", ["export", "--source", str(path), "--output", str(output)]):
        assert export() == 0
    assert read_receipt(output) == value


@pytest.mark.parametrize("failure", [400, 402, 404, 413, 422, "wrong_model"])
def test_actual_permanent_provider_failure_advises_repair(failure):
    from src.core.analysis_errors import classify_analysis_error

    if failure == "wrong_model":
        payload = success().json()
        payload["model"] = "other/model"
        response = httpx.Response(200, json=payload)
    else:
        response = rejection(failure)
    calls = []

    def handler(request):
        calls.append(request)
        return response

    client = OpenRouterClient(api_key="test", transport=httpx.MockTransport(handler))
    with pytest.raises(OpenRouterError) as caught:
        asyncio.run(client.generate(**KWARGS))
    error_class, _ = classify_analysis_error(caught.value)
    state = {
        "status": "failed",
        "failure": {"stage": "analysis", "codes": ["analysis_failed", error_class]},
        "analysis_results": {"request_metadata": client.last_request},
    }
    receipt = make_receipt(state, environ={})
    assert receipt["request"]["state"] == "permanent_rejection"
    assert receipt["retry"]["action"] == "repair_required"
    if failure == "wrong_model":
        assert "model_identity_mismatch" in receipt["diagnostic"]["codes"]
    assert len(calls) == 1


@pytest.mark.parametrize(
    "fault,code,stage",
    [
        ("fingerprint", "source_review_fingerprint_mismatch", "source_review"),
        ("write_packet", "review_packet_write_failed", "source_review"),
        ("preflight_recovery", "publication_recovery_required", "site_publication"),
        (
            "publication_recovery_required",
            "publication_recovery_required",
            "site_publication",
        ),
        ("publication_rolled_back", "publication_rolled_back", "site_publication"),
        ("invalid_publication_stage", "invalid_publication_stage", "site_publication"),
        ("filesystem_error", "filesystem_error", "site_publication"),
    ],
)
def test_actual_workflow_failures_keep_fixed_reasons(
    tmp_path, monkeypatch, fault, code, stage
):
    from src.core.publication_transaction import PublicationError
    from test_review_pipeline import load_modules, state_for
    from test_reviewed_report import prepared_result
    from test_version_references import source

    _, workflow = load_modules()
    inputs = [source("A campaign advisory.", "good")]
    monkeypatch.setattr(workflow, "filter_exploitation_articles", lambda items: items)
    state = asyncio.run(workflow.filter_articles(state_for(tmp_path, inputs)))
    state["analysis_results"] = {
        **prepared_result(inputs),
        "request_metadata": request_state(),
    }
    last_good = tmp_path / "index.md"
    from src.core.reviewed_report import resolve_reviewed_analysis

    original = resolve_reviewed_analysis(prepared_result(inputs)).source
    last_good.write_text(original)

    def fail(*_):
        if fault in {"write_packet", "filesystem_error"}:
            raise OSError("private-filesystem-marker")
        raise PublicationError(code)

    if fault == "fingerprint":
        state["articles_fingerprint"] = "c" * 64
    elif fault == "write_packet":
        monkeypatch.setattr(workflow, "write_review_packet", fail)
    elif fault == "preflight_recovery":
        monkeypatch.setattr(workflow, "ensure_no_pending_publication", fail)
    else:
        monkeypatch.setattr(workflow, "promote_artifacts", fail)
    rejected = asyncio.run(workflow.generate_report(state))
    assert rejected["status"] == "failed"
    receipt = make_receipt(rejected, environ={})
    assert receipt["diagnostic"]["codes"] == [code]
    assert receipt["diagnostic"]["stage"] == stage
    if stage == "site_publication":
        assert receipt["retry"]["action"] == "recover_publication"
    assert last_good.read_text() == original
    assert "private-filesystem-marker" not in str(receipt)

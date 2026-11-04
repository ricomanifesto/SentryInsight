"""Fixed diagnostic evidence must never retain private child/provider text."""

import asyncio
from copy import deepcopy
import json

import httpx
import pytest

from scripts import verify_grc_workflow_once as trial
from scripts import verify_selected_models_once as base
from test_grc_full_trial import reply, run, streamed
import test_grc_full_trial as cases

layout = cases.layout
prepared = cases.prepared

SENTINEL = "PRIVATE_PROMPT_KEY_ANSWER_EXCEPTION_SENTINEL"


def assert_private(tmp_path, result, capsys):
    base.write_metadata(tmp_path / "trial.json", result)
    for path in tmp_path.rglob("*.json"):
        assert SENTINEL.encode() not in path.read_bytes()
    captured = capsys.readouterr()
    assert SENTINEL not in captured.out + captured.err


def failed_close(layout, *, invalid=False):
    value = reply(layout, 0)
    if invalid:
        value["usage"].pop("cost")
    response = streamed(value)
    original = response.aclose
    calls = []

    async def close():
        calls.append(True)
        if len(calls) > 1:
            raise RuntimeError(SENTINEL)
        await original()

    response.aclose = close
    return response


def test_fixed_diagnostic_contract_is_versioned_and_closed():
    assert trial.diagnostics.VERSION == 1
    assert trial.diagnostics.record(
        "analysis", "response_close", "unknown_failure"
    ) == {"stage": "analysis", "phase": "response_close", "code": "unknown_failure"}


@pytest.mark.parametrize("invalid", [False, True])
def test_response_close_evidence_and_dual_fault_primary_precedence(
    tmp_path, layout, prepared, capsys, invalid
):
    seen = []

    def handler(request):
        seen.append(request)
        return failed_close(layout, invalid=invalid)

    result = run(tmp_path, layout, prepared, handler, lambda: SENTINEL)
    primary = result["diagnostics"]["failure"]
    assert len(seen) == 1 and result["states"]["plan"] == "pending"
    assert primary["phase"] == ("response_validation" if invalid else "response_close")
    assert primary["code"] == ("response_refused" if invalid else "unknown_failure")
    assert (
        result["operations"][0]["usage"] is None
        if invalid
        else result["operations"][0]["usage"]["cost"] == 0.007
    )
    if invalid:
        assert result["diagnostics"]["secondary"][0]["phase"] == "response_close"
        assert result["diagnostics"]["last"]["phase"] == "response_close"
    assert_private(tmp_path, result, capsys)


@pytest.mark.parametrize(
    "boundary",
    [
        "derive_worker",
        "derived_body_validation",
        "plan_binding",
        "replay_worker",
        "host_validation",
    ],
)
def test_owned_failure_boundaries_stop_without_raw_exception(
    tmp_path, layout, prepared, monkeypatch, capsys, boundary
):
    seen = []
    original_worker = trial.worker

    async def worker(*args, **kwargs):
        mode = args[1]
        if (boundary == "derive_worker" and mode == "derive") or (
            boundary == "replay_worker" and mode == "replay"
        ):
            raise RuntimeError(SENTINEL)
        return await original_worker(*args, **kwargs)

    def refuse(*_args, **_kwargs):
        raise base.TrialError(SENTINEL)

    monkeypatch.setattr(trial, "worker", worker)
    if boundary == "derived_body_validation":
        monkeypatch.setattr(trial, "validate_derived", refuse)
    elif boundary == "plan_binding":
        monkeypatch.setattr(trial.WorkflowClaim, "bind_plan", refuse)
    elif boundary == "host_validation":
        monkeypatch.setattr(base, "validate_host_metadata", refuse)

    def handler(request):
        stage = len(seen)
        seen.append(request)
        return streamed(reply(layout, stage))

    result = run(tmp_path, layout, prepared, handler, lambda: SENTINEL)
    assert len(seen) == (2 if boundary in {"replay_worker", "host_validation"} else 1)
    assert result["diagnostics"]["failure"]["phase"] == boundary
    assert result["outcome"] == "stopped" and result["published"] is False
    assert_private(tmp_path, result, capsys)


def test_worker_recognition_refusal_is_not_an_inferred_production_fallback_cause(
    tmp_path, layout, prepared, capsys
):
    seen = []

    def handler(request):
        seen.append(request)
        return streamed(
            reply(
                layout,
                0,
                content="- Article 2: Title: Fictional supplier access incident score 8 relevant\n"
                + SENTINEL,
            )
        )

    result = run(tmp_path, layout, prepared, handler)
    assert len(seen) == 1
    assert result["diagnostics"]["failure"] == trial.diagnostics.record(
        "analysis", "worker_recognition_gate", "gate_wrapper"
    )
    assert_private(tmp_path, result, capsys)


@pytest.mark.parametrize(
    "point", ["initial", "sending", "finish", "bind", "failure_record"]
)
def test_failed_save_latches_unknown_and_never_retries_persistence(
    tmp_path, layout, prepared, monkeypatch, capsys, point
):
    calls, seen, failed = [], [], []
    original_save, original_worker = base.Claim._save, trial.worker

    def save(claim):
        calls.append(deepcopy(claim.value))
        original_save(claim)
        states = claim.value["states"]
        selected = (
            point == "initial"
            and len(calls) == 1
            or point == "sending"
            and states["analysis"] == "sending"
            or point == "finish"
            and states["analysis"] == "response_received"
            or point == "bind"
            and claim.value["requests"]["plan"]["wire_sha256"] is not None
            or point == "failure_record"
            and claim.value["diagnostics"]["failure"] is not None
        )
        if selected and not failed:
            failed.append(len(calls))
            raise OSError(SENTINEL)  # The bytes may already have been written.

    async def worker(*args, **kwargs):
        if point == "failure_record" and args[1] == "derive":
            raise RuntimeError(SENTINEL)
        return await original_worker(*args, **kwargs)

    monkeypatch.setattr(base.Claim, "_save", save)
    monkeypatch.setattr(trial, "worker", worker)

    def handler(request):
        seen.append(request)
        return streamed(reply(layout, 0))

    if point == "initial":
        with pytest.raises(trial.TrialFailure) as error:
            run(tmp_path, layout, prepared, handler)
        assert error.value.diagnostic["code"] == "persistence_unknown"
        result = {
            "diagnostics": trial.diagnostics.details(
                error.value.diagnostic, error.value
            )
        }
    else:
        result = run(tmp_path, layout, prepared, handler)
        assert result["states"] is None and result["claim_persistence"] == "unknown"
        records = [
            result["diagnostics"]["failure"],
            *result["diagnostics"]["secondary"],
        ]
        assert any(row["code"] == "persistence_unknown" for row in records)
    assert len(calls) == failed[0]
    assert len(seen) == (0 if point in {"initial", "sending"} else 1)
    assert_private(tmp_path, result, capsys)


def test_cancellation_saves_uncertainty_once_without_extra_post(
    tmp_path, layout, prepared, monkeypatch, capsys
):
    seen, saves = [], []
    original = base.Claim._save

    def save(claim):
        saves.append(deepcopy(claim.value["states"]))
        original(claim)

    def handler(request):
        seen.append(request)
        raise asyncio.CancelledError(SENTINEL)

    monkeypatch.setattr(base.Claim, "_save", save)
    result = run(tmp_path, layout, prepared, handler)
    assert len(seen) == 1 and result["states"]["analysis"] == "uncertain"
    assert result["diagnostics"]["failure"] == trial.diagnostics.record(
        "analysis", "request_send", "cancelled"
    )
    assert sum(row["analysis"] == "uncertain" for row in saves) == 1
    assert_private(tmp_path, result, capsys)


@pytest.mark.parametrize(
    "value",
    [
        {},
        {"diagnostic_version": True, "error": {}},
        {
            "diagnostic_version": 1,
            "error": {"stage": "analysis", "phase": "unknown", "code": "check_refused"},
        },
        {
            "diagnostic_version": 1,
            "error": {
                "stage": "analysis",
                "phase": "worker_recognition_gate",
                "code": "private reason",
            },
        },
        {
            "diagnostic_version": 1,
            "error": {
                "stage": "analysis",
                "phase": "worker_recognition_gate",
                "code": "check_refused",
                "message": SENTINEL,
            },
        },
        {
            "diagnostic_version": 1,
            "error": {
                "stage": "analysis",
                "phase": "worker_wait",
                "code": "check_refused",
            },
        },
        {"diagnostic_version": 1, "error": {}, "result": {"raw": SENTINEL}},
    ],
)
def test_malformed_mixed_unknown_worker_envelopes_are_never_diagnostics(value):
    with pytest.raises(trial.TrialFailure) as error:
        trial.worker_envelope(value, "derive")
    assert error.value.diagnostic == trial.diagnostics.record(
        "analysis", "worker_protocol", "invalid_worker_envelope"
    )
    assert SENTINEL not in str(error.value) + json.dumps(error.value.diagnostic)


@pytest.mark.parametrize("final", [False, True])
def test_source_fences_have_fixed_evidence_without_changing_payload(
    tmp_path, layout, prepared, monkeypatch, capsys, final
):
    original, calls, seen = trial.source_snapshot, [], []

    def source(value):
        calls.append(True)
        result = original(value)
        if len(calls) == (4 if final else 2):
            result[SENTINEL] = SENTINEL
        return result

    def handler(request):
        stage = len(seen)
        seen.append(request)
        return streamed(reply(layout, stage))

    monkeypatch.setattr(trial, "source_snapshot", source)
    result = run(tmp_path, layout, prepared, handler)
    assert len(seen) == (2 if final else 0)
    assert result["diagnostics"]["failure"]["phase"] == (
        "final_source_guard" if final else "source_guard"
    )
    assert_private(tmp_path, result, capsys)


def test_report_fence_unknown_preserves_primary_and_does_not_assert_changed():
    original = trial.diagnostics.record("analysis", "response_close", "unknown_failure")
    failure = trial.TrialFailure(original)
    receipt = {
        "diagnostics": trial.diagnostics.details(original, failure),
        "outcome": "stopped",
    }
    trial.report_fence_result(receipt, None, RuntimeError(SENTINEL))
    assert receipt["diagnostics"]["failure"] == original
    assert receipt["diagnostics"]["secondary"][-1] == trial.diagnostics.record(
        "control", "report_fence", "unknown_failure"
    )
    assert receipt["remote_reports_unchanged"] is None and SENTINEL not in json.dumps(
        receipt
    )


def test_calibration_failure_emits_only_sanitized_versioned_metadata(
    tmp_path, monkeypatch, capsys
):
    directory = tmp_path / "grc-full-trial"
    directory.mkdir(mode=0o700)
    monkeypatch.setenv("RUNNER_TEMP", str(tmp_path))
    monkeypatch.setattr(trial, "ci_layout", lambda: None)

    async def unavailable(_layout):
        raise RuntimeError(SENTINEL)

    monkeypatch.setattr(trial, "prepare", unavailable)
    with pytest.raises(SystemExit) as error:
        trial.calibrate_ci()
    assert error.value.code == 1
    value = json.loads((directory / "calibration.json").read_bytes())
    assert value["diagnostics"]["failure"] == trial.diagnostics.record(
        "calibration", "calibration_worker", "unknown_failure"
    )
    assert SENTINEL not in (directory / "calibration.json").read_text()
    captured = capsys.readouterr()
    assert (
        SENTINEL not in captured.out + captured.err and "Traceback" not in captured.err
    )


class FakeInput:
    def __init__(self, blocked=False):
        self.blocked = blocked

    def write(self, _data):
        pass

    async def drain(self):
        if self.blocked:
            await asyncio.Event().wait()

    def close(self):
        pass


class FakeOutput:
    def __init__(self, data):
        self.data = data

    async def read(self, _limit):
        data, self.data = self.data, b""
        return data


class FakeProcess:
    def __init__(self, data=b"", *, blocked=False, cleanup_faults=False, status=0):
        self.stdin, self.stdout = FakeInput(blocked), FakeOutput(data)
        self.returncode = None
        self.cleanup_faults, self.status = cleanup_faults, status
        self.kills, self.waits = 0, 0

    def kill(self):
        self.kills += 1
        if self.cleanup_faults:
            raise RuntimeError(SENTINEL)
        self.returncode = -9

    async def wait(self):
        self.waits += 1
        if self.cleanup_faults:
            raise RuntimeError(SENTINEL)
        self.returncode = self.status
        return self.status


@pytest.mark.parametrize(
    "case",
    [
        "launch",
        "timeout",
        "exit",
        "malformed",
        "oversize",
        "duplicate",
        "controlled_import",
    ],
)
def test_worker_process_failures_have_fixed_envelopes_and_preserve_cleanup_primary(
    layout, tmp_path, monkeypatch, capsys, case
):
    output = b"{" + SENTINEL.encode()
    if case == "oversize":
        output = SENTINEL.encode() + b"x" * 100001
    elif case == "duplicate":
        output = b'{"diagnostic_version":1,"diagnostic_version":1,"error":{}}'
    elif case == "controlled_import":
        output = json.dumps(
            {
                "diagnostic_version": 1,
                "error": trial.diagnostics.record(
                    "analysis", "worker_import", "unknown_failure"
                ),
            }
        ).encode()
    process = FakeProcess(
        output,
        blocked=case == "timeout",
        cleanup_faults=case == "timeout",
        status=17 if case == "exit" else 0,
    )

    async def launch(*_args, **_kwargs):
        if case == "launch":
            raise OSError(SENTINEL)
        return process

    original_timeout = asyncio.timeout
    monkeypatch.setattr(trial.asyncio, "create_subprocess_exec", launch)
    monkeypatch.setattr(
        trial.asyncio, "timeout", lambda _seconds: original_timeout(0.01)
    )
    with pytest.raises(trial.TrialFailure) as error:
        asyncio.run(trial.worker(layout, "derive", (b"{}",)))
    expected = {
        "launch": ("worker_launch", "unknown_failure"),
        "timeout": ("worker_io", "timeout"),
        "exit": ("worker_wait", "worker_exit_failed"),
        "malformed": ("worker_protocol", "invalid_worker_envelope"),
        "oversize": ("worker_protocol", "worker_output_refused"),
        "duplicate": ("worker_protocol", "invalid_worker_envelope"),
        "controlled_import": ("worker_import", "unknown_failure"),
    }
    assert error.value.diagnostic == trial.diagnostics.record(
        "analysis", *expected[case]
    )
    if case == "timeout":
        assert process.kills == process.waits == 1
        assert len(error.value.secondary) == 2 and all(
            row["phase"] == "worker_cleanup" for row in error.value.secondary
        )
        assert (
            trial.diagnostics.details(error.value.diagnostic, error.value)["last"][
                "phase"
            ]
            == "worker_cleanup"
        )
    assert_private(
        tmp_path,
        {"diagnostics": trial.diagnostics.details(error.value.diagnostic, error.value)},
        capsys,
    )


def test_response_close_timeout_is_bounded_after_validated_metadata(
    tmp_path, layout, prepared, monkeypatch, capsys
):
    original_timeout = asyncio.timeout
    monkeypatch.setattr(
        trial.asyncio,
        "timeout",
        lambda seconds: original_timeout(0.01 if seconds == 5 else seconds),
    )
    seen = []

    def handler(request):
        seen.append(request)
        response = streamed(reply(layout, 0))
        original, calls = response.aclose, []

        async def close():
            calls.append(True)
            if len(calls) > 1:
                await asyncio.Event().wait()
            await original()

        response.aclose = close
        return response

    result = run(tmp_path, layout, prepared, handler)
    assert len(seen) == 1 and result["operations"][0]["usage"]["cost"] == 0.007
    assert result["diagnostics"]["failure"] == trial.diagnostics.record(
        "analysis", "response_close", "timeout"
    )
    assert_private(tmp_path, result, capsys)


def test_claim_close_cannot_replace_an_existing_worker_failure(
    tmp_path, layout, prepared, monkeypatch, capsys
):
    original_close = base.Claim.close

    def close(claim):
        original_close(claim)
        raise RuntimeError(SENTINEL)

    async def unavailable(*_args, **_kwargs):
        raise RuntimeError(SENTINEL)

    monkeypatch.setattr(base.Claim, "close", close)
    monkeypatch.setattr(trial, "worker", unavailable)
    result = run(
        tmp_path, layout, prepared, lambda _request: streamed(reply(layout, 0))
    )
    assert result["diagnostics"]["failure"]["phase"] == "derive_worker"
    assert result["diagnostics"]["secondary"][-1]["phase"] == "claim_close"
    assert_private(tmp_path, result, capsys)


def test_request_timeout_has_durable_uncertainty_and_fixed_code(
    tmp_path, layout, prepared, capsys
):
    class Client:
        async def send(self, *_args, **_kwargs):
            raise httpx.ReadTimeout(SENTINEL)

    async def execute():
        return await trial.execute(
            prepared,
            layout,
            base.Context("a" * 40, "12345", base.TEST_REF),
            tmp_path / "claim.json",
            lambda: SENTINEL,
            Client(),
        )

    result = asyncio.run(execute())
    assert result["states"]["analysis"] == "uncertain"
    assert result["diagnostics"]["failure"] == trial.diagnostics.record(
        "analysis", "request_send", "timeout"
    )
    assert_private(tmp_path, result, capsys)


@pytest.mark.parametrize("body_failed", [False, True])
def test_scratch_cleanup_failure_preserves_primary_and_is_not_retried(
    layout, tmp_path, monkeypatch, capsys, body_failed
):
    original = trial.tempfile.TemporaryDirectory
    cleanups = []

    class Temporary:
        def __init__(self, **kwargs):
            self.actual = original(**kwargs)
            self.name = self.actual.name

        def cleanup(self):
            cleanups.append(True)
            self.actual.cleanup()
            raise RuntimeError(SENTINEL)

    monkeypatch.setattr(trial.tempfile, "TemporaryDirectory", Temporary)
    primary = trial.TrialFailure(
        trial.diagnostics.record(
            "analysis", "worker_protocol", "invalid_worker_envelope"
        )
    )
    with pytest.raises(trial.TrialFailure) as error:
        with trial.worker_scratch("analysis"):
            if body_failed:
                raise primary
    if body_failed:
        assert error.value.diagnostic == primary.diagnostic
        assert error.value.secondary[-1]["phase"] == "worker_scratch_cleanup"
        assert (
            trial.diagnostics.details(error.value.diagnostic, error.value)["last"][
                "phase"
            ]
            == "worker_scratch_cleanup"
        )
    else:
        assert error.value.diagnostic == trial.diagnostics.record(
            "analysis", "worker_scratch_cleanup", "unknown_failure"
        )
    assert cleanups == [True]
    assert_private(
        tmp_path,
        {"diagnostics": trial.diagnostics.details(error.value.diagnostic, error.value)},
        capsys,
    )


def synthetic_receipt(prior_failure):
    marker = trial.diagnostics.record(
        "analysis", "derived_body_validation", "derived_body_refused"
    )
    failure = trial.TrialFailure(marker) if prior_failure else None
    return {
        "schema_version": 2,
        "outcome": "stopped" if prior_failure else "passed",
        "states": {"analysis": "response_received", "plan": "pending"},
        "claim_persistence": "confirmed",
        "actual_cost": None,
        "operations": [
            {"stage": "analysis", "http_status": 200, "usage": {"cost": 0.007}}
        ],
        "diagnostics": trial.diagnostics.details(marker, failure),
        "published": False,
        "production_ready": False,
    }


@pytest.mark.parametrize("prior_failure", [False, True])
def test_sender_context_exit_keeps_returned_receipt_and_primary(
    tmp_path, monkeypatch, capsys, prior_failure
):
    original = synthetic_receipt(prior_failure)
    closes = []

    class Sender:
        def __init__(self, **_kwargs):
            pass

        async def __aenter__(self):
            return self

        async def __aexit__(self, *_args):
            closes.append(True)
            raise RuntimeError(SENTINEL)

    async def execute(*_args, **_kwargs):
        return deepcopy(original)

    monkeypatch.setattr(trial.httpx, "AsyncClient", Sender)
    monkeypatch.setattr(trial, "execute", execute)
    context = base.Context("a" * 40, "12345", base.TEST_REF)
    result = asyncio.run(
        trial.run_sender(None, None, context, tmp_path, lambda: SENTINEL)
    )
    assert closes == [True] and result["operations"] == original["operations"]
    assert result["states"] == original["states"] and result["outcome"] == "stopped"
    assert result["diagnostics"]["last"] == trial.diagnostics.record(
        "trial", "sender_close", "unknown_failure"
    )
    if prior_failure:
        assert result["diagnostics"]["failure"] == original["diagnostics"]["failure"]
        assert result["diagnostics"]["secondary"][-1]["phase"] == "sender_close"
    else:
        assert result["diagnostics"]["failure"] == trial.diagnostics.record(
            "trial", "sender_close", "unknown_failure"
        )
    assert_private(tmp_path, result, capsys)


def test_sender_exit_cannot_replace_raised_primary_before_receipt(
    tmp_path, monkeypatch, capsys
):
    primary = trial.TrialFailure(
        trial.diagnostics.record(
            "analysis", "derived_body_validation", "derived_body_refused"
        )
    )

    class Sender:
        def __init__(self, **_kwargs):
            pass

        async def __aenter__(self):
            return self

        async def __aexit__(self, *_args):
            raise RuntimeError(SENTINEL)

    async def execute(*_args, **_kwargs):
        raise primary

    monkeypatch.setattr(trial.httpx, "AsyncClient", Sender)
    monkeypatch.setattr(trial, "execute", execute)
    with pytest.raises(trial.TrialFailure) as error:
        asyncio.run(
            trial.run_sender(
                None,
                None,
                base.Context("a" * 40, "1", base.TEST_REF),
                tmp_path,
                lambda: SENTINEL,
            )
        )
    assert error.value.diagnostic == primary.diagnostic
    assert error.value.secondary[-1]["phase"] == "sender_close"
    assert (
        trial.diagnostics.details(error.value.diagnostic, error.value)["last"]["phase"]
        == "sender_close"
    )
    assert_private(
        tmp_path,
        {"diagnostics": trial.diagnostics.details(error.value.diagnostic, error.value)},
        capsys,
    )


@pytest.mark.parametrize("prior_failure", [False, True])
def test_control_context_exit_keeps_receipt_and_writes_only_after_cleanup(
    tmp_path, layout, prepared, monkeypatch, capsys, prior_failure
):
    import sys

    directory = tmp_path.resolve() / "grc-full-trial"
    directory.mkdir(mode=0o700)
    monkeypatch.setenv("RUNNER_TEMP", str(tmp_path.resolve()))
    monkeypatch.setattr(sys, "argv", ["trial", "--expected-commit", "a" * 40])
    monkeypatch.setattr(
        base,
        "validate_context",
        lambda *_args: base.Context("a" * 40, "12345", base.TEST_REF),
    )
    monkeypatch.setattr(
        trial,
        "git",
        lambda _root, *args: (
            ("a" * 40).encode() if args == ("rev-parse", "HEAD") else b""
        ),
    )
    monkeypatch.setattr(trial, "ci_layout", lambda: layout)
    monkeypatch.setattr(base, "public_json", lambda *_args, **_kwargs: {})
    monkeypatch.setattr(base, "validate_prior_runs", lambda *_args: None)
    monkeypatch.setattr(trial, "remote_snapshot", lambda _client: {"fixed": "snapshot"})
    original, closed, writes = synthetic_receipt(prior_failure), [], []

    async def prepare(_layout):
        return prepared

    async def send(*_args, **_kwargs):
        return deepcopy(original)

    class Control:
        def __init__(self, **_kwargs):
            pass

        def __enter__(self):
            return self

        def __exit__(self, *_args):
            closed.append(True)
            raise RuntimeError(SENTINEL)

    original_write = base.write_metadata

    def write(path, value):
        assert closed == [True]
        writes.append(path)
        original_write(path, value)

    monkeypatch.setattr(trial, "prepare", prepare)
    monkeypatch.setattr(trial, "run_sender", send)
    monkeypatch.setattr(trial.httpx, "Client", Control)
    monkeypatch.setattr(base, "write_metadata", write)
    assert trial.main() == 1
    result = json.loads((directory / "trial.json").read_bytes())
    assert len(writes) == 1 and result["operations"] == original["operations"]
    assert result["states"] == original["states"] and result["actual_cost"] is None
    assert result["diagnostics"]["last"] == trial.diagnostics.record(
        "control", "control_close", "unknown_failure"
    )
    if prior_failure:
        assert result["diagnostics"]["failure"] == original["diagnostics"]["failure"]
        assert result["diagnostics"]["secondary"][-1]["phase"] == "control_close"
    else:
        assert result["diagnostics"]["failure"] == trial.diagnostics.record(
            "control", "control_close", "unknown_failure"
        )
    assert SENTINEL not in (directory / "trial.json").read_text()
    output = capsys.readouterr()
    assert SENTINEL not in output.out + output.err and "Traceback" not in output.err


def test_latest_observation_survives_secondary_cap_and_wrapping():
    primary = trial.diagnostics.record(
        "analysis", "response_validation", "response_refused"
    )
    failure = trial.diagnostics.Error(primary)
    for phase in (
        "response_close",
        "worker_cleanup",
        "worker_scratch_cleanup",
        "sender_close",
        "control_close",
    ):
        failure.add_secondary(
            trial.diagnostics.record("trial", phase, "unknown_failure")
        )
    assert failure.diagnostic == primary and len(failure.secondary) == 3
    assert failure.secondary[-1]["phase"] == "worker_scratch_cleanup"
    wrapped = trial.stopped(failure, "trial", "context")
    assert trial.diagnostics.details(wrapped.diagnostic, wrapped)[
        "last"
    ] == trial.diagnostics.record("trial", "control_close", "unknown_failure")

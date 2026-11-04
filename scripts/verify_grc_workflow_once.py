#!/usr/bin/env python3
"""Closed fictional GRC analysis/derived-plan trial; ordinary paid routes stay disabled."""

from __future__ import annotations

import argparse
import asyncio
import base64
from contextlib import contextmanager
from dataclasses import dataclass, field
import json
import math
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from typing import Callable

import httpx

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts import verify_selected_models_once as base  # noqa: E402
from scripts import grc_trial_diagnostics as diagnostics  # noqa: E402


class TrialFailure(diagnostics.Error, base.TrialError):
    """Only fixed diagnostic fields can cross an owned failure boundary."""


def stopped(error, stage, phase, refused_code=None):
    if isinstance(error, TrialFailure):
        return error
    if isinstance(error, diagnostics.Error):
        return TrialFailure(error.diagnostic, error.secondary)
    code = diagnostics.code_for(error)
    if isinstance(error, httpx.TimeoutException):
        code = "timeout"
    elif isinstance(error, base.TrialError) and refused_code is not None:
        code = refused_code
    return TrialFailure(diagnostics.record(stage, phase, code))


def retain_failure(claim, failure, stage, http_status=None):
    if failure.claim_recorded or claim.persistence_unknown:
        return
    try:
        claim.record_failure(failure, stage, http_status)
        failure.claim_recorded = True
    except BaseException as error:
        secondary = stopped(error, stage, "claim_persistence")
        failure.add_secondary(secondary.diagnostic)


INPUT_RESERVES = (8000, 24000)
OUTPUT_TOKENS = 8000
RESERVATIONS = (96000, 128000)
SOURCE_COMMIT = "a1c61bb5199829d4e95439991b8e547e09ef48af"
LOCAL_EQUIVALENT = "2e46c3110479d74fcba744ee899e14e91d68d195"
SOURCE_TREE = "3ce97d6557220431cc434a1b66ce6d52b869f2d1"
CASE_SHA = "f21bbf7ad30e72e485ecfb6ae6ce078fcd98959d4f0d3c5a28eab0f2b3955b08"
WORKFLOW_SHA = "2a3cc73b1be3bee1a783e2e8520b23909fe3555bfba6bcfdfd66004ae4653c56"
MODEL = "google/gemini-4-argon"
PROVIDER = "google-vertex/global"
REGULATIONS = ("GDPR", "SOX", "PCI-DSS", "ISO 27001", "NIST", "CCPA")
CANONICAL = (
    "604b76b05da093be1c978042d0f4f55cb224fc2e20f0db3c1deb33f0c95d8c06",
    "eec4c52ba8f669cc1e62b2830118eea03d6c7298f00af5d1768fa33c647d0825",
)
WIRE = (
    "69628f60f627330e870b5096010b3fcc35fffbbc215f3cf280c49d021bd17728",
    "574f1936ea907956414c96a19c34721a0183819acc7d1c850a0248f282f0219f",
)
WIRE_BYTES = (2363, 17299)
RESPONSE_LIMIT = 524288
REMOTE_MAIN = {
    "SentryInsight": base.REMOTE_MAIN["SentryInsight"],
    "GRCInsight": SOURCE_COMMIT,
}


@dataclass(frozen=True)
class Layout:
    source: Path
    python: Path


@dataclass(frozen=True)
class Prepared:
    wires: tuple[bytes, bytes] = field(repr=False)


def git(source, *args):
    try:
        return subprocess.check_output(
            ["git", "--no-optional-locks", *args],
            cwd=source,
            env={
                "PATH": os.defpath,
                "GIT_CONFIG_NOSYSTEM": "1",
                "GIT_CONFIG_GLOBAL": "/dev/null",
                "GIT_TERMINAL_PROMPT": "0",
                "GIT_NO_LAZY_FETCH": "1",
            },
            stderr=subprocess.DEVNULL,
            timeout=15,
        )
    except Exception:
        raise base.TrialError("source_refused") from None


def source_snapshot(layout):
    source = layout.source
    base.require(
        git(source, "rev-parse", "HEAD").decode().strip()
        in {SOURCE_COMMIT, LOCAL_EQUIVALENT},
        "source_refused",
    )
    base.require(
        git(source, "rev-parse", "HEAD^{tree}").decode().strip() == SOURCE_TREE,
        "source_refused",
    )
    base.require(
        not git(source, "status", "--porcelain", "--untracked-files=all").strip(),
        "source_refused",
    )
    base.require(
        base.sha(
            (source / "agent/tests/fixtures/selected_model_case.json").read_bytes()
        )
        == CASE_SHA,
        "fixture_refused",
    )
    base.require(
        base.sha(
            (
                ROOT / "scripts/grc_workflow_fixture/selected_workflow_case.json"
            ).read_bytes()
        )
        == WORKFLOW_SHA,
        "fixture_refused",
    )
    return {
        name: base.sha((source / name).read_bytes())
        for name in git(source, "ls-files", "-z").decode().split("\0")
        if name
    }


def worker_envelope(value, mode):
    stage = {
        "prepare": "trial",
        "calibrate": "calibration",
        "derive": "analysis",
        "replay": "plan",
    }[mode]
    try:
        if (
            type(value) is not dict
            or type(value.get("diagnostic_version")) is not int
            or value["diagnostic_version"] != diagnostics.VERSION
        ):
            raise ValueError()
        if set(value) == {"diagnostic_version", "error"}:
            item = diagnostics.validate(value["error"])
            if (
                item["stage"] != stage
                or item["phase"] not in diagnostics.WORKER_PHASES
                or item["code"] not in diagnostics.WORKER_CODES
            ):
                raise ValueError()
            raise TrialFailure(item)
        if set(value) != {"diagnostic_version", "result", "diagnostic"}:
            raise ValueError()
        if diagnostics.validate(value["diagnostic"]) != diagnostics.record(
            stage, "worker_complete", "ok"
        ):
            raise ValueError()
        result = value["result"]
        keys = {"wires", "derived"} | (
            {"host"} if mode in {"calibrate", "replay"} else set()
        )
        if type(result) is not dict or set(result) != keys:
            raise ValueError()
        return result
    except TrialFailure:
        raise
    except BaseException:
        raise TrialFailure(
            diagnostics.record(stage, "worker_protocol", "invalid_worker_envelope")
        ) from None


def worker_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Worker protocol refused")
        result[key] = value
    return result


@contextmanager
def worker_scratch(stage):
    try:
        directory = tempfile.TemporaryDirectory(prefix="grc-closed-worker-")
    except BaseException as error:
        raise stopped(error, stage, "worker_scratch_create") from None
    failure = None
    try:
        yield Path(directory.name)
    except BaseException as error:
        failure = stopped(error, stage, "worker_io")
    finally:
        try:
            directory.cleanup()
        except BaseException as error:
            cleanup = stopped(error, stage, "worker_scratch_cleanup")
            if failure is None:
                failure = cleanup
            else:
                failure.add_secondary(cleanup.diagnostic)
    if failure is not None:
        raise failure from None


async def worker(layout, mode, responses=()):
    base.require(mode in {"prepare", "calibrate", "derive", "replay"}, "worker_refused")
    base.require(
        len(responses)
        == {"prepare": 0, "calibrate": 0, "derive": 1, "replay": 2}[mode],
        "worker_refused",
    )
    base.require(
        all(type(raw) is bytes and 0 < len(raw) <= RESPONSE_LIMIT for raw in responses),
        "worker_refused",
    )
    stage = {
        "prepare": "trial",
        "calibrate": "calibration",
        "derive": "analysis",
        "replay": "plan",
    }[mode]
    data = base.canonical([base64.b64encode(raw).decode() for raw in responses])
    process = None
    phase = "worker_launch"
    with worker_scratch(stage) as scratch:
        try:
            async with asyncio.timeout(90):
                process = await asyncio.create_subprocess_exec(
                    str(layout.python),
                    "-s",
                    "-P",
                    "-B",
                    str(ROOT / "scripts/grc_workflow_trial_worker.py"),
                    mode,
                    str(layout.source.resolve()),
                    cwd=scratch,
                    env=worker_environment(scratch),
                    stdin=asyncio.subprocess.PIPE,
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.DEVNULL,
                )
                phase = "worker_io"
                assert process.stdin is not None and process.stdout is not None
                process.stdin.write(data)
                await process.stdin.drain()
                process.stdin.close()
                output = bytearray()
                while block := await process.stdout.read(4096):
                    output.extend(block)
                    if len(output) > 100000:
                        raise TrialFailure(
                            diagnostics.record(
                                stage, "worker_protocol", "worker_output_refused"
                            )
                        )
                phase = "worker_wait"
                await process.wait()
                if process.returncode != 0:
                    raise TrialFailure(
                        diagnostics.record(stage, phase, "worker_exit_failed")
                    )
                phase = "worker_protocol"
                try:
                    value = json.loads(output, object_pairs_hook=worker_object)
                except BaseException:
                    raise TrialFailure(
                        diagnostics.record(stage, phase, "invalid_worker_envelope")
                    ) from None
                return worker_envelope(value, mode)
        except BaseException as error:
            failure = stopped(error, stage, phase)
            if process is not None and process.returncode is None:
                try:
                    process.kill()
                except BaseException as cleanup:
                    failure.add_secondary(
                        stopped(cleanup, stage, "worker_cleanup").diagnostic
                    )
                try:
                    async with asyncio.timeout(5):
                        await process.wait()
                except BaseException as cleanup:
                    failure.add_secondary(
                        stopped(cleanup, stage, "worker_cleanup").diagnostic
                    )
            raise failure from None


def worker_environment(scratch):
    environment = base.worker_environment(scratch, scratch, {})
    # Preserve the real parser's set-based ordering across separate replay
    # processes without sorting or changing production parser behavior.
    environment["PYTHONHASHSEED"] = "0"
    return environment


def decoded_wires(value, count):
    rows = value.get("wires")
    base.require(type(rows) is list and len(rows) == count, "worker_refused")
    try:
        wires = tuple(base64.b64decode(row, validate=True) for row in rows)
    except Exception:
        raise base.TrialError("worker_refused") from None
    base.require(all(0 < len(raw) <= 40000 for raw in wires), "worker_refused")
    return wires


def validate_wire(stage, wire):
    base.require(
        stage in (0, 1) and type(wire) is bytes and len(wire) <= 40000, "wire_refused"
    )
    value = json.loads(wire)
    keys = {
        "model",
        "max_tokens",
        "stream",
        "messages",
        "provider",
        "reasoning",
        "service_tier",
    }
    if stage:
        keys.add("response_format")
    base.require(
        set(value) == keys
        and value["model"] == MODEL
        and type(value["max_tokens"]) is int
        and value["max_tokens"] == OUTPUT_TOKENS
        and value["stream"] is False
        and value["service_tier"] == "default"
        and value["reasoning"] == {"effort": "low", "exclude": True}
        and value["provider"]
        == {
            "only": [PROVIDER],
            "allow_fallbacks": False,
            "require_parameters": True,
            "data_collection": "deny",
            "zdr": True,
            "max_price": {"prompt": 2, "completion": 10, "request": 0},
        },
        "wire_refused",
    )
    rows = value["messages"]
    base.require(
        type(rows) is list
        and len(rows) == 2
        and all(
            type(row) is dict
            and set(row) == {"role", "content"}
            and type(row["content"]) is str
            for row in rows
        )
        and [row["role"] for row in rows] == ["system", "user"],
        "wire_refused",
    )
    complete = {"messages": rows}
    if stage:
        complete["response_format"] = value["response_format"]
    base.require(
        len(json.dumps(complete, ensure_ascii=True).encode()) + 4096
        <= INPUT_RESERVES[stage],
        "input_reserve_refused",
    )
    return value


def validate_prepared(value):
    base.require(
        type(value) is Prepared and len(value.wires) == 2, "preparation_refused"
    )
    for stage, wire in enumerate(value.wires):
        payload = validate_wire(stage, wire)
        base.require(
            len(wire) == WIRE_BYTES[stage]
            and base.sha(wire) == WIRE[stage]
            and base.sha(base.canonical(payload)) == CANONICAL[stage],
            "preparation_refused",
        )


async def prepare(layout):
    phase = "calibration_source"
    try:
        before = source_snapshot(layout)
        phase = "calibration_worker"
        value = await worker(layout, "calibrate")
        phase = "calibration_payload"
        prepared = Prepared(decoded_wires(value, 2))
        validate_prepared(prepared)
        phase = "calibration_host"
        base.validate_host_metadata(base.Case.GRC, value.get("host"))
        phase = "calibration_source"
        base.require(before == source_snapshot(layout), "source_changed")
        return prepared
    except BaseException as error:
        raise stopped(error, "calibration", phase, "calibration_refused") from None


def validate_derived(prepared, value):
    base.require(set(value) == {"wires", "derived"}, "derived_refused")
    wires = decoded_wires(value, 2)
    base.require(wires[0] == prepared.wires[0], "derived_refused")
    fields = value["derived"]
    base.require(
        type(fields) is dict
        and set(fields) == {"grc_relevant_count", "regulations"}
        and type(fields["grc_relevant_count"]) is int
        and fields["grc_relevant_count"] in (1, 2),
        "derived_refused",
    )
    regulations = fields["regulations"]
    base.require(
        type(regulations) is list
        and len(regulations) <= 6
        and all(type(row) is str and row in REGULATIONS for row in regulations)
        and len(set(regulations)) == len(regulations),
        "derived_refused",
    )
    expected = json.loads(prepared.wires[1])
    text = expected["messages"][1]["content"]
    for original, replacement in (
        (
            "GRC-Relevant Articles: 2\n",
            f'GRC-Relevant Articles: {fields["grc_relevant_count"]}\n',
        ),
        (
            "- Regulations/Frameworks: None identified\n",
            "- Regulations/Frameworks: "
            + (", ".join(regulations) if regulations else "None identified")
            + "\n",
        ),
    ):
        base.require(text.count(original) == 1, "derived_refused")
        text = text.replace(original, replacement)
    expected["messages"][1]["content"] = text
    base.require(validate_wire(1, wires[1]) == expected, "derived_refused")
    return wires[1]


class WorkflowClaim(base.Claim):
    def __init__(self, path, context):
        self.persistence_unknown = False
        self.close_failure = None
        self.active_diagnostic = diagnostics.record(
            "trial", "claim_create", "in_progress"
        )
        self.saved_failure = None
        try:
            super().__init__(path, context)
        except BaseException as error:
            if self.persistence_unknown:
                failure = TrialFailure(
                    diagnostics.record("trial", "claim_create", "persistence_unknown")
                )
            else:
                failure = stopped(error, "trial", "claim_create", "claim_unavailable")
            if self.close_failure is not None:
                failure.add_secondary(self.close_failure.diagnostic)
            raise failure from None

    def close(self):
        try:
            super().close()
        except BaseException as error:
            self.fd = -1  # An uncertain close must not be retried on a reused fd.
            self.close_failure = stopped(error, "trial", "claim_close")

    def _initial_value(self, context):
        return {
            "diagnostics": diagnostics.details(self.active_diagnostic),
            "run_id": context.run_id,
            "commit": context.commit,
            "ref": context.ref,
            "scope": "new_grc_two_stage_fictional_trial",
            "historical_allocations": "consumed_not_reused",
            "ceiling_microusd": 224000,
            "reserved_microusd": 224000,
            "source_commit": SOURCE_COMMIT,
            "source_tree": SOURCE_TREE,
            "source_fixture_sha256": CASE_SHA,
            "workflow_fixture_sha256": WORKFLOW_SHA,
            "states": {"analysis": "pending", "plan": "pending"},
            "requests": {
                name: {
                    "reserve_microusd": RESERVATIONS[index],
                    "input_reserve": INPUT_RESERVES[index],
                    "max_tokens": OUTPUT_TOKENS,
                    "requested_model": MODEL,
                    "requested_provider": PROVIDER,
                    "calibration_wire_sha256": WIRE[index],
                    "canonical_payload_sha256": CANONICAL[0] if index == 0 else None,
                    "wire_sha256": WIRE[0] if index == 0 else None,
                }
                for index, name in enumerate(("analysis", "plan"))
            },
        }

    def _save(self):
        if self.persistence_unknown:
            raise TrialFailure(
                diagnostics.record(
                    self.active_diagnostic["stage"],
                    self.active_diagnostic["phase"],
                    "persistence_unknown",
                )
            )
        try:
            base.require(
                self.value["historical_allocations"] == "consumed_not_reused"
                and self.value["reserved_microusd"] == 224000
                and self.value["ceiling_microusd"] == 224000,
                "claim_refused",
            )
            super()._save()
        except BaseException:
            self.persistence_unknown = True
            raise TrialFailure(
                diagnostics.record(
                    self.active_diagnostic["stage"],
                    self.active_diagnostic["phase"],
                    "persistence_unknown",
                )
            ) from None

    def checkpoint(self, stage, phase):
        self.active_diagnostic = diagnostics.record(stage, phase, "in_progress")
        self.value["diagnostics"] = diagnostics.details(
            self.active_diagnostic, self.saved_failure
        )
        self._save()

    def record_failure(self, failure, stage, http_status=None):
        # This is also the sole uncertainty save after a failed/cancelled POST.
        # A previous save failure latches _save and must never be retried.
        if self.persistence_unknown:
            return
        self.saved_failure = failure
        self.active_diagnostic = failure.diagnostic
        self.value["diagnostics"] = diagnostics.details(self.active_diagnostic, failure)
        if stage in {"analysis", "plan"} and self.value["states"][stage] == "sending":
            self.value["states"][stage] = (
                "http_error" if http_status not in (None, 200) else "uncertain"
            )
        self._save()

    def start_stage(self, stage):
        base.require(type(stage) is int and stage in (0, 1), "claim_refused")
        name = ("analysis", "plan")[stage]
        base.require(self.value["states"][name] == "pending", "claim_already_consumed")
        if stage:
            base.require(
                self.value["states"]["analysis"] == "response_received"
                and self.value["requests"]["plan"]["wire_sha256"] is not None,
                "claim_refused",
            )
        self.value["states"][name] = "sending"
        self._save()

    def finish_stage(self, stage, state):
        base.require(type(stage) is int and stage in (0, 1), "claim_refused")
        name = ("analysis", "plan")[stage]
        base.require(
            self.value["states"][name] == "sending"
            and state in {"response_received", "http_error", "uncertain"},
            "claim_refused",
        )
        self.value["states"][name] = state
        self._save()

    def bind_plan(self, wire):
        base.require(
            self.value["states"] == {"analysis": "response_received", "plan": "pending"}
            and self.value["requests"]["plan"]["wire_sha256"] is None,
            "claim_refused",
        )
        self.value["requests"]["plan"]["wire_sha256"] = base.sha(wire)
        self.value["requests"]["plan"]["canonical_payload_sha256"] = base.sha(
            base.canonical(json.loads(wire))
        )
        self._save()


def response_metadata(raw, stage):
    try:
        value = json.loads(raw)
        base.require(
            type(value) is dict
            and "error" not in value
            and value.get("model") == MODEL
            and value.get("service_tier") in (None, "default")
            and value.get("provider") in (None, "Google"),
            "response_refused",
        )
        choices = value.get("choices")
        base.require(
            type(choices) is list and len(choices) == 1 and type(choices[0]) is dict,
            "response_refused",
        )
        choice = choices[0]
        message = choice.get("message")
        base.require(
            choice.get("finish_reason") == "stop"
            and "error" not in choice
            and type(message) is dict
            and "error" not in message
            and not message.get("refusal")
            and type(message.get("content")) is str
            and bool(message["content"].strip()),
            "response_refused",
        )
        usage = value.get("usage")
        base.require(type(usage) is dict, "accounting_unknown")
        for name in ("prompt_tokens", "completion_tokens", "total_tokens"):
            base.require(
                type(usage.get(name)) is int and 0 < usage[name] <= 2**53,
                "accounting_unknown",
            )
        cost = usage.get("cost")
        base.require(
            type(cost) in (int, float) and math.isfinite(cost) and cost >= 0,
            "accounting_unknown",
        )
        base.require(
            usage["prompt_tokens"] <= INPUT_RESERVES[stage]
            and usage["completion_tokens"] <= OUTPUT_TOKENS
            and usage["total_tokens"]
            == usage["prompt_tokens"] + usage["completion_tokens"]
            and cost * 1000000 <= RESERVATIONS[stage]
            and cost * 1000000
            <= usage["prompt_tokens"] * 2 + usage["completion_tokens"] * 10 + 1,
            "accounting_unknown",
        )
        safe_usage = {
            name: usage[name]
            for name in ("prompt_tokens", "completion_tokens", "total_tokens", "cost")
        }
        details = usage.get("completion_tokens_details")
        if details is not None:
            base.require(type(details) is dict, "accounting_unknown")
            if "reasoning_tokens" in details:
                count = details["reasoning_tokens"]
                base.require(
                    type(count) is int and 0 <= count <= usage["completion_tokens"],
                    "accounting_unknown",
                )
                safe_usage["reasoning_tokens"] = count
        identifier = value.get("id")
        if type(identifier) is not str or not re.fullmatch(
            r"gen-[A-Za-z0-9_-]{1,120}", identifier
        ):
            identifier = None
        return {
            "resolved_model": MODEL,
            "actual_service_tier": value.get("service_tier"),
            "serving_provider": value.get("provider"),
            "generation_id": identifier,
            "usage": safe_usage,
        }
    except Exception:
        raise base.TrialError("response_or_accounting_unknown") from None


async def post_once(client, wire, key, stage, row, claim):
    name = ("analysis", "plan")[stage]
    phase, response, failure, result = "request_send", None, None, None
    try:
        claim.checkpoint(name, phase)
        claim.start_stage(stage)  # fsync sending before the only possible POST.
        request = httpx.Request(
            "POST",
            base.ENDPOINT,
            content=wire,
            headers={
                "Authorization": "Bearer " + key,
                "Content-Type": "application/json",
                "Accept-Encoding": "identity",
                "X-Title": "Fixed fictional GRC workflow verification",
            },
            extensions={"timeout": httpx.Timeout(360).as_dict()},
        )
        async with asyncio.timeout(360):
            response = await client.send(
                request, stream=True, follow_redirects=False, auth=None
            )
            phase = "response_status"
            claim.checkpoint(name, phase)
            row["http_status"] = response.status_code
            if response.status_code != 200:
                raise TrialFailure(diagnostics.record(name, phase, "http_rejected"))
            phase = "response_read"
            claim.checkpoint(name, phase)
            base.require(
                response.headers.get("content-encoding", "identity").casefold()
                == "identity",
                "response_encoding_refused",
            )
            raw = bytearray()
            async for block in response.aiter_raw(chunk_size=65536):
                raw.extend(block)
                base.require(len(raw) <= RESPONSE_LIMIT, "response_too_large")
            phase = "response_validation"
            claim.checkpoint(name, phase)
            claim.finish_stage(stage, "response_received")
            row.update(response_metadata(bytes(raw), stage))
            result = bytes(raw)
    except BaseException as error:
        refused = {
            "response_read": "response_read_refused",
            "response_validation": "response_refused",
        }.get(phase)
        failure = stopped(error, name, phase, refused)
    if response is not None:
        if failure is None:
            try:
                claim.checkpoint(name, "response_close")
            except BaseException as error:
                failure = stopped(error, name, "response_close")
        try:
            async with asyncio.timeout(5):
                await response.aclose()
        except BaseException as error:
            cleanup = stopped(error, name, "response_close")
            if failure is None:
                failure = cleanup
            else:
                failure.add_secondary(cleanup.diagnostic)
    if failure is not None:
        retain_failure(claim, failure, name, row["http_status"])
        raise failure from None
    return result


async def execute(
    prepared, layout, context, claim_path, read_key: Callable[[], str], client
):
    try:
        validate_prepared(prepared)
    except BaseException as error:
        raise stopped(
            error, "trial", "calibration_payload", "calibration_refused"
        ) from None
    try:
        before = source_snapshot(layout)
    except BaseException as error:
        raise stopped(error, "trial", "source_guard", "source_refused") from None
    rows, responses = [], []
    outcome, host, primary = "stopped", None, None
    last = diagnostics.record("trial", "claim_create", "in_progress")
    with WorkflowClaim(claim_path, context) as claim:
        try:
            claim.checkpoint("trial", "context")
            key = read_key()
            base.require(
                type(key) is str and bool(key.strip()), "credential_unavailable"
            )
        except BaseException as error:
            raise stopped(error, "trial", "context") from None
        wire = prepared.wires[0]
        for stage in range(2):
            name = ("analysis", "plan")[stage]
            row = {
                "stage": name,
                "requested_model": MODEL,
                "requested_provider": PROVIDER,
                "wire_sha256": base.sha(wire),
                "canonical_payload_sha256": base.sha(base.canonical(json.loads(wire))),
                "http_status": None,
                "usage": None,
                "outcome": "stopped",
            }
            rows.append(row)
            phase, refused = "source_guard", "source_refused"
            try:
                claim.checkpoint(name, phase)
                base.require(before == source_snapshot(layout), "source_changed")
                raw = await post_once(client, wire, key, stage, row, claim)
                responses.append(raw)
                if stage == 0:
                    phase, refused = "derive_worker", None
                    claim.checkpoint(name, phase)
                    derived = await worker(layout, "derive", responses)
                    phase, refused = "derived_body_validation", "derived_body_refused"
                    claim.checkpoint(name, phase)
                    wire = validate_derived(prepared, derived)
                    phase, refused = "plan_binding", None
                    claim.checkpoint(name, phase)
                    claim.bind_plan(wire)
                    row["outcome"] = "recognized_analysis_passed"
                else:
                    phase, refused = "replay_worker", None
                    claim.checkpoint(name, phase)
                    replay = await worker(layout, "replay", responses)
                    phase, refused = "host_validation", "host_refused"
                    claim.checkpoint(name, phase)
                    base.require(
                        decoded_wires(replay, 2) == (prepared.wires[0], wire),
                        "replay_refused",
                    )
                    base.require(
                        validate_derived(
                            prepared,
                            {name: replay[name] for name in ("wires", "derived")},
                        )
                        == wire,
                        "replay_refused",
                    )
                    host = base.validate_host_metadata(
                        base.Case.GRC, replay.get("host")
                    )
                    base.require(host["outcome"] == "passed", "host_refused")
                    row["outcome"] = "host_rendered"
                    outcome = "passed"
                last = diagnostics.record(name, "complete", "ok")
                row["diagnostic"] = last
            except BaseException as error:
                primary = stopped(error, name, phase, refused)
                retain_failure(claim, primary, name, row["http_status"])
                row["diagnostic"] = primary.diagnostic
                last = primary.diagnostic
                break
        try:
            if primary is None:
                claim.checkpoint("trial", "final_source_guard")
            base.require(before == source_snapshot(layout), "source_changed")
        except BaseException as error:
            failure = stopped(error, "trial", "final_source_guard", "source_refused")
            if primary is None:
                primary = failure
                retain_failure(claim, primary, "trial")
            else:
                primary.add_secondary(failure.diagnostic)
            last, outcome = failure.diagnostic, "stopped"
        states = None if claim.persistence_unknown else dict(claim.value["states"])
        persistence = "unknown" if claim.persistence_unknown else "confirmed"
    if claim.close_failure is not None:
        if primary is None:
            primary = claim.close_failure
        else:
            primary.add_secondary(claim.close_failure.diagnostic)
        last, outcome = claim.close_failure.diagnostic, "stopped"
    costs = [row["usage"]["cost"] if row["usage"] is not None else None for row in rows]
    return {
        "schema_version": 2,
        "scope": "grc_full_fictional_workflow_only",
        "run_id": context.run_id,
        "executor_commit": context.commit,
        "source_commit": SOURCE_COMMIT,
        "source_tree": SOURCE_TREE,
        "source_fixture_sha256": CASE_SHA,
        "workflow_fixture_sha256": WORKFLOW_SHA,
        "reserved_microusd": 224000,
        "states": states,
        "claim_persistence": persistence,
        "operations": rows,
        "diagnostics": diagnostics.details(last, primary),
        "actual_cost": (
            sum(costs)
            if len(costs) == 2 and all(value is not None for value in costs)
            else None
        ),
        "host": host,
        "outcome": outcome,
        "published": False,
        "production_ready": False,
    }


def remote_snapshot(client):
    result = {}
    for repo, expected in REMOTE_MAIN.items():
        ref = base.public_json(client, f"repos/ricomanifesto/{repo}/git/ref/heads/main")
        base.require(
            ref.get("object", {}).get("sha") == expected, "remote_main_changed"
        )
        tree = base.public_json(
            client,
            f"repos/ricomanifesto/{repo}/git/trees/{expected}",
            {"recursive": "1"},
        )
        base.require(
            tree.get("truncated") is False and type(tree.get("tree")) is list,
            "remote_fence_unavailable",
        )
        blobs = {
            row["path"]: row["sha"]
            for row in tree["tree"]
            if row.get("type") == "blob"
            and (
                row.get("path", "").startswith(("site/", "reports/"))
                or row.get("path")
                in {
                    "index.md",
                    "index.html",
                    "current-findings.json",
                    ".sentryinsight-articles-fingerprint",
                }
            )
        }
        base.require(blobs, "remote_fence_unavailable")
        result[repo] = {"commit": expected, "report_blobs": blobs}
    return result


def ci_layout():
    workspace = Path(os.environ["GITHUB_WORKSPACE"]).resolve()
    return Layout(
        workspace / "sources/grc", workspace / "sources/grc/agent/.venv/bin/python"
    )


def calibrate_ci():
    directory = Path(os.environ["RUNNER_TEMP"]) / "grc-full-trial"
    try:
        prepared = asyncio.run(prepare(ci_layout()))
        value = {
            "outcome": "calibration_passed",
            "wire_sha256": list(WIRE),
            "canonical_payload_sha256": list(CANONICAL),
            "live_requests": 0,
            "input_reserves": INPUT_RESERVES,
            "output_tokens_each": OUTPUT_TOKENS,
            "reserved_microusd": 224000,
            "diagnostics": diagnostics.details(
                diagnostics.record("calibration", "complete", "ok")
            ),
        }
    except BaseException as error:
        failure = stopped(error, "calibration", "calibration_worker")
        value = {
            "outcome": "calibration_stopped",
            "live_requests": 0,
            "diagnostics": diagnostics.details(failure.diagnostic, failure),
        }
        try:
            base.write_metadata(directory / "calibration.json", value)
        except BaseException:
            pass
        raise SystemExit(1) from None
    try:
        base.write_metadata(directory / "calibration.json", value)
    except BaseException:
        raise SystemExit(1) from None
    return prepared


def report_fence_result(receipt, unchanged, error=None):
    receipt["remote_reports_unchanged"] = unchanged
    if unchanged is True and error is None:
        return
    failure = (
        stopped(error, "control", "report_fence")
        if error is not None
        else TrialFailure(
            diagnostics.record("control", "report_fence", "report_fence_refused")
        )
    )
    observed = failure.diagnostic
    previous = receipt["diagnostics"]["failure"]
    if previous is not None:
        failure = TrialFailure(
            previous, receipt["diagnostics"]["secondary"] + [failure.diagnostic]
        )
    receipt["diagnostics"] = diagnostics.details(observed, failure)
    receipt["outcome"] = "stopped"


def merge_receipt_failure(receipt, failure):
    previous = receipt["diagnostics"]["failure"]
    if previous is not None:
        failure = TrialFailure(
            previous,
            receipt["diagnostics"]["secondary"]
            + [failure.diagnostic]
            + failure.secondary,
        )
    receipt["diagnostics"] = diagnostics.details(failure.diagnostic, failure)
    receipt["outcome"] = "stopped"


async def run_sender(prepared, layout, context, directory, read_key):
    sender, receipt, failure = None, None, None
    phase = "sender_open"
    try:
        sender = httpx.AsyncClient(
            transport=httpx.AsyncHTTPTransport(retries=0, trust_env=False),
            trust_env=False,
            timeout=360,
        )
        active = await sender.__aenter__()
        phase = "sender_execution"
        receipt = await execute(
            prepared, layout, context, directory / "claim.json", read_key, active
        )
    except BaseException as error:
        failure = stopped(error, "trial", phase)
    finally:
        if sender is not None:
            try:
                async with asyncio.timeout(5):
                    await sender.__aexit__(None, None, None)
            except BaseException as error:
                cleanup = stopped(error, "trial", "sender_close")
                if failure is None:
                    failure = cleanup
                else:
                    failure.add_secondary(cleanup.diagnostic)
    if receipt is not None:
        if failure is not None:
            merge_receipt_failure(receipt, failure)
        return receipt
    if failure is not None:
        raise failure from None
    raise TrialFailure(
        diagnostics.record("trial", "sender_execution", "unknown_failure")
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--expected-commit", required=True)
    args = parser.parse_args()
    os.umask(0o077)
    phase, context, directory = "context", None, None
    control, receipt, failure = None, None, None
    try:
        context = base.validate_context(os.environ, args.expected_commit)
        base.require(os.environ.get("RUNNER_DEBUG") != "1", "debug_refused")
        base.require(
            git(ROOT, "rev-parse", "HEAD").decode().strip() == context.commit
            and not git(ROOT, "status", "--porcelain", "--untracked-files=all").strip(),
            "executor_changed",
        )
        directory = Path(os.environ["RUNNER_TEMP"]).resolve() / "grc-full-trial"
        base.require(
            directory.is_dir() and directory.resolve() == directory, "output_refused"
        )
        layout = ci_layout()

        def identity_encoding(response):
            base.require(
                response.headers.get("content-encoding", "identity").casefold()
                == "identity",
                "remote_fence_unavailable",
            )

        control = httpx.Client(
            transport=httpx.HTTPTransport(retries=0, trust_env=False),
            trust_env=False,
            timeout=30,
            headers={"Accept-Encoding": "identity"},
            event_hooks={"response": [identity_encoding]},
        )
        control.__enter__()
        history = base.public_json(
            control,
            f"repos/{base.REPOSITORY}/actions/workflows/verify-nemotron.yml/runs",
            {"event": "workflow_dispatch", "head_sha": context.commit, "per_page": 100},
        )
        base.validate_prior_runs(context, history)
        phase = "report_fence"
        before = remote_snapshot(control)
        phase = "calibration_worker"
        prepared = asyncio.run(prepare(layout))
        phase = "sender_execution"
        receipt = asyncio.run(
            run_sender(
                prepared,
                layout,
                context,
                directory,
                lambda: os.environ.get("OPENROUTER_API_KEY", ""),
            )
        )
        phase = "report_fence"
        try:
            report_fence_result(receipt, before == remote_snapshot(control))
        except BaseException as error:
            report_fence_result(receipt, None, error)
        receipt["remote_report_snapshot_sha256"] = base.sha(base.canonical(before))
    except BaseException as error:
        failure = stopped(error, "trial", phase)
    finally:
        if control is not None:
            try:
                control.__exit__(None, None, None)
            except BaseException as error:
                cleanup = stopped(error, "control", "control_close")
                if failure is None:
                    failure = cleanup
                else:
                    failure.add_secondary(cleanup.diagnostic)
    if receipt is not None:
        if failure is not None:
            merge_receipt_failure(receipt, failure)
    elif failure is not None:
        receipt = {
            "schema_version": 2,
            "outcome": "stopped",
            "states": None,
            "claim_persistence": "unknown",
            "actual_cost": None,
            "operations": [],
            "published": False,
            "production_ready": False,
            "diagnostics": diagnostics.details(failure.diagnostic, failure),
        }
    if receipt is not None and context is not None and directory is not None:
        try:
            import stat

            parent = directory.lstat()
            if not (
                stat.S_ISDIR(parent.st_mode)
                and stat.S_IMODE(parent.st_mode) == 0o700
                and parent.st_uid == os.getuid()
                and directory.resolve() == directory
            ):
                raise ValueError()
            # Only one independent write, after all owned client cleanup. Never
            # replace a precise receipt with an empty generic cleanup fallback.
            base.write_metadata(directory / "trial.json", receipt)
            if (
                receipt["outcome"] == "passed"
                and receipt.get("remote_reports_unchanged") is True
            ):
                return 0
        except BaseException:
            pass
    print(
        "GRC trial stopped; inspect sanitized state before any separately approved action."
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

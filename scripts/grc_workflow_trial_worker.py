#!/usr/bin/env python3
"""Secret-free, denied-network execution of the real fictional GRC workflow."""

from __future__ import annotations

import asyncio
import base64
from contextlib import ExitStack, redirect_stdout
import hashlib
import importlib
import io
import json
import logging
import os
from pathlib import Path
import re
import runpy
import socket
import sys
from unittest.mock import patch

import httpx

sys.path.insert(0, str(Path(__file__).resolve().parent))
import grc_trial_diagnostics as diagnostics  # noqa: E402

WORKFLOW_SHA = "2a3cc73b1be3bee1a783e2e8520b23909fe3555bfba6bcfdfd66004ae4653c56"
CASE_SHA = "f21bbf7ad30e72e485ecfb6ae6ce078fcd98959d4f0d3c5a28eab0f2b3955b08"
REGULATIONS = ("GDPR", "SOX", "PCI-DSS", "ISO 27001", "NIST", "CCPA")
RESPONSE_LIMIT = 524288


class CheckRefused(ValueError):
    def __init__(self, code="check_refused"):
        super().__init__("Fictional workflow refused")
        if code not in diagnostics.GATE_CODES | {"check_refused"}:
            raise ValueError("Diagnostic record refused")
        self.code = code


class WorkerTrace:
    def __init__(self, stage="worker"):
        self.stage, self.phase, self.primary = stage, "worker_context", None

    def capture(self, error):
        if self.primary is None:
            code = diagnostics.code_for(error)
            if isinstance(error, CheckRefused):
                code = "check_refused"
                if (self.stage, self.phase) == (
                    "analysis",
                    "worker_recognition_gate",
                ):
                    code = error.code
            self.primary = diagnostics.record(self.stage, self.phase, code)


def require(value, code="check_refused"):
    if not value:
        raise CheckRefused(code)


def deny(*_args, **_kwargs):
    raise RuntimeError("Offline worker forbids network")


class Captured(BaseException):
    """Stop before returning an unsupplied model response."""


def recognized_analysis(text, articles, parsed):
    """Do not mistake the legacy parser's fallback-to-all for model compatibility."""
    rows = {}
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("Reason:"):
            continue
        match = re.fullmatch(
            r"Article ([12]):\s*Title:\s*(.*?)\s+score\s+(10|[0-9](?:\.[0-9]+)?)\s+relevant[.]?",
            line,
        )
        if match is None:
            # Refuse explicit declarations anywhere, independently of their
            # surrounding markup/prose. Never strip or parse them into rows.
            require(re.search(r"`{3,}|~{3,}", line) is None, "gate_wrapper")
            if re.search(r"(?<!\w)article\s*(?:\d|:)", line, re.IGNORECASE):
                raise CheckRefused(
                    "gate_format" if line.startswith("Article ") else "gate_wrapper"
                )
            continue
        index = int(match[1]) - 1
        require(index not in rows, "gate_duplicate")
        require(match[2] == articles[index].title, "gate_binding")
        require(1 <= float(match[3]) <= 10, "gate_score")
        rows[index] = match[2]
    require(1 in rows, "gate_supplier")  # The supplier is the positive control.
    require(
        type(parsed) is dict and set(parsed) == {"grc_articles", "summary", "analysis"},
        "gate_parsed_shape",
    )
    require(
        parsed["summary"]
        == {
            "total_articles": 2,
            "grc_relevant_count": len(rows),
            "confidence_score": 0.8,
        },
        "gate_parsed_shape",
    )
    require(
        parsed["grc_articles"]
        == [
            {
                "title": title,
                "relevance_score": 7.0,
                "summary": "GRC-relevant content identified",
            }
            for title in rows.values()
        ],
        "gate_parsed_shape",
    )
    analysis = parsed["analysis"]
    require(
        type(analysis) is dict
        and set(analysis)
        == {
            "regulations_mentioned",
            "frameworks_referenced",
            "industries_affected",
            "risk_categories",
            "regulatory_bodies",
        },
        "gate_categories",
    )
    regulations = analysis["regulations_mentioned"]
    require(
        type(regulations) is list
        and all(type(value) is str for value in regulations)
        and len(regulations) == len(set(regulations)),
        "gate_categories",
    )
    require(all(value in REGULATIONS for value in regulations), "gate_categories")
    frameworks = analysis["frameworks_referenced"]
    require(
        type(frameworks) is list
        and all(type(value) is str for value in frameworks)
        and set(frameworks)
        == set(value for value in regulations if "ISO" in value or "NIST" in value),
        "gate_categories",
    )
    require(
        all(
            analysis[name] == []
            for name in ("industries_affected", "risk_categories", "regulatory_bodies")
        ),
        "gate_categories",
    )
    return {"grc_relevant_count": len(rows), "regulations": regulations}


async def run_workflow(source, mode, responses, trace):
    trace.phase = "worker_import"
    sys.path.insert(0, str(source / "agent"))
    from loguru import logger

    logger.disable("")
    adapter = runpy.run_path(str(source / "scripts/rehearse_selected_model_offline.py"))
    # This separately pinned project's modules resolve only in its interpreter.
    workflow = importlib.import_module("core.workflow")
    validate_rendered_report = importlib.import_module(
        "core.report_plan"
    ).validate_rendered_report
    GRCAnalysisConfig = importlib.import_module("models.api").GRCAnalysisConfig
    model_service = importlib.import_module("services.model_service")
    route = importlib.import_module("services.model_route")
    ARGON_ROUTE, RouteActivation = route.ARGON_ROUTE, route.RouteActivation

    require(ARGON_ROUTE.endpoint == "google-vertex/global")
    case_raw = (source / "agent/tests/fixtures/selected_model_case.json").read_bytes()
    require(hashlib.sha256(case_raw).hexdigest() == CASE_SHA)
    case = adapter["validate_case"]()
    workflow_raw = (
        Path(__file__).parent / "grc_workflow_fixture/selected_workflow_case.json"
    ).read_bytes()
    require(hashlib.sha256(workflow_raw).hexdigest() == WORKFLOW_SHA)
    fixture = json.loads(workflow_raw)
    captured, derived, feed_calls = [], [], []

    def respond(request):
        trace.phase = "worker_request_capture"
        index = len(captured)
        require(index < 2 and request.method == "POST")
        require(str(request.url) == "https://openrouter.ai/api/v1/chat/completions")
        payload = json.loads(request.content)
        text = "\n".join(row["content"] for row in payload["messages"])
        require(fixture["analysis_response"] not in text)
        require(json.dumps(case["calibration_plan"]) not in text)
        captured.append(request.content)
        if index >= len(responses):
            trace.phase = "worker_derived_capture"
            raise Captured()
        trace.phase = "worker_workflow"
        return httpx.Response(200, content=responses[index])

    async def fetch(url):
        require(url == fixture["feed_url"] and not feed_calls)
        feed_calls.append(url)
        return {
            "title": case["feed_info"]["title"],
            "link": fixture["feed_home"],
            "last_updated": fixture["published"],
            "entries": [
                {
                    "title": row["title"],
                    "link": row["url"],
                    "description": row["snippet"],
                    "content": "",
                    "published": fixture["published"],
                }
                for row in case["analysis_data"]["source_evidence"]
            ],
        }

    async def enrich(articles):
        return articles

    real_service = model_service.GRCModelService
    real_parser = real_service._process_analysis_response

    def parse(self, text, articles):
        trace.phase = "worker_analysis_parser"
        try:
            parsed = real_parser(self, text, articles)
        except BaseException as error:
            trace.capture(error)
            raise
        trace.phase = "worker_recognition_gate"
        try:
            recognized_analysis(text, articles, parsed)
        except BaseException as error:
            trace.capture(error)
            raise
        derived.append(parsed)
        trace.phase = "worker_workflow"
        return parsed

    def fields():
        # The workflow may reconcile model selections with its deterministic
        # local signals before building the plan. Read its actual processed map.
        return {
            "grc_relevant_count": derived[0]["summary"]["grc_relevant_count"],
            "regulations": derived[0]["analysis"]["regulations_mentioned"],
        }

    def create_service(**kwargs):
        require(kwargs["model_name"] == "openrouter/" + ARGON_ROUTE.model_id)
        require(kwargs["max_tokens"] == 8000)
        return real_service(
            **kwargs,
            activation=RouteActivation.OFFLINE,
            transport=httpx.MockTransport(respond),
        )

    with ExitStack() as stack:
        stack.enter_context(
            patch.object(workflow, "datetime", adapter["FixedDatetime"])
        )
        stack.enter_context(
            patch.object(model_service, "datetime", adapter["FixedDatetime"])
        )
        stack.enter_context(patch.object(workflow.rss_service, "fetch_feed", fetch))
        stack.enter_context(
            patch.object(workflow.rss_service, "enrich_articles", enrich)
        )
        stack.enter_context(patch.object(workflow, "GRCModelService", create_service))
        stack.enter_context(
            patch.object(real_service, "_process_analysis_response", parse)
        )
        if mode == "calibrate":
            responses[:] = [
                json.dumps(
                    {
                        "model": ARGON_ROUTE.model_id,
                        "choices": [
                            {"finish_reason": "stop", "message": {"content": answer}}
                        ],
                    }
                ).encode()
                for answer in (
                    fixture["analysis_response"],
                    json.dumps(case["calibration_plan"]),
                )
            ]
        try:
            trace.phase = "worker_workflow"
            result = await workflow.run_grc_analysis_endpoint(
                fixture["feed_url"],
                GRCAnalysisConfig(
                    model="openrouter/" + ARGON_ROUTE.model_id, max_tokens=8000
                ),
            )
        except Captured:
            trace.phase = "worker_derived_capture"
            require(mode in {"prepare", "derive"})
            require(len(captured) == (1 if mode == "prepare" else 2))
            require(mode == "prepare" or len(derived) == 1)
            return {
                "wires": [base64.b64encode(raw).decode() for raw in captured],
                "derived": fields() if derived else None,
            }
        trace.phase = "worker_host_validation"
        require(
            mode in {"calibrate", "replay"} and len(captured) == 2 and len(derived) == 1
        )
        require(result.status == "completed")
        metadata, report = result.metadata, result.report
        if metadata is None or report is None:
            raise CheckRefused()
        require(
            metadata.analysis_mode == "model"
            and metadata.resolved_model == ARGON_ROUTE.model_id
        )
        require(len(metadata.source_articles) == 2)
        plan = metadata.report_plan
        if plan is None:
            raise CheckRefused()
        require(plan["regulatory_changes"] == [])
        controls = plan["control_implications"]
        require(
            any(
                row["control_id"] == "third_party_risk" and row["source_ids"] == [2]
                for row in controls
            )
        )
        validate_rendered_report(report.content, plan, metadata.source_articles)
        host = {
            "outcome": "passed",
            "stage": "host_rendered",
            "source_count": 2,
            "grounded_control_findings": len(controls),
            "regulatory_changes": 0,
            "rendered_sha256": hashlib.sha256(report.content.encode()).hexdigest(),
        }
        return {
            "wires": [base64.b64encode(raw).decode() for raw in captured],
            "derived": fields(),
            "host": host,
        }


def main():
    os.umask(0o077)
    logging.disable(logging.CRITICAL)
    trace = WorkerTrace()
    try:
        mode, source_path = sys.argv[1:]
        require(mode in {"prepare", "calibrate", "derive", "replay"})
        trace.stage = {
            "prepare": "trial",
            "calibrate": "calibration",
            "derive": "analysis",
            "replay": "plan",
        }[mode]
        require(sys.flags.safe_path and sys.flags.no_user_site)
        require(not sys.flags.ignore_environment and sys.flags.hash_randomization == 0)
        require(os.environ.get("PYTHONHASHSEED") == "0")
        require(not os.environ.get("OPENROUTER_API_KEY"))
        trace.phase = "worker_input"
        raw = sys.stdin.buffer.read(2 * RESPONSE_LIMIT * 2 + 1)
        require(len(raw) <= 2 * RESPONSE_LIMIT * 2)
        encoded = json.loads(raw)
        require(
            type(encoded) is list
            and len(encoded)
            == {"prepare": 0, "calibrate": 0, "derive": 1, "replay": 2}[mode]
        )
        responses = [base64.b64decode(value, validate=True) for value in encoded]
        require(all(0 < len(value) <= RESPONSE_LIMIT for value in responses))
        with ExitStack() as stack:
            for name in ("connect", "connect_ex", "sendto", "sendmsg"):
                if hasattr(socket.socket, name):
                    stack.enter_context(patch.object(socket.socket, name, deny))
            for name in ("create_connection", "getaddrinfo"):
                stack.enter_context(patch.object(socket, name, deny))
            stack.enter_context(
                patch.object(httpx.HTTPTransport, "handle_request", deny)
            )
            stack.enter_context(
                patch.object(httpx.AsyncHTTPTransport, "handle_async_request", deny)
            )
            with redirect_stdout(io.StringIO()):
                value = asyncio.run(
                    run_workflow(Path(source_path).resolve(), mode, responses, trace)
                )
        output = {
            "diagnostic_version": diagnostics.VERSION,
            "result": value,
            "diagnostic": diagnostics.record(trace.stage, "worker_complete", "ok"),
        }
        sys.stdout.buffer.write(json.dumps(output, sort_keys=True).encode())
        return 0
    except BaseException as error:
        trace.capture(error)
        sys.stdout.buffer.write(
            json.dumps(
                {"diagnostic_version": diagnostics.VERSION, "error": trace.primary},
                sort_keys=True,
            ).encode()
        )
        return 0


if __name__ == "__main__":
    raise SystemExit(main())

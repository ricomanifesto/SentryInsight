#!/usr/bin/env python3
"""Secret-free, network-denied preparation and response replay for two fixtures."""

from __future__ import annotations

import asyncio
from contextlib import ExitStack
from dataclasses import replace
import hashlib
import importlib
import json
import logging
import os
from pathlib import Path
import socket
import sys
from unittest.mock import patch

import httpx


class QualityRejected(ValueError):
    """A completed host validator rejected the known answer."""


def require(condition):
    if not condition:
        raise ValueError("Fixed fixture invariant failed")


def deny(*_args, **_kwargs):
    raise RuntimeError("Fixture worker forbids network access")


async def sentry(source, scratch, captured, response):
    sys.path.insert(0, str(source))
    from scripts.rehearse_report_offline import FixedDatetime
    from scripts.verify_nemotron_once import load_case, require_tokenizer_cache
    from src.core import analyze, model_client, reviewed_report
    from src.core.model_route import RouteActivation
    from src.core.finding_evidence import EvidenceError
    from src.core.report_artifact import ReportArtifactError
    from src.core.report_validation import ReportPreparationError
    from src.core.reporting import ReportingGroundingError
    from src.core.source_review import SourceReviewError
    from scripts.build_site import build_site

    require_tokenizer_cache()
    case = load_case()
    config = json.loads((source / "config/config.json").read_bytes())
    config["analysis"]["model"] = "openrouter/moonshotai/kimi-k3.1-pro"
    config["analysis"]["max_tokens"] = 32000
    config["output_path"] = str(scratch / "index.md")

    def handler(request):
        require(not captured)
        captured.append(request.content)
        return (
            httpx.Response(200, content=response)
            if response is not None
            else httpx.Response(
                200,
                json={
                    "model": "moonshotai/kimi-k3.1-pro",
                    "service_tier": "default",
                    "choices": [
                        {
                            "finish_reason": "stop",
                            "message": {"content": case["calibration_response"]},
                        }
                    ],
                },
            )
        )

    factory = model_client.build_model_client

    def offline_factory(**kwargs):
        return factory(
            **kwargs,
            activation=RouteActivation.OFFLINE,
            transport=httpx.MockTransport(handler),
        )

    with (
        patch.object(analyze, "build_model_client", offline_factory),
        patch.object(analyze, "datetime", FixedDatetime),
        patch.object(reviewed_report, "datetime", FixedDatetime),
    ):
        result = await analyze.analyze_exploitation(case["articles"], config)
        require(len(captured) == 1 and not result.get("error"))
        try:
            candidate = reviewed_report.resolve_reviewed_analysis(result)
        except (
            reviewed_report.ReviewedReportValidationError,
            EvidenceError,
            ReportArtifactError,
            ReportPreparationError,
            ReportingGroundingError,
            SourceReviewError,
        ):
            raise QualityRejected() from None
        counts = candidate.coverage["counts"]
        require(
            counts["input_sources"] == 2
            and counts["eligible_sources"] == 1
            and counts["review_required_sources"] == 1
        )
        report = scratch / "index.md"
        report.write_text(candidate.source)
        build_site(
            report_path=report,
            output_path=scratch / "rendered",
            template_path=source / "site",
        )
        require(
            "Partial source coverage" in (scratch / "rendered/index.html").read_text()
        )
        return {
            "outcome": "passed",
            "stage": "host_rendered",
            "source_count": 2,
            "eligible_sources": 1,
            "held_sources": 1,
            "rendered_sha256": hashlib.sha256(
                (scratch / "rendered/index.html").read_bytes()
            ).hexdigest(),
        }


async def grc(source, scratch, captured, response):
    sys.path.insert(0, str(source / "agent"))
    # Load this exact source's clock/fixture adapter without importing another repo's scripts package.
    import runpy

    adapter = runpy.run_path(str(source / "scripts/rehearse_selected_model_offline.py"))
    # GRC is a separate, frozen project executed by its own interpreter. These
    # fixed modules resolve from its agent path, not the executor's environment.
    importlib.import_module("loguru").logger.disable("")
    model_service = importlib.import_module("services.model_service")
    model_route = importlib.import_module("services.model_route")
    report_plan = importlib.import_module("core.report_plan")

    case = adapter["validate_case"]()

    def handler(request):
        require(not captured)
        require(
            request.method == "POST"
            and str(request.url) == "https://openrouter.ai/api/v1/chat/completions"
        )
        require(
            json.loads(request.content)["provider"]["only"]
            == [model_route.ARGON_ROUTE.endpoint]
        )
        captured.append(request.content)
        return (
            httpx.Response(200, content=response)
            if response is not None
            else httpx.Response(
                200,
                json={
                    "model": "google/gemini-4-argon",
                    "service_tier": "default",
                    "choices": [
                        {
                            "finish_reason": "stop",
                            "message": {
                                "content": json.dumps(case["calibration_plan"])
                            },
                        }
                    ],
                },
            )
        )

    with patch.object(model_service, "datetime", adapter["FixedDatetime"]):
        service = model_service.GRCModelService(
            model_name="openrouter/google/gemini-4-argon",
            max_tokens=8000,
            activation=model_route.RouteActivation.OFFLINE,
            transport=httpx.MockTransport(handler),
        )
        generation = await service.generate_grc_report(
            case["analysis_data"], case["feed_info"]
        )
        if generation.failure_reason is not None:
            raise QualityRejected()
        plan = generation.report_plan
        require(len(captured) == 1 and plan is not None)
        try:
            report_plan.validate_rendered_report(
                generation.content, plan, case["analysis_data"]["source_evidence"]
            )
        except ValueError:
            raise QualityRejected() from None
        # The consultation supports abstention; success also needs a grounded supplier control.
        controls = plan["control_implications"]
        if not (
            plan["regulatory_changes"] == []
            and any(
                row["control_id"] == "third_party_risk" and row["source_ids"] == [2]
                for row in controls
            )
        ):
            raise QualityRejected()
        return {
            "outcome": "passed",
            "stage": "host_rendered",
            "source_count": 2,
            "grounded_control_findings": len(controls),
            "regulatory_changes": 0,
            "rendered_sha256": hashlib.sha256(generation.content.encode()).hexdigest(),
        }


async def grc_vertex(source, scratch, captured, response):
    """The sole test rebind changes only the endpoint, inside a denied-network worker."""
    sys.path.insert(0, str(source / "agent"))
    model_route = importlib.import_module("services.model_route")
    require(model_route.ARGON_ROUTE.endpoint == "google-ai-studio")
    policy = replace(model_route.ARGON_ROUTE, endpoint="google-vertex/global")
    with patch.object(model_route, "ARGON_ROUTE", policy):
        return await grc(source, scratch, captured, response)


def main():
    os.umask(0o077)
    logging.disable(logging.CRITICAL)
    try:
        mode, case, path = sys.argv[1:]
        vertex = mode in {"prepare_vertex", "validate_vertex"}
        require(
            (vertex and case == "grc")
            or (mode in {"prepare", "validate"} and case in {"sentry", "grc"})
        )
        source = Path(path).resolve()
        scratch = Path(os.environ["TRIAL_WORKER_SCRATCH"]).resolve()
        require(Path.cwd() == scratch and not os.environ.get("OPENROUTER_API_KEY"))
        response = (
            sys.stdin.buffer.read(4 * 1024 * 1024 + 1)
            if mode in {"validate", "validate_vertex"}
            else None
        )
        require(response is None or 0 < len(response) <= 4 * 1024 * 1024)
        captured = []
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
            result = asyncio.run(
                (grc_vertex if vertex else (sentry if case == "sentry" else grc))(
                    source, scratch, captured, response
                )
            )
        require(len(captured) == 1)
        output = (
            captured[0]
            if mode in {"prepare", "prepare_vertex"}
            else json.dumps(result, sort_keys=True).encode()
        )
        sys.stdout.buffer.write(output)
        return 0
    except QualityRejected:
        if len(sys.argv) > 1 and sys.argv[1] in {"validate", "validate_vertex"}:
            sys.stdout.write('{"outcome":"failed","stage":"host_rejected"}')
            return 0
        return 1
    except BaseException:
        # Availability/import/transport/protocol failures are not quality results.
        # No provider/library/source strings become child diagnostics.
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

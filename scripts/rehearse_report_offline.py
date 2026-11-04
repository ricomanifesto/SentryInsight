#!/usr/bin/env python3
"""Rehearse the production graph with fixed synthetic inputs, strictly offline.

Only bounded JSON metadata reaches stdout. Reports and local admission history
live in automatically removed scratch directories. There is no live mode.
"""

import argparse
import asyncio
from contextlib import contextmanager, ExitStack
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
import logging
import os
from pathlib import Path
import shlex
import shutil
import socket
import subprocess
import sys
import tempfile
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
CACHE_FILE = "9b5ad71b2ce5302211f9c61530b329a4922fc6a4"
CACHE_SHA256 = "223921b76ee99bde995b7ff738513eef100fb51d18c93597a113bcffe865b2a7"
MODEL_ID = "nvidia/nemotron-3-ultra-550b-a55b:free"
POLICY = {
    "allow_fallbacks": False,
    "max_price": {"prompt": 0, "completion": 0, "request": 0, "image": 0},
}
SCENARIOS = (
    "partial_success",
    "all_held",
    "unsupported_evidence",
    "invalid_version_reference",
    "output_truncated",
    "model_identity_mismatch",
    "transient_then_success",
    "transient_cap",
    "uncertain_transport",
    "lost_completion_ack",
)


def sha256(value):
    return hashlib.sha256(value).hexdigest()


def digest(value):
    return sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode())


def require(condition):
    if not condition:
        raise RuntimeError("Offline rehearsal invariant failed")


def deny_network(*_args, **_kwargs):
    raise RuntimeError("Offline rehearsal forbids network access")


class FixedDatetime(datetime):
    @classmethod
    def now(cls, tz=None):
        value = cls(2026, 1, 2, 12, tzinfo=timezone.utc)
        return value if tz is not None else value.replace(tzinfo=None)


@contextmanager
def offline_environment(scratch, tokenizer_cache):
    """Discard inherited secrets/config and deny Python and Node networking."""
    cache = tokenizer_cache.resolve()
    require(sha256((cache / CACHE_FILE).read_bytes()) == CACHE_SHA256)
    home = scratch / "home"
    home.mkdir()
    # The production Python bridge deliberately forwards only PATH/HOME/TMPDIR.
    # These settings therefore apply to every Git child without altering it.
    (home / ".gitconfig").write_text(
        "[user]\n name = Offline Fixture\n email = offline@example.invalid\n"
        '[protocol]\n allow = never\n[protocol "file"]\n allow = always\n'
        "[credential]\n helper =\n[core]\n hooksPath = /dev/null\n"
    )
    node = shutil.which("node")
    if node is None:
        raise RuntimeError("Offline rehearsal requires Node")
    guard = scratch / "deny-network.cjs"
    guard.write_text(
        "const deny = () => { throw new Error('offline network denied'); };\n"
        "globalThis.fetch = deny;\n"
        "for (const [module, names] of [\n"
        " ['node:net', ['connect', 'createConnection']],\n"
        " ['node:tls', ['connect']],\n"
        " ['node:http2', ['connect']],\n"
        " ['node:dgram', ['createSocket']],\n"
        " ['node:http', ['request', 'get']],\n"
        " ['node:https', ['request', 'get']],\n"
        " ['node:dns', ['lookup', 'resolve', 'resolve4', 'resolve6']],\n"
        " ['node:dns/promises', ['lookup', 'resolve', 'resolve4', 'resolve6']],\n"
        "]) { const api = require(module); for (const name of names) api[name] = deny; }\n"
        "require('node:net').Socket.prototype.connect = deny;\n"
    )
    binaries = scratch / "bin"
    binaries.mkdir()
    # Quote absolute paths for this Node launcher, including paths with spaces.
    launcher = binaries / "node"
    launcher.write_text(
        "#!/bin/sh\n"
        "export GIT_CONFIG_NOSYSTEM=1 GIT_ALLOW_PROTOCOL=file GIT_TERMINAL_PROMPT=0\n"
        f"export GIT_CONFIG_GLOBAL={shlex.quote(str(home / '.gitconfig'))}\n"
        f'exec {shlex.quote(node)} --require {shlex.quote(str(guard))} "$@"\n'
    )
    launcher.chmod(0o700)
    environment = {
        "PATH": str(binaries) + os.pathsep + os.environ.get("PATH", os.defpath),
        "HOME": str(home),
        "TMPDIR": str(scratch),
        "TIKTOKEN_CACHE_DIR": str(cache),
        "GIT_CONFIG_NOSYSTEM": "1",
        "GIT_CONFIG_GLOBAL": str(home / ".gitconfig"),
        "GIT_ALLOW_PROTOCOL": "file",
        "GIT_TERMINAL_PROMPT": "0",
        "OTEL_SDK_DISABLED": "true",
        "LOGFIRE_SEND_TO_LOGFIRE": "false",
        "LANGSMITH_TRACING": "false",
        "LANGCHAIN_TRACING_V2": "false",
    }
    with ExitStack() as stack:
        stack.enter_context(patch.dict(os.environ, environment, clear=True))
        for name in ("connect", "connect_ex"):
            stack.enter_context(patch.object(socket.socket, name, deny_network))
        for name in ("sendto", "sendmsg"):
            if hasattr(socket.socket, name):
                stack.enter_context(patch.object(socket.socket, name, deny_network))
        for name in ("create_connection", "getaddrinfo"):
            stack.enter_context(patch.object(socket, name, deny_network))
        import httpx

        stack.enter_context(
            patch.object(httpx.HTTPTransport, "handle_request", deny_network)
        )
        stack.enter_context(
            patch.object(httpx.AsyncHTTPTransport, "handle_async_request", deny_network)
        )
        yield


def command(argv, cwd):
    result = subprocess.run(
        argv,
        cwd=cwd,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        timeout=60,
        check=True,
    )
    return result.stdout.decode().strip()


class LocalAdmission:
    """Use the unchanged admission CLI, exclusively in a disposable file remote."""

    def __init__(self, root):
        self.worker = root / "worker"
        self.remote = root / "remote.git"
        self.worker.mkdir(parents=True)
        shutil.copytree(ROOT / "publication", self.worker / "publication")
        command(["git", "init", "--quiet", "--bare", str(self.remote)], root)
        command(["git", "init", "--quiet", "--initial-branch=main"], self.worker)
        command(["git", "add", "publication"], self.worker)
        command(["git", "commit", "--quiet", "-m", "Offline fixture"], self.worker)
        command(["git", "remote", "add", "origin", str(self.remote)], self.worker)
        self.revision = command(["git", "rev-parse", "HEAD"], self.worker)
        event = root / "event.json"
        event.write_text("{}\n")
        admitted = self.cli(
            "admit",
            "--event-name",
            "workflow_dispatch",
            "--event-path",
            str(event),
            "--run-id",
            "800",
            "--run-attempt",
            "1",
        )
        require(admitted["decision"] == "admitted")
        self.cli("invoked", "--key", "run:800", "--run-id", "800")

    def cli(self, *args):
        return json.loads(command(["node", "publication/cli.js", *args], self.worker))

    def budget(self, *, lose_ack=False):
        from src.core.attempt_budget import AdmissionAttemptBudget, AttemptBudgetError

        owner = self

        class Budget(AdmissionAttemptBudget):
            async def finish(self, *args, **kwargs):
                await super().finish(*args, **kwargs)
                if lose_ack:
                    raise AttemptBudgetError()

        budget = Budget(
            key="run:800", run_id="800", revision=owner.revision, run_attempt="1"
        )
        # root is an existing bridge instance attribute, not a new authority.
        budget.root = self.worker
        return budget

    def history(self):
        raw = command(
            [
                "git",
                "--git-dir",
                str(self.remote),
                "show",
                "publication-admission:state.json",
            ],
            self.worker,
        )
        records = json.loads(raw)["records"]
        return {
            "reserved": sum(row["stage"] == "request_reserved" for row in records),
            "finished": sum(row["stage"] == "request_finished" for row in records),
            "dispositions": [
                row["disposition"]
                for row in records
                if row["stage"] == "request_finished"
            ],
        }


def public_snapshot(root):
    from src.core.publication_transaction import _allowed

    return {
        item.relative_to(root).as_posix(): sha256(item.read_bytes())
        for item in root.rglob("*")
        if item.is_file() and _allowed(item.relative_to(root).as_posix())
    }


def tracked_snapshot():
    from src.core.publication_transaction import _allowed

    names = command(["git", "ls-files", "-z"], ROOT).split("\0")
    return {
        name: sha256((ROOT / name).read_bytes()) for name in names if _allowed(name)
    }


def compare_pages_package(output, root):
    from scripts.package_pages import package_pages

    inputs = root / "package-input"
    inputs.mkdir()
    shutil.copy2(output / "index.md", inputs / "index.md")
    shutil.copytree(output / "reports", inputs / "reports")
    for name in ("site", "assets", "contracts"):
        shutil.copytree(ROOT / name, inputs / name)
    package = root / "package"
    package_pages(repo_root=inputs, output_path=package)
    expected = public_snapshot(output)
    expected.pop(".sentryinsight-articles-fingerprint")
    require(public_snapshot(package) == expected)
    files = {
        item.relative_to(package).as_posix(): sha256(item.read_bytes())
        for item in package.rglob("*")
        if item.is_file()
    }
    return {
        "artifact_count": len(files),
        "tree_sha256": digest(files),
        "matches_promoted_artifacts": True,
    }


async def run_scenario(name, root, seed):
    import httpx
    from src.core import analyze, model_client, reviewed_report, workflow
    from src.core.failure_receipt import make_receipt, record_request, write_receipt
    from src.core.openrouter_client import OpenRouterClient
    from src.core.report_artifact import parse_report_artifact

    from scripts.verify_nemotron_once import load_case

    case = load_case()
    inputs = case["articles"]
    answer = case["calibration_response"]
    if name == "all_held":
        inputs = inputs[1:]
    elif name == "unsupported_evidence":
        answer = answer.replace(
            "**Exceptions**: Not stated in supplied sources.",
            "**Exceptions**: Example Gateway 99 is unaffected.",
        )
    elif name == "invalid_version_reference":
        answer = answer.replace(
            "version-71841d46af47ebc043156fad6820c826",
            "version-00000000000000000000000000000000",
        )
    output = root / "artifacts"
    if seed is None:
        output.mkdir(parents=True)
    else:
        shutil.copytree(seed, output)
        # Test-owned last-good site represents a different previous source plan.
        (output / ".sentryinsight-articles-fingerprint").write_text("0" * 64)
    before = public_snapshot(output)
    admission = LocalAdmission(root / "admission")
    config = json.loads((ROOT / "config/config.json").read_bytes())
    config["output_path"] = str(output / "index.md")
    require(config["analysis"]["max_input_tokens"] == 200000)
    receipt_path = root / "failure.json"
    write_receipt(receipt_path, make_receipt(None, started=True, environ={}))
    requests = []
    finishes = []
    selected_clients = []

    class Feed:
        def __init__(self, _url):
            pass

        async def fetch_articles(self):
            return deepcopy(inputs)

        async def enrich_article_content(self, articles):
            return articles

    def provider(request):
        payload = json.loads(request.content)
        require(
            request.method == "POST"
            and str(request.url) == "https://openrouter.ai/api/v1/chat/completions"
        )
        require(set(payload) == {"model", "max_tokens", "provider", "messages"})
        require(
            payload["model"] == MODEL_ID
            and payload["max_tokens"] == 32000
            and payload["provider"] == POLICY
        )
        require(
            [message["role"] for message in payload["messages"]] == ["system", "user"]
        )
        require("example.test/advisories/withheld" not in json.dumps(payload))
        require(request.headers["authorization"] == "Bearer offline-synthetic-key")
        require(not requests or requests[0]["sha256"] == digest(payload))
        requests.append(
            {
                "sha256": digest(payload),
                "message_tokens_cl100k": sum(
                    len(analyze.tokenizer.encode(message["content"]))
                    for message in payload["messages"]
                ),
            }
        )
        if name == "uncertain_transport":
            raise httpx.ReadTimeout("synthetic uncertainty")
        if name == "transient_cap" or (
            name == "transient_then_success" and len(requests) == 1
        ):
            return httpx.Response(503, json={"error": {"code": 503}})
        finish = "length" if name == "output_truncated" else "stop"
        finishes.append(finish)
        return httpx.Response(
            200,
            json={
                "model": (
                    "synthetic/unexpected:free"
                    if name == "model_identity_mismatch"
                    else MODEL_ID
                ),
                "choices": [{"finish_reason": finish, "message": {"content": answer}}],
            },
        )

    def client_with_mock_transport(**kwargs):
        require(kwargs["api_key"] == "offline-synthetic-key")
        kwargs.update(
            attempt_budget=admission.budget(lose_ack=name == "lost_completion_ack"),
            on_request=lambda value: record_request(receipt_path, value),
            transport=httpx.MockTransport(provider),
        )
        actual = OpenRouterClient(**kwargs)
        selected_clients.append(actual)
        return actual

    stages = []

    async def invoke():
        state = None
        async for update in workflow.create_exploitation_analysis_graph().astream(
            {
                "config": config,
                "status": "started",
                "articles": [],
                "filtered_articles": [],
                "analysis_results": {},
            },
            stream_mode="updates",
        ):
            require(len(update) == 1)
            stage, state = next(iter(update.items()))
            stages.append(stage)
        require(state is not None)
        return state

    with (
        patch.object(workflow, "SentryDigestFeedClient", Feed),
        patch.dict(os.environ, {"OPENROUTER_API_KEY": "offline-synthetic-key"}),
        patch.object(model_client, "OpenRouterClient", client_with_mock_transport),
        patch.object(analyze, "datetime", FixedDatetime),
        patch.object(reviewed_report, "datetime", FixedDatetime),
    ):
        state = await invoke()
        first_requests = len(requests)
        restarted = None
        if name in {
            "transient_cap",
            "uncertain_transport",
            "lost_completion_ack",
            "model_identity_mismatch",
        }:
            restarted = await invoke()
            require(restarted["status"] == "failed" and len(requests) == first_requests)

    after = public_snapshot(output)
    validated_models = {
        client.last_generation["resolved_model"]
        for client in selected_clients
        if client.last_generation is not None
    }
    require(validated_models <= {MODEL_ID})
    bounded = make_receipt(state, environ={})
    successful = name in {"partial_success", "transient_then_success"}
    require(bool(state.get("report_generated")) == successful)
    require(
        state["status"]
        == (
            "completed_with_review"
            if successful
            else "review_required" if name == "all_held" else "failed"
        )
    )
    require(
        len(requests)
        == {"all_held": 0, "transient_then_success": 2, "transient_cap": 3}.get(name, 1)
    )
    if not successful:
        require(before == after)
    coverage = None
    package = None
    if successful:
        artifact = parse_report_artifact((output / "index.md").read_text())
        if artifact.source_coverage is None:
            raise RuntimeError("Offline rehearsal requires source coverage")
        coverage = artifact.source_coverage["counts"]
        require(
            coverage["input_sources"] == 2
            and coverage["eligible_sources"] == 1
            and coverage["review_required_sources"] == 1
        )
        require("Partial source coverage" in (output / "index.md").read_text())
        require("Partial source coverage" in (output / "index.html").read_text())
        require(
            (output / "reports/index.json").is_file()
            and (output / "current-findings.json").is_file()
        )
        package = compare_pages_package(output, root)
    return {
        "scenario": name,
        "status": state["status"],
        "stages": stages,
        "mock_requests": len(requests),
        "request_limit": 3,
        "request_sha256": requests[0]["sha256"] if requests else None,
        "input_tokens_cl100k_including_256_reserve": (
            requests[0]["message_tokens_cl100k"] + 256 if requests else None
        ),
        "requested_model": MODEL_ID,
        "resolved_model": next(iter(validated_models), None),
        "finish_reason": finishes[-1] if finishes else None,
        "request": bounded["request"],
        "diagnostic": bounded["diagnostic"],
        "retry": bounded["retry"],
        "durable_history": admission.history(),
        "restart_blocked": restarted is not None,
        "report_generated": successful,
        "coverage_counts": coverage,
        "pages_package": package,
        "scratch_artifact_count": len(after),
        "scratch_tree_sha256": digest(after),
        "last_good_preserved": before == after if seed is not None else None,
    }, output


async def rehearse(tokenizer_cache):
    logging.disable(logging.CRITICAL)
    with tempfile.TemporaryDirectory(prefix="sentryinsight-offline-") as directory:
        scratch = Path(directory)
        require(shutil.disk_usage(scratch).free >= 1024**3)
        with offline_environment(scratch, tokenizer_cache):
            # Import under the network denial, clean environment and pinned cache.
            from scripts.verify_nemotron_once import CASE_SHA256

            before = tracked_snapshot()
            results = []
            seed = None
            for name in SCENARIOS:
                result, output = await run_scenario(name, scratch / name, seed)
                results.append(result)
                if seed is None:
                    seed = output
            after = tracked_snapshot()
            require(before == after)
            return {
                "schema_version": 1,
                "code_commit": command(["git", "rev-parse", "HEAD"], ROOT),
                "rehearsal_source_sha256": sha256(Path(__file__).read_bytes()),
                "fixture_sha256": CASE_SHA256,
                "outcome": "offline_rehearsal_passed",
                "offline_only": True,
                "published": False,
                "live_requests": 0,
                "provider_boundary": "httpx_mock_transport",
                "admission_boundary": "disposable_local_file_remote",
                "telemetry_configured": False,
                "production_ready": False,
                "tracked_public_artifacts_unchanged": True,
                "tracked_public_artifact_count": len(before),
                "tracked_public_tree_sha256": digest(before),
                "scenarios": results,
                "github_permissions_verified": False,
            }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline-only", required=True, action="store_true")
    parser.add_argument("--tokenizer-cache", required=True, type=Path)
    args = parser.parse_args()
    try:
        receipt = asyncio.run(rehearse(args.tokenizer_cache))
        encoded = json.dumps(receipt, sort_keys=True, separators=(",", ":"))
        require(len(encoded.encode()) < 24576)
        print(encoded)
        return 0
    except (Exception, KeyboardInterrupt):
        # Neither library errors nor source/report strings are CLI diagnostics.
        print(
            '{"offline_only":true,"outcome":"offline_rehearsal_failed","published":false}',
            file=sys.stderr,
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

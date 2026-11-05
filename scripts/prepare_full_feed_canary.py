#!/usr/bin/env python3
"""Closed, offline-only full-feed prompt capture through the actual host graph."""

import argparse
from copy import deepcopy
from contextlib import contextmanager, ExitStack, nullcontext
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import json
import logging
import os
from pathlib import Path
import sys
import socket
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
FEED_SHA = "f3a601d5927c3e77668c840b9adaa08da3100f1d8e3c33f23123457e37cb0414"
FEED_REVISION = "9495aeda2c7639f1e0c3e29ca72af746e1f88a51"
FEED_URL = f"https://raw.githubusercontent.com/ricomanifesto/SentryDigest/{FEED_REVISION}/feed.xml"
CACHE_FILE = "9b5ad71b2ce5302211f9c61530b329a4922fc6a4"
CACHE_SHA = "223921b76ee99bde995b7ff738513eef100fb51d18c93597a113bcffe865b2a7"


def sha(value):
    return hashlib.sha256(value).hexdigest()


def canonical(value):
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode()


def require(value):
    if not value:
        raise ValueError("Closed canary refused")


def verify_feed(raw):
    require(type(raw) is bytes and len(raw) == 31105 and sha(raw) == FEED_SHA)


class FixedClock(datetime):
    @classmethod
    def now(cls, tz=None):
        value = cls(2026, 11, 5, 12, tzinfo=timezone.utc)
        return value if tz is not None else value.replace(tzinfo=None)


@dataclass(frozen=True, repr=False)
class Prepared:
    pack: bytes
    wire: bytes
    metadata: dict


async def prepare(raw, scratch):
    verify_feed(raw)
    location = os.environ.get("TIKTOKEN_CACHE_DIR")
    if not isinstance(location, str) or not location:
        raise ValueError("Closed canary refused")
    cache = Path(location)
    try:
        require(cache.is_dir() and sha((cache / CACHE_FILE).read_bytes()) == CACHE_SHA)
    except OSError:
        raise ValueError("Closed canary refused") from None
    # This closed offline operation owns its process environment while running.
    # No inherited model override, credential, gateway or exporter survives to
    # an application import. Direct callers receive the same fence as the CLI.
    with capture_environment(cache):
        result = await _prepare_owned(raw, scratch)
        if not isinstance(result, Prepared):
            raise ValueError("Closed canary refused")
        return result


def deny_network(*_args, **_kwargs):
    raise ValueError("Closed canary refused")


@contextmanager
def capture_environment(cache):
    environment = {
        "PATH": os.defpath,
        "TIKTOKEN_CACHE_DIR": str(cache.resolve()),
        "OTEL_SDK_DISABLED": "true",
        "LOGFIRE_SEND_TO_LOGFIRE": "false",
        "LANGSMITH_TRACING": "false",
        "LANGCHAIN_TRACING_V2": "false",
    }
    with ExitStack() as stack:
        previous_logging = logging.root.manager.disable
        logging.disable(logging.CRITICAL)
        stack.callback(logging.disable, previous_logging)
        stack.enter_context(patch.dict(os.environ, environment, clear=True))
        for name in ("connect", "connect_ex", "sendto", "sendmsg"):
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


async def _prepare_owned(
    raw, scratch, *, replay=None, expected=None, attempt_budget=None
):
    import httpx
    from src.services import fetch
    from src.services.article_content import normalize_feed_content
    from src.core import analyze, model_client, reviewed_report, workflow
    from src.core.model_route import KIMI_ROUTE, OFFLINE_KEY, RouteActivation

    original = model_client.OpenRouterClient
    actual_factory = model_client.build_model_client
    capture = []

    def feed_reply(request):
        require(str(request.url) == FEED_URL)
        return httpx.Response(
            200, content=raw, headers={"content-type": "application/xml"}
        )

    async with httpx.AsyncClient(
        transport=httpx.MockTransport(feed_reply)
    ) as feed_client:
        parser = fetch.SentryDigestFeedClient(FEED_URL)
        with patch.object(fetch, "datetime", FixedClock):
            articles = await parser._fetch_articles_with_client(feed_client)
    for article in articles:
        content = (
            normalize_feed_content(article.get("content"))
            or "# " + article.get("title", "") + "\n"
        )
        if not article.get("content") and article.get("summary"):
            content += normalize_feed_content(article["summary"]) + "\n"
        article.update(content=content, content_kind="feed", source_links=[])
    require(len(articles) == 30)
    pack = canonical(
        {"feed_sha256": FEED_SHA, "feed_revision": FEED_REVISION, "articles": articles}
    )
    plan = analyze.prepare_source_review(articles)

    class FrozenFeed:
        def __init__(self, _url):
            pass

        async def fetch_articles(self):
            return deepcopy(articles)

        async def enrich_article_content(self, values):
            require(canonical(values) == canonical(articles))
            return values

    def response(request):
        require(not capture)
        require(
            request.method == "POST"
            and str(request.url) == "https://openrouter.ai/api/v1/chat/completions"
        )
        body = json.loads(request.content)
        require(body["model"] == KIMI_ROUTE.model_id and body["max_tokens"] == 32000)
        require(body["provider"] == KIMI_ROUTE.provider_payload())
        require(
            body["service_tier"] == "default"
            and body["reasoning"] == {"effort": "low", "exclude": True}
        )
        if expected is not None:
            require(request.content == expected.wire and pack == expected.pack)
        capture.append(bytes(request.content))
        if replay is not None:
            return httpx.Response(200, content=replay)
        return httpx.Response(400, json={"error": {"code": 400}})

    def constructor(**kwargs):
        require(
            kwargs.get("api_key") == OFFLINE_KEY
            and kwargs.get("activation") is RouteActivation.OFFLINE
            and type(kwargs.get("transport")) is httpx.MockTransport
            and kwargs.get("max_tokens") == 32000
        )
        return original(**kwargs, max_attempts=1, attempt_budget=attempt_budget)

    def factory(**kwargs):
        selection = kwargs.get("model")
        require(
            selection is not None
            and selection.provider_id == "openrouter"
            and selection.model_id == KIMI_ROUTE.model_id
            and kwargs.get("max_tokens") == 32000
        )
        return actual_factory(
            **kwargs,
            activation=RouteActivation.OFFLINE,
            transport=httpx.MockTransport(response),
        )

    config = json.loads((ROOT / "config/config.json").read_bytes())
    config["analysis"]["model"] = "openrouter/" + KIMI_ROUTE.model_id
    config["feed_url"] = FEED_URL
    scratch = Path(scratch)
    scratch.mkdir(parents=True, exist_ok=True)
    config["output_path"] = str(scratch / "index.md")
    final = None
    disabled = {
        "OTEL_SDK_DISABLED": "true",
        "LOGFIRE_SEND_TO_LOGFIRE": "false",
        "LANGSMITH_TRACING": "false",
        "LANGCHAIN_TRACING_V2": "false",
    }
    previous_logging = logging.root.manager.disable
    logging.disable(logging.CRITICAL)
    try:
        with (
            patch.dict(os.environ, disabled),
            patch.object(workflow, "SentryDigestFeedClient", FrozenFeed),
            patch.object(model_client, "OpenRouterClient", constructor),
            patch.object(analyze, "build_model_client", factory),
            patch.object(analyze, "datetime", FixedClock),
            (
                patch.object(reviewed_report, "datetime", FixedClock)
                if replay is None
                else nullcontext()
            ),
            patch.object(workflow, "datetime", FixedClock),
        ):
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
                final = next(iter(update.values()))
    finally:
        logging.disable(previous_logging)
    require(len(capture) == 1 and final is not None)
    if final is None:
        raise ValueError("Closed canary refused")
    if replay is not None:
        from src.core.validation_diagnostics import sanitize_diagnostic

        return {
            "host_replay_requests": len(capture),
            "host_validated": bool(final.get("report_generated")),
            "status": final["status"],
            "diagnostic": (
                sanitize_diagnostic(final.get("failure_diagnostic"))
                if final.get("failure_diagnostic")
                else None
            ),
        }
    require(final["status"] == "failed")
    wire = capture[0]
    payload = json.loads(wire)
    counts = {"eligible": 0, "review_required": 0}
    for source in plan.packet["sources"]:
        counts[source["state"]] = counts.get(source["state"], 0) + 1
    metadata = {
        "schema_version": 1,
        "offline_only": True,
        "production_ready": False,
        "feed_sha256": FEED_SHA,
        "feed_revision": FEED_REVISION,
        "source_pack_sha256": sha(pack),
        "source_review_sha256": sha(canonical(plan.packet)),
        "input_sources": len(articles),
        "eligible_sources": counts["eligible"],
        "held_sources": counts["review_required"],
        "wire_sha256": sha(wire),
        "canonical_request_sha256": sha(canonical(payload)),
        "wire_bytes": len(wire),
        "message_tokens_cl100k": sum(
            len(analyze.tokenizer.encode(row["content"])) for row in payload["messages"]
        ),
        "max_tokens": 32000,
        "requested_model": KIMI_ROUTE.model_id,
        "provider_only": ["moonshotai/mxfp4"],
        "mock_capture_requests": 1,
        "external_requests": 0,
        "article_fetches": 0,
        "published": False,
        "output_fate": "approval_required_before_any_real_send",
        "financial_grant_issued": False,
    }
    return Prepared(pack, wire, metadata)


def main():
    import asyncio
    import tempfile

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline-only", required=True, action="store_true")
    parser.add_argument("--feed-file", required=True, type=Path)
    args = parser.parse_args()
    try:
        with tempfile.TemporaryDirectory(prefix="sentry-canary-capture-") as directory:
            value = asyncio.run(prepare(args.feed_file.read_bytes(), Path(directory)))
        print(json.dumps(value.metadata, sort_keys=True))
    except BaseException:
        print(
            json.dumps(
                {
                    "outcome": "refused",
                    "phase": "offline_capture",
                    "external_requests": 0,
                    "published": False,
                }
            )
        )
        raise SystemExit(1) from None


if __name__ == "__main__":
    main()

"""Opt-in recovery profile of the standalone verifier, with mock transports only.

The exact free nemotron-3.5 route, 32,000 output cap and 8,000 reasoning budget
must be on the outgoing request before anything is sent. One request at most,
no retries, no publication, and only an exact zero-cost natural stop passes.
"""

import asyncio
import json
import logging
import sys
import tempfile

import httpx
import pytest

from scripts import verify_report_generation as verifier
from scripts.verify_report_generation import (
    MODEL_ID,
    RECOVERY_MODEL_ID,
    RecoveryClient,
    VerificationClient,
    verify_articles,
)
from src.core import openrouter_client as openrouter_module
from src.core import publication_transaction
from src.core.openrouter_client import OpenRouterError
from src.core.opencode_client import parse_model_selection
from report_recovery_fixtures import (
    ALPHA_ADVISORY,
    finding,
    id_for,
    key_for,
    report,
    standard_articles,
)

ZERO_PRICES = {"prompt": 0, "completion": 0, "request": 0, "image": 0}
CONTENT = report(
    finding(
        "Synthetic gateway campaign",
        [key_for("alpha")],
        vendor_links=id_for("alpha", ALPHA_ADVISORY),
    )
)
USAGE = {
    "prompt_tokens": 1200,
    "completion_tokens": 9000,
    "completion_tokens_details": {"reasoning_tokens": 6000},
    "total_tokens": 10200,
    "cost": 0,
}


def completion(content=CONTENT, *, model=RECOVERY_MODEL_ID, usage=USAGE, **extra):
    body = {
        "model": model,
        "choices": [{"finish_reason": "stop", "message": {"content": content}}],
        **extra,
    }
    if usage is not None:
        body["usage"] = usage
    return httpx.Response(200, json=body)


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    """Temporary working tree, private temp root and failing publication hooks."""
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("SENTRYINSIGHT_MODEL", raising=False)
    temp_root = tmp_path / "temp"
    temp_root.mkdir()
    monkeypatch.setattr(tempfile, "tempdir", str(temp_root))

    def forbidden(*args, **kwargs):
        raise AssertionError("publication must never be reached")

    for name in ("promote_artifacts", "recover_publication"):
        monkeypatch.setattr(publication_transaction, name, forbidden)
    sentinel = tmp_path / "index.md"
    sentinel.write_bytes(b"last-good sentinel")
    yield tmp_path, temp_root, sentinel
    assert sentinel.read_bytes() == b"last-good sentinel"
    assert list(temp_root.iterdir()) == []
    assert sorted(path.name for path in tmp_path.iterdir()) == ["index.md", "temp"]


def run(responses):
    requests = []

    def provider(request):
        requests.append(json.loads(request.content))
        return responses[min(len(requests), len(responses)) - 1]

    client = RecoveryClient("synthetic-key", httpx.MockTransport(provider))
    receipt = asyncio.run(verify_articles(standard_articles(), client=client))
    return client, receipt, requests


def test_outgoing_request_carries_the_exact_recovery_envelope(isolated):
    client, receipt, requests = run([completion()])
    [payload] = requests
    assert set(payload) == {"model", "max_tokens", "messages", "provider", "reasoning"}
    assert payload["model"] == RECOVERY_MODEL_ID == "nvidia/nemotron-3.5-super-vl:free"
    assert payload["max_tokens"] == 32000
    assert payload["reasoning"] == {"max_tokens": 8000}
    assert payload["provider"] == {
        "allow_fallbacks": False,
        "max_price": ZERO_PRICES,
        "require_parameters": True,
    }
    assert [message["role"] for message in payload["messages"]] == ["system", "user"]
    assert "https://news.example.test/held" not in payload["messages"][1]["content"]
    assert client.verification is None


def test_successful_synthetic_response_passes_with_bounded_receipt(isolated):
    client, receipt, requests = run([completion()])
    assert receipt["outcome"] == "validation_passed"
    assert receipt["profile"] == "recovery"
    assert receipt["requested_model"] == RECOVERY_MODEL_ID
    assert receipt["reasoning_max_tokens"] == 8000
    assert receipt["max_output_tokens"] == 32000
    assert receipt["attempted"] == receipt["requests_sent"] == len(requests) == 1
    assert receipt["published"] is receipt["production_ready"] is False
    assert receipt["provider"]["finish_reason"] == "stop"
    assert receipt["provider"]["usage"]["cost"] == 0
    assert receipt["provider"]["usage"]["completion_tokens"] == 9000
    assert receipt["provider"]["usage"]["reasoning_tokens"] == 6000
    assert "refusal" not in receipt["provider"]
    serialized = json.dumps(receipt)
    assert CONTENT not in serialized
    assert "Synthetic gateway campaign" not in serialized
    assert client.last_generation == {
        "requested_model": RECOVERY_MODEL_ID,
        "resolved_model": RECOVERY_MODEL_ID,
    }


@pytest.mark.parametrize("status", [400, 404])
def test_unsupported_capability_consumes_the_one_attempt_and_stops(status, isolated):
    rejection = httpx.Response(
        status,
        json={"error": {"code": status, "message": "requested parameters unsupported"}},
    )
    client, receipt, requests = run([rejection, completion()])
    assert receipt["outcome"] == "analysis_failed"
    assert receipt["attempted"] == receipt["requests_sent"] == len(requests) == 1
    assert requests[0]["reasoning"] == {"max_tokens": 8000}
    assert client.last_request["state"] == "permanent_rejection"
    with pytest.raises(OpenRouterError):
        asyncio.run(
            client.generate(
                system_prompt="synthetic",
                user_prompt="synthetic",
                model=parse_model_selection("openrouter/" + RECOVERY_MODEL_ID),
            )
        )
    assert len(requests) == 1


def test_transient_failure_is_not_retried(isolated):
    client, receipt, requests = run([httpx.Response(503), completion()])
    assert receipt["outcome"] == "analysis_failed"
    assert receipt["attempted"] == receipt["requests_sent"] == len(requests) == 1


def usage_with(**changes):
    usage = json.loads(json.dumps(USAGE))
    for key, value in changes.items():
        if value is ...:
            usage.pop(key, None)
        else:
            usage[key] = value
    return usage


@pytest.mark.parametrize(
    ("usage", "refusal"),
    [
        (None, "usage_missing"),
        ("not a mapping", "usage_missing"),
        (usage_with(cost=...), "cost_not_zero"),
        (usage_with(cost=None), "cost_not_zero"),
        (usage_with(cost="0"), "cost_not_zero"),
        (usage_with(cost=False), "cost_not_zero"),
        (usage_with(cost=0.000001), "cost_not_zero"),
        (usage_with(completion_tokens=...), "completion_usage_invalid"),
        (usage_with(completion_tokens=0), "completion_usage_invalid"),
        (usage_with(completion_tokens=32001), "completion_usage_invalid"),
        (usage_with(completion_tokens=32000), "completion_usage_invalid"),
        (usage_with(completion_tokens=9000.0), "completion_usage_invalid"),
        (usage_with(completion_tokens_details=...), "reasoning_usage_invalid"),
        (
            usage_with(completion_tokens_details={"reasoning_tokens": 8001}),
            "reasoning_usage_invalid",
        ),
        (
            usage_with(completion_tokens_details={"reasoning_tokens": True}),
            "reasoning_usage_invalid",
        ),
        (
            usage_with(
                completion_tokens=100,
                completion_tokens_details={"reasoning_tokens": 101},
            ),
            "reasoning_usage_invalid",
        ),
        (usage_with(reasoning_tokens=5999), "reasoning_usage_invalid"),
    ],
    ids=[
        "usage-missing",
        "usage-not-mapping",
        "cost-missing",
        "cost-null",
        "cost-string",
        "cost-boolean",
        "cost-nonzero",
        "completion-missing",
        "completion-zero",
        "completion-over-cap",
        "completion-exact-cap-natural-stop",
        "completion-float",
        "reasoning-missing",
        "reasoning-over-budget",
        "reasoning-boolean",
        "reasoning-over-completion",
        "reasoning-counts-disagree",
    ],
)
def test_bad_or_missing_cost_and_usage_fail_closed(usage, refusal, isolated):
    client, receipt, requests = run([completion(usage=usage), completion()])
    assert receipt["outcome"] == "analysis_failed"
    assert receipt["provider"]["refusal"] == refusal
    assert receipt["attempted"] == receipt["requests_sent"] == len(requests) == 1
    assert CONTENT not in json.dumps(receipt)


@pytest.mark.parametrize(
    "response",
    [
        completion(model="nvidia/nemotron-3.5-super-vl"),
        completion(model=MODEL_ID),
        httpx.Response(
            200,
            json={
                "model": RECOVERY_MODEL_ID,
                "choices": [{"finish_reason": "length", "message": {"content": "x"}}],
                "usage": USAGE,
            },
        ),
    ],
    ids=["paid-variant", "old-model", "length-finish"],
)
def test_wrong_model_or_unnatural_stop_is_refused(response, isolated):
    _, receipt, requests = run([response, completion()])
    assert receipt["outcome"] == "analysis_failed"
    assert receipt["requests_sent"] == len(requests) == 1


@pytest.mark.parametrize("status", [201, 202, 203])
def test_success_status_other_than_200_is_refused(status, isolated):
    body = json.loads(completion().content)
    client, receipt, requests = run([httpx.Response(status, json=body), completion()])
    assert receipt["outcome"] == "analysis_failed"
    assert receipt["provider"]["refusal"] == "http_status_not_ok"
    assert receipt["provider"]["http_status"] == status
    assert receipt["attempted"] == receipt["requests_sent"] == len(requests) == 1
    assert CONTENT not in json.dumps(receipt)


@pytest.mark.parametrize(
    ("completion_tokens", "reasoning_tokens"),
    [(1, 0), (1, 1), (31999, 8000), (31999, 0)],
    ids=["one-token", "one-token-all-reasoning", "below-cap-full-budget", "below-cap"],
)
def test_usage_inside_the_strict_bounds_passes(
    completion_tokens, reasoning_tokens, isolated
):
    usage = usage_with(
        completion_tokens=completion_tokens,
        completion_tokens_details={"reasoning_tokens": reasoning_tokens},
    )
    _, receipt, requests = run([completion(usage=usage)])
    assert receipt["outcome"] == "validation_passed"
    assert receipt["provider"]["usage"]["completion_tokens"] == completion_tokens
    assert receipt["provider"]["usage"]["reasoning_tokens"] == reasoning_tokens
    assert receipt["requests_sent"] == len(requests) == 1


def test_policy_not_asserted_on_the_prepared_request_stops_before_send(
    isolated, monkeypatch
):
    # Simulate a client change that drops the capability policy.
    monkeypatch.setattr(openrouter_module, "BOUNDED_REASONING_MODEL", "another/model")
    client, receipt, requests = run([completion()])
    assert receipt["outcome"] == "analysis_failed"
    assert receipt["provider"]["refusal"] == "capability_policy_not_established"
    assert receipt["requests_sent"] == 0
    assert requests == []
    assert client.last_request == {}


@pytest.mark.parametrize(
    ("url", "change"),
    [
        (verifier.RECOVERY_ENDPOINT, {"reasoning": {"max_tokens": 16000}}),
        (verifier.RECOVERY_ENDPOINT, {"provider": {"allow_fallbacks": False}}),
        (
            verifier.RECOVERY_ENDPOINT,
            {
                "provider": {
                    "allow_fallbacks": False,
                    "max_price": ZERO_PRICES,
                    "require_parameters": 1,
                }
            },
        ),
        (verifier.RECOVERY_ENDPOINT, {"models": [RECOVERY_MODEL_ID]}),
        (verifier.RECOVERY_ENDPOINT, {"max_tokens": 31999}),
        ("https://example.test/api/v1/chat/completions", {}),
        (
            verifier.RECOVERY_ENDPOINT,
            {
                "messages": [
                    {"role": "system", "content": "synthetic"},
                    {"role": "user", "content": "synthetic"},
                    "extraneous",
                ]
            },
        ),
        (
            verifier.RECOVERY_ENDPOINT,
            {
                "messages": [
                    "extraneous",
                    {"role": "system", "content": "synthetic"},
                    {"role": "user", "content": "synthetic"},
                ]
            },
        ),
        (
            verifier.RECOVERY_ENDPOINT,
            {
                "messages": [
                    {"role": "system", "content": "synthetic"},
                    {"role": "user", "content": "synthetic"},
                    {"role": "user", "content": "synthetic"},
                ]
            },
        ),
        (
            verifier.RECOVERY_ENDPOINT,
            {"messages": [{"role": "system", "content": "synthetic"}]},
        ),
        (
            verifier.RECOVERY_ENDPOINT,
            {
                "messages": [
                    {"role": "user", "content": "synthetic"},
                    {"role": "system", "content": "synthetic"},
                ]
            },
        ),
        (
            verifier.RECOVERY_ENDPOINT,
            {
                "messages": [
                    {"role": "system", "content": "synthetic", "name": "x"},
                    {"role": "user", "content": "synthetic"},
                ]
            },
        ),
        (
            verifier.RECOVERY_ENDPOINT,
            {
                "messages": [
                    {"role": "system"},
                    {"role": "user", "content": "synthetic"},
                ]
            },
        ),
        (
            verifier.RECOVERY_ENDPOINT,
            {
                "messages": [
                    {"role": "system", "content": "synthetic"},
                    {"role": "user", "content": ["synthetic"]},
                ]
            },
        ),
        (
            verifier.RECOVERY_ENDPOINT,
            {
                "messages": [
                    {"role": "system", "content": ""},
                    {"role": "user", "content": "synthetic"},
                ]
            },
        ),
    ],
    ids=[
        "larger-budget",
        "no-require-parameters",
        "integer-require-parameters",
        "fallback-models",
        "other-cap",
        "other-endpoint",
        "trailing-non-dict-message",
        "leading-non-dict-message",
        "three-messages",
        "one-message",
        "swapped-roles",
        "extra-message-key",
        "missing-content",
        "non-string-content",
        "empty-content",
    ],
)
def test_transport_guard_refuses_any_other_outgoing_envelope(url, change):
    calls = []
    client = RecoveryClient(
        "synthetic-key", httpx.MockTransport(lambda request: calls.append(request))
    )
    payload = {
        "model": RECOVERY_MODEL_ID,
        "max_tokens": 32000,
        "messages": [
            {"role": "system", "content": "synthetic"},
            {"role": "user", "content": "synthetic"},
        ],
        "provider": {
            "allow_fallbacks": False,
            "max_price": ZERO_PRICES,
            "require_parameters": True,
        },
        "reasoning": {"max_tokens": 8000},
        **change,
    }

    async def send():
        async with httpx.AsyncClient(transport=client.guard) as http:
            await http.post(url, json=payload)

    with pytest.raises(OpenRouterError):
        asyncio.run(send())
    assert calls == []
    assert client.sent == 0
    assert client.metadata["refusal"] == "request_envelope_refused"


def test_recovery_profile_refuses_active_paid_verification(monkeypatch):
    class Verification:
        bridge = None

        def assert_key(self, key):
            return None

    monkeypatch.setattr(openrouter_module, "active_verification", Verification)
    with pytest.raises(OpenRouterError):
        RecoveryClient("synthetic-key", httpx.MockTransport(lambda request: None))


def test_default_profile_keeps_the_fixed_verifier_contract(isolated):
    requests = []

    def provider(request):
        requests.append(json.loads(request.content))
        return completion(model=MODEL_ID)

    client = VerificationClient("synthetic-key", httpx.MockTransport(provider))
    receipt = asyncio.run(verify_articles(standard_articles(), client=client))
    [payload] = requests
    assert payload["model"] == MODEL_ID
    assert "reasoning" not in payload
    assert payload["provider"] == {"allow_fallbacks": False, "max_price": ZERO_PRICES}
    assert receipt["requested_model"] == MODEL_ID
    assert not {"profile", "reasoning_max_tokens", "requests_sent"} & set(receipt)
    assert receipt["outcome"] == "validation_passed"


def test_profile_and_client_must_agree():
    recovery = RecoveryClient("synthetic-key", httpx.MockTransport(lambda r: None))
    default = VerificationClient("synthetic-key", httpx.MockTransport(lambda r: None))
    with pytest.raises(ValueError):
        asyncio.run(
            verify_articles(standard_articles(), client=recovery, profile="default")
        )
    with pytest.raises(ValueError):
        asyncio.run(
            verify_articles(standard_articles(), client=default, profile="recovery")
        )
    with pytest.raises(ValueError):
        asyncio.run(verify_articles(standard_articles(), profile="unknown"))


def test_cli_recovery_preflight_is_offline_and_run_requires_a_key(
    tmp_path, monkeypatch, capsys
):
    articles = tmp_path / "articles.json"
    articles.write_text(json.dumps(standard_articles()))
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    # main() disables logging process-wide; keep that out of later tests.
    monkeypatch.setattr(logging, "disable", lambda *args: None)

    def no_network(*args, **kwargs):
        raise AssertionError("no transport may be created for preflight")

    monkeypatch.setattr(httpx, "AsyncHTTPTransport", no_network)
    monkeypatch.setattr(sys, "argv", ["verify", str(articles), "--profile", "recovery"])
    assert verifier.main() == 0
    receipt = json.loads(capsys.readouterr().out)
    assert receipt["outcome"] == "preflight_only"
    assert receipt["profile"] == "recovery"
    assert receipt["requested_model"] == RECOVERY_MODEL_ID
    assert receipt["attempted"] == receipt["requests_sent"] == 0

    monkeypatch.setattr(
        sys, "argv", ["verify", str(articles), "--profile", "recovery", "--run"]
    )
    assert verifier.main() == 1

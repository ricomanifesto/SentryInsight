"""A reasoning budget only for the exact observed free route and output cap.

Mock transport only. Live provider honoring of the budget is a later
acceptance check, not something these tests can establish.
"""

import asyncio
import hashlib
import json
from unittest.mock import AsyncMock

import httpx
import pytest

from src.core import openrouter_client as openrouter_module
from src.core.opencode_client import parse_model_selection
from src.core.openrouter_client import (
    OpenRouterClient,
    OpenRouterError,
    OpenRouterOutputLimitExceeded,
)

ROUTE = "openrouter/nvidia/nemotron-3.5-super-vl:free"
CAP = 32000
ZERO_PRICES = {"prompt": 0, "completion": 0, "request": 0, "image": 0}
SYSTEM = "synthetic system prompt"
USER = "synthetic user prompt"


@pytest.fixture(autouse=True)
def no_retry_wait(monkeypatch):
    sleep = AsyncMock()
    monkeypatch.setattr(asyncio, "sleep", sleep)
    return sleep


def ok(model=ROUTE, content="Complete report", **choice):
    return httpx.Response(
        200,
        json={
            "model": model.removeprefix("openrouter/"),
            "choices": [
                {"finish_reason": "stop", "message": {"content": content}, **choice}
            ],
        },
    )


def run(responses, *, model=ROUTE, max_tokens=CAP, **client_kwargs):
    requests, snapshots = [], []

    def handler(request):
        requests.append(json.loads(request.content))
        response = responses[min(len(requests), len(responses)) - 1]
        return response(model) if callable(response) else response

    client = OpenRouterClient(
        api_key="test-key",
        max_tokens=max_tokens,
        transport=httpx.MockTransport(handler),
        on_request=lambda snapshot: snapshots.append(dict(snapshot)),
        **client_kwargs,
    )

    async def generate():
        return await client.generate(
            system_prompt=SYSTEM,
            user_prompt=USER,
            model=parse_model_selection(model),
        )

    return client, generate, requests, snapshots


def legacy_payload(model_id, max_tokens):
    payload = {
        "model": model_id,
        "max_tokens": max_tokens,
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": USER},
        ],
    }
    if model_id.endswith(":free") or model_id == "openrouter/free":
        payload["provider"] = {"allow_fallbacks": False, "max_price": ZERO_PRICES}
    return payload


def digest(payload):
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def test_exact_route_sends_the_bounded_reasoning_payload():
    _, generate, requests, snapshots = run([ok])
    assert asyncio.run(generate()) == "Complete report"
    [payload] = requests
    expected = legacy_payload("nvidia/nemotron-3.5-super-vl:free", CAP)
    expected["provider"]["require_parameters"] = True
    expected["reasoning"] = {"max_tokens": 8000}
    assert payload == expected
    assert payload["provider"]["max_price"] == ZERO_PRICES
    assert payload["provider"]["allow_fallbacks"] is False
    assert "models" not in payload and "route" not in payload
    assert snapshots[-1]["request_sha256"] == digest(payload)


@pytest.mark.parametrize(
    ("model", "max_tokens"),
    [
        (ROUTE, 4000),
        (ROUTE, 31999),
        (ROUTE, 32001),
        ("openrouter/nvidia/nemotron-3-ultra-550b-a55b:free", CAP),
        ("openrouter/nvidia/nemotron-3.5-super-vl", CAP),
        # The model ID "openrouter/free" is the free router behind the provider.
        ("openrouter/openrouter/free", CAP),
        ("openrouter/example/paid-model", CAP),
    ],
)
def test_every_other_route_or_cap_keeps_todays_payload_and_hash(model, max_tokens):
    _, generate, requests, snapshots = run([ok], model=model, max_tokens=max_tokens)
    asyncio.run(generate())
    [payload] = requests
    expected = legacy_payload(model.removeprefix("openrouter/"), max_tokens)
    assert payload == expected
    assert snapshots[-1]["request_sha256"] == digest(expected)


def test_active_paid_verification_keeps_its_own_provider_policy():
    client = OpenRouterClient(api_key="test-key", max_tokens=CAP)

    class Verification:
        def provider_policy(self, purpose):
            assert purpose == "report"
            return {"order": ["example-provider"], "allow_fallbacks": False}

    client.verification = Verification()
    payload = client._payload(SYSTEM, USER, "nvidia/nemotron-3.5-super-vl:free")
    assert "reasoning" not in payload
    assert payload["provider"] == Verification().provider_policy("report")


def test_identical_inputs_hash_identically_and_retries_keep_one_hash():
    _, first, _, first_snapshots = run([ok])
    _, second, _, second_snapshots = run([ok])
    asyncio.run(first())
    asyncio.run(second())
    assert (
        first_snapshots[-1]["request_sha256"] == second_snapshots[-1]["request_sha256"]
    )

    unavailable = httpx.Response(503, json={"error": {"code": 503}})
    _, generate, requests, snapshots = run([unavailable, unavailable, unavailable])
    with pytest.raises(OpenRouterError):
        asyncio.run(generate())
    assert len(requests) == 3
    assert all(payload == requests[0] for payload in requests)
    assert "reasoning" in requests[0]
    assert {snapshot["request_sha256"] for snapshot in snapshots} == {
        digest(requests[0])
    }


@pytest.mark.parametrize("sibling", [False, True])
def test_length_finish_is_an_output_limit_rejection_without_retry_or_text(
    sibling, caplog
):
    choices = [{"finish_reason": "length", "message": {"content": "PARTIALMARKER"}}]
    if sibling:
        choices.append(
            {"finish_reason": "stop", "message": {"content": "COMPLETEMARKER"}}
        )
    response = httpx.Response(
        200,
        json={
            "model": ROUTE.removeprefix("openrouter/"),
            "choices": choices,
            "usage": {
                "completion_tokens": CAP,
                "completion_tokens_details": {"reasoning_tokens": 8000},
            },
        },
    )
    _, generate, requests, snapshots = run([response])
    with pytest.raises(OpenRouterOutputLimitExceeded):
        asyncio.run(generate())
    assert len(requests) == 1
    assert snapshots[-1]["state"] == "permanent_rejection"
    assert "PARTIALMARKER" not in caplog.text
    assert "COMPLETEMARKER" not in caplog.text


@pytest.mark.parametrize("status", [400, 404])
def test_provider_rejecting_the_parameter_is_terminal_with_no_second_send(status):
    rejection = httpx.Response(
        status,
        json={"error": {"code": status, "message": "parameter not supported"}},
    )
    _, generate, requests, snapshots = run([rejection, ok])
    with pytest.raises(OpenRouterError):
        asyncio.run(generate())
    assert len(requests) == 1
    assert requests[0]["reasoning"] == {"max_tokens": 8000}
    assert snapshots[-1]["state"] == "permanent_rejection"


def test_a_budget_not_below_the_cap_fails_before_any_reservation(monkeypatch):
    monkeypatch.setattr(openrouter_module, "REASONING_MAX_TOKENS", CAP)
    budget = AsyncMock()
    _, generate, requests, snapshots = run([ok], attempt_budget=budget)
    with pytest.raises(OpenRouterError):
        asyncio.run(generate())
    budget.reserve.assert_not_awaited()
    assert requests == [] and snapshots == []

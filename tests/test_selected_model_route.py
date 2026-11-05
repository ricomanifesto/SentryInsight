"""Selected paid routing remains an offline-only, fixed policy."""

import asyncio
from copy import deepcopy
import json
import os
from unittest.mock import patch

import httpx
import pytest

from src.core.model_client import build_model_client
from src.core.opencode_client import (
    ModelSelection,
    OpenCodeClient,
    parse_model_selection,
)
from src.core.openrouter_client import OpenRouterClient
from src.core.model_route import (
    KIMI_ROUTE,
    OFFLINE_KEY,
    RouteActivation,
    ModelRouteError,
)

MODEL = parse_model_selection("openrouter/" + KIMI_ROUTE.model_id)


def completion():
    return {
        "model": KIMI_ROUTE.model_id,
        "service_tier": "default",
        "choices": [{"finish_reason": "stop", "message": {"content": "report"}}],
        "usage": {
            "prompt_tokens": 5,
            "completion_tokens": 10,
            "completion_tokens_details": {"reasoning_tokens": 6},
            "total_tokens": 15,
            "cost": 0.00011,
        },
    }


def invoke(client, prompt="user"):
    return asyncio.run(
        client.generate(system_prompt="system", user_prompt=prompt, model=MODEL)
    )


def offline(handler, **kwargs):
    return build_model_client(
        timeout=120,
        max_tokens=32000,
        model=MODEL,
        activation=RouteActivation.OFFLINE,
        transport=httpx.MockTransport(handler),
        **kwargs,
    )


def test_selected_factory_is_disabled_before_key_access_or_gateway_selection():
    with (
        patch.dict(os.environ, {}, clear=True),
        patch(
            "src.core.model_client.os.getenv", side_effect=AssertionError("key access")
        ),
    ):
        with pytest.raises(ModelRouteError, match="disabled"):
            build_model_client(timeout=120, max_tokens=32000, model=MODEL)


def test_selected_route_cannot_use_direct_or_gateway_clients_without_offline_boundary():
    client = OpenRouterClient(
        api_key=OFFLINE_KEY, transport=httpx.MockTransport(lambda _: None)
    )
    with pytest.raises(ModelRouteError, match="disabled"):
        invoke(client)
    with pytest.raises(ModelRouteError, match="disabled"):
        invoke(OpenCodeClient())


def test_selected_payload_pins_endpoint_prices_privacy_standard_tier_and_markdown():
    requests = []

    def handler(request):
        requests.append(request)
        return httpx.Response(200, json=completion())

    client = offline(handler)
    assert invoke(client) == "report"
    payload = json.loads(requests[0].content)
    assert set(payload) == {
        "model",
        "max_tokens",
        "messages",
        "provider",
        "reasoning",
        "service_tier",
        "stream",
    }
    assert payload["model"] == KIMI_ROUTE.model_id
    assert payload["max_tokens"] == 32000
    assert payload["provider"] == {
        "only": ["moonshotai/mxfp4"],
        "allow_fallbacks": False,
        "require_parameters": True,
        "data_collection": "deny",
        "zdr": True,
        "max_price": {"prompt": 2, "completion": 10, "request": 0},
    }
    assert payload["reasoning"] == {"effort": "low", "exclude": True}
    assert payload["service_tier"] == "default"
    assert payload["stream"] is False
    assert str(requests[0].url) == "https://openrouter.ai/api/v1/chat/completions"
    assert client.last_request["usage"]["completion_tokens"] == 10
    assert client.last_request["usage"]["reasoning_tokens"] == 6


@pytest.mark.parametrize(
    "defect",
    [
        "length",
        "missing_finish",
        "error",
        "refusal",
        "model",
        "tier",
        "extra_choice",
        "reasoning_usage",
        "over_budget",
    ],
)
def test_selected_route_rejects_incomplete_or_mismatched_output_without_retry(defect):
    value = deepcopy(completion())
    choice = value["choices"][0]
    if defect == "length":
        choice["finish_reason"] = "length"
    elif defect == "missing_finish":
        del choice["finish_reason"]
    elif defect == "error":
        choice["error"] = {"message": "private provider body"}
    elif defect == "refusal":
        choice["message"]["refusal"] = "private provider body"
    elif defect == "model":
        value["model"] = "moonshotai/kimi-k3"
    elif defect == "tier":
        value["service_tier"] = "priority"
    elif defect == "extra_choice":
        value["choices"].append(deepcopy(choice))
    elif defect == "reasoning_usage":
        value["usage"]["completion_tokens_details"]["reasoning_tokens"] = 11
    else:
        value["usage"]["completion_tokens"] = 32001
    requests = []
    client = offline(
        lambda request: requests.append(request) or httpx.Response(200, json=value)
    )
    with pytest.raises(Exception) as failure:
        invoke(client)
    assert "private provider body" not in str(failure.value)
    assert len(requests) == 1
    with pytest.raises(Exception):
        invoke(client)
    assert len(requests) == 1


def test_selected_complete_messages_exceeding_input_bound_never_post():
    requests = []
    client = offline(lambda request: requests.append(request))
    with pytest.raises(ModelRouteError, match="input"):
        invoke(client, "token " * 200001)
    assert not requests


def test_offline_activation_rejects_real_transport_or_non_synthetic_key():
    client = OpenRouterClient(
        api_key="not-the-offline-key",
        activation=RouteActivation.OFFLINE,
        transport=httpx.MockTransport(lambda _: None),
    )
    with pytest.raises(ModelRouteError):
        invoke(client)
    with pytest.raises(ModelRouteError):
        build_model_client(
            timeout=120,
            max_tokens=32000,
            model=MODEL,
            activation=RouteActivation.OFFLINE,
        )


@pytest.mark.parametrize(
    "model_id",
    [
        "moonshotai/kimi-k3.1-pro:nitro",
        "moonshotai/kimi-k3.1-pro:floor",
        "moonshotai/kimi-k3.1-pro:online",
        "moonshotai/kimi-k3.1-pro-20261023",
        "MoonshotAI/Kimi-K3.1-Pro",
    ],
)
def test_selected_family_variants_cannot_bypass_factory_client_or_gateway(model_id):
    model = parse_model_selection("openrouter/" + model_id)
    requests = []

    class UntouchedBudget:
        async def reserve(self, *_args):
            raise AssertionError("selected variant touched the request budget")

    with patch(
        "src.core.model_client.os.getenv", side_effect=AssertionError("key access")
    ):
        with pytest.raises(ModelRouteError):
            build_model_client(timeout=120, max_tokens=32000, model=model)
    for client in (
        OpenCodeClient(),
        OpenRouterClient(
            api_key=OFFLINE_KEY,
            attempt_budget=UntouchedBudget(),
            transport=httpx.MockTransport(lambda request: requests.append(request)),
        ),
    ):
        with pytest.raises(ModelRouteError):
            asyncio.run(
                client.generate(system_prompt="system", user_prompt="user", model=model)
            )
    assert not requests


@pytest.mark.parametrize("subclass", [False, True])
def test_analyzer_cannot_send_selected_prompt_to_an_arbitrary_injected_client(
    tmp_path, subclass
):
    from src.core.analyze import analyze_exploitation

    class UnownedClient:
        async def generate(self, **kwargs):
            raise AssertionError("unowned client received source evidence")

    class OverriddenClient(OpenRouterClient):
        async def generate(self, **kwargs):
            raise AssertionError("subclass received source evidence")

    client = OverriddenClient(api_key=OFFLINE_KEY) if subclass else UnownedClient()

    result = asyncio.run(
        analyze_exploitation(
            [],
            {
                "output_path": str(tmp_path / "index.md"),
                "analysis": {"model": "openrouter/" + KIMI_ROUTE.model_id},
            },
            model_client=client,
        )
    )
    assert "disabled for injected clients" in result["error"]
    assert not list(tmp_path.iterdir())


@pytest.mark.parametrize(
    "raw_cap", [0, False, True, 0.0, 32000.0, "32000", "", None, 32001]
)
def test_analyzer_rejects_selected_raw_cap_before_coercion_and_preflight(
    tmp_path, raw_cap
):
    from src.core.analyze import analyze_exploitation

    result = asyncio.run(
        analyze_exploitation(
            [],
            {
                "output_path": str(tmp_path / "index.md"),
                "analysis": {
                    "model": "openrouter/" + KIMI_ROUTE.model_id,
                    "max_tokens": raw_cap,
                },
            },
        )
    )
    assert "output allowance is invalid" in result["error"]
    assert not list(tmp_path.iterdir())


@pytest.mark.parametrize(
    "owner,identifier",
    [
        ("moonshotai", "kimi-k3.1-pro"),
        ("moonshotai", "kimi-k3.1-pro:online"),
        ("anthropic", "moonshotai/kimi-k3.1-pro"),
        ("anthropic", "kimi-k3.1-pro"),
        (" openrouter ", "moonshotai/kimi-k3.1-pro"),
        ("openrouter", " moonshotai/kimi-k3.1-pro"),
        ("openrouter", "moonshotai/kimi-k3.1-pro "),
        ("openrouter", "moonshotai / kimi-k3.1-pro"),
        ("openrouter", "openrouter/moonshotai/kimi-k3.1-pro"),
    ],
)
def test_canonical_family_ownership_is_enforced_at_every_entrypoint(
    tmp_path, owner, identifier
):
    from src.core.analyze import analyze_exploitation

    model = ModelSelection(provider_id=owner, model_id=identifier)

    class UntouchedBudget:
        async def reserve(self, *_args):
            raise AssertionError("budget touched")

    class UnownedClient:
        async def generate(self, **kwargs):
            raise AssertionError("selected source prompt escaped")

    with patch(
        "src.core.model_client.os.getenv", side_effect=AssertionError("key access")
    ):
        with pytest.raises(ModelRouteError):
            build_model_client(timeout=120, max_tokens=32000, model=model)
    for client in (
        OpenCodeClient(),
        OpenRouterClient(
            api_key=OFFLINE_KEY,
            attempt_budget=UntouchedBudget(),
            transport=httpx.MockTransport(lambda _: pytest.fail("POST")),
        ),
    ):
        with pytest.raises(ModelRouteError):
            asyncio.run(
                client.generate(system_prompt="system", user_prompt="user", model=model)
            )
    result = asyncio.run(
        analyze_exploitation(
            [],
            {
                "output_path": str(tmp_path / "index.md"),
                "analysis": {"model": owner + "/" + identifier, "max_tokens": 32000},
            },
            model_client=UnownedClient(),
        )
    )
    assert result.get("error")
    assert not list(tmp_path.iterdir())


@pytest.mark.parametrize(
    "content",
    [
        [{"type": "image_url", "image_url": {"url": "https://example.test/a.png"}}],
        {"text": "user"},
        None,
    ],
)
def test_selected_route_refuses_non_text_content_before_post(content):
    requests = []
    client = offline(lambda request: requests.append(request))
    with pytest.raises(ModelRouteError, match="text-only"):
        invoke(client, content)
    assert not requests

import asyncio
import json
import traceback
import unittest
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime
from pathlib import Path
from unittest.mock import AsyncMock, patch

import httpx
import pytest

from src.core import openrouter_client as openrouter_client_module
from src.core.opencode_client import parse_model_selection
from src.core.openrouter_client import (
    OpenRouterClient,
    OpenRouterError,
    OpenRouterUnavailable,
)

FREE_MODEL = "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free"


@pytest.fixture(autouse=True)
def no_retry_wait(monkeypatch):
    sleep = AsyncMock()
    monkeypatch.setattr(asyncio, "sleep", sleep)
    return sleep


def generate_with_responses(responses):
    requests = []

    def handler(request):
        requests.append(request)
        response = responses[min(len(requests) - 1, len(responses) - 1)]
        if isinstance(response, Exception):
            raise response
        return response

    client = OpenRouterClient(
        api_key="secret-key", transport=httpx.MockTransport(handler)
    )

    async def generate():
        return await client.generate(
            system_prompt="private system prompt",
            user_prompt="private article contents",
            model=parse_model_selection(FREE_MODEL),
        )

    return generate, requests


def completion():
    return httpx.Response(
        200,
        json={
            "model": FREE_MODEL.removeprefix("openrouter/"),
            "choices": [{"message": {"content": "Generated report"}}],
        },
    )


@pytest.mark.parametrize("content", ["private incomplete report", "", None])
@pytest.mark.parametrize("complete_choice_first", [False, True])
def test_output_limit_rejects_partial_response_without_retry_or_content_logs(
    content, complete_choice_first, no_retry_wait, caplog
):
    from src.core.analysis_errors import classify_analysis_error

    choices = [{"finish_reason": "length", "message": {"content": content}}]
    if complete_choice_first:
        choices.insert(
            0,
            {"finish_reason": "stop", "message": {"content": "private full choice"}},
        )
    generate, requests = generate_with_responses(
        [httpx.Response(200, json={"choices": choices})]
    )

    with pytest.raises(OpenRouterError, match="output token limit") as raised:
        asyncio.run(generate())

    assert len(requests) == 1
    no_retry_wait.assert_not_awaited()
    assert classify_analysis_error(raised.value) == (
        "model_output_limit_exceeded",
        {"http_status": 200, "attempts": 1},
    )
    diagnostics = "".join(traceback.format_exception(raised.value)) + caplog.text
    for private_text in (
        "private incomplete report",
        "private full choice",
        "private article contents",
        "private system prompt",
        "secret-key",
    ):
        assert private_text not in diagnostics


def test_natural_stop_returns_the_complete_response():
    generate, requests = generate_with_responses(
        [
            httpx.Response(
                200,
                json={
                    "model": FREE_MODEL.removeprefix("openrouter/"),
                    "choices": [
                        {
                            "finish_reason": "stop",
                            "message": {"content": "Complete report"},
                        }
                    ],
                },
            )
        ]
    )
    assert asyncio.run(generate()) == "Complete report"
    assert len(requests) == 1


def test_default_analysis_sends_expanded_output_allowance_to_same_model(monkeypatch):
    from src.core import model_client
    from test_analyze_guards import import_analyze_with_stubs

    analyze = import_analyze_with_stubs()
    config = json.loads(
        (Path(__file__).resolve().parents[1] / "config/config.json").read_text()
    )
    requests = []

    def provider(request):
        requests.append(json.loads(request.content))
        return httpx.Response(
            200,
            json={
                # The provider echoes the configured production model.
                "model": requests[-1]["model"],
                "choices": [
                    {"finish_reason": "stop", "message": {"content": "Complete report"}}
                ],
            },
        )

    def client_with_mock_transport(**kwargs):
        return OpenRouterClient(transport=httpx.MockTransport(provider), **kwargs)

    monkeypatch.setenv("OPENROUTER_API_KEY", "test-key")
    monkeypatch.delenv("SENTRYINSIGHT_MODEL", raising=False)
    monkeypatch.setattr(model_client, "OpenRouterClient", client_with_mock_transport)
    monkeypatch.setattr(analyze, "build_model_client", model_client.build_model_client)

    result = asyncio.run(
        analyze.analyze_exploitation(
            [
                {
                    "title": "Synthetic",
                    "source": "Synthetic",
                    "link": "https://example.test/report",
                    "content": "A service advisory.",
                }
            ],
            config,
        )
    )

    assert "error" not in result
    assert result["exploitation_report"] == "Complete report"
    [request] = requests
    assert request["max_tokens"] == 96000
    assert "reasoning" not in request
    assert request["model"] == "nvidia/nemotron-3.5-super-vl:free"


@pytest.mark.parametrize(
    "response",
    [
        httpx.Response(200, json={"error": {"code": 429, "message": "private"}}),
        httpx.Response(200, json={"error": {"code": "503"}}),
        *[
            httpx.Response(code, json={"error": {"code": code}})
            for code in (408, 429, 500, 502, 503, 504)
        ],
        httpx.ConnectError("secret connection detail"),
    ],
)
def test_retryable_failure_recovers(response, no_retry_wait):
    generate, requests = generate_with_responses([response, completion()])

    assert asyncio.run(generate()) == "Generated report"
    assert len(requests) == 2
    no_retry_wait.assert_awaited_once_with(1.0)


@pytest.mark.parametrize(
    "response, diagnostic",
    [
        (httpx.Response(503, json={"error": {"code": 503}}), "HTTP 503"),
        (httpx.ConnectTimeout("secret timeout"), "OpenRouter API unavailable"),
    ],
)
def test_retry_exhaustion_is_bounded(response, diagnostic, no_retry_wait, caplog):
    generate, requests = generate_with_responses([response])

    with pytest.raises(OpenRouterError, match=diagnostic):
        asyncio.run(generate())

    assert len(requests) == 3
    assert [call.args[0] for call in no_retry_wait.await_args_list] == [1.0, 2.0]
    assert "attempt 3/3" in caplog.text
    assert "secret" not in caplog.text


@pytest.mark.parametrize("code", [400, 401, 402, 403, 404, 413, 422])
@pytest.mark.parametrize("http_status", [200, None])
def test_permanent_errors_are_not_retried(code, http_status, no_retry_wait, caplog):
    generate, requests = generate_with_responses(
        [
            httpx.Response(
                http_status or code,
                json={
                    "error": {
                        "code": code,
                        "message": "secret-key private article contents",
                        "metadata": {"raw": "private system prompt"},
                    }
                },
            )
        ]
    )

    with pytest.raises(OpenRouterError) as raised:
        asyncio.run(generate())

    assert len(requests) == 1
    no_retry_wait.assert_not_awaited()
    diagnostics = str(raised.value) + caplog.text
    assert f"HTTP {http_status or code}" in diagnostics
    assert f"provider_code={code}" in diagnostics
    for private_text in ("secret-key", "private article", "private system", "metadata"):
        assert private_text not in diagnostics


@pytest.mark.parametrize(
    "code", ["secret-key\nforged log", {"private": "payload"}, True, None]
)
def test_unknown_provider_error_is_sanitized_and_not_retried(
    code, no_retry_wait, caplog
):
    generate, requests = generate_with_responses(
        [httpx.Response(200, json={"error": {"code": code, "message": "secret-key"}})]
    )

    with pytest.raises(OpenRouterError, match="provider_code=unknown") as raised:
        asyncio.run(generate())

    assert len(requests) == 1
    no_retry_wait.assert_not_awaited()
    assert "secret-key" not in str(raised.value) + caplog.text
    assert "forged log" not in str(raised.value) + caplog.text


def test_transient_provider_error_diagnostics_do_not_log_payload(caplog):
    generate, requests = generate_with_responses(
        [httpx.Response(200, json={"error": {"code": 503, "message": "secret-key"}})]
    )

    with pytest.raises(OpenRouterError, match="provider_code=503") as raised:
        asyncio.run(generate())

    assert len(requests) == 3
    assert "HTTP 200" in str(raised.value)
    assert "provider_code=503" in caplog.text
    assert "secret-key" not in caplog.text + str(raised.value)


@pytest.mark.parametrize("status", [200, 429, 503])
def test_retry_after_is_honored(status, no_retry_wait):
    generate, requests = generate_with_responses(
        [
            httpx.Response(
                status, headers={"Retry-After": "5"}, json={"error": {"code": 503}}
            ),
            completion(),
        ]
    )

    assert asyncio.run(generate()) == "Generated report"
    assert len(requests) == 2
    no_retry_wait.assert_awaited_once_with(5.0)


def test_long_retry_after_stops_instead_of_retrying_early(no_retry_wait):
    generate, requests = generate_with_responses(
        [
            httpx.Response(
                429, headers={"Retry-After": "3600"}, json={"error": {"code": 429}}
            )
        ]
    )

    with pytest.raises(OpenRouterError, match="HTTP 429"):
        asyncio.run(generate())

    assert len(requests) == 1
    no_retry_wait.assert_not_awaited()


def test_retry_after_http_date_is_honored(no_retry_wait):
    now = datetime(2026, 9, 30, 12, 0, tzinfo=timezone.utc)
    retry_at = now + timedelta(seconds=20)
    generate, _ = generate_with_responses(
        [
            httpx.Response(
                503,
                headers={"Retry-After": format_datetime(retry_at)},
                json={"error": {"code": 503}},
            ),
            completion(),
        ]
    )

    with patch("src.core.openrouter_client.datetime") as clock:
        clock.now.return_value = now
        assert asyncio.run(generate()) == "Generated report"
    assert no_retry_wait.await_count == 1
    no_retry_wait.assert_awaited_once_with(20.0)


@pytest.mark.parametrize("error", [{}, {"message": "private provider details"}])
def test_http_transient_error_without_provider_code_stays_uncertain(error):
    generate, requests = generate_with_responses(
        [httpx.Response(503, json={"error": error}), completion()]
    )

    with pytest.raises(OpenRouterError):
        asyncio.run(generate())
    assert len(requests) == 1


def test_permanent_http_status_overrides_transient_provider_code(no_retry_wait):
    generate, requests = generate_with_responses(
        [httpx.Response(401, json={"error": {"code": 503}})]
    )
    with pytest.raises(OpenRouterError):
        asyncio.run(generate())
    assert len(requests) == 1
    no_retry_wait.assert_not_awaited()


def test_transport_traceback_does_not_expose_original_details(caplog):
    generate, _ = generate_with_responses(
        [httpx.ConnectError("private connection secret")]
    )
    with pytest.raises(OpenRouterUnavailable) as raised:
        asyncio.run(generate())
    diagnostics = "".join(traceback.format_exception(raised.value)) + caplog.text
    assert "private connection secret" not in diagnostics


def test_local_protocol_error_is_not_retried(no_retry_wait):
    generate, requests = generate_with_responses(
        [httpx.LocalProtocolError("private header")]
    )
    with pytest.raises(OpenRouterUnavailable):
        asyncio.run(generate())
    assert len(requests) == 1
    no_retry_wait.assert_not_awaited()


@pytest.mark.parametrize("retry_after", ["invalid private value", "NaN", "-1"])
def test_invalid_retry_after_uses_bounded_backoff(retry_after, no_retry_wait):
    generate, _ = generate_with_responses(
        [
            httpx.Response(
                429, headers={"Retry-After": retry_after}, json={"error": {"code": 429}}
            ),
            completion(),
        ]
    )

    assert asyncio.run(generate()) == "Generated report"
    no_retry_wait.assert_awaited_once_with(1.0)


def test_cancelled_request_is_not_retried(no_retry_wait):
    requests = []

    def handler(request):
        requests.append(request)
        raise asyncio.CancelledError()

    client = OpenRouterClient(api_key="test", transport=httpx.MockTransport(handler))
    with pytest.raises(asyncio.CancelledError):
        asyncio.run(
            client.generate(
                system_prompt="",
                user_prompt="",
                model=parse_model_selection(FREE_MODEL),
            )
        )

    assert len(requests) == 1
    no_retry_wait.assert_not_awaited()


class OpenRouterClientTests(unittest.TestCase):
    def test_generate_posts_chat_completion_with_model(self):
        requests = []

        def handler(request):
            requests.append(request)
            payload = json.loads(request.content.decode())
            self.assertEqual(payload["model"], "nvidia/nemotron-3-ultra-550b-a55b:free")
            self.assertEqual(payload["max_tokens"], 1234)
            self.assertEqual(
                payload["messages"][0], {"role": "system", "content": "system"}
            )
            self.assertEqual(
                payload["messages"][1], {"role": "user", "content": "user"}
            )
            return httpx.Response(
                200,
                json={
                    "model": FREE_MODEL.removeprefix("openrouter/"),
                    "choices": [{"message": {"content": "Generated report"}}],
                },
            )

        client = OpenRouterClient(
            api_key="secret-key",
            max_tokens=1234,
            transport=httpx.MockTransport(handler),
        )

        result = asyncio.run(
            client.generate(
                system_prompt="system",
                user_prompt="user",
                model=parse_model_selection(FREE_MODEL),
            )
        )

        self.assertEqual(result, "Generated report")
        self.assertEqual(requests[0].url.path, "/api/v1/chat/completions")
        self.assertEqual(requests[0].headers["Authorization"], "Bearer secret-key")

    def test_generate_redacts_failed_response_body(self):
        def handler(request):
            return httpx.Response(500, text="secret prompt fragment")

        client = OpenRouterClient(
            api_key="secret-key",
            transport=httpx.MockTransport(handler),
        )

        with self.assertRaisesRegex(
            OpenRouterError,
            r"OpenRouter chat completion failed: HTTP 500",
        ) as raised:
            asyncio.run(
                client.generate(
                    system_prompt="system",
                    user_prompt="user",
                    model=parse_model_selection(FREE_MODEL),
                )
            )

        self.assertNotIn("secret prompt fragment", str(raised.exception))
        self.assertNotIn("secret-key", str(raised.exception))

    def test_generate_classifies_connection_failure_as_unavailable(self):
        def handler(request):
            raise httpx.ConnectError("secret connection detail", request=request)

        client = OpenRouterClient(
            api_key="secret-key",
            transport=httpx.MockTransport(handler),
        )

        with self.assertRaisesRegex(
            OpenRouterUnavailable,
            "OpenRouter API unavailable",
        ) as raised:
            asyncio.run(
                client.generate(
                    system_prompt="system",
                    user_prompt="user",
                    model=parse_model_selection(FREE_MODEL),
                )
            )

        self.assertNotIn("secret connection detail", str(raised.exception))

    def test_generate_rejects_non_openrouter_model(self):
        def handler(request):
            raise AssertionError("must not call the API for a non-openrouter model")

        client = OpenRouterClient(
            api_key="secret-key",
            transport=httpx.MockTransport(handler),
        )

        with self.assertRaisesRegex(OpenRouterError, "openrouter"):
            asyncio.run(
                client.generate(
                    system_prompt="system",
                    user_prompt="user",
                    model=parse_model_selection("anthropic/claude-sonnet-4-6"),
                )
            )

    def test_generate_requires_text_output(self):
        def handler(request):
            return httpx.Response(200, json={"choices": [{"message": {"content": ""}}]})

        client = OpenRouterClient(
            api_key="secret-key",
            transport=httpx.MockTransport(handler),
        )

        with self.assertRaisesRegex(OpenRouterError, "did not include text output"):
            asyncio.run(
                client.generate(
                    system_prompt="system",
                    user_prompt="user",
                    model=parse_model_selection(FREE_MODEL),
                )
            )


if __name__ == "__main__":
    unittest.main()


@pytest.mark.parametrize(
    "response",
    [
        httpx.Response(200, json={}),
        httpx.Response(200, json={"choices": None}),
        httpx.Response(200, json={"choices": []}),
        httpx.Response(200, json=[]),
        httpx.Response(200, text="private invalid JSON"),
        httpx.ReadTimeout("private timeout details"),
    ],
)
def test_ambiguous_provider_completion_is_not_replayed(response, no_retry_wait):
    generate, requests = generate_with_responses([response, completion()])
    with pytest.raises(OpenRouterError):
        asyncio.run(generate())
    assert len(requests) == 1
    no_retry_wait.assert_not_awaited()


def test_usage_records_reasoning_tokens_latency_and_cap_headroom_without_text(caplog):
    client = OpenRouterClient(
        api_key="secret-key",
        max_tokens=32000,
        transport=httpx.MockTransport(
            lambda _request: httpx.Response(
                200,
                json={
                    "model": FREE_MODEL.removeprefix("openrouter/"),
                    "choices": [{"message": {"content": "private report body"}}],
                    "usage": {
                        "prompt_tokens": 62963,
                        "completion_tokens": 30000,
                        "total_tokens": 92963,
                        "cost": 0,
                        "completion_tokens_details": {"reasoning_tokens": 4000},
                        "prompt_tokens_details": {"cached_tokens": "invalid"},
                    },
                },
            )
        ),
    )

    with caplog.at_level("INFO", logger="src.core.openrouter_client"):
        asyncio.run(
            client.generate(
                system_prompt="private system prompt",
                user_prompt="private article contents",
                model=parse_model_selection(FREE_MODEL),
            )
        )

    assert client.last_request["usage"] == {
        "prompt_tokens": 62963,
        "completion_tokens": 30000,
        "reasoning_tokens": 4000,
        "total_tokens": 92963,
        "cost": 0,
    }
    elapsed = client.last_request["elapsed_seconds"]
    assert type(elapsed) is float and elapsed >= 0
    [line] = [r.getMessage() for r in caplog.records if "OpenRouter usage" in r.message]
    summary = json.loads(line.split(": ", 1)[1])
    assert summary["reasoning_tokens"] == 4000
    assert summary["cached_tokens"] is None
    assert summary["max_tokens_used_fraction"] == 0.938
    assert "private" not in caplog.text and "secret-key" not in caplog.text


def _usage_client(usage):
    return OpenRouterClient(
        api_key="secret-key",
        transport=httpx.MockTransport(
            lambda _request: httpx.Response(
                200,
                json={
                    "model": FREE_MODEL.removeprefix("openrouter/"),
                    "choices": [{"message": {"content": "report"}}],
                    "usage": usage,
                },
            )
        ),
    )


def _generate(client):
    return asyncio.run(
        client.generate(
            system_prompt="system",
            user_prompt="user",
            model=parse_model_selection(FREE_MODEL),
        )
    )


def test_top_level_reasoning_count_survives_details_without_that_count():
    client = _usage_client(
        {
            "completion_tokens": 10,
            "reasoning_tokens": 4,
            "completion_tokens_details": {"audio_tokens": 0},
        }
    )

    _generate(client)

    assert client.last_request["usage"] == {
        "completion_tokens": 10,
        "reasoning_tokens": 4,
    }


def test_a_usage_logging_failure_never_changes_the_request_outcome(monkeypatch):
    def broken(*_args, **_kwargs):
        raise RuntimeError("log sink failed")

    monkeypatch.setattr(openrouter_client_module.logger, "info", broken)
    client = _usage_client({"completion_tokens": 10})

    assert _generate(client) == "report"
    assert client.last_request["usage"] == {"completion_tokens": 10}


def test_reasoning_max_tokens_is_optional_and_off_by_default():
    seen = []

    def handler(request):
        seen.append(json.loads(request.content))
        return completion()

    default_client = OpenRouterClient(
        api_key="secret-key",
        max_tokens=96000,
        transport=httpx.MockTransport(handler),
    )
    explicit_client = OpenRouterClient(
        api_key="secret-key",
        max_tokens=96000,
        reasoning_max_tokens=24000,
        transport=httpx.MockTransport(handler),
    )

    assert _generate(default_client) == "Generated report"
    assert _generate(explicit_client) == "Generated report"
    assert "reasoning" not in seen[0]
    assert seen[0]["max_tokens"] == 96000
    assert seen[1]["reasoning"] == {"max_tokens": 24000}

    for bad in (0, -1, 96000, 96001, True, False, "24000", 24000.0):
        with pytest.raises(ValueError, match="reasoning_max_tokens"):
            OpenRouterClient(
                api_key="secret-key",
                max_tokens=96000,
                reasoning_max_tokens=bad,  # type: ignore[arg-type]
            )
    with pytest.raises(ValueError, match="recovery_max_tokens"):
        OpenRouterClient(
            api_key="secret-key",
            max_tokens=96000,
            recovery_max_tokens=64000,
        )


def test_output_limit_recovery_raises_budget_without_capping_reasoning_and_logs_advisory(
    no_retry_wait, caplog
):
    payloads = []
    responses = [
        httpx.Response(
            200,
            json={
                "model": FREE_MODEL.removeprefix("openrouter/"),
                "choices": [
                    {
                        "finish_reason": "length",
                        "message": {"content": "private truncated draft"},
                    }
                ],
                "usage": {
                    "prompt_tokens": 74796,
                    "completion_tokens": 96000,
                    "total_tokens": 170796,
                    "cost": 0,
                    "completion_tokens_details": {"reasoning_tokens": 89000},
                },
            },
        ),
        httpx.Response(
            200,
            json={
                "model": FREE_MODEL.removeprefix("openrouter/"),
                "choices": [
                    {
                        "finish_reason": "stop",
                        "message": {"content": "Complete recovered report"},
                    }
                ],
                "usage": {
                    "prompt_tokens": 74796,
                    "completion_tokens": 102000,
                    "completion_tokens_details": {"reasoning_tokens": 95000},
                },
            },
        ),
    ]

    def handler(request):
        payloads.append(json.loads(request.content))
        return responses[len(payloads) - 1]

    client = OpenRouterClient(
        api_key="secret-key",
        max_tokens=96000,
        recovery_max_tokens=131072,
        timeout=1800.0,
        total_timeout=3600.0,
        transport=httpx.MockTransport(handler),
    )

    with caplog.at_level("INFO", logger="src.core.openrouter_client"):
        result = asyncio.run(
            client.generate(
                system_prompt="private system prompt",
                user_prompt="private article contents",
                model=parse_model_selection(FREE_MODEL),
            )
        )

    assert result == "Complete recovered report"
    assert len(payloads) == 2
    assert payloads[0]["max_tokens"] == 96000
    assert payloads[1]["max_tokens"] == 131072
    assert payloads[1]["max_tokens"] >= payloads[0]["max_tokens"]
    assert "reasoning" not in payloads[0]
    assert "reasoning" not in payloads[1]
    assert payloads[1]["messages"][0]["content"] == "private system prompt"
    assert client.last_request["attempts"] == 2
    assert client.last_request["state"] == "response_received"
    no_retry_wait.assert_not_awaited()

    usage_lines = [
        json.loads(r.getMessage().split(": ", 1)[1])
        for r in caplog.records
        if "OpenRouter usage" in r.message
    ]
    assert len(usage_lines) == 2
    assert usage_lines[0]["max_tokens"] == 96000
    assert usage_lines[0]["timeout_seconds"] == 1800.0
    assert usage_lines[0]["max_tokens_used_fraction"] == 1.0
    assert usage_lines[1]["max_tokens"] == 131072
    assert usage_lines[1]["timeout_seconds"] <= 1800.0
    assert usage_lines[1]["max_tokens_used_fraction"] == round(102000 / 131072, 3)

    [line] = [
        r.getMessage()
        for r in caplog.records
        if "OpenRouter output-limit recovery advisory" in r.message
    ]
    advisory = json.loads(line.split(": ", 1)[1])
    assert advisory["event"] == "output_limit_recovery"
    assert advisory["attempt"] == 1
    assert advisory["next_attempt"] == 2
    assert advisory["max_attempts"] == 3
    assert advisory["previous_max_tokens"] == 96000
    assert advisory["recovery_max_tokens"] == 131072
    assert advisory["reasoning_capped"] is False
    assert advisory["attempt_timeout_seconds"] == 1800.0
    assert advisory["next_attempt_timeout_seconds"] <= 1800.0
    assert advisory["usage"]["reasoning_tokens"] == 89000
    assert advisory["usage"]["completion_tokens"] == 96000
    for private_text in (
        "private truncated draft",
        "private system prompt",
        "private article contents",
        "Complete recovered report",
        "secret-key",
    ):
        assert private_text not in caplog.text


def test_two_length_limited_responses_fail_with_output_limit_error(
    no_retry_wait, caplog
):
    from src.core.analysis_errors import classify_analysis_error
    from src.core.attempt_budget import AttemptBudgetError, MemoryAttemptBudget
    from src.core.openrouter_client import OpenRouterOutputLimitExceeded

    payloads = []

    def handler(request):
        payloads.append(json.loads(request.content))
        return httpx.Response(
            200,
            json={
                "model": FREE_MODEL.removeprefix("openrouter/"),
                "choices": [
                    {
                        "finish_reason": "length",
                        "message": {
                            "content": f"private truncated attempt {len(payloads)}"
                        },
                    }
                ],
                "usage": {
                    "prompt_tokens": 74796,
                    "completion_tokens": payloads[-1]["max_tokens"],
                    "completion_tokens_details": {"reasoning_tokens": 80000},
                },
            },
        )

    budget = MemoryAttemptBudget()
    client = OpenRouterClient(
        api_key="secret-key",
        max_tokens=96000,
        recovery_max_tokens=131072,
        attempt_budget=budget,
        transport=httpx.MockTransport(handler),
    )

    with pytest.raises(
        OpenRouterOutputLimitExceeded, match="output token limit"
    ) as raised:
        asyncio.run(
            client.generate(
                system_prompt="private system prompt",
                user_prompt="private article contents",
                model=parse_model_selection(FREE_MODEL),
            )
        )

    assert len(payloads) == 2
    assert [p["max_tokens"] for p in payloads] == [96000, 131072]
    assert all("reasoning" not in p for p in payloads)
    no_retry_wait.assert_not_awaited()
    assert classify_analysis_error(raised.value) == (
        "model_output_limit_exceeded",
        {"http_status": 200, "attempts": 2},
    )
    assert budget.disposition == "permanent_rejection"
    with pytest.raises(AttemptBudgetError):
        _generate(client)
    diagnostics = "".join(traceback.format_exception(raised.value)) + caplog.text
    for private_text in (
        "private truncated attempt 1",
        "private truncated attempt 2",
        "private system prompt",
        "private article contents",
        "secret-key",
    ):
        assert private_text not in diagnostics


@pytest.mark.parametrize("second_finishes", [True, False])
def test_production_analysis_recovers_once_and_fails_on_second_length_limit(
    second_finishes, monkeypatch, tmp_path
):
    from src.core import analyze, model_client

    config = json.loads(
        (Path(__file__).resolve().parents[1] / "config/config.json").read_text()
    )
    config["output_path"] = str(tmp_path / "index.md")
    requests = []

    def provider(request):
        payload = json.loads(request.content)
        requests.append(payload)
        if len(requests) == 1 or not second_finishes:
            return httpx.Response(
                200,
                json={
                    "model": payload["model"],
                    "choices": [
                        {
                            "finish_reason": "length",
                            "message": {"content": "TRUNCATED_PARTIAL_MARKER"},
                        }
                    ],
                    "usage": {
                        "prompt_tokens": 74796,
                        "completion_tokens": payload["max_tokens"],
                        "completion_tokens_details": {"reasoning_tokens": 85000},
                    },
                },
            )
        return httpx.Response(
            200,
            json={
                "model": payload["model"],
                "choices": [
                    {
                        "finish_reason": "stop",
                        "message": {"content": "Recovered report"},
                    }
                ],
            },
        )

    def client_with_mock_transport(**kwargs):
        return OpenRouterClient(transport=httpx.MockTransport(provider), **kwargs)

    monkeypatch.setenv("OPENROUTER_API_KEY", "test-key")
    monkeypatch.delenv("SENTRYINSIGHT_MODEL", raising=False)
    monkeypatch.setattr(model_client, "OpenRouterClient", client_with_mock_transport)
    monkeypatch.setattr(analyze, "build_model_client", model_client.build_model_client)

    result = asyncio.run(
        analyze.analyze_exploitation(
            [
                {
                    "title": "Synthetic",
                    "source": "Synthetic",
                    "link": "https://example.test/report",
                    "content": "A service advisory.",
                }
            ],
            config,
        )
    )

    assert len(requests) == 2
    assert requests[0]["max_tokens"] == 96000
    assert requests[1]["max_tokens"] == 131072
    assert "reasoning" not in requests[0]
    assert "reasoning" not in requests[1]
    assert "TRUNCATED_PARTIAL_MARKER" not in json.dumps(result)
    if second_finishes:
        assert "error" not in result
        assert result["exploitation_report"] == "Recovered report"
    else:
        assert result["error_class"] == "model_output_limit_exceeded"
        assert result["error_detail"] == {"http_status": 200, "attempts": 2}


def test_output_limit_recovery_respects_single_attempt_and_job_timeout_budget(
    monkeypatch, caplog
):
    from src.core.analyze import analysis_timeout_budget
    from src.core.openrouter_client import OpenRouterOutputLimitExceeded

    single_calls = []

    def single_handler(request):
        single_calls.append(request)
        return httpx.Response(
            200,
            json={
                "model": FREE_MODEL.removeprefix("openrouter/"),
                "choices": [
                    {"finish_reason": "length", "message": {"content": "partial"}}
                ],
            },
        )

    single_client = OpenRouterClient(
        api_key="secret-key",
        max_tokens=96000,
        recovery_max_tokens=131072,
        max_attempts=1,
        transport=httpx.MockTransport(single_handler),
    )
    with pytest.raises(OpenRouterOutputLimitExceeded) as raised:
        _generate(single_client)
    assert len(single_calls) == 1
    assert raised.value.attempts == 1

    # Simulate an attempt that leaves less than MIN_RECOVERY_TIMEOUT_SECONDS remaining.
    clock = [1000.0]
    monkeypatch.setattr(openrouter_client_module.time, "monotonic", lambda: clock[0])
    timeout_calls = []

    def slow_handler(request):
        timeout_calls.append(request)
        clock[0] += 100.0
        return httpx.Response(
            200,
            json={
                "model": FREE_MODEL.removeprefix("openrouter/"),
                "choices": [
                    {"finish_reason": "length", "message": {"content": "partial"}}
                ],
            },
        )

    bounded_client = OpenRouterClient(
        api_key="secret-key",
        max_tokens=96000,
        recovery_max_tokens=131072,
        timeout=1800.0,
        total_timeout=180.0,
        transport=httpx.MockTransport(slow_handler),
    )
    with caplog.at_level("WARNING", logger="src.core.openrouter_client"):
        with pytest.raises(OpenRouterOutputLimitExceeded) as raised:
            _generate(bounded_client)
    assert len(timeout_calls) == 1
    assert raised.value.attempts == 1
    assert "timeout_budget_exhausted" in caplog.text

    # When time remains, attempt 2's HTTP timeout is clamped to remaining budget.
    clock[0] = 2000.0
    observed_timeouts = []

    def clamped_handler(request):
        observed_timeouts.append(request.extensions["timeout"]["read"])
        if len(observed_timeouts) == 1:
            clock[0] += 2100.0
            return httpx.Response(
                200,
                json={
                    "model": FREE_MODEL.removeprefix("openrouter/"),
                    "choices": [
                        {"finish_reason": "length", "message": {"content": "partial"}}
                    ],
                },
            )
        return completion()

    clamped_client = OpenRouterClient(
        api_key="secret-key",
        max_tokens=96000,
        recovery_max_tokens=131072,
        timeout=1800.0,
        total_timeout=3600.0,
        transport=httpx.MockTransport(clamped_handler),
    )
    assert _generate(clamped_client) == "Generated report"
    assert observed_timeouts == [1800.0, 1500.0]

    # Budget math keeps initial + recovery attempts well inside the 75-minute CI job.
    per_request, total = analysis_timeout_budget(96000)
    assert per_request == 1800.0
    assert total == 3600.0
    assert analysis_timeout_budget(32000) == (640.0, 1280.0)
    workflow_text = (
        Path(__file__).resolve().parents[1] / ".github/workflows/generate-report.yml"
    ).read_text()
    assert "timeout-minutes: 75" in workflow_text
    assert total <= (75 - 15) * 60


def test_analyze_rejects_invalid_reasoning_max_tokens_before_provider_call(
    monkeypatch, tmp_path
):
    from src.core import analyze

    called = []
    monkeypatch.setattr(
        analyze, "build_model_client", lambda **kwargs: called.append(kwargs)
    )

    result = asyncio.run(
        analyze.analyze_exploitation(
            [
                {
                    "title": "Synthetic",
                    "source": "Synthetic",
                    "link": "https://example.test/report",
                    "content": "A service advisory.",
                }
            ],
            {
                "output_path": str(tmp_path / "index.md"),
                "analysis": {
                    "model": FREE_MODEL,
                    "max_tokens": 96000,
                    "reasoning_max_tokens": 96000,
                },
            },
        )
    )

    assert not called
    assert result["error_class"] == "analysis_exception"
    assert "reasoning_max_tokens" in result["error"]

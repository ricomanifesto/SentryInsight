import asyncio
import json
import traceback
import unittest
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime
from unittest.mock import AsyncMock, patch

import httpx
import pytest

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
        200, json={"choices": [{"message": {"content": "Generated report"}}]}
    )


@pytest.mark.parametrize(
    "response",
    [
        httpx.Response(200, json={}),
        httpx.Response(200, json={"choices": None}),
        httpx.Response(200, json={"choices": []}),
        httpx.Response(200, json=[]),
        httpx.Response(200, text="private invalid JSON"),
        httpx.Response(200, json={"error": {"code": 429, "message": "private"}}),
        httpx.Response(200, json={"error": {"code": "503"}}),
        *[httpx.Response(code) for code in (408, 429, 500, 502, 503, 504)],
        httpx.ConnectError("secret connection detail"),
        httpx.ReadTimeout("private timeout details"),
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
        (httpx.Response(200, json={}), "did not include choices"),
        (httpx.Response(503), "HTTP 503"),
        (httpx.ReadTimeout("secret timeout"), "OpenRouter API unavailable"),
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
        [httpx.Response(status, headers={"Retry-After": "5"}, json={}), completion()]
    )

    assert asyncio.run(generate()) == "Generated report"
    assert len(requests) == 2
    no_retry_wait.assert_awaited_once_with(5.0)


def test_long_retry_after_stops_instead_of_retrying_early(no_retry_wait):
    generate, requests = generate_with_responses(
        [httpx.Response(429, headers={"Retry-After": "3600"})]
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
            httpx.Response(503, headers={"Retry-After": format_datetime(retry_at)}),
            completion(),
        ]
    )

    with patch("src.core.openrouter_client.datetime") as clock:
        clock.now.return_value = now
        assert asyncio.run(generate()) == "Generated report"
    assert no_retry_wait.await_count == 1
    no_retry_wait.assert_awaited_once_with(20.0)


@pytest.mark.parametrize("error", [{}, {"message": "private provider details"}])
def test_http_transient_error_without_provider_code_retries(error):
    generate, requests = generate_with_responses(
        [httpx.Response(503, json={"error": error}), completion()]
    )

    assert asyncio.run(generate()) == "Generated report"
    assert len(requests) == 2


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
        [httpx.Response(429, headers={"Retry-After": retry_after}), completion()]
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
                json={"choices": [{"message": {"content": "Generated report"}}]},
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

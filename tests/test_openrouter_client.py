import asyncio
import json
import unittest

import httpx

from src.core.opencode_client import parse_model_selection
from src.core.openrouter_client import (
    OpenRouterClient,
    OpenRouterError,
    OpenRouterUnavailable,
)

FREE_MODEL = "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free"


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

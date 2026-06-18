import asyncio
import json
import unittest

import httpx

from src.core.opencode_client import OpenCodeClient, parse_model_selection


class OpenCodeClientTests(unittest.TestCase):
    def test_generate_posts_session_message_with_model(self):
        requests = []

        def handler(request):
            requests.append(request)
            if request.url.path == "/session":
                return httpx.Response(200, json={"id": "session-1"})
            if request.url.path == "/session/session-1/message":
                payload = json.loads(request.content.decode())
                self.assertEqual(
                    payload["model"],
                    {"providerID": "openai", "modelID": "gpt-5"},
                )
                return httpx.Response(
                    200,
                    json={
                        "info": {"id": "message-1"},
                        "parts": [{"type": "text", "text": "Generated report"}],
                    },
                )
            return httpx.Response(404)

        client = OpenCodeClient(
            base_url="http://opencode.test",
            transport=httpx.MockTransport(handler),
        )

        result = asyncio.run(
            client.generate(
                system_prompt="system",
                user_prompt="user",
                model=parse_model_selection("openai/gpt-5"),
            )
        )

        self.assertEqual(result, "Generated report")
        self.assertEqual(
            [request.url.path for request in requests],
            ["/session", "/session/session-1/message"],
        )

    def test_generate_redacts_failed_response_body(self):
        def handler(request):
            if request.url.path == "/session":
                return httpx.Response(500, text="secret prompt fragment")
            return httpx.Response(404)

        client = OpenCodeClient(
            base_url="http://opencode.test",
            transport=httpx.MockTransport(handler),
        )

        with self.assertRaisesRegex(
            Exception,
            r"Failed to create OpenCode session: HTTP 500",
        ) as raised:
            asyncio.run(
                client.generate(
                    system_prompt="system",
                    user_prompt="user",
                    model=parse_model_selection("openai/gpt-5"),
                )
            )

        self.assertNotIn("secret prompt fragment", str(raised.exception))


if __name__ == "__main__":
    unittest.main()

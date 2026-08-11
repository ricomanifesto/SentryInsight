import asyncio
from types import SimpleNamespace
import unittest

import httpx
import openai

from src.core.openai_client import (
    OpenAIClient,
    OpenAIError,
    OpenAIUnavailable,
)


class FakeResponses:
    def __init__(self, outcome):
        self.outcome = outcome
        self.calls = []

    async def create(self, **kwargs):
        self.calls.append(kwargs)
        if isinstance(self.outcome, Exception):
            raise self.outcome
        return self.outcome


class FakeAsyncOpenAI:
    def __init__(self, outcome):
        self.responses = FakeResponses(outcome)


class OpenAIClientTests(unittest.TestCase):
    def test_generate_uses_responses_api_with_sol_and_xhigh_reasoning(self):
        sdk_client = FakeAsyncOpenAI(SimpleNamespace(output_text="Generated report"))
        client = OpenAIClient(
            max_output_tokens=16_000,
            reasoning_effort="xhigh",
            sdk_client=sdk_client,
        )

        result = asyncio.run(
            client.generate(
                system_prompt="system",
                user_prompt="user",
                model="gpt-5.6-sol",
                title="SentryInsight report",
            )
        )

        self.assertEqual(result, "Generated report")
        self.assertEqual(
            sdk_client.responses.calls,
            [
                {
                    "model": "gpt-5.6-sol",
                    "instructions": "system",
                    "input": "user",
                    "max_output_tokens": 16_000,
                    "reasoning": {"effort": "xhigh"},
                    "metadata": {"request_title": "SentryInsight report"},
                }
            ],
        )

    def test_generate_redacts_failed_response_body(self):
        request = httpx.Request("POST", "https://api.openai.com/v1/responses")
        response = httpx.Response(500, request=request)
        error = openai.InternalServerError(
            "secret prompt fragment",
            response=response,
            body={"error": "secret prompt fragment"},
        )
        client = OpenAIClient(
            max_output_tokens=16_000,
            reasoning_effort="xhigh",
            sdk_client=FakeAsyncOpenAI(error),
        )

        with self.assertRaisesRegex(
            OpenAIError, r"OpenAI response failed: HTTP 500"
        ) as raised:
            asyncio.run(
                client.generate(
                    system_prompt="system",
                    user_prompt="user",
                    model="gpt-5.6-sol",
                )
            )

        self.assertNotIn("secret prompt fragment", str(raised.exception))

    def test_generate_classifies_connection_failure_as_unavailable(self):
        request = httpx.Request("POST", "https://api.openai.com/v1/responses")
        error = openai.APIConnectionError(
            message="secret connection detail", request=request
        )
        client = OpenAIClient(
            max_output_tokens=16_000,
            reasoning_effort="xhigh",
            sdk_client=FakeAsyncOpenAI(error),
        )

        with self.assertRaisesRegex(
            OpenAIUnavailable, "OpenAI API unavailable"
        ) as raised:
            asyncio.run(
                client.generate(
                    system_prompt="system",
                    user_prompt="user",
                    model="gpt-5.6-sol",
                )
            )

        self.assertNotIn("secret connection detail", str(raised.exception))

    def test_generate_requires_text_output(self):
        client = OpenAIClient(
            max_output_tokens=16_000,
            reasoning_effort="xhigh",
            sdk_client=FakeAsyncOpenAI(SimpleNamespace(output_text="")),
        )

        with self.assertRaisesRegex(OpenAIError, "did not include text output"):
            asyncio.run(
                client.generate(
                    system_prompt="system",
                    user_prompt="user",
                    model="gpt-5.6-sol",
                )
            )


if __name__ == "__main__":
    unittest.main()

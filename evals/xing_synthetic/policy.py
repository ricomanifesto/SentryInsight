"""Own the fixed recipient, input budget and request/receipt boundary."""

import hashlib
from copy import deepcopy
import json
import math
import re
from pathlib import Path
from typing import Any

import httpx

MODEL = "xingchen-agi/xing4.0-29b-a4b:free"
API = "https://openrouter.ai/api/v1/chat/completions"
ENDPOINTS = f"https://openrouter.ai/api/v1/models/{MODEL}/endpoints"
ZDR = "https://openrouter.ai/api/v1/endpoints/zdr"
MAX_REQUESTS = 6
MAX_INPUT = 200_000
MAX_OUTPUT = 32_000
CONTEXT = 262_144
FRAMING_RESERVE = 2_048
MAX_RESPONSE_BYTES = 512 * 1024
TOKENIZER_SHA = "fdcbbfdf8655a2e8b8a9fe478de0e9347e857c9b043f9752d04ed660286c3ac5"
TOKENIZER_URL = (
    "https://huggingface.co/XingChen-AGI/Xing4.0-29B-A4B/resolve/"
    "a32a2e99b5877c6b7ad16e9954ec08488bcc5fa2/tokenizer.model"
)
PROVIDER = {
    "only": ["phala"],
    "allow_fallbacks": False,
    "require_parameters": True,
    "data_collection": "deny",
    "zdr": True,
    "max_price": {"prompt": 0, "completion": 0, "request": 0, "image": 0},
}


class PilotError(RuntimeError):
    """Only host-owned codes cross the logging boundary."""

    def __init__(self, code: str, metadata: dict | None = None):
        super().__init__(code)
        self.metadata = metadata or {}


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


class TokenBudget:
    def __init__(self, path: Path):
        data = path.read_bytes()
        if hashlib.sha256(data).hexdigest() != TOKENIZER_SHA:
            raise PilotError("tokenizer_identity")
        # Only the explicit calibration/run path loads the native tokenizer.
        import sentencepiece

        self.processor = sentencepiece.SentencePieceProcessor()
        self.processor.LoadFromSerializedProto(data)

    def count(self, messages: list[dict[str, str]]) -> int:
        # The provider does not publish its chat template. Count all text using
        # the pinned author tokenizer, reserve framing separately, and retain
        # another 30,144 tokens of context headroom. This is not an exact server
        # usage claim; actual usage is checked after completion, without retry.
        return FRAMING_RESERVE + sum(
            len(self.processor.EncodeAsIds(m["content"])) for m in messages
        )


def payload_for(messages: list[dict[str, str]], budget: TokenBudget) -> dict:
    if [m.get("role") for m in messages] != ["system", "user"] or any(
        set(m) != {"role", "content"}
        or not isinstance(m["content"], str)
        or not m["content"].strip()
        for m in messages
    ):
        raise PilotError("invalid_messages")
    count = budget.count(messages)
    if not 0 < count <= MAX_INPUT or count + MAX_OUTPUT > CONTEXT:
        raise PilotError("input_budget")
    return {
        "model": MODEL,
        "messages": messages,
        "max_tokens": MAX_OUTPUT,
        "temperature": 1,
        "reasoning": {"enabled": True, "exclude": True},
        "provider": deepcopy(PROVIDER),
        "stream": False,
    }


def validate_payload(payload: dict) -> None:
    expected = {
        "model": MODEL,
        "max_tokens": MAX_OUTPUT,
        "temperature": 1,
        "reasoning": {"enabled": True, "exclude": True},
        "provider": PROVIDER,
        "stream": False,
    }
    if set(payload) != {*expected, "messages"} or any(
        payload.get(key) != value for key, value in expected.items()
    ):
        raise PilotError("request_policy")


def validate_endpoint_policy(endpoints: dict, zdr: dict) -> None:
    """Unknown/missing safety, pricing, parameter or identity facts fail closed."""
    try:
        rows = endpoints["data"]["endpoints"]
        eligible = [r for r in rows if r["tag"] == "phala"]
        if len(eligible) != 1:
            raise ValueError
        row = eligible[0]
        retained = [
            r
            for r in zdr["data"]
            if r.get("model_id") == MODEL and r.get("tag") == "phala"
        ]
        if (
            endpoints["data"]["id"] != MODEL
            or row["model_id"] != MODEL
            or row["provider_name"] != "Phala"
            or row["status"] != 0
            or row["context_length"] < CONTEXT
            or row["max_completion_tokens"] < MAX_OUTPUT
            or not {"max_tokens", "reasoning", "temperature"}
            <= set(row["supported_parameters"])
            or len(retained) != 1
            or retained[0].get("safety_retention") is not False
            or retained[0].get("provider_name") != "Phala"
        ):
            raise ValueError
        prices = row["pricing"]
        for required in ("prompt", "completion"):
            if required not in prices:
                raise ValueError
        for key, value in prices.items():
            if key == "discount":
                continue
            if isinstance(value, bool) or float(value) != 0:
                raise ValueError
    except (KeyError, TypeError, ValueError, OverflowError):
        raise PilotError("endpoint_policy") from None


async def bounded_json(client: httpx.AsyncClient, method: str, url: str, **kwargs):
    """No redirects, retries, raw provider errors or unbounded response bodies."""
    try:
        async with client.stream(method, url, **kwargs) as response:
            if response.status_code != 200:
                raise PilotError(
                    "provider_http_status", {"http_status": response.status_code}
                )
            body = bytearray()
            async for chunk in response.aiter_bytes():
                body.extend(chunk)
                if len(body) > MAX_RESPONSE_BYTES:
                    raise PilotError("response_size")
            value = json.loads(body)
            if not isinstance(value, dict):
                raise PilotError("response_shape")
            return value
    except (httpx.HTTPError, ValueError, UnicodeError):
        raise PilotError("provider_transport_or_json") from None


async def check_policy(client: httpx.AsyncClient) -> None:
    endpoints = await bounded_json(client, "GET", ENDPOINTS)
    # The full retention directory is larger than a completion. GET it through
    # a separately bounded reader; never attach the inference credential.
    try:
        async with client.stream("GET", ZDR) as response:
            if response.status_code != 200:
                raise PilotError("endpoint_policy")
            data = bytearray()
            async for chunk in response.aiter_bytes():
                data.extend(chunk)
                if len(data) > 16 * 1024 * 1024:
                    raise PilotError("endpoint_policy")
            retained = json.loads(data)
    except (httpx.HTTPError, ValueError, UnicodeError):
        raise PilotError("endpoint_policy") from None
    validate_endpoint_policy(endpoints, retained)


def completion(data: dict, secret: str) -> tuple[str, dict]:
    """Retain sanitized usage on rejection, never arbitrary provider strings."""
    safe: dict = {"http_status": 200}
    try:
        usage = data.get("usage") or {}
        safe_usage = {}
        for field in ("prompt_tokens", "completion_tokens", "total_tokens", "cost"):
            value = usage.get(field)
            if value is not None and (
                isinstance(value, bool)
                or not isinstance(value, (int, float))
                or not math.isfinite(value)
                or value < 0
                or (field != "cost" and int(value) != value)
            ):
                raise PilotError("invalid_usage", safe)
            safe_usage[field] = value
        reasoning = (usage.get("completion_tokens_details") or {}).get(
            "reasoning_tokens"
        )
        if reasoning is not None and (type(reasoning) is not int or reasoning < 0):
            raise PilotError("invalid_usage", safe)
        safe_usage["reasoning_tokens"] = reasoning
        safe["usage"] = safe_usage
        identifier = data.get("id")
        if (
            not isinstance(identifier, str)
            or not re.fullmatch(r"gen-[A-Za-z0-9_-]{1,100}", identifier)
            or secret in identifier
        ):
            identifier = None
        safe["response_id"] = identifier
        choices = data["choices"]
        if len(choices) != 1:
            raise PilotError("response_shape", safe)
        finish = choices[0].get("finish_reason")
        safe["finish_reason"] = (
            finish
            if finish in {"stop", "length", "content_filter", "error", "tool_calls"}
            else "invalid"
        )
        if data.get("model") not in {MODEL, MODEL.removesuffix(":free")}:
            raise PilotError("model_mismatch", safe)
        if data.get("provider") != "Phala":
            raise PilotError("provider_mismatch", safe)
        safe.update(model=MODEL, provider="Phala")
        if safe_usage["cost"] not in (None, 0):
            raise PilotError("unexpected_cost", safe)
        if (safe_usage["prompt_tokens"] or 0) > MAX_INPUT:
            raise PilotError("provider_input_budget", safe)
        if (safe_usage["completion_tokens"] or 0) > MAX_OUTPUT:
            raise PilotError("provider_output_budget", safe)
        if finish != "stop":
            raise PilotError("incomplete_completion", safe)
        message = choices[0]["message"]
        text = message.get("content")
        if (
            not isinstance(text, str)
            or not text.strip()
            or len(text.encode()) > MAX_RESPONSE_BYTES
            or secret in text
            or message.get("tool_calls")
        ):
            raise PilotError("invalid_completion", safe)
        return text, safe
    except (KeyError, TypeError, IndexError, AttributeError):
        raise PilotError("response_shape", safe) from None

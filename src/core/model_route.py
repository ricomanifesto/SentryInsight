"""Fixed Kimi route, prepared offline without enabling paid execution."""

from dataclasses import dataclass
from enum import Enum
import math

import httpx

OFFLINE_KEY = "offline-synthetic-key"
ENDPOINT_BASE = "https://openrouter.ai/api/v1"


class RouteActivation(Enum):
    DISABLED = "disabled"
    OFFLINE = "offline"


class ModelRouteError(ValueError):
    """Static refusal that contains no prompt, answer or provider body."""


@dataclass(frozen=True)
class ModelRoutePolicy:
    model_id: str
    endpoint: str
    context_tokens: int
    max_output_tokens: int
    max_input_tokens: int

    def provider_payload(self) -> dict:
        return {
            "only": [self.endpoint],
            "allow_fallbacks": False,
            "require_parameters": True,
            "data_collection": "deny",
            "zdr": True,
            "max_price": {"prompt": 2, "completion": 10, "request": 0},
        }

    def require_offline(self, activation, transport, api_key, base_url) -> None:
        if (
            activation is not RouteActivation.OFFLINE
            or type(transport) is not httpx.MockTransport
            or api_key != OFFLINE_KEY
            or base_url != ENDPOINT_BASE
        ):
            raise ModelRouteError(
                "Selected paid model route is disabled outside offline rehearsal"
            )

    def validate_output(self, output) -> None:
        if type(output) is not int or not 1 <= output <= self.max_output_tokens:
            raise ModelRouteError("Selected model output allowance is invalid")

    def validate_input(self, payload: dict) -> None:
        if any(type(row["content"]) is not str for row in payload["messages"]):
            raise ModelRouteError("Selected model input must be text-only")
        import tiktoken

        output = payload["max_tokens"]
        self.validate_output(output)
        # This retains the application's existing estimator. It is not an
        # attestation of the provider tokenizer. Count both messages and framing.
        encoding = tiktoken.get_encoding("cl100k_base")
        count = (
            sum(len(encoding.encode(row["content"])) for row in payload["messages"])
            + 256
        )
        if count > self.max_input_tokens or count + output > self.context_tokens:
            raise ModelRouteError(
                "Selected model input exceeds the complete-message budget"
            )


KIMI_ROUTE = ModelRoutePolicy(
    model_id="moonshotai/kimi-k3.1-pro",
    endpoint="moonshotai/mxfp4",
    context_tokens=1048576,
    max_output_tokens=32000,
    max_input_tokens=200000,
)


def selected_route(
    model_id: str, provider_id: str = "openrouter"
) -> ModelRoutePolicy | None:
    """Recognize family ownership for refusal; only exact canonical IDs opt in.

    Normalization never turns a malformed/native/aliased request into an
    accepted route. It prevents those forms from escaping into legacy clients.
    """

    def normalized(value):
        return "/".join(part.strip().casefold() for part in value.split("/"))

    # Family names identify ownership even when a caller supplies a native or
    # wrong provider. Only the raw canonical pair below can receive the policy.
    family_names = (KIMI_ROUTE.model_id.split("/", 1)[1],)
    parts = normalized(provider_id).split("/") + normalized(model_id).split("/")
    family = any(part.startswith(name) for part in parts for name in family_names)
    if not family:
        return None
    if provider_id != "openrouter" or model_id != KIMI_ROUTE.model_id:
        raise ModelRouteError(
            "Selected model requires its exact canonical OpenRouter identity; other forms are disabled"
        )
    return KIMI_ROUTE


def validate_completion(payload: dict, model_id: str, max_tokens: int) -> dict | None:
    """Accept complete visible output; account for reasoning inside completion."""
    choices = payload.get("choices")
    if (
        "error" in payload
        or payload.get("model") != model_id
        or payload.get("service_tier") not in (None, "default")
        or type(choices) is not list
        or len(choices) != 1
    ):
        raise ModelRouteError("Selected model completion identity or tier is invalid")
    choice = choices[0]
    message = choice.get("message") if type(choice) is dict else None
    if (
        type(choice) is not dict
        or choice.get("finish_reason") != "stop"
        or "error" in choice
        or type(message) is not dict
        or message.get("refusal")
        or "error" in message
        or not isinstance(message.get("content"), str)
        or not message["content"].strip()
    ):
        raise ModelRouteError(
            "Selected model did not return one complete visible answer"
        )
    raw = payload.get("usage")
    if raw is None:
        return None  # Missing accounting is unknown, never zero cost.
    if type(raw) is not dict:
        raise ModelRouteError("Selected model usage is invalid")
    result = {}
    for name in ("prompt_tokens", "completion_tokens", "total_tokens", "cost"):
        if name not in raw:
            continue
        value = raw[name]
        allowed = (int, float) if name == "cost" else (int,)
        if (
            type(value) not in allowed
            or not 0 <= value <= 2**53
            or not math.isfinite(value)
        ):
            raise ModelRouteError("Selected model usage is invalid")
        result[name] = value
    details = raw.get("completion_tokens_details")
    if details is not None:
        if type(details) is not dict:
            raise ModelRouteError("Selected model usage is invalid")
        if "reasoning_tokens" in details:
            value = details["reasoning_tokens"]
            if type(value) is not int or not 0 <= value <= result.get(
                "completion_tokens", -1
            ):
                raise ModelRouteError("Selected model reasoning accounting is invalid")
            result["reasoning_tokens"] = value
    if result.get("completion_tokens", 0) > max_tokens:
        raise ModelRouteError("Selected model combined output exceeded its allowance")
    return result

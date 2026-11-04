"""Select the model client used for report generation.

Prefer a direct OpenRouter client when an API key is configured, so the
pipeline can run without a locally hosted OpenCode gateway (for example in CI).
Otherwise fall back to OpenCode for local development. Both clients expose the
same ``generate`` contract.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Protocol

import httpx

from .opencode_client import ModelSelection, OpenCodeClient
from .openrouter_client import OPENROUTER_API_KEY_ENV_VAR, OpenRouterClient
from .attempt_budget import AdmissionAttemptBudget, AttemptBudgetError
from .failure_receipt import ENV_PATH, record_request
from .model_route import ENDPOINT_BASE, OFFLINE_KEY, RouteActivation, selected_route


class ReportModelClient(Protocol):
    async def generate(
        self,
        *,
        system_prompt: str,
        user_prompt: str,
        model: ModelSelection | None = None,
        title: str = "Report generation",
    ) -> str: ...


def build_model_client(
    *,
    timeout: float,
    max_tokens: int,
    model: ModelSelection | None = None,
    activation: RouteActivation = RouteActivation.DISABLED,
    transport: httpx.AsyncBaseTransport | None = None,
) -> OpenCodeClient | OpenRouterClient:
    """Return the model client selected by the environment.

    Uses OpenRouter directly when ``OPENROUTER_API_KEY`` is set; otherwise uses
    a local OpenCode server.
    """
    route = (
        selected_route(model.model_id)
        if model and model.provider_id.casefold() == "openrouter"
        else None
    )
    if route is not None:
        # The selected paid profile has no live activation path. This check
        # precedes any environment credential lookup or gateway selection.
        route.validate_output(max_tokens)
        route.require_offline(activation, transport, OFFLINE_KEY, ENDPOINT_BASE)
        return OpenRouterClient(
            api_key=OFFLINE_KEY,
            max_tokens=max_tokens,
            timeout=timeout,
            activation=activation,
            transport=transport,
        )
    api_key = os.getenv(OPENROUTER_API_KEY_ENV_VAR, "").strip()
    durable = os.getenv("SENTRYINSIGHT_ATTEMPT_STORE")
    if durable and (durable != "admission" or not api_key or not os.getenv(ENV_PATH)):
        raise AttemptBudgetError()
    if api_key:
        budget = AdmissionAttemptBudget.from_environment() if durable else None
        receipt_path = Path(os.environ[ENV_PATH]) if durable else None
        return OpenRouterClient(
            api_key=api_key,
            max_tokens=max_tokens,
            timeout=timeout,
            attempt_budget=budget,
            on_request=(
                (lambda value: record_request(receipt_path, value))
                if receipt_path is not None
                else None
            ),
        )
    return OpenCodeClient(timeout=timeout)

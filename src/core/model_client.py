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

from .opencode_client import ModelSelection, OpenCodeClient
from .openrouter_client import OPENROUTER_API_KEY_ENV_VAR, OpenRouterClient
from .attempt_budget import AdmissionAttemptBudget, AttemptBudgetError
from .failure_receipt import ENV_PATH, record_request
from .paid_verification import active_verification
from .repair_budget import RepairBudget, RepairBudgetError, RepairSlotAttemptBudget


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
    recovery_max_tokens: int | None = None,
    reasoning_max_tokens: int | None = None,
    total_timeout: float | None = None,
    output_limit_recovery: bool | None = None,
) -> OpenCodeClient | OpenRouterClient:
    """Return the model client selected by the environment.

    Uses OpenRouter directly when ``OPENROUTER_API_KEY`` is set; otherwise uses
    a local OpenCode server.
    """
    verification = active_verification()
    api_key = os.getenv(OPENROUTER_API_KEY_ENV_VAR, "").strip()
    durable = os.getenv("SENTRYINSIGHT_ATTEMPT_STORE")
    if durable and (durable != "admission" or not api_key or not os.getenv(ENV_PATH)):
        raise AttemptBudgetError()
    if api_key:
        budget = (
            verification.bridge
            if verification
            else AdmissionAttemptBudget.from_environment() if durable else None
        )
        receipt_path = Path(os.environ[ENV_PATH]) if durable else None
        return OpenRouterClient(
            api_key=api_key,
            max_tokens=max_tokens,
            recovery_max_tokens=recovery_max_tokens,
            reasoning_max_tokens=reasoning_max_tokens,
            timeout=timeout,
            total_timeout=total_timeout,
            output_limit_recovery=output_limit_recovery,
            attempt_budget=budget,
            on_request=(
                (lambda value: record_request(receipt_path, value))
                if receipt_path is not None
                else None
            ),
        )
    return OpenCodeClient(timeout=timeout)


def build_repair_client(
    *,
    repair_budget: RepairBudget,
    timeout: float,
    max_tokens: int,
    reasoning_max_tokens: int | None = None,
) -> OpenRouterClient:
    """Return a single-send OpenRouter client bound to one separate repair slot.

    Repair needs the production client: without an API key, or during paid
    verification, no repair request is built.
    """
    if active_verification() is not None:
        raise RepairBudgetError(
            "Repair requests are forbidden during paid verification"
        )
    api_key = os.getenv(OPENROUTER_API_KEY_ENV_VAR, "").strip()
    durable = os.getenv("SENTRYINSIGHT_ATTEMPT_STORE")
    if not api_key or (durable and (durable != "admission" or not os.getenv(ENV_PATH))):
        raise RepairBudgetError("Repair requires the production client and store")
    return OpenRouterClient(
        api_key=api_key,
        max_tokens=max_tokens,
        reasoning_max_tokens=reasoning_max_tokens,
        timeout=timeout,
        total_timeout=timeout,
        output_limit_recovery=False,
        max_attempts=1,
        attempt_budget=RepairSlotAttemptBudget(repair_budget),
    )

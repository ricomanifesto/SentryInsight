"""Direct OpenRouter client with one admission-backed budget for every send."""

from __future__ import annotations

import asyncio
import hashlib
import json
import logging
import math
import re
import time
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from typing import Any, Callable

import httpx

from .attempt_budget import AttemptBudget, MemoryAttemptBudget
from .opencode_client import ModelSelection
from .retry_policy import MAX_ATTEMPTS, MAX_RETRY_DELAY, retry_decision
from .paid_verification import active_verification

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
OPENROUTER_API_KEY_ENV_VAR = "OPENROUTER_API_KEY"
RETRYABLE_CODES = {408, 429, 500, 502, 503, 504}
_PERMANENT_CODES = {400, 401, 402, 403, 404, 413, 422}
USAGE_KEYS = (
    "prompt_tokens",
    "cached_tokens",
    "completion_tokens",
    "reasoning_tokens",
    "total_tokens",
    "cost",
)
MIN_RECOVERY_TIMEOUT_SECONDS = 120.0
FREE_ROUTE_MAX_COMPLETION_TOKENS = 131072
logger = logging.getLogger(__name__)


def validate_reasoning_max_tokens(
    reasoning_max_tokens: int | None, max_tokens: int
) -> int | None:
    """Validate an optional reasoning token ceiling against ``max_tokens``."""
    if reasoning_max_tokens is None:
        return None
    if (
        type(reasoning_max_tokens) is not int
        or type(max_tokens) is not int
        or not 0 < reasoning_max_tokens < max_tokens
    ):
        raise ValueError(
            "reasoning_max_tokens must be an integer between 1 and max_tokens - 1"
        )
    return reasoning_max_tokens


class OpenRouterError(RuntimeError):
    """Fixed diagnostic message plus bounded provider and attempt metadata."""

    def __init__(
        self,
        message: str,
        *,
        retryable: bool = False,
        http_status: int | None = None,
        provider_code: int | None = None,
        request_state: str = "uncertain",
    ) -> None:
        super().__init__(message)
        self.retryable = retryable
        self.http_status = http_status
        self.provider_code = provider_code
        self.request_state = request_state
        self.attempts: int | None = None


class OpenRouterUnavailable(OpenRouterError):
    """Transport could not deliver a usable response."""


class OpenRouterModelMismatch(OpenRouterError):
    """Resolved model differs from the requested model."""


class OpenRouterOutputLimitExceeded(OpenRouterError):
    """Provider returned partial output after reaching the output limit."""


class OpenRouterClient:
    def __init__(
        self,
        *,
        api_key: str,
        max_tokens: int = 4000,
        recovery_max_tokens: int | None = None,
        reasoning_max_tokens: int | None = None,
        base_url: str = OPENROUTER_BASE_URL,
        timeout: float = 120.0,
        total_timeout: float | None = None,
        output_limit_recovery: bool | None = None,
        transport: httpx.AsyncBaseTransport | None = None,
        max_attempts: int = MAX_ATTEMPTS,
        attempt_budget: AttemptBudget | None = None,
        on_request: Callable[[dict], None] | None = None,
    ) -> None:
        if type(max_attempts) is not int or not 1 <= max_attempts <= MAX_ATTEMPTS:
            raise ValueError("max_attempts must be between 1 and 3")
        if recovery_max_tokens is not None and (
            type(recovery_max_tokens) is not int
            or type(max_tokens) is not int
            or recovery_max_tokens < max_tokens
        ):
            raise ValueError(
                "recovery_max_tokens must be an integer greater than or equal to max_tokens"
            )
        validated_reasoning = validate_reasoning_max_tokens(
            reasoning_max_tokens, max_tokens
        )
        if total_timeout is not None and (
            type(total_timeout) not in (int, float)
            or not math.isfinite(total_timeout)
            or total_timeout <= 0
        ):
            raise ValueError("total_timeout must be a positive finite number")
        if (
            output_limit_recovery is not None
            and type(output_limit_recovery) is not bool
        ):
            raise ValueError("output_limit_recovery must be a boolean")
        self.api_key = api_key
        self.max_tokens = max_tokens
        self.recovery_max_tokens = recovery_max_tokens
        self.reasoning_max_tokens = validated_reasoning
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.total_timeout = float(total_timeout) if total_timeout is not None else None
        self.output_limit_recovery = (
            recovery_max_tokens is not None
            if output_limit_recovery is None
            else output_limit_recovery
        )
        self.transport = transport
        self.max_attempts = max_attempts
        self.verification = active_verification()
        if self.verification:
            self.verification.assert_key(api_key)
        self.attempt_budget = (
            self.verification.bridge
            if self.verification
            else attempt_budget or MemoryAttemptBudget()
        )
        self.on_request = on_request
        self.last_generation: dict[str, str] | None = None
        self.last_request: dict = {}
        self._last_attempt_max_tokens: int = max_tokens
        self._last_attempt_timeout: float | None = None

    def _payload(
        self,
        system_prompt: str,
        user_prompt: str,
        model_id: str,
        *,
        max_tokens: int | None = None,
        reasoning: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "model": model_id,
            "max_tokens": self.max_tokens if max_tokens is None else max_tokens,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        }
        if reasoning is not None:
            payload["reasoning"] = dict(reasoning)
        if model_id.endswith(":free") or model_id == "openrouter/free":
            payload["provider"] = {
                "allow_fallbacks": False,
                "max_price": {"prompt": 0, "completion": 0, "request": 0, "image": 0},
            }
        if self.verification:
            payload["provider"] = self.verification.provider_policy("report")
        return payload

    def _recovery_budget(self, current_max_tokens: int, model_id: str) -> int:
        """Return the output token budget for the one recovery attempt (never lower)."""
        if self.verification:
            return current_max_tokens
        if self.recovery_max_tokens is not None:
            return max(current_max_tokens, self.recovery_max_tokens)
        if model_id.endswith(":free") or model_id == "openrouter/free":
            return max(current_max_tokens, FREE_ROUTE_MAX_COMPLETION_TOKENS)
        return current_max_tokens

    def _log_output_limit_advisory(self, advisory: dict[str, Any]) -> None:
        """Log bounded recovery metadata without prompt or response text."""
        try:
            logger.warning(
                "OpenRouter output-limit recovery advisory: %s",
                json.dumps(advisory, sort_keys=True),
            )
        except Exception:  # noqa: BLE001 - logging must not alter delivery
            pass

    def _snapshot(self):
        if self.on_request is not None:
            self.on_request(self.last_request)

    async def _complete_attempt(self, reservation, disposition, delay):
        self.last_request["state"] = disposition
        # A failed snapshot leaves the ledger reservation unresolved. Sending
        # another request cannot be justified by a missing local receipt.
        self._snapshot()
        try:
            await self.attempt_budget.finish(
                reservation,
                disposition,
                retry_after=(
                    delay if disposition in {"not_sent", "retryable_rejection"} else 0
                ),
            )
        except BaseException:
            self.last_request["state"] = "uncertain"
            self._snapshot()
            raise

    async def generate(
        self,
        *,
        system_prompt: str,
        user_prompt: str,
        model: ModelSelection | None = None,
        title: str = "Report generation",
    ) -> str:
        if model is None or model.provider_id != "openrouter":
            raise OpenRouterError("OpenRouter calls require an openrouter/* model")
        self.last_generation = None
        current_max_tokens = self.max_tokens
        current_reasoning: dict[str, Any] | None = (
            {"max_tokens": self.reasoning_max_tokens}
            if self.reasoning_max_tokens is not None
            else None
        )
        payload = self._payload(
            system_prompt,
            user_prompt,
            model.model_id,
            max_tokens=current_max_tokens,
            reasoning=current_reasoning,
        )
        request_sha256 = hashlib.sha256(
            json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest()
        output_limit_recovered = False
        deadline = (
            time.monotonic() + self.total_timeout
            if self.total_timeout is not None
            else None
        )
        async with httpx.AsyncClient(
            base_url=self.base_url,
            timeout=self.timeout,
            transport=self.transport,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
                "X-Title": title,
            },
        ) as client:
            while True:
                if self.verification:
                    current_reasoning_cap = (
                        current_reasoning.get("max_tokens")
                        if isinstance(current_reasoning, dict)
                        else None
                    )
                    await self.verification.assert_report(
                        model.model_id,
                        current_max_tokens,
                        reasoning_max_tokens=current_reasoning_cap,
                    )
                reservation = await self.attempt_budget.reserve(
                    request_sha256, self.max_attempts
                )
                attempt = reservation["attempt"]
                self.last_request = {
                    "state": "reserved",
                    "attempts": attempt,
                    "limit": self.max_attempts,
                    "request_sha256": request_sha256,
                    "http_status": None,
                    "provider_code": None,
                    "usage": None,
                    "elapsed_seconds": None,
                }
                # This must succeed before entering the network operation.
                self._snapshot()
                response = None
                error = None
                disposition = "uncertain"
                delay = 0.0
                text = ""
                recover_now = False
                attempt_timeout = (
                    min(self.timeout, max(0.0, deadline - time.monotonic()))
                    if deadline is not None
                    else self.timeout
                )
                self._last_attempt_max_tokens = current_max_tokens
                self._last_attempt_timeout = round(attempt_timeout, 1)
                try:
                    if self.verification:
                        self.verification.check_deadline()
                    started = time.monotonic()
                    try:
                        response = await client.post(
                            "/chat/completions", json=payload, timeout=attempt_timeout
                        )
                    except httpx.TransportError as exc:
                        unsent = isinstance(
                            exc,
                            (
                                httpx.ConnectError,
                                httpx.ConnectTimeout,
                                httpx.PoolTimeout,
                            ),
                        )
                        raise OpenRouterUnavailable(
                            "OpenRouter API unavailable",
                            retryable=unsent,
                            request_state="not_sent" if unsent else "uncertain",
                        ) from None
                    self.last_request.update(
                        http_status=response.status_code,
                        usage=self._usage(response),
                        elapsed_seconds=round(time.monotonic() - started, 3),
                    )
                    self._log_usage()
                    text = self._response_text(response)
                    resolved = response.json().get("model")
                    if (
                        not isinstance(resolved, str)
                        or len(resolved) > 256
                        or re.fullmatch(r"[A-Za-z0-9._-]+/[A-Za-z0-9._:+-]+", resolved)
                        is None
                        or resolved != model.model_id
                    ):
                        raise OpenRouterModelMismatch(
                            "OpenRouter resolved model does not match the requested model",
                            http_status=response.status_code,
                            request_state="permanent_rejection",
                        )
                    self.last_generation = {
                        "requested_model": model.model_id,
                        "resolved_model": resolved,
                    }
                    disposition = "response_received"
                except OpenRouterOutputLimitExceeded as failure:
                    error = failure
                    self.last_request["provider_code"] = failure.provider_code
                    remaining = (
                        deadline - time.monotonic() if deadline is not None else None
                    )
                    min_recovery = min(MIN_RECOVERY_TIMEOUT_SECONDS, self.timeout)
                    can_recover = (
                        self.output_limit_recovery
                        and not output_limit_recovered
                        and attempt < self.max_attempts
                    )
                    has_time = remaining is None or remaining >= min_recovery
                    if can_recover and has_time:
                        next_max_tokens = self._recovery_budget(
                            current_max_tokens, model.model_id
                        )
                        next_attempt_timeout = (
                            min(self.timeout, remaining)
                            if remaining is not None
                            else self.timeout
                        )
                        self._log_output_limit_advisory(
                            {
                                "event": "output_limit_recovery",
                                "attempt": attempt,
                                "next_attempt": attempt + 1,
                                "max_attempts": self.max_attempts,
                                "previous_max_tokens": current_max_tokens,
                                "recovery_max_tokens": next_max_tokens,
                                "reasoning_capped": current_reasoning is not None,
                                "attempt_timeout_seconds": round(attempt_timeout, 1),
                                "next_attempt_timeout_seconds": round(
                                    next_attempt_timeout, 1
                                ),
                                "usage": self.last_request.get("usage"),
                                "elapsed_seconds": self.last_request.get(
                                    "elapsed_seconds"
                                ),
                                "remaining_timeout_seconds": (
                                    round(remaining, 1)
                                    if remaining is not None
                                    else None
                                ),
                            }
                        )
                        output_limit_recovered = True
                        current_max_tokens = next_max_tokens
                        payload = self._payload(
                            system_prompt,
                            user_prompt,
                            model.model_id,
                            max_tokens=current_max_tokens,
                            reasoning=current_reasoning,
                        )
                        disposition = "retryable_rejection"
                        delay = 0.0
                        recover_now = True
                    else:
                        if can_recover and not has_time:
                            self._log_output_limit_advisory(
                                {
                                    "event": "output_limit_recovery_skipped",
                                    "reason": "timeout_budget_exhausted",
                                    "attempt": attempt,
                                    "max_attempts": self.max_attempts,
                                    "previous_max_tokens": current_max_tokens,
                                    "attempt_timeout_seconds": round(
                                        attempt_timeout, 1
                                    ),
                                    "usage": self.last_request.get("usage"),
                                    "elapsed_seconds": self.last_request.get(
                                        "elapsed_seconds"
                                    ),
                                    "remaining_timeout_seconds": (
                                        round(max(0.0, remaining), 1)
                                        if remaining is not None
                                        else None
                                    ),
                                }
                            )
                        disposition = failure.request_state
                        delay = 0.0
                except OpenRouterError as failure:
                    error = failure
                    disposition = failure.request_state
                    self.last_request["provider_code"] = failure.provider_code
                    delay = self._retry_delay(response, attempt)
                    if disposition in {"not_sent", "retryable_rejection"} and (
                        not math.isfinite(delay) or delay > MAX_RETRY_DELAY
                    ):
                        disposition = "deferred_rejection"
                    if (
                        deadline is not None
                        and disposition in {"not_sent", "retryable_rejection"}
                        and deadline - time.monotonic() - delay
                        < min(30.0, self.timeout)
                    ):
                        disposition = "deferred_rejection"
                finally:
                    # Unexpected exceptions and cancellation retain uncertainty.
                    # A lost completion acknowledgement never permits a send.
                    await self._complete_attempt(reservation, disposition, delay)
                if error is None:
                    return text
                error.attempts = attempt
                if recover_now:
                    continue
                advice = retry_decision(
                    disposition, attempts=attempt, limit=self.max_attempts, delay=delay
                )
                if not error.retryable or advice["action"] != "retry_after":
                    logger.error(
                        "OpenRouter attempt %d/%d failed: %s; stopping",
                        attempt,
                        self.max_attempts,
                        error,
                    )
                    raise error
                logger.warning(
                    "OpenRouter attempt %d/%d failed: %s; retrying in %.1fs",
                    attempt,
                    self.max_attempts,
                    error,
                    delay,
                )
                await asyncio.sleep(delay)

    def _log_usage(self) -> None:
        """One bounded line per response: token counts, latency and cap headroom.

        Generation time is dominated by output decoding, so the log records
        what bounds it: output and reasoning tokens, the observed output rate
        and how close the response came to ``max_tokens``. No text is logged.
        Diagnostics never change the request outcome, so a failure here is
        swallowed.
        """
        try:
            self._write_usage_log()
        except Exception:  # noqa: BLE001 - logging must not alter delivery
            pass

    def _write_usage_log(self) -> None:
        usage = self.last_request.get("usage") or {}
        elapsed = self.last_request.get("elapsed_seconds")
        completion = usage.get("completion_tokens")
        attempt_max_tokens = self._last_attempt_max_tokens
        summary = {
            "http_status": self.last_request.get("http_status"),
            "attempt": self.last_request.get("attempts"),
            "max_tokens": attempt_max_tokens,
            "timeout_seconds": self._last_attempt_timeout,
            "elapsed_seconds": elapsed,
            **{key: usage.get(key) for key in USAGE_KEYS},
            "output_tokens_per_second": (
                round(completion / elapsed, 1)
                if type(completion) is int and elapsed
                else None
            ),
            "max_tokens_used_fraction": (
                round(completion / attempt_max_tokens, 3)
                if type(completion) is int and attempt_max_tokens
                else None
            ),
        }
        logger.info("OpenRouter usage: %s", json.dumps(summary, sort_keys=True))

    @staticmethod
    def _usage(response: httpx.Response) -> dict | None:
        try:
            payload = response.json()
        except ValueError:
            return None
        if not isinstance(payload, dict) or type(payload.get("usage")) is not dict:
            return None
        raw = payload["usage"]
        # Reasoning and cached-prompt counts arrive nested; keep them flat.
        nested = {
            "reasoning_tokens": ("completion_tokens_details", "reasoning_tokens"),
            "cached_tokens": ("prompt_tokens_details", "cached_tokens"),
        }
        flat: dict[str, Any] = dict(raw)
        for key, (parent, child) in nested.items():
            details = raw.get(parent)
            if type(details) is dict and child in details:
                flat[key] = details[child]
        return {
            key: value
            for key in USAGE_KEYS
            if isinstance(value := flat.get(key), (int, float))
            and not isinstance(value, bool)
            and 0 <= value <= 2**63
            and math.isfinite(value)
        }

    @staticmethod
    def _retry_delay(response: httpx.Response | None, attempt: int) -> float:
        """Honor Retry-After; the caller stops if the wait exceeds our budget."""
        backoff = float(2 ** (attempt - 1))
        value = response.headers.get("Retry-After") if response is not None else None
        if not value:
            return backoff
        try:
            delay = float(value)
        except ValueError:
            try:
                retry_at = parsedate_to_datetime(value)
                delay = (retry_at - datetime.now(timezone.utc)).total_seconds()
            except (ValueError, TypeError, OverflowError):
                return backoff
        if math.isnan(delay) or delay < 0:
            return backoff
        return max(backoff, delay)

    def _response_text(self, response: httpx.Response) -> str:
        try:
            payload = response.json()
        except ValueError:
            payload = None
        has_error = isinstance(payload, dict) and "error" in payload
        if not response.is_success or has_error:
            code = None
            raw_error = payload.get("error") if isinstance(payload, dict) else None
            if isinstance(raw_error, dict):
                candidate = raw_error.get("code")
                if type(candidate) is str and re.fullmatch(r"[0-9]{3}", candidate):
                    candidate = int(candidate)
                if type(candidate) is int and 100 <= candidate <= 599:
                    code = candidate
            transient_status = (
                response.is_success or response.status_code in RETRYABLE_CODES
            )
            explicit_transient = (
                has_error
                and transient_status
                and code in RETRYABLE_CODES
                and "choices" not in payload
                and "usage" not in payload
            )
            state = "uncertain"
            if explicit_transient:
                state = "retryable_rejection"
            elif response.status_code in _PERMANENT_CODES or code in _PERMANENT_CODES:
                state = "permanent_rejection"
            message = f"OpenRouter chat completion failed: HTTP {response.status_code}"
            if has_error:
                message += f"; provider_code={code or 'unknown'}"
            raise OpenRouterError(
                message,
                retryable=explicit_transient,
                request_state=state,
                http_status=response.status_code,
                provider_code=code,
            )
        if not isinstance(payload, dict):
            raise OpenRouterError(
                f"OpenRouter response was not a JSON object (HTTP {response.status_code})",
                http_status=response.status_code,
            )
        try:
            return self._extract_text(payload)
        except OpenRouterOutputLimitExceeded as exc:
            raise OpenRouterOutputLimitExceeded(
                f"{exc} (HTTP {response.status_code})",
                http_status=response.status_code,
                request_state="permanent_rejection",
            ) from None
        except OpenRouterError as exc:
            raise OpenRouterError(
                f"{exc} (HTTP {response.status_code})",
                http_status=response.status_code,
                request_state=exc.request_state,
            ) from None

    def _extract_text(self, payload: dict[str, Any]) -> str:
        choices = payload.get("choices")
        if not isinstance(choices, list) or not choices:
            raise OpenRouterError(
                "OpenRouter response did not include choices", retryable=True
            )

        # HTTP 200 only confirms transport success. Reject partial output before
        # reading it, even when another choice contains a complete response.
        if any(
            isinstance(choice, dict) and choice.get("finish_reason") == "length"
            for choice in choices
        ):
            raise OpenRouterOutputLimitExceeded(
                "OpenRouter response reached the output token limit"
            )

        text_parts: list[str] = []
        for choice in choices:
            if not isinstance(choice, dict):
                continue
            message = choice.get("message")
            if isinstance(message, dict):
                content = message.get("content")
                if isinstance(content, str) and content.strip():
                    text_parts.append(content)

        if text_parts:
            return "\n".join(text_parts)

        raise OpenRouterError("OpenRouter response did not include text output")

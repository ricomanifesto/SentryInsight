"""Default-off, single-use paid verification; fail before sending on uncertainty."""

from __future__ import annotations

import asyncio
from datetime import datetime
from decimal import Decimal, InvalidOperation
import hashlib
import json
import logging
import math
import os
from pathlib import Path
import re
import time
from types import MappingProxyType
from typing import Any

import httpx

from .attempt_budget import AdmissionAttemptBudget, AttemptBudgetError

PROFILE_ID = "kimi-moonshot-verification-20261117"
FLAG = "SENTRYINSIGHT_PAID_VERIFICATION"
EVIDENCE = "SENTRYINSIGHT_BILLING_EVIDENCE"
_HEX = re.compile(r"[a-f0-9]{64}")
_current: Verification | None = None
logger = logging.getLogger(__name__)


class PaidVerificationError(RuntimeError):
    def __init__(self):
        super().__init__(
            "Paid verification unavailable or unresolved; no further request authorized"
        )


def _require(condition: bool) -> None:
    if not condition:
        raise PaidVerificationError()


def _now_ms() -> float:
    return time.time() * 1000


def _amount(value: Any) -> Decimal:
    _require(type(value) in (int, float, str))
    try:
        number = Decimal(str(value))
    except InvalidOperation:
        raise PaidVerificationError() from None
    _require(number.is_finite() and number >= 0)
    return number


def _scope() -> tuple[str, ...]:
    return tuple(
        os.environ.get(key, "")
        for key in (
            "SENTRYINSIGHT_ADMISSION_KEY",
            "GITHUB_RUN_ID",
            "SENTRYINSIGHT_SOURCE_REVISION",
            "GITHUB_RUN_ATTEMPT",
        )
    )


class Verification:
    def __init__(
        self,
        bridge: AdmissionAttemptBudget,
        profile: dict,
        profile_sha256: str,
        key_sha256: str,
    ):
        self.bridge = bridge
        self.profile = MappingProxyType(dict(profile))
        self.profile_sha256 = profile_sha256
        self.scope = _scope()
        self.key_sha256 = key_sha256
        self.valid_until = 0
        self.not_before = (
            datetime.fromisoformat(
                profile["periodStart"].replace("Z", "+00:00")
            ).timestamp()
            * 1000
        )
        self.period_end = (
            datetime.fromisoformat(
                profile["periodEnd"].replace("Z", "+00:00")
            ).timestamp()
            * 1000
        )

    def bind_deadline(self, deadline: int) -> None:
        _require(
            type(deadline) is int
            and deadline <= self.period_end
            and deadline <= _now_ms() + 3600000
        )
        self.valid_until = deadline
        self.check_deadline()

    def check_deadline(self) -> None:
        current = _now_ms()
        _require(
            math.isfinite(current) and self.not_before <= current < self.valid_until
        )

    async def _call(self, command: str, arguments: list[str]) -> dict:
        _require(self.scope == _scope())
        try:
            return await asyncio.to_thread(
                self.bridge._invoke, command, ["--run-attempt", "1", *arguments]
            )
        except AttemptBudgetError:
            raise PaidVerificationError() from None

    def assert_key(self, key: str) -> None:
        _require(hashlib.sha256(key.encode()).hexdigest() == self.key_sha256)

    def provider_policy(self, operation: str) -> dict:
        _require(operation in {"report", "triage"})
        report = operation == "report"
        provider = self.profile["provider" if report else "triageProvider"]
        return {
            "only": [provider],
            "order": [provider],
            "allow_fallbacks": False,
            "require_parameters": True,
            "max_price": {
                "prompt": self.profile[
                    "reportPromptPrice" if report else "triagePromptPrice"
                ],
                "completion": self.profile[
                    "reportCompletionPrice" if report else "triageCompletionPrice"
                ],
                "request": "0",
            },
        }

    async def assert_report(self, model: str, max_tokens: int) -> None:
        _require(
            model == self.profile["model"]
            and max_tokens == self.profile["reportOutput"]
        )
        result = await self._call("verification-report", [])
        _require(result == {"verified": True})

    async def claim_triage(self, slot: int, raw: bytes) -> None:
        result = await self._call(
            "verification-triage",
            ["--slot", str(slot), "--request-sha256", hashlib.sha256(raw).hexdigest()],
        )
        _require(result == {"claimed": True})


def active_verification() -> Verification | None:
    selected = os.environ.get(FLAG, "")
    if not selected:
        return None
    current = _current
    if current is None:
        raise PaidVerificationError()
    _require(selected == PROFILE_ID and current.scope == _scope())
    current.check_deadline()
    return current


async def _read(client: httpx.AsyncClient, path: str, *, key: str = "") -> dict:
    response = await client.get(
        "https://openrouter.ai/api/v1/" + path,
        headers={"Authorization": "Bearer " + key} if key else {},
    )
    _require(response.status_code == 200 and len(response.content) <= 524288)
    value = response.json()
    _require(type(value) is dict and type(value.get("data")) is dict)
    return value["data"]


async def _verify_metadata(profile: dict, evidence: dict, key: str, transport) -> None:
    _require(evidence.get("keySha256") == hashlib.sha256(key.encode()).hexdigest())
    async with httpx.AsyncClient(
        timeout=15, transport=transport, follow_redirects=False
    ) as client:
        metadata = await _read(client, "key", key=key)
        workspace = metadata.get("workspace_id")
        if not isinstance(workspace, str) or not workspace:
            raise PaidVerificationError()
        _require(
            evidence.get("scopeSha256")
            == hashlib.sha256(("workspace:" + workspace).encode()).hexdigest()
        )
        _require(_amount(metadata.get("byok_usage_monthly")) == 0)
        _require(
            _amount(metadata.get("usage_monthly")) * 1000000
            <= evidence.get("actualMicrousd", -1)
        )
        for report in (True, False):
            model = profile["model" if report else "triageModel"]
            data = await _read(client, f"models/{model}/endpoints")
            _require(data.get("id") == model and type(data.get("endpoints")) is list)
            tag = profile["provider" if report else "triageProvider"]
            endpoints = [
                row
                for row in data["endpoints"]
                if type(row) is dict and row.get("tag") == tag
            ]
            _require(len(endpoints) == 1)
            endpoint = endpoints[0]
            context = endpoint.get("context_length")
            _require(
                type(context) is int
                and 0
                < context
                <= profile["reportContext" if report else "triageContext"]
            )
            if report:
                _require(
                    type(endpoint.get("max_completion_tokens")) is int
                    and endpoint["max_completion_tokens"] >= profile["reportOutput"]
                )
            pricing = endpoint.get("pricing")
            _require(type(pricing) is dict)
            for field, ceiling in (
                ("prompt", "reportPromptPrice" if report else "triagePromptPrice"),
                (
                    "completion",
                    "reportCompletionPrice" if report else "triageCompletionPrice",
                ),
            ):
                _require(
                    _amount(pricing.get(field)) * 1000000 <= _amount(profile[ceiling])
                )
            _require(_amount(pricing.get("request", 0)) == 0)


async def initialize_verification(
    config: dict, *, bridge=None, transport=None
) -> Verification | None:
    """Reserve the complete run before triage; never change persistent defaults."""
    global _current
    _current = None
    if not os.environ.get(FLAG, ""):
        return None
    _require(
        os.environ[FLAG] == PROFILE_ID
        and os.environ.get("GITHUB_EVENT_NAME") == "workflow_dispatch"
        and os.environ.get("GITHUB_REF") == "refs/heads/main"
        and os.environ.get("GITHUB_RUN_ATTEMPT") == "1"
        and os.environ.get("SENTRYINSIGHT_ATTEMPT_STORE") == "admission"
        and bool(os.environ.get("OPENROUTER_API_KEY", "").strip())
        and bool(os.environ.get("SENTRYINSIGHT_FAILURE_RECEIPT"))
        and bool(os.environ.get(EVIDENCE))
    )
    analysis = config.get("analysis", {})
    _require(
        analysis.get("max_tokens") == 32000
        and analysis.get("max_input_tokens") == 200000
    )
    try:
        proof_path = Path(os.environ[EVIDENCE])
        _require(not proof_path.is_symlink() and proof_path.stat().st_size <= 4096)
        evidence = json.loads(proof_path.read_text())
        _require(type(evidence) is dict and type(evidence.get("actualMicrousd")) is int)
        selected_bridge = bridge or AdmissionAttemptBudget.from_environment()
        exported = await asyncio.to_thread(
            selected_bridge._invoke, "verification-profile", []
        )
        profile, digest = exported["profile"], exported["sha256"]
        _require(
            type(profile) is dict
            and type(digest) is str
            and _HEX.fullmatch(digest) is not None
        )
        canonical = (json.dumps(profile, sort_keys=True, indent=2) + "\n").encode()
        _require(
            hashlib.sha256(canonical).hexdigest() == digest
            and profile.get("id") == PROFILE_ID
            and profile.get("model") == "moonshotai/kimi-k3.1-pro"
            and profile.get("provider") == "moonshotai/mxfp4"
            and profile.get("reportAttempts") == 3
            and profile.get("reportOutput") == 32000
            and profile.get("triageRequests") == 64
            and profile.get("reserveMicrousd") == 7956100
            and profile.get("limitMicrousd") == 8000000
        )
        await _verify_metadata(
            profile,
            evidence,
            os.environ["OPENROUTER_API_KEY"],
            transport,
        )
        verification = Verification(
            selected_bridge, profile, digest, evidence["keySha256"]
        )
        evidence_digest = hashlib.sha256(
            (json.dumps(evidence, sort_keys=True, indent=2) + "\n").encode()
        ).hexdigest()
        reserved = await verification._call(
            "verification-reserve",
            [
                "--billing-evidence",
                str(proof_path),
                "--evidence-sha256",
                evidence_digest,
            ],
        )
        _require(
            set(reserved) == {"reservedMicrousd", "profileSha256", "validUntil"}
            and reserved["reservedMicrousd"] == profile["reserveMicrousd"]
            and reserved["profileSha256"] == digest
        )
        verification.bind_deadline(reserved["validUntil"])
    except (
        OSError,
        ValueError,
        KeyError,
        TypeError,
        httpx.HTTPError,
        AttemptBudgetError,
    ):
        raise PaidVerificationError() from None
    _current = verification
    os.environ["SENTRYINSIGHT_MODEL"] = "openrouter/" + profile["model"]
    logger.info(
        "Paid verification reserved: %s",
        json.dumps(
            {"profile_sha256": digest, "reserved_microusd": profile["reserveMicrousd"]},
            sort_keys=True,
        ),
    )
    return verification

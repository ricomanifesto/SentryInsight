"""Sequential, one-attempt trials with allowlisted receipts and opt-in review."""

import asyncio
import json
import re
import time
from pathlib import Path
from typing import Any, Awaitable, Callable

import httpx

from .fixtures import CASE_NAMES, PreparedCase, evaluate
from .private_review import EncryptedReview
from .policy import (
    API,
    MAX_REQUESTS,
    MODEL,
    PilotError,
    bounded_json,
    check_policy,
    completion,
    digest,
    validate_payload,
)


def _write_receipt(output: Path, receipt: dict) -> None:
    (output / "metadata" / "receipt.json").write_text(
        json.dumps(receipt, indent=2, allow_nan=False) + "\n"
    )


async def run_cases(
    cases: list[PreparedCase],
    *,
    secret: str,
    output: Path,
    candidate_sha: str,
    review_outputs: bool = False,
    review_recipient: EncryptedReview | None = None,
    transport: httpx.AsyncBaseTransport | None = None,
    sleep: Callable[[float], Awaitable[None]] = asyncio.sleep,
    clock: Callable[[], float] = time.monotonic,
) -> dict:
    if (
        not secret
        or tuple(c.name for c in cases) != CASE_NAMES
        or len(cases) != MAX_REQUESTS
    ):
        raise PilotError("invalid_run_plan")
    if not re.fullmatch(r"[0-9a-f]{40}", candidate_sha):
        raise PilotError("candidate_identity")
    if review_outputs != (review_recipient is not None):
        raise PilotError("review_configuration")
    if review_recipient is not None:
        await review_recipient.preflight()
    output.mkdir(mode=0o700, parents=True, exist_ok=False)
    (output / "metadata").mkdir(mode=0o700)
    trials: list[dict[str, Any]] = [
        {
            "case": c.name,
            "outcome": "not_attempted",
            "request_sha256": c.request_sha256,
            "input_tokens_with_framing_reserve": c.input_tokens_with_reserve,
        }
        for c in cases
    ]
    receipt: dict[str, Any] = {
        "schema": 1,
        "candidate_sha": candidate_sha,
        "requested_model": MODEL,
        "requested_provider": "Phala",
        "planned": MAX_REQUESTS,
        "attempted": 0,
        "automated_passes": 0,
        "complete": False,
        "human_review": "not_performed",
        "production_ready": False,
        "synthetic_review_outputs": review_outputs,
        "trials": trials,
    }
    _write_receipt(output, receipt)
    last_submission: float | None = None
    async with httpx.AsyncClient(
        timeout=httpx.Timeout(1600, connect=30),
        transport=transport,
        follow_redirects=False,
        trust_env=False,
    ) as client:
        for case, trial in zip(cases, trials, strict=True):
            started = clock()
            raw: str | None = None
            try:
                # Revalidate public policy directly before each submission. The
                # GETs carry no credential and never count as model attempts.
                if last_submission is not None:
                    await sleep(max(0, 60 - (clock() - last_submission)))
                validate_payload(case.payload)
                async with asyncio.timeout(60):
                    await check_policy(client)
                if receipt["attempted"] >= MAX_REQUESTS:
                    raise PilotError("request_limit")
                if digest(case.payload) != trial["request_sha256"]:
                    raise PilotError("request_identity")
                receipt["attempted"] += 1
                trial["outcome"] = "submitted"
                _write_receipt(output, receipt)
                last_submission = clock()
                async with asyncio.timeout(1600):
                    data = await bounded_json(
                        client,
                        "POST",
                        API,
                        headers={"Authorization": f"Bearer {secret}"},
                        json=case.payload,
                    )
                raw, safe_metadata = completion(data, secret)
                trial.update(safe_metadata)
                if review_recipient is not None:
                    trial["encrypted_review"] = await review_recipient.seal(
                        output, case.name, raw, candidate_sha, case.request_sha256
                    )
                _, checks = evaluate(case, raw)
                trial["checks"] = checks
                if not all(checks.values()):
                    raise PilotError("known_answer_mismatch")
                trial["outcome"] = "automated_pass"
                receipt["automated_passes"] += 1
            except PilotError as exc:
                # Only this module's fixed codes are emitted. Never stringify an
                # arbitrary transport/validator exception or its response body.
                trial["outcome"] = "failed"
                trial["code"] = str(exc)
                trial.update(exc.metadata)
            except Exception:
                trial["outcome"] = "failed"
                trial["code"] = "validation_or_internal_error"
            finally:
                trial["duration_seconds"] = round(max(0, clock() - started), 3)
                _write_receipt(output, receipt)
                # Raw output never enters logs, summaries or metadata artifacts.
                raw = None
            if trial["outcome"] != "automated_pass":
                break
    receipt["complete"] = receipt["automated_passes"] == MAX_REQUESTS
    _write_receipt(output, receipt)
    return receipt

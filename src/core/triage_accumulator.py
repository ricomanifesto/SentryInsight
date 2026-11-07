"""Fold triage receipts into a counts-only ledger and bound its rates offline.

The unit is the unique article URL hash (``url_sha256``) across runs, because
articles recur across dispatches and dates. Bounds use Hoeffding's inequality
for outcomes in [0, 1], so they assume nothing about the rate distribution.
Every function here is pure: no files, network or configuration are read.
"""

from __future__ import annotations

import copy
import hashlib
import math
from typing import Any, Iterable, Mapping

from . import exploitation_triage as triage

LEDGER_VERSION = 1
RECEIPT_SCHEMA_VERSION = 1
DECIDED_MODES = ("shadow", "enabled")
NO_PLAN_DELTA = 0.05
RATES = ("drop", "miss")
_COUNT_KEYS = (
    "runs_decided",
    "runs_legacy_full",
    "runs_shadow",
    "runs_enabled",
    "positions_decided",
    "positions_unhashed",
    "positions_legacy_full",
)


class TriageAccumulatorError(ValueError):
    """Raised for a receipt, ledger or plan this module refuses to use."""


def published_url_sha256(url: str) -> str | None:
    """Hash a published Reporting URL the way a receipt hashes its article.

    Reports write ``normalize_reporting_url(article["link"])`` while receipts
    hash the stripped raw link, so the two agree exactly when the feed link
    was already canonical. A non-canonical feed link has no published match.
    """
    return triage.url_sha256({"link": url})


def run_identity(receipt: Mapping[str, Any]) -> str:
    """Identify a run by the SHA-256 of its canonical receipt encoding."""
    return hashlib.sha256(triage.encode_receipt_unchecked(dict(receipt))).hexdigest()


def empty_ledger() -> dict[str, Any]:
    ledger: dict[str, Any] = {
        "ledger_version": LEDGER_VERSION,
        "receipt_schema_version": RECEIPT_SCHEMA_VERSION,
        "runs": [],
        "hashes": {},
    }
    ledger.update({key: 0 for key in _COUNT_KEYS})
    return _with_unique_counts(ledger)


def _check_receipt(receipt: Any) -> dict[str, Any]:
    if not isinstance(receipt, dict):
        raise TriageAccumulatorError("Triage receipt must be a JSON object")
    version = receipt.get("schema_version")
    if type(version) is not int or version != RECEIPT_SCHEMA_VERSION:
        raise TriageAccumulatorError(
            f"Unsupported triage receipt schema_version: {version!r}"
        )
    try:
        return triage.validate_receipt(receipt)
    except triage.TriageReceiptError as exc:
        raise TriageAccumulatorError("Triage receipt failed validation") from exc


def _is_would_drop(seen: Mapping[str, int]) -> bool:
    return seen.get(triage.ACCEPTED_IRRELEVANT, 0) > 0


def _with_unique_counts(ledger: dict[str, Any]) -> dict[str, Any]:
    entries = ledger["hashes"].values()
    ledger["unique_decided"] = len(ledger["hashes"])
    ledger["would_drop"] = sum(_is_would_drop(entry["seen"]) for entry in entries)
    ledger["conflicting"] = sum(len(entry["seen"]) > 1 for entry in entries)
    return ledger


def validate_ledger(ledger: Any) -> dict[str, Any]:
    """Accept only the counts-and-hashes ledger shape ``fold_receipts`` writes."""
    expected = {
        "ledger_version",
        "receipt_schema_version",
        "runs",
        "hashes",
        "unique_decided",
        "would_drop",
        "conflicting",
        *_COUNT_KEYS,
    }
    optional = {"plan", "frozen"}
    if not isinstance(ledger, dict) or set(ledger) - optional != expected:
        raise TriageAccumulatorError("Ledger has an unexpected shape")
    present = optional & set(ledger)
    if present and present != optional:
        raise TriageAccumulatorError("Ledger plan and frozen looks go together")
    if present:
        _check_frozen(ledger["frozen"], _check_plan(ledger["plan"]))
    if ledger["ledger_version"] != LEDGER_VERSION:
        raise TriageAccumulatorError("Unsupported ledger_version")
    if ledger["receipt_schema_version"] != RECEIPT_SCHEMA_VERSION:
        raise TriageAccumulatorError("Unsupported ledger receipt_schema_version")
    runs = ledger["runs"]
    if not isinstance(runs, list) or not all(triage._hex64(run) for run in runs):
        raise TriageAccumulatorError("Ledger runs must be SHA-256 identities")
    if len(set(runs)) != len(runs):
        raise TriageAccumulatorError("Ledger runs must be unique")
    for key in _COUNT_KEYS:
        if not triage._count(ledger[key]):
            raise TriageAccumulatorError(f"Ledger {key} must be a count")
    hashes = ledger["hashes"]
    if not isinstance(hashes, dict):
        raise TriageAccumulatorError("Ledger hashes must be an object")
    orders = []
    for key, entry in hashes.items():
        if not triage._hex64(key) or not isinstance(entry, dict):
            raise TriageAccumulatorError("Ledger hash entries are invalid")
        if set(entry) != {"first_seen", "seen"} or not triage._count(
            entry["first_seen"]
        ):
            raise TriageAccumulatorError("Ledger hash entries are invalid")
        seen = entry["seen"]
        if (
            not isinstance(seen, dict)
            or not seen
            or not all(
                name in triage.DISPOSITIONS
                and name != triage.LEGACY_FULL
                and triage._count(count)
                and count > 0
                for name, count in seen.items()
            )
        ):
            raise TriageAccumulatorError("Ledger dispositions are invalid")
        orders.append(entry["first_seen"])
    if sorted(orders) != list(range(len(orders))):
        raise TriageAccumulatorError("Ledger first_seen order is invalid")
    recomputed = _with_unique_counts(
        {"hashes": hashes, "unique_decided": 0, "would_drop": 0, "conflicting": 0}
    )
    for key in ("unique_decided", "would_drop", "conflicting"):
        if ledger[key] != recomputed[key]:
            raise TriageAccumulatorError(f"Ledger {key} does not match its hashes")
    return ledger


def fold_receipts(
    receipts: Iterable[Any], ledger: Mapping[str, Any] | None = None
) -> dict[str, Any]:
    """Fold receipts into a new ledger; a run already folded is skipped.

    Only ``decided`` runs contribute positions. A hash is would-drop when any
    run disposed it ``accepted_irrelevant``; a hash seen with more than one
    disposition across runs is also counted as conflicting.
    """
    result = (
        empty_ledger() if ledger is None else copy.deepcopy(validate_ledger(ledger))
    )
    runs = set(result["runs"])
    hashes: dict[str, dict[str, Any]] = result["hashes"]
    for receipt in receipts:
        value = _check_receipt(receipt)
        identity = run_identity(value)
        if identity in runs:
            continue
        runs.add(identity)
        result["runs"].append(identity)
        records = value["records"]
        if value["status"] != "decided":
            result["runs_legacy_full"] += 1
            result["positions_legacy_full"] += len(records)
            continue
        if value["mode"] not in DECIDED_MODES:
            raise TriageAccumulatorError("Decided receipt has an unknown mode")
        result["runs_decided"] += 1
        result[f"runs_{value['mode']}"] += 1
        for record in records:
            result["positions_decided"] += 1
            digest = record["url_sha256"]
            if digest is None:
                result["positions_unhashed"] += 1
                continue
            entry = hashes.setdefault(digest, {"first_seen": len(hashes), "seen": {}})
            disposition = record["disposition"]
            entry["seen"][disposition] = entry["seen"].get(disposition, 0) + 1
    result["runs"].sort()
    return _with_unique_counts(result)


def join_must_keep(
    ledger: Mapping[str, Any], published_hashes: Iterable[str]
) -> dict[str, Any]:
    """Add cited counts: decided hashes that a published report links to."""
    result = copy.deepcopy(validate_ledger(ledger))
    published = set()
    for digest in published_hashes:
        if not triage._hex64(digest):
            raise TriageAccumulatorError("Published hashes must be SHA-256 hex")
        published.add(digest)
    hashes = result["hashes"]
    cited = sorted(
        (digest for digest in published if digest in hashes),
        key=lambda digest: hashes[digest]["first_seen"],
    )
    result["published"] = len(published)
    result["published_unmatched"] = len(published) - len(cited)
    result["cited"] = len(cited)
    result["cited_and_dropped"] = sum(
        _is_would_drop(hashes[digest]["seen"]) for digest in cited
    )
    result["cited_hashes"] = cited
    return result


def one_sided_half_width(n: int, delta: float) -> float:
    """Hoeffding: P(mean - p >= t) <= exp(-2 n t^2) for outcomes in [0, 1]."""
    return math.sqrt(math.log(1 / delta) / (2 * n))


def two_sided_half_width(n: int, delta: float) -> float:
    return math.sqrt(math.log(2 / delta) / (2 * n))


def _check_plan(plan: Any) -> dict[str, Any]:
    if not isinstance(plan, Mapping) or set(plan) != {
        "epsilon_drop",
        "epsilon_miss",
        "delta",
        "checkpoints",
    }:
        raise TriageAccumulatorError(
            "Plan must define exactly epsilon_drop, epsilon_miss, delta and"
            " checkpoints"
        )
    for key in ("epsilon_drop", "epsilon_miss", "delta"):
        value = plan[key]
        if (
            isinstance(value, bool)
            or not isinstance(value, (int, float))
            or not 0 < value < 1
        ):
            raise TriageAccumulatorError(f"Plan {key} must be between 0 and 1")
    checkpoints = plan["checkpoints"]
    if (
        not isinstance(checkpoints, list)
        or not checkpoints
        or not all(type(c) is int and c > 0 for c in checkpoints)
        or checkpoints != sorted(set(checkpoints))
    ):
        raise TriageAccumulatorError(
            "Plan checkpoints must be strictly increasing positive integers"
        )
    return dict(plan)


def _ordered_outcomes(ledger: Mapping[str, Any]) -> dict[str, list[bool]]:
    hashes = ledger["hashes"]
    decided = sorted(hashes, key=lambda digest: hashes[digest]["first_seen"])
    return {
        "drop": [_is_would_drop(hashes[digest]["seen"]) for digest in decided],
        "miss": [
            _is_would_drop(hashes[digest]["seen"])
            for digest in ledger.get("cited_hashes", [])
        ],
    }


def _check_frozen(frozen: Any, plan: Mapping[str, Any]) -> dict[str, list[dict]]:
    """Frozen looks are, per rate, a prefix of the plan's checkpoints."""
    if not isinstance(frozen, dict) or set(frozen) != set(RATES):
        raise TriageAccumulatorError("Frozen checkpoints have an unexpected shape")
    for rate in RATES:
        looks = frozen[rate]
        if not isinstance(looks, list) or len(looks) > len(plan["checkpoints"]):
            raise TriageAccumulatorError("Frozen checkpoints have an unexpected shape")
        for look, checkpoint in zip(looks, plan["checkpoints"]):
            if not isinstance(look, dict) or set(look) != {"checkpoint", "events"}:
                raise TriageAccumulatorError("Frozen checkpoints are invalid")
            events: Any = look.get("events")
            if (
                look.get("checkpoint") != checkpoint
                or type(events) is not int
                or not 0 <= events <= checkpoint
            ):
                raise TriageAccumulatorError("Frozen checkpoints are invalid")
    return frozen


def freeze_checkpoints(
    ledger: Mapping[str, Any],
    plan: Mapping[str, Any],
    frozen: Mapping[str, Any] | None = None,
) -> dict[str, list[dict[str, int]]]:
    """Record each checkpoint's observation the first time it is reached.

    A frozen look is never recomputed: later runs that change a hash's
    outcome, or later citations that reorder the cited sample, only affect
    checkpoints not yet reached. Pass the frozen looks from a stored ledger
    so repeated updates spend the pre-registered budget only once per look.
    """
    checked = _check_plan(plan)
    result = (
        {rate: [] for rate in RATES}
        if frozen is None
        else copy.deepcopy(_check_frozen(frozen, checked))
    )
    outcomes = _ordered_outcomes(ledger)
    for rate in RATES:
        looks = result[rate]
        for checkpoint in checked["checkpoints"][len(looks) :]:
            if len(outcomes[rate]) < checkpoint:
                break
            looks.append(
                {"checkpoint": checkpoint, "events": sum(outcomes[rate][:checkpoint])}
            )
    return result


def _interval(rate: float, lower: float, upper: float) -> dict[str, float]:
    return {
        "rate": rate,
        "lower": max(0.0, rate - lower),
        "upper": min(1.0, rate + upper),
    }


def bounds(
    ledger: Mapping[str, Any],
    plan: Mapping[str, Any] | None = None,
    frozen: Mapping[str, Any] | None = None,
) -> dict:
    """Bound the would-drop and cited-miss rates, with a pre-registered verdict.

    With a plan, checkpoint ``c`` uses the first ``c`` unique hashes in
    first-seen order (cited hashes for the miss rate), frozen when first
    reached. ``delta`` is split evenly over the checkpoints and then over the
    two monitored rates, so every look at both rates together holds at
    ``delta``. The drop rate gets a two-sided bound; the miss rate a one-sided
    bound in each direction (for a given true rate only one direction can be
    wrong). Without a plan, only half-widths at ``delta`` 0.05 are reported
    and no tolerance is inferred.
    """
    outcomes = _ordered_outcomes(ledger)
    if plan is None:
        result: dict[str, Any] = {"verdict": "no_plan", "delta": NO_PLAN_DELTA}
        for name, width in (
            ("drop", two_sided_half_width),
            ("miss", one_sided_half_width),
        ):
            n = len(outcomes[name])
            result[name] = {
                "n": n,
                "rate": sum(outcomes[name]) / n if n else None,
                "half_width": width(n, NO_PLAN_DELTA) if n else None,
                "sided": "two" if name == "drop" else "one",
            }
        return result

    checked = _check_plan(plan)
    looks = freeze_checkpoints(ledger, checked, frozen)
    per_checkpoint = checked["delta"] / len(checked["checkpoints"])
    per_rate = per_checkpoint / len(RATES)
    rows: dict[int, dict[str, Any]] = {
        c: {"checkpoint": c, "drop": None, "miss": None} for c in checked["checkpoints"]
    }
    violation = sufficient = False
    for look in looks["drop"]:
        c = look["checkpoint"]
        width = two_sided_half_width(c, per_rate)
        rows[c]["drop"] = _interval(look["events"] / c, width, width)
        violation |= rows[c]["drop"]["lower"] > checked["epsilon_drop"]
    for look in looks["miss"]:
        c = look["checkpoint"]
        width = one_sided_half_width(c, per_rate)
        rows[c]["miss"] = _interval(look["events"] / c, width, width)
        violation |= rows[c]["miss"]["lower"] > checked["epsilon_miss"]
        sufficient |= rows[c]["miss"]["upper"] <= checked["epsilon_miss"]
    if violation:
        verdict = "stop_violation"
    elif sufficient:
        verdict = "stop_sufficient"
    else:
        verdict = "continue"
    return {
        "verdict": verdict,
        "delta": checked["delta"],
        "per_checkpoint_delta": per_checkpoint,
        "per_rate_delta": per_rate,
        "epsilon_drop": checked["epsilon_drop"],
        "epsilon_miss": checked["epsilon_miss"],
        "drop_n": len(outcomes["drop"]),
        "miss_n": len(outcomes["miss"]),
        "frozen": looks,
        "checkpoints": list(rows.values()),
    }

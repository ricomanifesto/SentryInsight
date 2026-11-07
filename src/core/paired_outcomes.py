"""Compare report validity between two arms run on the same feeds.

A triage benchmark runs each frozen feed once without triage and once with it.
Comparing the two marginal validity rates treats the arms as independent
samples, but they share every input, so only the feeds whose outcome changed
carry evidence about the arm. This module counts those discordant pairs and
applies the exact two-sided sign test (McNemar's exact test). It also tallies
failure codes per arm, so a failure class that one arm introduces or removes is
visible beside the count. Every function is pure and reads no files.
"""

from __future__ import annotations

from collections import Counter
from math import comb
from typing import Any, Iterable, Mapping

VALID = "published-valid"
OUTCOMES = frozenset({VALID, "validation_failure"})
DEFAULT_ALPHA = 0.05


class PairedOutcomeError(ValueError):
    """Raised for runs that do not form complete, unique pairs."""


def exact_sign_test(baseline_only: int, treatment_only: int) -> float:
    """Two-sided exact binomial p-value for the discordant counts at p = 1/2."""
    n = baseline_only + treatment_only
    if n == 0:
        return 1.0
    k = min(baseline_only, treatment_only)
    tail = sum(comb(n, i) for i in range(k + 1)) / 2**n
    return min(1.0, 2 * tail)


def _pairs(
    runs: Iterable[Mapping[str, Any]], arms: tuple[str, str]
) -> dict[str, dict[str, Mapping[str, Any]]]:
    pairs: dict[str, dict[str, Mapping[str, Any]]] = {}
    for run in runs:
        mode, feed, outcome = run.get("mode"), run.get("date"), run.get("outcome")
        if outcome not in OUTCOMES:
            raise PairedOutcomeError(f"Unknown outcome: {outcome!r}")
        if mode not in arms or not isinstance(feed, str):
            continue
        if mode in pairs.setdefault(feed, {}):
            raise PairedOutcomeError(f"duplicate {mode} run for {feed}")
        pairs[feed][mode] = run
    incomplete = sorted(feed for feed, arm in pairs.items() if len(arm) != 2)
    if incomplete:
        raise PairedOutcomeError(f"Feeds without both arms: {incomplete}")
    if not pairs:
        raise PairedOutcomeError("There are no complete pairs to compare")
    return pairs


def compare_paired_outcomes(
    runs: Iterable[Mapping[str, Any]],
    *,
    baseline: str,
    treatment: str,
    alpha: float = DEFAULT_ALPHA,
) -> dict[str, Any]:
    """Counts, the exact sign test and per-arm failure codes; never run content."""
    pairs = _pairs(runs, (baseline, treatment))
    cells: Counter[tuple[bool, bool]] = Counter()
    codes = {baseline: Counter(), treatment: Counter()}
    shared: set[str] = set()
    for arm in pairs.values():
        valid = {mode: arm[mode]["outcome"] == VALID for mode in arm}
        cells[(valid[baseline], valid[treatment])] += 1
        failed = {
            mode: set(map(str, arm[mode].get("failure_codes") or ()))
            for mode in arm
            if not valid[mode]
        }
        for mode, found in failed.items():
            codes[mode].update(found)
        if len(failed) == 2:
            shared |= failed[baseline] & failed[treatment]
    baseline_only = cells[(True, False)]
    treatment_only = cells[(False, True)]
    p_value = exact_sign_test(baseline_only, treatment_only)
    if p_value > alpha:
        verdict = "no_evidence_of_difference"
    elif treatment_only > baseline_only:
        verdict = "treatment_more_valid"
    else:
        verdict = "baseline_more_valid"
    return {
        "pairs": len(pairs),
        "valid": {
            baseline: cells[(True, True)] + baseline_only,
            treatment: cells[(True, True)] + treatment_only,
        },
        "both_valid": cells[(True, True)],
        "both_failed": cells[(False, False)],
        "baseline_only_valid": baseline_only,
        "treatment_only_valid": treatment_only,
        "sign_test_p": p_value,
        "alpha": alpha,
        "verdict": verdict,
        "failure_codes": {
            mode: dict(sorted(found.items())) for mode, found in codes.items()
        },
        "shared_failure_codes": sorted(shared),
    }

from __future__ import annotations

import copy
import hashlib
import math

import pytest

from src.core import exploitation_triage as triage
from src.core import triage_accumulator as acc
from src.core.report_artifact import parse_report_artifact
from src.core.reporting import build_reporting_catalog, resolve_reporting_keys

LABEL_FOR = {
    triage.ACCEPTED_RELEVANT: (triage.RELEVANT, 0.99),
    triage.ACCEPTED_IRRELEVANT: (triage.NOT_EXPLOITATION, 0.99),
    triage.UNCERTAIN_KEPT: (triage.NOT_EXPLOITATION, 0.6),
    triage.INSUFFICIENT_KEPT: (triage.INSUFFICIENT, 0.9),
}


def h(name: str) -> str:
    return hashlib.sha256(name.encode()).hexdigest()


def receipt(items, *, mode="shadow", status="decided", elapsed_ms=5):
    """A valid receipt; items are (hash-or-None, disposition) pairs."""
    records = []
    for position, (digest, disposition) in enumerate(items):
        if status == "legacy_full":
            disposition = triage.LEGACY_FULL
            label = probabilities = confidence = None
        else:
            label, confidence = LABEL_FOR[disposition]
            rest = (1 - confidence) / (len(triage.LABELS) - 1)
            probabilities = {
                name: confidence if name == label else rest for name in triage.LABELS
            }
        records.append(
            {
                "position": position,
                "url_sha256": digest,
                "label": label,
                "probabilities": probabilities,
                "confidence": confidence,
                "disposition": disposition,
            }
        )
    counts = {
        name: sum(r["disposition"] == name for r in records)
        for name in triage.DISPOSITIONS
    }
    drop = counts[triage.ACCEPTED_IRRELEVANT]
    value = {
        "schema_version": 1,
        "policy_version": triage.POLICY_VERSION,
        "mode": mode,
        "status": status,
        "reason": "timeout" if status == "legacy_full" else None,
        "counterfactual": mode == "shadow",
        "requested_model": triage.MODEL,
        "models": [],
        "min_probability": 0.95,
        "timeout_seconds": 8.0,
        "article_count": len(records),
        "kept_count": len(records) - drop if mode == "enabled" else len(records),
        "would_drop_count": drop,
        "dispositions": counts,
        "input_tokens": None,
        "cost": None,
        "usage_missing": None,
        "elapsed_ms": elapsed_ms,
        "prompt_tokens_full": None,
        "prompt_tokens_triaged": None,
        "records": records,
    }
    return triage.validate_receipt(value)


KEEP = triage.ACCEPTED_RELEVANT
DROP = triage.ACCEPTED_IRRELEVANT
UNSURE = triage.UNCERTAIN_KEPT


def test_fold_deduplicates_unique_hashes_across_runs():
    first = receipt([(h("a"), KEEP), (h("b"), DROP), (None, KEEP)])
    second = receipt(
        [(h("a"), KEEP), (h("b"), DROP), (h("c"), KEEP)],
        mode="enabled",
        elapsed_ms=9,
    )
    ledger = acc.fold_receipts([first, second])
    assert ledger["runs_decided"] == 2
    assert ledger["runs_shadow"] == ledger["runs_enabled"] == 1
    assert ledger["positions_decided"] == 6
    assert ledger["positions_unhashed"] == 1
    assert ledger["unique_decided"] == 3
    assert ledger["would_drop"] == 1
    assert ledger["conflicting"] == 0
    assert ledger["hashes"][h("a")] == {"first_seen": 0, "seen": {KEEP: 2}}
    assert [ledger["hashes"][h(x)]["first_seen"] for x in "abc"] == [0, 1, 2]


def test_any_drop_marks_would_drop_and_disagreement_is_conflicting():
    ledger = acc.fold_receipts(
        [
            receipt([(h("a"), UNSURE), (h("b"), KEEP)]),
            receipt([(h("a"), DROP), (h("b"), KEEP)], elapsed_ms=6),
        ]
    )
    assert ledger["would_drop"] == 1
    assert ledger["conflicting"] == 1
    assert ledger["hashes"][h("a")]["seen"] == {UNSURE: 1, DROP: 1}


def test_legacy_full_runs_are_counted_but_contribute_no_positions():
    ledger = acc.fold_receipts(
        [
            receipt([(h("a"), KEEP), (h("b"), KEEP)], status="legacy_full"),
            receipt([(h("c"), DROP)]),
        ]
    )
    assert ledger["runs_legacy_full"] == 1
    assert ledger["positions_legacy_full"] == 2
    assert ledger["runs_decided"] == 1
    assert ledger["positions_decided"] == 1
    assert set(ledger["hashes"]) == {h("c")}


@pytest.mark.parametrize("version", [0, 2, "1", True, None])
def test_unknown_receipt_schema_versions_are_refused(version):
    value = copy.deepcopy(receipt([(h("a"), KEEP)]))
    value["schema_version"] = version
    with pytest.raises(acc.TriageAccumulatorError, match="schema_version"):
        acc.fold_receipts([value])


def test_receipts_with_text_fields_are_refused():
    value = copy.deepcopy(receipt([(h("a"), KEEP)]))
    value["records"][0]["title"] = "Article title"
    with pytest.raises(acc.TriageAccumulatorError, match="validation"):
        acc.fold_receipts([value])


def test_refolding_the_same_run_is_idempotent():
    first = receipt([(h("a"), DROP)])
    second = receipt([(h("b"), KEEP)], elapsed_ms=7)
    once = acc.fold_receipts([first])
    updated = acc.fold_receipts([first, second], once)
    assert updated == acc.fold_receipts([first, second])
    assert acc.fold_receipts([first, second], updated) == updated
    assert once == acc.fold_receipts([first])  # input ledger is not mutated
    assert len(updated["runs"]) == 2


def test_ledger_holds_counts_and_hashes_only():
    ledger = acc.fold_receipts([receipt([(h("a"), DROP)])])
    assert acc.validate_ledger(ledger) is ledger
    tampered = copy.deepcopy(ledger)
    tampered["hashes"][h("a")]["title"] = "Article title"
    with pytest.raises(acc.TriageAccumulatorError):
        acc.validate_ledger(tampered)
    tampered = copy.deepcopy(ledger)
    tampered["would_drop"] = 0
    with pytest.raises(acc.TriageAccumulatorError, match="would_drop"):
        acc.validate_ledger(tampered)


REPORT = """---
schema_version: 2
report_date: 2026-08-13
generated_at: 2026-08-13T13:21:22Z
digest_issue_url: https://ricomanifesto.github.io/SentryDigest/archive/2026-08-13/
---
# Exploitation Report

## Executive Summary

Attackers are exploiting an exposed service.

## Active Exploitation Details

### Example vulnerability (CVE-2026-1234)
- **Description**: Attackers can execute code remotely.
- **Impact**: Full service compromise.
- **Severity**: critical
- **Exploitation Status**: active
- **Action**: patch
- **CVE IDs**: CVE-2026-1234
- **Reporting**: {keys}

## Affected Systems and Products

- **Example Product**: Supported versions are affected.
"""


def published_report(articles) -> str:
    catalog = build_reporting_catalog(articles)
    return resolve_reporting_keys(REPORT.format(keys=", ".join(catalog)), catalog)


def test_published_reporting_link_maps_to_the_receipt_hash():
    canonical = {
        "link": "https://example.com/news/exploit",
        "title": "Exploit",
        "source": "Example",
    }
    other = {"link": "https://example.org/a?b=1", "title": "Other", "source": "Org"}
    artifact = parse_report_artifact(published_report([canonical, other]))
    published = {
        acc.published_url_sha256(reference.url)
        for finding in artifact.findings
        for reference in finding.reporting
    }
    assert published == {triage.url_sha256(canonical), triage.url_sha256(other)}


def test_non_canonical_feed_links_have_no_published_match():
    # Reports publish the normalized URL; receipts hash the raw stripped link.
    raw = {"link": "HTTPS://Example.com/x#frag", "title": "T", "source": "S"}
    artifact = parse_report_artifact(published_report([raw]))
    url = artifact.findings[0].reporting[0].url
    assert url == "https://example.com/x"
    assert acc.published_url_sha256(url) != triage.url_sha256(raw)


def test_join_must_keep_counts_cited_and_cited_dropped():
    ledger = acc.fold_receipts(
        [receipt([(h("a"), DROP), (h("b"), KEEP), (h("c"), DROP)])]
    )
    joined = acc.join_must_keep(ledger, [h("c"), h("b"), h("z")])
    assert joined["published"] == 3
    assert joined["published_unmatched"] == 1
    assert joined["cited"] == 2
    assert joined["cited_and_dropped"] == 1
    assert joined["cited_hashes"] == [h("b"), h("c")]
    with pytest.raises(acc.TriageAccumulatorError):
        acc.join_must_keep(ledger, ["not-a-hash"])


@pytest.mark.parametrize(("n", "expected"), [(50, 0.173), (150, 0.100), (600, 0.050)])
def test_pinned_one_sided_half_widths(n, expected):
    assert acc.one_sided_half_width(n, 0.05) == pytest.approx(expected, abs=5e-4)


def test_pinned_two_sided_half_width():
    assert acc.two_sided_half_width(600, 0.05) == pytest.approx(0.055, abs=5e-4)


def ledger_with(decided: int, drops: int, cited: int, cited_drops: int):
    """Decided hashes in order; the first `cited` are cited, drops listed first."""
    items = []
    for index in range(decided):
        dropped = index < cited_drops or cited <= index < cited + drops - cited_drops
        items.append((h(f"x{index}"), DROP if dropped else KEEP))
    # Receipts are capped at 64 KiB, so large fixtures span several runs.
    runs = [
        receipt(items[start : start + 100], elapsed_ms=start)
        for start in range(0, len(items), 100)
    ]
    ledger = acc.fold_receipts(runs)
    return acc.join_must_keep(ledger, [h(f"x{index}") for index in range(cited)])


PLAN = {
    "epsilon_drop": 0.5,
    "epsilon_miss": 0.2,
    "delta": 0.05,
    "checkpoints": [25, 50, 100, 200, 400],
}


def test_pinned_per_checkpoint_delta_and_half_width():
    # Five checkpoints at delta 0.05 give 0.01 per checkpoint, and the
    # one-sided half-width at n=100 for that delta is about 0.152.
    result = acc.bounds(acc.empty_ledger(), PLAN)
    assert result["per_checkpoint_delta"] == pytest.approx(0.01)
    assert acc.one_sided_half_width(100, 0.01) == pytest.approx(0.152, abs=5e-4)


def test_union_bound_splits_each_checkpoint_across_both_rates():
    result = acc.bounds(ledger_with(120, 0, 100, 0), PLAN)
    assert result["per_rate_delta"] == pytest.approx(0.005)
    rows = {row["checkpoint"]: row for row in result["checkpoints"]}
    # Hoeffding at delta / (2 * checkpoints): sqrt(ln(1 / 0.005) / (2 * 100)).
    assert rows[100]["miss"]["upper"] == pytest.approx(math.sqrt(math.log(200) / 200))
    assert rows[100]["drop"]["upper"] == pytest.approx(math.sqrt(math.log(400) / 200))
    assert rows[200]["miss"] is None and rows[200]["drop"] is None


def test_verdict_stop_sufficient_when_miss_upper_bound_meets_tolerance():
    result = acc.bounds(ledger_with(120, 0, 100, 0), PLAN)
    assert result["verdict"] == "stop_sufficient"


def test_verdict_continue_before_the_bound_is_tight_enough():
    result = acc.bounds(ledger_with(60, 0, 50, 0), PLAN)
    rows = {row["checkpoint"]: row for row in result["checkpoints"]}
    assert rows[50]["miss"]["upper"] > PLAN["epsilon_miss"]
    assert result["verdict"] == "continue"


def test_verdict_stop_violation_when_miss_lower_bound_exceeds_tolerance():
    result = acc.bounds(ledger_with(30, 25, 25, 25), PLAN)
    assert result["verdict"] == "stop_violation"


def test_verdict_stop_violation_when_drop_lower_bound_exceeds_tolerance():
    result = acc.bounds(ledger_with(100, 100, 0, 0), PLAN)
    assert result["miss_n"] == 0
    assert result["verdict"] == "stop_violation"


def test_checkpoints_use_first_seen_order_not_the_running_total():
    # 25 clean hashes reach the first checkpoint; later drops do not change it.
    items = [(h(f"k{i}"), KEEP) for i in range(25)]
    items += [(h(f"d{i}"), DROP) for i in range(15)]
    ledger = acc.fold_receipts([receipt(items)])
    rows = acc.bounds(ledger, PLAN)["checkpoints"]
    assert rows[0]["drop"]["rate"] == 0.0
    assert acc.bounds(ledger)["drop"]["rate"] == pytest.approx(15 / 40)


def test_no_plan_reports_half_widths_without_tolerances():
    result = acc.bounds(ledger_with(600, 60, 150, 0))
    assert result["verdict"] == "no_plan"
    assert result["delta"] == 0.05
    assert result["drop"]["n"] == 600
    assert result["drop"]["rate"] == pytest.approx(0.1)
    assert result["drop"]["half_width"] == pytest.approx(0.055, abs=5e-4)
    assert result["miss"]["half_width"] == pytest.approx(0.100, abs=5e-4)
    assert "epsilon_drop" not in result and "epsilon_miss" not in result


def test_no_plan_on_an_empty_ledger_has_no_widths():
    result = acc.bounds(acc.empty_ledger())
    assert result["drop"] == {"n": 0, "rate": None, "half_width": None, "sided": "two"}


@pytest.mark.parametrize(
    "plan",
    [
        {**PLAN, "delta": 0},
        {**PLAN, "epsilon_miss": 1.5},
        {**PLAN, "checkpoints": []},
        {**PLAN, "checkpoints": [50, 25]},
        {k: v for k, v in PLAN.items() if k != "epsilon_drop"},
        {**PLAN, "extra": 1},
    ],
)
def test_invalid_plans_are_refused(plan):
    with pytest.raises(acc.TriageAccumulatorError, match="Plan"):
        acc.bounds(acc.empty_ledger(), plan)


def test_frozen_looks_are_not_recomputed_when_outcomes_change():
    first = receipt([(h(f"k{i}"), KEEP) for i in range(25)])
    ledger = acc.join_must_keep(acc.fold_receipts([first]), [])
    frozen = acc.freeze_checkpoints(ledger, PLAN)
    assert frozen == {"drop": [{"checkpoint": 25, "events": 0}], "miss": []}

    # A later run drops every early hash; the reached look keeps its sample.
    later = receipt([(h(f"k{i}"), DROP) for i in range(25)], elapsed_ms=99)
    updated = acc.join_must_keep(acc.fold_receipts([first, later]), [])
    assert acc.freeze_checkpoints(updated, PLAN, frozen) == frozen
    assert acc.bounds(updated, PLAN, frozen)["verdict"] == "continue"
    # Without the stored looks the same data would read as a violation.
    assert acc.bounds(updated, PLAN)["verdict"] == "stop_violation"


def test_frozen_looks_only_grow_and_are_idempotent():
    ledger = ledger_with(60, 0, 30, 0)
    frozen = acc.freeze_checkpoints(ledger, PLAN)
    assert [look["checkpoint"] for look in frozen["drop"]] == [25, 50]
    assert [look["checkpoint"] for look in frozen["miss"]] == [25]
    assert acc.freeze_checkpoints(ledger, PLAN, frozen) == frozen
    grown = acc.freeze_checkpoints(ledger_with(120, 0, 60, 0), PLAN, frozen)
    assert grown["drop"][:2] == frozen["drop"]
    assert [look["checkpoint"] for look in grown["drop"]] == [25, 50, 100]


@pytest.mark.parametrize(
    "frozen",
    [
        {"drop": [{"checkpoint": 50, "events": 0}], "miss": []},
        {"drop": [{"checkpoint": 25, "events": 26}], "miss": []},
        {"drop": []},
    ],
)
def test_invalid_frozen_looks_are_refused(frozen):
    with pytest.raises(acc.TriageAccumulatorError, match="Frozen"):
        acc.bounds(acc.empty_ledger(), PLAN, frozen)


def test_ledger_plan_and_frozen_looks_are_validated_together():
    ledger = acc.fold_receipts([receipt([(h("a"), KEEP)])])
    with_plan = {**ledger, "plan": PLAN, "frozen": {"drop": [], "miss": []}}
    assert acc.validate_ledger(with_plan) is with_plan
    with pytest.raises(acc.TriageAccumulatorError, match="together"):
        acc.validate_ledger({**ledger, "plan": PLAN})

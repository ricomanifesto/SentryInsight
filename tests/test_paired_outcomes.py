import json
import subprocess
import sys
from pathlib import Path

import pytest

from src.core.paired_outcomes import (
    PairedOutcomeError,
    compare_paired_outcomes,
    exact_sign_test,
)

ROOT = Path(__file__).resolve().parents[1]


def run(date, mode, valid, codes=()):
    return {
        "date": date,
        "mode": mode,
        "outcome": "published-valid" if valid else "validation_failure",
        "failure_codes": list(codes),
    }


def test_exact_sign_test_matches_the_binomial_tail():
    assert exact_sign_test(0, 0) == 1.0
    assert exact_sign_test(1, 0) == 1.0
    assert exact_sign_test(5, 0) == pytest.approx(0.0625)
    assert exact_sign_test(0, 6) == pytest.approx(0.03125)
    assert exact_sign_test(7, 3) == exact_sign_test(3, 7) == pytest.approx(0.34375)


def test_marginal_rates_are_compared_only_through_discordant_pairs():
    # Two of five valid without triage and three of five with it looks like an
    # improvement, but only one feed changed outcome: no evidence either way.
    runs = [
        run("d1", "off", True),
        run("d1", "enabled", True),
        run("d2", "off", False, ["analysis_failed", "model_output_limit_exceeded"]),
        run("d2", "enabled", False, ["unsupported_vendor_link"]),
        run("d3", "off", True),
        run("d3", "enabled", True),
        run("d4", "off", False, ["analysis_failed", "model_output_limit_exceeded"]),
        run("d4", "enabled", False, ["invalid_reporting_source_syntax"]),
        run("d5", "off", False, ["invalid_version_reference_field"]),
        run("d5", "enabled", True),
    ]

    result = compare_paired_outcomes(runs, baseline="off", treatment="enabled")

    assert result["pairs"] == 5
    assert result["valid"] == {"off": 2, "enabled": 3}
    assert result["both_valid"] == 2
    assert result["both_failed"] == 2
    assert result["baseline_only_valid"] == 0
    assert result["treatment_only_valid"] == 1
    assert result["sign_test_p"] == 1.0
    assert result["verdict"] == "no_evidence_of_difference"
    assert result["failure_codes"] == {
        "off": {
            "analysis_failed": 2,
            "invalid_version_reference_field": 1,
            "model_output_limit_exceeded": 2,
        },
        "enabled": {
            "invalid_reporting_source_syntax": 1,
            "unsupported_vendor_link": 1,
        },
    }
    # Both arms failed on the same feeds for different reasons.
    assert result["shared_failure_codes"] == []


def test_a_consistent_one_sided_change_is_reported_with_its_direction():
    runs = []
    for index in range(6):
        runs += [run(f"d{index}", "off", False, ["x"]), run(f"d{index}", "on", True)]

    result = compare_paired_outcomes(runs, baseline="off", treatment="on", alpha=0.05)

    assert result["sign_test_p"] == pytest.approx(0.03125)
    assert result["verdict"] == "treatment_more_valid"


@pytest.mark.parametrize(
    "runs, message",
    [
        ([run("d1", "off", True)], "both arms"),
        (
            [run("d1", "off", True), run("d1", "off", True), run("d1", "on", True)],
            "duplicate",
        ),
        ([{"date": "d1", "mode": "off", "outcome": "maybe"}], "outcome"),
        ([], "no complete pairs"),
    ],
)
def test_incomplete_duplicate_or_unknown_runs_are_refused(runs, message):
    with pytest.raises(PairedOutcomeError, match=message):
        compare_paired_outcomes(runs, baseline="off", treatment="on")


def test_cli_reads_a_runs_file_and_prints_counts_only(tmp_path):
    path = tmp_path / "paired.json"
    path.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "runs": [
                    run("d1", "off", False, ["model_output_limit_exceeded"]),
                    run("d1", "enabled", True) | {"report_sha256": "secret"},
                ],
            }
        )
    )

    completed = subprocess.run(
        [sys.executable, "-B", "scripts/compare_paired_outcomes.py", str(path)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )

    printed = json.loads(completed.stdout)
    assert printed["treatment_only_valid"] == 1
    assert "secret" not in completed.stdout

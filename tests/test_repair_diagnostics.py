"""A rejected report keeps a bounded reason a repair can act on.

The reason names the failed check, field and finding, plus categorical
expected/observed values. It never carries text, CVEs, URLs or hashes.
"""

import json

import pytest

from src.core.finding_evidence import EvidenceError
from src.core.validation_diagnostics import sanitize_diagnostic, validation_diagnostic

PRIVATE = "PRIVATE-MARKER https://private.example/secret"


def evidence(code, field, expected, observed, index=2):
    error = EvidenceError(
        PRIVATE, code=code, field=field, expected=expected, observed=observed
    )
    error.finding_index = index
    error.cves = (PRIVATE,)
    error.finding_sha256 = PRIVATE
    return error


def test_grounding_rejection_keeps_categorical_expected_and_observed():
    diagnostic = validation_diagnostic(
        "finding_evidence",
        evidence(
            "unsupported_exploitation_status",
            "Exploitation Status",
            "unknown",
            "observed",
        ),
    )
    assert diagnostic["codes"] == ["unsupported_exploitation_status"]
    assert diagnostic["field"] == "Exploitation Status"
    assert diagnostic["finding_index"] == 2
    assert diagnostic["expected"] == "unknown"
    assert diagnostic["observed"] == "observed"
    assert PRIVATE not in json.dumps(diagnostic)


@pytest.mark.parametrize(
    ("expected", "observed", "safe"),
    [
        (True, False, (True, False)),
        (3, 1_000_001, (3, "invalid")),
        (PRIVATE, "not_observed", ("invalid", "not_observed")),
        (None, None, (None, None)),
    ],
)
def test_expected_and_observed_are_bounded(expected, observed, safe):
    diagnostic = validation_diagnostic(
        "finding_evidence",
        evidence(
            "affected_version_not_grounded", "Affected Versions", expected, observed
        ),
    )
    assert (diagnostic["expected"], diagnostic["observed"]) == safe
    assert PRIVATE not in json.dumps(diagnostic)


def test_unknown_codes_never_carry_values():
    diagnostic = validation_diagnostic(
        "finding_evidence", evidence("looks_like_a_secret", PRIVATE, "unknown", True)
    )
    assert diagnostic["expected"] is None and diagnostic["observed"] is None


def test_sanitizer_reapplies_the_same_bounds_to_untrusted_input():
    hostile = {
        "stage": "finding_evidence",
        "codes": ["affected_version_not_grounded", PRIVATE],
        "field": "Affected Versions",
        "finding_index": 1,
        "expected": PRIVATE,
        "observed": {"nested": PRIVATE},
        "extra": PRIVATE,
    }
    clean = sanitize_diagnostic(hostile)
    assert set(clean) == {
        "schema_version",
        "stage",
        "codes",
        "field",
        "finding_index",
        "issues_truncated",
        "expected",
        "observed",
    }
    assert clean["expected"] == "invalid" and clean["observed"] == "invalid"
    assert PRIVATE not in json.dumps(clean)

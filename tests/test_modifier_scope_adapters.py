"""Existing finite adapter boundaries, independently fixed expectations."""

import pytest
from src.core.finding_evidence import assess_exploitation
from test_owned_relation_contract import article

A = "CVE-2026-1234"


@pytest.mark.parametrize(
    "text,status,excludes",
    [
        (f"{A} is not under active exploitation.", "unknown", True),
        (f"{A} is not under limited, targeted exploitation.", "unknown", False),
        (
            f"Example Group may have not widely gained access by exploiting a vulnerability ({A}).",
            "unknown",
            False,
        ),
        (
            f"Example Group may have not gained access by exploiting a vulnerability ({A}).",
            "unknown",
            False,
        ),
        (
            f"{A} was not actively exploited and weaponized in the wild.\n\n{A} is exploited.",
            "active",
            False,
        ),
        (
            f"{A} is not actively exploited and weaponized in the wild.\n\n{A} is exploited.",
            "unknown",
            True,
        ),
    ],
)
def test_existing_adapter_scope(text, status, excludes):
    a = assess_exploitation([article(text)], [A])
    assert not a.unsupported and a.status == status
    assert any(r.assertion_projection.excludes for r in a.relations) == excludes

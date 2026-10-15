"""Restricted historical denials preserve occurrence uncertainty."""

import pytest
from src.core.finding_evidence import assess_exploitation
from test_owned_relation_contract import article
from test_historical_exploitation import HISTORICAL, RELATIVE


@pytest.mark.parametrize(
    "text,expected",
    [
        (HISTORICAL.replace("gained access", "never gained access"), "unknown"),
        (RELATIVE.replace("first began", "never began"), "unknown"),
        (HISTORICAL, "observed"),
        (RELATIVE, "observed"),
        ("CVE-2026-1234 has never been exploited.", "not_observed"),
        ("CVE-2026-1234 was not exploited.", "not_observed"),
    ],
)
def test_denial_does_not_erase_platform_role_or_time(text, expected):
    a = assess_exploitation([article(text)], ["CVE-2026-1234"])
    assert not a.unsupported and a.status == expected
    if expected == "unknown":
        assert not a.negative

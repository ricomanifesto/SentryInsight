"""Complete source-owned directive and context relations preserve their operands."""

import pytest
from src.core.recommendations import parse_recommendation
from src.core.finding_evidence import recommendation_action


@pytest.mark.parametrize("connector", [" and ", ", and ", ", but ", "; "])
@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("monitor_voice", ["active", "passive"])
def test_condition_nouns_cannot_borrow_a_later_operator(
    connector, reverse, monitor_voice
):
    monitoring = (
        "Users should monitor logs"
        if monitor_voice == "active"
        else "Logs should be monitored"
    ) + ", if reports and observations are accurate"
    parts = [monitoring, "The patch should be installed"]
    if reverse:
        parts.reverse()
    text = connector.join(parts) + "."
    parsed = parse_recommendation(text)
    assert parsed is not None and not parsed.ambiguous
    assert len(parsed.clauses) == 2
    by_verb = {c.verb: c for c in parsed.clauses}
    assert by_verb["monitor"].conditions == (
        "if reports and observations are accurate",
    )
    assert by_verb["install"].conditions == ()
    assert all(c.source_text == text for c in parsed.clauses)
    assert recommendation_action([text]) == "patch"

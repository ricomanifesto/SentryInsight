"""Complete source-owned directive and context relations preserve their operands."""

import pytest
from src.core.assertions import source_qualification
from src.core.finding_evidence import _owned_recommendation
from src.core.recommendations import RecommendationContext


@pytest.mark.parametrize("negative", ["", "not "])
@pytest.mark.parametrize("feature", ["MPLS OAM", "EXAMPLE FEATURE"])
def test_existing_typed_prerequisite_is_not_passive_advice(negative, feature):
    text = f"In the case of CVE-2026-1234, {feature} must {negative}be explicitly activated, as it is disabled by default."
    relation = source_qualification(text)
    assert relation and not relation.unsupported and relation.modal == "capability"
    owned = _owned_recommendation(text)
    assert isinstance(owned, RecommendationContext)
    assert owned.source_text == text


@pytest.mark.parametrize(
    "tail",
    [
        " Users should install the patch.",
        " Unclassified statements extend the prerequisite.",
    ],
)
def test_context_must_consume_the_whole_source_not_swallow_a_tail(tail):
    text = (
        "In the case of CVE-2026-1234, MPLS OAM must be explicitly activated, as it is disabled by default."
        + tail
    )
    relation = source_qualification(text)
    assert relation and relation.unsupported
    assert not isinstance(_owned_recommendation(text), RecommendationContext)

"""Complete source-owned directive and context relations preserve their operands."""

import pytest
from src.core.recommendations import bind_directive_frame


@pytest.mark.parametrize("voice", ["active", "passive"])
@pytest.mark.parametrize("modifier", ["", "simply "])
@pytest.mark.parametrize("negative", ["", "not "])
def test_classification_slots_remain_original_positions(voice, modifier, negative):
    target = "the infrastructure behind Example"
    text = (
        f"Users should {negative}view {target} {modifier}as a list of domains to block."
        if voice == "active"
        else f'{target.capitalize().replace("example","Example")} should {negative}be viewed {modifier}as a list of domains to block.'
    )
    f = bind_directive_frame(text)
    assert (
        f.text == text and f.argument_relation == "classification" and not f.unsupported
    )
    assert text[slice(*f.patient_span)].casefold() == target.casefold()
    assert text[slice(*f.classification_span)] == "a list of domains to block"
    assert (
        f.classification_modifier_span is None
        if not modifier
        else text[slice(*f.classification_modifier_span)] == "simply"
    )
    assert f.object_members == ("infrastructure",)

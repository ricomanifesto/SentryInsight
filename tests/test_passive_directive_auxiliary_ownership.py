"""Complete source-owned directive and context relations preserve their operands."""

import pytest
from src.core.recommendations import bind_directive_frame, has_owned_advice_cue


@pytest.mark.parametrize(
    "tail",
    [
        "Results have been published.",
        "The data has not been published.",
        "It may be relevant.",
    ],
)
def test_later_auxiliary_cannot_make_an_earlier_active_event_passive(tail):
    text = (
        "A winning entry must run code of the attacker's choice on the phone or pull sensitive information from it. "
        + tail
    )
    frame = bind_directive_frame(text)
    assert frame.voice == "active" and not frame.required
    assert not has_owned_advice_cue(text)


@pytest.mark.parametrize(
    "text",
    [
        "The report should be installed.",
        "The report should have been installed.",
        "The patch should unexpectedly be installed.",
        "The patch should begin to be installed.",
    ],
)
def test_unknown_target_or_stack_keeps_required_passive_failure(text):
    frame = bind_directive_frame(text)
    assert frame.voice == "passive" and frame.required and frame.unsupported

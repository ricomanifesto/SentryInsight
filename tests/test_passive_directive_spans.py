"""Complete source-owned directive and context relations preserve their operands."""

import pytest
import src.core.recommendations as recommendations


def frame(text, **kwargs):
    owner = getattr(recommendations, "bind_directive_frame", None)
    assert callable(owner), "one positioned directive-frame owner is required"
    return owner(text, **kwargs)


@pytest.mark.parametrize(
    "text,voice,operator,verb,patient",
    [
        ("Users should install the patch.", "active", (6, 12), (13, 20), (21, 30)),
        ("The patch should be installed.", "passive", (10, 16), (20, 29), (0, 9)),
        ("The update must not be applied.", "passive", (11, 15), (23, 30), (0, 10)),
        (
            "Logs should be monitored as soon as possible.",
            "passive",
            (5, 11),
            (15, 24),
            (0, 4),
        ),
        (
            "The patch and the update should be applied.",
            "passive",
            (25, 31),
            (35, 42),
            (0, 24),
        ),
        ("  The patch  should be installed. ", "passive", (13, 19), (23, 32), (2, 11)),
    ],
)
def test_exact_frame_slots_preserve_original_text(text, voice, operator, verb, patient):
    f = frame(text)
    assert f.text == text and f.voice == voice and not f.unsupported
    assert f.operator_span == operator and f.verb_span == verb
    assert f.patient_span == patient and f.patient_text == text[slice(*patient)]
    assert f.patient_owner is None
    assert f.binding.negative == (" not " in text)


@pytest.mark.parametrize("modal", ["should", "must", "needs to"])
def test_destination_remains_a_separate_original_slot(modal):
    text = f"The appliance {modal} be upgraded to version 2.0."
    f = frame(text)
    assert f.voice == "passive" and f.verb == "upgrade"
    assert f.patient_text == "The appliance"
    assert text[slice(*f.patient_span)] == "The appliance"
    assert text[slice(*f.tail_span)] == "to version 2.0"
    assert f.argument_relation == "direct_destination"
    assert f.object_members == ("system",) and not f.unsupported


@pytest.mark.parametrize(
    "text,negative",
    [("applied", False), ("must not be applied", True), ("should be applied", False)],
)
def test_passive_patient_inheritance_is_an_explicit_edge(text, negative):
    parent = frame("The patch should be installed")
    child = frame(text, inherited=parent)
    assert child.voice == "passive" and child.verb == "apply"
    assert child.patient_span is None and child.patient_owner is parent
    assert child.patient_text == "The patch" and child.object_members == ("patch",)
    assert child.binding.negative == negative and not child.unsupported


@pytest.mark.parametrize(
    "text", ["Users should monitor logs", "logs should be monitored", "monitor logs"]
)
def test_new_explicit_target_does_not_inherit_the_previous_patient(text):
    f = frame(text, inherited=frame("The patch should be installed"))
    assert f.patient_owner is None and f.patient_text == "logs"
    assert f.verb == "monitor" and f.object_members == ("evidence",)


@pytest.mark.parametrize(
    "text",
    ["must have been applied", "being applied", "forged", "applied inexplicably"],
)
def test_inheritance_never_rescues_unknown_operator_or_residual(text):
    f = frame(text, inherited=frame("The patch should be installed"))
    assert f.required and f.unsupported


@pytest.mark.parametrize(
    "text",
    [
        "The report should be installed",
        "The patch should have been installed",
        "The patch should be invented",
        "The patch that users deny should be installed",
    ],
)
def test_required_cue_and_frame_share_the_same_failure(text):
    f = frame(text)
    assert f.required and f.unsupported
    assert recommendations.has_owned_advice_cue(text)


@pytest.mark.parametrize(
    "text",
    [
        "The patch should be installed and applied.",
        "The patch should be installed and must not be applied.",
    ],
)
def test_renderer_relations_retain_their_frame_and_patient_edge(text):
    parsed = recommendations.parse_recommendation(text)
    assert parsed is not None and not parsed.ambiguous
    first, second = parsed.clauses
    assert first.directive_frame.voice == second.directive_frame.voice == "passive"
    assert second.directive_frame.patient_owner is first.directive_frame
    assert first.source_text == second.source_text == text


@pytest.mark.parametrize(
    "text", ["The patch was installed.", "The update has been applied."]
)
def test_descriptive_completion_does_not_acquire_a_deontic_owner(text):
    assert not frame(text).required

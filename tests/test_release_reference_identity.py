"""Bound release identities retain exact operands, spans and polarity."""

from dataclasses import replace
import pytest
import src.core.recommendations as rec
from src.core.finding_evidence import _version_argument_identity
from test_finding_generation import render, catalog_for, CVE, OTHER


def nominal(text):
    owner = getattr(rec, "_bind_nominal", None)
    assert callable(owner), "one bound nominal owner is required"
    return owner(text, version_identity=_version_argument_identity)


@pytest.mark.parametrize(
    "text",
    [
        "latest release",
        "latest releases",
        "latest version",
        "latest versions",
        "the latest release",
        "the latest releases",
        "the latest version",
        "the latest versions",
    ],
)
def test_generic_identity_is_literal_and_has_exact_complete_spans(text):
    bound = nominal(text)
    assert bound is not None and bound.text == text and bound.roles == ("release",)
    assert len(bound.members) == 1
    member = bound.members[0]
    ref = member.release
    assert (
        ref.kind == "latest" and ref.identifier is None and ref.identifier_span is None
    )
    assert text[slice(*member.span)] == ref.text == text
    assert ref.text[slice(*ref.selector_span)] == "latest"
    assert ref.text[slice(*ref.head_span)] == text.split()[-1]
    assert not bound.negative


@pytest.mark.parametrize("text", ["version 2.0", "versions 13.1.2"])
def test_numeric_identity_keeps_original_numeric_literal(text):
    bound = nominal(text)
    member = bound.members[0]
    ref = member.release
    assert ref.kind == "numbered" and ref.identifier == text.split()[-1]
    assert ref.text[slice(*ref.identifier_span)] == ref.identifier
    assert ref.selector_span is None
    assert bound.roles == ("release",)


@pytest.mark.parametrize(
    "text",
    [
        "a fixed version",
        "the recommended Example versions",
        "a supported version of Example",
        "NX-OS releases",
    ],
)
def test_existing_delegated_identity_retains_its_owner_without_number_inference(text):
    bound = nominal(text)
    member = bound.members[0]
    ref = member.release
    assert bound.roles == ("release",) and ref.kind == "delegated"
    assert ref.identifier is None and ref.identifier_span is None
    assert bound.text[slice(*member.span)] == ref.text == text


@pytest.mark.parametrize(
    "target",
    [
        "no version 2.0",
        "no latest release",
        "neither the latest release nor version 2.0",
    ],
)
def test_nominal_negative_wrapper_belongs_to_that_operand(target):
    bound = nominal(target)
    assert bound.negative and set(bound.roles) == {"release"}
    for member in bound.members:
        assert bound.text[slice(*member.span)] == member.release.text


@pytest.mark.parametrize(
    "text,relation,direct,destination",
    [
        (
            "Users should install the latest release.",
            "direct",
            "the latest release",
            None,
        ),
        (
            "Users should update to the latest version.",
            "destination",
            None,
            "the latest version",
        ),
        (
            "Users should update software to no version 2.0.",
            "direct_destination",
            "software",
            "no version 2.0",
        ),
        (
            "The appliance should be updated to the latest release.",
            "direct_destination",
            "The appliance",
            "the latest release",
        ),
    ],
)
def test_frame_keeps_direct_and_destination_operands_separate(
    text, relation, direct, destination
):
    frame = rec.bind_directive_frame(text, version_identity=_version_argument_identity)
    target = getattr(frame, "target_binding", None)
    assert target is not None and target.relation == relation
    assert (target.direct.text if target.direct else None) == direct
    assert (target.destination.text if target.destination else None) == destination
    assert frame.argument_relation == relation and frame.object_members == target.roles
    assert not frame.unsupported
    if destination == "no version 2.0":
        assert target.destination.negative and not target.direct.negative
        assert not frame.binding.negative


def test_inherited_passive_patient_retains_its_existing_owner_edge():
    parsed = rec.parse_recommendation(
        "The latest release should be installed and applied."
    )
    assert parsed and not parsed.ambiguous
    first, second = parsed.clauses
    assert second.directive_frame.patient_owner is first.directive_frame
    assert second.directive_frame.patient_span is None
    assert (
        first.directive_frame.target_binding.direct
        == second.directive_frame.target_binding.direct
    )


@pytest.mark.parametrize(
    "kind,field,value",
    [
        ("latest", "kind", "current"),
        ("latest", "identifier", "2.0"),
        ("latest", "identifier_span", (0, 3)),
        ("latest", "selector_span", (0, 3)),
        ("latest", "head_span", (0, 3)),
        ("numbered", "identifier", None),
        ("numbered", "identifier", "9.9"),
        ("numbered", "identifier_span", (0, 3)),
        ("delegated", "identifier", "2.0"),
    ],
)
def test_incompatible_reference_states_cannot_be_constructed(kind, field, value):
    source = {
        "latest": "the latest version",
        "numbered": "version 2.0",
        "delegated": "a fixed version",
    }[kind]
    ref = nominal(source).members[0].release
    with pytest.raises(ValueError):
        replace(ref, **{field: value})


@pytest.mark.parametrize(
    "text",
    [
        "the latest stable release",
        "the latest latest version",
        "the newest release",
        "current release",
        "the release",
        "release 2.0",
        "latest firmware versions",
        "the latest version that attackers exploit",
        "the latest version unexpectedly",
    ],
)
def test_unknown_nominal_material_cannot_be_consumed(text):
    assert nominal(text) is None


@pytest.mark.parametrize(
    "instruction,first,second",
    [
        (
            "Users should update to no version 2.0 and administrators should monitor logs.",
            "none",
            "monitor",
        ),
        (
            "Users should update to no latest release and administrators should install the patch.",
            "none",
            "patch",
        ),
    ],
)
def test_negative_directive_cannot_constrain_an_independent_sibling_cve(
    instruction, first, second
):
    left, right = instruction.rstrip(".").split(" and administrators should ")
    source = f"## {CVE}\n\n{left}.\n\n## {OTHER}\n\nAdministrators should {right}."
    records, _ = render(catalog_for(source))
    assert {r.cves: dict(r.fields)["Action"] for r in records} == {
        (CVE,): first,
        (OTHER,): second,
    }


@pytest.mark.parametrize(
    "text,action",
    [
        (
            "Users should update to no version 2.0 and administrators should monitor logs.",
            "monitor",
        ),
        (
            "Users should update to the latest release and administrators should not monitor logs.",
            "patch",
        ),
        (
            "Users should update to no latest release but administrators should monitor logs.",
            "monitor",
        ),
    ],
)
def test_independent_clause_roles_keep_local_nominal_prohibition(text, action):
    records, _ = render(catalog_for(f"## {CVE}\n\n{text}"))
    assert dict(records[0].fields)["Action"] == action


def test_conditions_urgency_and_operand_negation_remain_distinct():
    text = "Users should update to no latest release immediately, if exposed."
    parsed = rec.parse_recommendation(text, version_identity=_version_argument_identity)
    assert parsed and not parsed.ambiguous
    (clause,) = parsed.clauses
    assert clause.polarity == "negative" and clause.modal == "should"
    assert clause.directive_modifiers == ("immediately",)
    assert clause.conditions == ("if exposed",)
    assert clause.directive_frame.target_binding.destination.negative
    assert not clause.directive_frame.binding.negative

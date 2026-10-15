"""A determiner owns an explicit audience or a grammatical imperative addressee."""

from dataclasses import replace

import pytest

from src.core.recommendations import bind_directive_frame, parse_recommendation
from src.core.finding_evidence import recommendation_action


@pytest.mark.parametrize(
    "audience",
    [
        "Users",
        "Customers",
        "Admins",
        "Administrators",
        "Operators",
        "Owners",
        "Vendors",
        "Maintainers",
        "Organizations",
    ],
)
@pytest.mark.parametrize(
    "verb,action",
    [
        ("update", "patch"),
        ("upgrade", "patch"),
        ("patch", "patch"),
        ("mitigate", "mitigate"),
        ("investigate", "investigate"),
        ("monitor", "monitor"),
        ("restart", "none"),
    ],
)
def test_explicit_audience_system_actions(audience, verb, action):
    text = f"{audience} should {verb} their systems."
    directive = parse_recommendation(text)
    assert directive and not any(c.unsupported for c in directive.clauses)
    assert recommendation_action([text]) == action
    frame = directive.clauses[0].directive_frame
    nominal = frame.target_binding.direct
    (member,) = nominal.members
    determiner = getattr(member, "determiner", None)
    assert determiner is not None
    assert nominal.text[slice(*determiner.span)] == "their"
    assert nominal.text[slice(*member.head_span)] == "systems"
    assert determiner.person == 3 and determiner.number == "plural"
    assert determiner.owner is frame.binding.audience
    assert determiner.owner.kind == "explicit"
    assert determiner.owner.text == audience


@pytest.mark.parametrize(
    "verb,action",
    [
        ("update", "patch"),
        ("upgrade", "patch"),
        ("patch", "patch"),
        ("mitigate", "mitigate"),
        ("investigate", "investigate"),
        ("monitor", "monitor"),
        ("restart", "none"),
    ],
)
def test_imperative_addressee_is_local_syntax(verb, action):
    text = f"{verb.capitalize()} your systems."
    directive = parse_recommendation(text)
    assert directive and not any(c.unsupported for c in directive.clauses)
    assert recommendation_action([text]) == action
    frame = directive.clauses[0].directive_frame
    determiner = frame.target_binding.direct.members[0].determiner
    owner = determiner.owner
    assert owner is frame.binding.audience
    assert owner.kind == "implicit-addressee" and owner.person == 2
    assert owner.source_text == frame.text and owner.span is None
    assert owner.text == ""


@pytest.mark.parametrize(
    "spelling",
    [
        "their",
        "Their",
        "THEIR",
        "your",
        "Your",
        "YOUR",
        "our",
        "Our",
        "OUR",
        "my",
        "My",
        "MY",
        "his",
        "His",
        "HIS",
        "her",
        "Her",
        "HER",
        "its",
        "Its",
        "ITS",
    ],
)
def test_unowned_passive_determiner_cannot_be_product(spelling):
    frame = bind_directive_frame(f"{spelling} systems should be updated.")
    assert frame.required and frame.unsupported


@pytest.mark.parametrize(
    "text",
    [
        "Update their systems.",
        "They should update their systems.",
        "It should update its systems.",
        "Users should update your systems.",
        "Users should update Your systems.",
        "Users should update OUR systems.",
        "You should update their systems.",
        "Users and you should update their systems.",
        "Users and you should update your systems.",
        "Users should update their own systems.",
        "Users should update their their systems.",
        "Users should update their the systems.",
        "Users should update the Their systems.",
        "Users should install their patches.",
        "Users should upgrade to their latest versions.",
        "Users should rotate their credentials.",
        "The vendor urges users to update its systems.",
        "Users should update their systems and admins should monitor your systems.",
    ],
)
def test_unknown_or_foreign_owner_stays_unsupported(text):
    parsed = parse_recommendation(text)
    assert (
        parsed is None or parsed.ambiguous or any(c.unsupported for c in parsed.clauses)
    )


@pytest.mark.parametrize(
    "text,owners",
    [
        (
            "Users should update their systems and restart their systems.",
            ["Users", "Users"],
        ),
        (
            "Users should update their systems and admins should monitor their systems.",
            ["Users", "admins"],
        ),
        ("The vendor urges users to update their systems.", ["users"]),
        ("Users should update their systems if the vendor approves.", ["Users"]),
        ("You should update your systems.", ["You"]),
    ],
)
def test_directive_edges_preserve_owner_not_reporter_or_condition(text, owners):
    parsed = parse_recommendation(text)
    assert parsed and not any(c.unsupported for c in parsed.clauses)
    assert [
        c.directive_frame.target_binding.direct.members[0].determiner.owner.text
        for c in parsed.clauses
    ] == owners


def test_member_spans_are_independent_and_validated():
    parsed = parse_recommendation(
        "Users should update their systems and their appliances."
    )
    assert parsed and not any(c.unsupported for c in parsed.clauses)
    nominal = parsed.clauses[0].directive_frame.target_binding.direct
    assert len(nominal.members) == 2
    for member in nominal.members:
        assert nominal.text[slice(*member.determiner.span)] == "their"
        assert nominal.text[slice(*member.head_span)] in {"systems", "appliances"}
    bad = replace(nominal.members[0].determiner, span=(0, 1))
    with pytest.raises(ValueError):
        replace(nominal, members=(replace(nominal.members[0], determiner=bad),))


@pytest.mark.parametrize(
    "first,first_possessive,second,second_possessive",
    [("Users", "their", "you", "your"), ("You", "your", "users", "their")],
)
@pytest.mark.parametrize("restart", [False, True])
def test_object_list_after_independent_audience_transition(
    first, first_possessive, second, second_possessive, restart
):
    text = (
        f"{first} should update {first_possessive} systems and "
        f"{second} should monitor {second_possessive} systems"
        + (f" and restart {second_possessive} systems" if restart else "")
        + f" and {second_possessive} appliances."
    )
    parsed = parse_recommendation(text)
    assert parsed and not parsed.ambiguous
    assert recommendation_action([text]) == "patch"
    assert len(parsed.clauses) == (3 if restart else 2)
    owners = []
    for index, clause in enumerate(parsed.clauses):
        frame = clause.directive_frame
        owner = frame.binding.audience
        assert owner and owner.supported and owner.kind == "explicit"
        assert owner.text == (first if index == 0 else second)
        owners.append(owner)
        nominal = frame.target_binding.direct
        for member in nominal.members:
            determiner = member.determiner
            assert determiner and determiner.owner is owner
            assert nominal.text[slice(*determiner.span)] == (
                first_possessive if index == 0 else second_possessive
            )
            assert nominal.text[slice(*member.head_span)] in {"systems", "appliances"}
    assert owners[0] is not owners[1]
    if restart:
        assert owners[2] is owners[1]
    assert len(parsed.clauses[-1].directive_frame.target_binding.direct.members) == 2


@pytest.mark.parametrize(
    "text",
    [
        "Users should update their systems and you should monitor their appliances.",
        "You should update your systems and users should monitor your appliances.",
        "Users should update their systems and you should monitor your systems and restart their appliances.",
        "You should update your systems and users should monitor their systems and restart your appliances.",
    ],
)
def test_independent_audience_does_not_borrow_previous_possessor(text):
    parsed = parse_recommendation(text)
    assert parsed and parsed.ambiguous
    assert any(clause.unsupported for clause in parsed.clauses)


@pytest.mark.parametrize(
    "predicate,action",
    [
        ("review logs on", "investigate"),
        ("rotate credentials for", "none"),
        ("install patches for", "patch"),
    ],
)
@pytest.mark.parametrize("determiner", ["their", "the"])
def test_nested_modifier_keeps_existing_possessive_boundary(
    predicate, action, determiner
):
    text = f"Users should {predicate} {determiner} systems."
    parsed = parse_recommendation(text)
    assert parsed is not None
    if determiner == "their":
        assert parsed.ambiguous and any(c.unsupported for c in parsed.clauses)
    else:
        assert not parsed.ambiguous
        assert recommendation_action([text]) == action

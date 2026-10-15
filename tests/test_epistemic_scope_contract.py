"""Knowledge absence retains source ownership and independent factual claims."""

import pytest
from src.core.finding_evidence import assess_exploitation
from test_owned_relation_contract import article

A = "CVE-2026-1234"
B = "CVE-2026-5678"
cases = []


def add(group, text, status, ids=(A,), *, conflict=False, unsupported=False):
    cases.append(
        {
            "id": f'{group}-{sum(c["group"]==group for c in cases)+1:03}',
            "group": group,
            "sources": [text] if isinstance(text, str) else text,
            "expected_status": status,
            "ids": list(ids),
            "expected_conflict": conflict,
            "expected_unsupported": unsupported,
        }
    )


for finite, status in [
    ("is", "active"),
    ("are", "active"),
    ("was", "observed"),
    ("were", "observed"),
]:
    for event in ["exploited", "weaponized", "under active exploitation"]:
        add("known-positive", f"{A} {finite} known to be {event}.", status)
        for neg in ["not", "never"]:
            add(
                "knowledge-negative",
                f"{A} {finite} {neg} known to be {event}.",
                "unknown",
            )
            add(
                "event-negative",
                f"{A} {finite} known {neg} to be {event}.",
                "unknown" if event.startswith("under") else "not_observed",
            )
    add("known-positive", f"Attackers {finite} known to be exploiting {A}.", status)
    for neg in ["not", "never"]:
        add(
            "knowledge-negative",
            f"Attackers {finite} {neg} known to be exploiting {A}.",
            "unknown",
        )
        add(
            "event-negative",
            f"Attackers {finite} known to {neg} be exploiting {A}.",
            "not_observed",
        )

for modifier in [
    "actively",
    "currently",
    "now",
    "widely",
    "publicly",
    "successfully",
    "likely",
    "also",
]:
    for text in [
        f"{A} is not {modifier} known to be exploited.",
        f"{A} is {modifier} not known to be exploited.",
        f"{A} is not known to be {modifier} exploited.",
    ]:
        add("knowledge-modifier-order", text, "unknown")
    add(
        "current-coexistence",
        [
            f"{A} is not {modifier} known to be exploited.",
            f"{A} is actively exploited.",
        ],
        "active",
    )
    add(
        "historical-coexistence",
        [
            f"{A} is not known to be {modifier} exploited.",
            f"{A} was exploited yesterday.",
        ],
        "observed",
    )

for finite, positive, expected in [
    ("is", "is actively exploited", "active"),
    ("was", "was exploited yesterday", "observed"),
]:
    for voice in ["cve", "actor"]:
        unknown = (
            f"{A} {finite} not known to be exploited."
            if voice == "cve"
            else f"Attackers {finite} not known to be exploiting {A}."
        )
        add("independent-positive", [unknown, f"{A} {positive}."], expected)

for text, status in [
    (f"{A} is not known to be exploited and weaponized.", "unknown"),
    (f"{A} is not known to be exploited and is actively exploited.", "active"),
    (f"{A} is not known to be exploited but was exploited yesterday.", "observed"),
    (f"{A} is not known to be exploited but weaponized.", "unknown"),
    (f"{A} is known not to be exploited and weaponized.", "not_observed"),
    (f"{A} is not only known to be exploited but is actively exploited.", "active"),
    (f"{A} is known to be not only exploited but weaponized.", "active"),
]:
    add("coordination", text, status)

for text in [
    f"The vendor has found evidence that {A} is not known to be exploited.",
    f"There is no evidence that {A} is not known to be exploited.",
    f"{A} is not known to be exploited if reports are accurate.",
    f"{A} is not known to be exploited as investigators confirmed yesterday.",
    f"It is possible that {A} is not known to be exploited.",
]:
    add("wrappers", text, "unknown")
for text in [
    f"{A} and {B} are not known to be exploited.",
    f"Attackers are not known to be exploiting {A} and {B}.",
]:
    add("joint-owner", text, "unknown", (A, B))
add(
    "sibling-owner",
    f"{A} is not known to be exploited. {B} is actively exploited.",
    "active",
    (B,),
)
add(
    "sibling-owner",
    f"{A} is not known to be exploited. {B} was exploited yesterday.",
    "unknown",
    (A,),
)

for text, status, conflict in [
    (f"{A} is not exploited.", "not_observed", False),
    (f"{A} is not widely exploited.", "unknown", False),
    (f"{A} is not actively exploited.", "unknown", False),
    (f"{A} is not actively exploited. {A} is actively exploited.", "unknown", True),
    (f"{A} is not actively exploited. {A} was exploited yesterday.", "observed", False),
    (f"{A} may not be exploited.", "unknown", False),
    (f"{A} has begun to be exploited.", "observed", False),
    (f"Attackers continue to exploit {A}.", "active", False),
    (f"Attackers continued to exploit {A}.", "observed", False),
    (f"Exploitation of {A} has not been confirmed.", "unknown", False),
    (f"Exploitation of {A} has not been observed.", "not_observed", False),
    (
        f"The vendor has not found evidence that {A} is exploited.",
        "not_observed",
        False,
    ),
]:
    add("ordinary-preservation", text, status, conflict=conflict)

for text in [
    f"{A} is not not known to be exploited.",
    f"{A} is never not known to be exploited.",
    f"{A} is not known not to be exploited.",
    f"{A} is known to not be never exploited.",
    f"{A} is known known to be exploited.",
    f"{A} may be known to be exploited.",
    f"{A} has been known to be exploited.",
    f"{A} is not known to have been exploited.",
    f"{A} is known to be being exploited.",
    f"{A} will be known to be exploited.",
    f"{A} has not begun to be exploited.",
    f"Attackers do not continue to exploit {A}.",
    f"{A} is not known to be exploited tomorrow.",
    f"{A} was known to be exploited now.",
    f"{A} is observed known to be exploited.",
]:
    add("unsupported-stacks", text, "unknown", unsupported=True)


add(
    "owned-correlative",
    "CVE-2026-1234 is not known to be not only exploited but weaponized.",
    "unknown",
)
add(
    "owned-correlative",
    "CVE-2026-1234 is not only not known to be exploited but is actively exploited.",
    "active",
)
add(
    "owned-correlative",
    "CVE-2026-1234 is not known to be exploited and was weaponized yesterday.",
    "observed",
)
add(
    "owned-correlative",
    "CVE-2026-1234 was not known to be exploited but weaponized in the wild.",
    "unknown",
)


@pytest.mark.parametrize("row", cases, ids=lambda row: row["id"])
def test_epistemic_scope_and_independent_source_claims(row):
    sources = [
        article(text, link=f"https://example.test/epistemic/{i}")
        for i, text in enumerate(row["sources"])
    ]
    assessment = assess_exploitation(sources, row["ids"])
    assert assessment.status == row["expected_status"]
    assert assessment.conflicting == row["expected_conflict"]
    assert bool(assessment.unsupported) == row["expected_unsupported"]

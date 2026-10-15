"""Literal release targets compose existing action frames and source ownership."""

import pytest
from src.core.finding_evidence import (
    EvidenceError,
    _complete_recommendation_fragment,
    _recommendation_source_statements,
    validate_finding_evidence,
)
from test_finding_generation import CVE, catalog_for, render

rows = []


def add(group, text, action=None, *, unsupported=False):
    rows.append(
        {
            "id": f'{group}-{sum(x["group"]==group for x in rows)+1:03d}',
            "group": group,
            "text": text,
            "expected_action": action,
            "expected_unsupported": unsupported,
        }
    )


frames = [
    "install {}",
    "apply {}",
    "patch {}",
    "upgrade {}",
    "update {}",
    "upgrade to {}",
    "update to {}",
    "upgrade the appliance to {}",
    "update software to {}",
]
forms = [
    ("Users should {}.", "patch"),
    ("Users should not {}.", "none"),
    ("Users should {} only if exposed.", "none"),
]
for target in ["the latest release", "the latest version"]:
    for frame in frames:
        for form, action in forms:
            add("generic-frames", form.format(frame.format(target)), action)
for target in [
    "latest release",
    "latest version",
    "latest releases",
    "latest versions",
    "the latest releases",
    "the latest versions",
]:
    add("generic-nominals", f"Users should update to {target}.", "patch")
for form, action in [
    ("Update to {}.", "patch"),
    ("Do not update to {}.", "none"),
    ("Users must update to {}.", "patch"),
    ("Users need to update to {}.", "patch"),
    ("Users are advised to update to {}.", "patch"),
    ("Users are not advised to update to {}.", "none"),
    ("The vendor recommends updating to {}.", "patch"),
    ("The vendor does not recommend updating to {}.", "none"),
    ("Users should immediately update to {}.", "patch"),
    ("Users should update to {} as soon as possible.", "patch"),
    ("If exposed, users should update to {}.", "none"),
    ("Users should update to {}. Do not do so until access is approved.", "none"),
    ("The appliance should be updated to {}.", "patch"),
    ("The appliance must not be upgraded to {}.", "none"),
    ("{} should be installed.", "patch"),
    ("{} should not be applied.", "none"),
    ("{} should be installed and applied.", "patch"),
    ("Users should update to {} and monitor logs.", "patch"),
    ("Users should monitor logs and update to {}.", "patch"),
    ("Users should update to {} or monitor logs.", "none"),
    ("Users should not update to {} but monitor logs.", "monitor"),
    (
        "Users should update to {} and administrators should monitor logs if exposed.",
        "patch",
    ),
    ("Users should update to {} but users should not install the patch.", "none"),
]:
    for target in ["the latest release", "the latest version"]:
        add("generic-context", form.format(target), action)
for target in [
    "version 2.0",
    "a fixed version",
    "the recommended versions",
    "a supported version of Example",
]:
    for form, action in forms:
        add("existing-owner", form.format("update to " + target), action)
for text in [
    "Users should update to no version 2.0.",
    "Users should upgrade the appliance to no version 2.0.",
    "The appliance should be updated to no version 2.0.",
    "Users should update to neither version 2.0 nor version 3.0.",
    "Users should update to the latest version and then upgrade to no version 2.0.",
    "Users should update to no latest release.",
    "Users should install no latest release.",
    "Users should update to neither the latest release nor version 2.0.",
]:
    add("nominal-negation", text, "none")
for text in [
    "Users should update to the advisory.",
    "Users should upgrade to the vendor.",
    "Users should install to the latest release.",
    "Users should monitor the latest version.",
    "Users should update to latest firmware versions.",
    "Users should update to release 2.0.",
    "Users should update to version.",
    "Users should update to the release.",
    "Users should update to the fixed release.",
    "Users should update to the supported release.",
    "Users should update to the most recent release.",
    "Users should update to the latest stable release.",
    "Users should update to the latest latest version.",
    "Users should update to the latest version unexpectedly.",
    "Users should update to the latest version that attackers exploit.",
    "Users should update to the latest version from an unrecognized channel.",
    "Users should consider updating to the latest version.",
    "The latest version should have been installed.",
    "The latest version should be invented.",
    "Users should migrate to the latest version.",
    "Widgets should update to the latest release.",
]:
    add("unsupported-boundary", text, unsupported=True)
for text in [
    "The latest release is available.",
    "The latest version was installed.",
    "Update 1.2 fixes the vulnerability.",
]:
    add("narrative", text, "none")
for target in [
    "the latest release and version 2.0",
    "the latest release and the patch",
]:
    add("nominal-coordination", "Users should install " + target + ".", "patch")


@pytest.mark.parametrize("case", rows, ids=[row["id"] for row in rows])
def test_complete_release_target_behavior(case):
    text = case["text"]
    catalog = catalog_for(f"## {CVE}\n\n{text}")
    if case["expected_unsupported"]:
        with pytest.raises(EvidenceError):
            render(catalog)
        return
    records, report = render(catalog)
    fields = dict(records[0].fields)
    assert fields["Action"] == case["expected_action"]
    assert fields["Affected Versions"] == "Not stated in supplied sources."
    if case["group"] == "narrative":
        assert fields["Recommended Actions"] == "Not stated in supplied sources."
        return
    assert text in fields["Recommended Actions"]
    units = tuple(_recommendation_source_statements(text))
    assert " ".join(units) == text
    assert all(_complete_recommendation_fragment(unit) for unit in units)
    if "latest" in text:
        changed = report.replace("latest release", "version 9.9").replace(
            "latest version", "version 9.9"
        )
        assert changed != report
        with pytest.raises(EvidenceError):
            validate_finding_evidence(changed, catalog)

import hashlib

import pytest

from src.core.finding_evidence import ABSENT, EvidenceError, validate_finding_evidence
from src.core.reporting import build_reporting_catalog

CVE = "CVE-2026-1234"
OTHER = "CVE-2026-5678"


def source(content, suffix="one"):
    return {
        "title": "Synthetic advisory",
        "source": "Synthetic publisher",
        "link": f"https://example.test/{suffix}",
        "content": content,
        "content_kind": "article",
    }


def report(keys, versions=ABSENT, cves=CVE, exceptions=ABSENT, status="active"):
    return f"""## Active Exploitation Details

### Gateway ({cves})
- **Description**: A service vulnerability.
- **Exploitation Status**: {status}
- **Action**: monitor
- **CVE IDs**: {cves}
- **Reporting**: {', '.join(keys)}
- **Affected Versions**: {versions}
- **Exceptions**: {exceptions}
- **Recommended Actions**: {ABSENT}
- **Vendor Links**: {ABSENT}
"""


def contract(catalog, cves=(CVE,)):
    from src.core.version_references import build_version_reference_context

    return next(
        item
        for item in build_version_reference_context(catalog)
        if item["cves"] == list(cves)
    )


def resolve(candidate, catalog):
    from src.core.version_references import resolve_version_references

    return resolve_version_references(candidate, catalog)


def test_no_range_scope_has_explicit_absence_without_inferred_fixed_versions():
    catalog = build_reporting_catalog(
        [
            source(
                f"{CVE} is actively exploited.\n\n"
                "A patch was released on October 21.\n\n"
                f"{OTHER} affects Gateway 9.0."
            )
        ]
    )
    item = contract(catalog)
    assert item["absence_allowed"] is True
    assert item["constraints"] == []
    candidate = report(catalog)
    assert resolve(candidate, catalog) == candidate
    validate_finding_evidence(candidate, catalog)


def test_source_owned_constraint_keeps_complete_qualifiers_and_exclusions():
    catalog = build_reporting_catalog(
        [
            source(
                f"{CVE} is actively exploited.\n\nAffected versions:\n\n"
                "Gateway 2.3 (Windows only), and users of Gateway 2.3.9 are not affected"
            )
        ]
    )
    item = contract(catalog)
    assert item["absence_allowed"] is False
    [constraint] = item["constraints"]
    assert constraint["text"] == "Gateway 2.3 (Windows only)"
    assert constraint["source_key"] in catalog
    assert (
        constraint["content_sha256"]
        == hashlib.sha256(next(iter(catalog.values())).content.encode()).hexdigest()
    )
    rendered = resolve(
        report(catalog, constraint["id"], exceptions="Gateway 2.3.9"), catalog
    )
    assert "**Affected Versions**: Gateway 2.3 (Windows only)" in rendered
    assert constraint["id"] not in rendered
    validate_finding_evidence(rendered, catalog)


@pytest.mark.parametrize(
    "value",
    [
        "Gateway before 9.0",
        "Unknown",
        "version-deadbeefdeadbeef",
        ABSENT + "; Gateway 9.0",
    ],
)
def test_unsupported_claims_are_rejected_without_rewriting_or_content_errors(value):
    catalog = build_reporting_catalog([source(f"{CVE} is actively exploited.")])
    candidate = report(catalog, value)
    with pytest.raises(EvidenceError) as caught:
        resolve(candidate, catalog)
    assert caught.value.field == "Affected Versions"
    assert value not in str(caught.value)
    assert caught.value.finding_index == 1
    assert caught.value.cves == (CVE,)
    assert candidate == report(catalog, value)


def test_absence_cannot_drop_a_required_constraint_from_an_uncited_source():
    catalog = build_reporting_catalog(
        [
            source(f"{CVE} is actively exploited."),
            source(
                f"{CVE} is actively exploited.\n\nAffected versions: Gateway 2.3", "two"
            ),
        ]
    )
    with pytest.raises(EvidenceError, match="absence"):
        resolve(report([next(iter(catalog))]), catalog)


def test_wrong_cve_stale_source_and_uncited_references_fail_closed():
    first = source(f"{CVE} is actively exploited.\n\nAffected versions: Gateway 2.3")
    second = source(
        f"{OTHER} is actively exploited.\n\nAffected versions: Gateway 4.5", "two"
    )
    catalog = build_reporting_catalog([first, second])
    reference = contract(catalog)["constraints"][0]["id"]
    with pytest.raises(EvidenceError):
        resolve(report(catalog, reference, cves=OTHER), catalog)
    changed = build_reporting_catalog(
        [{**first, "content": first["content"] + "\nUpdated."}]
    )
    with pytest.raises(EvidenceError):
        resolve(report(changed, reference), changed)
    both = build_reporting_catalog(
        [first, {**second, "content": second["content"].replace(OTHER, CVE)}]
    )
    with pytest.raises(EvidenceError):
        resolve(report([list(both)[1]], reference), both)


def test_duplicate_and_partial_reference_sets_are_rejected():
    catalog = build_reporting_catalog(
        [
            source(
                f"{CVE} is actively exploited.\n\nAffected versions: Gateway 2.3; Gateway 2.4"
            )
        ]
    )
    refs = [entry["id"] for entry in contract(catalog)["constraints"]]
    assert len(refs) == 2
    for value in (refs[0], f"{refs[0]}; {refs[0]}"):
        with pytest.raises(EvidenceError):
            resolve(report(catalog, value), catalog)
    rendered = resolve(report(catalog, "; ".join(refs)), catalog)
    validate_finding_evidence(rendered, catalog)


def test_ambiguous_and_unlabelled_version_evidence_cannot_be_called_absent():
    for text in (
        f"{CVE} is actively exploited.\n\nGateway 2.3",
        f"{CVE} is actively exploited. Customers should install the update for {OTHER}.",
    ):
        catalog = build_reporting_catalog([source(text)])
        assert contract(catalog)["absence_allowed"] is False
        with pytest.raises(EvidenceError):
            resolve(report(catalog), catalog)


@pytest.mark.parametrize(
    "detail",
    [
        "Gateway 9.0 is vulnerable in another configuration.",
        "Gateway versions earlier than 7 also permit access.",
    ],
)
def test_a_known_list_cannot_hide_unresolved_version_prose(detail):
    catalog = build_reporting_catalog(
        [
            source(
                f"{CVE} is actively exploited.\n\nAffected versions: Gateway 2.3\n\n"
                f"A separate observation follows.\n\n{detail}"
            )
        ]
    )
    item = contract(catalog)
    assert item["blocked"] is True
    with pytest.raises(EvidenceError, match="unresolved"):
        resolve(report(catalog, item["constraints"][0]["id"]), catalog)


def test_contradictory_constraints_fail_closed():
    catalog = build_reporting_catalog(
        [
            source(f"{CVE} is actively exploited.\n\nAffected versions: Gateway 2.3"),
            source(
                f"{CVE} is actively exploited.\n\nAffected versions: users of Gateway 2.3 are not affected",
                "two",
            ),
        ]
    )
    item = contract(catalog)
    assert item["blocked"] is True
    with pytest.raises(EvidenceError, match="unresolved"):
        resolve(report(catalog, item["constraints"][0]["id"]), catalog)


def test_absence_requires_the_cited_source_to_belong_to_the_cve_scope():
    catalog = build_reporting_catalog(
        [
            source(f"{CVE} is actively exploited."),
            source(f"{OTHER} is actively exploited.", "two"),
        ]
    )
    with pytest.raises(EvidenceError):
        resolve(report([list(catalog)[1]]), catalog)
    with pytest.raises(EvidenceError):
        resolve(report([list(catalog)[0]], cves=""), catalog)


def test_joint_scopes_preserve_qualifiers_and_do_not_accept_singleton_references():
    catalog = build_reporting_catalog(
        [
            source(
                f"{CVE} and {OTHER} are actively exploited.\n\nAffected versions: Gateway 2.3 (Windows only)"
            )
        ]
    )
    joint = contract(catalog, (CVE, OTHER))
    reference = joint["constraints"][0]["id"]
    rendered = resolve(report(catalog, reference, cves=f"{CVE}, {OTHER}"), catalog)
    assert "Gateway 2.3 (Windows only)" in rendered
    with pytest.raises(EvidenceError):
        resolve(report(catalog, reference), catalog)
    with pytest.raises(EvidenceError):
        resolve(
            report(catalog, reference + " (Linux only)", cves=f"{CVE}, {OTHER}"),
            catalog,
        )


@pytest.mark.parametrize(
    "detail",
    [
        "Gateway 1.x",
        "Gateway 1.*",
        "Gateway 7",
        "All Gateway releases permit access.",
        "Gateway versions earlier than 7 permit access.",
    ],
)
def test_unresolved_range_forms_never_authorize_absence(detail):
    catalog = build_reporting_catalog(
        [source(f"{CVE} is actively exploited.\n\n{detail}")]
    )
    assert contract(catalog)["absence_allowed"] is False
    with pytest.raises(EvidenceError):
        resolve(report(catalog), catalog)


@pytest.mark.parametrize("known_list", [False, True])
@pytest.mark.parametrize(
    "assertion",
    [
        "Gateway 7 is vulnerable.",
        "Gateway 7 is affected.",
        "Gateway 7 remains impacted.",
        "Users of Gateway 7 are affected.",
    ],
)
def test_bare_major_assertions_block_absence_and_incomplete_lists(
    known_list, assertion
):
    prefix = (
        "Affected versions: Gateway 2.3\n\nA separate observation follows.\n\n"
        if known_list
        else ""
    )
    catalog = build_reporting_catalog(
        [source(f"{CVE} is actively exploited.\n\n{prefix}{assertion}")]
    )
    scope = contract(catalog)
    assert scope["blocked"] is True
    assert scope["absence_allowed"] is False
    value = "; ".join(item["id"] for item in scope["constraints"]) or ABSENT
    with pytest.raises(EvidenceError) as caught:
        resolve(report(catalog, value), catalog)
    assert caught.value.code == "unresolved_version_evidence"


def test_explicit_bare_major_list_retains_its_complete_constraint():
    catalog = build_reporting_catalog(
        [
            source(
                f"{CVE} is actively exploited.\n\nAffected versions: Gateway 7 (Windows only)"
            )
        ]
    )
    scope = contract(catalog)
    assert scope["blocked"] is False
    [constraint] = scope["constraints"]
    assert constraint["text"] == "Gateway 7 (Windows only)"
    rendered = resolve(report(catalog, constraint["id"]), catalog)
    validate_finding_evidence(rendered, catalog)


def test_actor_identifiers_do_not_become_bare_major_version_numbers():
    catalog = build_reporting_catalog(
        [
            source(
                f"{CVE} is actively exploited.\n\n"
                "The activity targeting vulnerable devices is tracked as UTA0576."
            )
        ]
    )
    assert contract(catalog)["absence_allowed"] is True
    assert resolve(report(catalog), catalog) == report(catalog)


def test_resolved_versions_do_not_bypass_existing_exclusion_checks():
    catalog = build_reporting_catalog(
        [
            source(
                f"{CVE} is actively exploited.\n\nAffected versions: Gateway 2.3, and users of Gateway 2.3.9 are not affected"
            )
        ]
    )
    reference = contract(catalog)["constraints"][0]["id"]
    rendered = resolve(report(catalog, reference), catalog)
    with pytest.raises(EvidenceError) as caught:
        validate_finding_evidence(rendered, catalog)
    assert caught.value.code == "missing_source_exclusions"


def test_wrapped_claim_and_duplicate_fields_cannot_hide_behind_a_reference():
    catalog = build_reporting_catalog(
        [source(f"{CVE} is actively exploited.\n\nAffected versions: Gateway 2.3")]
    )
    reference = contract(catalog)["constraints"][0]["id"]
    candidate = report(catalog, reference)
    for bad in (
        candidate.replace(reference, reference + "\n  and Gateway 9.0"),
        candidate.replace(
            reference, reference + "\n- **Affected Versions**: " + ABSENT
        ),
    ):
        with pytest.raises(EvidenceError):
            resolve(bad, catalog)


@pytest.mark.parametrize(
    "detail",
    [
        "Fixed in Gateway 2.3.",
        "Fixed in Gateway 7.",
        "CVSS score: 9.8.",
        "CVSS score: 7.",
        "The flaw has a CVSS score of 9.8.",
    ],
)
def test_fixed_releases_and_severity_scores_do_not_become_affected_ranges(detail):
    catalog = build_reporting_catalog(
        [source(f"{CVE} is actively exploited.\n\n{detail}")]
    )
    item = contract(catalog)
    assert item["constraints"] == []
    assert item["absence_allowed"] is True
    assert resolve(report(catalog), catalog) == report(catalog)
    with pytest.raises(EvidenceError):
        resolve(report(catalog, "Gateway before 2.3"), catalog)


@pytest.mark.parametrize(
    "detail",
    [
        "A botnet of more than 2.4 million devices lost access to its servers.",
        "A botnet of 12 million devices has 3 command servers.",
        "A botnet of 12 million devices contacted servers on July 6.",
    ],
)
def test_no_cve_scaled_quantities_do_not_assert_affected_versions(detail):
    catalog = build_reporting_catalog(
        [source("Attackers are exploiting devices in active attacks.\n\n" + detail)]
    )
    scope = contract(catalog, ())
    assert scope["blocked"] is False
    assert scope["absence_allowed"] is True
    assert scope["constraints"] == []
    candidate = report(catalog, cves="None", status="unknown")
    assert resolve(candidate, catalog) == candidate
    validate_finding_evidence(candidate, catalog)
    with pytest.raises(EvidenceError) as caught:
        validate_finding_evidence(report(catalog, cves="None"), catalog)
    assert caught.value.code == "unsupported_exploitation_status"
    with pytest.raises(EvidenceError):
        resolve(
            report(
                catalog, versions="Gateway before 3.1", cves="None", status="unknown"
            ),
            catalog,
        )


@pytest.mark.parametrize(
    "detail",
    [
        "The Moonbot 3.1 botnet targets Gateway 7.",
        "The Moonbot 3.1 botnet targets Gateway 7.2.",
        "The Moonbot 3.1 botnet targets earlier Gateway releases.",
        "The Moonbot 3.1 botnet targets Gateway v7.",
        "The Moonbot 3.1 botnet is vulnerable.",
        "A campaign affecting 2.4 million devices leaves Gateway 7 vulnerable.",
        "A botnet controls 2.4 million devices running Gateway 7.",
        "Users of Moonbot 3.1 botnet are affected.",
        "The Moonbot 3.1 botnet targets Gateway releases from July 2025.",
        "The botnet of 1.3 million devices targets Gateway version July 2025.",
        "The Moonbot 3.1 botnet targets Gateway July 2025.",
        "The Moonbot 3.1 botnet targets Gateway releases in July 2025.",
        "The Moonbot 3.1 botnet targets a Gateway build released in July 2025.",
        "The Moonbot 3.1 botnet targets Gateway software released in July 2025.",
        "The Moonbot 3.1 botnet targets Gateway firmware shipped in July 2025.",
        "The Moonbot 3.1 botnet targets Gateway editions released in July 2025.",
        "The Moonbot 3.1 botnet targets the Gateway image distributed on July 8, 2025.",
        "The botnet of 1.3 million devices targets Gateway software released in July 2025.",
        "Android 8.1 botnet infections were confirmed on televisions running that operating system.",
        "The Gateway firmware shipped with the Moonbot 3.1 botnet in July 2025 is targeted.",
        "When investigators disrupted the Moonbot 3.1 botnet in July 2025, "
        "the more than 12 million devices involved were uncertified.",
        "Investigators disrupted the Moonbot 3.1 botnet.",
    ],
)
def test_non_version_numbers_do_not_hide_unresolved_target_versions(detail):
    catalog = build_reporting_catalog(
        [source("Attackers are exploiting devices in active attacks.\n\n" + detail)]
    )
    assert contract(catalog, ())["blocked"] is True
    with pytest.raises(EvidenceError) as caught:
        resolve(report(catalog, cves="None", status="unknown"), catalog)
    assert caught.value.code == "unresolved_version_evidence"


def test_quantity_near_a_known_version_list_does_not_hide_required_constraint():
    catalog = build_reporting_catalog(
        [
            source(
                "Attackers are exploiting devices in active attacks.\n\n"
                "A botnet of 2.4 million devices lost its servers.\n\n"
                "Affected versions: Gateway 7 (Windows only)"
            )
        ]
    )
    scope = contract(catalog, ())
    assert scope["blocked"] is False
    assert scope["absence_allowed"] is False
    [constraint] = scope["constraints"]
    assert constraint["text"] == "Gateway 7 (Windows only)"
    with pytest.raises(EvidenceError):
        resolve(report(catalog, cves="None", status="unknown"), catalog)
    rendered = resolve(
        report(catalog, constraint["id"], cves="None", status="unknown"), catalog
    )
    validate_finding_evidence(rendered, catalog)

"""Unknown source-level qualification ownership must remain fail-closed."""

import pytest

from src.core.finding_evidence import EvidenceError, validate_finding_evidence
from src.core.reporting import build_reporting_catalog
from src.core.version_references import (
    build_version_reference_context,
    resolve_version_references,
)
from test_version_references import report, source, with_version_state

TARGET = "An attack vector targets instances running version 3.2 or earlier."
RANGE = "instances running version 3.2 or earlier"


@pytest.mark.parametrize(
    "content",
    [
        TARGET + "\n\nOnly Windows installations are impacted.",
        "Only Windows installations are impacted.\n\n" + TARGET,
        TARGET + "\n\nThis applies only when remote administration is enabled.",
        "This applies only when remote administration is enabled.\n\n" + TARGET,
        TARGET + "\n\n- Only Windows installations are impacted.",
        "## Windows installations only\n\n" + TARGET,
        "## Deployment conditions\n\nOnly Windows installations are impacted.\n\n"
        "## Attack vector\n\n" + TARGET,
        TARGET + "\n\nOnly the database product is impacted.",
        "The following statement is incorrect.\n\n" + TARGET,
        TARGET + "\n\nThe preceding statement is incorrect.",
    ],
)
def test_unknown_source_qualification_ownership_cannot_publish_an_unrestricted_range(
    content,
):
    catalog = build_reporting_catalog([source(content)])
    [scope] = build_version_reference_context(catalog)
    assert scope["state"] == "blocked"
    assert not scope["absence_allowed"]
    assert not scope["unresolved_allowed"]
    with pytest.raises(EvidenceError):
        resolve_version_references(
            report(catalog, cves="None", status="unknown"), catalog
        )
    # A forged canonical field cannot bypass the source-scope check either.
    forged = with_version_state(
        report(catalog, RANGE, cves="None", status="unknown"), "supported"
    )
    with pytest.raises(EvidenceError):
        validate_finding_evidence(forged, catalog)


CVE_A = "CVE-2026-1234"
CVE_B = "CVE-2026-5678"


def scope_for(catalog, cves=(CVE_A,), context=None):
    return next(
        item
        for item in build_version_reference_context(catalog, context)
        if item["cves"] == list(cves)
    )


def assert_scope_rejected(catalog, scope, cited_keys=None):
    assert scope["state"] == "blocked"
    assert "unowned_version_evidence" in scope["failure_reasons"]
    assert not scope["absence_allowed"]
    assert not scope["unresolved_allowed"]
    keys = list(cited_keys or catalog)
    value = "; ".join(c["id"] for c in scope["constraints"])
    with pytest.raises(EvidenceError):
        resolve_version_references(
            report(
                keys,
                value or "Not stated in supplied sources.",
                cves=CVE_A,
                status="unknown",
            ),
            catalog,
        )
    forged = with_version_state(
        report(keys, "Gateway 2.3", cves=CVE_A, status="unknown"), "supported"
    )
    with pytest.raises(EvidenceError):
        validate_finding_evidence(forged, catalog)


def test_unowned_introductory_range_cannot_become_absence_after_cvss_classification():
    catalog = build_reporting_catalog(
        [
            source(
                "Every release from 1.0.0 through 1.12.8 has the flaws.\n\n"
                f"{CVE_A} CVSS score: 9.8.\n\n{CVE_B} CVSS score: 8.8."
            )
        ]
    )
    assert_scope_rejected(catalog, scope_for(catalog))
    assert scope_for(catalog, (CVE_B,))["state"] == "blocked"


@pytest.mark.parametrize("layout", ["paragraph", "heading"])
def test_joint_range_is_not_discarded_for_one_of_its_cves(layout):
    intro = f"{CVE_A} and {CVE_B} are described."
    if layout == "heading":
        intro = f"## {CVE_A} and {CVE_B}"
    catalog = build_reporting_catalog(
        [source(intro + "\n\nAffected versions: Gateway 2.3 (Windows only)")]
    )
    assert_scope_rejected(catalog, scope_for(catalog))
    joint = scope_for(catalog, (CVE_A, CVE_B))
    assert joint["state"] == "supported"
    assert [c["text"] for c in joint["constraints"]] == ["Gateway 2.3 (Windows only)"]


@pytest.mark.parametrize(
    "pending",
    [
        "Affected versions: Gateway 9.0",
        "Only Windows installations are impacted.",
        "This applies only when remote administration is enabled.",
    ],
)
def test_unaccounted_peer_context_blocks_an_otherwise_supported_scope(pending):
    catalog = build_reporting_catalog(
        [
            source(f"{CVE_A} is described.\n\nAffected versions: Gateway 2.3"),
            source(
                f"{CVE_A} CVSS score: 9.8.\n\n{CVE_B} CVSS score: 8.8.\n\n" + pending,
                "peer",
            ),
        ]
    )
    scope = scope_for(catalog)
    assert [c["text"] for c in scope["constraints"]] == ["Gateway 2.3"]
    assert_scope_rejected(catalog, scope, [next(iter(catalog))])


@pytest.mark.parametrize(
    "tail",
    [
        f"{CVE_B} affects Gateway 3.2; Gateway 7.0 is affected.",
        f"Unlike {CVE_B}, Gateway 7.0 is affected.",
        f"{CVE_B} affects Gateway 3.2. Only Windows installations are impacted.",
        f"{CVE_B} affects Gateway 3.2\nOnly Windows installations are impacted.",
        f"{CVE_B} affects Gateway 3.2 (Windows only).",
    ],
)
def test_foreign_cve_mention_or_prefix_cannot_hide_unowned_range_context(tail):
    catalog = build_reporting_catalog([source(f"{CVE_A} is described.\n\n" + tail)])
    assert_scope_rejected(catalog, scope_for(catalog))


@pytest.mark.parametrize(
    "content",
    [
        f"## {CVE_A}\n\n{CVE_B} affects Gateway 3.2.",
        f"## {CVE_B}\n\nAffected versions: Gateway 3.2 (for {CVE_A})",
    ],
)
def test_conflicting_section_and_sentence_attribution_remains_unaccounted(content):
    catalog = build_reporting_catalog([source(content)])
    assert_scope_rejected(catalog, scope_for(catalog))


def test_unowned_affected_version_heading_without_digits_cannot_authorize_absence():
    catalog = build_reporting_catalog(
        [
            source(
                f"{CVE_A} is described.\n\n{CVE_B} is described.\n\n## Affected Versions"
            )
        ]
    )
    assert_scope_rejected(catalog, scope_for(catalog))


@pytest.mark.parametrize(
    "heading",
    [
        "Gateway 7.0 or earlier is affected",
        "Versions before 7.0",
        "Gateway 7 is affected",
    ],
)
def test_unowned_version_assertion_heading_blocks_without_supplying_a_fact(heading):
    catalog = build_reporting_catalog(
        [source(f"{CVE_A} is described.\n\n{CVE_B} is described.\n\n## {heading}")]
    )
    scope = scope_for(catalog)
    assert scope["constraints"] == []
    assert scope["unresolved_references"] == []
    assert_scope_rejected(catalog, scope)


@pytest.mark.parametrize("heading", ["Fixed in Gateway 7", "CVSS score: 9.8"])
def test_unowned_non_affected_heading_keeps_its_existing_role(heading):
    catalog = build_reporting_catalog(
        [source(f"{CVE_A} is described.\n\n{CVE_B} is described.\n\n## {heading}")]
    )
    scope = scope_for(catalog)
    assert scope["state"] == "not_stated"
    assert scope["constraints"] == []
    assert scope["unresolved_references"] == []


@pytest.mark.parametrize("cache_kind", ["empty", "omitted_peer", "omitted_group"])
def test_detail_context_cache_cannot_reduce_authoritative_catalog_scope(cache_kind):
    catalog = build_reporting_catalog(
        [
            source(f"{CVE_A} is described."),
            source(f"{CVE_A} is described.\n\nAffected versions: Gateway 2.3", "peer"),
            source(f"{CVE_B} is described.", "other"),
        ]
    )
    first = next(iter(catalog))
    cache = [] if cache_kind == "empty" else [{"source_key": first, "cves": [CVE_A]}]
    if cache_kind == "omitted_group":
        cache = [{"source_key": list(catalog)[-1], "cves": [CVE_B]}]
    assert build_version_reference_context(
        catalog, cache
    ) == build_version_reference_context(catalog)


@pytest.mark.parametrize(
    "control",
    [
        f"A patch was released on October 21.\n\n{CVE_B} affects Gateway 9.0.",
        f"Fixed in Gateway 7.\n\n{CVE_B} affects Gateway 9.0.",
        f"CVSS score: 9.8.\n\n{CVE_B} affects Gateway 9.0.",
        f"## {CVE_B}\n\nAffected versions: Gateway 9.0",
    ],
)
def test_proven_foreign_scope_and_non_affected_controls_keep_absence(control):
    catalog = build_reporting_catalog([source(f"{CVE_A} is described.\n\n" + control)])
    scope = scope_for(catalog)
    assert scope["state"] == "not_stated"
    assert scope["constraints"] == []
    assert scope["absence_allowed"]

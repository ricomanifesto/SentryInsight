"""Complete version predicates need explicit subject ownership."""

import pytest

from src.core.reporting import build_reporting_catalog
from test_source_table_ownership import article_table, catalog_from_html
from test_version_references import CVE, contract, source


@pytest.mark.parametrize("where", ["section", "table"])
@pytest.mark.parametrize(
    "statement,constraint",
    [
        ("Versions before 1.3.0 are affected.", "Versions before 1.3.0"),
        (
            "Versions before 1.3.0 (Windows only) are still affected.",
            "Versions before 1.3.0 (Windows only)",
        ),
        (
            "Versions before 1.3.0 are affected, and 1.3.0 is the fixed version (release notes).",
            "Versions before 1.3.0",
        ),
        (
            "Versions before 1.3.0 are affected, and 1.3.0 is the fixed version ( release notes ).",
            "Versions before 1.3.0",
        ),
        ("NVD lists 0.24.0 and earlier as affected.", "0.24.0 and earlier"),
    ],
)
def test_an_explicit_subject_keeps_the_complete_affected_constraint(
    where, statement, constraint
):
    if where == "table":
        _, catalog = catalog_from_html(
            article_table([["Gateway", f"{CVE}, missing authentication.", statement]])
        )
    else:
        catalog = build_reporting_catalog([source(f"## {CVE}\n\n{statement}")])
    item = contract(catalog)
    assert item["blocked"] is False
    assert [row["text"] for row in item["constraints"]] == [constraint]


def test_direct_predicates_do_not_gain_whole_source_cve_ownership():
    catalog = build_reporting_catalog(
        [
            source(
                f"{CVE} is described.\n\nAn agent extension has a separate flaw without an assigned identifier.\n\nVersions before 7.1 are affected."
            )
        ]
    )
    assert contract(catalog)["blocked"] is True


@pytest.mark.parametrize(
    "statement",
    [
        "Versions before 1.3.0 are affected on Windows only.",
        "Versions before 1.3.0 are affected, but hosted deployments cannot be ruled out.",
        "Versions before 1.3.0 may be affected.",
        "Versions before 1.3.0 are not unaffected.",
        "Versions before 1.3.0 are affected; another unknown clause applies.",
    ],
)
def test_unconsumed_or_uncertain_clauses_remain_blocked(statement):
    _, catalog = catalog_from_html(article_table([["Gateway", CVE, statement]]))
    assert contract(catalog)["blocked"] is True


def test_a_fixed_release_alone_still_does_not_establish_an_affected_range():
    _, catalog = catalog_from_html(
        article_table([["Gateway", CVE, "1.3.0 is the fixed version (release notes)."]])
    )
    item = contract(catalog)
    assert item["blocked"] is False
    assert item["constraints"] == []
    assert item["absence_allowed"] is True


def test_a_later_uncertain_release_is_not_discarded_after_a_known_range():
    _, catalog = catalog_from_html(
        article_table(
            [
                [
                    "Gateway",
                    CVE,
                    "Versions before 1.3.0 are affected. Whether 1.4.0 is affected cannot be ruled out.",
                ]
            ]
        )
    )
    assert contract(catalog)["blocked"] is True


@pytest.mark.parametrize(
    "detail",
    [
        "Affected versions: Gateway 2.0; Versions before 7.1 are affected.",
        "Affected versions: Gateway 2.0; NVD lists 7.1 and earlier as affected.",
        "Affected versions:\nGateway 2.0, and NVD lists 7.1 and earlier as affected.",
    ],
)
def test_a_legacy_list_cue_cannot_bypass_direct_clause_ownership(detail):
    catalog = build_reporting_catalog([source(f"{CVE} is described.\n\n{detail}")])
    assert contract(catalog)["blocked"] is True


def test_a_complete_predicate_does_not_open_a_list_of_following_dates():
    _, catalog = catalog_from_html(
        article_table(
            [
                [
                    "Gateway",
                    CVE,
                    "Versions before 1.3.0 are affected. The agency added the flaw to its catalog on May 5, 2025.",
                ]
            ]
        )
    )
    item = contract(catalog)
    assert item["blocked"] is False
    assert [row["text"] for row in item["constraints"]] == ["Versions before 1.3.0"]


@pytest.mark.parametrize(
    "qualifier",
    [
        "Windows only.",
        "Only self-hosted installations.",
        "When module X is enabled.",
        "Whether later releases are affected is unknown.",
    ],
)
@pytest.mark.parametrize("separator", [" ", "</p><p>"])
def test_following_qualifications_are_not_erased_for_lack_of_digits(
    qualifier, separator
):
    statement = (
        "<p>Versions before 1.3.0 are affected." + separator + qualifier + "</p>"
    )
    _, catalog = catalog_from_html(article_table([["Gateway", CVE, statement]]))
    assert contract(catalog)["blocked"] is True


def test_a_later_constraints_matching_words_do_not_retain_an_earlier_qualifier():
    _, catalog = catalog_from_html(
        article_table(
            [
                [
                    "Gateway",
                    CVE,
                    "Versions before 1.3.0 are affected. Windows only. Affected versions: Gateway 3.0 (Windows only).",
                ]
            ]
        )
    )
    assert contract(catalog)["blocked"] is True


@pytest.mark.parametrize("qualifier", ["Restricted to ARM64.", "Limited to x86."])
@pytest.mark.parametrize("separator", [" ", "</p><p>"])
def test_digits_in_a_qualifier_do_not_make_it_independent_narrative(
    qualifier, separator
):
    _, catalog = catalog_from_html(
        article_table(
            [
                [
                    "Gateway",
                    CVE,
                    "<p>Versions before 1.3.0 are affected."
                    + separator
                    + qualifier
                    + "</p>",
                ]
            ]
        )
    )
    assert contract(catalog)["blocked"] is True


def test_a_dangling_range_fragment_after_a_complete_predicate_remains_unresolved():
    _, catalog = catalog_from_html(
        article_table([["Gateway", CVE, "Versions 2.0 are affected.\nand earlier"]])
    )
    assert contract(catalog)["blocked"] is True

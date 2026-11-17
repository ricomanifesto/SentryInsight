"""A source table owns rows and cells without assigning neighboring evidence."""

import pytest

from src.core.article_prompt import canonical_source_article, format_article_summary
from src.core.finding_evidence import (
    _partition_detail_spans,
    build_finding_detail_context,
)
from src.core.reporting import (
    build_reporting_catalog,
    deserialize_reporting_catalog,
    serialize_reporting_catalog,
)
from src.services.article_content import extract_article_content, normalize_feed_content
from test_version_references import CVE, OTHER, contract, source


def article_table(rows, *, prefix="", suffix="", headers=None):
    headers = headers or ["Product", "Flaw", "Status"]
    return (
        "<article>"
        + prefix
        + "<table><tr>"
        + "".join(f"<th>{name}</th>" for name in headers)
        + "</tr>"
        + "".join(
            "<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>"
            for row in rows
        )
        + "</table>"
        + suffix
        + "</article>"
    )


def catalog_from_html(markup):
    extracted = extract_article_content(markup, "https://example.test/advisory")
    article = source(extracted.text)
    article["source_links"] = list(extracted.links)
    return extracted, build_reporting_catalog([article])


def scope_texts(catalog, cves):
    [retained] = catalog.values()
    return [
        span.text
        for span in _partition_detail_spans(retained, cves).scoped
        if span.role == "body"
    ]


def test_each_cve_row_keeps_its_complete_cell_local_evidence():
    _, catalog = catalog_from_html(
        article_table(
            [
                [
                    "Gateway",
                    f"{CVE}, missing authentication.",
                    "<p>Affected versions: Gateway before 1.3.0</p><p>Users should upgrade only after backing up.</p>",
                ],
                [
                    "Console",
                    f"{OTHER}, template injection.",
                    "<p>Affected versions: Console 4.0 and earlier</p><p>No patched version is listed.</p>",
                ],
            ]
        )
    )
    first, second = scope_texts(catalog, [CVE]), scope_texts(catalog, [OTHER])
    assert "Affected versions: Gateway before 1.3.0" in first
    assert "Users should upgrade only after backing up." in first
    assert not any("Console 4.0" in text for text in first)
    assert "Affected versions: Console 4.0 and earlier" in second
    assert "No patched version is listed." in second
    assert not any("Gateway before" in text for text in second)


def test_a_separate_row_without_a_cve_cannot_supply_another_rows_range():
    _, catalog = catalog_from_html(
        article_table(
            [
                [
                    "Gateway",
                    f"{CVE}, missing authentication.",
                    "Affected versions: Gateway before 1.3.0",
                ],
                [
                    "Agent extension",
                    "Authentication bypass without an assigned identifier.",
                    "Affected versions: Agent extension before 7.1",
                ],
            ]
        )
    )
    item = contract(catalog)
    assert item["blocked"] is False
    assert [entry["text"] for entry in item["constraints"]] == ["Gateway before 1.3.0"]


def test_a_row_boundary_ends_the_previous_cells_version_list():
    _, catalog = catalog_from_html(
        article_table(
            [
                [
                    "Gateway",
                    f"{CVE}, missing authentication.",
                    "Affected versions: Gateway 2.0",
                ],
                [
                    "Agent extension",
                    "A separate authentication bypass.",
                    "Agent extension 7.1",
                ],
            ]
        )
    )
    item = contract(catalog)
    assert item["blocked"] is False
    assert [entry["text"] for entry in item["constraints"]] == ["Gateway 2.0"]


def test_background_ids_in_status_do_not_manufacture_a_joint_row_scope():
    _, catalog = catalog_from_html(
        article_table(
            [
                [
                    "Gateway",
                    f"{CVE}, missing authentication.",
                    f"Affected versions: Gateway 2.0. Background comparison with {OTHER} affects Console 7.1.",
                ],
            ]
        )
    )
    scopes = [item["cves"] for item in build_finding_detail_context(catalog)]
    assert [CVE, OTHER] not in scopes
    assert contract(catalog)["blocked"] is True


@pytest.mark.parametrize(
    "layout",
    ["merged", "nested", "duplicate_header", "missing_identity", "malformed_identity"],
)
def test_unsupported_table_structure_retains_evidence_without_certifying_scope(layout):
    identity = f"{CVE}, missing authentication."
    markup = article_table(
        [["Gateway", identity, "Affected versions: Gateway 2.0"]],
        prefix=f"<p>{CVE} is described.</p>",
    )
    if layout == "merged":
        markup = markup.replace("<td>Gateway</td>", '<td rowspan="2">Gateway</td>')
    elif layout == "nested":
        markup = markup.replace(
            "Gateway 2.0", "<table><tr><td>Gateway 2.0</td></tr></table>"
        )
    elif layout == "duplicate_header":
        markup = markup.replace("<th>Status</th>", "<th>Flaw</th>")
    elif layout == "missing_identity":
        markup = markup.replace(identity, "")
    else:
        markup = markup.replace(
            identity, f"{CVE} and CVE-2026-12, missing authentication."
        )
    extracted, catalog = catalog_from_html(markup)
    assert "Gateway 2.0" in extracted.text
    assert contract(catalog)["blocked"] is True


def test_table_scope_does_not_leak_into_following_section_owned_prose():
    _, catalog = catalog_from_html(
        article_table(
            [
                [
                    "Console",
                    f"{OTHER}, template injection.",
                    "Affected versions: Console 4.0",
                ]
            ],
            prefix=f"<h2>{CVE}</h2><p>{CVE} is described.</p>",
            suffix="<p>Users of Gateway 2.1 are not affected.</p>",
        )
    )
    assert "Users of Gateway 2.1 are not affected." in scope_texts(catalog, [CVE])
    assert "Users of Gateway 2.1 are not affected." not in scope_texts(catalog, [OTHER])


def test_structural_content_round_trip_preserves_literals_links_and_qualifiers():
    phrase = "Gateway &lt;2.0 | `preview`"
    markup = article_table(
        [
            [
                "Gateway",
                f"{CVE}, missing authentication.",
                f'<p>{phrase}</p><ul><li>Windows only<ul><li>Exclude hosted deployments.</li></ul></li></ul><a href="/release">Release notes</a>',
            ]
        ]
    )
    extracted, catalog = catalog_from_html(markup)
    [retained] = catalog.values()
    assert normalize_feed_content(extracted.text) == extracted.text
    restored = deserialize_reporting_catalog(serialize_reporting_catalog(catalog))
    assert restored == catalog
    canonical = canonical_source_article(retained, [CVE])
    assert canonical["content"] == extracted.text
    assert extracted.text in format_article_summary(canonical)
    texts = "\n".join(scope_texts(catalog, [CVE]))
    assert "Gateway <2.0 | `preview`" in texts
    assert "Windows only" in texts and "Exclude hosted deployments." in texts
    assert retained.links == ("https://example.test/release",)


@pytest.mark.parametrize(
    "identity",
    [
        "Same vulnerability",
        "See above",
        "Authentication bypass, the same flaw as above",
    ],
)
def test_referential_identity_cannot_prove_a_row_is_a_separate_issue(identity):
    _, catalog = catalog_from_html(
        article_table(
            [
                [
                    "Gateway",
                    f"{CVE}, missing authentication.",
                    "Affected versions: Gateway 2.0",
                ],
                ["Agent extension", identity, "Affected versions: Agent extension 7.1"],
            ]
        )
    )
    assert contract(catalog)["blocked"] is True


def canonical_table():
    return (
        "```retained-table-v1\n"
        "| Product | Flaw | Status |\n"
        "| --- | --- | --- |\n"
        f"| Gateway | {CVE}, missing authentication. | Affected versions: Gateway 2.0 |\n"
        "```"
    )


def test_normalization_preserves_a_table_but_normalizes_html_outside_it():
    value = (
        "<p>Before &amp; context.</p>\n\n"
        + canonical_table()
        + "\n\n<p>After &lt;2.0 stays literal.</p>"
    )
    normalized = normalize_feed_content(value)
    assert (
        normalized
        == "Before & context.\n\n" + canonical_table() + "\n\nAfter <2.0 stays literal."
    )
    assert normalize_feed_content(normalized) == normalized


@pytest.mark.parametrize("mutation", ["unclosed", "unequal_cells", "bad_entity"])
def test_malformed_carrier_retains_its_version_evidence_without_ownership(mutation):
    content = canonical_table()
    if mutation == "unclosed":
        content = content.removesuffix("```")
    elif mutation == "unequal_cells":
        content = content.replace("Gateway 2.0 |", "Gateway 2.0 | extra |")
    else:
        content = content.replace("Gateway 2.0", "Gateway &lt;2.0")
    retained = normalize_feed_content(content)
    assert CVE in retained and "2.0" in retained
    assert contract(build_reporting_catalog([source(retained)]))["blocked"] is True


def test_table_decodes_entities_once_without_recursively_parsing_cell_syntax():
    literal = "literal &amp;#124; &amp;#10; &amp;amp; `code` ```retained-table-v1"
    _, catalog = catalog_from_html(
        article_table(
            [
                ["Gateway", f"{CVE}, missing authentication.", literal],
            ]
        )
    )
    text = "\n".join(scope_texts(catalog, [CVE]))
    assert "literal &#124; &#10; &amp; `code` ```retained-table-v1" in text


def test_an_unrecognized_header_row_is_not_dropped_from_opaque_evidence():
    _, catalog = catalog_from_html(
        article_table(
            [["Note", "No further details", "No further details"]],
            headers=["Unrecognized", CVE, "Affected versions: Gateway 2.0"],
        )
    )
    assert contract(catalog)["blocked"] is True


def test_a_no_cve_table_cannot_certify_absence_for_a_generic_finding():
    _, catalog = catalog_from_html(
        article_table(
            [
                [
                    "Gateway",
                    "Authentication bypass without an assigned identifier.",
                    "Affected versions: Gateway 2.0",
                ],
            ]
        )
    )
    assert contract(catalog, cves=())["blocked"] is True


def test_a_whole_recommendation_cannot_be_cut_at_a_foreign_cve_sentence():
    from src.core.finding_evidence import EvidenceError

    _, catalog = catalog_from_html(
        article_table(
            [
                [
                    "Gateway",
                    f"{CVE}, missing authentication.",
                    f"Users should install the update. This action also addresses {OTHER}.",
                ],
            ]
        )
    )
    with pytest.raises(EvidenceError, match="recommendation"):
        scope_texts(catalog, [CVE])


def test_different_versions_does_not_assert_a_separate_vulnerability():
    _, catalog = catalog_from_html(
        article_table(
            [
                [
                    "Gateway",
                    f"{CVE}, missing authentication.",
                    "Affected versions: Gateway 2.0",
                ],
                ["Gateway", "Different versions", "Affected versions: Gateway 3.0"],
            ]
        )
    )
    assert contract(catalog)["blocked"] is True


@pytest.mark.parametrize(
    "opening", ["    ```retained-table-v1", "```retained-table-v1 unknown"]
)
def test_malformed_opening_cannot_hide_its_own_version_evidence(opening):
    content = opening + f" {CVE} Affected versions: Gateway 2.0\n```"
    catalog = build_reporting_catalog([source(content)])
    assert contract(catalog)["blocked"] is True


@pytest.mark.parametrize(
    "literal",
    [
        "&#124;",
        "&#10;",
        "&amp;",
        "|",
        "`\n```",
        "<2.0",
        "a\r\nb",
        "a\u2028b",
        "a\u2029b",
    ],
)
def test_cell_codec_preserves_literal_content_without_recursive_interpretation(literal):
    from src.services.source_tables import render_source_table, source_tables

    rows = [("Product", "Flaw", "Status"), ("Gateway", CVE, literal)]
    rendered = render_source_table(rows, opaque=False)
    [table] = source_tables(rendered)
    assert table.opaque is False
    assert table.rows == tuple(rows)
    assert normalize_feed_content(rendered) == rendered


def test_a_foreign_heading_in_a_status_cell_cannot_reassign_its_following_range():
    _, catalog = catalog_from_html(
        article_table(
            [
                [
                    "Gateway",
                    CVE,
                    f"<h3>{OTHER}</h3><p>Affected versions: Console 7.1</p>",
                ],
            ]
        )
    )
    assert contract(catalog)["blocked"] is True
    assert contract(catalog, cves=(OTHER,))["blocked"] is True


def test_a_joint_identity_cell_retains_a_real_shared_scope():
    _, catalog = catalog_from_html(
        article_table(
            [
                [
                    "Gateway",
                    f"{CVE} and {OTHER}, a shared exploit chain.",
                    "Affected versions: Gateway 2.0",
                ],
            ]
        )
    )
    item = contract(catalog, cves=(CVE, OTHER))
    assert item["blocked"] is False
    assert [row["text"] for row in item["constraints"]] == ["Gateway 2.0"]


@pytest.mark.parametrize(
    "identity",
    [
        "Authentication bypass described in the first row",
        "Authentication bypass in the earlier entry",
    ],
)
def test_a_flaw_description_cannot_hide_an_unconsumed_reference(identity):
    _, catalog = catalog_from_html(
        article_table(
            [
                ["Gateway", CVE, "Affected versions: Gateway 2.0"],
                ["Agent extension", identity, "Affected versions: Agent extension 7.1"],
            ]
        )
    )
    assert contract(catalog)["blocked"] is True


def test_an_identifier_free_row_cannot_override_an_enclosing_cve_section():
    _, catalog = catalog_from_html(
        article_table(
            [
                [
                    "Gateway",
                    "A separate authentication bypass.",
                    "Affected versions: Gateway 2.0",
                ]
            ],
            prefix=f"<h2>{CVE}</h2>",
        )
    )
    assert contract(catalog)["blocked"] is True


@pytest.mark.parametrize(
    "kind", ["related", "related-posts", "social", "newsletter", "advertisement"]
)
@pytest.mark.parametrize("tag", ["tr", "tbody"])
def test_table_collection_keeps_existing_unrelated_content_exclusions(kind, tag):
    promotional = f'<tr><td>Promotion</td><td>{OTHER}</td><td>Affected versions: Promotion 7.1 <a href="/promotion">More</a></td></tr>'
    if tag == "tr":
        promotional = promotional.replace("<tr>", f'<tr class="{kind}">')
    else:
        promotional = f'<tbody class="{kind}">{promotional}</tbody>'
    markup = f"<article><table><thead><tr><th>Product</th><th>Flaw</th><th>Status</th></tr></thead><tbody><tr><td>Gateway</td><td>{CVE}</td><td>Affected versions: Gateway 2.0</td></tr></tbody>{promotional}</table></article>"
    extracted, _ = catalog_from_html(markup)
    assert "Promotion" not in extracted.text
    assert OTHER not in extracted.text
    assert "https://example.test/promotion" not in extracted.links


@pytest.mark.parametrize(
    "row", [["Gateway", CVE, ""], ["Gateway", "", "Affected versions: Gateway 2.0"]]
)
def test_empty_cells_keep_the_canonical_column_layout(row):
    from src.services.source_tables import source_tables

    extracted, _ = catalog_from_html(article_table([row]))
    [table] = source_tables(extracted.text)
    assert table.opaque is False
    assert table.rows[1] == tuple(row)


def test_an_entirely_excluded_table_cannot_poison_surrounding_evidence():
    markup = f'<article><p>{CVE} is described.</p><p>Affected versions: Gateway 2.0</p><table><tr class="related"><td>Promotion</td><td>{OTHER}</td></tr></table></article>'
    extracted, catalog = catalog_from_html(markup)
    assert "retained-table" not in extracted.text
    assert contract(catalog)["blocked"] is False

"""Source quarantine is an explicit input boundary, never a claim repair."""

import copy
import json

import pytest

from src.core.source_review import (
    SourceReviewError,
    prepare_source_review,
    validate_review_packet,
    write_review_packet,
)
from test_version_references import source
from test_unresolved_versions import NARRATIVE

A = "CVE-2026-1234"
B = "CVE-2026-5678"
AMBIGUOUS = "An attack vector targets instances running version 3.2 or earlier."


def by_url(plan):
    return {row["url"].rsplit("/", 1)[-1]: row for row in plan.packet["sources"]}


def test_all_inputs_have_a_disposition_without_promoting_ambiguous_versions():
    plan = prepare_source_review(
        [source("A service advisory.", "ready"), source(AMBIGUOUS, "held")]
    )
    rows = by_url(plan)
    assert rows["ready"]["state"] == "eligible"
    assert rows["held"]["state"] == "review_required"
    assert plan.eligible_keys == (rows["ready"]["key"],)
    assert len(plan.catalog) == 2
    assert set(plan.eligible_catalog) == set(plan.eligible_keys)
    serialized = json.dumps(plan.packet)
    assert AMBIGUOUS not in serialized
    assert "version_reference" not in serialized
    assert validate_review_packet(plan.packet) == plan.packet


@pytest.mark.parametrize(
    "content,reason",
    [
        ("Affected versions:", "empty_version_list"),
        (
            "Affected versions: Gateway 7\n\n"
            "Affected versions: users of Gateway 7 are not affected",
            "contradictory_version_constraints",
        ),
    ],
)
def test_hard_source_failures_remain_rejected_not_review_eligible(content, reason):
    plan = prepare_source_review([source(content, "bad"), source("An advisory.", "ok")])
    bad = by_url(plan)["bad"]
    assert bad["state"] == bad["direct_state"] == "source_rejected"
    assert reason in bad["reason_codes"]
    assert bad["key"] not in plan.eligible_catalog


def test_existing_unresolved_source_is_held_without_expanding_its_claim_contract():
    plan = prepare_source_review([source(NARRATIVE)])
    [row] = plan.packet["sources"]
    assert row["state"] == "review_required"
    assert "unresolved_version_evidence" in row["reason_codes"]
    assert not plan.eligible_keys


@pytest.mark.parametrize(
    "identity_place", ["content", "title", "source", "link", "source_links", "cves"]
)
def test_cohort_closure_includes_every_prompt_visible_cve_identity(identity_place):
    held = source(f"{A} is described.\n\n" + AMBIGUOUS, "held")
    peer = source("A service advisory.", "peer")
    if identity_place == "source_links":
        peer[identity_place] = [f"https://vendor.example/{A}"]
    elif identity_place == "cves":
        peer[identity_place] = [A]
    elif identity_place == "link":
        peer[identity_place] += "?id=" + A
    else:
        peer[identity_place] += " " + A
    plan = prepare_source_review([held, peer])
    rows = plan.packet["sources"]
    held_row = next(row for row in rows if row["url"].endswith("/held"))
    peer_row = next(row for row in rows if row != held_row)
    assert peer_row["state"] == "review_required"
    assert held_row["key"] in peer_row["origin_keys"]
    assert not plan.eligible_keys


def test_cohort_closure_is_transitive_and_preserves_independent_evidence():
    plan = prepare_source_review(
        [
            source(f"{A} is described.\n\n{AMBIGUOUS}", "held"),
            source(f"{A} and {B} are described.", "bridge"),
            source(f"{B} is described.", "peer"),
            source("An independent advisory.", "independent"),
        ]
    )
    rows = by_url(plan)
    assert {rows[k]["state"] for k in ("held", "bridge", "peer")} == {"review_required"}
    assert rows["independent"]["state"] == "eligible"
    assert len(plan.eligible_keys) == 1


@pytest.mark.parametrize(
    "field", ["title", "source", "link", "source_links", "cves", "content_kind"]
)
def test_plan_fingerprint_binds_metadata_even_when_body_is_unchanged(field):
    article = source("An independent advisory.")
    first = prepare_source_review([article]).packet["plan_id"]
    changed = copy.deepcopy(article)
    changed[field] = {
        "title": "Changed title",
        "source": "Changed publisher",
        "link": "https://example.test/changed",
        "source_links": ["https://vendor.example/advisory"],
        "cves": [A],
        "content_kind": "feed",
    }[field]
    assert prepare_source_review([changed]).packet["plan_id"] != first


@pytest.mark.parametrize(
    "mutate",
    [
        lambda a: a.update(link="javascript:alert(1)"),
        lambda a: a.update(cves=["CVE-2026-12"]),
        lambda a: a.update(content_kind="unknown"),
        lambda a: a.update(content=""),
        lambda a: a.update(content=" \n\t "),
        lambda a: a.update(content=None),
        lambda a: a.pop("content"),
    ],
)
def test_invalid_input_is_a_whole_plan_failure_not_an_omitted_source(mutate):
    bad = source("An advisory.", "bad")
    mutate(bad)
    with pytest.raises(SourceReviewError):
        prepare_source_review([source("Good advisory.", "good"), bad])


def test_conflicting_duplicate_metadata_fails_instead_of_overwriting_a_source():
    first = source("An advisory.")
    second = {**first, "cves": [A]}
    with pytest.raises(SourceReviewError):
        prepare_source_review([first, second])


def test_structured_identifiers_are_normalized_before_fingerprinting():
    article = source("An advisory.")
    assert (
        prepare_source_review([{**article, "cves": [" cve-2026-1234 ", A]}]).packet
        == prepare_source_review([{**article, "cves": [A]}]).packet
    )


def test_packet_is_immutable_idempotent_and_contains_metadata_only(tmp_path):
    packet = prepare_source_review([source(AMBIGUOUS)]).packet
    path = write_review_packet(packet, tmp_path)
    before = path.read_bytes()
    assert write_review_packet(packet, tmp_path) == path
    assert path.read_bytes() == before
    assert path.name == packet["plan_id"] + ".json"
    assert path.stat().st_mode & 0o777 == 0o600
    assert AMBIGUOUS not in path.read_text()
    path.write_text("{}")
    with pytest.raises(SourceReviewError):
        write_review_packet(packet, tmp_path)
    assert path.read_text() == "{}"


def test_forged_packet_cannot_be_persisted(tmp_path):
    packet = copy.deepcopy(prepare_source_review([source(AMBIGUOUS)]).packet)
    packet["sources"][0]["state"] = "eligible"
    with pytest.raises(SourceReviewError):
        write_review_packet(packet, tmp_path)
    assert not list(tmp_path.iterdir())


@pytest.mark.parametrize("mode", [0o644, 0o666])
@pytest.mark.parametrize("race", [False, True])
def test_existing_packet_permissions_are_checked_on_both_creation_paths(
    tmp_path, monkeypatch, mode, race
):
    packet = prepare_source_review([source(AMBIGUOUS)]).packet
    path = write_review_packet(packet, tmp_path)
    path.chmod(mode)
    if race:
        original = type(path).exists
        monkeypatch.setattr(
            type(path),
            "exists",
            lambda current: False if current == path else original(current),
        )
    with pytest.raises(SourceReviewError, match="review_packet_permissions_invalid"):
        write_review_packet(packet, tmp_path)
    assert path.stat().st_mode & 0o777 == mode
    assert json.loads(path.read_text()) == packet


def test_input_order_does_not_change_the_canonical_plan():
    articles = [source(AMBIGUOUS, "held"), source("Advisory.", "ready")]
    assert (
        prepare_source_review(articles).packet
        == prepare_source_review(articles[::-1]).packet
    )


def test_plan_fingerprint_includes_non_version_finding_assessments(monkeypatch):
    from src.core import source_review

    articles = [source(f"{A} is actively exploited.")]
    before = prepare_source_review(articles).packet["plan_id"]
    original = source_review.build_finding_detail_context

    def changed(catalog):
        context = original(catalog)
        for item in context:
            item["exploitation"]["status"] = "unknown"
        return context

    monkeypatch.setattr(source_review, "build_finding_detail_context", changed)
    assert prepare_source_review(articles).packet["plan_id"] != before


@pytest.mark.parametrize(
    "articles", [None, "source", {"content": "text"}, [None], ["source"]]
)
def test_invalid_input_container_has_a_fixed_failure_code(articles):
    with pytest.raises(SourceReviewError, match="invalid_review_input_catalog"):
        prepare_source_review(articles)


def test_reused_packet_directory_is_synced_before_success(tmp_path, monkeypatch):
    import os
    import stat
    from src.core import source_review

    plan = prepare_source_review([source("An advisory.")])
    source_review.write_review_packet(plan.packet, tmp_path)
    original = os.fsync

    def fail_directory(fd):
        if stat.S_ISDIR(os.fstat(fd).st_mode):
            raise OSError("directory sync failure")
        return original(fd)

    monkeypatch.setattr(source_review.os, "fsync", fail_directory)
    with pytest.raises(SourceReviewError, match="review_packet_persistence_failed"):
        source_review.write_review_packet(plan.packet, tmp_path)


@pytest.mark.parametrize(
    "title",
    [
        "Advisory for CVE-**2026**-1234",
        "<div>CVE-**2026**-1234</div>",
        "Advisory for CVE&#45;2026&#45;1234",
        r"Advisory for CVE\-2026\-1234",
    ],
)
@pytest.mark.parametrize("field", ["title", "source", "content"])
def test_reader_visible_cve_in_held_source_metadata_closes_the_cohort(title, field):
    held = source(AMBIGUOUS, "held")
    held[field] = title + ("\n\n" + AMBIGUOUS if field == "content" else "")
    plan = prepare_source_review(
        [source("CVE-2026-1234 is actively exploited.", "peer"), held]
    )
    assert plan.eligible_keys == ()
    assert all(row["cves"] == ["CVE-2026-1234"] for row in plan.packet["sources"])
    assert all(row["state"] == "review_required" for row in plan.packet["sources"])


def test_separate_source_metadata_fields_do_not_invent_cve_membership():
    article = source("A service mentions CVE", "one")
    article["title"] = "2026-1234 advisory"
    plan = prepare_source_review([article])
    assert plan.packet["sources"][0]["cves"] == []


def test_separate_markdown_blocks_do_not_invent_cve_membership():
    article = source("CVE-\n\n2026-1234", "one")
    plan = prepare_source_review([article])
    assert plan.packet["sources"][0]["cves"] == []


@pytest.mark.parametrize("field", ["title", "source", "content"])
@pytest.mark.parametrize("definition_source", ["held", "separate"])
@pytest.mark.parametrize(
    "identifier,label",
    [
        ("CVE-[2026][ref]-1234", "ref"),
        ("CVE-[2026][]-1234", "2026"),
        ("CVE-[2026]-1234", "2026"),
        ("CVE-[2026][ReF  Name]-1234", "ref name"),
    ],
)
def test_reference_context_closes_cve_cohorts(
    field, definition_source, identifier, label
):
    held = source(AMBIGUOUS, "held")
    held[field] = identifier + ("\n\n" + AMBIGUOUS if field == "content" else "")
    separate = source("A separate advisory.", "separate")
    provider = held if definition_source == "held" else separate
    provider["content"] += f"\n\n[{label}]: https://example.test/reference"
    plan = prepare_source_review(
        [source(f"{A} is actively exploited.", "peer"), held, separate]
    )
    rows = by_url(plan)
    assert A in rows["held"]["cves"]
    assert rows["held"]["state"] == rows["peer"]["state"] == "review_required"
    assert plan.eligible_keys == (rows["separate"]["key"],)


def test_removing_a_reference_provider_cannot_change_an_eligible_source_identity():
    held = source(AMBIGUOUS + "\n\n[ref]: https://example.test/reference", "held")
    peer = source("A service advisory.", "peer")
    peer["title"] = "CVE-[2026][ref]-1234"
    with pytest.raises(SourceReviewError, match="review_selection_changed_evidence"):
        prepare_source_review([peer, held])


@pytest.mark.parametrize(
    "definition", ["", "```\n[ref]: https://example.test/reference\n```"]
)
def test_missing_or_code_only_reference_definition_does_not_invent_a_cve(definition):
    held = source(AMBIGUOUS + "\n\n" + definition, "held")
    held["title"] = "CVE-[2026][ref]-1234"
    plan = prepare_source_review([source(f"{A} is actively exploited.", "peer"), held])
    rows = by_url(plan)
    assert rows["held"]["cves"] == []
    assert plan.eligible_keys == (rows["peer"]["key"],)


def test_shared_reference_environment_preserves_first_definition_and_is_not_mutated():
    from src.core.report_validation import markdown_plain_text, markdown_references

    refs = markdown_references(
        "[ref]: https://example.test/first\n\n[ref]: https://example.test/second"
    )
    before = copy.deepcopy(refs)
    assert refs["REF"]["href"] == "https://example.test/first"
    assert (
        markdown_plain_text("CVE-[2026][ref]-1234", inline=True, references=refs) == A
    )
    markdown_plain_text(
        "[new]: https://example.test/new\n\n[ref]: https://example.test/third",
        references=refs,
    )
    assert refs == before
    assert (
        markdown_plain_text("CVE-[2026][new]-1234", inline=True, references=refs) != A
    )


def ordered_sources(*contents):
    from src.core.reporting import reporting_key

    articles = [
        source("An advisory.", f"ordered-{index}") for index in range(len(contents))
    ]
    articles.sort(key=lambda article: reporting_key(article["link"]))
    for article, content in zip(articles, contents):
        article["content"] = content
    return articles


@pytest.mark.parametrize("held_prefix", ["", "```\n\n"])
def test_unclosed_neighbor_block_cannot_hide_shared_or_isolated_reference_context(
    held_prefix,
):
    articles = ordered_sources(
        "An ordinary source.\n\n```",
        held_prefix + AMBIGUOUS + "\n\n[ref]: https://example.test/reference",
        f"{A} is actively exploited.",
    )
    articles[1]["title"] = "CVE-[2026][ref]-1234"
    plan = prepare_source_review(articles)
    rows = plan.packet["sources"]
    assert rows[1]["state"] == rows[2]["state"] == "review_required"
    assert A in rows[1]["cves"]
    assert prepare_source_review(list(reversed(articles))).packet == plan.packet


def test_removing_first_definition_is_safe_only_when_remaining_reference_preserves_identity():
    from src.core.article_prompt import format_article_summary
    from src.core.report_validation import markdown_references
    from src.core.source_review import review_articles

    articles = ordered_sources(
        AMBIGUOUS + "\n\n[ref]: https://example.test/first",
        "A service advisory.\n\n[ref]: https://example.test/second",
    )
    articles[1]["title"] = "CVE-[2026][ref]-1234"
    plan = prepare_source_review(articles)
    full = markdown_references(
        "".join(map(format_article_summary, review_articles(plan, eligible_only=False)))
    )
    selected = markdown_references(
        "".join(map(format_article_summary, review_articles(plan)))
    )
    assert full["REF"]["href"] == "https://example.test/first"
    assert selected["REF"]["href"] == "https://example.test/second"
    assert plan.packet["sources"][1]["cves"] == [A]
    assert plan.eligible_keys == (plan.packet["sources"][1]["key"],)


def test_unrelated_open_block_cannot_hide_a_reference_defined_by_another_source():
    articles = ordered_sources(
        AMBIGUOUS + "\n\n```",
        AMBIGUOUS,
        "A separate advisory.\n\n[ref]: https://example.test/reference",
        f"{A} is actively exploited.",
    )
    articles[1]["title"] = "CVE-[2026][ref]-1234"
    plan = prepare_source_review(articles)
    rows = plan.packet["sources"]
    assert rows[1]["cves"] == [A]
    assert rows[1]["state"] == rows[3]["state"] == "review_required"
    assert plan.eligible_keys == (rows[2]["key"],)

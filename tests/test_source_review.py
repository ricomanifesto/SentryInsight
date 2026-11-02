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
    "identity_place", ["content", "title", "link", "source_links", "cves"]
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

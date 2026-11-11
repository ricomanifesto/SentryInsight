"""Large valid advisories keep every evidence link within the packet byte budget."""

import copy
import json

import pytest

from src.core.exploitation_prompt import build_exploitation_prompt
from src.core.source_review import (
    MAX_PACKET_BYTES,
    SourceReviewError,
    canonical_json,
    digest,
    prepare_source_review,
    review_articles,
    validate_review_packet,
    write_review_packet,
)
from src.core.validation_diagnostics import validation_diagnostic
from test_version_references import source


def linked_article(count):
    return {
        **source("An independent service advisory."),
        "source_links": [f"https://vendor.example/advisory/{n}" for n in range(count)],
    }


@pytest.mark.parametrize("count", [512, 513, 1366])
def test_large_link_lists_are_retained_in_the_packet_prompt_and_disk(count, tmp_path):
    article = linked_article(count)
    plan = prepare_source_review([article])
    assert plan.packet["sources"][0]["links"] == article["source_links"]
    assert review_articles(plan)[0]["source_links"] == article["source_links"]
    prompt = build_exploitation_prompt(plan)
    assert "\n".join(article["source_links"]) in prompt
    path = write_review_packet(plan.packet, tmp_path)
    assert validate_review_packet(json.loads(path.read_bytes())) == plan.packet
    assert write_review_packet(plan.packet, tmp_path) == path


def test_final_link_beyond_old_limit_changes_the_plan_and_cve_cohort():
    article = linked_article(1366)
    first = prepare_source_review([article])
    changed = copy.deepcopy(article)
    changed["source_links"][-1] += "/CVE-2026-1234"
    second = prepare_source_review([changed])
    assert second.packet["plan_id"] != first.packet["plan_id"]
    assert second.packet["sources"][0]["cves"] == ["CVE-2026-1234"]
    held = source(
        "CVE-2026-1234 is described.\n\n"
        "An attack vector targets instances running version 3.2 or earlier.",
        "held",
    )
    combined = prepare_source_review([held, changed])
    assert not combined.eligible_keys
    assert {row["state"] for row in combined.packet["sources"]} == {"review_required"}
    peer = next(
        a
        for a in review_articles(combined, eligible_only=False)
        if a["link"] == article["link"]
    )
    assert peer["source_links"] == changed["source_links"]


def test_invalid_final_link_is_not_hidden_by_a_large_list():
    article = linked_article(1366)
    article["source_links"][-1] = "javascript:alert(1)"
    with pytest.raises(SourceReviewError):
        prepare_source_review([article])
    packet = prepare_source_review([linked_article(1366)]).packet
    packet["sources"][0]["links"][-1] = "javascript:alert(1)"
    with pytest.raises(SourceReviewError, match="invalid_review_packet"):
        validate_review_packet(packet)


def rehash(packet):
    packet["plan_id"] = digest({k: v for k, v in packet.items() if k != "plan_id"})


def test_packet_byte_boundary_includes_all_links_and_preserves_safe_diagnostics(
    tmp_path,
):
    packet = prepare_source_review([linked_article(1366)]).packet
    # Pad only ASCII URL metadata, retaining every original link and the fixed
    # size digest. The byte boundary applies to canonical JSON, not its final LF.
    packet["sources"][0]["links"].append("https://vendor.example/padding/")
    padding = MAX_PACKET_BYTES - len(canonical_json(packet).encode())
    assert padding > 0
    packet["sources"][0]["links"][-1] += "x" * padding
    rehash(packet)
    assert len(canonical_json(packet).encode()) == MAX_PACKET_BYTES
    assert validate_review_packet(packet) == packet
    path = write_review_packet(packet, tmp_path)
    assert path.stat().st_size == MAX_PACKET_BYTES + 1
    assert write_review_packet(packet, tmp_path) == path
    packet["sources"][0]["links"][-1] += "x"
    rehash(packet)
    with pytest.raises(SourceReviewError) as caught:
        write_review_packet(packet, tmp_path)
    assert caught.value.code == "review_packet_size_limit_exceeded"
    assert validation_diagnostic("source_review", caught.value)["codes"] == [
        "review_packet_size_limit_exceeded"
    ]
    assert len(list(tmp_path.iterdir())) == 1

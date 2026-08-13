import hashlib

from src.core.content_fingerprint import (
    compute_articles_fingerprint,
    read_stored_fingerprint,
    write_stored_fingerprint,
)


def test_fingerprint_is_stable_regardless_of_article_order():
    articles_a = [{"link": "https://a"}, {"link": "https://b"}]
    articles_b = [{"link": "https://b"}, {"link": "https://a"}]

    assert compute_articles_fingerprint(articles_a) == compute_articles_fingerprint(
        articles_b
    )


def test_fingerprint_changes_when_article_set_changes():
    original = compute_articles_fingerprint([{"link": "https://a"}])
    changed = compute_articles_fingerprint(
        [{"link": "https://a"}, {"link": "https://c"}]
    )

    assert original != changed


def test_fingerprint_changes_when_enriched_content_or_cves_change():
    original = compute_articles_fingerprint(
        [{"link": "https://a", "content": "CVE pending", "cves": []}]
    )
    enriched = compute_articles_fingerprint(
        [
            {
                "link": "https://a",
                "content": "Assigned CVE-2026-55040",
                "cves": ["CVE-2026-55040"],
            }
        ]
    )

    assert original != enriched


def test_fingerprint_normalizes_structured_cves_like_prompt_heading():
    spaced = compute_articles_fingerprint(
        [{"link": "https://a", "cves": ["cve 2026 1234", "not assigned"]}]
    )
    canonical = compute_articles_fingerprint(
        [{"link": "https://a", "cves": ["CVE-2026-1234", "pending"]}]
    )

    assert spaced == canonical


def test_fingerprint_changes_when_source_attribution_changes():
    original = compute_articles_fingerprint(
        [{"link": "https://a", "source": "Original Research Team"}]
    )
    corrected = compute_articles_fingerprint(
        [{"link": "https://a", "source": "Corrected Research Team"}]
    )

    assert original != corrected


def test_fingerprint_omits_unknown_source_like_the_prompt():
    missing = compute_articles_fingerprint([{"link": "https://a"}])
    unknown = compute_articles_fingerprint(
        [{"link": "https://a", "source": " Unknown\n SOURCE "}]
    )

    assert missing == unknown


def test_fingerprint_ignores_content_after_prompt_cutoff():
    visible_prefix = "A" * 2000
    original = compute_articles_fingerprint(
        [{"link": "https://a", "content": visible_prefix + "old suffix"}]
    )
    changed_suffix = compute_articles_fingerprint(
        [{"link": "https://a", "content": visible_prefix + "new suffix"}]
    )

    assert original == changed_suffix


def test_fingerprint_records_transition_to_truncated_prompt_content():
    visible_prefix = "A" * 2000
    exact_limit = compute_articles_fingerprint(
        [{"link": "https://a", "content": visible_prefix}]
    )
    truncated = compute_articles_fingerprint(
        [{"link": "https://a", "content": visible_prefix + "B"}]
    )

    assert exact_limit != truncated


def test_fingerprint_uses_summary_only_when_it_is_prompt_content():
    with_content = compute_articles_fingerprint(
        [{"link": "https://a", "content": "Full text", "summary": "Old summary"}]
    )
    changed_hidden_summary = compute_articles_fingerprint(
        [{"link": "https://a", "content": "Full text", "summary": "New summary"}]
    )
    summary_only = compute_articles_fingerprint(
        [{"link": "https://a", "summary": "Old summary"}]
    )
    changed_visible_summary = compute_articles_fingerprint(
        [{"link": "https://a", "summary": "New summary"}]
    )

    assert with_content == changed_hidden_summary
    assert summary_only != changed_visible_summary


def test_fingerprint_distinguishes_missing_from_explicitly_empty_content():
    missing = compute_articles_fingerprint([{"link": "https://a"}])
    explicitly_empty = compute_articles_fingerprint(
        [{"link": "https://a", "content": "", "summary": ""}]
    )

    assert missing != explicitly_empty


def test_fingerprint_preserves_prompt_visible_line_boundaries():
    separate_clauses = compute_articles_fingerprint(
        [
            {
                "link": "https://a",
                "content": (
                    "CVE-2026-1111 is not exploited\n"
                    "Attackers actively exploit CVE-2026-2222"
                ),
            }
        ]
    )
    same_line = compute_articles_fingerprint(
        [
            {
                "link": "https://a",
                "content": (
                    "CVE-2026-1111 is not exploited "
                    "Attackers actively exploit CVE-2026-2222"
                ),
            }
        ]
    )

    assert separate_clauses != same_line


def test_fingerprint_normalizes_title_like_generated_heading():
    multiline = compute_articles_fingerprint(
        [
            {
                "link": "https://a",
                "title": (
                    "CVE-2026-1111 is not exploited\n"
                    "Attackers actively exploit CVE-2026-2222"
                ),
            }
        ]
    )
    same_line = compute_articles_fingerprint(
        [
            {
                "link": "https://a",
                "title": (
                    "CVE-2026-1111 is not exploited "
                    "Attackers actively exploit CVE-2026-2222"
                ),
            }
        ]
    )

    assert multiline == same_line


def test_fingerprint_applies_untitled_article_prompt_fallback():
    missing = compute_articles_fingerprint([{"link": "https://a"}])
    blank = compute_articles_fingerprint([{"link": "https://a", "title": "  "}])
    fallback = compute_articles_fingerprint(
        [{"link": "https://a", "title": "Untitled article"}]
    )

    assert missing == blank == fallback


def test_fingerprint_invalidates_legacy_identity_only_hash():
    legacy_fingerprint = hashlib.sha256(b"https://a").hexdigest()

    assert compute_articles_fingerprint([{"link": "https://a"}]) != legacy_fingerprint


def test_fingerprint_falls_back_to_title_when_link_missing():
    fingerprint = compute_articles_fingerprint([{"title": "Only a title"}])

    assert fingerprint == compute_articles_fingerprint([{"title": "Only a title"}])


def test_read_stored_fingerprint_returns_none_when_missing(tmp_path):
    path = tmp_path / "fingerprint"

    assert read_stored_fingerprint(str(path)) is None


def test_write_and_read_stored_fingerprint_round_trip(tmp_path):
    path = tmp_path / "fingerprint"

    write_stored_fingerprint("abc123", str(path))

    assert read_stored_fingerprint(str(path)) == "abc123"

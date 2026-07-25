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

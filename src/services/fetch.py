import logging
from dataclasses import dataclass, field
from html.parser import HTMLParser
import re
from typing import List, Dict, Any
import httpx
import feedparser
from datetime import datetime

from ..core.cve import extract_cve_ids

logger = logging.getLogger(__name__)

ARTICLE_BODY_MARKERS = {
    "article-body",
    "articlebody",
    "entry-content",
    "post-content",
    "story-body",
}
BLOCK_TAGS = {
    "article",
    "blockquote",
    "br",
    "div",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "li",
    "main",
    "p",
    "section",
    "td",
    "th",
    "tr",
}
SKIP_TAGS = {
    "aside",
    "footer",
    "nav",
    "noscript",
    "script",
    "style",
    "svg",
    "template",
}
VOID_TAGS = {
    "area",
    "base",
    "br",
    "col",
    "embed",
    "hr",
    "img",
    "input",
    "link",
    "meta",
    "param",
    "source",
    "track",
    "wbr",
}


def _normalize_text(text: str) -> str:
    lines = []
    for line in text.splitlines():
        normalized = re.sub(r"\s+", " ", line).strip()
        if normalized:
            lines.append(normalized)
    return "\n".join(lines)


def _is_article_body(attrs: dict[str, str]) -> bool:
    item_properties = set(attrs.get("itemprop", "").casefold().split())
    if "articlebody" in item_properties:
        return True
    identifiers = " ".join((attrs.get("id", ""), attrs.get("class", "")))
    normalized = identifiers.casefold().replace("_", "-")
    tokens = set(re.split(r"\s+", normalized))
    return bool(tokens & ARTICLE_BODY_MARKERS)


def _article_body_priority(tag: str, attrs: dict[str, str]) -> int:
    if _is_article_body(attrs):
        return 3
    if tag == "article":
        return 2
    if tag == "main":
        return 1
    return 0


@dataclass
class ArticleTextCandidate:
    tag: str
    priority: int
    order: int
    tag_depth: int = 1
    parts: list[str] = field(default_factory=list)


class ArticleBodyParser(HTMLParser):
    """Extract readable text from a source page's primary article body."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.hidden_depth = 0
        self.candidates: list[ArticleTextCandidate] = []
        self.active_candidates: list[ArticleTextCandidate] = []
        self.meta_descriptions: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        normalized_tag = tag.casefold()
        attr_map = {name.casefold(): value or "" for name, value in attrs}

        if normalized_tag in SKIP_TAGS:
            self.hidden_depth += 1
            return
        if self.hidden_depth:
            return

        if normalized_tag == "meta":
            meta_name = (
                attr_map.get("property", "") or attr_map.get("name", "")
            ).casefold()
            if meta_name in {"description", "og:description"}:
                description = attr_map.get("content", "").strip()
                if description:
                    self.meta_descriptions.append(description)

        for candidate in self.active_candidates:
            if candidate.tag == normalized_tag and normalized_tag not in VOID_TAGS:
                candidate.tag_depth += 1

        priority = _article_body_priority(normalized_tag, attr_map)
        if priority and normalized_tag not in VOID_TAGS:
            candidate = ArticleTextCandidate(
                tag=normalized_tag,
                priority=priority,
                order=len(self.candidates),
            )
            self.candidates.append(candidate)
            self.active_candidates.append(candidate)

        if normalized_tag in BLOCK_TAGS:
            for candidate in self.active_candidates:
                candidate.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        normalized_tag = tag.casefold()
        if normalized_tag in SKIP_TAGS:
            if self.hidden_depth:
                self.hidden_depth -= 1
            return
        if self.hidden_depth:
            return

        for candidate in list(self.active_candidates):
            if normalized_tag in BLOCK_TAGS:
                candidate.parts.append("\n")
            if normalized_tag == candidate.tag:
                candidate.tag_depth -= 1
                if candidate.tag_depth == 0:
                    self.active_candidates.remove(candidate)

    def handle_data(self, data: str) -> None:
        if not self.hidden_depth:
            for candidate in self.active_candidates:
                candidate.parts.append(data)

    def primary_text(self) -> str:
        populated_candidates = []
        for candidate in self.candidates:
            candidate_text = _normalize_text("".join(candidate.parts))
            if candidate_text:
                populated_candidates.append((candidate, candidate_text))
        if not populated_candidates:
            return ""
        _, selected_text = max(
            populated_candidates,
            key=lambda item: (item[0].priority, -item[0].order),
        )
        return selected_text


class FeedContentParser(HTMLParser):
    """Extract visible text from an RSS content fragment."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.hidden_depth = 0
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        normalized_tag = tag.casefold()
        if normalized_tag in SKIP_TAGS:
            self.hidden_depth += 1
        elif not self.hidden_depth and normalized_tag in BLOCK_TAGS:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        normalized_tag = tag.casefold()
        if normalized_tag in SKIP_TAGS:
            if self.hidden_depth:
                self.hidden_depth -= 1
        elif not self.hidden_depth and normalized_tag in BLOCK_TAGS:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if not self.hidden_depth:
            self.parts.append(data)


def flatten_feed_content(value: Any) -> str:
    if isinstance(value, list):
        return "\n".join(flatten_feed_content(item) for item in value)
    if isinstance(value, dict):
        return flatten_feed_content(value.get("value", ""))
    return "" if value is None else str(value)


def extract_feed_content_text(value: Any) -> str:
    parser = FeedContentParser()
    parser.feed(flatten_feed_content(value))
    return _normalize_text("".join(parser.parts))


def extract_article_text(source_html: str) -> str:
    """Return primary article text, falling back to page description metadata."""
    parser = ArticleBodyParser()
    parser.feed(source_html)
    article_body = parser.primary_text()
    if article_body:
        return article_body
    return _normalize_text("\n".join(parser.meta_descriptions))


def merge_article_cves(article: Dict[str, Any], *texts: Any) -> None:
    existing_cves = article.get("cves", [])
    if existing_cves is None:
        existing_cves = []
    elif isinstance(existing_cves, str):
        existing_cves = [existing_cves]
    cve_text = "\n".join(
        [*(str(value) for value in existing_cves), *(str(value) for value in texts)]
    )
    article["cves"] = extract_cve_ids(cve_text)


class SentryDigestFeedClient:
    """
    Client for fetching articles from the SentryDigest RSS feed.
    """

    def __init__(self, feed_url: str):
        """
        Initialize the fetcher with the feed URL

        Args:
            feed_url: URL of the SentryDigest RSS feed
        """
        self.feed_url = feed_url
        self.client = None

    async def _fetch_articles_with_client(
        self, client: httpx.AsyncClient
    ) -> List[Dict[str, Any]]:
        response = await client.get(self.feed_url)
        response.raise_for_status()

        feed = feedparser.parse(response.text)
        articles = []
        for entry in feed.entries:
            article = {
                "title": entry.get("title", ""),
                "link": entry.get("link", ""),
                "summary": extract_feed_content_text(entry.get("description", "")),
                "published": entry.get("published", ""),
                "source": entry.get("dc_source", "Unknown Source"),
                "date": entry.get("dc_date", datetime.now().strftime("%Y-%m-%d")),
                "content": extract_feed_content_text(entry.get("content", "")),
                "cves": entry.get("cves", []),
            }
            merge_article_cves(
                article,
                article["title"],
                article["link"],
                article["summary"],
                article["content"],
            )
            articles.append(article)
        return articles

    async def fetch_articles(self) -> List[Dict[str, Any]]:
        """
        Fetch articles from SentryDigest RSS feed

        Returns:
            List of articles with basic metadata
        """
        logger.info(f"Fetching articles from {self.feed_url}")

        try:
            if self.client is not None:
                articles = await self._fetch_articles_with_client(self.client)
            else:
                async with httpx.AsyncClient(
                    follow_redirects=True, timeout=30.0
                ) as client:
                    articles = await self._fetch_articles_with_client(client)

            logger.info(f"Extracted {len(articles)} articles from feed")
            return articles

        except Exception as e:
            logger.error(f"Error fetching articles: {e}")
            raise

    async def enrich_article_content(
        self, articles: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """
        Enrich articles with full content

        Args:
            articles: List of article dictionaries

        Returns:
            Enriched list of articles with full content
        """
        logger.info(f"Enriching {len(articles)} articles with content")

        # List to store enriched articles
        enriched_articles = []

        # Process each article
        for article in articles:
            logger.info(f"Enriching article: {article.get('title', '')}")

            # Skip if the article already has content
            if "content" in article and article["content"]:
                article["content"] = extract_feed_content_text(article["content"])
            if article.get("content"):
                merge_article_cves(
                    article,
                    article.get("title", ""),
                    article.get("summary", ""),
                    article["content"],
                )
                enriched_articles.append(article)
                continue

            # Combine title and summary for basic content
            full_content = article.get("title", "") + "\n"

            # Add summary if available
            if "summary" in article and article["summary"]:
                full_content += article["summary"] + "\n"

            article_link = article.get("link", "")
            if not article_link:
                article["content"] = full_content
                enriched_articles.append(article)
                continue

            # Use async fetch for full article content
            try:
                timeout = httpx.Timeout(10.0, connect=5.0)
                async with httpx.AsyncClient(
                    timeout=timeout, follow_redirects=True
                ) as client:
                    logger.info(f"Fetching full content for: {article_link}")
                    response = await client.get(article_link)

                    if response.status_code == 200:
                        article_text = extract_article_text(response.text)
                        article["content"] = full_content
                        if article_text:
                            article["content"] += "\n" + article_text
                    else:
                        # Use what we have if we can't fetch the full article
                        logger.warning(
                            f"Could not fetch full content: {response.status_code}"
                        )
                        article["content"] = full_content
            except Exception as e:
                logger.warning(f"Error fetching full content: {e}")
                # Fall back to summary if error occurs
                article["content"] = full_content

            merge_article_cves(
                article,
                article.get("title", ""),
                article.get("summary", ""),
                article.get("content", ""),
            )

            enriched_articles.append(article)

        logger.info(f"Enriched {len(enriched_articles)} articles with content")
        return enriched_articles

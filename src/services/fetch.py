import logging
from dataclasses import dataclass, field
from html.parser import HTMLParser
import re
from typing import List, Dict, Any
import httpx
import feedparser
from datetime import datetime

from ..core.cve import extract_cve_ids
from ..core.prompt_content import get_prompt_visible_content

logger = logging.getLogger(__name__)

ARTICLE_BODY_MARKERS = {
    "article-body",
    "articlebody",
    "entry-content",
    "post-content",
    "story-body",
}
ARTICLE_COLLECTION_MARKERS = {
    "archive",
    "cards",
    "feed",
    "grid",
    "items",
    "list",
    "recommendations",
    "related",
    "results",
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
PAGE_SKIP_TAGS = SKIP_TAGS | {"head"}
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
CURRENT_VULNERABILITY_LINK_PATTERN = re.compile(
    r"^(?:(?:this|the)\s+)?(?:cve|vulnerability|security\s+"
    r"(?:issue|flaw|vulnerability)|issue|flaw|bug)"
    r"(?:\s+(?:details?|record|information))?[.:]?$",
    re.IGNORECASE,
)
AUXILIARY_LINK_PATTERN = re.compile(
    r"\b(?:additional|another|more|next|other|previous|related)\b", re.IGNORECASE
)


def _normalize_text(text: str) -> str:
    lines = []
    for line in text.splitlines():
        normalized = re.sub(r"\s+", " ", line).strip()
        if normalized:
            lines.append(normalized)
    return "\n".join(lines)


def _referenced_link_cves(href_cves: list[str], link_text: str) -> list[str]:
    if not href_cves:
        return []
    visible_cves = set(extract_cve_ids(link_text))
    explicit_cves = [cve for cve in href_cves if cve in visible_cves]
    if explicit_cves:
        return explicit_cves
    normalized_text = " ".join(link_text.split())
    if AUXILIARY_LINK_PATTERN.search(normalized_text):
        return []
    if CURRENT_VULNERABILITY_LINK_PATTERN.fullmatch(normalized_text):
        return href_cves
    return []


def _link_cve_annotation(href_cves: list[str], link_text: str) -> str:
    visible_cves = set(extract_cve_ids(link_text))
    inferred_cves = [
        cve
        for cve in _referenced_link_cves(href_cves, link_text)
        if cve not in visible_cves
    ]
    return f" ({', '.join(inferred_cves)})" if inferred_cves else ""


def _is_hidden_element(attrs: dict[str, str]) -> bool:
    return "hidden" in attrs or attrs.get("aria-hidden", "").casefold() == "true"


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


def _is_article_collection(tag: str, attrs: dict[str, str]) -> bool:
    if tag in {"ol", "ul"}:
        return True
    identifiers = " ".join((attrs.get("id", ""), attrs.get("class", "")))
    tokens = set(re.split(r"[\s_-]+", identifiers.casefold()))
    return bool(tokens & ARTICLE_COLLECTION_MARKERS)


@dataclass
class ArticleTextCandidate:
    tag: str
    priority: int
    order: int
    parent_order: int | None = None
    parent_is_collection: bool = False
    tag_depth: int = 1
    parts: list[str] = field(default_factory=list)


@dataclass
class ActiveCveLink:
    href_cves: list[str]
    parts: list[str] = field(default_factory=list)
    article_candidates: list[ArticleTextCandidate] = field(default_factory=list)


class ArticleBodyParser(HTMLParser):
    """Extract readable text from a source page's primary article body."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.hidden_depth = 0
        self.hidden_tag = ""
        self.candidates: list[ArticleTextCandidate] = []
        self.active_candidates: list[ArticleTextCandidate] = []
        self.element_stack: list[tuple[str, int, bool]] = []
        self.next_element_order = 0
        self.meta_descriptions: list[str] = []
        self.active_cve_link: ActiveCveLink | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        normalized_tag = tag.casefold()
        attr_map = {name.casefold(): value or "" for name, value in attrs}

        if self.hidden_depth:
            if normalized_tag == self.hidden_tag:
                self.hidden_depth += 1
            return
        if normalized_tag in SKIP_TAGS or _is_hidden_element(attr_map):
            if normalized_tag not in VOID_TAGS:
                self.hidden_depth = 1
                self.hidden_tag = normalized_tag
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

        element_order = self.next_element_order
        self.next_element_order += 1
        parent_context = self.element_stack[-1] if self.element_stack else None
        parent_order = parent_context[1] if parent_context else None
        priority = _article_body_priority(normalized_tag, attr_map)
        if priority and normalized_tag not in VOID_TAGS:
            candidate = ArticleTextCandidate(
                tag=normalized_tag,
                priority=priority,
                order=len(self.candidates),
                parent_order=parent_order,
                parent_is_collection=bool(parent_context and parent_context[2]),
            )
            self.candidates.append(candidate)
            self.active_candidates.append(candidate)

        if normalized_tag == "a" and (href := attr_map.get("href")):
            href_cves = extract_cve_ids(href)
            if href_cves:
                self.active_cve_link = ActiveCveLink(
                    href_cves=href_cves,
                    article_candidates=list(self.active_candidates),
                )

        if normalized_tag == "img" and (alt_text := attr_map.get("alt", "").strip()):
            if self.active_cve_link:
                self.active_cve_link.parts.append(alt_text)
            for candidate in self.active_candidates:
                candidate.parts.append(f" {alt_text} ")

        if normalized_tag in BLOCK_TAGS:
            for candidate in self.active_candidates:
                candidate.parts.append("\n")
        if normalized_tag not in VOID_TAGS:
            self.element_stack.append(
                (
                    normalized_tag,
                    element_order,
                    _is_article_collection(normalized_tag, attr_map),
                )
            )

    def handle_endtag(self, tag: str) -> None:
        normalized_tag = tag.casefold()
        if self.hidden_depth:
            if normalized_tag == self.hidden_tag:
                self.hidden_depth -= 1
                if not self.hidden_depth:
                    self.hidden_tag = ""
            return

        if normalized_tag == "a" and self.active_cve_link:
            annotation = _link_cve_annotation(
                self.active_cve_link.href_cves, "".join(self.active_cve_link.parts)
            )
            for candidate in self.active_cve_link.article_candidates:
                candidate.parts.append(annotation)
            self.active_cve_link = None

        for candidate in list(self.active_candidates):
            if normalized_tag in BLOCK_TAGS:
                candidate.parts.append("\n")
            if normalized_tag == candidate.tag:
                candidate.tag_depth -= 1
                if candidate.tag_depth == 0:
                    self.active_candidates.remove(candidate)
        for index in range(len(self.element_stack) - 1, -1, -1):
            if self.element_stack[index][0] == normalized_tag:
                del self.element_stack[index:]
                break

    def handle_data(self, data: str) -> None:
        if not self.hidden_depth:
            if self.active_cve_link:
                self.active_cve_link.parts.append(data)
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
        selection_options = list(populated_candidates)
        sibling_groups: dict[
            tuple[int, int], list[tuple[ArticleTextCandidate, str]]
        ] = {}
        for candidate, candidate_text in populated_candidates:
            if candidate.parent_order is not None:
                sibling_groups.setdefault(
                    (candidate.priority, candidate.parent_order), []
                ).append((candidate, candidate_text))
        for siblings in sibling_groups.values():
            if len(siblings) > 1 and not siblings[0][0].parent_is_collection:
                first_candidate = min(siblings, key=lambda item: item[0].order)[0]
                combined_text = _normalize_text(
                    "\n".join(
                        text
                        for _, text in sorted(siblings, key=lambda item: item[0].order)
                    )
                )
                selection_options.append((first_candidate, combined_text))
        _, selected_text = max(
            selection_options,
            key=lambda item: (item[0].priority, len(item[1]), -item[0].order),
        )
        return selected_text


class FeedContentParser(HTMLParser):
    """Extract visible text from an RSS content fragment."""

    def __init__(self, skip_tags: set[str] | None = None) -> None:
        super().__init__(convert_charrefs=True)
        self.skip_tags = SKIP_TAGS if skip_tags is None else skip_tags
        self.hidden_depth = 0
        self.hidden_tag = ""
        self.parts: list[str] = []
        self.active_cve_link: ActiveCveLink | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        normalized_tag = tag.casefold()
        attr_map = {name.casefold(): value or "" for name, value in attrs}
        if self.hidden_depth:
            if normalized_tag == self.hidden_tag:
                self.hidden_depth += 1
        elif normalized_tag in self.skip_tags or _is_hidden_element(attr_map):
            if normalized_tag not in VOID_TAGS:
                self.hidden_depth = 1
                self.hidden_tag = normalized_tag
        else:
            if normalized_tag == "a" and (href := attr_map.get("href")):
                href_cves = extract_cve_ids(href)
                if href_cves:
                    self.active_cve_link = ActiveCveLink(href_cves=href_cves)
            if normalized_tag == "img" and (
                alt_text := attr_map.get("alt", "").strip()
            ):
                if self.active_cve_link:
                    self.active_cve_link.parts.append(alt_text)
                self.parts.append(f" {alt_text} ")
            if normalized_tag in BLOCK_TAGS:
                self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        normalized_tag = tag.casefold()
        if self.hidden_depth:
            if normalized_tag == self.hidden_tag:
                self.hidden_depth -= 1
                if not self.hidden_depth:
                    self.hidden_tag = ""
        elif normalized_tag in BLOCK_TAGS:
            self.parts.append("\n")
        if normalized_tag == "a" and self.active_cve_link:
            self.parts.append(
                _link_cve_annotation(
                    self.active_cve_link.href_cves,
                    "".join(self.active_cve_link.parts),
                )
            )
            self.active_cve_link = None

    def handle_data(self, data: str) -> None:
        if not self.hidden_depth:
            self.parts.append(data)
            if self.active_cve_link:
                self.active_cve_link.parts.append(data)


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
    page_parser = FeedContentParser(skip_tags=PAGE_SKIP_TAGS)
    page_parser.feed(source_html)
    page_text = _normalize_text("".join(page_parser.parts))
    metadata_text = _normalize_text("\n".join(parser.meta_descriptions))
    if metadata_text and page_text:
        return _normalize_text(f"{metadata_text}\n{page_text}")
    return metadata_text or page_text


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


def merge_prompt_visible_article_cves(article: Dict[str, Any]) -> None:
    prompt_content = article.get("content") or article.get("summary")
    visible_content = (
        ""
        if prompt_content is None
        else get_prompt_visible_content(str(prompt_content).strip())
    )
    merge_article_cves(
        article,
        article.get("title", ""),
        article.get("link", ""),
        visible_content,
    )


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
            description = entry.get("description", "")
            content = entry.get("content", "")
            entry_cves = entry.get("cves", [])
            if isinstance(entry_cves, str):
                entry_cves = [entry_cves]
            article = {
                "title": entry.get("title", ""),
                "link": entry.get("link", ""),
                "summary": extract_feed_content_text(description),
                "published": entry.get("published", ""),
                "source": entry.get("dc_source", "Unknown Source"),
                "date": entry.get("dc_date", datetime.now().strftime("%Y-%m-%d")),
                "content": extract_feed_content_text(content),
                "cves": [*(entry_cves or [])],
            }
            merge_prompt_visible_article_cves(article)
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

            # Feed content is sanitized once during ingestion. Parsing the resulting
            # plain text again would reinterpret escaped markup as live HTML.
            if article.get("content"):
                merge_prompt_visible_article_cves(article)
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
                merge_prompt_visible_article_cves(article)
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

            merge_prompt_visible_article_cves(article)

            enriched_articles.append(article)

        logger.info(f"Enriched {len(enriched_articles)} articles with content")
        return enriched_articles

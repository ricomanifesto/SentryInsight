"""Track the source article set behind the last published report.

The analysis model runs at temperature=1, so the rendered report text
never matches byte-for-byte between runs even when the underlying
articles are unchanged. Fingerprinting normalized enriched source records
(rather than the LLM's rendered output) lets the workflow detect "nothing
new happened" and skip redundant analysis/TTS steps entirely.
"""

import hashlib
import json
from pathlib import Path
import re
from typing import Any, Dict, List, Optional

FINGERPRINT_PATH = ".sentryinsight-articles-fingerprint"
FINGERPRINT_SCHEMA_VERSION = "source-content-v6"
PROMPT_ARTICLE_CHAR_LIMIT = 2000


def _normalize_fingerprint_value(value: Any) -> str:
    return re.sub(r"\s+", " ", "" if value is None else str(value)).strip()


def _normalize_prompt_content(article: Dict[str, Any]) -> str:
    content = article.get("content") or article.get("summary")
    visible_content = "" if content is None else str(content).strip()
    return visible_content[:PROMPT_ARTICLE_CHAR_LIMIT]


def compute_articles_fingerprint(articles: List[Dict[str, Any]]) -> str:
    """Compute a stable fingerprint of enriched source article records."""
    records = set()
    for article in articles:
        raw_cves = article.get("cves", [])
        if isinstance(raw_cves, str):
            raw_cves = [raw_cves]
        normalized_cves = sorted(
            {
                normalized
                for value in raw_cves or []
                if (normalized := _normalize_fingerprint_value(value))
            }
        )
        record = {
            "cves": normalized_cves,
            "identity": _normalize_fingerprint_value(
                article.get("link") or article.get("title")
            ),
            "prompt_content": _normalize_prompt_content(article),
            "source": _normalize_fingerprint_value(article.get("source")),
            "title": _normalize_fingerprint_value(article.get("title")),
        }
        if any(record.values()):
            records.add(json.dumps(record, sort_keys=True, separators=(",", ":")))
    fingerprint_input = "\n".join([FINGERPRINT_SCHEMA_VERSION, *sorted(records)])
    return hashlib.sha256(fingerprint_input.encode("utf-8")).hexdigest()


def read_stored_fingerprint(path: str = FINGERPRINT_PATH) -> Optional[str]:
    """Read the fingerprint recorded for the last published report, if any."""
    fingerprint_path = Path(path)
    if not fingerprint_path.exists():
        return None
    return fingerprint_path.read_text().strip() or None


def write_stored_fingerprint(fingerprint: str, path: str = FINGERPRINT_PATH) -> None:
    """Persist the fingerprint for the report just published."""
    Path(path).write_text(fingerprint + "\n")

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

from .cve import extract_cve_ids
from .prompt_content import get_prompt_visible_content, normalize_prompt_metadata

FINGERPRINT_PATH = ".sentryinsight-articles-fingerprint"
FINGERPRINT_SCHEMA_VERSION = "source-content-v10"


def _normalize_fingerprint_value(value: Any) -> str:
    return re.sub(r"\s+", " ", "" if value is None else str(value)).strip()


def _normalize_prompt_content(article: Dict[str, Any]) -> str:
    content = article.get("content") or article.get("summary")
    visible_content = "" if content is None else str(content).strip()
    return get_prompt_visible_content(visible_content)


def compute_articles_fingerprint(articles: List[Dict[str, Any]]) -> str:
    """Compute a stable fingerprint of enriched source article records."""
    records = set()
    for article in articles:
        raw_cves = article.get("cves", [])
        if isinstance(raw_cves, str):
            raw_cves = [raw_cves]
        normalized_cves = sorted(
            extract_cve_ids("\n".join(str(value) for value in raw_cves or []))
        )
        record = {
            "cves": normalized_cves,
            "link": normalize_prompt_metadata(article.get("link")),
            "prompt_content": _normalize_prompt_content(article),
            "source": _normalize_fingerprint_value(article.get("source")),
            "title": normalize_prompt_metadata(article.get("title")),
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

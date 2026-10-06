"""Track the source article set behind the last published report.

The analysis model runs at temperature=1, so the rendered report text
never matches byte-for-byte between runs even when the underlying
articles are unchanged. Fingerprinting the retained article evidence (rather
than the model's rendered output) lets the workflow detect "nothing new
happened" and skip the paid analysis/TTS steps entirely.
"""

import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List, Optional

FINGERPRINT_PATH = ".sentryinsight-articles-fingerprint"


def compute_articles_fingerprint(articles: List[Dict[str, Any]]) -> str:
    """Compute a stable fingerprint identifying the set of source articles."""
    identifiers = sorted(
        {
            json.dumps(
                {
                    "identity": str(
                        article.get("link") or article.get("title") or ""
                    ).strip(),
                    "content": article.get("content") or article.get("summary") or "",
                    "content_kind": article.get("content_kind", "feed"),
                    "links": sorted(article.get("source_links", [])),
                },
                sort_keys=True,
            )
            for article in articles
            if str(article.get("link") or article.get("title") or "").strip()
        }
    )
    return hashlib.sha256("\n".join(identifiers).encode("utf-8")).hexdigest()


def read_stored_fingerprint(path: str = FINGERPRINT_PATH) -> Optional[str]:
    """Read the fingerprint recorded for the last published report, if any."""
    fingerprint_path = Path(path)
    if not fingerprint_path.exists():
        return None
    return fingerprint_path.read_text().strip() or None


def write_stored_fingerprint(fingerprint: str, path: str = FINGERPRINT_PATH) -> None:
    """Persist the fingerprint for the report just published."""
    Path(path).write_text(fingerprint + "\n")

"""Track the source article set behind the last published report.

The analysis model runs at temperature=1, so the rendered report text
never matches byte-for-byte between runs even when the underlying
articles are unchanged. Fingerprinting the article identities (rather
than the LLM's rendered output) lets the workflow detect "nothing new
happened" and skip the paid analysis/TTS steps entirely.
"""

import hashlib
from pathlib import Path
from typing import Any, Dict, List, Optional

FINGERPRINT_PATH = ".sentryinsight-articles-fingerprint"
FINGERPRINT_SCHEMA_VERSION = "source-content-v2"


def compute_articles_fingerprint(articles: List[Dict[str, Any]]) -> str:
    """Compute a stable fingerprint identifying the set of source articles."""
    identifiers = sorted(
        {
            str(article.get("link") or article.get("title") or "").strip()
            for article in articles
        }
        - {""}
    )
    fingerprint_input = "\n".join([FINGERPRINT_SCHEMA_VERSION, *identifiers])
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

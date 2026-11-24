import logging
from typing import List, Dict, Any
from datetime import datetime, timezone
from pathlib import Path

import tiktoken

from .exploitation_coverage import (
    EXPLOITATION_RELEVANCE_PATTERN as EXPLOITATION_RELEVANCE_PATTERN,
    CVE_CONTEXT_PATTERN as CVE_CONTEXT_PATTERN,
    STRUCTURED_CVES_PATTERN as STRUCTURED_CVES_PATTERN,
    SENTENCE_PATTERN as SENTENCE_PATTERN,
    URL_PATTERN as URL_PATTERN,
    NEGATED_EXPLOITATION_PATTERN as NEGATED_EXPLOITATION_PATTERN,
    collect_prompt_cves as collect_prompt_cves,
    has_exploitation_relevance as has_exploitation_relevance,
    has_negated_exploitation_relevance as has_negated_exploitation_relevance,
    normalize_cve_match as normalize_cve_match,
    collect_structured_prompt_cves as collect_structured_prompt_cves,
    collect_url_prompt_cves as collect_url_prompt_cves,
    iter_line_sentences as iter_line_sentences,
    strip_cve_metadata_noise as strip_cve_metadata_noise,
    has_positive_exploitation_sentence as has_positive_exploitation_sentence,
    has_negated_cve_sentence as has_negated_cve_sentence,
    sentence_containing_position as sentence_containing_position,
    collect_exploitation_relevant_prompt_cves as collect_exploitation_relevant_prompt_cves,
    _coverage_subject_text as _coverage_subject_text,
)

from .model_config import resolve_model, validate_model
from .model_client import ReportModelClient, build_model_client
from .opencode_client import OpenCodeUnavailable, parse_model_selection
from .openrouter_client import (
    FREE_ROUTE_MAX_COMPLETION_TOKENS,
    validate_reasoning_max_tokens,
)
from .paid_verification import active_verification
from .analysis_errors import classify_analysis_error
from .derivations import derivation_scope
from .article_prompt import (
    clean_article_source as clean_article_source,
    collect_structured_cves as collect_structured_cves,
    format_article_summary as format_article_summary,
)
from .exploitation_prompt import ANALYSIS_SYSTEM_PROMPT, build_exploitation_prompt
from .version_references import PROTOCOL_KEY, PROTOCOL_VERSION
from .reporting import serialize_reporting_catalog
from .source_review import (
    PLAN_KEY,
    SourceReviewError,
    prepare_source_review,
    review_articles,
    write_review_packet,
)
from .publication_transaction import PublicationError, ensure_no_pending_publication

logger = logging.getLogger(__name__)

# Initialize tokenizer for token counting
tokenizer = tiktoken.get_encoding("cl100k_base")

# Observed free-route output rate is ~116 tokens/s (131k tokens ~= 19 min).
# Cap each HTTP attempt at 30 min (tolerable down to ~53-73 tok/s) and total
# initial + recovery wall-clock time at 60 min, leaving 15 min inside the
# 75-minute CI job timeout for setup, validation, browser checks and publish.
ANALYSIS_PER_REQUEST_TIMEOUT_CAP_SECONDS = 1800.0
ANALYSIS_TOTAL_TIMEOUT_CAP_SECONDS = 3600.0


def analysis_timeout_budget(max_tokens: int) -> tuple[float, float]:
    """Return bounded (per_request_timeout, total_timeout) seconds for analysis."""
    request_timeout = min(
        ANALYSIS_PER_REQUEST_TIMEOUT_CAP_SECONDS,
        max(120.0, float(max_tokens) / 50.0),
    )
    total_timeout = min(request_timeout * 2.0, ANALYSIS_TOTAL_TIMEOUT_CAP_SECONDS)
    return request_timeout, total_timeout


def filter_exploitation_articles(
    articles: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    """
    Filter articles to only include those with exploitation-related content

    Args:
        articles: List of article dictionaries

    Returns:
        Filtered list of articles with exploitation content
    """
    logger.info(f"Filtering {len(articles)} articles for exploitation content")

    # Pass all articles to the AI for analysis
    # This gives the AI more context to work with
    return articles


async def analyze_exploitation(
    articles: List[Dict[str, Any]],
    config: Dict[str, Any],
    *,
    model_client: ReportModelClient | None = None,
) -> Dict[str, Any]:
    """
    Analyze exploitation-related articles

    Args:
        articles: List of article dictionaries with exploitation content
        config: Configuration dictionary

    Returns:
        Exploitation analysis report
    """
    with derivation_scope():
        return await _analyze_exploitation(articles, config, model_client=model_client)


async def _analyze_exploitation(
    articles: List[Dict[str, Any]],
    config: Dict[str, Any],
    *,
    model_client: ReportModelClient | None,
) -> Dict[str, Any]:
    logger.info(f"Analyzing exploitation in {len(articles)} articles")

    # Initialize the AI model through OpenCode.
    model_name = resolve_model(config)
    analysis_config = config.get("analysis", {})
    verification = active_verification()
    max_tokens = (
        int(verification.profile["reportOutput"])
        if verification is not None
        else int(analysis_config.get("max_tokens", 4000))
    )
    try:
        validate_model(model_name)
        model_selection = parse_model_selection(model_name)
    except ValueError as e:
        logger.error(f"Invalid model configuration: {e}")
        return {
            "exploitation_report": f"# Error: Invalid Model\n\n{str(e)}",
            "date": datetime.now(timezone.utc).date().isoformat(),
            "error": str(e),
            "error_class": "analysis_exception",
            "error_detail": {},
        }
    try:
        reasoning_max_tokens = validate_reasoning_max_tokens(
            analysis_config.get("reasoning_max_tokens"), max_tokens
        )
    except ValueError as e:
        logger.error(f"Invalid analysis configuration: {e}")
        return {
            "exploitation_report": f"# Error: Invalid Analysis Configuration\n\n{str(e)}",
            "date": datetime.now(timezone.utc).date().isoformat(),
            "error": str(e),
            "error_class": "analysis_exception",
            "error_detail": {},
        }

    # Normalize and retain the complete host plan before constructing a provider.
    try:
        root = Path(config.get("output_path", "index.md")).parent
        ensure_no_pending_publication(root)
        plan = prepare_source_review(
            articles,
            advisory=config.get("analysis", {}).get("grounding") == "advisory",
        )
        write_review_packet(plan.packet, root / ".sentryinsight-review")
    except (SourceReviewError, PublicationError, OSError) as exc:
        return {
            "error": "Source review preflight failed",
            "error_class": "source_review_failed",
            "error_detail": {},
            "source_review_code": (
                exc.code
                if isinstance(exc, (SourceReviewError, PublicationError))
                else "review_packet_write_failed"
            ),
            "exploitation_report": "",
        }
    review_metadata = {
        PLAN_KEY: plan.packet,
        "reporting_sources": serialize_reporting_catalog(plan.catalog),
        "reporting_metadata_cves": {
            row["key"]: row["metadata_cves"] for row in plan.packet["sources"]
        },
    }
    articles = review_articles(plan)
    if not articles:
        return {
            **review_metadata,
            "skipped": True,
            "skip_reason": "source_review_required",
            "exploitation_report": "",
            "analyzed_article_count": 0,
        }

    all_cves = set()
    all_systems = set()
    all_attack_vectors = set()

    for article in articles:
        article_summary = format_article_summary(article)

        # Extract expected CVEs only when prompt text ties them to exploit activity.
        for cve in collect_exploitation_relevant_prompt_cves(article_summary):
            all_cves.add(cve)
        if "affected_systems" in article:
            for system in article.get("affected_systems", []):
                all_systems.add(system)
        if "attack_vectors" in article:
            for vector in article.get("attack_vectors", []):
                all_attack_vectors.add(vector)

    prompt = build_exploitation_prompt(plan)

    # Estimate token count for logging
    estimated_tokens = len(tokenizer.encode(prompt))
    logger.info(f"Estimated token count for analysis prompt: {estimated_tokens}")

    if estimated_tokens > int(
        config.get("analysis", {}).get("max_input_tokens", 100000)
    ):
        return {
            **review_metadata,
            "error": "Complete source evidence exceeds analysis input budget; no source text was truncated",
            "error_class": "input_budget_exceeded",
            "error_detail": {},
            "exploitation_report": "",
            "date": datetime.now(timezone.utc).date().isoformat(),
        }

    # Call the AI model
    client = None
    request_timeout, total_timeout = analysis_timeout_budget(max_tokens)
    is_free_route = (
        verification is None
        and model_selection is not None
        and model_selection.provider_id == "openrouter"
        and (
            model_selection.model_id.endswith(":free")
            or model_selection.model_id == "openrouter/free"
        )
    )
    recovery_max_tokens = (
        max(max_tokens, FREE_ROUTE_MAX_COMPLETION_TOKENS)
        if is_free_route
        else max_tokens
    )
    try:
        client = (
            model_client
            if model_client is not None
            else build_model_client(
                timeout=request_timeout,
                max_tokens=max_tokens,
                recovery_max_tokens=recovery_max_tokens,
                reasoning_max_tokens=reasoning_max_tokens,
                total_timeout=total_timeout,
                output_limit_recovery=True,
            )
        )
        exploitation_report = await client.generate(
            system_prompt=ANALYSIS_SYSTEM_PROMPT,
            user_prompt=prompt,
            model=model_selection,
            title="SentryInsight exploitation report",
        )

        return {
            **review_metadata,
            "exploitation_report": exploitation_report,
            "request_metadata": getattr(client, "last_request", None),
            "repair_eligible": verification is None,
            PROTOCOL_KEY: PROTOCOL_VERSION,
            "date": datetime.now(timezone.utc).date().isoformat(),
            "analyzed_article_count": len(articles),
            "cves_identified": list(all_cves),
        }
    except OpenCodeUnavailable as e:
        logger.warning(f"Skipping exploitation analysis: {e}")
        return {
            **review_metadata,
            "exploitation_report": "",
            "date": datetime.now(timezone.utc).date().isoformat(),
            "analyzed_article_count": len(articles),
            "cves_identified": list(all_cves),
            "skipped": True,
            "skip_reason": str(e),
        }
    except Exception as e:
        logger.error(f"Error during exploitation analysis: {e}")
        error_class, error_detail = classify_analysis_error(e)
        return {
            **review_metadata,
            "exploitation_report": f"# Error Generating Exploitation Report\n\nAn error occurred during analysis: {str(e)}\n\n## Partial Data\n\nCVEs identified: {', '.join(all_cves) if all_cves else 'None'}\n\nAffected systems: {', '.join(all_systems) if all_systems else 'None'}",
            "request_metadata": getattr(client, "last_request", None),
            "date": datetime.now(timezone.utc).date().isoformat(),
            "error": str(e),
            "error_class": error_class,
            "error_detail": error_detail,
        }

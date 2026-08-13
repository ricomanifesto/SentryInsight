import logging
import re
from typing import List, Dict, Any
from datetime import datetime

import tiktoken

from .model_config import resolve_model, validate_model
from .model_client import build_model_client
from .opencode_client import OpenCodeUnavailable, parse_model_selection
from .cve import extract_cve_ids
from .prompt_content import get_prompt_visible_content

logger = logging.getLogger(__name__)

# Initialize tokenizer for token counting
tokenizer = tiktoken.get_encoding("cl100k_base")

UNKNOWN_SOURCE_SENTINELS = {"unknown source"}

EXPLOITATION_RELEVANCE_PATTERN = re.compile(
    r"\b(?:"
    r"active(?:ly)? exploit(?:s|ed|ing|ation)?|"
    r"exploit(?:s|ed|ing|ation)?|"
    r"in the wild|"
    r"zero[\s-]?day|"
    r"0day|"
    r"weaponiz(?:ed|ation)|"
    r"under attack|"
    r"attackers? (?:are )?exploit(?:s|ed|ing)?|"
    r"backdoor|"
    r"malware|"
    r"threat actor|"
    r"campaign"
    r")\b",
    re.IGNORECASE,
)
CVE_CONTEXT_PATTERN = re.compile(
    r"\bCVE[-\s]?(\d{4})[-\s]?(\d{4,})(?!\d|\.\.\.|…)\b",
    re.IGNORECASE,
)
STRUCTURED_CVES_PATTERN = re.compile(r"CVEs:\s*([^)]*)", re.IGNORECASE)
SENTENCE_PATTERN = re.compile(r"[^.!?\n]+(?:[.!?]+|$)")
URL_PATTERN = re.compile(r"https?://\S+", re.IGNORECASE)
NEGATED_EXPLOITATION_PATTERN = re.compile(
    r"\b(?:"
    r"no evidence(?:\s+(?:of|that))?|"
    r"no\s+(?:(?:known|confirmed|observed|active)\s+)?(?=exploit)|"
    r"not\s+(?:actively\s+|being\s+)?(?=exploit)|"
    r"without\s+(?:evidence|signs?|reports?)(?:\s+of)?|"
    r"has not been|"
    r"have not been|"
    r"not known to be|"
    r"not reported to be|"
    r"not observed to be|"
    r"not detected as|"
    r"no signs? of|"
    r"no reports? of"
    r")\b.{0,120}\b(?:"
    r"exploit(?:ed|ing|ation)?|"
    r"in the wild|"
    r"weaponiz(?:ed|ation)|"
    r"under attack"
    r")\b",
    re.IGNORECASE | re.DOTALL,
)
POSTPOSED_NEGATED_EXPLOITATION_PATTERN = re.compile(
    r"\b(?:exploit(?:s|ed|ing|ation)?)\b.{0,120}\b"
    r"(?:has|have|had|is|are|was|were)\s+(?:not|never)\s+"
    r"(?:been\s+)?(?:confirmed|detected|known|observed|occurred|reported|seen)\b",
    re.IGNORECASE | re.DOTALL,
)
UNCONFIRMED_EXPLOITATION_PATTERN = re.compile(
    r"(?:"
    r"\b(?:can|could|might|possible|potential(?:ly)?)\b[^,.;\n]{0,100}"
    r"\bexploit(?:ed|ing|ation)?\b|"
    r"(?<!active )(?<!confirmed )(?<!observed )\bexploitation\s+of\b"
    r"[^,.;\n]{0,100}\b(?:can|could|may|might)\b(?=\s+"
    r"(?:(?:not|also|possibly|potentially|eventually|ultimately)\s+)*"
    r"(?:allow|cause|enable|expose|give|lead|permit|provide|result))|"
    r"\bmay\b(?=\s+(?:(?:not|also|possibly|potentially|eventually|ultimately)\s+)*"
    r"(?:be\s+)?(?:allow|cause|enable|exploit|expose|give|lead|permit|provide|result))"
    r"[^,.;\n]{0,100}"
    r"\bexploit(?:ed|ing|ation)?\b|"
    r"\bif\b.{0,100}\bexploit(?:ed|ing|ation)?\b|"
    r"\bindicative of\b.{0,100}\bexploit(?:ed|ing|ation)?\b|"
    r"\bnot enough evidence\b.{0,160}\b(?:exploit(?:ed|ing|ation)?|correlat)"
    r")",
    re.IGNORECASE | re.DOTALL,
)
GROUPED_ISSUES_PATTERN = re.compile(
    r"\b(?:all|both|these|the listed)\s+"
    r"(?:CVEs?|flaws?|issues?|vulnerabilit(?:y|ies))\b",
    re.IGNORECASE,
)
EXPLOITATION_CLAUSE_BOUNDARY_PATTERN = re.compile(
    r"(?:"
    r"[;,]\s*(?=(?:and|attackers?|threat actors?)\b)|"
    r"\s+(?=and\s+(?:attackers?|threat actors?|researchers?|they)\b)|"
    r"(?:[;,]\s*|\s+)(?=(?:but|however)\b|"
    r"yet\s+(?:attackers?|threat actors?|researchers?|they)\b)"
    r")",
    re.IGNORECASE,
)
FOLLOWING_CVE_REFERENCE_PATTERN = re.compile(
    r"\b(?:the|this|that|said)\s+(?:flaw|issue|vulnerability|bug|zero[\s-]?day)\b|"
    r"\bit\b",
    re.IGNORECASE,
)


def clean_article_source(value: Any) -> str:
    if value is None:
        return ""
    source = " ".join(str(value).split())
    if source.casefold() in UNKNOWN_SOURCE_SENTINELS:
        return ""
    return source


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


def format_article_summary(article: Dict[str, Any]) -> str:
    def clean_text(value: Any, default: str = "") -> str:
        if value is None:
            return default
        return str(value).strip()

    title = clean_text(article.get("title"), "Untitled article") or "Untitled article"
    source = clean_article_source(article.get("source"))
    link = clean_text(article.get("link"))
    content = clean_text(
        article.get("content") or article.get("summary"), "No content available"
    )

    metadata = []
    if source:
        metadata.append(f"Source: {source}")
    if link:
        metadata.append(f"URL: {link}")
    if article_cves := collect_structured_cves(article):
        metadata.append(f"CVEs: {', '.join(article_cves)}")

    heading = f"**{title}**"
    if metadata:
        heading = f"{heading} ({'; '.join(metadata)})"

    visible_content = get_prompt_visible_content(content)
    return f"{heading}\n\n{visible_content}\n\n"


def collect_structured_cves(article: Dict[str, Any]) -> list[str]:
    """Collect CVE IDs from structured article metadata."""
    values = article.get("cves", [])
    if values is None:
        values = []
    elif isinstance(values, str):
        values = [values]
    return [cve.upper() for cve in extract_cve_ids("\n".join(map(str, values)))]


def collect_prompt_cves(article_summary: str) -> list[str]:
    """Collect CVE IDs from the exact article text sent to the model."""
    return [cve.upper() for cve in extract_cve_ids(article_summary)]


def has_exploitation_relevance(article_summary: str) -> bool:
    """Return whether prompt-visible article text describes exploit activity."""
    return bool(EXPLOITATION_RELEVANCE_PATTERN.search(article_summary))


def has_negated_exploitation_relevance(article_summary: str) -> bool:
    """Return whether prompt-visible text negates exploitation activity."""
    relevant_clauses = [
        clause
        for clause in EXPLOITATION_CLAUSE_BOUNDARY_PATTERN.split(article_summary)
        if has_exploitation_relevance(clause)
    ]
    return bool(relevant_clauses) and all(
        NEGATED_EXPLOITATION_PATTERN.search(clause)
        or UNCONFIRMED_EXPLOITATION_PATTERN.search(clause)
        or POSTPOSED_NEGATED_EXPLOITATION_PATTERN.search(clause)
        for clause in relevant_clauses
    )


def normalize_cve_match(match: re.Match[str]) -> str:
    return f"CVE-{match.group(1)}-{match.group(2)}".upper()


def collect_structured_prompt_cves(article_summary: str) -> list[str]:
    structured_cves: list[str] = []
    for metadata_match in STRUCTURED_CVES_PATTERN.finditer(article_summary):
        structured_cves.extend(collect_prompt_cves(metadata_match.group(1)))
    return structured_cves


def collect_url_prompt_cves(article_summary: str) -> list[str]:
    url_cves: list[str] = []
    for url_match in URL_PATTERN.finditer(article_summary):
        url_cves.extend(collect_prompt_cves(url_match.group(0)))
    return url_cves


def iter_line_sentences(text: str) -> list[str]:
    sentences: list[str] = []
    for line in text.splitlines():
        for sentence_match in SENTENCE_PATTERN.finditer(line):
            sentence = sentence_match.group(0).strip()
            if sentence:
                sentences.append(sentence)
    return sentences


def strip_cve_metadata_noise(article_summary: str) -> str:
    without_urls = URL_PATTERN.sub("", article_summary)
    return STRUCTURED_CVES_PATTERN.sub("", without_urls)


def has_positive_exploitation_sentence(article_summary: str) -> bool:
    return any(
        has_exploitation_relevance(sentence)
        and not has_negated_exploitation_relevance(sentence)
        for sentence in iter_line_sentences(strip_cve_metadata_noise(article_summary))
    )


def has_positive_grouped_exploitation_clause(article_summary: str) -> bool:
    for sentence in iter_line_sentences(strip_cve_metadata_noise(article_summary)):
        for clause in EXPLOITATION_CLAUSE_BOUNDARY_PATTERN.split(sentence):
            if (
                GROUPED_ISSUES_PATTERN.search(clause)
                and has_exploitation_relevance(clause)
                and not has_negated_exploitation_relevance(clause)
            ):
                return True
    return False


def sentence_context_at_position(text: str, position: int) -> tuple[str, int]:
    line_start = text.rfind("\n", 0, position) + 1
    line_end = text.find("\n", position)
    if line_end == -1:
        line_end = len(text)

    line = text[line_start:line_end]
    line_position = position - line_start
    for sentence_match in SENTENCE_PATTERN.finditer(line):
        if sentence_match.start() <= line_position < sentence_match.end():
            return sentence_match.group(0), line_position - sentence_match.start()
    return line, line_position


def clause_containing_position(text: str, position: int) -> str:
    """Return the exploitation clause containing a character position."""
    clause_start = 0
    for boundary_match in EXPLOITATION_CLAUSE_BOUNDARY_PATTERN.finditer(text):
        if position < boundary_match.start():
            return text[clause_start : boundary_match.start()]
        clause_start = boundary_match.end()
    return text[clause_start:]


def collect_exploitation_relevant_prompt_cves(article_summary: str) -> list[str]:
    """Collect prompt CVEs that are tied to non-negated exploit activity."""
    cves: list[str] = []
    seen: set[str] = set()

    def add_cve(cve: str) -> None:
        normalized_cve = cve.upper()
        if normalized_cve in seen:
            return
        seen.add(normalized_cve)
        cves.append(normalized_cve)

    structured_cves = collect_structured_prompt_cves(article_summary)
    metadata_context_cves = structured_cves or collect_url_prompt_cves(article_summary)
    article_body = strip_cve_metadata_noise(article_summary)
    article_sentences = iter_line_sentences(article_body)
    body_has_positive_exploitation = has_positive_exploitation_sentence(article_body)
    contextless_cves: list[str] = []
    explicitly_negated_cves: set[str] = set()
    has_non_negated_cve_context = False
    for cve in metadata_context_cves:
        indexed_cve_sentences = []
        for index, sentence in enumerate(article_sentences):
            cve_clauses = [
                clause_containing_position(sentence, match.start())
                for match in CVE_CONTEXT_PATTERN.finditer(sentence)
                if normalize_cve_match(match) == cve.upper()
            ]
            if cve_clauses:
                indexed_cve_sentences.append((index, cve_clauses))
        if indexed_cve_sentences:
            cve_context_is_negated = all(
                has_negated_exploitation_relevance(clause)
                for _, clauses in indexed_cve_sentences
                for clause in clauses
            )
            has_non_negated_cve_context = (
                has_non_negated_cve_context or not cve_context_is_negated
            )
            if cve_context_is_negated:
                explicitly_negated_cves.add(cve.upper())
            nearby_sentences = []
            for index, cve_clauses in indexed_cve_sentences:
                nearby_sentences.extend(cve_clauses)
                if index:
                    preceding_sentence = article_sentences[index - 1]
                    if not collect_prompt_cves(
                        preceding_sentence
                    ) and FOLLOWING_CVE_REFERENCE_PATTERN.search(" ".join(cve_clauses)):
                        nearby_sentences.append(preceding_sentence)
                if index + 1 < len(article_sentences):
                    following_sentence = article_sentences[index + 1]
                    if not collect_prompt_cves(
                        following_sentence
                    ) and FOLLOWING_CVE_REFERENCE_PATTERN.search(following_sentence):
                        nearby_sentences.append(following_sentence)
            if not cve_context_is_negated and any(
                has_exploitation_relevance(sentence)
                and not has_negated_exploitation_relevance(sentence)
                for sentence in nearby_sentences
            ):
                add_cve(cve)
        else:
            contextless_cves.append(cve)

    if body_has_positive_exploitation:
        if has_positive_grouped_exploitation_clause(article_body):
            for cve in metadata_context_cves:
                if cve.upper() not in explicitly_negated_cves:
                    add_cve(cve)
        elif len(contextless_cves) == 1 and not has_non_negated_cve_context:
            add_cve(contextless_cves[0])

    for match in CVE_CONTEXT_PATTERN.finditer(article_body):
        cve_sentence, cve_position = sentence_context_at_position(
            article_body, match.start()
        )
        cve_context = clause_containing_position(cve_sentence, cve_position)
        if has_exploitation_relevance(
            cve_context
        ) and not has_negated_exploitation_relevance(cve_context):
            add_cve(normalize_cve_match(match))

    return cves


async def analyze_exploitation(
    articles: List[Dict[str, Any]], config: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Analyze exploitation-related articles

    Args:
        articles: List of article dictionaries with exploitation content
        config: Configuration dictionary

    Returns:
        Exploitation analysis report
    """
    logger.info(f"Analyzing exploitation in {len(articles)} articles")

    # Initialize the AI model through OpenCode.
    model_name = resolve_model(config)
    max_tokens = int(config.get("analysis", {}).get("max_tokens", 4000))
    try:
        validate_model(model_name)
        model_selection = parse_model_selection(model_name)
    except ValueError as e:
        logger.error(f"Invalid model configuration: {e}")
        return {
            "exploitation_report": f"# Error: Invalid Model\n\n{str(e)}",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "error": str(e),
        }

    # Prepare all article summaries
    all_article_summaries = []
    all_cves = set()
    all_systems = set()
    all_attack_vectors = set()

    for article in articles:
        article_summary = format_article_summary(article)
        all_article_summaries.append(article_summary)

        # Extract expected CVEs only when prompt text ties them to exploit activity.
        for cve in collect_exploitation_relevant_prompt_cves(article_summary):
            all_cves.add(cve)
        if "affected_systems" in article:
            for system in article.get("affected_systems", []):
                all_systems.add(system)
        if "attack_vectors" in article:
            for vector in article.get("attack_vectors", []):
                all_attack_vectors.add(vector)

    # Create a comprehensive prompt for exploitation analysis
    prompt = f"""
You're a cybersecurity expert specializing in vulnerability and exploitation analysis. Analyze the following security news articles to generate a comprehensive report on active exploitation.

Generate a report following this EXACT structure with professional markdown formatting:

# Exploitation Report

## Executive Summary

[Write two to three concise executive-readable paragraphs covering the most critical exploitation activity. Do not emit one long block of text. Only mention CVE IDs if they are explicitly provided in the articles. Do not mention when CVE IDs are missing or unavailable.]

## Active Exploitation Details

[For each actively exploited vulnerability, create a well-formatted subsection:

### Vulnerability Name
- **Description**: Detailed description of the vulnerability
- **Impact**: What attackers can achieve
- **Status**: Current exploitation status and patch availability
- **CVE ID**: [Only include this line if a CVE ID is mentioned in the articles]
]

## Affected Systems and Products

[Create a well-formatted bullet list:
- **Product/System Name**: Specific details about affected versions or components
- **Platform**: Description of affected platforms or environments
]

## Attack Vectors and Techniques

[Use clear formatting for attack methods:
- **Technique Name**: Description of how the attack works
- **Vector**: Specific attack vector details
]

## Threat Actor Activities

[Organize threat actor information clearly:
- **Actor/Group**: Activities and targeting details
- **Campaign**: Operation descriptions and impacts
]

Formatting requirements:
- Use proper markdown with **bold** for emphasis
- Create clear bullet points with good spacing
- Use ### for subsections within main sections
- Include the ## Executive Summary section and split it into multiple paragraphs
- Write professional, well-structured content
- Only mention CVE IDs when they are actually provided in the source articles
- Include every CVE ID extracted from the article metadata when it is relevant to exploitation details
- Do NOT mention missing or unavailable CVE information
- Do not leave Threat Actor Activities as a single stale-looking item when broader actor or campaign activity appears elsewhere in the report; include the relevant actor, campaign, or unknown-operator roll-ups grounded in the articles

Focus specifically on:
- Zero-day vulnerabilities being actively exploited
- Recently patched vulnerabilities that were exploited
- New attack vectors and techniques
- Critical vulnerabilities with high impact
- Notable threat actors and their activities

Here are the articles:

{"".join(all_article_summaries)}

Generate a well-formatted exploitation report following the structure above. Be comprehensive but only include CVE IDs when they are explicitly mentioned in the articles.
"""

    # Estimate token count for logging
    estimated_tokens = len(tokenizer.encode(prompt))
    logger.info(f"Estimated token count for analysis prompt: {estimated_tokens}")

    # Call the AI model
    try:
        client = build_model_client(
            timeout=max(120.0, float(max_tokens) / 20), max_tokens=max_tokens
        )
        exploitation_report = await client.generate(
            system_prompt="You are a cybersecurity threat hunter specializing in vulnerability exploitation analysis. Your task is to create a comprehensive report on current exploit activity based on recent security articles. Be extremely thorough in identifying ALL exploited vulnerabilities mentioned in the articles, including zero-days, active exploits, and recently patched vulnerabilities that were exploited in the wild.",
            user_prompt=prompt,
            model=model_selection,
            title="SentryInsight exploitation report",
        )

        return {
            "exploitation_report": exploitation_report,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "analyzed_article_count": len(articles),
            "cves_identified": list(all_cves),
        }
    except OpenCodeUnavailable as e:
        logger.warning(f"Skipping exploitation analysis: {e}")
        return {
            "exploitation_report": "",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "analyzed_article_count": len(articles),
            "cves_identified": list(all_cves),
            "skipped": True,
            "skip_reason": str(e),
        }
    except Exception as e:
        logger.error(f"Error during exploitation analysis: {e}")
        return {
            "exploitation_report": f"# Error Generating Exploitation Report\n\nAn error occurred during analysis: {str(e)}\n\n## Partial Data\n\nCVEs identified: {', '.join(all_cves) if all_cves else 'None'}\n\nAffected systems: {', '.join(all_systems) if all_systems else 'None'}",
            "date": datetime.now().strftime("%Y-%m-%d"),
            "error": str(e),
        }

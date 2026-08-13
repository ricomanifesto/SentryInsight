import logging
import re
from typing import List, Dict, Any
from datetime import datetime

import tiktoken

from .model_config import resolve_model, validate_model
from .model_client import build_model_client
from .opencode_client import OpenCodeUnavailable, parse_model_selection
from .cve import extract_cve_ids
from .prompt_content import (
    get_prompt_visible_content,
    normalize_prompt_metadata,
    normalize_prompt_source,
)

logger = logging.getLogger(__name__)

# Initialize tokenizer for token counting
tokenizer = tiktoken.get_encoding("cl100k_base")

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
CONFIRMED_EXPLOITATION_PATTERN = re.compile(
    r"\b(?:"
    r"active(?:ly)? exploit(?:s|ed|ing|ation)?|"
    r"attackers? (?:are )?exploit(?:s|ed|ing)?|"
    r"in the wild|"
    r"under attack"
    r")\b",
    re.IGNORECASE,
)
CVE_CONTEXT_PATTERN = re.compile(
    r"(?<![A-Za-z0-9])CVE[-\s]?(\d{4})[-\s]?(\d{4,})" r"(?![A-Za-z0-9]|\.\.\.|…)",
    re.IGNORECASE,
)
STRUCTURED_CVES_PATTERN = re.compile(r"CVEs:\s*([^)]*)", re.IGNORECASE)
GENERATED_HEADING_PATTERN = re.compile(
    r"^(?P<title>\*\*.*\*\*)\s+\((?P<metadata>.*)\)\s*$"
)
SENTENCE_PATTERN = re.compile(r"(?:[^.!?\n]|(?<=\d)\.(?=\d))+?(?:[!?]+|\.+(?!\d)|$)")
SENTENCE_ABBREVIATION_PATTERN = re.compile(r"\b(?:[A-Za-z]\.){2,}(?=\s+[a-z])")
SENTENCE_PERIOD_PLACEHOLDER = "\ue000"
URL_PATTERN = re.compile(r"https?://\S+", re.IGNORECASE)
NEGATED_EXPLOITATION_PATTERN = re.compile(
    r"\b(?:"
    r"no evidence(?:\s+(?:of|that))?|"
    r"neither\b.{0,120}\bnor|"
    r"no\s+(?:(?:known|confirmed|observed|active)\s+)?(?=exploit)|"
    r"(?:has|have|had)\s+never\s+been|"
    r"not\s+(?:all|both|these|the listed)\s+"
    r"(?:CVEs?|flaws?|issues?|vulnerabilit(?:y|ies))|"
    r"(?:(?:has|have|had|is|are|was|were)\s+)?not\s+"
    r"(?:(?:actively|currently|yet)\s+)*(?:(?:being|been)\s+)?"
    r"(?:(?:actively|currently)\s+)*(?=exploit)|"
    r"no\s+longer\s+(?:(?:actively|currently)\s+)*(?:being\s+)?(?=exploit)|"
    r"(?:can(?:not|'t|’t)|could(?:\s+not|n't|n’t)|unable\s+to|"
    r"(?:not\s+possible|impossible)\s+to)\s+(?:be\s+)?(?=exploit)|"
    r"without\s+(?:evidence|signs?|reports?)(?:\s+of)?|"
    r"has not been|"
    r"have not been|"
    r"not\s+(?:known|reported|observed)\s+to\s+(?:be|have\s+been)|"
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
    r"\b(?:alleged|believed|likely|possibly|potentially|reported|suspected|thought)"
    r"\s+to\s+(?:be\s+)?exploit(?:ed|ing)?\b|"
    r"\b(?:exploitation|exploit activity)\b[^,.;\n]{0,60}\b"
    r"(?:likely|suspected|unconfirmed|possible|potential)\b|"
    r"\b(?:proof[\s-]of[\s-]concept|PoC)\s+exploit\b|"
    r"\bexploit(?:s)?\s+(?:is|are)\s+(?:publicly\s+)?available\b|"
    r"\b(?:can|could|might|would|possible|potential(?:ly)?)\b[^,.;\n]{0,100}"
    r"\bexploit(?:ed|ing|ation)?\b|"
    r"\b(?:can|could|might|would|possible|potential(?:ly)?)\b[^,.;\n]{0,100}"
    r"\b(?:backdoor|malware)\b|"
    r"(?<!active )(?<!confirmed )(?<!observed )\bexploitation\s+of\b"
    r"[^,.;\n]{0,100}\b(?:can|could|may|might|would)\b(?=\s+"
    r"(?:(?:not|also|possibly|potentially|eventually|ultimately)\s+)*"
    r"(?:allow|cause|enable|expose|give|lead|permit|provide|result))|"
    r"\bmay\b(?=\s+(?:(?:not|also|possibly|potentially|eventually|ultimately)\s+)*"
    r"(?:be\s+)?(?:allow|cause|enable|exploit|expose|give|lead|permit|provide|result))"
    r"[^,.;\n]{0,100}"
    r"\bexploit(?:ed|ing|ation)?\b|"
    r"\b(?:if|when)\b.{0,100}\bexploit(?:ed|ing|ation)?\b|"
    r"\bindicative of\b.{0,100}\bexploit(?:ed|ing|ation)?\b|"
    r"\bnot enough evidence\b.{0,160}\b(?:exploit(?:ed|ing|ation)?|correlat)"
    r")",
    re.IGNORECASE | re.DOTALL,
)
GOVERNING_UNCERTAINTY_PATTERN = re.compile(
    r"\b(?:active(?:ly)?\s+)?(?:exploitation|exploit activity)\b"
    r"[^,.;\n]{0,60}\b(?:likely|suspected|unconfirmed|possible|potential)\b",
    re.IGNORECASE,
)
INTERROGATIVE_EXPLOITATION_PATTERN = re.compile(
    r"^[^?\n]{0,240}\b(?:"
    r"exploit(?:s|ed|ing|ation)?|"
    r"in the wild|"
    r"weaponiz(?:ed|ation)|"
    r"under attack"
    r")\b[^?\n]*\?",
    re.IGNORECASE,
)
GROUPED_ISSUES_PATTERN = re.compile(
    r"\b(?:"
    r"both(?=\s+(?:are|were|have|had|remain|continue)\b)|"
    r"(?:all|both|these|the listed)\s+"
    r"(?:CVEs?|flaws?|issues?|vulnerabilit(?:y|ies))|"
    r"the\s+(?:CVEs|flaws|issues|vulnerabilities)"
    r")\b",
    re.IGNORECASE,
)
EXPLOITATION_CLAUSE_BOUNDARY_PATTERN = re.compile(
    r"(?:"
    r"[;,]\s*(?=(?:attackers?|threat actors?|not\s+CVE-\d{4}-\d{4,}|"
    r"CVE-\d{4}-\d{4,}\s+(?:is|was|has)|"
    r"CVE-\d{4}-\d{4,}(?:\s*(?:,|and)\s*CVE-\d{4}-\d{4,})+"
    r"\s+(?:are|were|have))\b)|"
    r"\s+(?=and\s+(?:attackers?|threat actors?|researchers?|they|it|"
    r"the\s+(?:flaw|issue|vulnerability|bug))\b)|"
    r"\s+(?=and\s+CVE-\d{4}-\d{4,}\s+(?:is|was|has)\b)|"
    r"(?:[;,]\s*|\s+)(?=(?:but|however|while|whereas)\b|"
    r"yet\s+(?:attackers?|threat actors?|researchers?|they)\b)"
    r")",
    re.IGNORECASE,
)
FOLLOWING_CVE_REFERENCE_PATTERN = re.compile(
    r"\b(?:the|this|that|said)\s+(?:(?:affected|new|same)\s+)?"
    r"(?:flaw|issue|vulnerability|bug|zero[\s-]?day)\b|"
    r"\bit\b",
    re.IGNORECASE,
)
FOLLOWING_PLURAL_CVE_REFERENCE_PATTERN = re.compile(
    r"\b(?:they|both|(?:these|those|the)\s+"
    r"(?:flaws?|issues?|vulnerabilit(?:y|ies)|bugs?|zero[\s-]?days?))\b",
    re.IGNORECASE,
)
NEW_VULNERABILITY_REFERENT_PATTERN = re.compile(
    r"\b(?:(?:a|an)\s+(?:(?:different|new|separate|second|third)\s+)?|"
    r"(?:another|different|separate|second|third)\s+)"
    r"(?:flaw|issue|vulnerability|bug|zero[\s-]?day)\b",
    re.IGNORECASE,
)
FOLLOWING_REFERENCE_SENTENCE_LIMIT = 3


def clean_article_source(value: Any) -> str:
    return normalize_prompt_source(value)


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

    title = normalize_prompt_metadata(article.get("title")) or "Untitled article"
    source = clean_article_source(article.get("source"))
    link = normalize_prompt_metadata(article.get("link"))
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
        or INTERROGATIVE_EXPLOITATION_PATTERN.search(clause)
        or GOVERNING_UNCERTAINTY_PATTERN.search(clause)
        or (
            UNCONFIRMED_EXPLOITATION_PATTERN.search(clause)
            and not CONFIRMED_EXPLOITATION_PATTERN.search(clause)
        )
        or POSTPOSED_NEGATED_EXPLOITATION_PATTERN.search(clause)
        for clause in relevant_clauses
    )


def normalize_cve_match(match: re.Match[str]) -> str:
    return f"CVE-{match.group(1)}-{match.group(2)}".upper()


def get_generated_heading_metadata(article_summary: str) -> str:
    first_line = article_summary.partition("\n")[0]
    match = GENERATED_HEADING_PATTERN.fullmatch(first_line)
    return match.group("metadata") if match else ""


def collect_structured_prompt_cves(article_summary: str) -> list[str]:
    structured_cves: list[str] = []
    metadata = get_generated_heading_metadata(article_summary)
    for metadata_match in STRUCTURED_CVES_PATTERN.finditer(metadata):
        structured_cves.extend(collect_prompt_cves(metadata_match.group(1)))
    return structured_cves


def collect_url_prompt_cves(article_summary: str) -> list[str]:
    url_cves: list[str] = []
    metadata = get_generated_heading_metadata(article_summary)
    for url_match in URL_PATTERN.finditer(metadata):
        url_cves.extend(collect_prompt_cves(url_match.group(0)))
    return url_cves


def iter_line_sentences(text: str) -> list[str]:
    sentences: list[str] = []
    for line in text.splitlines():
        protected_line = SENTENCE_ABBREVIATION_PATTERN.sub(
            lambda match: match.group(0).replace(".", SENTENCE_PERIOD_PLACEHOLDER),
            line,
        )
        for sentence_match in SENTENCE_PATTERN.finditer(protected_line):
            sentence = (
                sentence_match.group(0)
                .replace(SENTENCE_PERIOD_PLACEHOLDER, ".")
                .strip()
            )
            if sentence:
                sentences.append(sentence)
    return sentences


def strip_cve_metadata_noise(article_summary: str) -> str:
    first_line, separator, remainder = article_summary.partition("\n")
    match = GENERATED_HEADING_PATTERN.fullmatch(first_line)
    if not match:
        return article_summary
    return match.group("title") + (separator + remainder if separator else "")


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
    protected_line = SENTENCE_ABBREVIATION_PATTERN.sub(
        lambda match: match.group(0).replace(".", SENTENCE_PERIOD_PLACEHOLDER),
        line,
    )
    for sentence_match in SENTENCE_PATTERN.finditer(protected_line):
        if sentence_match.start() <= line_position < sentence_match.end():
            return (
                sentence_match.group(0).replace(SENTENCE_PERIOD_PLACEHOLDER, "."),
                line_position - sentence_match.start(),
            )
    return line, line_position


def clause_containing_position(text: str, position: int) -> str:
    """Return the exploitation clause containing a character position."""
    clause_start = 0
    for boundary_match in EXPLOITATION_CLAUSE_BOUNDARY_PATTERN.finditer(text):
        if position < boundary_match.start():
            return text[clause_start : boundary_match.start()]
        clause_start = boundary_match.end()
    return text[clause_start:]


def following_clause_after_position(text: str, position: int) -> str:
    boundaries = list(EXPLOITATION_CLAUSE_BOUNDARY_PATTERN.finditer(text))
    for index, boundary in enumerate(boundaries):
        if position < boundary.start():
            clause_end = (
                boundaries[index + 1].start()
                if index + 1 < len(boundaries)
                else len(text)
            )
            return text[boundary.end() : clause_end]
    return ""


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
            has_positive_following_reference = False
            for index, cve_clauses in indexed_cve_sentences:
                nearby_sentences.extend(cve_clauses)
                sentence_has_multiple_cves = (
                    len(collect_prompt_cves(article_sentences[index])) > 1
                )
                if index:
                    preceding_sentence = article_sentences[index - 1]
                    if not collect_prompt_cves(
                        preceding_sentence
                    ) and FOLLOWING_CVE_REFERENCE_PATTERN.search(" ".join(cve_clauses)):
                        nearby_sentences.append(preceding_sentence)
                for following_sentence in article_sentences[
                    index + 1 : index + 1 + FOLLOWING_REFERENCE_SENTENCE_LIMIT
                ]:
                    if collect_prompt_cves(following_sentence):
                        break
                    if NEW_VULNERABILITY_REFERENT_PATTERN.search(following_sentence):
                        break
                    has_following_reference = bool(
                        FOLLOWING_CVE_REFERENCE_PATTERN.search(following_sentence)
                        or (
                            sentence_has_multiple_cves
                            and FOLLOWING_PLURAL_CVE_REFERENCE_PATTERN.search(
                                following_sentence
                            )
                        )
                    )
                    if not has_following_reference:
                        continue
                    nearby_sentences.append(following_sentence)
                    if has_exploitation_relevance(following_sentence):
                        has_positive_following_reference = (
                            has_positive_following_reference
                            or not has_negated_exploitation_relevance(
                                following_sentence
                            )
                        )
                        break
            if (not cve_context_is_negated or has_positive_following_reference) and any(
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
        following_clause = following_clause_after_position(cve_sentence, cve_position)
        following_reference = bool(
            FOLLOWING_CVE_REFERENCE_PATTERN.search(following_clause)
        )
        context_is_positive = has_exploitation_relevance(
            cve_context
        ) and not has_negated_exploitation_relevance(cve_context)
        following_reference_is_positive = (
            following_reference
            and has_exploitation_relevance(following_clause)
            and not has_negated_exploitation_relevance(following_clause)
        )
        following_reference_is_negative = (
            following_reference
            and has_exploitation_relevance(following_clause)
            and has_negated_exploitation_relevance(following_clause)
        )
        if following_reference_is_positive or (
            context_is_positive and not following_reference_is_negative
        ):
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

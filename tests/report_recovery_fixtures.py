"""Synthetic example.test fixtures for vendor link IDs and finding order.

Fictional publishers, titles and URLs only. No case reproduces a real
article, advisory, report or diagnostic record.
"""

from src.core.reporting import (
    build_reporting_catalog,
    reporting_key,
    serialize_reporting_catalog,
)
from src.core.source_review import PLAN_KEY, prepare_source_review
from src.core.vendor_link_references import link_id
from src.core.version_references import PROTOCOL_KEY, PROTOCOL_VERSION

ABSENT = "Not stated in supplied sources."
DATE = "2026-11-02"
GENERATED_AT = "2026-11-02T12:00:00Z"
ALPHA_ADVISORY = "https://vendor.example.test/advisory/alpha"
ALPHA_NOTES = "https://vendor.example.test/notes/alpha?id=one"
BETA_ADVISORY = "https://vendor.example.test/advisory/beta"
HELD_ADVISORY = "https://vendor.example.test/advisory/held"
# A legal URL that the semicolon field grammar cannot carry as one entry.
SEPARATOR_LINK = "https://vendor.example.test/advisory/alpha;revision=2"
# The held source's wording is an uncertain version claim, so review holds it.
HELD_CONTENT = "An attack vector targets instances running version 3.2 or earlier."


def news_url(name: str) -> str:
    return f"https://news.example.test/{name}"


def key_for(name: str) -> str:
    return reporting_key(news_url(name))


def article(name: str, links=(), content: str | None = None) -> dict:
    return {
        "title": f"Synthetic {name} advisory",
        "source": "Synthetic publisher",
        "link": news_url(name),
        "content": content or f"A {name} service advisory.",
        "content_kind": "article",
        "source_links": list(links),
    }


def id_for(name: str, url: str, articles=None) -> str:
    """The ID the host mints for this source's current content and URL."""
    articles = articles or [*standard_articles(), article("lonely")]
    source = build_reporting_catalog(articles)[key_for(name)]
    return link_id(source.key, source.content, url)


def finding(
    title: str,
    keys,
    *,
    severity: str = "unknown",
    vendor_links: str = ABSENT,
    description: str = "A campaign described by the supplied reporting.",
) -> str:
    return (
        f"### {title}\n"
        f"- **Description**: {description}\n"
        f"- **Severity**: {severity}\n"
        "- **Exploitation Status**: unknown\n"
        "- **Action**: monitor\n"
        f"- **Reporting**: {', '.join(keys)}\n"
        f"- **Affected Versions**: {ABSENT}\n"
        f"- **Exceptions**: {ABSENT}\n"
        f"- **Recommended Actions**: {ABSENT}\n"
        f"- **Vendor Links**: {vendor_links}\n\n"
    )


SUMMARY = (
    "The supplied reporting describes a campaign. Exploitation status is unknown.\n\n"
    "Review the source details before choosing a response.\n\n"
)
TRAILER = (
    "## Affected Systems and Products\n\n"
    "- Review the reporting for system details.\n\n"
    "## Attack Vectors and Techniques\n\n"
    "- Review the reporting for technique details.\n\n"
    "## Threat Actor Activities\n\n"
    "- The reported campaign requires further investigation.\n"
    "- Review the supplied reporting before assigning an actor.\n"
)


def report(findings: str, *, summary: str = SUMMARY, trailer: str = TRAILER) -> str:
    return (
        "# Exploitation Report\n\n## Executive Summary\n\n"
        + summary
        + "## Active Exploitation Details\n\n"
        + findings
        + trailer
    )


def prepared_result(articles, exploitation_report: str) -> dict:
    plan = prepare_source_review(articles)
    return {
        PLAN_KEY: plan.packet,
        "reporting_sources": serialize_reporting_catalog(plan.catalog),
        "reporting_metadata_cves": {
            row["key"]: row["metadata_cves"] for row in plan.packet["sources"]
        },
        PROTOCOL_KEY: PROTOCOL_VERSION,
        "exploitation_report": exploitation_report,
        "date": DATE,
        "generated_at": GENERATED_AT,
    }


def standard_articles() -> list[dict]:
    return [
        article("alpha", [ALPHA_ADVISORY, ALPHA_NOTES, SEPARATOR_LINK]),
        article("beta", [BETA_ADVISORY]),
        article("held", [HELD_ADVISORY], content=HELD_CONTENT),
    ]

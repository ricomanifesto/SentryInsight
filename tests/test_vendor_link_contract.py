"""The prompt and the vendor-link check state the same rule.

A vendor link is accepted only when it is a supplied Source link of an
article the finding cites. The prompt must say so, because every article in
the prompt lists its own Source links and a link copied from an uncited
article is rejected before publication.
"""

from src.core.exploitation_prompt import build_exploitation_prompt
from src.core.finding_evidence import EvidenceError, validate_vendor_links
from src.core.reporting import build_reporting_catalog, reporting_key
from src.core.source_review import prepare_source_review

import pytest

CVE = "CVE-2026-1234"


def article(name):
    return {
        "title": f"{name} advisory for {CVE}",
        "source": name,
        "link": f"https://{name}.example/news",
        "content": f"{CVE} is actively exploited. Install the update.",
        "source_links": [f"https://{name}.example/advisory"],
    }


def report(keys, link):
    return (
        "## Active Exploitation Details\n\n"
        f"### Gateway ({CVE})\n"
        f"- **CVE IDs**: {CVE}\n"
        f"- **Reporting**: {', '.join(keys)}\n"
        f"- **Vendor Links**: {link}\n"
    )


def test_the_prompt_limits_vendor_links_to_cited_articles():
    plan = prepare_source_review([article("alpha"), article("beta")])
    prompt = build_exploitation_prompt(plan)
    assert (
        "Source links of the articles cited in this finding's Reporting field" in prompt
    )
    assert "a link supplied only by an uncited article is rejected" in prompt


def test_a_link_from_an_uncited_article_is_rejected_and_citing_it_passes():
    articles = [article("alpha"), article("beta")]
    catalog = build_reporting_catalog(articles)
    alpha, beta = (reporting_key(a["link"]) for a in articles)
    beta_link = "https://beta.example/advisory"

    with pytest.raises(EvidenceError) as rejected:
        validate_vendor_links(report([alpha], beta_link), catalog)
    assert rejected.value.code == "unsupported_vendor_link"
    validate_vendor_links(report([alpha, beta], beta_link), catalog)

"""Host-owned source coverage, separate from every asserted finding."""

import html
import json
import re
from typing import Any, Sequence

from markdown_it import MarkdownIt
from .heading_identity import normalize_heading_identity
from .report_validation import inline_token_plain_text

from .source_review import (
    SourceReviewError,
    canonical_json,
    digest,
    validate_review_packet,
)

COVERAGE_HEADING = "## Source Coverage and Review"


def visible_candidate_text(report: str, *, reject_host_namespace: bool = False) -> str:
    """Match rendered inline identities without joining unrelated block text.

    The site uses CommonMark and removes raw HTML tokens. Inline text therefore
    stays adjacent through emphasis, links and removed tags, while separate
    blocks retain a boundary. Check both the site's raw heading slug and the
    visible heading identity so encoded/formatted headings cannot impersonate
    its host-owned coverage anchor or label.
    """
    tokens = MarkdownIt("commonmark", {"html": True}).parse(report)
    visible = []
    reserved = normalize_heading_identity(COVERAGE_HEADING)
    for index, token in enumerate(tokens):
        if token.type == "inline":
            visible.append(inline_token_plain_text(token))
        elif token.type in {"code_block", "fence"}:
            visible.append(token.content)
        if reject_host_namespace and token.type == "heading_open":
            inline = tokens[index + 1]
            identities = {
                normalize_heading_identity(inline.content),
                normalize_heading_identity(inline_token_plain_text(inline)),
            }
            if reserved in identities:
                raise SourceReviewError("model_supplied_coverage")
    text = "\n\n".join(visible)
    if reject_host_namespace and re.search(
        r"^\s*(?:source_coverage|source_review_plan|schema_version)\s*:",
        report + "\n" + text,
        re.M | re.I,
    ):
        raise SourceReviewError("model_supplied_coverage")
    return text


def _require(condition: bool) -> None:
    if not condition:
        raise SourceReviewError("invalid_source_coverage")


def _counts(plan: dict[str, Any], cited: Sequence[str]) -> dict[str, int]:
    rows = plan["sources"]
    eligible = sum(row["state"] == "eligible" for row in rows)
    return {
        "input_sources": len(rows),
        "eligible_sources": eligible,
        "cited_sources": len(cited),
        "review_required_sources": sum(
            row["state"] == "review_required" for row in rows
        ),
        "rejected_sources": sum(row["state"] == "source_rejected" for row in rows),
        "unrepresented_eligible_sources": eligible - len(cited),
    }


def make_source_coverage(
    plan: dict[str, Any], cited_keys: Sequence[str]
) -> dict[str, Any]:
    validate_review_packet(plan)
    cited = sorted(set(cited_keys))
    coverage: dict[str, Any] = {
        "schema_version": 1,
        "plan": plan,
        "cited_source_keys": cited,
        "counts": _counts(plan, cited),
    }
    coverage["coverage_id"] = digest(coverage)
    return validate_source_coverage(coverage)


def validate_source_coverage(coverage: Any) -> dict[str, Any]:
    _require(isinstance(coverage, dict))
    _require(
        set(coverage)
        == {"schema_version", "plan", "cited_source_keys", "counts", "coverage_id"}
    )
    _require(
        type(coverage["schema_version"]) is int and coverage["schema_version"] == 1
    )
    plan = validate_review_packet(coverage["plan"])
    cited = coverage["cited_source_keys"]
    _require(
        isinstance(cited, list)
        and bool(cited)
        and all(isinstance(key, str) for key in cited)
    )
    _require(cited == sorted(set(cited)))
    eligible = {row["key"] for row in plan["sources"] if row["state"] == "eligible"}
    _require(set(cited) <= eligible)
    counts = coverage["counts"]
    _require(
        isinstance(counts, dict)
        and all(type(value) is int for value in counts.values())
    )
    _require(counts == _counts(plan, cited))
    _require(
        coverage["coverage_id"]
        == digest({k: v for k, v in coverage.items() if k != "coverage_id"})
    )
    return coverage


def parse_source_coverage(value: str) -> dict[str, Any]:
    try:
        coverage = json.loads(value)
    except (ValueError, RecursionError):
        raise SourceReviewError("invalid_source_coverage") from None
    _require(canonical_json(coverage) == value)
    return validate_source_coverage(coverage)


def _label(value: str) -> str:
    # This text is an article label, not generated report prose or active HTML.
    return re.sub(r"([\\`*_{}\[\]()#+.!|~-])", r"\\\1", html.escape(value))


def source_disposition(row: dict[str, Any], cited: Sequence[str]) -> str:
    if row["state"] == "eligible":
        return (
            "Cited in validated findings"
            if row["key"] in cited
            else "Eligible input; not represented"
        )
    if row["direct_state"] == "eligible":
        return "Held with related source evidence"
    return (
        "Awaiting human review"
        if row["state"] == "review_required"
        else "Rejected by source validation"
    )


def coverage_markdown(coverage: dict[str, Any]) -> str:
    validate_source_coverage(coverage)
    counts = coverage["counts"]
    partial = counts["cited_sources"] < counts["input_sources"]
    lines = [
        COVERAGE_HEADING,
        "",
        "**Partial source coverage.**" if partial else "**Source coverage.**",
        (
            f"This report cites {counts['cited_sources']} of {counts['input_sources']} input sources. "
            f"Eligible model inputs: {counts['eligible_sources']}. "
            f"Sources awaiting review: {counts['review_required_sources']}. "
            f"Sources rejected by validation: {counts['rejected_sources']}. "
            f"Eligible sources not represented: {counts['unrepresented_eligible_sources']}."
        ),
        "",
        "These are source counts, not finding counts. Held or rejected sources do not establish findings. "
        "An unrepresented source has not been declared irrelevant or reviewed. "
        "This report covers the eligible evidence, not a complete product advisory.",
        "",
        "Linked labels below are article titles, not asserted report findings.",
        "",
        "| Source article | Disposition |",
        "| --- | --- |",
    ]
    for row in coverage["plan"]["sources"]:
        label = _label(row["publisher"] + " — " + row["title"])
        state = source_disposition(row, coverage["cited_source_keys"])
        lines.append(f"| [{label}](<{row['url']}>) | {state} |")
    return "\n".join(lines) + "\n"


def split_source_coverage(body: str, coverage: dict[str, Any]) -> str:
    """Remove only the exact host-owned suffix, never arbitrary coverage prose."""
    suffix = coverage_markdown(coverage).rstrip()
    normalized = body.rstrip()
    _require(normalized.endswith("\n\n" + suffix))
    report = normalized[: -len(suffix)].rstrip()
    visible_candidate_text(report, reject_host_namespace=True)
    return report + "\n"


def coverage_notice_html(coverage: dict[str, Any]) -> str:
    validate_source_coverage(coverage)
    counts = coverage["counts"]
    heading = (
        "Partial source coverage"
        if counts["cited_sources"] < counts["input_sources"]
        else "Source coverage"
    )
    return (
        '<p id="source-coverage-notice" class="vendor-guidance" role="note">'
        f"<strong>{heading}.</strong> "
        f"{counts['cited_sources']} of {counts['input_sources']} input sources are cited. "
        f"{counts['review_required_sources']} await review; {counts['rejected_sources']} failed source validation. "
        '<a href="#source-coverage-and-review">Review source dispositions</a>.</p>'
    )


def coverage_html(coverage: dict[str, Any]) -> str:
    """Controlled markup: all source labels/URLs are escaped, never parsed as HTML."""
    validate_source_coverage(coverage)
    counts = coverage["counts"]
    parts = [
        '<section aria-labelledby="source-coverage-and-review">',
        '<h2 id="source-coverage-and-review">Source Coverage and Review</h2>',
        f"<p>Eligible model inputs: {counts['eligible_sources']}. Eligible sources not represented: "
        f"{counts['unrepresented_eligible_sources']}.</p>",
        "<p>These are source counts, not finding counts. Held or rejected sources do not establish findings. "
        "An unrepresented source has not been declared irrelevant or reviewed. "
        "This report covers the eligible evidence, not a complete product advisory.</p>",
        '<table width="100%"><caption>Linked article titles and source dispositions</caption>'
        '<thead><tr><th scope="col">Source article</th><th scope="col">Disposition</th></tr></thead><tbody>',
    ]
    for row in coverage["plan"]["sources"]:
        label = html.escape(row["publisher"] + " — " + row["title"])
        url = html.escape(row["url"], quote=True)
        state = source_disposition(row, coverage["cited_source_keys"])
        parts.append(f'<tr><td><a href="{url}">{label}</a></td><td>{state}</td></tr>')
    parts.append("</tbody></table></section>")
    return "\n".join(parts)

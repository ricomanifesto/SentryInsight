"""Frozen independently expected projection and cache identity before edits."""

import copy
import hashlib
import itertools
from dataclasses import asdict
import httpx
import pytest
from src.core.relations import OwnedClause, EvidenceReporter
from src.core.content_fingerprint import compute_articles_fingerprint
from src.core.reporting import build_reporting_catalog
from src.core.assertions import parse_assertions
from src.core.finding_evidence import validate_finding_evidence, EvidenceError
from src.services.article_content import extract_article_content
from test_assertion_subject_contract import publish
from test_owned_relation_contract import article
from test_finding_generation_pipeline import run_real_pipeline, REPRESENTATIVE_ARTICLES

A = "CVE-2026-1234"
REPORTERS = {
    "direct": None,
    "positive": EvidenceReporter("Vendor", "has found evidence", "affirmative"),
    "negative": EvidenceReporter("Vendor", "has not found evidence", "negative"),
    "past_absence": EvidenceReporter(
        "Vendor", "had not found evidence", "negative", as_of="at publication"
    ),
    "qualified_positive": EvidenceReporter(
        "Vendor", "said", "affirmative", "denied report"
    ),
    "qualified_negative": EvidenceReporter(
        "Vendor", "has not found evidence", "negative", "double negation"
    ),
}
# Literal independent base table; no production constants or helpers derive it.
TABLE = {
    ("direct", "affirmative", ""): ["active", "observed", None],
    ("direct", "negative", ""): ["not_observed"] * 3,
    ("direct", "affirmative", "possible"): ["potential"] * 3,
    ("direct", "negative", "possible"): ["unknown"] * 3,
    ("negative", "affirmative", ""): ["not_observed"] * 3,
    ("negative", "negative", ""): ["unknown"] * 3,
    ("negative", "affirmative", "possible"): ["unknown"] * 3,
    ("negative", "negative", "possible"): ["unknown"] * 3,
}
ROWS = []
for reporter, polarity, modal, conditional, tense in itertools.product(
    REPORTERS,
    ["affirmative", "negative"],
    ["", "possible", "unknown"],
    [False, True],
    ["current", "past", "unspecified"],
):
    qualified = reporter.startswith("qualified")
    family = "negative" if reporter in ("negative", "past_absence") else "direct"
    expected = (
        "unknown"
        if qualified or conditional or modal == "unknown"
        else TABLE[(family, polarity, modal)][
            ["current", "past", "unspecified"].index(tense)
        ]
    )
    ROWS.append(
        dict(
            reporter=reporter,
            polarity=polarity,
            modal=modal,
            conditional=conditional,
            tense=tense,
            expected=expected,
        )
    )


@pytest.mark.parametrize(
    "row", ROWS, ids=lambda r: "-".join(str(v) for v in r.values())
)
def test_total_projection(row):
    reporter = REPORTERS[row["reporter"]]
    for finite in (False, True):
        clause = OwnedClause(
            kind="assertion",
            modal=row["modal"],
            polarity=row["polarity"],
            tense=row["tense"],
            conditions=("if reports are accurate",) if row["conditional"] else (),
            reporter=reporter,
            finite=finite,
        )
        assert clause.assertion_status == row["expected"]
        assert clause.reporter == reporter


@pytest.mark.parametrize(
    "field,value", [("modal", "invented"), ("tense", "future"), ("polarity", "mixed")]
)
@pytest.mark.parametrize("qualified", [False, True])
def test_invalid_state_is_not_rescued(field, value, qualified):
    data = dict(
        kind="assertion",
        tense="current",
        polarity="negative",
        conditions=("if reports are accurate",) if qualified else (),
    )
    data[field] = value
    assert OwnedClause(**data).assertion_status is None


@pytest.mark.parametrize(
    "kind,unsupported", [("context", False), ("directive", False), ("assertion", True)]
)
def test_nonassertion_or_unsupported_has_no_projection(kind, unsupported):
    assert (
        OwnedClause(
            kind=kind,
            unsupported=unsupported,
            tense="current",
            polarity="negative",
            modal="possible",
        ).assertion_status
        is None
    )


SENTENCES = [
    (f"Attackers might not be actively exploiting {A}.", "unknown"),
    (f"{A} might not be actively exploited.", "unknown"),
    (f"It is possible that {A} is not actively exploited.", "unknown"),
    (
        f"The vendor has not found evidence that attackers might be exploiting {A}.",
        "unknown",
    ),
    (
        f"The vendor has not found evidence that attackers are not exploiting {A}.",
        "unknown",
    ),
    (
        f"The vendor has not found evidence that attackers might not be exploiting {A}.",
        "unknown",
    ),
    (
        f"The vendor has found evidence that attackers might not be exploiting {A}.",
        "unknown",
    ),
    (
        f"The vendor had not found evidence that attackers were exploiting {A} at the time of publication.",
        "unknown",
    ),
    (
        f"The vendor has found evidence that attackers are not exploiting {A}.",
        "not_observed",
    ),
    (
        f"The vendor has found evidence that attackers were exploiting {A} yesterday.",
        "observed",
    ),
    (f"The vendor has found evidence that attackers are exploiting {A}.", "active"),
    (
        f"The vendor has found evidence that attackers might be exploiting {A}.",
        "potential",
    ),
    (
        f"If reports are accurate, the vendor has not found evidence that attackers are exploiting {A}.",
        "unknown",
    ),
    (
        f"The vendor has not found no evidence that attackers are exploiting {A}.",
        "unknown",
    ),
    (
        f"{A} might not only be actively exploited but also is weaponized in the wild.",
        "potential",
    ),
    ("Attackers might not be exploiting the gateway.", "unknown"),
    (f"Attackers might not be exploiting {A} and CVE-2026-5678.", "unknown"),
]


@pytest.fixture(autouse=True)
def no_transport(monkeypatch):
    def forbidden(*args, **kwargs):
        raise AssertionError("Real transport forbidden")

    monkeypatch.setattr(httpx.Client, "send", forbidden)
    monkeypatch.setattr(httpx.AsyncClient, "send", forbidden)


@pytest.mark.parametrize("text,expected", SENTENCES)
def test_actual_graph_projection(monkeypatch, tmp_path, text, expected):
    from src.core.cve import extract_cve_ids

    ids = extract_cve_ids(text)
    clauses = parse_assertions(text)
    assert not any(c.unsupported for c in clauses)
    findings = publish(monkeypatch, tmp_path, text, ids, [expected])
    assert len(findings) == 1
    report = (tmp_path / "index.md").read_text()
    if expected == "unknown":
        damaged = report.replace(
            "**Exploitation Status**: unknown", "**Exploitation Status**: not_observed"
        )
        with pytest.raises(EvidenceError):
            validate_finding_evidence(
                damaged,
                build_reporting_catalog(
                    [article(text, cves=ids)]
                    + [
                        article(
                            f"Attackers are actively exploiting {c}.",
                            link=f"https://example.test/{c}",
                        )
                        for c in ["CVE-2026-9998", "CVE-2026-9999"]
                    ]
                ),
            )


def structured(markup="<p>CVE-2026-1234 is actively exploited.</p>"):
    x = extract_article_content(
        "<article>" + markup + "</article>", "https://example.test/story"
    )
    return dict(
        title="Security report",
        source="Publisher",
        link="https://example.test/story",
        content=x.text,
        content_kind="article",
        content_format="text",
        source_blocks=[asdict(b) for b in x.blocks],
        source_links=list(x.links),
        source_link_contexts=[asdict(link) for link in x.link_contexts],
    )


IDENTITY = []


def pair(name, before, after, equal=False):
    IDENTITY.append(dict(name=name, before=before, after=after, equal=equal))


base = structured()
for field, value in [("kind", "quotation"), ("kind", "context")]:
    changed = copy.deepcopy(base)
    changed["source_blocks"][0][field] = value
    pair("block-" + value, [base], [changed])
pair("blocks-added", [{**base, "source_blocks": []}], [base])
heading = structured(
    "<h2>CVE-2026-1234</h2><p>CVE-2026-1234 is actively exploited.</p>"
)
changed = copy.deepcopy(heading)
changed["source_blocks"][0]["level"] = 3
pair("heading-level", [heading], [changed])
listing = structured("<ul><li>CVE-2026-1234 is actively exploited.</li></ul>")
changed = copy.deepcopy(listing)
changed["source_blocks"][0]["list_id"] += 1
pair("list-owner", [listing], [changed])
table = structured("<table><tr><td>Gateway</td><td>2.0</td></tr></table>")
for field, value in [("table", 9), ("header", True), ("cells", ("Gate", "way2.0"))]:
    changed = copy.deepcopy(table)
    changed["source_blocks"][0][field] = value
    pair("table-" + field, [table], [changed])
linked = structured(
    '<p>See <a href="https://vendor.example/advisory">security advisory</a> for CVE-2026-1234.</p>'
)
for field, value in [
    ("label", "vendor security advisory"),
    ("context", "CVE-2026-5678 security advisory"),
    ("url", "https://vendor.example/other"),
]:
    changed = copy.deepcopy(linked)
    changed["source_link_contexts"][0][field] = value
    pair("link-" + field, [linked], [changed])
for field, value in [
    ("title", "Changed title"),
    ("source", "Other publisher"),
    ("cves", ["CVE-2026-5678"]),
    ("content_kind", "feed"),
]:
    pair("metadata-" + field, [base], [{**base, field: value}])
other = {**linked, "link": "https://example.test/other-story"}
pair("source-order", [base, other], [other, base], True)
pair("exact-duplicates", [base], [base, base], True)
pair("unused-date", [base], [{**base, "date": "2099-01-01"}], True)
pair("dictionary-order", [base], [dict(reversed(list(base.items())))], True)
pair(
    "raw-feed-equivalence",
    [
        dict(
            title="Payload report",
            source="Publisher",
            link="https://example.test/literal",
            content="<p>Payload: &lt;script&gt;example&lt;/script&gt;.</p>",
        )
    ],
    [
        dict(
            title="Payload report",
            source="Publisher",
            link="https://example.test/literal",
            content="Payload: <script>example</script>.",
            content_format="text",
        )
    ],
    True,
)


@pytest.mark.parametrize("row", IDENTITY, ids=lambda r: r["name"])
def test_semantic_input_identity(row):
    for side in ("before", "after"):
        build_reporting_catalog(row[side])
    assert (
        compute_articles_fingerprint(row["before"])
        == compute_articles_fingerprint(row["after"])
    ) is row["equal"]


NAMES = (
    "index.md",
    "index.html",
    "current-findings.json",
    ".sentryinsight-articles-fingerprint",
)


@pytest.mark.parametrize(
    "change", ["structure", "unsupported_structure", "link_context", "unchanged"]
)
def test_actual_graph_cache_boundary(monkeypatch, tmp_path, change):
    inputs = copy.deepcopy(REPRESENTATIVE_ARTICLES)
    if change == "structure":
        inputs = [structured()] + [
            article(
                f"Attackers are actively exploiting {cve}.",
                link=f"https://example.test/{cve}",
            )
            for cve in ["CVE-2026-9998", "CVE-2026-9999"]
        ]
    first = run_real_pipeline(monkeypatch, tmp_path / "index.md", articles=inputs)
    assert first["status"] == "completed"
    previous = {n: (tmp_path / n).read_bytes() for n in NAMES}
    changed = copy.deepcopy(inputs)
    if change == "structure":
        changed[0]["source_blocks"][0]["kind"] = "quotation"
    elif change == "unsupported_structure":
        content = changed[0]["content"]
        digest = hashlib.sha256(content.encode()).hexdigest()
        changed[0]["source_blocks"] = [
            dict(
                start=0,
                end=len(content),
                text=content,
                text_sha256=digest,
                kind="paragraph",
            )
        ]
    elif change == "link_context":
        changed[0]["source_link_contexts"][0]["label"] = "security advisory"
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=changed,
        expect_model_call=change not in {"unchanged", "unsupported_structure"},
    )
    if change == "unsupported_structure":
        assert result["status"] == "failed", result
        assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
        assert all((tmp_path / n).read_bytes() == v for n, v in previous.items())
        return
    assert result["status"] == (
        "completed_unchanged" if change == "unchanged" else "completed"
    )
    if change == "unchanged":
        assert all((tmp_path / n).read_bytes() == v for n, v in previous.items())
    else:
        assert (tmp_path / NAMES[-1]).read_bytes() != previous[NAMES[-1]]


@pytest.mark.parametrize(
    "field,value", [("text_sha256", "0" * 64), ("start", True), ("end", 999999)]
)
def test_invalid_structure_cannot_hide_behind_cached_hash(
    monkeypatch, tmp_path, field, value
):
    inputs = [structured()]
    prior = {n: b"Previous validated artifact" for n in NAMES}
    prior[NAMES[-1]] = (compute_articles_fingerprint(inputs) + "\n").encode()
    for n, data in prior.items():
        (tmp_path / n).write_bytes(data)
    inputs[0]["source_blocks"][0][field] = value
    result = run_real_pipeline(
        monkeypatch, tmp_path / "index.md", articles=inputs, expect_model_call=False
    )
    assert result["status"] == "failed", result
    assert result["analysis_results"]["error"] == "invalid_retained_source"
    assert all((tmp_path / n).read_bytes() == v for n, v in prior.items())


@pytest.mark.parametrize(
    "text",
    [
        f"Attackers might not be exploiting {A} and consider exploiting CVE-2026-5678.",
        f"The vendor has not found evidence that attackers can continue to exploit {A}.",
        f"Attackers do not continue to exploit {A}.",
    ],
)
def test_unknown_relation_remains_terminal(monkeypatch, tmp_path, text):
    for n in NAMES:
        (tmp_path / n).write_bytes(b"Previous validated artifact")
    result = run_real_pipeline(
        monkeypatch,
        tmp_path / "index.md",
        articles=[article(text)],
        expect_model_call=False,
    )
    assert result["status"] == "failed"
    assert result["analysis_results"]["error"] == "unsupported_evidence_relation"
    assert all(
        (tmp_path / n).read_bytes() == b"Previous validated artifact" for n in NAMES
    )


@pytest.mark.parametrize("qualified", [False, True])
def test_unknown_reporter_polarity_cannot_establish_a_state(qualified):
    clause = OwnedClause(
        kind="assertion",
        tense="current",
        conditions=("if reports are accurate",) if qualified else (),
        reporter=EvidenceReporter("Vendor", "reported", "unclassified"),
    )
    assert clause.assertion_status is None


@pytest.mark.parametrize("repeat_first", [False, True])
def test_conflicting_same_source_versions_retain_order(repeat_first):
    first = structured()
    second = {**first, "title": "A different version of this source"}
    original = [first, second]
    changed = [first, second, first] if repeat_first else [second, first]
    assert compute_articles_fingerprint(original) != compute_articles_fingerprint(
        changed
    )


def test_recursive_list_ownership_participates_in_identity():
    first = structured("<ul><li>Gateway flaws<ul><li>CVE-2026-1234</li></ul></li></ul>")
    second = copy.deepcopy(first)
    second["source_blocks"][0]["children"][0]["list_id"] = 1
    build_reporting_catalog([first])
    build_reporting_catalog([second])
    assert compute_articles_fingerprint([first]) != compute_articles_fingerprint(
        [second]
    )


def test_prepared_source_is_shared_without_reinterpreting_literal_data(monkeypatch):
    from src.core import reporting

    original = structured(
        "<p>Payload: &lt;script&gt;example&lt;/script&gt; &amp;amp;.</p>"
    )
    prepared = reporting.prepare_reporting_input(original)
    before = compute_articles_fingerprint([original])

    def forbidden(*_, **__):
        raise AssertionError("Prepared evidence must not reenter raw extraction")

    monkeypatch.setattr(reporting, "reporting_content", forbidden)
    source = next(iter(build_reporting_catalog([prepared]).values()))
    summary = reporting.format_article_summary(prepared)
    assert (
        source.content == prepared.content == "Payload: <script>example</script> &amp;."
    )
    assert source.content in summary
    assert (
        source.blocks == prepared.blocks
        and source.link_contexts == prepared.link_contexts
    )
    assert compute_articles_fingerprint([prepared]) == before


@pytest.mark.parametrize(
    "field,value",
    [
        ("source_links", "https://example.test/invalid-type"),
        ("source_link_contexts", [42]),
        ("source_link_contexts", [{"url": "javascript:invalid"}]),
    ],
)
def test_invalid_link_evidence_cannot_take_unchanged_branch(
    monkeypatch, tmp_path, field, value
):
    inputs = [structured()]
    prior = {name: b"Previous validated artifact" for name in NAMES}
    prior[NAMES[-1]] = (compute_articles_fingerprint(inputs) + "\n").encode()
    for name, data in prior.items():
        (tmp_path / name).write_bytes(data)
    inputs[0][field] = value
    result = run_real_pipeline(
        monkeypatch, tmp_path / "index.md", articles=inputs, expect_model_call=False
    )
    assert result["status"] == "failed", result
    assert result["analysis_results"]["error"] == "invalid_retained_source"
    assert all((tmp_path / name).read_bytes() == data for name, data in prior.items())

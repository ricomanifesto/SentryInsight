"""Source-owned vendor selection, with no repair of unsupported output."""

import json
from pathlib import Path

import pytest

from src.core.finding_evidence import ABSENT, EvidenceError, validate_vendor_links
from src.core.reporting import build_reporting_catalog, split_vendor_urls
from src.core.vendor_references import (
    PROTOCOL_KEY,
    PROTOCOL_VERSION,
    build_vendor_reference_context,
    resolve_analysis_vendor_references,
    resolve_vendor_references,
)
from src.core.validation_diagnostics import validation_diagnostic
from src.core.report_artifact import parse_report_artifact
from test_report_artifact import REPORT
from test_vendor_link_contract import article, report


def catalog(*articles):
    return build_reporting_catalog(articles or [article("alpha")])


def selection(c):
    return build_vendor_reference_context(c)[0]["id"]


def test_reference_resolves_exact_source_link_and_preserves_absence():
    c = catalog()
    resolved = resolve_vendor_references(report(c, selection(c)), c)
    assert "Vendor Links**: https://alpha.example/advisory" in resolved
    validate_vendor_links(resolved, c)
    raw = report(c, ABSENT)
    assert resolve_vendor_references(raw, c) == raw


@pytest.mark.parametrize(
    "value,code",
    [
        ("vendor-" + "0" * 32, "unsupported_vendor_reference"),
        ("vendor-fake", "invalid_vendor_reference"),
        ("https://alpha.example/advisory", "invalid_vendor_reference"),
        ("Unresolved from supplied sources.", "invalid_vendor_reference"),
        ("", "invalid_vendor_reference"),
    ],
)
def test_invalid_choices_never_become_absence(value, code):
    c = catalog()
    with pytest.raises(EvidenceError) as err:
        resolve_vendor_references(report(c, value), c)
    assert err.value.code == code
    diagnostic = validation_diagnostic("finding_evidence", err.value)
    assert diagnostic["codes"] == [code]
    assert "https://" not in json.dumps(diagnostic)


@pytest.mark.parametrize("change", ["content", "remove", "url", "source"])
def test_stale_references_are_rejected(change):
    a = article("alpha")
    old = catalog(a)
    ref = selection(old)
    if change == "content":
        a["content"] += " New evidence."
    elif change == "remove":
        a["source_links"] = []
    elif change == "url":
        a["source_links"] = [a["source_links"][0] + "?new=1"]
    else:
        a["link"] += "/changed"
    new = catalog(a)
    with pytest.raises(EvidenceError, match="unsupported_vendor_reference"):
        resolve_vendor_references(report(new, ref), new)


def test_uncited_source_id_is_rejected_even_when_url_is_identical():
    a, b = article("alpha"), article("beta")
    b["source_links"] = a["source_links"]
    c = catalog(a, b)
    keys = list(c)
    ref = next(
        r["id"] for r in build_vendor_reference_context(c) if r["source_key"] == keys[1]
    )
    with pytest.raises(EvidenceError, match="unsupported_vendor_reference"):
        resolve_vendor_references(report([keys[0]], ref), c)


@pytest.mark.parametrize("same_url", [False, True])
def test_duplicate_tokens_or_resolved_urls_rejected(same_url):
    a, b = article("alpha"), article("beta")
    b["source_links"] = a["source_links"]
    c = catalog(a, b)
    refs = [r["id"] for r in build_vendor_reference_context(c)]
    value = "; ".join(refs if same_url else [refs[0], refs[0]])
    with pytest.raises(EvidenceError, match="duplicate_vendor_reference"):
        resolve_vendor_references(report(c, value), c)


@pytest.mark.parametrize("marker", [None, True, 0, 2, "1"])
def test_live_protocol_cannot_be_omitted_or_tampered(marker):
    c = catalog()
    result = {} if marker is None else {PROTOCOL_KEY: marker}
    with pytest.raises(EvidenceError, match="Invalid vendor reference protocol"):
        resolve_analysis_vendor_references(result, report(c, ABSENT), c)
    assert resolve_analysis_vendor_references(
        {PROTOCOL_KEY: PROTOCOL_VERSION}, report(c, ABSENT), c
    ) == report(c, ABSENT)


@pytest.mark.parametrize(
    "url",
    [
        "https://vendor.example/advisory;version=1",
        "https://vendor.example/advisory?q=a;b",
        "https://vendor.example/advisory?next=a;https://other.example/",
    ],
)
def test_semicolons_survive_resolution_validation_and_public_artifact(url):
    a = article("alpha")
    a["source_links"] = [url]
    c = catalog(a)
    resolved = resolve_vendor_references(report(c, selection(c)), c)
    validate_vendor_links(resolved, c)
    assert split_vendor_urls(url) == [url]
    # Public artifacts retain URLs, not internal reference IDs.
    public = REPORT.replace(
        "- **Action**: patch", "- **Action**: patch\n- **Vendor Links**: " + url
    )
    artifact = parse_report_artifact(public)
    assert artifact.findings[0].vendor_links == (url,)


def test_normalization_identity_and_reserved_query_differences():
    a = article("alpha")
    a["source_links"] = ["https://VENDOR.example:443/old/../advisory#patch"]
    ref = selection(catalog(a))
    a["source_links"] = ["https://vendor.example/advisory"]
    assert selection(catalog(a)) == ref
    a["source_links"] = ["https://vendor.example/advisory?q=a;b"]
    ref = selection(catalog(a))
    a["source_links"] = ["https://vendor.example/advisory?q=a%3Bb"]
    assert selection(catalog(a)) != ref


def test_actual_captured_source_links_all_roundtrip():
    s = json.loads(
        (Path(__file__).parent / "fixtures/vendor_source_acc7a2d0e979.json").read_text()
    )
    # Public captured metadata; synthetic body explicitly does not claim replay
    # of the missing rejected answer or original 7995-character source content.
    c = catalog(
        {
            "title": s["title"],
            "source": s["publisher"],
            "link": s["url"],
            "content": "CVE-2017-16995",
            "source_links": s["links"],
        }
    )
    assert list(c) == [s["key"]]
    refs = build_vendor_reference_context(c)
    for choices in [[r["id"]] for r in refs] + [[r["id"] for r in refs]]:
        resolved = resolve_vendor_references(report(c, "; ".join(choices)), c)
        validate_vendor_links(resolved, c)
    assert len(refs) == 3


@pytest.mark.parametrize("mutation", ["duplicate_field", "wrapped", "misplaced"])
def test_field_shape_is_closed(mutation):
    c = catalog()
    ref = selection(c)
    raw = report(c, ref)
    if mutation == "duplicate_field":
        raw += "- **Vendor Links**: " + ABSENT + "\n"
    elif mutation == "wrapped":
        raw += " extra hidden text\n"
    else:
        raw = ref + "\n" + raw
    with pytest.raises(EvidenceError):
        resolve_vendor_references(raw, c)


def test_reference_shaped_text_inside_source_owned_url_is_not_model_protocol():
    url = "https://vendor.example/vendor-" + "a" * 32
    a = article("alpha")
    a["source_links"] = [url]
    c = catalog(a)
    resolved = resolve_vendor_references(report(c, selection(c)), c)
    validate_vendor_links(resolved, c)
    assert url in resolved


def test_mandatory_protocol_at_shared_reviewed_boundary():
    from test_reviewed_report import prepared_result
    from src.core.reviewed_report import resolve_reviewed_analysis

    for advisory in (False, True):
        result = prepared_result()
        result.pop(PROTOCOL_KEY)
        with pytest.raises(EvidenceError) as err:
            resolve_reviewed_analysis(result, advisory=advisory)
        assert err.value.code == "invalid_vendor_reference_protocol"


def test_duplicate_hash_collision_fails_closed(monkeypatch):
    from src.core import vendor_references as module

    c = catalog()
    refs = build_vendor_reference_context(c)
    monkeypatch.setattr(module, "build_vendor_reference_context", lambda _: refs + refs)
    with pytest.raises(EvidenceError) as err:
        resolve_vendor_references(report(c, selection(c)), c)
    assert err.value.code == "vendor_reference_collision"


def test_prompt_warns_membership_is_not_advisory_relevance():
    from src.core.exploitation_prompt import build_exploitation_prompt
    from src.core.source_review import prepare_source_review

    prompt = build_exploitation_prompt(prepare_source_review([article("alpha")]))
    refs = json.loads(
        prompt.split("BEGIN VENDOR LINK REFERENCES\n")[1].split(
            "\nEND VENDOR LINK REFERENCES"
        )[0]
    )
    assert refs == build_vendor_reference_context(catalog())
    assert "Membership alone does not make a link an advisory" in prompt
    assert "explicitly output exactly Not stated in supplied sources." in prompt

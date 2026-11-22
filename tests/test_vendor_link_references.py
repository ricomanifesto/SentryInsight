"""Source-owned vendor link IDs: offered from eligible inventories, resolved
only for the finding that cites their owner, and never guessed or invented."""

import json

import pytest

from src.core import vendor_link_references as references
from src.core.exploitation_prompt import build_exploitation_prompt
from src.core.finding_evidence import (
    EvidenceError,
    MAX_VENDOR_LINK_POSITION,
    grounding_failure_diagnostic,
    validate_finding_evidence,
    validate_vendor_links,
)
from src.core.finding_grouping import group_related_findings
from src.core.report_artifact import parse_report_artifact
from src.core.reporting import build_reporting_catalog
from src.core.reviewed_report import resolve_reviewed_analysis
from src.core.source_review import SourceReviewError, prepare_source_review
from src.core.validation_diagnostics import (
    sanitize_diagnostic,
    validation_diagnostic,
)
from src.core.vendor_link_references import (
    LINK_ID_PATTERN,
    build_vendor_link_context,
    link_id,
    resolve_vendor_link_ids,
    vendor_link_targets,
)
from report_recovery_fixtures import (
    ABSENT,
    ALPHA_ADVISORY,
    ALPHA_NOTES,
    BETA_ADVISORY,
    HELD_ADVISORY,
    HELD_CONTENT,
    SEPARATOR_LINK,
    TRAILER,
    article,
    finding,
    id_for,
    key_for,
    prepared_result,
    report,
    standard_articles,
)

MODES = (False, True)
MODE_IDS = ("strict", "advisory")
CVE = "CVE-2099-71001"


def catalog():
    return build_reporting_catalog(standard_articles()[:2])


def pipeline(findings, *, advisory=False, articles=None, **kwargs):
    articles = articles or standard_articles()
    result = prepared_result(articles, report(findings, **kwargs))
    return resolve_reviewed_analysis(result, advisory=advisory)


def pipeline_error(findings, *, advisory=False, **kwargs):
    with pytest.raises(EvidenceError) as caught:
        pipeline(findings, advisory=advisory, **kwargs)
    return caught.value


def alpha_finding(vendor_links, keys=None, **kwargs):
    return finding(
        "Synthetic gateway campaign",
        keys or [key_for("alpha")],
        vendor_links=vendor_links,
        **kwargs,
    )


# Identity and the offered contract


def test_link_id_is_deterministic_source_owned_and_well_formed():
    content = "A alpha service advisory."
    first = link_id(key_for("alpha"), content, ALPHA_ADVISORY)
    assert first == link_id(key_for("alpha"), content, ALPHA_ADVISORY)
    assert LINK_ID_PATTERN.fullmatch(first)
    # The same URL in another source is a different, separately owned ID.
    assert link_id(key_for("beta"), content, ALPHA_ADVISORY) != first
    assert link_id(key_for("alpha"), content, ALPHA_NOTES) != first
    # The source-content digest is part of the identity.
    assert link_id(key_for("alpha"), content + " Revised.", ALPHA_ADVISORY) != first


def test_an_id_minted_for_other_source_content_does_not_resolve():
    stale = link_id(key_for("alpha"), "Earlier synthetic wording.", ALPHA_ADVISORY)
    with pytest.raises(EvidenceError) as caught:
        resolve_vendor_link_ids(report(alpha_finding(stale)), catalog())
    assert caught.value.code == "unsupported_vendor_link"


def test_contract_offers_only_eligible_links_the_field_grammar_can_carry():
    plan = prepare_source_review(standard_articles())
    context = build_vendor_link_context(plan.eligible_catalog)
    assert context == {
        key_for("alpha"): [
            [id_for("alpha", ALPHA_ADVISORY), ALPHA_ADVISORY],
            [id_for("alpha", ALPHA_NOTES), ALPHA_NOTES],
        ],
        key_for("beta"): [[id_for("beta", BETA_ADVISORY), BETA_ADVISORY]],
    }
    # The separator link is in the inventory but stays on the legacy path.
    assert SEPARATOR_LINK in plan.eligible_catalog[key_for("alpha")].links
    assert key_for("held") not in context


def test_prompt_carries_the_compact_contract_and_the_cited_source_rule():
    plan = prepare_source_review(standard_articles())
    prompt = build_exploitation_prompt(plan)
    context = build_vendor_link_context(plan.eligible_catalog)
    block = (
        "BEGIN VENDOR LINK CONTRACT\n"
        + json.dumps(context, ensure_ascii=True, separators=(",", ":"))
        + "\nEND VENDOR LINK CONTRACT"
    )
    assert block in prompt
    assert prompt.index("END REPORTING SOURCE CONTRACT") < prompt.index(block)
    assert (
        "Source links of the articles cited in this finding's Reporting field" in prompt
    )
    assert "a link supplied only by an uncited article is rejected" in prompt
    assert id_for("held", HELD_ADVISORY) not in prompt


def test_id_collision_fails_closed(monkeypatch):
    monkeypatch.setattr(references, "link_id", lambda *_: "link-" + "0" * 16)
    with pytest.raises(SourceReviewError) as caught:
        vendor_link_targets(catalog())
    assert caught.value.code == "invalid_review_input_catalog"


def test_repeated_identical_link_in_one_source_is_not_a_collision():
    repeated = build_reporting_catalog([article("alpha", [ALPHA_ADVISORY] * 2)])
    assert vendor_link_targets(repeated) == {
        id_for("alpha", ALPHA_ADVISORY): (key_for("alpha"), ALPHA_ADVISORY)
    }


# Resolution


def test_owned_cited_ids_resolve_to_exact_inventory_urls_in_field_order():
    ids = f"{id_for('alpha', ALPHA_NOTES)};  {id_for('alpha', ALPHA_ADVISORY)}"
    text = report(alpha_finding(ids))
    resolved = resolve_vendor_link_ids(text, catalog())
    assert f"- **Vendor Links**: {ALPHA_NOTES};  {ALPHA_ADVISORY}\n" in resolved
    assert "link-" not in resolved
    # Only the Vendor Links value changed.
    assert resolved.replace(f"{ALPHA_NOTES};  {ALPHA_ADVISORY}", ids) == text
    validate_vendor_links(resolved, catalog())
    validate_finding_evidence(resolved, catalog())


@pytest.mark.parametrize("advisory", MODES, ids=MODE_IDS)
@pytest.mark.parametrize(
    "template",
    [
        "{alpha}; {alpha}",
        "{alpha};{alpha}; {notes}",
        "{alpha}; " + ALPHA_ADVISORY,
        ALPHA_ADVISORY + "; {alpha}",
        "{alpha}; {beta}; {beta_alias}",
    ],
    ids=[
        "same-id-twice",
        "same-id-twice-with-another",
        "id-then-same-raw-url",
        "raw-url-then-same-id",
        "two-owners-same-url",
    ],
)
def test_duplicate_reference_selections_are_invalid(advisory, template):
    articles = [
        article("alpha", [ALPHA_ADVISORY, ALPHA_NOTES, SEPARATOR_LINK]),
        article("beta", [BETA_ADVISORY, ALPHA_ADVISORY]),
        article("held", [HELD_ADVISORY], content=HELD_CONTENT),
    ]
    value = template.format(
        alpha=id_for("alpha", ALPHA_ADVISORY, articles),
        notes=id_for("alpha", ALPHA_NOTES, articles),
        beta=id_for("beta", BETA_ADVISORY, articles),
        beta_alias=id_for("beta", ALPHA_ADVISORY, articles),
    )
    findings = alpha_finding(value, keys=[key_for("alpha"), key_for("beta")])
    error = pipeline_error(findings, advisory=advisory, articles=articles)
    assert (error.code, error.field, error.finding_index) == (
        "invalid_vendor_link",
        "Vendor Links",
        1,
    )


def test_duplicate_raw_urls_without_ids_keep_legacy_behavior():
    text = report(alpha_finding(f"{ALPHA_ADVISORY}; {ALPHA_ADVISORY}"))
    assert resolve_vendor_link_ids(text, catalog()) == text
    validate_vendor_links(text, catalog())


def test_text_without_ids_is_returned_unchanged():
    text = report(alpha_finding(ALPHA_ADVISORY))
    assert resolve_vendor_link_ids(text, catalog()) == text


@pytest.mark.parametrize("advisory", MODES, ids=MODE_IDS)
def test_pipeline_resolves_owned_ids_and_the_artifact_parses(advisory):
    candidate = pipeline(
        alpha_finding(id_for("alpha", ALPHA_ADVISORY)), advisory=advisory
    )
    assert f"- **Vendor Links**: {ALPHA_ADVISORY}\n" in candidate.report
    assert "link-" not in candidate.source
    assert "link-" not in candidate.grounded_report
    [parsed] = parse_report_artifact(candidate.source).findings
    assert parsed.vendor_links == (ALPHA_ADVISORY,)


@pytest.mark.parametrize("advisory", MODES, ids=MODE_IDS)
def test_id_owned_by_an_uncited_source_is_unsupported_until_cited(advisory):
    beta_id = id_for("beta", BETA_ADVISORY)
    error = pipeline_error(alpha_finding(beta_id), advisory=advisory)
    assert (error.code, error.field, error.finding_index) == (
        "unsupported_vendor_link",
        "Vendor Links",
        1,
    )
    candidate = pipeline(
        alpha_finding(beta_id, keys=[key_for("alpha"), key_for("beta")]),
        advisory=advisory,
    )
    assert f"- **Vendor Links**: {BETA_ADVISORY}\n" in candidate.report


@pytest.mark.parametrize("advisory", MODES, ids=MODE_IDS)
@pytest.mark.parametrize(
    "entry",
    [
        "link-" + "0" * 16,
        "link-" + "f" * 16,
        id_for("held", HELD_ADVISORY),
        id_for("alpha", BETA_ADVISORY),
        id_for("alpha", SEPARATOR_LINK),
    ],
    ids=["zero", "unknown", "held-source", "wrong-owner", "not-offered"],
)
def test_well_formed_unknown_or_unowned_id_is_unsupported(advisory, entry):
    error = pipeline_error(alpha_finding(entry), advisory=advisory)
    assert error.code == "unsupported_vendor_link"


@pytest.mark.parametrize("advisory", MODES, ids=MODE_IDS)
@pytest.mark.parametrize(
    "template",
    [
        "{upper}",
        "{short}",
        "`{id}`",
        "[{id}]({url})",
        "{id};",
        "{id}; " + ABSENT,
        ABSENT + "; {id}",
        "{id}; vendor.example.test/advisory/alpha",
        "{id}, {id2}",
    ],
    ids=[
        "uppercase",
        "short",
        "code-wrapped",
        "markdown-link",
        "trailing-empty",
        "absence-after",
        "absence-before",
        "schemeless-sibling",
        "comma-separated",
    ],
)
def test_malformed_id_syntax_is_invalid(advisory, template):
    alpha = id_for("alpha", ALPHA_ADVISORY)
    value = template.format(
        id=alpha,
        id2=id_for("alpha", ALPHA_NOTES),
        upper=alpha.upper(),
        short=alpha[:-1],
        url=ALPHA_ADVISORY,
    )
    error = pipeline_error(alpha_finding(value), advisory=advisory)
    assert (error.code, error.field) == ("invalid_vendor_link", "Vendor Links")


@pytest.mark.parametrize("advisory", MODES, ids=MODE_IDS)
@pytest.mark.parametrize(
    ("value", "code"),
    [
        (ALPHA_ADVISORY, None),
        (f"{ALPHA_ADVISORY}; {id_for('alpha', ALPHA_NOTES)}", None),
        ("https://vendor.example.test/advisory/other", "unsupported_vendor_link"),
        (BETA_ADVISORY, "unsupported_vendor_link"),
        ("vendor.example.test/advisory/alpha", "invalid_vendor_link"),
        ("https://user:pass@vendor.example.test/advisory/alpha", "invalid_vendor_link"),
        (SEPARATOR_LINK, "invalid_vendor_link"),
    ],
    ids=[
        "exact-raw",
        "raw-and-id",
        "same-host-other-path",
        "uncited-raw",
        "no-scheme",
        "credentials",
        "separator-link-legacy",
    ],
)
def test_legacy_raw_url_behavior_is_unchanged(advisory, value, code):
    if code is None:
        candidate = pipeline(alpha_finding(value), advisory=advisory)
        assert "link-" not in candidate.report
        return
    assert pipeline_error(alpha_finding(value), advisory=advisory).code == code


@pytest.mark.parametrize("advisory", MODES, ids=MODE_IDS)
@pytest.mark.parametrize("name", ["alpha", "lonely"])
def test_valid_absence_passes_with_or_without_offered_links(advisory, name):
    articles = [*standard_articles(), article("lonely")]
    findings = finding("Synthetic gateway campaign", [key_for(name)])
    candidate = pipeline(findings, advisory=advisory, articles=articles)
    assert f"- **Vendor Links**: {ABSENT}\n" in candidate.report


def test_missing_vendor_links_field_keeps_its_existing_code():
    findings = alpha_finding(ABSENT).replace(f"- **Vendor Links**: {ABSENT}\n", "")
    error = pipeline_error(findings)
    assert (error.code, error.field) == ("missing_detail_field", "Vendor Links")


def test_an_id_is_rejected_before_merging_can_lend_a_citation():
    alpha, beta = key_for("alpha"), key_for("beta")
    beta_id = id_for("beta", BETA_ADVISORY)
    title = f"Synthetic gateway flaw ({CVE})"
    findings = finding(title, [alpha], vendor_links=beta_id) + finding(
        title, [beta], vendor_links=beta_id
    )
    findings = findings.replace(
        "- **Severity**", f"- **CVE IDs**: {CVE}\n- **Severity**"
    )
    with pytest.raises(EvidenceError) as caught:
        resolve_vendor_link_ids(report(findings), catalog())
    assert (caught.value.code, caught.value.finding_index) == (
        "unsupported_vendor_link",
        1,
    )


def test_a_valid_repeated_pair_merges_and_keeps_every_resolved_link():
    alpha, beta = key_for("alpha"), key_for("beta")
    findings = finding(
        f"Synthetic gateway flaw ({CVE})",
        [alpha],
        vendor_links=id_for("alpha", ALPHA_ADVISORY),
    ) + finding(
        f"Synthetic gateway flaw ({CVE})",
        [beta],
        vendor_links=id_for("beta", BETA_ADVISORY),
    )
    findings = findings.replace(
        "- **Severity**", f"- **CVE IDs**: {CVE}\n- **Severity**"
    )
    resolved = resolve_vendor_link_ids(report(findings), catalog())
    merged = group_related_findings(resolved, catalog())
    assert merged != resolved
    assert f"- **Reporting**: {alpha}, {beta}\n" in merged
    assert f"- **Vendor Links**: {ALPHA_ADVISORY}; {BETA_ADVISORY}\n" in merged
    validate_vendor_links(merged, catalog())


@pytest.mark.parametrize(
    ("place", "index"),
    [("summary", None), ("description", 1), ("trailer", None)],
)
def test_a_stray_id_anywhere_else_is_invalid(place, index):
    stray = id_for("alpha", ALPHA_ADVISORY)
    kwargs = {}
    description = "A campaign described by the supplied reporting."
    if place == "summary":
        kwargs["summary"] = f"See {stray} for the advisory.\n\n"
    elif place == "description":
        description = f"A campaign; see {stray}."
    else:
        kwargs["trailer"] = TRAILER + f"- Background reference {stray}.\n"
    text = report(alpha_finding(ABSENT, description=description), **kwargs)
    with pytest.raises(EvidenceError) as caught:
        resolve_vendor_link_ids(text, catalog())
    assert (caught.value.code, caught.value.finding_index) == (
        "invalid_vendor_link",
        index,
    )


def test_id_shaped_url_segments_are_not_mistaken_for_ids():
    shaped = id_for("alpha", ALPHA_ADVISORY)
    path_link = f"https://vendor.example.test/files/{shaped}"
    query_link = f"https://vendor.example.test/files?ref={shaped}"
    shaped_catalog = build_reporting_catalog(
        [article("alpha", [path_link, query_link])]
    )
    text = report(alpha_finding(f"{path_link}; {query_link}"))
    assert resolve_vendor_link_ids(text, shaped_catalog) == text
    validate_vendor_links(text, shaped_catalog)


@pytest.mark.parametrize("advisory", MODES, ids=MODE_IDS)
def test_resolved_candidate_matches_the_raw_url_candidate_byte_for_byte(advisory):
    by_id = pipeline(
        alpha_finding(
            f"{id_for('alpha', ALPHA_ADVISORY)}; {id_for('beta', BETA_ADVISORY)}",
            keys=[key_for("alpha"), key_for("beta")],
        ),
        advisory=advisory,
    )
    by_url = pipeline(
        alpha_finding(
            f"{ALPHA_ADVISORY}; {BETA_ADVISORY}",
            keys=[key_for("alpha"), key_for("beta")],
        ),
        advisory=advisory,
    )
    assert by_id.source == by_url.source
    assert by_id.coverage == by_url.coverage
    assert by_id.coverage["counts"]["cited_sources"] == 2


def test_rejection_diagnostic_carries_no_link_text():
    error = pipeline_error(alpha_finding(id_for("beta", BETA_ADVISORY)))
    serialized = json.dumps(validation_diagnostic("finding_evidence", error))
    for forbidden in ("link-", "example.test", BETA_ADVISORY):
        assert forbidden not in serialized
        assert forbidden not in str(error)


def _exported_diagnostics(text: str, error: EvidenceError) -> tuple[dict, dict, dict]:
    grounding = grounding_failure_diagnostic(text, catalog(), error)
    validation = validation_diagnostic("finding_evidence", error)
    sanitized = sanitize_diagnostic(validation)
    return grounding, validation, sanitized


@pytest.mark.parametrize("advisory", MODES, ids=MODE_IDS)
@pytest.mark.parametrize(
    ("value", "reason", "position"),
    [
        ("vendor.example.test/advisory/alpha", "invalid_url_scheme", 1),
        (
            f"{ALPHA_ADVISORY}; https://user:pass@vendor.example.test/advisory/alpha",
            "url_credentials_not_allowed",
            2,
        ),
        (f"{ALPHA_ADVISORY};", "empty_url", 2),
        (f"{ALPHA_ADVISORY}; https:///advisory/alpha", "missing_url_host", 2),
        (
            f"{ALPHA_ADVISORY}; https://vendor.example.test:99999/advisory/alpha",
            "invalid_url_port",
            2,
        ),
        (
            f"{ALPHA_ADVISORY}; https://bad..example.test/advisory/alpha",
            "invalid_url_host",
            2,
        ),
        (
            f"{ALPHA_ADVISORY}; https://[::1/advisory/alpha",
            "invalid_url_syntax",
            2,
        ),
        # Malformed-before-unsupported precedence: entry 1 is unsupported, entry 2 is malformed.
        (
            f"{BETA_ADVISORY}; vendor.example.test/advisory/alpha",
            "invalid_url_scheme",
            2,
        ),
    ],
    ids=[
        "no-scheme",
        "credentials",
        "empty-entry",
        "missing-host",
        "invalid-port",
        "invalid-host",
        "invalid-syntax",
        "malformed-before-unsupported",
    ],
)
def test_normalization_and_precedence_diagnostics_carry_reason_and_position(
    advisory, value, reason, position
):
    findings = alpha_finding(value)
    error = pipeline_error(findings, advisory=advisory)
    assert error.code == "invalid_vendor_link"
    grounding, validation, sanitized = _exported_diagnostics(report(findings), error)
    for exported in (grounding, validation, sanitized):
        assert exported["vendor_link_reason"] == reason
        assert exported["vendor_link_position"] == position
    assert grounding["code"] == "invalid_vendor_link"
    assert validation["codes"] == ["invalid_vendor_link"]
    assert sanitized["codes"] == ["invalid_vendor_link"]


@pytest.mark.parametrize("advisory", MODES, ids=MODE_IDS)
@pytest.mark.parametrize(
    ("value", "code", "reason", "position"),
    [
        (
            f"{ALPHA_ADVISORY}; {BETA_ADVISORY}",
            "unsupported_vendor_link",
            "not_in_cited_sources",
            2,
        ),
        (
            f"{ALPHA_ADVISORY}; https://vendor.example.test/advisory/other",
            "unsupported_vendor_link",
            "not_in_cited_sources",
            2,
        ),
        (
            f"{ALPHA_ADVISORY}; {id_for('beta', BETA_ADVISORY)}",
            "unsupported_vendor_link",
            "uncited_link_reference",
            2,
        ),
        (
            f"{ALPHA_ADVISORY}; {'link-' + '0' * 16}",
            "unsupported_vendor_link",
            "unknown_link_reference",
            2,
        ),
        (
            f"{id_for('alpha', ALPHA_ADVISORY)}; {id_for('alpha', ALPHA_ADVISORY)}",
            "invalid_vendor_link",
            "duplicate_vendor_link",
            2,
        ),
        (
            f"{ALPHA_ADVISORY}; {id_for('alpha', ALPHA_ADVISORY)}",
            "invalid_vendor_link",
            "duplicate_vendor_link",
            2,
        ),
        (
            f"{id_for('alpha', ALPHA_ADVISORY)}; vendor.example.test/advisory/alpha",
            "invalid_vendor_link",
            "invalid_url_scheme",
            2,
        ),
    ],
    ids=[
        "uncited-raw-url",
        "absent-raw-url",
        "uncited-link-id",
        "unknown-link-id",
        "duplicate-link-id",
        "raw-and-duplicate-id",
        "id-with-malformed-sibling",
    ],
)
def test_unsupported_and_resolver_diagnostics_carry_reason_and_position(
    advisory, value, code, reason, position
):
    findings = alpha_finding(value)
    error = pipeline_error(findings, advisory=advisory)
    assert error.code == code
    grounding, validation, sanitized = _exported_diagnostics(report(findings), error)
    for exported in (grounding, validation, sanitized):
        assert exported["vendor_link_reason"] == reason
        assert exported["vendor_link_position"] == position
    assert grounding["code"] == code
    assert validation["codes"] == [code]
    assert sanitized["codes"] == [code]


@pytest.mark.parametrize("place", ["summary", "description", "trailer"])
def test_stray_link_reference_outside_vendor_links_omits_unknown_position(place):
    stray = id_for("alpha", ALPHA_ADVISORY)
    kwargs = {}
    description = "A campaign described by the supplied reporting."
    if place == "summary":
        kwargs["summary"] = f"See {stray} for the advisory.\n\n"
    elif place == "description":
        description = f"A campaign; see {stray}."
    else:
        kwargs["trailer"] = TRAILER + f"- Background reference {stray}.\n"
    text = report(alpha_finding(ABSENT, description=description), **kwargs)
    with pytest.raises(EvidenceError) as caught:
        resolve_vendor_link_ids(text, catalog())
    grounding, validation, sanitized = _exported_diagnostics(text, caught.value)
    for exported in (grounding, validation, sanitized):
        assert exported["vendor_link_reason"] == "stray_link_reference"
        assert "vendor_link_position" not in exported


@pytest.mark.parametrize(
    "validator", [validate_finding_evidence, validate_vendor_links], ids=MODE_IDS
)
@pytest.mark.parametrize(
    ("position", "expected_position"),
    [
        (MAX_VENDOR_LINK_POSITION, MAX_VENDOR_LINK_POSITION),
        (MAX_VENDOR_LINK_POSITION + 1, None),
    ],
    ids=["upper-bound-256", "over-bound-257"],
)
def test_vendor_link_position_bounds_in_validators(
    validator, position, expected_position
):
    value = "; ".join([ALPHA_ADVISORY] * (position - 1) + [BETA_ADVISORY])
    text = report(alpha_finding(value))
    with pytest.raises(EvidenceError) as caught:
        validator(text, catalog())
    assert caught.value.code == "unsupported_vendor_link"
    grounding, validation, sanitized = _exported_diagnostics(text, caught.value)
    for exported in (grounding, validation, sanitized):
        assert exported["vendor_link_reason"] == "not_in_cited_sources"
        if expected_position is None:
            assert "vendor_link_position" not in exported
        else:
            assert exported["vendor_link_position"] == expected_position


@pytest.mark.parametrize("bad_position", [0, -1, 257, True, False, 1.0, "1", None])
def test_diagnostic_exporters_enforce_strict_int_bounds(bad_position):
    text = report(alpha_finding(ABSENT))
    error = EvidenceError(
        "Unsupported vendor link",
        code="invalid_vendor_link",
        field="Vendor Links",
        expected=True,
        observed=False,
        vendor_link_reason="invalid_url_scheme",
        vendor_link_position=bad_position,
    )
    grounding, validation, _ = _exported_diagnostics(text, error)
    sanitized = sanitize_diagnostic(
        {
            "stage": "finding_evidence",
            "codes": ["invalid_vendor_link"],
            "field": "Vendor Links",
            "vendor_link_reason": "invalid_url_scheme",
            "vendor_link_position": bad_position,
        }
    )
    for exported in (grounding, validation, sanitized):
        assert exported["vendor_link_reason"] == "invalid_url_scheme"
        assert "vendor_link_position" not in exported


def test_diagnostic_exporters_reject_non_allowlisted_cross_class_and_unrelated_codes():
    text = report(alpha_finding(ABSENT))
    bad_reason = EvidenceError(
        "Unsupported vendor link",
        code="invalid_vendor_link",
        field="Vendor Links",
        vendor_link_reason="not_in_cited_sources",
        vendor_link_position=1,
    )
    for exported in _exported_diagnostics(text, bad_reason):
        assert "vendor_link_reason" not in exported
        assert exported["vendor_link_position"] == 1

    tampered = sanitize_diagnostic(
        {
            "stage": "finding_evidence",
            "codes": ["unsupported_vendor_link"],
            "field": "Vendor Links",
            "vendor_link_reason": "https://secret.example.test/raw?token=1",
            "vendor_link_position": 2,
        }
    )
    assert "vendor_link_reason" not in tampered
    assert tampered["vendor_link_position"] == 2

    unrelated = EvidenceError(
        "Missing field",
        code="missing_detail_field",
        field="Vendor Links",
        vendor_link_reason="empty_url",
        vendor_link_position=1,
    )
    for exported in _exported_diagnostics(text, unrelated):
        assert "vendor_link_reason" not in exported
        assert "vendor_link_position" not in exported
    unrelated_sanitized = sanitize_diagnostic(
        {
            "stage": "finding_evidence",
            "codes": ["missing_detail_field"],
            "field": "Vendor Links",
            "vendor_link_reason": "empty_url",
            "vendor_link_position": 1,
        }
    )
    assert "vendor_link_reason" not in unrelated_sanitized
    assert "vendor_link_position" not in unrelated_sanitized


@pytest.mark.parametrize("advisory", MODES, ids=MODE_IDS)
def test_persisted_diagnostic_exporters_redact_sensitive_vendor_link_text(advisory):
    sensitive_url = (
        "https://synthuser:synthsecret@vendor.example.test"
        "/advisory/secret-path?token=synthq#synthfrag"
    )
    findings = alpha_finding(f"{ALPHA_ADVISORY}; {sensitive_url}")
    error = pipeline_error(findings, advisory=advisory)
    grounding, validation, sanitized = _exported_diagnostics(report(findings), error)
    for exported in (grounding, validation, sanitized):
        assert exported["vendor_link_reason"] == "url_credentials_not_allowed"
        assert exported["vendor_link_position"] == 2
    assert set(grounding["sources"][0]) == {
        "key",
        "content_kind",
        "content_chars",
        "content_sha256",
    }
    forbidden_tokens = (
        "synthuser",
        "synthsecret",
        "vendor.example.test",
        "secret-path",
        "synthq",
        "synthfrag",
        "link-",
        "Synthetic gateway campaign",
    )
    for exported in (grounding, validation, sanitized):
        serialized = json.dumps(exported)
        for forbidden in forbidden_tokens:
            assert forbidden not in serialized
    for forbidden in forbidden_tokens[:-1]:
        assert forbidden not in str(error)

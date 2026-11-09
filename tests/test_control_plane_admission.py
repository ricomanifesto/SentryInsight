"""Product-side admission requests for the report control plane."""

import hashlib
import json

import httpx
import pytest

from src.control_plane import admission

PIPELINE = "reports"
POLICY = "standard"


def sha(data):
    if isinstance(data, str):
        data = data.encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def product_article(n, **overrides):
    record = {
        "id": f"feed-{n}",
        "title": f"Synthetic article {n}",
        "link": f"https://example.test/articles/{n}",
        "source": "Example Source",
        "published": "Sat, 08 Nov 2026 12:00:00 GMT",
        "summary": "A feed summary.",
        "content": f"Synthetic article {n} content.",
        "content_kind": "article",
        "source_links": ["https://example.test/advisory"],
        "cves": ["CVE-2026-0001"],
    }
    record.update(overrides)
    return record


def build(articles, revision="articles-1"):
    return admission.admission_body(
        articles, pipeline=PIPELINE, policy_id=POLICY, source_revision=revision
    )


def test_body_keeps_only_accepted_fields_and_unchanged_text():
    body = build([product_article(1, content="Ünïcode text — unchanged.")])
    value = json.loads(body)
    assert list(value) == [
        "schema",
        "pipeline",
        "policy_id",
        "source_revision",
        "articles",
    ]
    assert value["schema"] == "report-control-plane/admission/1"
    (record,) = value["articles"]
    assert sorted(record) == [
        "content",
        "content_kind",
        "cves",
        "link",
        "source",
        "source_links",
        "summary",
        "title",
    ]
    assert record["content"] == "Ünïcode text — unchanged."


def test_absent_optional_fields_are_omitted_not_invented():
    article = {"title": "T", "link": "https://example.test/a", "content": ""}
    (record,) = json.loads(build([article]))["articles"]
    assert record == article


def test_identity_matches_the_control_plane_derivation():
    body = build([product_article(1)])
    fingerprint, operation_id = admission.expected_identity(body, PIPELINE, POLICY)
    assert fingerprint == sha(body)
    assert operation_id == sha(
        f"report-control-plane/1\n{PIPELINE}\n{POLICY}\n{fingerprint}"
    )
    assert build([product_article(1)]) == body, "the same articles give the same bytes"


@pytest.mark.parametrize(
    ("articles", "revision", "reason"),
    [
        ([], "r", "articles_invalid"),
        ([product_article(1)] * 2, "r", "article_duplicate_key"),
        ([product_article(n) for n in range(101)], "r", "articles_invalid"),
        ([product_article(1, link="ftp://example.test/a")], "r", "article_invalid"),
        ([product_article(1, title=" ")], "r", "article_invalid"),
        ([product_article(1, content=None)], "r", "article_invalid"),
        ([product_article(1, content="x" * 65537)], "r", "article_invalid"),
        ([product_article(1, cves="CVE-2026-0001")], "r", "article_invalid"),
        ([product_article(1, content="\ud800")], "r", "article_invalid"),
        ([product_article(1, cves=["\ud800"])], "r", "article_invalid"),
        # 300 emoji are 600 UTF-16 units, past the 512-unit title bound.
        ([product_article(1, title="\U0001f512" * 300)], "r", "article_invalid"),
        ([product_article(1)], "schedule:x", "source_revision_reserved"),
        ([product_article(1)], " bad", "source_revision_invalid"),
    ],
)
def test_refuses_locally_what_the_control_plane_refuses(articles, revision, reason):
    with pytest.raises(admission.AdmissionRefused) as refused:
        build(articles, revision)
    assert refused.value.reason == reason


def test_record_bound_counts_ascii_escaped_bytes():
    # 32,760 two-byte characters fit the 64 KiB content bound in UTF-8 but
    # escape to six bytes each, past the 64 KiB record bound.
    wide = "é" * 32_760
    with pytest.raises(admission.AdmissionRefused) as refused:
        build([product_article(1, content=wide, summary="", source_links=[])])
    assert refused.value.reason == "article_too_large"
    assert build([product_article(1, content="é" * 10_000)])


def transport(status, payload):
    def handler(request):
        assert request.headers["authorization"] == "Bearer synthetic-token-0123456789"
        assert request.url.path == "/v1/operations"
        return httpx.Response(status, json=payload)

    return httpx.MockTransport(handler)


def submit(status, payload, body):
    with httpx.Client(transport=transport(status, payload)) as client:
        return admission.submit(
            client,
            "https://control.example.test",
            "synthetic-token-0123456789",
            body,
            pipeline=PIPELINE,
            policy_id=POLICY,
        )


def test_submit_returns_the_verified_operation():
    body = build([product_article(1)])
    _, operation_id = admission.expected_identity(body, PIPELINE, POLICY)
    for status, created in ((201, True), (200, False)):
        result = submit(
            status, {"operation": {"operation_id": operation_id, "state": "x"}}, body
        )
        assert (result.operation_id, result.created) == (operation_id, created)


def test_submit_refuses_a_mismatched_operation_identity():
    body = build([product_article(1)])
    with pytest.raises(admission.AdmissionError):
        submit(201, {"operation": {"operation_id": "0" * 64}}, body)


def test_submit_classifies_conflict_refusal_and_transient_failure():
    body = build([product_article(1)])
    with pytest.raises(admission.AdmissionConflict) as conflict:
        submit(
            409, {"error": "source_revision_conflict", "operation_id": "a" * 64}, body
        )
    assert conflict.value.operation_id == "a" * 64
    with pytest.raises(admission.AdmissionRefused) as refused:
        submit(422, {"error": "pipeline_unavailable"}, body)
    assert refused.value.reason == "pipeline_unavailable"
    with pytest.raises(admission.AdmissionTransient):
        submit(503, {"error": "config_invalid"}, body)

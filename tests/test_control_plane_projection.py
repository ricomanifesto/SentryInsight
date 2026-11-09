"""History projection of finished report runs: snapshot, request and delivery."""

import hashlib
import json

import httpx
import pytest

from src.control_plane import projection, run_snapshot
from src.control_plane.admission import PROJECTION_LIMITS, admission_body


def sha(data):
    return hashlib.sha256(data).hexdigest()


def article(n, **overrides):
    record = {
        "title": f"Article {n}",
        "link": f"https://example.test/{n}",
        "source": "Example",
        "summary": "Summary.",
        "published": "Sun, 08 Nov 2026 15:43:08 GMT",
        "date": "2026-11-09",
        "content": f"Full text {n}.",
        "content_kind": "article",
        "source_links": [],
    }
    record.update(overrides)
    return record


def state(**overrides):
    value = {
        "status": "completed",
        "articles": [article(1), article(2, content_kind="feed")],
        "filtered_articles": [article(1)],
    }
    value.update(overrides)
    return value


COMMIT = "a" * 40
FILES = {
    "index.md": b"# Report\n",
    "current-findings.json": b'{"report_date": "2026-11-08"}\n',
    "reports/2026-11-08.md": b"# Dated\n",
}


def test_publication_time_is_the_feed_time_in_utc_or_unknown():
    assert (
        run_snapshot.published_at("Sun, 08 Nov 2026 15:43:08 GMT")
        == "2026-11-08T15:43:08Z"
    )
    assert (
        run_snapshot.published_at("2026-11-08T10:43:08-05:00") == "2026-11-08T15:43:08Z"
    )
    for unknown in ("", None, "yesterday", "2026-11-08T10:43:08", 7):
        assert run_snapshot.published_at(unknown) is None


def test_snapshot_keeps_accepted_fields_and_never_invents_a_time():
    snapshot = run_snapshot.build_run_snapshot(
        state(articles=[article(1), article(2, published="not a date")])
    )
    first, second = snapshot["articles"]
    assert first["published_at"] == "2026-11-08T15:43:08Z"
    assert "published_at" not in second, "the fallback 'date' is never used"
    assert "date" not in first and "published" not in first
    assert snapshot["analyzed_links"] == ["https://example.test/1"]


def test_snapshot_drops_unrecordable_or_duplicate_sources_and_counts_them():
    snapshot = run_snapshot.build_run_snapshot(
        state(
            articles=[
                article(1),
                article(1),
                article(3, link="not a url"),
                article(4, content=[{"value": "x"}]),
            ],
            filtered_articles=None,
        )
    )
    assert [a["link"] for a in snapshot["articles"]] == [
        "https://example.test/1",
        "https://example.test/4",
    ]
    assert snapshot["articles"][1]["content"] == ""
    assert snapshot["dropped_articles"] == 2
    assert snapshot["analyzed_links"] is None


def test_writing_the_snapshot_never_raises(tmp_path, monkeypatch):
    monkeypatch.delenv(run_snapshot.ENV_PATH, raising=False)
    assert run_snapshot.write_run_snapshot(state()) is False
    target = tmp_path / "snapshot.json"
    assert run_snapshot.write_run_snapshot(state(), str(target)) is True
    assert json.loads(target.read_text())["schema"] == run_snapshot.SCHEMA
    assert run_snapshot.write_run_snapshot(state(), str(tmp_path / "no" / "x")) is False
    assert run_snapshot.write_run_snapshot(None, str(target)) is True


def plan(outcome="published", **kwargs):
    return projection.plan_run(
        run_snapshot.build_run_snapshot(kwargs.pop("state", state())),
        workflow_outcome=outcome,
        run_id="123",
        run_attempt="2",
        source_commit=kwargs.pop("source_commit", COMMIT),
        files=kwargs.pop("files", FILES),
        **kwargs,
    )


def test_a_published_run_names_its_commit_files_and_analyzed_sources():
    snapshot, files, request = plan()
    assert request["source_revision"] == "actions:123:2"
    assert request["snapshot_sha256"] == sha(snapshot)
    assert request["run"] == {
        "execution_id": "actions-run-123-2",
        "source_commit": COMMIT,
        "outcome": "succeeded",
        "reason": None,
        "executed_links": ["https://example.test/1"],
        "completed_at": None,
    }
    assert [f["path"] for f in request["artifact"]["files"]] == [
        "current-findings.json",
        "index.md",
        "reports/2026-11-08.md",
    ]
    assert json.loads(snapshot)["articles"][0]["published_at"] == "2026-11-08T15:43:08Z"


def test_failed_runs_keep_their_reason_and_other_outcomes_are_skipped():
    _, files, request = plan(
        "failed", state=state(failure={"codes": ["model_unavailable"]})
    )
    assert files is None and request["artifact"] is None
    assert (request["run"]["outcome"], request["run"]["reason"]) == (
        "failed",
        "model_unavailable",
    )
    assert request["run"]["source_commit"] is None
    assert plan("cancelled")[2]["run"]["reason"] == "generation_cancelled"
    for skipped in ("unchanged", "not-published"):
        assert plan(skipped) is None
    assert plan(state=state(articles=[])) is None
    with pytest.raises(projection.ProjectionError):
        plan(files=None)


def test_projection_bounds_admit_full_article_text():
    long_text = "x" * (100 * 1024)
    body = admission_body(
        [article(1, content=long_text)],
        pipeline="reports",
        policy_id="production",
        source_revision="actions:1:1",
        limits=PROJECTION_LIMITS,
    )
    assert long_text in body.decode()


class Recorder:
    def __init__(self, responses):
        self.responses = list(responses)
        self.requests = []

    def __call__(self, request):
        self.requests.append(request)
        status, payload = self.responses.pop(0)
        return httpx.Response(status, json=payload)


def client(recorder):
    store = projection.Store("https://store.example.test", "t" * 32)
    return projection.Client(
        store,
        httpx.Client(transport=httpx.MockTransport(recorder)),
        sleep=lambda _: None,
    )


def test_delivery_uploads_every_byte_then_projects_and_verifies_the_operation():
    snapshot, files, request = plan()
    operation_id = sha(
        f"report-control-plane/1\nreports\nproduction\n{sha(snapshot)}".encode()
    )
    recorder = Recorder(
        [(201, {})] * 4
        + [(201, {"operation": {"operation_id": operation_id, "state": "completed"}})]
    )
    result = client(recorder).project(snapshot, files, request)
    assert result == {
        "operation_id": operation_id,
        "created": True,
        "state": "completed",
    }
    paths = [r.url.path for r in recorder.requests]
    assert paths[0] == f"/v1/projections/blobs/{sha(snapshot)}"
    assert sorted(paths[1:4]) == sorted(
        f"/v1/projections/blobs/{sha(d)}" for d in files.values()
    )
    assert paths[4] == "/v1/projections"
    assert all(
        r.headers["authorization"] == "Bearer " + "t" * 32 for r in recorder.requests
    )


def test_delivery_retries_transient_failures_and_reports_refusals():
    snapshot, files, request = plan("failed")
    recorder = Recorder([(503, {}), (201, {}), (409, {"error": "projection_conflict"})])
    with pytest.raises(projection.ProjectionError, match="projection_conflict"):
        client(recorder).project(snapshot, files, request)
    recorder = Recorder([(503, {})] * 3)
    with pytest.raises(projection.ProjectionError, match="unavailable"):
        client(recorder).project(snapshot, files, request)


def test_unconfigured_store_skips_successfully(monkeypatch, capsys):
    monkeypatch.delenv(projection.URL_ENV, raising=False)
    monkeypatch.delenv(projection.TOKEN_ENV, raising=False)
    assert projection.main(["observe", "--source-commit", COMMIT]) == 0
    assert "not configured" in capsys.readouterr().out


def descriptor_client(payload, status=200):
    return httpx.Client(
        transport=httpx.MockTransport(
            lambda request: httpx.Response(status, json=payload)
        )
    )


def test_the_serving_commit_comes_only_from_this_sites_release_descriptor():
    origin, repository = "https://site.example.test/", "owner/site"
    good = {
        "kind": "release",
        "expected_repository": repository,
        "expected_origin": origin,
        "source_revision": COMMIT,
    }
    assert (
        projection.serving_commit(descriptor_client(good), origin, repository) == COMMIT
    )
    for bad in (
        {**good, "expected_repository": "owner/other"},
        {**good, "expected_origin": "https://other.test/"},
        {**good, "kind": "preview"},
        {**good, "source_revision": "main"},
    ):
        with pytest.raises(projection.ProjectionError):
            projection.serving_commit(descriptor_client(bad), origin, repository)
    with pytest.raises(projection.ProjectionError, match="unavailable"):
        projection.serving_commit(descriptor_client({}, 404), origin, repository)


def test_the_origin_is_the_site_configurations_production_origin():
    root = __import__("pathlib").Path(__file__).resolve().parents[1]
    assert projection.site_origin(root / "publication" / "site.json") == (
        "https://sentryinsight.ricomanifesto.com/"
    )


def test_rebuild_refuses_a_commit_name_that_is_not_hexadecimal(tmp_path):
    for name in ("--output=/tmp/x", "HEAD", "main~1", "abc"):
        with pytest.raises(projection.ProjectionError, match="hexadecimal"):
            projection.plan_rebuild(tmp_path, name, lambda url: [])


def test_rebuild_requires_a_retained_commit_addressed_feed():
    retained = "https://raw.githubusercontent.com/ricomanifesto/SentryDigest/42e6/site/feed.xml"
    assert (
        projection.feed_from_message(f"Update\n\nAdmission-Feed: {retained}\n")
        == retained
    )
    for message in (
        "Update\n\nAdmission-Feed: none\n",
        "Update\n",
        "Admission-Feed: https://other.test/feed.xml",
    ):
        assert projection.feed_from_message(message) is None

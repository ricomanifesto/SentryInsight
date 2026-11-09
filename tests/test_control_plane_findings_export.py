"""Findings export: accepted artifacts only, verified, deterministic, honest."""

import copy
import hashlib
import json

import httpx
import pytest

from src.control_plane import findings_export as fx
from src.control_plane.projection import Client, Store
from src.core.source_coverage import coverage_markdown
from test_source_coverage import fixture


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def report_text() -> str:
    _, coverage, body, header = fixture()
    return header + body.rstrip() + "\n\n" + coverage_markdown(coverage)


def artifact_for(files: dict[str, bytes]) -> tuple[str, dict]:
    listing = [
        {"path": p, "sha256": sha(d), "bytes": len(d)} for p, d in sorted(files.items())
    ]
    digest = fx.artifact_digest(listing)
    return digest, {"artifact_sha256": digest, "files": listing}


def source_record(url: str, content: str = "text") -> dict:
    key = sha(url.encode())
    return {
        "record_type": "source_revision",
        "record_id": f"sentryinsight:source:{key}:{sha(content.encode())}",
        "canonical_url": url,
        "article_key_sha256": key,
        "content_sha256": sha(content.encode()),
    }


def run_record(
    op: str,
    seq: int,
    outcome: str,
    artifact: str | None,
    sources,
    version=1,
    published=False,
):
    return {
        "record_type": "run",
        "record_id": f"sentryinsight:run:{op}",
        "record_version": version,
        "record_sha256": sha(f"{op}:{version}".encode()),
        "run": {
            "operation_id": op,
            "admission_seq": seq,
            "origin": "project",
            "source_revision": f"actions:{seq}:1",
            "source_commit": "a" * 40 if outcome == "succeeded" else None,
            "outcome": outcome,
            "reason": None if outcome == "succeeded" else "malformed_markdown",
        },
        "sources": [{"source_record_id": s["record_id"]} for s in sources],
        "artifact": None if artifact is None else {"sha256": artifact},
        "publications": (
            [{"target": "production", "state": "published"}] if published else []
        ),
        "report_published": published,
    }


class Store_:
    """A fake history store: export pages, manifests and artifact files."""

    def __init__(self, pages, artifacts):
        self.pages, self.artifacts, self.calls = pages, artifacts, []

    def __call__(self, request: httpx.Request) -> httpx.Response:
        self.calls.append(request.url.path)
        path = request.url.path
        if path == "/v1/export":
            after = int(request.url.params["after"])
            return httpx.Response(200, json=self.pages[after])
        parts = path.split("/")
        manifest, files = self.artifacts.get(parts[4], (None, None))
        if manifest is None:
            return httpx.Response(404, json={"error": "not_found"})
        if len(parts) == 5:
            return httpx.Response(200, json=manifest)
        name = "/".join(parts[6:])
        return (
            httpx.Response(200, content=files[name])
            if name in files
            else httpx.Response(404, json={"error": "not_found"})
        )


def client(store) -> Client:
    return Client(
        Store("https://store.example.test", "t" * 32),
        httpx.Client(transport=httpx.MockTransport(store)),
        sleep=lambda _: None,
    )


def page(records, after=0, cursor=3, more=False):
    return {
        "schema": fx.HISTORY_PAGE,
        "after": after,
        "next_cursor": cursor,
        "has_more": more,
        "records": records,
    }


@pytest.fixture
def world():
    text = report_text().encode()
    files = {"index.md": text, "current-findings.json": b'{"finding_count": 1}\n'}
    artifact, manifest = artifact_for(files)
    cited = [
        ref.url
        for f in fx.parse_report_artifact(text.decode()).findings
        for ref in f.reporting
    ]
    sources = [source_record(cited[0]), source_record("https://example.test/other")]
    runs = [
        run_record("1" * 64, 1, "succeeded", artifact, sources, published=True),
        run_record("2" * 64, 2, "failed", None, sources[:1]),
        run_record("3" * 64, 3, "in_progress", None, []),
    ]
    store = Store_({0: page([*sources, *runs])}, {artifact: (manifest, files)})
    return store, artifact, sources, runs, files


def test_findings_come_from_the_verified_accepted_artifact(world):
    store, artifact, sources, _, files = world
    doc = fx.build(client(store))
    assert doc["schema"] == fx.SCHEMA and doc["skipped_in_progress"] == 1
    done, failed = doc["entries"]
    assert done["findings_status"] == "parsed" and done["acceptance"] == fx.ACCEPTANCE
    assert done["report"]["artifact_sha256"] == artifact
    assert done["report"]["file_sha256"] == sha(files["index.md"])
    assert done["report"]["source_coverage"]["counts"]["cited_sources"] == 1
    [finding] = done["findings"]
    assert (
        finding["finding_key"] == f"sentryinsight:finding:{artifact}:{finding['slug']}"
    )
    assert (finding["basis"], finding["verification"]) == (fx.BASIS, fx.VERIFICATION)
    assert finding["description"], "the report's own description text"
    [citation] = finding["citations"]
    [evidence] = done["evidence"]
    assert (evidence["finding_key"], evidence["citation"]) == (
        finding["finding_key"],
        0,
    )
    assert evidence["reporting_fragment"] == citation["reporting_fragment"]
    assert evidence["link"] == "run_source"
    assert evidence["source_record_id"] == sources[0]["record_id"]
    assert evidence["article_key_sha256"] == sources[0]["article_key_sha256"]
    assert (
        done["report_published"] is True
        and done["publications"][0]["target"] == "production"
    )
    # A failed run is listed, with no artifact and no findings invented for it.
    assert (failed["outcome"], failed["reason"]) == ("failed", "malformed_markdown")
    assert (failed["findings"], failed["findings_status"], failed["report"]) == (
        [],
        "no_accepted_artifact",
        None,
    )
    assert failed["report_published"] is False


def test_every_record_is_sealed_and_the_export_is_deterministic(world):
    store = world[0]
    first = fx.canonical(fx.build(client(store)))
    assert (
        fx.canonical(fx.build(client(store))) == first
    ), "identical replay, identical bytes"
    doc = json.loads(first)
    for record, field in [
        (doc, "export_sha256"),
        *[(e, "entry_sha256") for e in doc["entries"]],
        *[(f, "finding_sha256") for e in doc["entries"] for f in e["findings"]],
    ]:
        body = {k: v for k, v in record.items() if k != field}
        assert record[field] == sha(fx.canonical(body))


def test_a_new_run_version_changes_its_entry_but_not_its_findings(world):
    store, artifact, sources, runs, files = world
    before = fx.build(client(store))
    newer = run_record(
        "1" * 64, 1, "succeeded", artifact, sources, version=2, published=True
    )
    newer["publications"].append({"target": "mirror", "state": "published"})
    store.pages = {
        0: page([*sources, runs[0], runs[1]], cursor=2, more=True),
        2: page([newer], after=2, cursor=4),
    }
    after = fx.build(client(store))
    old, new = before["entries"][0], after["entries"][0]
    assert new["run_record_version"] == 2, "the latest record version wins"
    assert new["entry_sha256"] != old["entry_sha256"]
    assert new["findings"] == old["findings"], "the accepted artifact is immutable"


def test_runs_sharing_one_artifact_share_finding_identity(world):
    store, artifact, sources, runs, _ = world
    twin = run_record("4" * 64, 4, "succeeded", artifact, sources)
    store.pages = {0: page([*sources, *runs, twin])}
    entries = fx.build(client(store))["entries"]
    keys = [
        (f["finding_key"], f["finding_sha256"]) for e in entries for f in e["findings"]
    ]
    assert len(keys) == 2 and keys[0] == keys[1], "one finding, seen in two runs"


def test_runs_sharing_an_artifact_keep_their_own_evidence_links(world):
    # The same report recorded twice, once with the cited source's fetched
    # text and once with only a feed excerpt (as a rebuild records it), and
    # once more with the citation not retained at all.
    store, artifact, sources, runs, _ = world
    excerpt = source_record(sources[0]["canonical_url"], content="feed excerpt")
    rebuilt = run_record("4" * 64, 4, "succeeded", artifact, [excerpt])
    bare = run_record("5" * 64, 5, "succeeded", artifact, [sources[1]])
    store.pages = {0: page([*sources, excerpt, *runs, rebuilt, bare])}
    done = [e for e in fx.build(client(store))["entries"] if e["findings"]]
    assert (
        len({fx.canonical(e["findings"]) for e in done}) == 1
    ), "one artifact, one finding record"
    links = [
        (e["evidence"][0]["link"], e["evidence"][0]["content_sha256"]) for e in done
    ]
    assert links == [
        ("run_source", sources[0]["content_sha256"]),
        ("run_source", excerpt["content_sha256"]),
        ("not_in_run_sources", None),
    ]
    assert len({e["entry_sha256"] for e in done}) == 3


def test_a_citation_the_run_cannot_back_is_marked_not_linked(world):
    store, artifact, sources, runs, _ = world
    runs[0]["sources"] = [{"source_record_id": sources[1]["record_id"]}]
    [evidence] = fx.build(client(store))["entries"][0]["evidence"]
    assert evidence["link"] == "not_in_run_sources"
    assert evidence["source_record_id"] is None and evidence["content_sha256"] is None


@pytest.mark.parametrize("tamper", ["file", "manifest"])
def test_bytes_that_do_not_match_the_run_are_refused(world, tamper):
    store, artifact, *_ = world
    manifest, files = store.artifacts[artifact]
    if tamper == "file":
        files = {**files, "index.md": files["index.md"] + b"\n"}
    else:
        manifest = copy.deepcopy(manifest)
        manifest["files"][0]["sha256"] = "0" * 64
    store.artifacts[artifact] = (manifest, files)
    with pytest.raises(fx.ExportError):
        fx.build(client(store))


def test_an_artifact_without_a_parseable_report_is_labelled_not_guessed(world):
    store, artifact, sources, runs, _ = world
    bad = {"index.md": b"# Not a versioned report\n"}
    other, manifest = artifact_for(bad)
    runs[0]["artifact"] = {"sha256": other}
    store.artifacts[other] = (manifest, bad)
    done = fx.build(client(store))["entries"][0]
    assert (done["findings_status"], done["findings"], done["report"]) == (
        "unparseable",
        [],
        None,
    )
    assert done["findings_note"]


def test_the_cli_writes_the_export_and_reports_its_digest(
    world, tmp_path, monkeypatch, capsys
):
    store = world[0]
    monkeypatch.setenv("CONTROL_PLANE_URL", "https://store.example.test")
    monkeypatch.setenv("CONTROL_PLANE_TOKEN", "t" * 32)
    real = httpx.Client
    monkeypatch.setattr(
        fx.httpx, "Client", lambda **kw: real(transport=httpx.MockTransport(store))
    )
    out = tmp_path / "findings.json"
    assert fx.main(["--out", str(out)]) == 0
    summary = json.loads(capsys.readouterr().out)
    assert summary["export_sha256"] == json.loads(out.read_text())["export_sha256"]
    assert (summary["entries"], summary["findings"]) == (2, 1)
    monkeypatch.delenv("CONTROL_PLANE_URL")
    assert fx.main(["--out", str(out)]) == 1


def test_the_committed_staging_fixture_is_sealed_and_labelled():
    from pathlib import Path

    path = Path(
        "backend/report-control-plane/fixtures/findings-export/staging-2026-11-09.json"
    )
    doc = json.loads(path.read_text())
    assert doc["schema"] == fx.SCHEMA

    def check(record, field):
        body = {k: v for k, v in record.items() if k != field}
        assert record[field] == sha(fx.canonical(body)), field

    check(doc, "export_sha256")
    statuses = {e["findings_status"] for e in doc["entries"]}
    assert {"parsed", "no_accepted_artifact"} <= statuses
    for e in doc["entries"]:
        check(e, "entry_sha256")
        assert bool(e["findings"]) == (e["findings_status"] == "parsed")
        for f in e["findings"]:
            check(f, "finding_sha256")
            assert (f["basis"], f["verification"]) == (fx.BASIS, fx.VERIFICATION)
            assert (
                f["finding_key"]
                == f"sentryinsight:finding:{e['report']['artifact_sha256']}:{f['slug']}"
            )
        keys = {f["finding_key"]: len(f["citations"]) for f in e["findings"]}
        assert len(e["evidence"]) == sum(keys.values()), "one link per citation"
        for ev in e["evidence"]:
            assert (
                ev["finding_key"] in keys and ev["citation"] < keys[ev["finding_key"]]
            )
            assert ev["link"] in {"run_source", "not_in_run_sources"}
            assert (ev["source_record_id"] is None) == (
                ev["link"] == "not_in_run_sources"
            )


def test_generated_at_is_the_same_instant_stated_in_utc(world):
    store, artifact, sources, runs, _ = world
    text = report_text().replace(
        "generated_at: 2026-11-02T12:00:00Z", "generated_at: 2026-11-02T12:00:00+05:00"
    )
    files = {"index.md": text.encode()}
    other, manifest = artifact_for(files)
    runs[0]["artifact"] = {"sha256": other}
    store.artifacts[other] = (manifest, files)
    done = fx.build(client(store))["entries"][0]
    assert done["findings_status"] == "parsed"
    assert done["report"]["generated_at"] == "2026-11-02T07:00:00Z"

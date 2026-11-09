// Projection of runs the authoritative producer already completed, against
// real local D1 and R2: immutable uploads, one-batch recording, replay,
// changed revisions, failed runs, observed publications in either order,
// interrupted projection, conflicts and the projector's narrow role.
import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { after, before, test } from "node:test";
import { ADMISSION, BINDING, admission, article, setup } from "./support/harness.mjs";

let env;
before(async () => {
  env = await setup();
  const seeded = await env.call("PUT", "/v1/pipelines/history", "operator", { policy_id: "standard", binding_id: sha("projection binding"), state: "active", mode: "project" });
  assert.equal(seeded.status, 200);
});
after(async () => {
  await env.stop();
});

const sha = (data) => createHash("sha256").update(data).digest("hex");
const commit = (label) => sha(label).slice(0, 40);
const runId = (id) => `sentryinsight:run:${id}`;
const sourceId = (link, content) => `sentryinsight:source:${sha(link)}:${sha(content)}`;
const latest = async () => new Map((await env.exportAll()).records.map((r) => [r.record_id, r]));
const tables = ["operations", "snapshots", "article_revisions", "operation_articles", "artifacts", "publications", "events", "export_changes", "identity_conflicts"];
const census = async () => Object.fromEntries(await Promise.all(tables.map(async (t) => [t, (await env.one(`SELECT count(*) AS n FROM ${t}`)).n])));

const upload = (bytes) => env.call("PUT", `/v1/projections/blobs/${sha(bytes)}`, "projector", bytes);
const segment = (a, b) => {
  const x = a.split("/");
  const y = b.split("/");
  for (let i = 0; i < Math.min(x.length, y.length); i += 1) if (x[i] !== y[i]) return x[i] < y[i] ? -1 : 1;
  return x.length - y.length;
};

// Upload a snapshot and report files, then post the projection.
async function projectRun({ revision, articles, files = null, outcome = "succeeded", reason = null, executed = null, sourceCommit = commit(revision), executionId = `actions-run-${sha(revision).slice(0, 8)}-1`, upload: doUpload = true }) {
  const snapshot = Buffer.from(JSON.stringify({ schema: ADMISSION, pipeline: "history", policy_id: "standard", source_revision: revision, articles }));
  const listing = files === null ? null : Object.entries(files).map(([path, text]) => ({ path, sha256: sha(text), bytes: Buffer.byteLength(text) })).sort((a, b) => segment(a.path, b.path));
  if (doUpload) {
    assert.ok([200, 201].includes((await upload(snapshot)).status));
    for (const text of Object.values(files ?? {})) assert.ok([200, 201].includes((await upload(Buffer.from(text))).status));
  }
  const body = {
    schema: "report-control-plane/projection/1",
    pipeline: "history",
    policy_id: "standard",
    source_revision: revision,
    snapshot_sha256: sha(snapshot),
    run: { execution_id: executionId, source_commit: outcome === "succeeded" ? sourceCommit : null, outcome, reason, executed_links: executed, completed_at: "2026-11-08T12:00:00Z" },
    artifact: listing === null ? null : { files: listing },
  };
  return { response: await env.call("POST", "/v1/projections", "projector", body), body, snapshot };
}

const observe = (sourceCommit, target = "github-pages", observedAt = "2026-11-08T12:05:00Z") =>
  env.call("POST", "/v1/projections/publications", "projector", {
    schema: "report-control-plane/publication-observation/1",
    pipeline: "history",
    source_commit: sourceCommit,
    target,
    observed_at: observedAt,
  });

const REPORT = { "index.md": "# Report\n", "current-findings.json": "{\"finding_count\": 1}\n", "reports/2026-11-08.md": "# Dated\n" };

test("a succeeded run is recorded once from verified uploads, replays as the same run, and exports with its provenance", async () => {
  const withTime = { ...article(8001, "Full text of an advisory."), content_kind: "article", published_at: "2026-11-07T09:30:00Z" };
  const excluded = { ...article(8002, "Feed text about an unrelated event."), content_kind: "feed" };
  const { response, snapshot } = await projectRun({ revision: "actions:1001:1", articles: [withTime, excluded], files: REPORT, executed: [withTime.link] });
  assert.equal(response.status, 201, JSON.stringify(response.body));
  const id = response.body.operation.operation_id;
  const row = await env.row(id);
  assert.deepEqual([row.state, row.origin, row.run_id, row.principal, row.executed_count], ["completed", "project", commit("actions:1001:1"), "projector", 1]);
  assert.equal((await env.r2(`snapshots/${sha(snapshot)}`)).length, 1, "the snapshot is retained under its digest");
  const file = await env.call("GET", `/v1/artifacts/${row.artifact_sha256}/files/current-findings.json`, "reader");
  assert.deepEqual(file.body, { finding_count: 1 });

  // Replay: identical projection, same operation, nothing new written.
  const before = await census();
  const replay = await projectRun({ revision: "actions:1001:1", articles: [withTime, excluded], files: REPORT, executed: [withTime.link], upload: false });
  assert.deepEqual([replay.response.status, replay.response.body.operation.operation_id], [200, id]);
  assert.deepEqual(await census(), before);

  const records = await latest();
  const run = records.get(runId(id));
  assert.deepEqual([run.run.origin, run.run.source_commit, run.run.outcome, run.report_published], ["project", commit("actions:1001:1"), "succeeded", false]);
  assert.deepEqual(run.sources.map((s) => s.outcome), ["executed", "excluded"]);
  assert.equal(records.get(sourceId(withTime.link, withTime.content)).times.published_at, "2026-11-07T09:30:00Z", "the producer's time is kept");
  assert.equal(records.get(sourceId(excluded.link, excluded.content)).times.published_at, null, "an absent time stays unknown");
  const retained = await env.call("GET", records.get(sourceId(withTime.link, withTime.content)).evidence.retained.fetch, "exporter");
  assert.equal(retained.body.content, withTime.content);
});

test("an observed deployment attaches whether it arrives before or after the run, once", async () => {
  const early = commit("observed-early");
  const pending = await observe(early, "github-pages", "2026-11-08T13:00:00Z");
  assert.deepEqual([pending.status, pending.body.runs], [202, []]);
  const { response } = await projectRun({ revision: "observed-early", articles: [article(8101)], files: { "index.md": "# Early\n" }, sourceCommit: early });
  const earlyId = response.body.operation.operation_id;

  const lateRun = await projectRun({ revision: "observed-late", articles: [article(8102)], files: { "index.md": "# Late\n" } });
  const lateId = lateRun.response.body.operation.operation_id;
  const observed = await observe(commit("observed-late"));
  assert.deepEqual([observed.status, observed.body.runs], [200, [lateId]]);
  assert.equal((await observe(commit("observed-late"), "github-pages", "2026-11-09T00:00:00Z")).body.observed_at, "2026-11-08T12:05:00Z", "the first observation is kept");

  const records = await latest();
  for (const [id, at] of [[earlyId, "2026-11-08T13:00:00Z"], [lateId, "2026-11-08T12:05:00Z"]]) {
    const run = records.get(runId(id));
    assert.deepEqual(run.publications.map((p) => [p.target, p.state, p.observed_at]), [["github-pages", "published", at]]);
    assert.equal(run.report_published, true);
  }
  assert.equal((await env.q("SELECT * FROM events WHERE operation_id = ? AND kind = 'publication_observed'", lateId)).length, 1);
});

test("a failed run, a changed revision and an interrupted projection are recorded truthfully", async () => {
  const failed = await projectRun({ revision: "actions:1201:1", articles: [article(8201)], outcome: "failed", reason: "generation_failed" });
  assert.equal(failed.response.status, 201);
  const failedId = failed.response.body.operation.operation_id;

  const first = article(8202, "First published text.");
  await projectRun({ revision: "actions:1202:1", articles: [first], files: { "index.md": "# One\n" } });
  const changed = { ...first, content: "Corrected published text." };

  // Interrupted after every byte is stored, before the batch: nothing is
  // recorded, and the retry records the run once.
  await env.fault("before_projection_batch");
  const interrupted = await projectRun({ revision: "actions:1203:1", articles: [changed], files: { "index.md": "# Two\n" } });
  assert.equal(interrupted.response.status, 500);
  assert.equal((await env.q("SELECT * FROM operations WHERE source_revision = 'actions:1203:1'")).length, 0);
  const retried = await projectRun({ revision: "actions:1203:1", articles: [changed], files: { "index.md": "# Two\n" }, upload: false });
  assert.equal(retried.response.status, 201);

  const records = await latest();
  const f = records.get(runId(failedId));
  assert.deepEqual([f.run.outcome, f.run.reason, f.artifact, f.report_published], ["failed", "generation_failed", null, false]);
  assert.deepEqual(f.sources.map((s) => s.outcome), ["not_reported"]);
  const revised = records.get(sourceId(changed.link, changed.content));
  assert.deepEqual([revised.revision.index, revised.revision.previous_content_sha256], [2, sha(first.content)]);
});

test("refusals: missing or wrong bytes, wrong pipeline, conflicts, and the projector's narrow role", async () => {
  const bytes = Buffer.from("not the declared digest");
  const wrong = await env.call("PUT", `/v1/projections/blobs/${sha("other")}`, "projector", bytes);
  assert.deepEqual([wrong.status, wrong.body.error], [422, "blob_digest_mismatch"]);

  const missing = await projectRun({ revision: "missing-1", articles: [article(8301)], files: REPORT, upload: false });
  assert.deepEqual([missing.response.status, missing.response.body.error], [409, "blob_missing"]);

  const reported = await projectRun({ revision: "conflict-p", articles: [article(8302)], files: { "index.md": "# P\n" } });
  const id = reported.response.body.operation.operation_id;
  const other = await projectRun({ revision: "conflict-p", articles: [article(8303)], files: { "index.md": "# Q\n" } });
  assert.deepEqual([other.response.status, other.response.body.error], [409, "source_revision_conflict"]);
  assert.equal((await latest()).get(runId(id)).identity_conflicts.length, 1);
  const rewritten = await projectRun({ revision: "conflict-p", articles: [article(8302)], files: { "index.md": "# P\n" }, executionId: "actions-run-other-1", upload: false });
  assert.deepEqual([rewritten.response.status, rewritten.response.body.error], [409, "projection_conflict"]);

  // An admission cannot write a projection pipeline, a projected run cannot be
  // published here, and a projection cannot write an execution pipeline.
  const admitted = await env.admit({ ...admission("history-admit", [article(8304)]), pipeline: "history" });
  assert.deepEqual([admitted.status, admitted.body.error], [422, "pipeline_projection_only"]);
  const published = await env.call("POST", `/v1/operations/${id}/publish`, "publisher", { target: "site" });
  assert.deepEqual([published.status, published.body.error], [409, "projection_not_publishable"]);
  const executePipeline = await env.call("POST", "/v1/projections", "projector", { ...reported.body, pipeline: "reports" });
  assert.deepEqual([executePipeline.status, executePipeline.body.error], [422, "pipeline_not_projection"]);
  assert.equal((await env.call("PUT", "/v1/pipelines/reports", "operator", { policy_id: "standard", binding_id: BINDING, state: "active" })).body.mode, "execute");

  for (const [method, route, body] of [
    ["POST", "/v1/operations", admission("projector-admit", [article(8305)])],
    ["GET", `/v1/operations/${id}`],
    ["GET", "/v1/export"],
    ["POST", "/v1/reconcile"],
  ]) {
    const response = await env.call(method, route, "projector", body);
    assert.deepEqual([response.status, response.body.error], [403, "forbidden"], `${method} ${route}`);
  }
  for (const who of ["manual", "exporter", "reader"]) {
    assert.equal((await env.call("POST", "/v1/projections", who, reported.body)).status, 403, who);
  }
});

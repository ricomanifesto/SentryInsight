// The research export and the product history it reads, against real local
// D1, R2 and Queue bindings: the end-to-end synthetic sequence, stable replay,
// a changed revision, a conflicting identity, missing evidence, syndicated
// copies, failed, incomplete and late outcomes, missing or corrupt retained
// content, a publication refusal that keeps last-good, interrupted recovery,
// paging, and the export role's read-only boundary.
import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { after, before, test } from "node:test";
import { REPORT_FILES, admission, admitted, article, completed, setup } from "./support/harness.mjs";

let env;
before(async () => {
  env = await setup();
});
after(async () => {
  await env.stop();
});

const sha = (data) => createHash("sha256").update(data).digest("hex");
const sourceId = (link, content) => `sentryinsight:source:${sha(link)}:${sha(content)}`;
const runId = (operationId) => `sentryinsight:run:${operationId}`;
const byId = (records) => new Map(records.map((r) => [r.record_id, r]));
const latest = async () => byId((await env.exportAll()).records);
const tables = ["operations", "snapshots", "article_revisions", "operation_articles", "artifacts", "publications", "targets", "events", "identity_conflicts"];
const census = async () => Object.fromEntries(await Promise.all(tables.map(async (t) => [t, (await env.one(`SELECT count(*) AS n FROM ${t}`)).n])));

function withKind(n, content, kind) {
  return { ...article(n, content), ...(kind === undefined ? {} : { content_kind: kind }) };
}

test("the MVP sequence: admit, retain, execute, verify, read back, publish, replay, revise", async () => {
  const fullText = withKind(9001, "Full article text about CVE-2026-0001.", "article");
  const excerpt = withKind(9002, "A short feed excerpt.", "feed");
  const body = admission("mvp-1", [fullText, excerpt]);

  // Admit and retain: the snapshot bytes are in R2 under their own digest.
  const first = await env.admit(body);
  assert.equal(first.status, 201);
  const id = first.body.operation.operation_id;
  const snapshot = first.body.operation.fingerprint;
  assert.equal(snapshot, sha(JSON.stringify(body)));
  const object = await env.stack.bucket.get(`snapshots/${snapshot}`);
  assert.equal(sha(new Uint8Array(await object.arrayBuffer())), snapshot);
  await env.waitState(id, "submitted");

  // Execute through the execution-service boundary; the service excludes one record.
  env.execution.succeed(id, REPORT_FILES, (job) => {
    job.executed = job.executed.filter((a) => a.article_key === fullText.link);
  });
  await env.reconcile();
  const done = await env.waitState(id, "completed");
  assert.equal(done.executed_count, 1);
  const marks = await env.q("SELECT article_key, executed FROM operation_articles WHERE operation_id = ? ORDER BY position", id);
  assert.deepEqual(marks.map((m) => m.executed), [1, 0]);

  // Read back the verified artifact through the read role.
  const file = await env.call("GET", `/v1/artifacts/${done.artifact_sha256}/files/reports/latest.json`, "reader");
  assert.deepEqual(file.body, { latest: true });

  // Publish, then export.
  assert.equal((await env.publish(id, "site-mvp")).status, 200);
  const records = await latest();
  const run = records.get(runId(id));
  assert.equal(run.schema, "sentryinsight-export/1");
  assert.equal(run.run.outcome, "succeeded");
  assert.equal(run.run.snapshot_sha256, snapshot);
  assert.equal(run.report_published, true);
  assert.deepEqual(run.publications.map((p) => [p.target, p.state]), [["site-mvp", "published"]]);
  assert.equal(run.artifact.sha256, done.artifact_sha256);
  assert.deepEqual(run.sources.map((s) => [s.source_record_id, s.outcome]), [
    [sourceId(fullText.link, fullText.content), "executed"],
    [sourceId(excerpt.link, excerpt.content), "excluded"],
  ]);
  assert.deepEqual(run.derived_claims, { status: "not_exported", reason: "artifact_not_interpreted" });
  const full = records.get(sourceId(fullText.link, fullText.content));
  assert.deepEqual([full.evidence.kind, full.canonical_url, full.publisher], ["full_text", fullText.link, "Example Source"]);
  assert.deepEqual([full.revision.index, full.revision.previous_content_sha256], [1, null]);
  assert.equal(full.times.published_at, null, "an unknown publication time stays unknown");
  assert.equal(full.first_seen_run_id, runId(id));
  assert.equal(records.get(sourceId(excerpt.link, excerpt.content)).evidence.kind, "excerpt");

  // The retained text is fetchable and re-verified; a digest alone is not text.
  const retained = await env.call("GET", full.evidence.retained.fetch, "exporter");
  assert.equal(retained.status, 200);
  assert.equal(retained.body.content, fullText.content);
  assert.equal(retained.body.content_sha256, full.content_sha256);

  // Replay: the same admission is the same operation, and the export is identical.
  const before = await census();
  const jobs = env.execution.jobCount();
  const repeat = await env.admit(body);
  assert.deepEqual([repeat.status, repeat.body.operation.operation_id], [200, id]);
  assert.deepEqual(await census(), before, "a replayed admission writes nothing");
  assert.equal(env.execution.jobCount(), jobs);
  const again = await latest();
  for (const key of [runId(id), full.record_id, sourceId(excerpt.link, excerpt.content)]) {
    assert.deepEqual(again.get(key), records.get(key), key);
  }

  // A changed revision: new content under the same URL is a distinct record
  // that names its predecessor; the unchanged record keeps its identity.
  const changed = { ...fullText, content: "Updated article text about CVE-2026-0001 with a fix." };
  const { cursor } = await env.exportAll();
  const next = await completed(env, admission("mvp-2", [changed, excerpt]));
  const delta = byId((await env.exportAll(cursor)).records);
  const revised = delta.get(sourceId(changed.link, changed.content));
  assert.deepEqual([revised.revision.index, revised.revision.previous_content_sha256], [2, sha(fullText.content)]);
  assert.equal(revised.canonical_url, fullText.link);
  assert.deepEqual(delta.get(sourceId(excerpt.link, excerpt.content)), records.get(sourceId(excerpt.link, excerpt.content)));
  assert.ok(delta.has(runId(next)));
  assert.ok(!delta.has(runId(id)), "the incremental page holds only what changed after the cursor");
});

test("a reused source revision with different bytes is refused, retained and visible once", async () => {
  const id = await completed(env, admission("conflict-x", [article(9101)]));
  const other = admission("conflict-x", [article(9102)]);
  for (let i = 0; i < 2; i += 1) {
    const refused = await env.admit(other);
    assert.deepEqual([refused.status, refused.body.error, refused.body.operation_id], [409, "source_revision_conflict", id]);
  }
  const refusedSnapshot = sha(JSON.stringify(other));
  assert.equal((await env.q("SELECT * FROM identity_conflicts WHERE refused_fingerprint = ?", refusedSnapshot)).length, 1);
  assert.equal((await env.q("SELECT * FROM events WHERE operation_id = ? AND kind = 'identity_conflict'", id)).length, 1);
  assert.equal((await env.r2(`snapshots/${refusedSnapshot}`)).length, 1, "the conflicting bytes are retained");
  assert.equal((await env.row(id)).state, "completed", "the existing operation is unchanged");
  const run = (await latest()).get(runId(id));
  assert.deepEqual(run.identity_conflicts.map((c) => [c.source_revision, c.refused_snapshot_sha256]), [["conflict-x", refusedSnapshot]]);
  const refusedText = await env.call("GET", `/v1/export/sources/${refusedSnapshot}/0`, "exporter");
  assert.deepEqual([refusedText.status, refusedText.body.content], [200, other.articles[0].content], "the conflicting content is readable");
});

test("revision order is commit order, not the Worker clock", async () => {
  const first = article(9151, "First text.");
  const second = { ...first, content: "Second text." };
  await completed(env, admission("clock-1", [first]));
  await completed(env, admission("clock-2", [second]));
  // A batch stamped earlier can commit later; model that skew directly.
  await env.stack.db.prepare("UPDATE article_revisions SET created_at = 0 WHERE article_key = ? AND content_sha256 = ?").bind(second.link, sha(second.content)).run();
  const records = await latest();
  const later = records.get(sourceId(second.link, second.content));
  assert.deepEqual([later.revision.index, later.revision.previous_content_sha256], [2, sha(first.content)]);
  assert.deepEqual(records.get(sourceId(first.link, first.content)).revision, { index: 1, previous_content_sha256: null });
});

test("missing evidence and syndicated copies are explicit, not corroboration", async () => {
  const text = "Identical wire copy about an exploited router.";
  const original = article(9201, text);
  const copy = { ...article(9202, text), source: "Syndicating Outlet" };
  const bare = article(9203, "");
  await completed(env, admission("syndication-1", [original, copy, bare]));
  const records = await latest();
  assert.deepEqual(records.get(sourceId(original.link, text)).independence, { status: "first_seen", same_content_first_url: null });
  assert.deepEqual(records.get(sourceId(copy.link, text)).independence, { status: "duplicate_content", same_content_first_url: original.link });
  const empty = records.get(sourceId(bare.link, ""));
  assert.deepEqual([empty.evidence.kind, empty.evidence.retained, empty.independence.status], ["metadata_only", null, "not_applicable"]);
  assert.equal(records.get(sourceId(original.link, text)).evidence.kind, "unspecified", "an absent coverage label is not guessed");
});

test("failed, incomplete and late outcomes stay separate from published findings", async () => {
  // Failed by the execution side.
  const failed = await admitted(env, admission("failed-1", [article(9301)]));
  env.execution.fail(failed, "generation_failed");
  await env.reconcile();
  const failedRow = await env.waitState(failed, "failed");

  // A late success after the failure changes nothing.
  env.execution.succeed(failed, REPORT_FILES);
  await env.reconcile();
  const lateRow = await env.row(failed);
  assert.deepEqual([lateRow.state, lateRow.version, lateRow.artifact_sha256], ["failed", failedRow.version, null]);

  // Incomplete: delivery dead-lettered before any execution.
  await env.fault("after_intent_before_send");
  assert.equal((await env.admit(admission("incomplete-1", [article(9302)]))).status, 500);
  const incomplete = (await env.one("SELECT operation_id FROM operations WHERE source_revision = 'incomplete-1'")).operation_id;
  await env.stack.worker.queue(env.stack.queues.dead, [{ id: "dlq-export", timestamp: new Date(), attempts: 1, body: { operation_id: incomplete, generation: 1 } }]);
  await env.waitState(incomplete, "dead_letter");

  const records = await latest();
  const f = records.get(runId(failed));
  assert.deepEqual([f.run.outcome, f.run.reason, f.run.execution.run_state, f.report_published, f.artifact], ["failed", "generation_failed", "failed", false, null]);
  assert.deepEqual(f.sources.map((s) => s.outcome), ["not_reported"]);
  const i = records.get(runId(incomplete));
  assert.deepEqual([i.run.outcome, i.run.reason, i.run.execution, i.report_published], ["incomplete", "delivery_exhausted", null, false]);
});

test("missing or corrupt retained content fails the run truthfully and is reported on fetch", async () => {
  async function held(label, n) {
    await env.fault("after_intent_before_send");
    assert.equal((await env.admit(admission(label, [article(n)]))).status, 500);
    return env.one("SELECT * FROM operations WHERE source_revision = ?", label);
  }
  const missing = await held("retained-missing", 9401);
  const corrupt = await held("retained-corrupt", 9402);
  await env.stack.bucket.delete(`snapshots/${missing.fingerprint}`);
  await env.stack.bucket.put(`snapshots/${corrupt.fingerprint}`, "{\"articles\": [not json");
  await env.waitFor(async () => {
    await env.reconcile();
    const rows = await Promise.all([env.row(missing.operation_id), env.row(corrupt.operation_id)]);
    return rows.every((r) => r.state === "failed");
  });
  const jobs = env.execution.jobCount();
  for (const row of [missing, corrupt]) {
    const current = await env.row(row.operation_id);
    assert.equal(current.reason, "snapshot_unavailable");
    assert.equal(env.execution.jobFor(row.operation_id), undefined, "nothing was sent for execution");
  }
  assert.equal(env.execution.jobCount(), jobs);
  const records = await latest();
  assert.equal(records.get(runId(missing.operation_id)).run.outcome, "failed");
  assert.equal(records.get(runId(missing.operation_id)).run.reason, "snapshot_unavailable");
  const fetchMissing = await env.call("GET", `/v1/export/sources/${missing.fingerprint}/0`, "exporter");
  assert.deepEqual([fetchMissing.status, fetchMissing.body.error], [404, "retained_content_unavailable"]);
  const fetchCorrupt = await env.call("GET", `/v1/export/sources/${corrupt.fingerprint}/0`, "exporter");
  assert.deepEqual([fetchCorrupt.status, fetchCorrupt.body.error], [409, "retained_content_mismatch"]);
});

test("a refused publication keeps the last-good report and is exported as refused", async () => {
  const older = await completed(env, admission("refusal-old", [article(9501)]), { "index.html": "old\n" });
  const newer = await completed(env, admission("refusal-new", [article(9502)]), { "index.html": "new\n" });
  assert.equal((await env.publish(newer, "site-refusal")).status, 200);
  const lastGood = await env.one("SELECT * FROM targets WHERE target = 'site-refusal'");
  const refused = await env.publish(older, "site-refusal");
  assert.deepEqual([refused.status, refused.body.error], [409, "stale_candidate"]);
  assert.deepEqual(await env.one("SELECT * FROM targets WHERE target = 'site-refusal'"), lastGood, "last-good is not replaced");
  const records = await latest();
  const o = records.get(runId(older));
  assert.deepEqual(o.publications.map((p) => [p.state, p.reason]), [["refused", "stale_candidate"]]);
  assert.equal(o.report_published, false);
  assert.equal(o.run.outcome, "succeeded", "a verified artifact is not a published report");
  const published = records.get(runId(newer));
  assert.equal(published.report_published, true);
  // The claim that led to the effect is audited in its own batch, so every
  // exported publication state arrives with an event and a new record_version.
  const claimed = await env.q("SELECT * FROM events WHERE subject = ? AND kind = 'publication_claimed'", published.publications[0].publication_id);
  assert.equal(claimed.length, 1);
  assert.ok(published.record_version >= claimed[0].id);
});

test("an interrupted handoff recovers, and the run record advances by version", async () => {
  await env.fault("after_intent_before_send");
  assert.equal((await env.admit(admission("interrupted-1", [article(9601)]))).status, 500);
  const id = (await env.one("SELECT operation_id FROM operations WHERE source_revision = 'interrupted-1'")).operation_id;
  const pending = (await latest()).get(runId(id));
  assert.equal(pending.run.outcome, "in_progress");
  await env.waitFor(async () => {
    await env.reconcile();
    return (await env.row(id)).state === "submitted";
  });
  env.execution.succeed(id, REPORT_FILES);
  await env.reconcile();
  await env.waitState(id, "completed");
  const recovered = (await latest()).get(runId(id));
  assert.equal(recovered.run.outcome, "succeeded");
  assert.ok(recovered.record_version > pending.record_version);
  assert.notEqual(recovered.record_sha256, pending.record_sha256);
  assert.equal((await env.q("SELECT * FROM operations WHERE source_revision = 'interrupted-1'")).length, 1);
  assert.equal(env.execution.counters.jobsCreated, env.execution.jobCount(), "one job per converged source set");
});

test("pages are bounded and their union is the full export", async () => {
  const whole = await env.exportAll();
  const paged = await env.exportAll(0, 1);
  const runs = (records) => records.filter((r) => r.record_type === "run");
  assert.deepEqual(byId(paged.records), byId(whole.records));
  assert.equal(paged.cursor, whole.cursor);
  const first = await env.exportPage(0, 1);
  assert.equal(runs(first.body.records).length, 1);
  assert.equal(first.body.has_more, true);
  assert.equal(first.body.coverage.gaps[0].kind, "before_first_admission");
  const tail = await env.exportPage(whole.cursor);
  assert.deepEqual([tail.body.records.length, tail.body.has_more, tail.body.next_cursor], [0, false, whole.cursor]);
  assert.ok(runs(whole.records).length >= 10);
});

test("the export role reads the export only, never writes, and leaks no operational identity", async () => {
  const id = (await env.one("SELECT operation_id FROM operations ORDER BY seq LIMIT 1")).operation_id;
  const before = await census();
  const page = await env.exportPage();
  assert.equal(page.status, 200);
  assert.deepEqual(await census(), before, "reading the export writes nothing");
  const text = JSON.stringify(page.body);
  for (const secret of Object.values(env.tokens)) assert.ok(!text.includes(secret));
  for (const field of ["principal", "claim_token", "receipt", "binding_id", "transition_nonce"]) assert.ok(!text.includes(`"${field}"`), field);
  // Principal names as values ("publisher" is also a record key, so it is not checked here).
  for (const name of ["manual", "operator", "reader", "exporter", "scheduler"]) assert.ok(!text.includes(`"${name}"`), name);
  const tokens = await env.q("SELECT claim_token FROM operations WHERE claim_token IS NOT NULL UNION SELECT claim_token FROM targets WHERE claim_token IS NOT NULL UNION SELECT receipt FROM publications WHERE receipt IS NOT NULL");
  for (const { claim_token: value } of tokens) assert.ok(!text.includes(value), "no stored token or receipt value");

  const denied = [
    ["POST", "/v1/operations", admission("export-write", [article(9701)])],
    ["GET", `/v1/operations/${id}`],
    ["POST", `/v1/operations/${id}/publish`, { target: "site" }],
    ["POST", "/v1/reconcile"],
    ["PUT", "/v1/pipelines/reports", { policy_id: "standard", binding_id: sha("x"), state: "retired" }],
    ["POST", `/v1/operations/${id}/retry`],
    ["GET", "/v1/targets/site-mvp"],
    ["GET", `/v1/artifacts/${sha("x")}`],
    ["GET", `/v1/artifacts/${sha("x")}/files/index.html`],
    ["PUT", "/v1/schedules/s1", { pipeline: "reports", policy_id: "standard", state: "paused" }],
    ["PUT", "/v1/schedules/s1/sources", { schema: "report-control-plane/source-bundle/1", articles: [article(9702)] }],
  ];
  for (const [method, route, body] of denied) {
    const response = await env.call(method, route, "exporter", body);
    assert.deepEqual([response.status, response.body.error], [403, "forbidden"], `${method} ${route}`);
  }
  assert.equal((await env.call("GET", "/v1/export", "reader")).status, 403);
  assert.equal((await env.call("GET", "/v1/export")).status, 401);
  for (const query of ["limit=0", "limit=26", "after=-1", "after=1&after=2", "cursor=1", "after=1e3"]) {
    const response = await env.call("GET", `/v1/export?${query}`, "exporter");
    assert.deepEqual([response.status, response.body.error], [422, "export_query_invalid"], query);
  }
  assert.deepEqual(await census(), before);
});

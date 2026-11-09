// Admission against the real local D1, R2 and Queue: A1 to A5, A7, A8, A36,
// A37, the scheduled entry (A2a) and scheduled reconciliation (A2b).
import assert from "node:assert/strict";
import { after, before, test } from "node:test";
import { BUNDLE, admission, admitted, article, setup, sleep } from "./support/harness.mjs";

let env;
before(async () => {
  env = await setup();
});
after(async () => {
  await env.stop();
});

test("A1 authenticated manual admission reaches submitted through the real Queue", async () => {
  const before = await env.counts();
  const response = await env.admit(admission("manual-1"));
  assert.equal(response.status, 201);
  const id = response.body.operation.operation_id;
  const row = await env.waitState(id, "submitted");
  assert.equal(row.principal, "manual");
  assert.match(row.execution_id, /^exec-/);
  const after = await env.counts();
  assert.equal(after.operations, before.operations + 1);
  assert.equal(after.snapshots, before.snapshots + 1);
  assert.equal(after.jobs, before.jobs + 1);
  assert.deepEqual((await env.r2(`snapshots/${row.fingerprint}`)).length, 1);
  const kinds = (await env.q("SELECT kind FROM events WHERE operation_id = ? ORDER BY id", id)).map((e) => e.kind);
  assert.deepEqual(kinds, ["admitted", "submitted"]);
});

test("A2a event principal and scheduled admission share the admission path", async () => {
  const response = await env.admit(admission("event-1", [article(21)]), "event");
  assert.equal(response.status, 201);
  assert.equal(response.body.operation.principal, "event");
  await env.waitState(response.body.operation.operation_id, "submitted");

  assert.equal((await env.call("PUT", "/v1/schedules/daily", "operator", { pipeline: "reports", policy_id: "standard", state: "active" })).status, 200);
  const bundle = JSON.stringify({ schema: BUNDLE, articles: [article(31), article(32)] });
  const staged = await env.call("PUT", "/v1/schedules/daily/sources", "manual", bundle);
  assert.equal(staged.status, 202);
  const before = await env.counts();
  await env.stack.worker.scheduled({ cron: "*/5 * * * *" });
  const scheduled = await env.q("SELECT * FROM operations WHERE principal = 'scheduler'");
  assert.equal(scheduled.length, 1);
  assert.equal(scheduled[0].source_revision, `schedule:daily:${staged.body.pending_bundle_sha256}`);
  assert.equal(scheduled[0].fingerprint, staged.body.pending_bundle_sha256);
  const schedule = await env.one("SELECT * FROM schedules WHERE schedule_id = 'daily'");
  assert.equal(schedule.last_admitted_fingerprint, staged.body.pending_bundle_sha256);
  assert.equal((await env.counts()).operations, before.operations + 1);
  await env.waitState(scheduled[0].operation_id, "submitted");
  // A refire admits nothing new.
  await env.stack.worker.scheduled({ cron: "*/5 * * * *" });
  assert.equal((await env.counts()).operations, before.operations + 1);
  assert.equal((await env.r2(`snapshots/${staged.body.pending_bundle_sha256}`)).length, 1);
});

test("A2b scheduled reconciliation alone sweeps and admits nothing", async () => {
  await sleep(300);
  const before = await env.counts();
  const sends = (await env.one("SELECT sum(send_attempts) AS n FROM operations")).n;
  const sweeps = (await env.one("SELECT count(*) AS n FROM events WHERE kind = 'sweep'")).n;
  await env.stack.worker.scheduled({ cron: "*/5 * * * *" });
  assert.deepEqual(await env.counts(), before);
  assert.equal((await env.one("SELECT sum(send_attempts) AS n FROM operations")).n, sends);
  assert.equal((await env.one("SELECT count(*) AS n FROM events WHERE kind = 'sweep'")).n, sweeps + 1);
});

test("A3 an unauthenticated or unauthorized caller changes nothing", async () => {
  const before = await env.counts();
  const submits = env.execution.counters.submits;
  const body = admission("unauthorized-1", [article(41)]);
  assert.equal((await env.admit(body, null)).status, 401);
  assert.equal((await env.admit(body, "not-a-real-token-value-xyz")).status, 401);
  assert.equal((await env.admit(body, "reader")).status, 403);
  assert.equal((await env.call("POST", "/v1/reconcile", "manual")).status, 403);
  assert.equal((await env.call("PUT", "/v1/pipelines/reports", "manual", {})).status, 403);
  await sleep(1500);
  assert.deepEqual(await env.counts(), before);
  assert.equal(env.execution.counters.submits, submits);
});

test("A4 parallel identical requests make one operation, object and job", async () => {
  const before = await env.counts();
  const body = admission("dup-1", [article(51)]);
  const responses = await Promise.all(Array.from({ length: 8 }, () => env.admit(body)));
  const ids = new Set(responses.map((r) => r.body.operation.operation_id));
  assert.equal(ids.size, 1);
  assert.equal(responses.filter((r) => r.status === 201).length, 1);
  assert.ok(responses.every((r) => r.status === 201 || r.status === 200));
  const [id] = ids;
  await env.waitState(id, "submitted");
  const after = await env.counts();
  assert.equal(after.operations, before.operations + 1);
  assert.equal(after.max_seq, before.max_seq + 1);
  assert.equal(after.snapshots, before.snapshots + 1);
  assert.equal(after.r2, before.r2 + 1);
  assert.equal(after.jobs, before.jobs + 1);
});

test("A5 A7 A37 conflicting reuse of a source revision is refused and rolled back", async () => {
  const before = await env.counts();
  const lastGood = await env.q("SELECT * FROM targets");
  const bodies = [61, 62, 63, 64, 65].map((n) => admission("conflict-1", [article(n), article(n + 100)]));
  const responses = await Promise.all(bodies.map((b) => env.admit(b)));
  assert.equal(responses.filter((r) => r.status === 201).length, 1);
  assert.equal(responses.filter((r) => r.status === 409 && r.body.error === "source_revision_conflict").length, 4);
  const winner = responses.find((r) => r.status === 201).body.operation.operation_id;
  await env.waitState(winner, "submitted");
  const after = await env.counts();
  assert.equal(after.operations, before.operations + 1);
  assert.equal(after.max_seq, before.max_seq + 1, "a rolled-back batch consumes no sequence value");
  assert.equal(after.snapshots, before.snapshots + 1);
  assert.equal(after.operation_articles, before.operation_articles + 2, "losers' article rows rolled back");
  assert.equal(after.article_revisions, before.article_revisions + 2);
  assert.equal(after.r2, before.r2 + 5, "losers' snapshots remain as harmless orphans");
  assert.deepEqual(await env.q("SELECT * FROM targets"), lastGood);
  // A sequential repeat of a loser is still a conflict, and still writes nothing.
  assert.equal((await env.admit(bodies.find((b, i) => responses[i].status === 409))).status, 409);
  assert.equal((await env.counts()).max_seq, after.max_seq);
});

test("A36 article metadata equals the admitted set and is queryable", async () => {
  const articles = [article(71), article(72, "different content")];
  const id = await admitted(env, admission("articles-1", articles));
  const rows = await env.q("SELECT article_key, content_sha256, position FROM operation_articles WHERE operation_id = ? ORDER BY position", id);
  assert.deepEqual(rows.map((r) => r.article_key), articles.map((a) => a.link));
  const revisions = await env.q("SELECT * FROM article_revisions WHERE article_key = ?", articles[1].link);
  assert.equal(revisions.length, 1);
  assert.equal(revisions[0].first_operation_id, id);
  // A new content for the same key is a new revision, never an update.
  const id2 = await admitted(env, admission("articles-2", [article(72, "changed content")]));
  assert.equal((await env.q("SELECT * FROM article_revisions WHERE article_key = ?", articles[1].link)).length, 2);
  const consumers = await env.q("SELECT DISTINCT operation_id FROM operation_articles WHERE article_key = ? ORDER BY operation_id", articles[1].link);
  assert.deepEqual(consumers.map((c) => c.operation_id).sort(), [id, id2].sort());
});

test("malformed, oversized and unsupported requests fail closed with no write", async () => {
  const before = await env.counts();
  const duplicate = `{"schema":"report-control-plane/admission/1","pipeline":"reports","policy_id":"standard","source_revision":"m1","source_revision":"m2","articles":[]}`;
  const cases = [
    [duplicate, 422, "request_malformed"],
    [JSON.stringify(admission("m3", [article(81), article(81)])), 422, "article_duplicate_key"],
    [JSON.stringify({ ...admission("m4"), extra: true }), 422, "field_unknown"],
    [JSON.stringify(admission("m5", [article(82)], { pipeline: "unknown" })), 422, "pipeline_unavailable"],
    [JSON.stringify(admission("m6", [article(83)], { policy_id: "other" })), 422, "policy_unsupported"],
    ["x".repeat(1024 * 1024 + 1), 413, "request_too_large"],
  ];
  for (const [body, status, reason] of cases) {
    const response = await env.admit(body);
    assert.equal(response.status, status, reason);
    assert.equal(response.body.error, reason);
  }
  assert.deepEqual(await env.counts(), before);
});

test("W-1 interruption after the snapshot, before the batch, leaves only an orphan object", async () => {
  const before = await env.counts();
  await env.fault("after_snapshot_before_batch");
  const response = await env.admit(admission("w1", [article(91)]));
  assert.equal(response.status, 500);
  const after = await env.counts();
  assert.equal(after.operations, before.operations);
  assert.equal(after.r2, before.r2 + 1);
});

test("A8 interruption after durable intent, before send: the sweeper delivers it once", async () => {
  await env.fault("after_intent_before_send");
  const body = admission("a8", [article(101)]);
  const response = await env.admit(body);
  assert.equal(response.status, 500);
  const row = await env.one("SELECT * FROM operations WHERE source_revision = 'a8'");
  assert.equal(row.state, "admitted");
  const submits = env.execution.counters.submits;
  await sleep(1500);
  assert.equal((await env.row(row.operation_id)).state, "admitted", "nothing was sent");
  assert.equal(env.execution.counters.submits, submits);
  await env.reconcile();
  const done = await env.waitState(row.operation_id, "submitted");
  assert.equal(done.send_attempts, 2);
  assert.equal(env.execution.jobFor(row.operation_id).execution_id, done.execution_id);
  // Repeating the identical request returns the same operation.
  const repeat = await env.admit(body);
  assert.equal(repeat.status, 200);
  assert.equal(repeat.body.operation.operation_id, row.operation_id);
});

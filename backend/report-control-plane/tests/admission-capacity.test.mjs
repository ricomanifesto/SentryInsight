import assert from "node:assert/strict";
import { test } from "node:test";
import { createHash } from "node:crypto";
import { ADMISSION_LIMITS, admit, recordAdmissionRefusal } from "../src/admission.js";
import { parseAdmission } from "../src/request.js";
import { BINDING, BUNDLE, admission, article, setup } from "./support/harness.mjs";

async function withEnv(fn) {
  const env = await setup();
  try { await fn(env); } finally { await env.stop(); }
}

async function fillAttempts(env, remaining = 0) {
  await env.stack.db.prepare(`WITH RECURSIVE n(x) AS (SELECT 1 UNION ALL SELECT x + 1 FROM n WHERE x < ?)
    INSERT INTO admission_reservations (operation_id, pipeline, fingerprint, principal, state, created_at)
    SELECT printf('%064x', x), 'fixture', printf('%064x', x), 'fixture', 'reserved', 0 FROM n`)
    .bind(ADMISSION_LIMITS.attempts - remaining).run();
}

test("aggregate admission slots serialize across principals and pipelines before R2 writes", async () => withEnv(async (env) => {
  await fillAttempts(env, 1);
  await env.call("PUT", "/v1/pipelines/other", "operator", { policy_id: "standard", binding_id: BINDING, state: "active" });
  const bodies = Array.from({ length: 6 }, (_, i) => admission(`capacity-${i}`, [article(i)], { pipeline: i % 2 ? "reports" : "other" }));
  const before = await env.counts();
  const responses = await Promise.all(bodies.map((body, i) => env.admit(body, i % 2 ? "manual" : "event")));
  assert.equal(responses.filter((r) => r.status === 201).length, 1);
  assert.equal(responses.filter((r) => r.status === 429 && r.body.error === "admission_capacity_exhausted").length, 5);
  assert.equal((await env.counts()).r2, before.r2 + 1);
  assert.equal((await env.one("SELECT count(*) AS n FROM admission_reservations")).n, ADMISSION_LIMITS.attempts);
  const winner = responses.findIndex((r) => r.status === 201);
  const replay = await env.admit(bodies[winner], "operator");
  assert.equal(replay.status, 200, "existing operations do not require spare capacity");
  assert.equal(replay.body.operation.operation_id, responses[winner].body.operation.operation_id);
  assert.equal((await env.one("SELECT sum(occurrences) AS n FROM admission_refusals WHERE reason = 'admission_capacity_exhausted'")).n, 5);
}));

test("snapshot byte capacity is atomic and also gates scheduled source staging", async () => withEnv(async (env) => {
  const body = admission("byte-boundary", [article(20)]);
  const bytes = Buffer.byteLength(JSON.stringify(body));
  await env.stack.db.prepare("INSERT INTO admission_snapshots (fingerprint, bytes, created_at) VALUES (?, ?, 0)")
    .bind("f".repeat(64), ADMISSION_LIMITS.snapshotBytes - bytes).run();
  const responses = await Promise.all([env.admit(body), env.admit(admission("byte-over", [article(21)]), "event")]);
  assert.equal(responses.filter((r) => r.status === 201).length, 1);
  assert.equal(responses.filter((r) => r.status === 429).length, 1);
  assert.equal((await env.r2()).length, 1);
  assert.ok((await env.one("SELECT sum(bytes) AS n FROM admission_snapshots")).n <= ADMISSION_LIMITS.snapshotBytes);
  await env.call("PUT", "/v1/schedules/bounded", "operator", { pipeline: "reports", policy_id: "standard", state: "active" });
  const before = await env.r2();
  const staged = await env.call("PUT", "/v1/schedules/bounded/sources", "event", { schema: BUNDLE, articles: [article(22)] });
  assert.equal(staged.status, 429);
  assert.deepEqual(await env.r2(), before);
  assert.equal((await env.one("SELECT pending_bundle_sha256 FROM schedules WHERE schedule_id = 'bounded'")).pending_bundle_sha256, null);
}));

test("a partial storage failure keeps a reusable reservation at the aggregate cap", async () => withEnv(async (env) => {
  const body = admission("reserved-retry", [article(30)]);
  await env.fault("after_snapshot_before_batch");
  assert.equal((await env.admit(body)).status, 500);
  const reservation = await env.one("SELECT * FROM admission_reservations");
  assert.equal(reservation.principal, "manual");
  assert.equal(reservation.state, "reserved");
  const before = await env.r2();
  await fillAttempts(env, 1);
  assert.equal((await env.admit(admission("reserved-other", [article(31)]))).status, 429);
  assert.equal((await env.admit(body, "event")).status, 201);
  assert.deepEqual(await env.r2(), before);
  assert.equal((await env.one("SELECT state FROM admission_reservations WHERE operation_id = ?", reservation.operation_id)).state, "admitted");
}));

test("conflicts and malformed admission refusals identify the authenticated caller without bearer tokens", async () => withEnv(async (env) => {
  const first = await env.admit(admission("audit-owner", [article(40)]), "manual");
  const refused = admission("audit-owner", [article(41)]);
  assert.equal((await env.admit(refused, "event")).status, 409);
  await fillAttempts(env, 2);
  const retained = await env.r2();
  assert.equal((await env.admit(refused, "operator")).status, 409);
  assert.deepEqual(await env.r2(), retained, "a known conflict stays replayable at capacity");
  const conflict = await env.one("SELECT * FROM identity_conflicts");
  assert.equal(conflict.principal, "event", "first authenticated observer owns the immutable conflict audit");
  const events = await env.q("SELECT * FROM events WHERE kind = 'identity_conflict'");
  assert.equal(events.length, 1);
  assert.equal(events[0].principal, "event");
  assert.equal(events[0].token, "source_revision_conflict");
  assert.equal(events[0].operation_id, first.body.operation.operation_id);
  assert.equal((await env.admit({ ...admission("bad"), unknown: true }, "event")).status, 422);
  const audit = await env.one("SELECT * FROM admission_refusals WHERE principal = 'event' AND reason = 'field_unknown'");
  assert.equal(audit.occurrences, 1);
  for (const token of Object.values(env.tokens)) assert.ok(!JSON.stringify({ conflict, events, audit }).includes(token));
  const before = await env.q("SELECT * FROM admission_refusals ORDER BY rowid");
  assert.equal((await env.admit(admission("unauthorized"), null)).status, 401);
  assert.deepEqual(await env.q("SELECT * FROM admission_refusals ORDER BY rowid"), before);
}));

test("an R2 write error retains capacity and the exact request can recover", async () => withEnv(async (env) => {
  const body = admission("r2-retry", [article(45)]);
  const bytes = new Uint8Array(Buffer.from(JSON.stringify(body)));
  const parsed = await parseAdmission(bytes);
  const fingerprint = createHash("sha256").update(bytes).digest("hex");
  const unavailable = { PRODUCT_DB: env.stack.db, ARTIFACTS: { put() { throw new Error("synthetic storage unavailable"); } } };
  await assert.rejects(admit(unavailable, { executionConfigured: true }, { ...parsed, principal: "manual", bytes, fingerprint }), /synthetic storage unavailable/);
  assert.equal((await env.r2()).length, 0);
  assert.equal((await env.one("SELECT state FROM admission_reservations")).state, "reserved");
  assert.equal((await env.one("SELECT bytes FROM admission_snapshots WHERE fingerprint = ?", fingerprint)).bytes, bytes.byteLength);
  assert.equal((await env.admit(body)).status, 201);
  assert.equal((await env.one("SELECT count(*) AS n FROM admission_reservations")).n, 1);
}));

test("snapshot identity capacity gates staging and known staged replays remain bounded", async () => withEnv(async (env) => {
  await env.call("PUT", "/v1/schedules/replayed", "operator", { pipeline: "reports", policy_id: "standard", state: "paused" });
  const bundle = { schema: BUNDLE, articles: [article(50)] };
  assert.equal((await env.call("PUT", "/v1/schedules/replayed/sources", "manual", bundle)).status, 202);
  await env.stack.db.prepare(`WITH RECURSIVE n(x) AS (SELECT 1 UNION ALL SELECT x + 1 FROM n WHERE x < ?)
    INSERT INTO admission_snapshots (fingerprint, bytes, created_at) SELECT printf('%064x', x), 1, 0 FROM n`)
    .bind(ADMISSION_LIMITS.snapshots - 1).run();
  const objects = await env.r2();
  assert.equal((await env.call("PUT", "/v1/schedules/replayed/sources", "event", { schema: BUNDLE, articles: [article(51)] })).status, 429);
  for (let i = 0; i < 3; i += 1) {
    assert.equal((await env.call("PUT", "/v1/schedules/replayed/sources", "event", bundle)).status, 202);
  }
  assert.deepEqual(await env.r2(), objects);
  assert.equal((await env.one("SELECT count(*) AS n FROM events WHERE kind = 'schedule_staged'")).n, 0);
  const schedule = await env.one("SELECT * FROM schedules WHERE schedule_id = 'replayed'");
  assert.equal(schedule.staged_by, "event");
  assert.equal(schedule.staging_count, 4);
}));

test("refusal diagnostics remain bounded when authenticated principal names rotate", async () => withEnv(async (env) => {
  for (let i = 0; i < ADMISSION_LIMITS.refusalCells + 4; i += 1) {
    await recordAdmissionRefusal(env.stack.db, { principal: `synthetic-${i}`, reason: "field_unknown" });
  }
  assert.equal((await env.one("SELECT count(*) AS n FROM admission_refusals")).n, ADMISSION_LIMITS.refusalCells + 1);
  const overflow = await env.one("SELECT * FROM admission_refusals WHERE audit_key = 'overflow'");
  assert.equal(overflow.occurrences, 4);
  assert.equal(overflow.principal, `synthetic-${ADMISSION_LIMITS.refusalCells + 3}`);
  await recordAdmissionRefusal(env.stack.db, { principal: "synthetic-0", reason: "field_unknown" });
  assert.equal((await env.one("SELECT occurrences FROM admission_refusals WHERE principal = 'synthetic-0'")).occurrences, 2);
}));

test("scheduled admission cap refusals preserve scheduler attribution", async () => withEnv(async (env) => {
  await env.call("PUT", "/v1/schedules/full", "operator", { pipeline: "reports", policy_id: "standard", state: "active" });
  await env.call("PUT", "/v1/schedules/full/sources", "manual", { schema: BUNDLE, articles: [article(60)] });
  await fillAttempts(env);
  await env.stack.worker.scheduled({ cron: "*/5 * * * *" });
  const audit = await env.one("SELECT * FROM admission_refusals WHERE principal = 'scheduler'");
  assert.equal(audit?.reason, "admission_capacity_exhausted");
  assert.equal((await env.counts()).operations, 0);
}));

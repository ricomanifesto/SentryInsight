// Persistence and concurrency on the real local engine: A20 reopen, A12
// restarts at two windows (product side), a Queue message pending across a
// restart, and A21 parallel handler and D1 requests.
import assert from "node:assert/strict";
import { after, before, test } from "node:test";
import { REPORT_FILES, admission, admitted, article, completed, setup, sleep } from "./support/harness.mjs";

let env;
before(async () => {
  env = await setup();
});
after(async () => {
  await env.stop();
});

const TABLES = ["pipelines", "snapshots", "operations", "article_revisions", "operation_articles", "artifacts", "publications", "targets", "schedules", "events"];
async function dump() {
  const tables = {};
  for (const t of TABLES) tables[t] = await env.q(`SELECT * FROM ${t} ORDER BY rowid`);
  return { tables, objects: await env.r2() };
}

test("A20 persisted rows and objects are identical after a reopen", async () => {
  const id = await completed(env, admission("a20", [article(1)]));
  assert.equal((await env.publish(id, "site-a20")).status, 200);
  const before = await dump();
  await env.restart();
  assert.deepEqual(await dump(), before);
  const next = await admitted(env, admission("a20-after", [article(2)]));
  assert.equal((await env.row(next)).seq, Math.max(...before.tables.operations.map((o) => o.seq)) + 1);
});

test("A12 product side: restart after intent and after execution completes; no duplicate work", async () => {
  await env.fault("after_intent_before_send");
  const response = await env.admit(admission("a12", [article(3)]));
  assert.equal(response.status, 500);
  const id = (await env.one("SELECT operation_id FROM operations WHERE source_revision = 'a12'")).operation_id;
  await env.restart();
  await sleep(300);
  await env.reconcile();
  await env.waitState(id, "submitted");
  const jobs = env.execution.counters.jobsCreated;
  env.execution.succeed(id, REPORT_FILES);
  await env.restart();
  await env.reconcile();
  const row = await env.waitState(id, "completed");
  assert.equal(env.execution.counters.jobsCreated, jobs);
  assert.equal((await env.q("SELECT * FROM artifacts WHERE artifact_sha256 = ?", row.artifact_sha256)).length, 1);
});

test("a Queue message pending at restart is recovered by the sweeper's staleness re-send", async () => {
  const response = await env.admit(admission("pending", [article(4)]));
  const id = response.body.operation.operation_id;
  await env.restart(); // before the batch timeout delivers the message
  const afterRestart = await env.row(id);
  const delivered = afterRestart.state !== "enqueued";
  if (!delivered) {
    await sleep(3200); // ENQUEUED_STALE_MS
    await env.reconcile();
  }
  const row = await env.waitState(id, "submitted", { timeout: 20000 });
  assert.equal(env.execution.jobFor(id).execution_id, row.execution_id);
  // The observed engine behaviour is recorded, not assumed.
  console.log(JSON.stringify({ pending_message_delivered_after_restart: delivered, send_attempts: row.send_attempts }));
});

test("A21 parallel handler and D1 requests: distinct sequences, correct winners", async () => {
  const before = await env.counts();
  const jobs = env.execution.counters.jobsCreated;
  const bodies = Array.from({ length: 12 }, (_, i) => admission(`a21-${i}`, [article(100 + i)]));
  const [admits] = await Promise.all([
    Promise.all(bodies.map((b, i) => env.admit(b, i % 2 ? "event" : "manual"))),
    Promise.all(Array.from({ length: 6 }, () => env.call("GET", "/v1/targets/site-a20", "reader"))),
    Promise.all([env.reconcile(), env.reconcile()]),
  ]);
  assert.ok(admits.every((r) => r.status === 201));
  const seqs = admits.map((r) => r.body.operation.seq).sort((a, b) => a - b);
  assert.equal(new Set(seqs).size, 12);
  assert.equal(seqs[11] - seqs[0], 11, "consecutive sequence values");
  for (const r of admits) await env.waitState(r.body.operation.operation_id, "submitted");
  const after = await env.counts();
  assert.equal(after.operations, before.operations + 12);
  assert.equal(env.execution.counters.jobsCreated, jobs + 12);
});

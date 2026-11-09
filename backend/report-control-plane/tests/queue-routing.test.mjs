// Non-default queue names on the real local engine, through the package's own
// producer, consumer and dead-letter topology: unknown-queue dispatch (Q4),
// dead-letter routing and exhaustion (Q5), persistence (Q6), manual recovery
// (Q7), stale replays (Q8) and a name change across a restart (Q10). Every
// check reads D1, the fake execution service's counters and the publisher's
// state file, never a success message.
import assert from "node:assert/strict";
import { randomBytes } from "node:crypto";
import { after, before, test } from "node:test";
import { admission, article, setup, sleep } from "./support/harness.mjs";

const NAMES = { admissions: "review-admission-jobs", dead: "review-admission-jobs-dead" };
const OTHER = "review-admission-other";
const RENAMED = { admissions: "renamed-admission-jobs", dead: "renamed-admission-jobs-dead" };

let env;
before(async () => {
  env = await setup({ vars: { ADMISSIONS_QUEUE_NAME: NAMES.admissions, DEAD_LETTER_QUEUE_NAME: NAMES.dead } });
});
after(async () => {
  await env.stop();
});

const message = (id, generation = 1, extra = {}) => ({ id: `m-${randomBytes(4).toString("hex")}`, timestamp: new Date(), attempts: 1, body: { operation_id: id, generation }, ...extra });
const dispatch = (queue, messages) => env.stack.worker.queue(queue, messages);
const events = async (id, kind) => (await env.q("SELECT * FROM events WHERE operation_id = ? AND kind = ?", id, kind)).length;
const eventCount = async () => (await env.one("SELECT count(*) AS n FROM events")).n;
const effects = async () => ((await env.publisherState())?.effects ?? []).length;
const fence = (row) => ({ state: row.state, version: row.version, generation: row.delivery_generation, send_attempts: row.send_attempts, claim: row.claim_token, reason: row.reason });

// The world outside one operation: rows, objects, jobs, calls, publications,
// targets and publisher effects.
async function world() {
  return {
    counts: await env.counts(),
    submits: env.execution.counters.submits,
    publications: (await env.one("SELECT count(*) AS n FROM publications")).n,
    targets: await env.q("SELECT * FROM targets ORDER BY target"),
    effects: await effects(),
  };
}

// An admitted row whose send was interrupted: no message is in flight.
async function heldAdmission(sourceRevision, n) {
  await env.fault("after_intent_before_send");
  const response = await env.admit(admission(sourceRevision, [article(n)]));
  assert.equal(response.status, 500);
  return (await env.one("SELECT * FROM operations WHERE source_revision = ?", sourceRevision)).operation_id;
}

const state = { dead: null };

test("Q4 a batch from an unknown queue is retried, never handled, with one bounded audit event", async () => {
  assert.deepEqual({ ...env.stack.queues }, NAMES, "the stack runs on the configured names");
  const id = await heldAdmission("q4", 1);
  const row = await env.row(id);
  const before = await world();
  const total = await eventCount();
  const unknown = await dispatch(OTHER, [
    message(id),
    message(randomBytes(32).toString("hex")), // well-formed, no such operation
    { id: "malformed", timestamp: new Date(), attempts: 1, body: { operation_id: id, generation: 1, extra: "x" } },
    { id: "empty", timestamp: new Date(), attempts: 1, body: null },
  ]);
  assert.equal(unknown.retryBatch.retry, true, "the whole batch is retried");
  assert.equal(unknown.ackAll, false);
  assert.deepEqual(unknown.explicitAcks, [], "nothing acknowledged");
  assert.equal(await eventCount(), total + 1, "one event, only for the known operation");
  const [audit] = await env.q("SELECT * FROM events WHERE operation_id = ? AND kind = 'queue_unknown'", id);
  assert.deepEqual({ subject: audit.subject, token: audit.token, detail: audit.detail }, { subject: null, token: null, detail: null }, "nothing reflected");
  // The defaults are just another unknown queue under configured names.
  const defaults = await dispatch("report-admissions-dead", [message(id)]);
  assert.equal(defaults.retryBatch.retry, true);
  assert.equal(await events(id, "queue_unknown"), 2);
  // A failing diagnostic still retries and records nothing.
  await env.fault("queue_unknown_record", 1);
  const failing = await dispatch(OTHER, [message(id)]);
  assert.equal(failing.retryBatch.retry, true);
  assert.deepEqual(failing.explicitAcks, []);
  assert.equal(await events(id, "queue_unknown"), 2);
  assert.deepEqual(fence(await env.row(id)), fence(row), "the operation is untouched");
  assert.deepEqual(await world(), before, "no job, call, object, publication, target or effect");
});

test("Q5 a dead-letter message on the configured name is a dead-letter disposition, never another call", async () => {
  const id = await heldAdmission("q5-dispatch", 2);
  const before = await world();
  const result = await dispatch(NAMES.dead, [message(id)]);
  assert.equal(result.outcome, "ok");
  assert.equal(result.explicitAcks.length, 1);
  const row = await env.row(id);
  assert.deepEqual([row.state, row.reason, row.delivery_generation], ["dead_letter", "delivery_exhausted", 1]);
  assert.equal(await events(id, "dead_letter"), 1);
  assert.deepEqual(await world(), before, "no execution call, job, publication or effect");
});

test("Q5 three transient failures on the real non-default topology dead-letter after exactly three calls", async () => {
  const before = await world();
  env.execution.plan.submitStatus.push(503, 503, 503);
  const response = await env.admit(admission("q5-exhaust", [article(3)]));
  assert.equal(response.status, 201);
  const id = response.body.operation.operation_id;
  const dead = await env.waitState(id, "dead_letter", { timeout: 20000 });
  assert.deepEqual([dead.reason, dead.delivery_generation, dead.retry_rounds, dead.send_attempts], ["delivery_exhausted", 1, 0, 1]);
  assert.equal(await events(id, "dead_letter"), 1);
  assert.equal(await events(id, "execution_transient"), 3);
  assert.equal(await events(id, "queue_unknown"), 0);
  await sleep(1500); // nothing further arrives from either queue
  const after = await world();
  assert.equal(env.execution.counters.submits, before.submits + 3, "exactly three execution calls");
  assert.equal(after.counts.jobs, before.counts.jobs, "no execution job");
  assert.equal(after.publications, before.publications);
  assert.deepEqual(after.targets, before.targets);
  assert.equal(after.effects, before.effects);
  assert.deepEqual(fence(await env.row(id)), fence(dead));
  state.dead = id;
});

test("Q6 the terminal row survives a restart on the same names, and old messages are acknowledged without effect", async () => {
  const id = state.dead;
  const row = await env.row(id);
  const history = await env.q("SELECT * FROM events WHERE operation_id = ? ORDER BY id", id);
  await env.restart();
  assert.deepEqual({ ...env.stack.queues }, NAMES);
  assert.deepEqual(await env.row(id), row);
  assert.deepEqual(await env.q("SELECT * FROM events WHERE operation_id = ? ORDER BY id", id), history);
  const before = await world();
  const main = await dispatch(NAMES.admissions, [message(id)]);
  const dlq = await dispatch(NAMES.dead, [message(id)]);
  assert.equal(main.explicitAcks.length + dlq.explicitAcks.length, 2, "both acknowledged");
  assert.equal(await events(id, "duplicate_delivery"), 1, "a settled generation-1 row ignores its own message");
  assert.equal(await events(id, "stale_dead_letter"), 1);
  assert.deepEqual(fence(await env.row(id)), fence(row));
  assert.deepEqual(await world(), before);
});

test("Q7 manual retry advances one generation and makes exactly one execution", async () => {
  const id = state.dead;
  const before = await world();
  const retried = await env.call("POST", `/v1/operations/${id}/retry`, "manual");
  assert.equal(retried.status, 202);
  const done = await env.waitState(id, "submitted");
  assert.deepEqual([done.delivery_generation, done.retry_rounds, done.send_attempts], [2, 1, 1]);
  assert.equal(await events(id, "manual_retry"), 1);
  assert.equal(env.execution.counters.submits, before.submits + 1, "one call");
  assert.equal((await env.counts()).jobs, before.counts.jobs + 1, "one job");
  assert.equal(done.execution_id, env.execution.jobFor(id).execution_id);
});

test("Q8 generation-1 admission and dead-letter replays change nothing after the retry", async () => {
  const id = state.dead;
  const row = await env.row(id);
  const before = await world();
  const stale = { delivery: await events(id, "stale_delivery"), dead: await events(id, "stale_dead_letter") };
  await dispatch(NAMES.admissions, [message(id, 1)]);
  await dispatch(NAMES.dead, [message(id, 1)]);
  assert.equal(await events(id, "stale_delivery"), stale.delivery + 1);
  assert.equal(await events(id, "stale_dead_letter"), stale.dead + 1);
  assert.deepEqual(fence(await env.row(id)), fence(row));
  assert.deepEqual(await world(), before, "no call, job, publication, last-good or effect");
});

test("Q10 rows left under one name set proceed under another after a restart, through the bounded re-send", async () => {
  const held = await heldAdmission("q10-held", 10);
  const response = await env.admit(admission("q10-pending", [article(11)]));
  const pending = response.body.operation.operation_id;
  const rows = { held: await env.row(held) };
  await env.restart({ ADMISSIONS_QUEUE_NAME: RENAMED.admissions, DEAD_LETTER_QUEUE_NAME: RENAMED.dead });
  assert.deepEqual({ ...env.stack.queues }, RENAMED);
  assert.deepEqual(await env.row(held), rows.held, "the restart changed no row");
  const delivered = (await env.row(pending)).state !== "enqueued";
  if (!delivered) await sleep(3200); // ENQUEUED_STALE_MS
  const settled = await env.waitFor(
    async () => {
      await env.reconcile();
      const both = [await env.row(held), await env.row(pending)];
      return both.every((r) => r.state === "submitted") ? both : null;
    },
    { timeout: 20000, every: 500 },
  );
  for (const row of settled) {
    assert.equal(row.delivery_generation, 1);
    assert.ok(row.send_attempts <= 3, "within the send bound");
    assert.equal(row.execution_id, env.execution.jobFor(row.operation_id).execution_id);
    assert.equal(await events(row.operation_id, "queue_unknown"), 0);
  }
  // Recorded, not assumed: whether the old queue's message arrived before the rename.
  console.log(JSON.stringify({ q10_pending_delivered_before_rename: delivered, send_attempts: settled.map((r) => r.send_attempts) }));
});

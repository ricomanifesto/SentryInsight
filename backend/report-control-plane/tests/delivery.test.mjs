// Delivery ownership against the real local Queue and handler: A9, A10, A22
// to A25, and overlapping old and new calls after a claim expires.
import assert from "node:assert/strict";
import { after, before, test } from "node:test";
import { admission, admitted, article, setup, sleep } from "./support/harness.mjs";

let env;
before(async () => {
  env = await setup();
});
after(async () => {
  await env.stop();
});

const message = (id, generation = 1) => ({ body: { operation_id: id, generation } });
const events = async (id, kind) => (await env.q("SELECT * FROM events WHERE operation_id = ? AND kind = ?", id, kind)).length;

// An admitted row with no message in flight: the send is interrupted.
async function heldAdmission(sourceRevision, n) {
  await env.fault("after_intent_before_send");
  const response = await env.admit(admission(sourceRevision, [article(n)]));
  assert.equal(response.status, 500);
  return (await env.one("SELECT * FROM operations WHERE source_revision = ?", sourceRevision)).operation_id;
}

test("A9 a duplicate delivery of a submitted operation is a no-op", async () => {
  const id = await admitted(env, admission("a9", [article(1)]));
  const counts = await env.counts();
  const submits = env.execution.counters.submits;
  const producer = await env.stack.mf.getQueueProducer("ADMISSIONS");
  await producer.send({ operation_id: id, generation: 1 });
  await env.waitFor(async () => (await events(id, "duplicate_delivery")) === 1);
  assert.deepEqual(await env.counts(), counts);
  assert.equal(env.execution.counters.submits, submits);
});

test("A22 concurrent duplicate deliveries: one durable claim winner calls the service", async () => {
  const id = await heldAdmission("a22", 2);
  const submits = env.execution.counters.submits;
  env.execution.plan.holdSubmitMs.push(400);
  const results = await Promise.all([
    env.stack.worker.queue(env.stack.queues.admissions, [{ id: "a", timestamp: new Date(), attempts: 1, ...message(id) }]),
    env.stack.worker.queue(env.stack.queues.admissions, [{ id: "b", timestamp: new Date(), attempts: 1, ...message(id) }]),
  ]);
  assert.deepEqual(results.map((r) => r.outcome), ["ok", "ok"]);
  assert.equal(env.execution.counters.submits, submits + 1, "the loser made no external call");
  assert.equal(await events(id, "claim_lost"), 1);
  assert.equal((await env.row(id)).state, "submitted");
});

test("A10 the service accepts but the response is lost: the retry gets the same ids", async () => {
  const jobs = env.execution.counters.jobsCreated;
  const submits = env.execution.counters.submits;
  env.execution.plan.dropSubmitResponses = 1;
  const id = await admitted(env, admission("a10", [article(3)]));
  assert.equal(env.execution.counters.jobsCreated, jobs + 1);
  assert.equal(env.execution.counters.submits, submits + 2);
  assert.equal((await env.row(id)).execution_id, env.execution.jobFor(id).execution_id);
  assert.equal(await events(id, "execution_transient"), 1);
});

test("A23 crash after acceptance, before submitted: the claim expires and the same ids are recorded", async () => {
  const jobs = env.execution.counters.jobsCreated;
  const submits = env.execution.counters.submits;
  await env.fault("after_accept_before_submitted");
  const response = await env.admit(admission("a23", [article(4)]));
  const id = response.body.operation.operation_id;
  await env.waitFor(async () => (await events(id, "claim_lost")) >= 1);
  const stuck = await env.row(id);
  assert.equal(stuck.state, "submitting");
  assert.equal(stuck.execution_id, null);
  await sleep(Math.max(0, stuck.claim_expires_at - Date.now()) + 200);
  await env.reconcile();
  const done = await env.waitState(id, "submitted");
  assert.equal(done.execution_id, env.execution.jobFor(id).execution_id);
  assert.equal(done.send_attempts, 2);
  assert.equal(env.execution.counters.jobsCreated, jobs + 1, "one job");
  assert.equal(env.execution.counters.submits, submits + 2);
});

test("an expired caller's late write is fenced: one execution, the current claim settles", async () => {
  const id = await heldAdmission("late-settle", 5);
  const jobs = env.execution.counters.jobsCreated;
  await env.fault("delay_before_submitted", 1, "delay", 4000);
  const old = env.stack.worker.queue(env.stack.queues.admissions, [{ id: "old", timestamp: new Date(), attempts: 1, ...message(id) }]);
  await env.waitFor(async () => (await env.row(id)).state === "submitting");
  const claimed = await env.row(id);
  await sleep(Math.max(0, claimed.claim_expires_at - Date.now()) + 200);
  const fresh = await env.stack.worker.queue(env.stack.queues.admissions, [{ id: "new", timestamp: new Date(), attempts: 1, ...message(id) }]);
  assert.equal(fresh.outcome, "ok");
  const settled = await env.row(id);
  assert.equal(settled.state, "submitted");
  await old;
  assert.equal(await events(id, "settle_lost"), 1, "the old claim's write changed nothing");
  const final = await env.row(id);
  assert.equal(final.version, settled.version);
  assert.equal(final.execution_id, settled.execution_id);
  assert.equal(env.execution.counters.jobsCreated, jobs + 1, "one authoritative execution");
});

test("overlapping old and new calls at the execution service admit one job", async () => {
  const id = await heldAdmission("overlap", 6);
  const jobs = env.execution.counters.jobsCreated;
  // The first call outlives the Worker's deadline at the service; the second
  // arrives while it is still in progress there.
  env.execution.plan.holdSubmitMs.push(3500);
  const first = await env.stack.worker.queue(env.stack.queues.admissions, [{ id: "first", timestamp: new Date(), attempts: 1, ...message(id) }]);
  assert.deepEqual(first.retryMessages.map((m) => m.msgId), ["first"]);
  assert.equal((await env.row(id)).state, "enqueued", "the timed-out caller released its claim");
  const second = await env.stack.worker.queue(env.stack.queues.admissions, [{ id: "second", timestamp: new Date(), attempts: 1, ...message(id) }]);
  assert.equal(second.outcome, "ok");
  assert.equal((await env.row(id)).state, "submitted");
  await sleep(2000); // the held first call completes at the service
  assert.equal(env.execution.counters.jobsCreated, jobs + 1);
  assert.equal((await env.row(id)).execution_id, env.execution.jobFor(id).execution_id);
});

test("A24 delivery exhaustion, manual retry, then stale old messages change nothing", async () => {
  env.execution.plan.submitStatus.push(503, 503, 503);
  const response = await env.admit(admission("a24", [article(7)]));
  const id = response.body.operation.operation_id;
  const dead = await env.waitState(id, "dead_letter", { timeout: 20000 });
  assert.equal(dead.reason, "delivery_exhausted");
  const retried = await env.call("POST", `/v1/operations/${id}/retry`, "manual");
  assert.equal(retried.status, 202);
  const done = await env.waitState(id, "submitted");
  assert.equal(done.delivery_generation, 2);
  const snapshot = { state: done.state, version: done.version, send_attempts: done.send_attempts };
  await env.stack.worker.queue(env.stack.queues.dead, [{ id: "stale-dlq", timestamp: new Date(), attempts: 1, ...message(id, 1) }]);
  await env.stack.worker.queue(env.stack.queues.admissions, [{ id: "stale-main", timestamp: new Date(), attempts: 1, ...message(id, 1) }]);
  const after = await env.row(id);
  assert.deepEqual({ state: after.state, version: after.version, send_attempts: after.send_attempts }, snapshot);
  assert.equal(await events(id, "stale_dead_letter"), 1);
  assert.equal(await events(id, "stale_delivery"), 1);
});

// Sweep until the row records send exhaustion; the caller arms the failures.
async function exhaustSends(id) {
  return env.waitFor(
    async () => {
      await env.reconcile();
      const row = await env.row(id);
      return row.state === "dead_letter" ? row : null;
    },
    { timeout: 20000, every: 300 },
  );
}

test("A25 exhausted sends are recorded by the sweeper; three manual rounds, then refused", async () => {
  await env.fault("queue_send", 1);
  const response = await env.admit(admission("a25", [article(8)]));
  assert.equal(response.status, 201, "the durable intent is admitted even when the send fails");
  const id = response.body.operation.operation_id;
  await env.fault("queue_send", 2);
  const dead = await exhaustSends(id);
  assert.equal(dead.reason, "send_exhausted");
  assert.equal(dead.send_attempts, 3);
  for (let round = 1; round <= 3; round += 1) {
    await env.fault("queue_send", 3);
    assert.equal((await env.call("POST", `/v1/operations/${id}/retry`, "manual")).status, 202);
    const row = await exhaustSends(id);
    assert.equal(row.delivery_generation, round + 1);
    assert.equal(row.retry_rounds, round);
  }
  const refused = await env.call("POST", `/v1/operations/${id}/retry`, "manual");
  assert.equal(refused.status, 409);
  assert.equal(refused.body.error, "retry_exhausted");
  assert.equal((await env.row(id)).delivery_generation, 4);
});

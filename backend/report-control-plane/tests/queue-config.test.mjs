// Invalid queue names seen by a running Worker (Q2, Q3): the declared local
// topology keeps the defaults while the Worker's variables carry the bad
// names, as a deployment whose declarations and variables disagree would.
// Every entry point must refuse before any write, send or call, and the
// scheduled admission is not lost once the configuration is corrected.
import assert from "node:assert/strict";
import { after, before, test } from "node:test";
import { BUNDLE, admission, admitted, article, setup } from "./support/harness.mjs";

let env;
before(async () => {
  env = await setup();
});
after(async () => {
  await env.stop();
});

const BAD = [
  ["empty", { ADMISSIONS_QUEUE_NAME: "" }],
  ["padded", { ADMISSIONS_QUEUE_NAME: " report-admissions" }],
  ["upper case", { DEAD_LETTER_QUEUE_NAME: "Report-Admissions-Dead" }],
  ["64 characters", { ADMISSIONS_QUEUE_NAME: "q".repeat(64) }],
  ["leading hyphen", { DEAD_LETTER_QUEUE_NAME: "-dead" }],
  ["not a string", { ADMISSIONS_QUEUE_NAME: 7 }],
  ["equal to the dead-letter default", { ADMISSIONS_QUEUE_NAME: "report-admissions-dead" }],
  ["both equal", { ADMISSIONS_QUEUE_NAME: "same-queue", DEAD_LETTER_QUEUE_NAME: "same-queue" }],
];

async function observed() {
  return {
    counts: await env.counts(),
    events: (await env.one("SELECT count(*) AS n FROM events")).n,
    operations: await env.q("SELECT operation_id, state, version, send_attempts, delivery_generation FROM operations ORDER BY seq"),
    schedules: await env.q("SELECT * FROM schedules ORDER BY schedule_id"),
    publications: (await env.one("SELECT count(*) AS n FROM publications")).n,
    targets: await env.q("SELECT * FROM targets ORDER BY target"),
    submits: env.execution.counters.submits,
    effects: ((await env.publisherState())?.effects ?? []).length,
  };
}

test("Q2 Q3 every entry point refuses invalid queue names before any effect", async () => {
  const id = await admitted(env, admission("config-held", [article(1)]));
  assert.equal((await env.call("PUT", "/v1/schedules/nightly", "operator", { pipeline: "reports", policy_id: "standard", state: "active" })).status, 200);
  assert.equal((await env.call("PUT", "/v1/schedules/nightly/sources", "manual", { schema: BUNDLE, articles: [article(2)] })).status, 202);
  const baseline = await observed();
  for (const [label, workerVars] of BAD) {
    await env.restart({}, { workerVars });
    const refusals = [
      await env.admit(admission(`config-${label}`, [article(3)])),
      await env.call("POST", `/v1/operations/${id}/retry`, "manual"),
      await env.publish(id, "site-config"),
      await env.reconcile(),
      await env.status(id),
    ];
    for (const r of refusals) assert.deepEqual([r.status, r.body], [503, { error: "config_invalid" }], label);
    assert.equal((await env.call("GET", "/healthz")).status, 200, `${label}: health is unauthenticated and unaffected`);
    const scheduled = await env.stack.worker.scheduled({ cron: "*/5 * * * *" });
    assert.notEqual(scheduled.outcome, "ok", `${label}: the scheduled handler did no work`);
    const batch = await env.stack.worker.queue(env.stack.queues.admissions, [{ id: "cfg", timestamp: new Date(), attempts: 1, body: { operation_id: id, generation: 1 } }]);
    assert.equal(batch.retryBatch.retry, true, `${label}: the batch is retried`);
    assert.deepEqual(batch.explicitAcks, [], `${label}: nothing acknowledged`);
    assert.deepEqual(await observed(), baseline, `${label}: no row, event, object, job, call, publication or effect`);
  }
  // Corrected configuration: the staged scheduled admission was deferred, not lost.
  await env.restart({}, {});
  const fired = await env.stack.worker.scheduled({ cron: "*/5 * * * *" });
  assert.equal(fired.outcome, "ok");
  const schedule = await env.one("SELECT * FROM schedules WHERE schedule_id = 'nightly'");
  assert.equal(schedule.last_admitted_fingerprint, schedule.pending_bundle_sha256);
  const scheduledRow = await env.one("SELECT * FROM operations WHERE principal = 'scheduler'");
  await env.waitState(scheduledRow.operation_id, "submitted");
  assert.equal((await env.status(id)).status, 200);
});

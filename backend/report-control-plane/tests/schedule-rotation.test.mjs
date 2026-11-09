// Scheduled admission rotates through a persisted cursor: schedules whose
// admission fails permanently, more of them than one sweep reads, cannot
// starve a newer schedule, and the cursor survives a restart and wraps.
import assert from "node:assert/strict";
import { after, before, test } from "node:test";
import { BUNDLE, article, setup } from "./support/harness.mjs";

let env;
before(async () => {
  env = await setup();
  // A projection pipeline refuses every admission (422), permanently.
  const seeded = await env.call("PUT", "/v1/pipelines/refusing", "operator", { policy_id: "standard", binding_id: "b".repeat(64), state: "active", mode: "project" });
  assert.equal(seeded.status, 200);
});
after(async () => {
  await env.stop();
});

async function schedule(id, pipeline, n) {
  assert.equal((await env.call("PUT", `/v1/schedules/${id}`, "operator", { pipeline, policy_id: "standard", state: "active" })).status, 200);
  const staged = await env.call("PUT", `/v1/schedules/${id}/sources`, "manual", JSON.stringify({ schema: BUNDLE, articles: [article(n)] }));
  assert.equal(staged.status, 202);
  return staged.body.pending_bundle_sha256;
}

// The schedules one scheduled run read, from the events it recorded.
async function sweep() {
  const mark = (await env.one("SELECT coalesce(max(id), 0) AS n FROM events")).n;
  await env.stack.worker.scheduled({ cron: "*/5 * * * *" });
  const rows = await env.q(
    "SELECT subject FROM events WHERE id > ? AND kind IN ('schedule_fired', 'schedule_bundle_unavailable') ORDER BY id",
    mark,
  );
  return rows.map((r) => r.subject);
}

test("permanently failing schedules beyond the bound cannot starve a newer one, across a restart and a wrap", async () => {
  const failing = [];
  for (let n = 0; n < 21; n += 1) {
    const id = `failing-${String(n).padStart(2, "0")}`;
    if (n % 2 === 0) {
      await schedule(id, "refusing", 7600 + n); // admission refused
    } else {
      const bundle = await schedule(id, "reports", 7600 + n);
      await env.stack.bucket.delete(`snapshots/${bundle}`); // bundle unavailable
    }
    failing.push(id);
  }
  const fresh = await schedule("newest", "reports", 7700);

  assert.deepEqual(await sweep(), failing.slice(0, 20), "the first sweep reads one bound of the oldest");
  await env.restart(); // a fresh Worker instance on the same database
  // The cursor persisted across the restart: the sweep resumes after the
  // first bound, reaches the newer schedule, and fills the rest of its bound
  // by wrapping to the start.
  assert.deepEqual(await sweep(), [failing[20], "newest", ...failing.slice(0, 18)]);
  const admitted = await env.q("SELECT * FROM operations WHERE principal = 'scheduler'");
  assert.deepEqual(admitted.map((o) => o.fingerprint), [fresh], "only the newer schedule was admitted");
  assert.equal((await env.one("SELECT last_admitted_fingerprint AS f FROM schedules WHERE schedule_id = 'newest'")).f, fresh);
  // The admitted schedule leaves the set; the failures stay eligible and the
  // rotation keeps covering every one of them.
  assert.deepEqual(await sweep(), [...failing.slice(18), ...failing.slice(0, 17)]);
});

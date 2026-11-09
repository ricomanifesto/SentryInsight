// The sweeper's bounded status pull rotates: a full batch of operations that
// stay pending cannot starve a newer one, and the cursor survives a restart.
import assert from "node:assert/strict";
import { after, before, test } from "node:test";
import { REPORT_FILES, admission, admitted, article, setup } from "./support/harness.mjs";

let env;
before(async () => {
  env = await setup();
});
after(async () => {
  await env.stop();
});

test("a newer submitted operation completes although the oldest batch stays pending", async () => {
  const ids = [];
  for (let n = 0; n < 21; n += 1) ids.push(await admitted(env, admission(`rotate-${n}`, [article(7000 + n)])));
  const newest = ids[20];
  env.execution.succeed(newest, REPORT_FILES);
  await env.reconcile();
  assert.equal((await env.row(newest)).state, "submitted", "the first sweep reads the oldest bound");
  await env.restart(); // the cursor is persisted, not held by the Worker
  await env.reconcile();
  assert.equal((await env.row(newest)).state, "completed", "reached by the second sweep after a restart");
  for (const id of ids.slice(0, 20)) assert.equal((await env.row(id)).state, "submitted");
});

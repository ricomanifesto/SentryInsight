// The sweeper's bounded status pull rotates: a full batch of operations that
// stay pending cannot starve a newer one.
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
  for (let sweep = 0; sweep < 2 && (await env.row(newest)).state !== "completed"; sweep += 1) await env.reconcile();
  assert.equal((await env.row(newest)).state, "completed", "reached within two sweeps");
  for (const id of ids.slice(0, 20)) assert.equal((await env.row(id)).state, "submitted");
});

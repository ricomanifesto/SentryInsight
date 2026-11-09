// Without an execution service or a publisher the Worker still serves:
// execution and publication refuse before any write, the sweeper skips them,
// and projection, reads and the export work. A half-configured dependency is
// invalid and fails closed.
import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { after, before, test } from "node:test";
import { ADMISSION, admission, article, setup } from "./support/harness.mjs";

const sha = (data) => createHash("sha256").update(data).digest("hex");
let env;
before(async () => {
  env = await setup({ omit: ["EXECUTION_URL", "EXECUTION_TOKEN", "PUBLISHER_URL", "PUBLISHER_TOKEN"] });
  await env.call("PUT", "/v1/pipelines/history", "operator", { policy_id: "standard", binding_id: sha("b"), state: "active", mode: "project" });
});
after(async () => {
  await env.stop();
});

test("execution and publication refuse before any write; projection, reads and export serve", async () => {
  assert.equal((await env.call("GET", "/healthz")).status, 200);
  const before = (await env.one("SELECT count(*) AS n FROM operations")).n;
  const refused = await env.admit(admission("unconfigured-1", [article(1)]));
  assert.deepEqual([refused.status, refused.body.error], [503, "execution_unconfigured"]);
  assert.equal((await env.one("SELECT count(*) AS n FROM operations")).n, before);

  const snapshot = Buffer.from(JSON.stringify({ schema: ADMISSION, pipeline: "history", policy_id: "standard", source_revision: "actions:1:1", articles: [article(2)] }));
  const report = Buffer.from("# Report\n");
  for (const bytes of [snapshot, report]) assert.equal((await env.call("PUT", `/v1/projections/blobs/${sha(bytes)}`, "projector", bytes)).status, 201);
  const projected = await env.call("POST", "/v1/projections", "projector", {
    schema: "report-control-plane/projection/1",
    pipeline: "history",
    policy_id: "standard",
    source_revision: "actions:1:1",
    snapshot_sha256: sha(snapshot),
    run: { execution_id: "actions-run-1-1", source_commit: sha("c").slice(0, 40), outcome: "succeeded", reason: null, executed_links: null, completed_at: null },
    artifact: { files: [{ path: "index.md", sha256: sha(report), bytes: report.byteLength }] },
  });
  assert.equal(projected.status, 201, JSON.stringify(projected.body));
  const id = projected.body.operation.operation_id;
  assert.equal((await env.status(id)).body.operation.state, "completed");
  const reconciled = await env.reconcile();
  assert.deepEqual([reconciled.status, reconciled.body.counts.pulled, reconciled.body.counts.publications], [200, 0, 0]);
  const page = await env.exportPage();
  assert.ok(page.body.records.some((r) => r.record_id === `sentryinsight:run:${id}`));
  const run = page.body.records.find((r) => r.record_id === `sentryinsight:run:${id}`);
  assert.deepEqual(run.sources.map((s) => s.outcome), ["not_reported"], "an unreported executed set is not guessed");
});

test("one variable of a pair without the other is invalid and fails closed", async () => {
  await env.restart({ EXECUTION_URL: "http://127.0.0.1:9" });
  const response = await env.call("GET", "/v1/export", "exporter");
  assert.deepEqual([response.status, response.body.error], [503, "config_invalid"]);
});

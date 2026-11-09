// Completion by pull against real local D1 and R2: A13, A14 and A29 to A32
// (the artifact rejection family), A28 convergence, binding retirement (A27,
// product side) and a failed execution (A17, product side).
import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { after, before, test } from "node:test";
import { BINDING, OTHER_BINDING, REPORT_FILES, admission, admitted, article, setup } from "./support/harness.mjs";

let env;
before(async () => {
  env = await setup();
});
after(async () => {
  await env.stop();
});

const sha = (data) => createHash("sha256").update(data).digest("hex");
let next = 1000;
const fresh = (label) => admission(`${label}-${next}`, [article(next++)]);

test("A13 completion lost before the batch: the next sweep completes once", async () => {
  const id = await admitted(env, fresh("a13"));
  env.execution.succeed(id, REPORT_FILES);
  await env.fault("before_completion_batch");
  assert.equal((await env.reconcile()).status, 500);
  assert.equal((await env.row(id)).state, "submitted");
  const artifact = env.execution.jobFor(id).artifact.sha256;
  assert.equal((await env.q("SELECT * FROM artifacts WHERE artifact_sha256 = ?", artifact)).length, 0);
  assert.equal((await env.r2(`artifacts/${artifact}/`)).length, 4, "parts and manifest written before the fault");
  await env.reconcile();
  const done = await env.row(id);
  assert.equal(done.state, "completed");
  assert.equal(done.artifact_sha256, artifact);
  assert.equal((await env.q("SELECT * FROM artifacts WHERE artifact_sha256 = ?", artifact)).length, 1);
  const objects = await env.r2(`artifacts/${artifact}/`);
  assert.deepEqual(objects.map((o) => o.key).sort(), [
    `artifacts/${artifact}/files/index.html`,
    `artifacts/${artifact}/files/reports/2026-01-01.md`,
    `artifacts/${artifact}/files/reports/latest.json`,
    `artifacts/${artifact}/manifest.json`,
  ]);
  assert.equal((await env.q("SELECT * FROM events WHERE operation_id = ? AND kind = 'completed'", id)).length, 1);
  // The accepted artifact is readable through the read role; bytes match.
  const file = await fetch(`${env.stack.url}/v1/artifacts/${artifact}/files/reports/2026-01-01.md`, {
    headers: { authorization: `Bearer ${env.tokens.reader}` },
  });
  assert.equal(await file.text(), REPORT_FILES["reports/2026-01-01.md"]);
  const manifest = await env.call("GET", `/v1/artifacts/${artifact}`, "reader");
  assert.equal(manifest.body.artifact_sha256, artifact);
  assert.equal(manifest.body.file_count, 3);
});

test("segment-ordered nested files complete; whole-string order is rejected", async () => {
  const files = { "a/b": "nested\n", "a-c": "sibling\n" };
  const good = await admitted(env, fresh("order-good"));
  env.execution.succeed(good, files);
  assert.deepEqual(env.execution.jobFor(good).artifact.files.map((f) => f.path), ["a/b", "a-c"]);
  await env.reconcile();
  assert.equal((await env.row(good)).state, "completed");
});

const tamper = {
  "corrupted part": ["artifact_part_mismatch", (job) => (job.files["index.html"] = "<html>synthetic REPORT</html>\n")],
  "missing part": ["artifact_part_missing", (job) => delete job.files["reports/latest.json"]],
  "served length differs": ["artifact_size_mismatch", (job) => (job.files["index.html"] += "x")],
  "duplicate path": [
    "artifact_path_duplicate",
    (job) => {
      job.artifact.files.splice(1, 0, { ...job.artifact.files[0] });
      job.artifact.file_count += 1;
      job.artifact.total_bytes += job.artifact.files[0].bytes;
    },
  ],
  "escaping path": ["artifact_path_invalid", (job) => (job.artifact.files[0].path = "../escape.html")],
  "count mismatch": ["artifact_count_mismatch", (job) => (job.artifact.file_count += 1)],
  "total size mismatch": ["artifact_size_mismatch", (job) => (job.artifact.total_bytes += 1)],
  "listed digest disagrees": ["artifact_digest_mismatch", (job) => (job.artifact.sha256 = job.artifact.accepted_output_sha256 = sha("other"))],
  "accepted output disagrees": ["artifact_accepted_mismatch", (job) => (job.artifact.accepted_output_sha256 = sha("stale output"))],
  "whole-string order": [
    "artifact_order_invalid",
    (job) => {
      job.files = { "a/b": "nested\n", "a-c": "sibling\n" };
      const list = [
        { path: "a-c", sha256: sha("sibling\n"), bytes: 8 },
        { path: "a/b", sha256: sha("nested\n"), bytes: 7 },
      ];
      const digest = sha(list.map((f) => `${f.path}\0${f.sha256}\n`).join(""));
      job.artifact = { accepted_output_sha256: digest, sha256: digest, file_count: 2, total_bytes: 15, files: list };
    },
  ],
  "executed article outside the admitted set": [
    "artifact_articles_invalid",
    (job) => (job.executed = [{ article_key: "https://example.test/never-admitted", content_sha256: sha("x") }]),
  ],
  "receipt names another execution": ["receipt_identity_mismatch", (job) => (job.execution_id = "exec-someone-else")],
  "malformed receipt": ["receipt_invalid", (job) => (job.rawReceipt = '{"schema": "execution-receipt/1", "schema": "x"}')],
};

for (const [name, [token, mutate]] of Object.entries(tamper)) {
  test(`A14 A29-A32 rejection: ${name}`, async () => {
    const id = await admitted(env, fresh("reject"));
    const lastGood = await env.q("SELECT * FROM targets ORDER BY target");
    env.execution.succeed(id, REPORT_FILES, mutate);
    const jobState = JSON.stringify({ ...env.execution.jobFor(id), rawReceipt: undefined });
    await env.reconcile();
    const row = await env.row(id);
    assert.equal(row.state, "failed");
    assert.equal(row.reason, "artifact_rejected");
    assert.equal(row.artifact_sha256, null);
    const rejected = await env.q("SELECT token FROM events WHERE operation_id = ? AND kind = 'artifact_rejected'", id);
    assert.deepEqual(rejected.map((e) => e.token), [token]);
    assert.equal((await env.q("SELECT * FROM artifacts WHERE first_operation_id = ?", id)).length, 0);
    assert.deepEqual(await env.q("SELECT * FROM targets ORDER BY target"), lastGood);
    assert.equal(JSON.stringify({ ...env.execution.jobFor(id), rawReceipt: undefined }), jobState, "the run is untouched");
    assert.equal((await env.publish(id)).status, 409, "a rejected operation cannot be published");
  });
}

test("A28 metadata-only convergence: one job, one artifact row, both operations complete concurrently", async () => {
  const articles = [article(next++), article(next++)];
  const jobs = env.execution.counters.jobsCreated;
  const one = await admitted(env, admission(`conv-a-${next}`, articles));
  const two = await admitted(env, admission(`conv-b-${next}`, articles), "event");
  assert.equal(env.execution.counters.jobsCreated, jobs + 1);
  assert.equal((await env.row(one)).execution_id, (await env.row(two)).execution_id);
  env.execution.succeed(one, { ...REPORT_FILES, "reports/2026-01-01.md": "# Converged\n" });
  const sweeps = await Promise.all([env.reconcile(), env.reconcile(), env.reconcile()]);
  assert.ok(sweeps.every((s) => s.status === 200), JSON.stringify(sweeps.map((s) => s.status)));
  const [a, b] = [await env.row(one), await env.row(two)];
  assert.equal(a.state, "completed");
  assert.equal(b.state, "completed");
  assert.equal(a.artifact_sha256, b.artifact_sha256);
  assert.equal((await env.q("SELECT * FROM artifacts WHERE artifact_sha256 = ?", a.artifact_sha256)).length, 1);
  assert.equal((await env.r2(`artifacts/${a.artifact_sha256}/`)).length, 4);
  for (const id of [one, two]) {
    assert.equal((await env.q("SELECT * FROM events WHERE operation_id = ? AND kind = 'completed'", id)).length, 1);
  }
  assert.equal(env.execution.counters.jobsCreated, jobs + 1, "convergence did not reset provider work");
});

test("A17 product side: a failed execution keeps its reason and cannot be published", async () => {
  const id = await admitted(env, fresh("a17"));
  const lastGood = await env.q("SELECT * FROM targets ORDER BY target");
  const effects = (await env.publisherState()).effects.length;
  env.execution.fail(id, "report_grounding_rejected");
  await env.reconcile();
  const row = await env.row(id);
  assert.deepEqual([row.state, row.reason], ["failed", "report_grounding_rejected"]);
  const refused = await env.publish(id);
  assert.equal(refused.status, 409);
  assert.equal(refused.body.error, "not_publishable");
  assert.deepEqual(await env.q("SELECT * FROM targets ORDER BY target"), lastGood);
  assert.equal((await env.publisherState()).effects.length, effects);
});

test("A27 product side: a binding the service no longer serves is refused terminally; retirement stops admission", async () => {
  // An in-flight operation whose binding is retired fails through the status pull.
  const inflight = await admitted(env, fresh("a27-inflight"));
  env.execution.fail(inflight, "binding_mismatch");
  await env.reconcile();
  assert.deepEqual([(await env.row(inflight)).state, (await env.row(inflight)).reason], ["failed", "binding_mismatch"]);
  // A pipeline bound to a binding the service does not serve: terminal refusal, no job.
  const jobs = env.execution.counters.jobsCreated;
  assert.equal((await env.call("PUT", "/v1/pipelines/reports", "operator", { policy_id: "standard", binding_id: OTHER_BINDING, state: "active" })).status, 200);
  const response = await env.admit(fresh("a27-new"));
  const id = response.body.operation.operation_id;
  assert.equal(response.body.operation.binding_id, OTHER_BINDING);
  const failed = await env.waitState(id, "failed");
  assert.equal(failed.reason, "binding_mismatch");
  assert.equal(env.execution.counters.jobsCreated, jobs);
  // Retiring the pipeline refuses new admissions before any write.
  const before = await env.counts();
  assert.equal((await env.call("PUT", "/v1/pipelines/reports", "operator", { policy_id: "standard", binding_id: OTHER_BINDING, state: "retired" })).status, 200);
  const refused = await env.admit(fresh("a27-retired"));
  assert.deepEqual([refused.status, refused.body.error], [422, "pipeline_unavailable"]);
  assert.deepEqual(await env.counts(), before);
  await env.call("PUT", "/v1/pipelines/reports", "operator", { policy_id: "standard", binding_id: BINDING, state: "active" });
});

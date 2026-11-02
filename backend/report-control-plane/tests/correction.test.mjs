// Regressions for reviewed gaps, against the real local D1, R2 and Queue:
// shared immutable scheduled sources, Unicode validity, contradictory success
// receipts, one completion event under interrupted concurrent settlement, and
// status recovery through the execution service's identities.
import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { after, before, test } from "node:test";
import { readExecution } from "../src/execution-client.js";
import { BINDING, BUNDLE, OTHER_BINDING, REPORT_FILES, admission, admitted, article, setup } from "./support/harness.mjs";

let env;
before(async () => {
  env = await setup();
});
after(async () => {
  await env.stop();
});

const sha = (data) => createHash("sha256").update(data).digest("hex");

test("two pipelines admit one immutable scheduled bundle as two bound operations", async () => {
  env.execution.served.add(OTHER_BINDING);
  assert.equal((await env.call("PUT", "/v1/pipelines/reports-b", "operator", { policy_id: "standard", binding_id: OTHER_BINDING, state: "active" })).status, 200);
  const bundle = JSON.stringify({ schema: BUNDLE, articles: [article(501)] });
  const fingerprint = sha(bundle);
  for (const [schedule, pipeline] of [["first", "reports"], ["second", "reports-b"]]) {
    assert.equal((await env.call("PUT", `/v1/schedules/${schedule}`, "operator", { pipeline, policy_id: "standard", state: "active" })).status, 200);
    assert.equal((await env.call("PUT", `/v1/schedules/${schedule}/sources`, "manual", bundle)).status, 202);
  }
  const before = await env.counts();
  await env.stack.worker.scheduled({ cron: "*/5 * * * *" });
  const rows = await env.q("SELECT * FROM operations WHERE principal = 'scheduler' ORDER BY pipeline");
  assert.deepEqual(rows.map((r) => [r.pipeline, r.binding_id, r.fingerprint]), [
    ["reports", BINDING, fingerprint],
    ["reports-b", OTHER_BINDING, fingerprint],
  ]);
  const after = await env.counts();
  assert.equal(after.operations, before.operations + 2);
  assert.equal(after.max_seq, before.max_seq + 2);
  assert.equal((await env.q("SELECT * FROM snapshots WHERE fingerprint = ?", fingerprint)).length, 1);
  assert.equal((await env.r2(`snapshots/${fingerprint}`)).length, 1, "one immutable object");
  for (const row of rows) {
    const done = await env.waitState(row.operation_id, "submitted");
    assert.equal(env.execution.jobFor(row.operation_id).binding_id, row.binding_id);
    assert.equal(done.binding_id, row.binding_id);
  }
  // A refire admits nothing more for either schedule.
  await env.stack.worker.scheduled({ cron: "*/5 * * * *" });
  assert.equal((await env.counts()).operations, after.operations);
  for (const [schedule, pipeline] of [["first", "reports"], ["second", "reports-b"]]) {
    await env.call("PUT", `/v1/schedules/${schedule}`, "operator", { pipeline, policy_id: "standard", state: "paused" });
  }
});

const LONE = "\\ud800";
const lone = (value) => value.replace("@", LONE);
const invalidFields = {
  content: (a) => ({ ...a, content: "x@y" }),
  title: (a) => ({ ...a, title: "Title @" }),
  source: (a) => ({ ...a, source: "Source @" }),
  summary: (a) => ({ ...a, summary: "@" }),
  content_kind: (a) => ({ ...a, content_kind: "@" }),
  source_links: (a) => ({ ...a, source_links: ["https://example.test/@"] }),
  cves: (a) => ({ ...a, cves: ["CVE-2026-0001@"] }),
};

test("a lone surrogate in any string or list field is refused before any write", async () => {
  const before = await env.counts();
  const submits = env.execution.counters.submits;
  for (const [field, change] of Object.entries(invalidFields)) {
    const body = lone(JSON.stringify(admission(`surrogate-${field}`, [change(article(510))])));
    assert.match(body, /\\ud800/);
    const response = await env.admit(body);
    assert.deepEqual([response.status, response.body.error], [422, "request_malformed"], field);
  }
  const lowSurrogate = JSON.stringify(admission("surrogate-low", [article(511, "a")])).replace('"a"', '"\\udc00a"');
  assert.equal((await env.admit(lowSurrogate)).status, 422);
  const bundle = lone(JSON.stringify({ schema: BUNDLE, articles: [article(512, "@")] }));
  assert.equal((await env.call("PUT", "/v1/schedules/first/sources", "manual", bundle)).status, 422);
  assert.deepEqual(await env.counts(), before);
  assert.equal(env.execution.counters.submits, submits);
});

test("valid non-ASCII and astral text, raw or escaped, is admitted with UTF-8 content digests", async () => {
  const content = "Exploited in café systems 😀 — 漢字";
  const raw = admission("unicode-raw", [{ ...article(520, content), title: "Café 😀", source: "Ünïcode", summary: "😀", cves: ["CVE-2026-0002"], source_links: ["https://example.test/é"] }]);
  const escaped = JSON.stringify(admission("unicode-escaped", [article(521, "😀 é")])).replace("😀", "\\ud83d\\ude00").replace("é", "\\u00e9");
  for (const [body, expected] of [[JSON.stringify(raw), content], [escaped, "😀 é"]]) {
    const response = await env.admit(body);
    assert.equal(response.status, 201);
    const id = response.body.operation.operation_id;
    const [row] = await env.q("SELECT content_sha256 FROM operation_articles WHERE operation_id = ?", id);
    assert.equal(row.content_sha256, sha(Buffer.from(expected, "utf8")));
    await env.waitState(id, "submitted");
  }
});

test("a success receipt without an artifact is a terminal, observable rejection", async () => {
  const id = await admitted(env, admission("null-artifact", [article(530)]));
  const lastGood = await env.q("SELECT * FROM targets ORDER BY target");
  const job = env.execution.jobFor(id);
  job.state = "running";
  await env.reconcile();
  assert.equal((await env.row(id)).state, "submitted", "a genuine nonterminal state stays pending");
  job.state = "succeeded";
  job.artifact = null;
  await env.reconcile();
  const row = await env.row(id);
  assert.deepEqual([row.state, row.reason, row.artifact_sha256], ["failed", "artifact_rejected", null]);
  const tokens = await env.q("SELECT token FROM events WHERE operation_id = ? AND kind = 'artifact_rejected'", id);
  assert.deepEqual(tokens.map((t) => t.token), ["receipt_success_without_artifact"]);
  assert.equal((await env.publish(id)).status, 409);
  assert.deepEqual(await env.q("SELECT * FROM targets ORDER BY target"), lastGood);
});

test("interrupted, then concurrent, completion records exactly one completion", async () => {
  const id = await admitted(env, admission("completion-race", [article(540)]));
  env.execution.succeed(id, REPORT_FILES);
  await env.fault("before_completion_batch");
  await env.reconcile();
  assert.equal((await env.row(id)).state, "submitted");
  await env.fault("before_completion_batch", 2, "delay", 1500);
  await Promise.all([env.reconcile(), env.reconcile()]);
  const row = await env.row(id);
  assert.equal(row.state, "completed");
  assert.equal((await env.q("SELECT * FROM events WHERE operation_id = ? AND kind = 'completed'", id)).length, 1);
  assert.equal((await env.q("SELECT * FROM artifacts WHERE artifact_sha256 = ?", row.artifact_sha256)).length, 1);
});

test("status reads carry the operation's snapshot and binding identities", async () => {
  const original = globalThis.fetch;
  let observed;
  globalThis.fetch = async (_url, options) => {
    observed = new Headers(options.headers);
    return new Response("{}", { status: 404 });
  };
  try {
    await readExecution({}, { EXECUTION_URL: "http://127.0.0.1:1", EXECUTION_TOKEN: "synthetic-only-token", CALL_TIMEOUT_MS: 1000 }, "a".repeat(64), "b".repeat(64), "c".repeat(64));
  } finally {
    globalThis.fetch = original;
  }
  assert.equal(observed.get("x-snapshot-sha256"), "b".repeat(64));
  assert.equal(observed.get("x-binding-id"), "c".repeat(64));
});

test("a service that lost its operation mapping recovers it through the ordinary status pull", async () => {
  const id = await admitted(env, admission("lost-mapping", [article(550)]));
  const jobs = env.execution.counters.jobsCreated;
  const submits = env.execution.counters.submits;
  env.execution.succeed(id, REPORT_FILES);
  const job = env.execution.jobFor(id);
  env.execution.loseMapping(id);
  await env.reconcile();
  const row = await env.row(id);
  assert.equal(row.state, "completed");
  assert.equal(row.execution_id, job.execution_id);
  assert.equal(env.execution.counters.jobsCreated, jobs, "no new job");
  assert.equal(env.execution.counters.submits, submits, "no resubmission");
  assert.equal(env.execution.counters.rebuilt, 1);
});

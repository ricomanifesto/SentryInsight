// A runnable synthetic demonstration of the product history and its research
// export on the local stack (real local D1, R2 and Queue; the fake execution
// service and the durable fake publisher from tests/support). Nothing is
// deployed, fetched or generated.
//
//   MINIFLARE_MODULE=/path/to/miniflare/dist/src/index.js \
//     node local/export-demo.mjs --out fixtures/export
//
// It writes example export pages, a retained-source response and a summary
// of the checks it made, and exits non-zero if any check fails.

import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { mkdir, writeFile } from "node:fs/promises";
import path from "node:path";
import { REPORT_FILES, admission, admitted, article, completed, setup } from "../tests/support/harness.mjs";

const sha = (data) => createHash("sha256").update(data).digest("hex");
const out = process.argv[process.argv.indexOf("--out") + 1];
if (!process.argv.includes("--out") || !out) {
  console.error("usage: node local/export-demo.mjs --out <directory>");
  process.exit(2);
}

const checks = [];
const check = (name, fn) => {
  fn();
  checks.push(name);
};
const runId = (id) => `sentryinsight:run:${id}`;
const sourceId = (link, content) => `sentryinsight:source:${sha(link)}:${sha(content)}`;
const byId = (records) => new Map(records.map((r) => [r.record_id, r]));
const write = (name, value) => writeFile(path.join(out, name), `${JSON.stringify(value, null, 2)}\n`);

const env = await setup();
try {
  await mkdir(out, { recursive: true });
  const advisory = { ...article(1, "Vendor advisory text: CVE-2026-0101 is exploited in the wild."), content_kind: "article", source: "Example Vendor" };
  const feed = { ...article(2, "Feed excerpt: a botnet targets edge routers."), content_kind: "feed", source: "Example Feed" };

  // 1. Admit, retain, execute (the service excludes the excerpt), verify, publish.
  const first = admission("demo-run-1", [advisory, feed]);
  const a = await admitted(env, first);
  env.execution.succeed(a, REPORT_FILES, (job) => {
    job.executed = job.executed.filter((x) => x.article_key === advisory.link);
  });
  await env.reconcile();
  await env.waitState(a, "completed");
  assert.equal((await env.publish(a, "site")).status, 200);
  const { cursor: afterFirst } = await env.exportAll();

  // 2. Replay the same admission: the same operation, nothing written.
  const replay = await env.admit(first);
  check("replayed admission is the same operation", () => assert.deepEqual([replay.status, replay.body.operation.operation_id], [200, a]));

  // 3. A changed revision, a syndicated copy and a metadata-only record.
  const revised = { ...advisory, content: "Vendor advisory text, revised: CVE-2026-0101 patch released." };
  const copy = { ...article(3, revised.content), source: "Example Syndicator" };
  const bare = { ...article(4, ""), source: "Example Index" };
  // Distinct report bytes: identical artifacts converge on one publication.
  const b = await completed(env, admission("demo-run-2", [revised, copy, bare, feed]), { "index.html": "<html>revised report</html>\n" });
  assert.equal((await env.publish(b, "site")).status, 200);
  assert.equal((await env.publish(b, "mirror")).status, 200);
  const incremental = (await env.exportPage(afterFirst, 25)).body;

  // 4. A reused source revision label with different bytes.
  const conflict = await env.admit(admission("demo-run-1", [article(5)]));
  check("conflicting identity is refused", () => assert.equal(conflict.status, 409));

  // 5. A failed run and 6. an incomplete (dead-lettered) run.
  const c = await admitted(env, admission("demo-failed", [article(6)]));
  env.execution.fail(c, "generation_failed");
  await env.reconcile();
  await env.waitState(c, "failed");
  await env.fault("after_intent_before_send");
  await env.admit(admission("demo-incomplete", [article(7)]));
  const d = (await env.one("SELECT operation_id FROM operations WHERE source_revision = 'demo-incomplete'")).operation_id;
  await env.stack.worker.queue(env.stack.queues.dead, [{ id: "demo-dlq", timestamp: new Date(), attempts: 1, body: { operation_id: d, generation: 1 } }]);
  await env.waitState(d, "dead_letter");

  // 7. An interrupted handoff, recovered by the sweeper.
  await env.fault("after_intent_before_send");
  await env.admit(admission("demo-interrupted", [article(8)]));
  const e = (await env.one("SELECT operation_id FROM operations WHERE source_revision = 'demo-interrupted'")).operation_id;
  await env.waitFor(async () => {
    await env.reconcile();
    return (await env.row(e)).state === "submitted";
  });
  env.execution.succeed(e, { "index.html": "recovered\n" });
  await env.reconcile();
  await env.waitState(e, "completed");

  // 8. The older run is refused for the mirror; last-good stays on the newer.
  const refusal = await env.publish(a, "mirror");
  const lastGood = await env.one("SELECT last_good_operation FROM targets WHERE target = 'mirror'");
  check("stale publication is refused", () => assert.equal(refusal.body.error, "stale_candidate"));
  check("last-good is not replaced", () => assert.equal(lastGood.last_good_operation, b));

  // 9. Backfill, incremental and replayed exports.
  const pages = [];
  let cursor = 0;
  for (;;) {
    const page = (await env.exportPage(cursor, 25)).body;
    pages.push(page);
    cursor = page.next_cursor;
    if (!page.has_more) break;
  }
  const backfill = byId(pages.flatMap((p) => p.records));
  const replayed = byId((await env.exportAll()).records);
  check("a replayed export is identical", () => assert.deepEqual(replayed, backfill));

  const run = (id) => backfill.get(runId(id));
  check("succeeded and published", () => assert.deepEqual([run(b).run.outcome, run(b).report_published], ["succeeded", true]));
  check("a refusal is recorded per target, apart from the earlier publication", () =>
    assert.deepEqual(run(a).publications.map((p) => [p.target, p.state, p.reason]), [["mirror", "refused", "stale_candidate"], ["site", "published", null]]),
  );
  check("failed run is exported as failed", () => assert.deepEqual([run(c).run.outcome, run(c).run.reason], ["failed", "generation_failed"]));
  check("incomplete run is exported as incomplete", () => assert.equal(run(d).run.outcome, "incomplete"));
  check("recovered run succeeded once", () => assert.equal(run(e).run.outcome, "succeeded"));
  check("conflict is visible on the existing run", () => assert.equal(run(a).identity_conflicts.length, 1));
  check("excluded source is marked", () => assert.deepEqual(run(a).sources.map((s) => s.outcome), ["executed", "excluded"]));
  const revisedRecord = backfill.get(sourceId(revised.link, revised.content));
  check("changed content is revision 2", () => assert.equal(revisedRecord.revision.index, 2));
  check("syndicated copy is not independent", () =>
    assert.equal(backfill.get(sourceId(copy.link, copy.content)).independence.status, "duplicate_content"),
  );
  check("empty content is metadata-only", () => assert.equal(backfill.get(sourceId(bare.link, "")).evidence.kind, "metadata_only"));
  check("the incremental page holds the second run and omits the untouched first", () => {
    assert.ok(incremental.records.some((r) => r.record_id === runId(b)));
    assert.ok(!incremental.records.some((r) => r.record_id === runId(a)));
  });

  // 10. Retained source text, re-verified on read.
  const full = backfill.get(sourceId(advisory.link, advisory.content));
  const retained = await env.call("GET", full.evidence.retained.fetch, "exporter");
  check("retained text matches its digest", () => assert.equal(retained.body.content_sha256, full.content_sha256));

  await write("page-backfill.json", { pages });
  await write("page-incremental.json", incremental);
  await write("source-retained.json", retained.body);
  const summary = {
    schema: "sentryinsight-export-demo/1",
    note: "Synthetic local run: real local D1, R2 and Queue, fake execution service and fake publisher. Not hosted evidence.",
    runs: { published_then_refused: a, revised_and_published: b, failed: c, incomplete: d, recovered: e },
    records: backfill.size,
    checks,
  };
  await write("demo-summary.json", summary);
  console.log(JSON.stringify({ ok: true, records: backfill.size, checks: checks.length, out }));
} finally {
  await env.stop();
}

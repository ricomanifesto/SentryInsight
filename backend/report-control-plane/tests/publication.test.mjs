// Publication against real local D1 and the durable fake publisher: A6, A15,
// A16, A33 to A35, W-8, competing targets, and the settlement mechanism
// itself exercised directly on the real local D1 binding.
import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { after, before, test } from "node:test";
import { settle } from "../src/publication.js";
import { REPORT_FILES, admission, article, completed, setup, sleep } from "./support/harness.mjs";

let env;
before(async () => {
  env = await setup();
});
after(async () => {
  await env.stop();
});

const sha = (data) => createHash("sha256").update(data).digest("hex");
const pubId = (target, artifact) => sha(`report-control-plane/publication/1\n${target}\n${artifact}`);
let next = 2000;
async function report(label, variant = label) {
  return completed(env, admission(`${label}-${next}`, [article(next++)]), { ...REPORT_FILES, "reports/2026-01-01.md": `# ${variant}\n` });
}
const effectsFor = async (id) => (await env.publisherState()).effects.filter((e) => e.publication_id === id).length;
const pubRow = (id) => env.one("SELECT * FROM publications WHERE publication_id = ?", id);
const targetRow = (t) => env.one("SELECT * FROM targets WHERE target = ?", t);

test("A15 effect applied, acknowledgement lost: unresolved, then settled by observation, one effect", async () => {
  const id = await report("a15");
  const artifact = (await env.row(id)).artifact_sha256;
  const p = pubId("site-a15", artifact);
  await env.publisherControl({ drop_ack: [p] });
  const first = await env.publish(id, "site-a15");
  assert.equal(first.status, 202);
  assert.equal(first.body.publication.state, "unresolved");
  assert.equal(await effectsFor(p), 1, "the effect happened");
  assert.equal((await targetRow("site-a15")).last_good_publication_id, null);
  await env.reconcile();
  assert.equal((await pubRow(p)).state, "published");
  const t = await targetRow("site-a15");
  assert.deepEqual([t.last_good_publication_id, t.last_good_artifact, t.active_publication_id], [p, artifact, null]);
  assert.equal(await effectsFor(p), 1);
});

test("A35 converged operations publish once and share the receipt", async () => {
  const articles = [article(next++)];
  const files = { ...REPORT_FILES, "reports/2026-01-01.md": "# converged publication\n" };
  const one = await completed(env, admission(`a35-a-${next}`, articles), files);
  const two = await completed(env, admission(`a35-b-${next}`, articles), files);
  const first = await env.publish(one, "site-a35");
  const second = await env.publish(two, "site-a35");
  assert.equal(first.status, 200);
  assert.equal(second.status, 200);
  assert.equal(first.body.publication.publication_id, second.body.publication.publication_id);
  assert.equal(await effectsFor(first.body.publication.publication_id), 1);
});

test("A16 competing and stale: the newer is published; the older is refused by sequence", async () => {
  const older = await report("a16-old");
  const newer = await report("a16-new");
  const published = await env.publish(newer, "site-a16");
  assert.equal(published.status, 200);
  const stale = await env.publish(older, "site-a16");
  assert.equal(stale.status, 409);
  assert.equal(stale.body.error, "stale_candidate");
  const t = await targetRow("site-a16");
  assert.equal(t.last_good_operation, newer);
  assert.equal((await env.publisherState()).effects.filter((e) => e.target === "site-a16").length, 1);
});

test("A6 overlapping claims on one target: one winner, one effect", async () => {
  const a = await report("a6-a");
  const b = await report("a6-b");
  for (const id of [a, b]) await env.publisherControl({ hold_ms: { [pubId("site-a6", (await env.row(id)).artifact_sha256)]: 700 } });
  const results = await Promise.all([env.publish(a, "site-a6"), env.publish(b, "site-a6")]);
  const statuses = results.map((r) => r.status).sort();
  assert.deepEqual(statuses, [200, 409]);
  assert.equal(results.find((r) => r.status === 409).body.error, "claim_held");
  assert.equal((await env.publisherState()).effects.filter((e) => e.target === "site-a6").length, 1);
});

test("A33 stale-owner settlement: zero rows on both statements, receipt and last-good unchanged", async () => {
  const id = await report("a33");
  const artifact = (await env.row(id)).artifact_sha256;
  const p = pubId("site-a33", artifact);
  await env.fault("delay_before_settle", 1, "delay", 3000);
  const slow = env.publish(id, "site-a33");
  await env.waitFor(async () => (await effectsFor(p)) === 1);
  await sleep(1700); // the slow owner's claim expires while it waits to settle
  const repaired = await env.publish(id, "site-a33");
  assert.equal(repaired.status, 200, "a later request observes the receipt and settles it");
  const settledPublication = await pubRow(p);
  const settledTarget = await targetRow("site-a33");
  assert.equal(settledTarget.last_good_publication_id, p, "the target already names this publication");
  const late = await slow;
  assert.equal(late.body.error, "settle_lost");
  assert.deepEqual(await pubRow(p), settledPublication, "receipt unchanged");
  assert.deepEqual(await targetRow("site-a33"), settledTarget, "last-good unchanged");
  assert.equal(await effectsFor(p), 1);
});

test("A34 a late old effect is refused by the publisher's fence", async () => {
  const older = await report("a34-old");
  const newer = await report("a34-new");
  const oldPub = pubId("site-a34", (await env.row(older)).artifact_sha256);
  const newPub = pubId("site-a34", (await env.row(newer)).artifact_sha256);
  await env.publisherControl({ hold_ms: { [oldPub]: 3500 } });
  const slow = env.publish(older, "site-a34");
  await env.waitFor(async () => (await pubRow(oldPub))?.state === "claimed");
  await sleep(1700); // the old claim expires; the old call is still held at the publisher
  const current = await env.publish(newer, "site-a34");
  assert.equal(current.status, 200);
  assert.equal((await pubRow(oldPub)).state, "superseded");
  await slow;
  await sleep(2500); // the held old call reaches the publisher and is refused there
  const state = await env.publisherState();
  assert.equal(state.receipts[oldPub], undefined);
  assert.equal(state.effects.filter((e) => e.target === "site-a34").length, 1);
  const t = await targetRow("site-a34");
  assert.equal(t.last_good_publication_id, newPub);
  await env.reconcile();
  assert.equal((await targetRow("site-a34")).last_good_publication_id, newPub, "last-good never moves backward");
});

test("W-8 claimed, then a crash before the effect: the next claimant observes nothing and publishes once", async () => {
  const id = await report("w8");
  const p = pubId("site-w8", (await env.row(id)).artifact_sha256);
  await env.fault("after_claim_before_effect");
  assert.equal((await env.publish(id, "site-w8")).status, 500);
  assert.equal((await pubRow(p)).state, "claimed");
  assert.equal(await effectsFor(p), 0);
  const inProgress = await env.publish(id, "site-w8");
  assert.deepEqual([inProgress.status, inProgress.body.publication.state], [202, "claimed"], "a live claim is not taken over");
  assert.equal(await effectsFor(p), 0);
  await sleep(1700);
  const retried = await env.publish(id, "site-w8");
  assert.equal(retried.status, 200);
  assert.equal(await effectsFor(p), 1);
  assert.equal((await pubRow(p)).attempts, 2);
});

test("competing targets: one artifact published to two targets settles each independently", async () => {
  const id = await report("targets");
  assert.equal((await env.publish(id, "site-x")).status, 200);
  assert.equal((await env.publish(id, "site-y")).status, 200);
  const artifact = (await env.row(id)).artifact_sha256;
  for (const t of ["site-x", "site-y"]) {
    assert.equal((await targetRow(t)).last_good_artifact, artifact);
    assert.equal(await effectsFor(pubId(t, artifact)), 1);
  }
});

// The settlement mechanism, run directly on the real local D1 binding.
test("settlement is all-or-nothing: stale, wrong-token and inconsistent pairs change neither row", async () => {
  const db = env.stack.db;
  const id = await report("settle");
  const row = await env.row(id);
  const target = "site-settle";
  const p = pubId(target, row.artifact_sha256);
  await db.batch([
    db.prepare(
      `INSERT INTO publications (publication_id, target, artifact_sha256, operation_id, candidate_seq, state, claim_token, created_at, updated_at)
       VALUES (?, ?, ?, ?, ?, 'claimed', 'tok-current', 0, 0)`,
    ).bind(p, target, row.artifact_sha256, id, row.seq),
    db.prepare(
      `INSERT INTO targets (target, active_publication_id, claim_token, claim_expires_at, updated_at) VALUES (?, ?, 'tok-current', 0, 0)`,
    ).bind(target, p),
  ]);
  const publication = await pubRow(p);
  const receipt = { publication_id: p, receipt_id: "receipt-test", target, artifact_sha256: row.artifact_sha256, remote_version: 1, candidate_seq: row.seq };
  const snapshot = async () => [await pubRow(p), await targetRow(target)];

  const before = await snapshot();
  assert.equal(await settle(db, publication, "tok-wrong", receipt), false, "wrong claim token");
  assert.deepEqual(await snapshot(), before);

  // Inconsistent pair: the target claims the publication but the publication
  // row is no longer held. The coupled statements still change neither row.
  await db.prepare("UPDATE publications SET state = 'conflict' WHERE publication_id = ?").bind(p).run();
  const inconsistent = await snapshot();
  assert.equal(await settle(db, publication, "tok-current", receipt), false);
  assert.deepEqual(await snapshot(), inconsistent);
  await db.prepare("UPDATE publications SET state = 'claimed' WHERE publication_id = ?").bind(p).run();

  assert.equal(await settle(db, publication, "tok-current", receipt), true, "the current claim settles");
  const settled = await snapshot();
  assert.equal(settled[0].state, "published");
  assert.equal(settled[1].last_good_publication_id, p);

  // A stale owner retrying after settlement: the target already names this
  // same publication as last-good, and still neither row changes.
  assert.equal(await settle(db, publication, "tok-current", receipt), false);
  assert.deepEqual(await snapshot(), settled);
  assert.equal((await env.q("SELECT * FROM events WHERE subject = ? AND kind = 'published'", p)).length, 1);
});

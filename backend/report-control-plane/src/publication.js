// Publication with a named active claim, a publisher-side fence and
// all-or-nothing settlement.
//
// The target row names its active publication and claim. Before a different
// publication may take an expired claim, the named publication is observed at
// the publisher: a receipt is settled, no receipt is superseded. Observation is
// repair; the fence is the publisher's conditional effect (expected remote
// version and an increasing candidate sequence), so a late old call cannot
// apply after a newer one.
//
// Every pair of target and publication writes is one D1 batch whose statements
// are coupled in SQL: the target update requires the publication's expected
// state, and the publication update requires a fresh token or nonce that only
// the target update in the same batch can have written. Both apply or neither
// does; the Worker reads both change counts and treats any other combination
// as an invariant violation.

import { allOrNone, now, record, rotatingBatch } from "./db.js";
import { fault } from "./faults.js";
import { publicationId } from "./identity.js";
import { observePublication, postPublication } from "./publisher-client.js";
import { randomToken } from "./util.js";

const FRESH = "('intent', 'conflict', 'superseded')";
const HELD = "('claimed', 'unresolved')";

function publicationRow(db, id) {
  return db.prepare("SELECT * FROM publications WHERE publication_id = ?").bind(id).first();
}

function targetRow(db, target) {
  return db.prepare("SELECT * FROM targets WHERE target = ?").bind(target).first();
}

export function publicationView(p) {
  if (p === null) return null;
  const receipt = p.receipt ? JSON.parse(p.receipt) : null;
  return {
    publication_id: p.publication_id,
    target: p.target,
    artifact_sha256: p.artifact_sha256,
    operation_id: p.operation_id,
    candidate_seq: p.candidate_seq,
    state: p.state,
    reason: p.reason,
    receipt_id: receipt?.receipt_id ?? null,
    remote_version: receipt?.remote_version ?? null,
  };
}

export function targetView(t) {
  if (t === null) return null;
  return {
    target: t.target,
    last_good: t.last_good_publication_id
      ? {
          artifact_sha256: t.last_good_artifact,
          operation_id: t.last_good_operation,
          seq: t.last_good_seq,
          publication_id: t.last_good_publication_id,
        }
      : null,
    remote_version: t.remote_version,
    active_publication_id: t.active_publication_id,
  };
}

// An audit event for a claim transition, written in the claim's own batch and
// only when its target update applied (the claim token is fresh, so only that
// update can have written it). It follows the coupled statements, so the
// change counts allOrNone reads are unchanged.
function claimEvent(db, subject, kind, target, token, at) {
  return db
    .prepare(
      `INSERT INTO events (subject, kind, token, detail, at)
       SELECT ?, ?, NULL, NULL, ? WHERE EXISTS (SELECT 1 FROM targets WHERE target = ? AND claim_token = ?)`,
    )
    .bind(subject, kind, at, target, token);
}

// Claim a free target for a fresh publication.
async function claimFree(db, settings, p) {
  const token = randomToken();
  const at = now();
  const results = await db.batch([
    db
      .prepare(
        `UPDATE targets SET active_publication_id = ?, claim_token = ?, claim_expires_at = ?, updated_at = ?
         WHERE target = ? AND active_publication_id IS NULL AND last_good_seq < ?
           AND EXISTS (SELECT 1 FROM publications WHERE publication_id = ? AND state IN ${FRESH}) RETURNING rowid`,
      )
      .bind(p.publication_id, token, at + settings.PUBLICATION_CLAIM_MS, at, p.target, p.candidate_seq, p.publication_id),
    db
      .prepare(
        `UPDATE publications SET state = 'claimed', claim_token = ?, attempts = attempts + 1, reason = NULL, updated_at = ?
         WHERE publication_id = ? AND state IN ${FRESH}
           AND EXISTS (SELECT 1 FROM targets WHERE target = ? AND claim_token = ?) RETURNING rowid`,
      )
      .bind(token, at, p.publication_id, p.target, token),
    claimEvent(db, p.publication_id, "publication_claimed", p.target, token, at),
  ]);
  return allOrNone(results, 2) ? token : null;
}

// Re-take this publication's own expired claim after observing no receipt.
async function reclaimOwn(db, settings, p, oldToken) {
  const token = randomToken();
  const at = now();
  const results = await db.batch([
    db
      .prepare(
        `UPDATE targets SET claim_token = ?, claim_expires_at = ?, updated_at = ?
         WHERE target = ? AND active_publication_id = ? AND claim_token = ? AND claim_expires_at < ?
           AND EXISTS (SELECT 1 FROM publications WHERE publication_id = ? AND claim_token = ? AND state IN ${HELD}) RETURNING rowid`,
      )
      .bind(token, at + settings.PUBLICATION_CLAIM_MS, at, p.target, p.publication_id, oldToken, at, p.publication_id, oldToken),
    db
      .prepare(
        `UPDATE publications SET state = 'claimed', claim_token = ?, attempts = attempts + 1, updated_at = ?
         WHERE publication_id = ? AND claim_token = ? AND state IN ${HELD}
           AND EXISTS (SELECT 1 FROM targets WHERE target = ? AND claim_token = ?) RETURNING rowid`,
      )
      .bind(token, at, p.publication_id, oldToken, p.target, token),
    claimEvent(db, p.publication_id, "publication_reclaimed", p.target, token, at),
  ]);
  return allOrNone(results, 2) ? token : null;
}

// Supersede another publication's expired claim (observed: no receipt) and
// claim the target for this one.
async function takeOver(db, settings, p, previous, oldToken) {
  const token = randomToken();
  const at = now();
  const results = await db.batch([
    db
      .prepare(
        `UPDATE targets SET active_publication_id = ?, claim_token = ?, claim_expires_at = ?, updated_at = ?
         WHERE target = ? AND active_publication_id = ? AND claim_token = ? AND claim_expires_at < ? AND last_good_seq < ?
           AND EXISTS (SELECT 1 FROM publications WHERE publication_id = ? AND state IN ${FRESH})
           AND EXISTS (SELECT 1 FROM publications WHERE publication_id = ? AND claim_token = ? AND state IN ${HELD}) RETURNING rowid`,
      )
      .bind(p.publication_id, token, at + settings.PUBLICATION_CLAIM_MS, at, p.target, previous, oldToken, at, p.candidate_seq,
        p.publication_id, previous, oldToken),
    db
      .prepare(
        `UPDATE publications SET state = 'claimed', claim_token = ?, attempts = attempts + 1, reason = NULL, updated_at = ?
         WHERE publication_id = ? AND state IN ${FRESH}
           AND EXISTS (SELECT 1 FROM targets WHERE target = ? AND claim_token = ?) RETURNING rowid`,
      )
      .bind(token, at, p.publication_id, p.target, token),
    db
      .prepare(
        `UPDATE publications SET state = 'superseded', claim_token = NULL, updated_at = ?
         WHERE publication_id = ? AND claim_token = ? AND state IN ${HELD}
           AND EXISTS (SELECT 1 FROM targets WHERE target = ? AND claim_token = ?) RETURNING rowid`,
      )
      .bind(at, previous, oldToken, p.target, token),
    claimEvent(db, p.publication_id, "publication_claimed", p.target, token, at),
    claimEvent(db, previous, "publication_superseded", p.target, token, at),
  ]);
  return allOrNone(results, 3) ? token : null;
}

// All-or-nothing settlement: the target advances last-good and releases the
// claim, and the publication records its receipt, together or not at all.
// The second statement requires the nonce only the first can have written in
// this batch, so a stale owner — even when the target already names this same
// publication as last-good — changes neither row.
export async function settle(db, p, token, receipt) {
  const nonce = randomToken();
  const at = now();
  const settled = `EXISTS (SELECT 1 FROM targets WHERE target = ? AND coupling_nonce = ?)`;
  const results = await db.batch([
    db
      .prepare(
        `UPDATE targets SET last_good_artifact = ?, last_good_operation = ?, last_good_seq = ?,
           last_good_publication_id = ?, remote_version = ?, active_publication_id = NULL, claim_token = NULL,
           claim_expires_at = NULL, coupling_nonce = ?, updated_at = ?
         WHERE target = ? AND active_publication_id = ? AND claim_token = ? AND last_good_seq < ?
           AND EXISTS (SELECT 1 FROM publications WHERE publication_id = ? AND claim_token = ? AND state IN ${HELD}) RETURNING rowid`,
      )
      .bind(p.artifact_sha256, p.operation_id, p.candidate_seq, p.publication_id, receipt.remote_version, nonce, at,
        p.target, p.publication_id, token, p.candidate_seq, p.publication_id, token),
    db
      .prepare(
        `UPDATE publications SET state = 'published', receipt = ?, claim_token = NULL, reason = NULL, updated_at = ?
         WHERE publication_id = ? AND claim_token = ? AND state IN ${HELD} AND ${settled} RETURNING rowid`,
      )
      .bind(JSON.stringify(receipt), at, p.publication_id, token, p.target, nonce),
    db
      .prepare(`INSERT INTO events (subject, kind, token, detail, at) SELECT ?, 'published', NULL, ?, ? WHERE ${settled}`)
      .bind(p.publication_id, JSON.stringify({ target: p.target, remote_version: receipt.remote_version }), at, p.target, nonce),
  ]);
  return allOrNone(results, 2);
}

// Release a held claim after the publisher refused the effect.
async function release(db, p, token, reason) {
  const nonce = randomToken();
  const at = now();
  const results = await db.batch([
    db
      .prepare(
        `UPDATE targets SET active_publication_id = NULL, claim_token = NULL, claim_expires_at = NULL,
           coupling_nonce = ?, updated_at = ?
         WHERE target = ? AND active_publication_id = ? AND claim_token = ?
           AND EXISTS (SELECT 1 FROM publications WHERE publication_id = ? AND claim_token = ? AND state = 'claimed') RETURNING rowid`,
      )
      .bind(nonce, at, p.target, p.publication_id, token, p.publication_id, token),
    db
      .prepare(
        `UPDATE publications SET state = 'conflict', claim_token = NULL, reason = ?, updated_at = ?
         WHERE publication_id = ? AND claim_token = ? AND state = 'claimed'
           AND EXISTS (SELECT 1 FROM targets WHERE target = ? AND coupling_nonce = ?) RETURNING rowid`,
      )
      .bind(reason, at, p.publication_id, token, p.target, nonce),
  ]);
  return allOrNone(results, 2);
}

async function refuse(db, p, reason) {
  await db
    .prepare(`UPDATE publications SET state = 'refused', reason = ?, updated_at = ? WHERE publication_id = ? AND state IN ${FRESH} RETURNING rowid`)
    .bind(reason, now(), p.publication_id)
    .run();
  await record(db, { operationId: p.operation_id, subject: p.publication_id, kind: "publish_refused", token: reason, at: now() });
}

async function current(db, p) {
  return publicationView(await publicationRow(db, p.publication_id));
}

// Make the effect under a held claim, then settle, refuse or leave unresolved.
async function effect(env, settings, p, token, expectedRemote) {
  const db = env.PRODUCT_DB;
  await fault(env, "after_claim_before_effect");
  const outcome = await postPublication(settings, p, expectedRemote);
  if (outcome.kind === "receipt") {
    await fault(env, "delay_before_settle");
    const settled = await settle(db, p, token, outcome.receipt);
    if (!settled) await record(db, { subject: p.publication_id, kind: "settle_lost", at: now() });
    const view = await current(db, p);
    return { status: view.state === "published" ? 200 : 409, body: { publication: view, ...(settled ? {} : { error: "settle_lost" }) } };
  }
  if (outcome.kind === "conflict") {
    await release(db, p, token, outcome.reason);
    await record(db, { subject: p.publication_id, kind: "publish_conflict", token: outcome.reason, at: now() });
    return { status: 409, body: { error: "publish_conflict", reason: outcome.reason, publication: await current(db, p) } };
  }
  // The effect may or may not have happened: keep the claim, observe later.
  await db
    .prepare("UPDATE publications SET state = 'unresolved', updated_at = ? WHERE publication_id = ? AND claim_token = ? AND state = 'claimed'")
    .bind(now(), p.publication_id, token)
    .run();
  await record(db, { subject: p.publication_id, kind: "publish_unresolved", at: now() });
  return { status: 202, body: { publication: await current(db, p) } };
}

// Observe the publication named by an expired claim; settle a receipt.
// Returns "settled", "none" or "transient".
async function repairExpired(env, settings, t) {
  const db = env.PRODUCT_DB;
  const named = await publicationRow(db, t.active_publication_id);
  if (named === null) return "transient";
  const observed = await observePublication(settings, named);
  if (observed.kind === "transient") return "transient";
  if (observed.kind === "none") return "none";
  await settle(db, named, t.claim_token, observed.receipt);
  return "settled";
}

async function advance(env, settings, p) {
  const db = env.PRODUCT_DB;
  for (let round = 0; round < 3; round += 1) {
    p = await publicationRow(db, p.publication_id);
    if (p.state === "published") return { status: 200, body: { publication: publicationView(p) } };
    if (p.state === "refused") return { status: 409, body: { error: "refused", publication: publicationView(p) } };
    const t = await targetRow(db, p.target);
    if (t.last_good_seq >= p.candidate_seq) {
      await refuse(db, p, "stale_candidate");
      return { status: 409, body: { error: "stale_candidate", publication: await current(db, p), target: targetView(t) } };
    }
    if (t.active_publication_id === null) {
      const token = await claimFree(db, settings, p);
      if (token === null) continue;
      return effect(env, settings, p, token, t.remote_version);
    }
    if (t.claim_expires_at > now()) {
      if (t.active_publication_id === p.publication_id) return { status: 202, body: { publication: publicationView(p) } };
      return { status: 409, body: { error: "claim_held", publication: publicationView(p) } };
    }
    const repaired = await repairExpired(env, settings, t);
    if (repaired === "transient") return { status: 503, body: { error: "publisher_unavailable" } };
    if (repaired === "settled") continue;
    const token =
      t.active_publication_id === p.publication_id
        ? await reclaimOwn(db, settings, p, t.claim_token)
        : await takeOver(db, settings, p, t.active_publication_id, t.claim_token);
    if (token === null) continue;
    return effect(env, settings, p, token, t.remote_version);
  }
  return { status: 409, body: { error: "claim_contended", publication: await current(db, p) } };
}

export async function publish(env, settings, operation, target) {
  const db = env.PRODUCT_DB;
  // A projected run was published, or not, by its own producer; its
  // publications are observations, never effects made here.
  if (operation.origin === "project") return { status: 409, body: { error: "projection_not_publishable" } };
  if (!settings.publisherConfigured) return { status: 503, body: { error: "publisher_unconfigured" } };
  if (operation.state !== "completed") {
    await record(db, { operationId: operation.operation_id, kind: "publish_refused", token: "not_completed", at: now() });
    return { status: 409, body: { error: "not_publishable", state: operation.state } };
  }
  const id = await publicationId(target, operation.artifact_sha256);
  const at = now();
  await db.batch([
    db
      .prepare(
        `INSERT INTO publications (publication_id, target, artifact_sha256, operation_id, candidate_seq, state, created_at, updated_at)
         VALUES (?, ?, ?, ?, ?, 'intent', ?, ?) ON CONFLICT (publication_id) DO NOTHING`,
      )
      .bind(id, target, operation.artifact_sha256, operation.operation_id, operation.seq, at, at),
    db.prepare("INSERT INTO targets (target, updated_at) VALUES (?, ?) ON CONFLICT (target) DO NOTHING").bind(target, at),
  ]);
  return advance(env, settings, await publicationRow(db, id));
}

// Sweeper repair: settle any held or superseded publication whose effect the
// publisher has a receipt for. Never makes an effect itself.
export async function repairPublications(env, settings, limit) {
  const db = env.PRODUCT_DB;
  // Rotates through candidates (rotatingBatch), so publications that stay
  // unobservable cannot keep newer ones from being settled.
  const results = await rotatingBatch(
    db,
    "repair",
    `SELECT rowid AS cursor_key, * FROM publications WHERE state IN ('claimed', 'unresolved', 'superseded')
       AND rowid > ? AND rowid <= ? ORDER BY rowid LIMIT ?`,
    limit,
  );
  let settled = 0;
  for (const p of results) {
    const t = await targetRow(db, p.target);
    const held = t.active_publication_id === p.publication_id;
    if (held && p.state === "claimed" && t.claim_expires_at > now()) continue;
    const observed = await observePublication(settings, p);
    if (observed.kind !== "receipt") continue;
    if (held) {
      if (await settle(db, p, t.claim_token, observed.receipt)) settled += 1;
    } else if (p.state === "superseded" && t.active_publication_id === null && t.last_good_seq < p.candidate_seq) {
      const token = await claimFree(db, settings, p);
      if (token !== null && (await settle(db, p, token, observed.receipt))) settled += 1;
    }
  }
  return settled;
}

// Admission: one shared path for manual, event and scheduled entries.
//
// Order: D1 reserves bounded retained capacity before R2 stores a snapshot;
// one later batch writes the operation, snapshot and article rows together,
// then delivery is sent. Interrupted attempts retain their reservations.

import { event, isConstraintError, now, operation } from "./db.js";
import { fault } from "./faults.js";
import { operationId as deriveOperationId } from "./identity.js";
import { sendDelivery } from "./delivery.js";
import { backoff } from "./timing.js";
import { randomToken } from "./util.js";

export class SnapshotConflict extends Error {}

// Retained capacity, shared by principals and execute pipelines. No clock
// reset or automatic release can make interrupted/refused bytes unaccounted.
export const ADMISSION_LIMITS = Object.freeze({ attempts: 10_000, snapshots: 10_000, snapshotBytes: 256 * 1024 * 1024, refusalCells: 256 });

// Each INSERT decides capacity in the same D1 writer transaction as its
// reservation. Reads outside this batch never grant capacity. A known digest
// may have been conservatively charged at the full request limit on upgrade.
const snapshotFits = `EXISTS (SELECT 1 FROM admission_snapshots WHERE fingerprint = ? AND bytes >= ?)
  OR ((SELECT count(*) FROM admission_snapshots) < ?
      AND coalesce((SELECT sum(bytes) FROM admission_snapshots), 0) <= ? - ?)`;
function snapshotArgs(fingerprint, bytes) {
  return [fingerprint, bytes, ADMISSION_LIMITS.snapshots, ADMISSION_LIMITS.snapshotBytes, bytes];
}

function snapshotReservation(db, { principal, fingerprint, bytes, at }, operationId = null) {
  return db.prepare(`INSERT INTO admission_snapshots (fingerprint, bytes, principal, created_at)
    SELECT ?, ?, ?, ? WHERE (${snapshotFits})
    ${operationId === null ? "" : "AND EXISTS (SELECT 1 FROM admission_reservations WHERE operation_id = ?)"}
    ON CONFLICT (fingerprint) DO NOTHING`)
    .bind(fingerprint, bytes, principal, at, ...snapshotArgs(fingerprint, bytes), ...(operationId === null ? [] : [operationId]));
}

// Staged source bundles and admission share this snapshot ledger. Replacing
// a pending bundle cannot leave unlimited unaccounted immutable objects.
export async function reserveSnapshot(db, { principal, fingerprint, bytes }) {
  await snapshotReservation(db, { principal, fingerprint, bytes, at: now() }).run();
  const row = await db.prepare("SELECT bytes FROM admission_snapshots WHERE fingerprint = ?").bind(fingerprint).first();
  return row !== null && row.bytes >= bytes;
}

async function reserveAdmission(db, { principal, pipeline, sourceRevision, fingerprint, bytes, operationId }) {
  const at = now();
  await db.batch([
    db.prepare(`INSERT INTO admission_reservations (operation_id, pipeline, source_revision, fingerprint, principal, state, created_at)
      SELECT ?, ?, ?, ?, ?, 'reserved', ?
      WHERE (SELECT count(*) FROM admission_reservations) < ? AND (${snapshotFits})
      ON CONFLICT (operation_id) DO NOTHING`)
      .bind(operationId, pipeline, sourceRevision, fingerprint, principal, at, ADMISSION_LIMITS.attempts, ...snapshotArgs(fingerprint, bytes)),
    snapshotReservation(db, { principal, fingerprint, bytes, at }, operationId),
  ]);
  const row = await db.prepare(`SELECT r.operation_id FROM admission_reservations r
    JOIN admission_snapshots s ON s.fingerprint = r.fingerprint
    WHERE r.operation_id = ? AND r.pipeline = ? AND r.fingerprint = ? AND s.bytes >= ?`)
    .bind(operationId, pipeline, fingerprint, bytes).first();
  return row !== null;
}

// Refusals are aggregate cells, not an unbounded append-only stream. At most
// 256 principal/reason cells and one overflow cell retain the latest caller,
// fixed reason and operation id, plus counts and first/last timestamps.
export async function recordAdmissionRefusal(db, { principal, reason, operationId = null, subject = null }) {
  try {
    await writeAdmissionRefusal(db, { principal, reason, operationId, subject });
    return true;
  } catch {
    // A diagnostic-store outage must preserve the caller's original refusal.
    return false;
  }
}

async function writeAdmissionRefusal(db, { principal, reason, operationId, subject }) {
  const key = `${principal}:${reason}`;
  const at = now();
  await db.batch([
    db.prepare(`INSERT INTO admission_refusals (audit_key, principal, reason, occurrences, operation_id, subject, first_at, last_at)
      SELECT ?, ?, ?, 1, ?, ?, ?, ?
      WHERE (SELECT count(*) FROM admission_refusals WHERE audit_key <> 'overflow') < ?
         OR EXISTS (SELECT 1 FROM admission_refusals WHERE audit_key = ?)
      ON CONFLICT (audit_key) DO UPDATE SET occurrences = occurrences + 1,
        operation_id = excluded.operation_id, subject = excluded.subject, last_at = excluded.last_at`)
      .bind(key, principal, reason, operationId, subject, at, at, ADMISSION_LIMITS.refusalCells, key),
    db.prepare(`INSERT INTO admission_refusals (audit_key, principal, reason, occurrences, operation_id, subject, first_at, last_at)
      SELECT 'overflow', ?, ?, 1, ?, ?, ?, ? WHERE NOT EXISTS (SELECT 1 FROM admission_refusals WHERE audit_key = ?)
      ON CONFLICT (audit_key) DO UPDATE SET principal = excluded.principal, reason = excluded.reason,
        occurrences = occurrences + 1, operation_id = excluded.operation_id, subject = excluded.subject, last_at = excluded.last_at`)
      .bind(principal, reason, operationId, subject, at, at, key),
  ]);
}

// Store immutable bytes under their own SHA-256; never overwrite.
export async function putImmutable(bucket, key, bytes, sha256) {
  const stored = await bucket.put(key, bytes, { sha256, onlyIf: { etagDoesNotMatch: "*" } });
  if (stored !== null) return "created";
  const existing = await bucket.head(key);
  const checksum = existing?.checksums?.sha256;
  const existingHex = checksum ? [...new Uint8Array(checksum)].map((b) => b.toString(16).padStart(2, "0")).join("") : null;
  if (existingHex !== sha256 || existing.size !== bytes.byteLength) throw new SnapshotConflict(key);
  return "existing";
}

// A refused reuse of a source revision label stays visible: one conflict row
// per distinct refused snapshot, and one audit event written only by the
// insert that created it. The refused bytes are already in R2 under their own
// digest; the conflict row is what lets the export serve them, since their
// snapshot row rolled back with the refused batch. Nothing about the existing
// operation changes. When the label was reused under another policy, the
// refused snapshot can equal the existing one.
export async function recordConflict(db, { principal = null, pipeline, sourceRevision, fingerprint, existing, operationId = null }) {
  const nonce = randomToken();
  const at = now();
  await db.batch([
    db
      .prepare(
        `INSERT INTO identity_conflicts (pipeline, source_revision, refused_fingerprint, existing_operation_id,
           observation_nonce, observed_at, principal)
         VALUES (?, ?, ?, ?, ?, ?, ?) ON CONFLICT (pipeline, source_revision, refused_fingerprint) DO NOTHING`,
      )
      .bind(pipeline, sourceRevision, fingerprint, existing, nonce, at, principal),
    db
      .prepare(
        `INSERT INTO events (operation_id, kind, token, detail, at, principal)
         SELECT ?, 'identity_conflict', 'source_revision_conflict', ?, ?, ?
         WHERE EXISTS (SELECT 1 FROM identity_conflicts WHERE pipeline = ? AND source_revision = ?
           AND refused_fingerprint = ? AND observation_nonce = ?)`,
      )
      .bind(existing, JSON.stringify({ refused_fingerprint: fingerprint }), at, principal, pipeline, sourceRevision, fingerprint, nonce),
    db.prepare("UPDATE admission_reservations SET state = 'identity_conflict' WHERE operation_id = ?")
      .bind(operationId),
  ]);
}

export async function admit(env, settings, request) {
  const outcome = await admitRequest(env, settings, request);
  if (outcome.status >= 400) {
    await recordAdmissionRefusal(env.PRODUCT_DB, {
      principal: request.principal, reason: outcome.body.error,
      operationId: await deriveOperationId(request.pipeline, request.policyId, request.fingerprint),
    });
  }
  return outcome;
}

async function admitRequest(env, settings, request) {
  const { principal, pipeline, policyId, sourceRevision, articles, bytes, fingerprint } = request;
  const db = env.PRODUCT_DB;
  const binding = await db.prepare("SELECT policy_id, binding_id, state, mode FROM pipelines WHERE pipeline = ?").bind(pipeline).first();
  if (binding === null || binding.state !== "active") return { status: 422, body: { error: "pipeline_unavailable" } };
  if (binding.policy_id !== policyId) return { status: 422, body: { error: "policy_unsupported" } };
  // A projection pipeline records runs its producer already completed; it is
  // written only through the projection route.
  if (binding.mode === "project") return { status: 422, body: { error: "pipeline_projection_only" } };
  if (!settings.executionConfigured) return { status: 503, body: { error: "execution_unconfigured" } };

  const operationId = await deriveOperationId(pipeline, policyId, fingerprint);
  const existing = await operation(db, operationId);
  if (existing !== null) return { status: 200, operation: existing };

  // Already retained conflicts remain idempotent even after capacity fills.
  const knownConflict = await db.prepare(`SELECT existing_operation_id FROM identity_conflicts
    WHERE pipeline = ? AND source_revision = ? AND refused_fingerprint = ?`).bind(pipeline, sourceRevision, fingerprint).first();
  if (knownConflict !== null) {
    return { status: 409, body: { error: "source_revision_conflict", operation_id: knownConflict.existing_operation_id } };
  }
  if (!(await reserveAdmission(db, { principal, pipeline, sourceRevision, fingerprint, bytes: bytes.byteLength, operationId }))) {
    // A concurrent winner can have committed while this caller was reserving.
    const same = await operation(db, operationId);
    if (same !== null) return { status: 200, operation: same };
    return { status: 429, body: { error: "admission_capacity_exhausted" } };
  }

  await putImmutable(env.ARTIFACTS, `snapshots/${fingerprint}`, bytes, fingerprint);
  await fault(env, "after_snapshot_before_batch");

  const at = now();
  const statements = [
    // One immutable snapshot can back several operations (one scheduled bundle
    // admitted by two pipelines); duplicates and conflicts are still decided by
    // the operation insert below, which rolls the whole batch back.
    db
      .prepare("INSERT INTO snapshots (fingerprint, bytes, created_at) VALUES (?, ?, ?) ON CONFLICT (fingerprint) DO NOTHING")
      .bind(fingerprint, bytes.byteLength, at),
    db
      .prepare(
        `INSERT INTO operations (operation_id, pipeline, policy_id, binding_id, source_revision, fingerprint,
           principal, state, send_attempts, next_send_at, created_at, updated_at)
         VALUES (?, ?, ?, ?, ?, ?, ?, 'admitted', 1, ?, ?, ?)`,
      )
      .bind(operationId, pipeline, policyId, binding.binding_id, sourceRevision, fingerprint, principal, at + backoff(settings, 1), at, at),
  ];
  articles.forEach((article, position) => {
    statements.push(
      db
        .prepare(
          `INSERT INTO article_revisions (article_key, content_sha256, title, source, first_operation_id, created_at,
             content_kind, content_bytes, published_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?) ON CONFLICT (article_key, content_sha256) DO NOTHING`,
        )
        .bind(article.article_key, article.content_sha256, article.title, article.source, operationId, at,
          article.content_kind, article.content_bytes, article.published_at),
      db
        .prepare("INSERT INTO operation_articles (operation_id, position, article_key, content_sha256) VALUES (?, ?, ?, ?)")
        .bind(operationId, position, article.article_key, article.content_sha256),
    );
  });
  statements.push(
    db.prepare("UPDATE admission_reservations SET state = 'admitted' WHERE operation_id = ?").bind(operationId),
    event(db, { operationId, principal, kind: "admitted", token: principal, detail: { articles: articles.length }, at }),
  );
  try {
    await db.batch(statements);
  } catch (error) {
    if (!isConstraintError(error)) throw error;
    const same = await operation(db, operationId);
    if (same !== null) return { status: 200, operation: same };
    const conflict = await db
      .prepare("SELECT operation_id FROM operations WHERE pipeline = ? AND source_revision = ?")
      .bind(pipeline, sourceRevision)
      .first();
    if (conflict !== null) {
      await recordConflict(db, { principal, pipeline, sourceRevision, fingerprint, existing: conflict.operation_id, operationId });
      return { status: 409, body: { error: "source_revision_conflict", operation_id: conflict.operation_id } };
    }
    throw error;
  }

  await fault(env, "after_intent_before_send");
  const row = await operation(db, operationId);
  await sendDelivery(env, row);
  return { status: 201, operation: await operation(db, operationId) };
}

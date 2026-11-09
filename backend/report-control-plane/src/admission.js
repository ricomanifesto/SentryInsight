// Admission: one shared path for manual, event and scheduled entries.
//
// Order: the content-addressed snapshot is stored first (an orphan is
// harmless), then one batch writes the operation, snapshot and article rows
// together, and only then is the delivery sent. A constraint failure rolls
// the whole batch back; classification is by reading, never by writing.

import { event, isConstraintError, now, operation } from "./db.js";
import { fault } from "./faults.js";
import { operationId as deriveOperationId } from "./identity.js";
import { sendDelivery } from "./delivery.js";
import { backoff } from "./timing.js";
import { randomToken } from "./util.js";

export class SnapshotConflict extends Error {}

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
async function recordConflict(db, { pipeline, sourceRevision, fingerprint, existing }) {
  const nonce = randomToken();
  const at = now();
  await db.batch([
    db
      .prepare(
        `INSERT INTO identity_conflicts (pipeline, source_revision, refused_fingerprint, existing_operation_id,
           observation_nonce, observed_at)
         VALUES (?, ?, ?, ?, ?, ?) ON CONFLICT (pipeline, source_revision, refused_fingerprint) DO NOTHING`,
      )
      .bind(pipeline, sourceRevision, fingerprint, existing, nonce, at),
    db
      .prepare(
        `INSERT INTO events (operation_id, kind, token, detail, at)
         SELECT ?, 'identity_conflict', 'source_revision_conflict', ?, ?
         WHERE EXISTS (SELECT 1 FROM identity_conflicts WHERE pipeline = ? AND source_revision = ?
           AND refused_fingerprint = ? AND observation_nonce = ?)`,
      )
      .bind(existing, JSON.stringify({ refused_fingerprint: fingerprint }), at, pipeline, sourceRevision, fingerprint, nonce),
  ]);
}

export async function admit(env, settings, request) {
  const { principal, pipeline, policyId, sourceRevision, articles, bytes, fingerprint } = request;
  const db = env.PRODUCT_DB;
  const binding = await db.prepare("SELECT policy_id, binding_id, state FROM pipelines WHERE pipeline = ?").bind(pipeline).first();
  if (binding === null || binding.state !== "active") return { status: 422, body: { error: "pipeline_unavailable" } };
  if (binding.policy_id !== policyId) return { status: 422, body: { error: "policy_unsupported" } };

  const operationId = await deriveOperationId(pipeline, policyId, fingerprint);
  const existing = await operation(db, operationId);
  if (existing !== null) return { status: 200, operation: existing };

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
             content_kind, content_bytes)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?) ON CONFLICT (article_key, content_sha256) DO NOTHING`,
        )
        .bind(article.article_key, article.content_sha256, article.title, article.source, operationId, at,
          article.content_kind, article.content_bytes),
      db
        .prepare("INSERT INTO operation_articles (operation_id, position, article_key, content_sha256) VALUES (?, ?, ?, ?)")
        .bind(operationId, position, article.article_key, article.content_sha256),
    );
  });
  statements.push(event(db, { operationId, kind: "admitted", token: principal, detail: { articles: articles.length }, at }));
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
      await recordConflict(db, { pipeline, sourceRevision, fingerprint, existing: conflict.operation_id });
      return { status: 409, body: { error: "source_revision_conflict", operation_id: conflict.operation_id } };
    }
    throw error;
  }

  await fault(env, "after_intent_before_send");
  const row = await operation(db, operationId);
  await sendDelivery(env, row);
  return { status: 201, operation: await operation(db, operationId) };
}

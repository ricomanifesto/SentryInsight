// The scheduled handler does two separate things: scheduled admission of a
// staged source bundle, and reconciliation of recorded gaps. Reconciliation
// never calls the execution service to submit; it only re-sends deliveries,
// records exhaustion, pulls status and settles observed publications.

import { admit } from "./admission.js";
import { LIMITS } from "./config.js";
import { now, record, rotatingBatch, rowsChanged } from "./db.js";
import { sendDelivery } from "./delivery.js";
import { pullStatus } from "./completion.js";
import { repairPublications } from "./publication.js";
import { parseBundle } from "./request.js";
import { backoff } from "./timing.js";
import { sha256Hex } from "./util.js";

// Re-send one row's delivery, bounded per generation; exhaustion is recorded.
async function resend(env, settings, row, at) {
  const db = env.PRODUCT_DB;
  if (row.send_attempts >= LIMITS.maxSendAttempts) {
    const result = await db
      .prepare(
        `UPDATE operations SET state = 'dead_letter', reason = 'send_exhausted', claim_token = NULL,
           claim_expires_at = NULL, version = version + 1, updated_at = ?
         WHERE operation_id = ? AND state = ? AND version = ? AND delivery_generation = ? RETURNING operation_id`,
      )
      .bind(at, row.operation_id, row.state, row.version, row.delivery_generation)
      .run();
    if (rowsChanged(result) === 1) {
      await record(db, { operationId: row.operation_id, kind: "dead_letter", token: "send_exhausted", at });
      return "exhausted";
    }
    return "stale";
  }
  const attempt = row.send_attempts + 1;
  const result = await db
    .prepare(
      `UPDATE operations SET send_attempts = ?, next_send_at = ?,
         enqueued_at = CASE WHEN state = 'enqueued' THEN ? ELSE enqueued_at END,
         version = version + 1, updated_at = ?
       WHERE operation_id = ? AND state = ? AND version = ? AND delivery_generation = ? RETURNING operation_id`,
    )
    .bind(attempt, at + backoff(settings, attempt), at, at, row.operation_id, row.state, row.version, row.delivery_generation)
    .run();
  if (rowsChanged(result) !== 1) return "stale";
  const updated = { ...row, send_attempts: attempt, version: row.version + 1 };
  return (await sendDelivery(env, updated)) ? "resent" : "send_failed";
}

// Submitted operations to poll, rotating by admission order (rotatingBatch).
function pullBatch(db, limit) {
  return rotatingBatch(
    db,
    "pull",
    "SELECT seq AS cursor_key, * FROM operations WHERE state = 'submitted' AND seq > ? AND seq <= ? ORDER BY seq LIMIT ?",
    limit,
  );
}

export async function reconcile(env, settings, trigger) {
  const db = env.PRODUCT_DB;
  const at = now();
  const counts = { resent: 0, exhausted: 0, send_failed: 0, pulled: 0, completed: 0, failed: 0, rejected: 0, publications: 0 };
  const due = await db
    .prepare(
      `SELECT * FROM operations
       WHERE (state = 'admitted' AND next_send_at <= ?)
          OR (state = 'enqueued' AND enqueued_at <= ? AND next_send_at <= ?)
          OR (state = 'submitting' AND claim_expires_at < ? AND next_send_at <= ?)
       ORDER BY seq LIMIT ?`,
    )
    .bind(at, at - settings.ENQUEUED_STALE_MS, at, at, at, LIMITS.sweepBatch)
    .all();
  // Without an execution service nothing is sent or pulled; rows wait.
  for (const row of settings.executionConfigured ? due.results : []) {
    const outcome = await resend(env, settings, row, at);
    if (outcome in counts) counts[outcome] += 1;
  }
  const submitted = settings.executionConfigured ? await pullBatch(db, LIMITS.sweepBatch) : [];
  for (const row of submitted) {
    counts.pulled += 1;
    const outcome = await pullStatus(env, settings, row);
    if (outcome === "completed") counts.completed += 1;
    if (outcome === "failed") counts.failed += 1;
    if (outcome === "artifact_rejected") counts.rejected += 1;
  }
  counts.publications = settings.publisherConfigured ? await repairPublications(env, settings, LIMITS.sweepBatch) : 0;
  await record(db, { kind: "sweep", token: trigger, detail: counts, at: now() });
  return counts;
}

// Admit each active schedule's staged bundle once, through the shared path.
export async function scheduledAdmission(env, settings) {
  const db = env.PRODUCT_DB;
  const at = now();
  const { results } = await db
    .prepare(
      `SELECT * FROM schedules WHERE state = 'active' AND pending_bundle_sha256 IS NOT NULL
         AND (last_admitted_fingerprint IS NULL OR last_admitted_fingerprint <> pending_bundle_sha256)
       ORDER BY schedule_id LIMIT ?`,
    )
    .bind(LIMITS.sweepBatch)
    .all();
  let admitted = 0;
  for (const schedule of results) {
    const fingerprint = schedule.pending_bundle_sha256;
    const object = await env.ARTIFACTS.get(`snapshots/${fingerprint}`);
    const bytes = object === null ? null : new Uint8Array(await object.arrayBuffer());
    if (bytes === null || (await sha256Hex(bytes)) !== fingerprint) {
      await record(db, { subject: schedule.schedule_id, kind: "schedule_bundle_unavailable", at });
      continue;
    }
    const { articles } = await parseBundle(bytes);
    const outcome = await admit(env, settings, {
      principal: "scheduler",
      pipeline: schedule.pipeline,
      policyId: schedule.policy_id,
      sourceRevision: `schedule:${schedule.schedule_id}:${fingerprint}`,
      articles,
      bytes,
      fingerprint,
    });
    if (outcome.status === 201 || outcome.status === 200) {
      await db
        .prepare(
          `UPDATE schedules SET last_admitted_fingerprint = ?, last_fired_at = ?, updated_at = ?
           WHERE schedule_id = ? AND pending_bundle_sha256 = ?`,
        )
        .bind(fingerprint, at, at, schedule.schedule_id, fingerprint)
        .run();
      if (outcome.status === 201) admitted += 1;
    }
    await record(db, { subject: schedule.schedule_id, kind: "schedule_fired", token: String(outcome.status), at });
  }
  return admitted;
}

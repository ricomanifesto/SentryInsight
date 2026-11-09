// Queue delivery: sending, the consumer's durable claim, the dead-letter
// disposition and the bounded manual retry.
//
// Retry owners: the sweeper re-sends rows whose send was never confirmed, the
// Queue retries enqueued messages, the execution service owns execution. The
// consumer calls the execution service only after winning a durable claim;
// only the current claim may record the outcome. A claim that expires does not
// prove the old call stopped, so admission at the execution service is
// idempotent per operation and binding, and a late caller's write is fenced
// by its claim token.

import { LIMITS } from "./config.js";
import { now, operation, record, rowsChanged } from "./db.js";
import { fault } from "./faults.js";
import { HEX64 } from "./identity.js";
import { submitExecution } from "./execution-client.js";
import { backoff } from "./timing.js";
import { randomToken, sha256Hex } from "./util.js";

const SETTLED = new Set(["submitted", "completed", "failed", "dead_letter"]);

// Send one delivery for the row's current generation and, if it was admitted,
// record that the send was confirmed. A failed send leaves the row for the
// sweeper. Returns true when the message was handed to the Queue.
export async function sendDelivery(env, row) {
  const db = env.PRODUCT_DB;
  try {
    await fault(env, "queue_send");
    await env.ADMISSIONS.send({ operation_id: row.operation_id, generation: row.delivery_generation });
  } catch (error) {
    await record(db, { operationId: row.operation_id, kind: "send_failed", token: "queue_send", at: now() });
    return false;
  }
  await fault(env, "after_send_before_enqueued");
  if (row.state === "admitted") {
    await db
      .prepare(
        `UPDATE operations SET state = 'enqueued', enqueued_at = ?, version = version + 1, updated_at = ?
         WHERE operation_id = ? AND state = 'admitted' AND version = ? AND delivery_generation = ?`,
      )
      .bind(now(), now(), row.operation_id, row.version, row.delivery_generation)
      .run();
  }
  return true;
}

function parseMessage(body) {
  if (
    body === null ||
    typeof body !== "object" ||
    Object.keys(body).sort().join(",") !== "generation,operation_id" ||
    typeof body.operation_id !== "string" ||
    !HEX64.test(body.operation_id) ||
    !Number.isInteger(body.generation) ||
    body.generation < 1
  ) {
    return null;
  }
  return body;
}

async function settleClaim(db, operationId, token, assignments, values, kind, tokenValue) {
  const at = now();
  const result = await db
    .prepare(
      `UPDATE operations SET ${assignments}, claim_token = NULL, claim_expires_at = NULL,
         version = version + 1, updated_at = ?
       WHERE operation_id = ? AND state = 'submitting' AND claim_token = ? RETURNING operation_id`,
    )
    .bind(...values, at, operationId, token)
    .run();
  const won = rowsChanged(result) === 1;
  await record(db, { operationId, kind: won ? kind : "settle_lost", token: tokenValue, at });
  return won;
}

// Returns "ack" or {retry: seconds}.
export async function handleDelivery(env, settings, body) {
  const db = env.PRODUCT_DB;
  if (!settings.executionConfigured) return { retry: settings.QUEUE_RETRY_DELAY_S };
  const message = parseMessage(body);
  if (message === null) return "ack";
  const row = await operation(db, message.operation_id);
  if (row === null) return "ack";
  if (message.generation !== row.delivery_generation) {
    await record(db, { operationId: row.operation_id, kind: "stale_delivery", detail: { generation: message.generation }, at: now() });
    return "ack";
  }
  if (SETTLED.has(row.state)) {
    await record(db, { operationId: row.operation_id, kind: "duplicate_delivery", token: row.state, at: now() });
    return "ack";
  }

  const token = randomToken();
  const at = now();
  const claim = await db
    .prepare(
      `UPDATE operations SET state = 'submitting', claim_token = ?, claim_expires_at = ?,
         version = version + 1, updated_at = ?
       WHERE operation_id = ? AND delivery_generation = ?
         AND (state IN ('admitted', 'enqueued') OR (state = 'submitting' AND claim_expires_at < ?)) RETURNING operation_id`,
    )
    .bind(token, at + settings.claimMs, at, row.operation_id, message.generation, at)
    .run();
  if (rowsChanged(claim) !== 1) {
    await record(db, { operationId: row.operation_id, kind: "claim_lost", at: now() });
    return "ack";
  }

  const object = await env.ARTIFACTS.get(`snapshots/${row.fingerprint}`);
  const bytes = object === null ? null : new Uint8Array(await object.arrayBuffer());
  if (bytes === null || (await sha256Hex(bytes)) !== row.fingerprint) {
    await settleClaim(db, row.operation_id, token, "state = 'failed', reason = ?", ["snapshot_unavailable"], "failed", "snapshot_unavailable");
    return "ack";
  }

  const outcome = await submitExecution(env, settings, row, bytes);
  if (outcome.kind === "accepted") {
    await fault(env, "after_accept_before_submitted");
    await fault(env, "delay_before_submitted");
    await settleClaim(
      db,
      row.operation_id,
      token,
      "state = 'submitted', execution_id = ?, run_id = ?, run_state = ?",
      [outcome.executionId, outcome.runId, outcome.state],
      "submitted",
      null,
    );
    return "ack";
  }
  if (outcome.kind === "refused") {
    await settleClaim(db, row.operation_id, token, "state = 'failed', reason = ?", [outcome.reason], "failed", outcome.reason);
    return "ack";
  }
  // Transient: give the claim back for this generation and let the Queue retry.
  await db
    .prepare(
      `UPDATE operations SET state = 'enqueued', claim_token = NULL, claim_expires_at = NULL,
         version = version + 1, updated_at = ?
       WHERE operation_id = ? AND state = 'submitting' AND claim_token = ?`,
    )
    .bind(now(), row.operation_id, token)
    .run();
  await record(db, { operationId: row.operation_id, kind: "execution_transient", token: outcome.reason, at: now() });
  return { retry: settings.QUEUE_RETRY_DELAY_S };
}

export async function handleDeadLetter(env, settings, body) {
  const db = env.PRODUCT_DB;
  const message = parseMessage(body);
  if (message === null) return;
  const at = now();
  const result = await db
    .prepare(
      `UPDATE operations SET state = 'dead_letter', reason = 'delivery_exhausted', claim_token = NULL,
         claim_expires_at = NULL, version = version + 1, updated_at = ?
       WHERE operation_id = ? AND delivery_generation = ?
         AND (state IN ('admitted', 'enqueued') OR (state = 'submitting' AND claim_expires_at < ?)) RETURNING operation_id`,
    )
    .bind(at, message.operation_id, message.generation, at)
    .run();
  const applied = rowsChanged(result) === 1;
  await record(db, {
    operationId: message.operation_id,
    kind: applied ? "dead_letter" : "stale_dead_letter",
    token: applied ? "delivery_exhausted" : null,
    detail: { generation: message.generation },
    at,
  });
}

export async function consume(batch, env, settings, handler) {
  for (const message of batch.messages) {
    try {
      const outcome = await handler(env, settings, message.body);
      if (outcome && outcome.retry !== undefined) message.retry({ delaySeconds: outcome.retry });
      else message.ack();
    } catch {
      message.retry({ delaySeconds: settings.QUEUE_RETRY_DELAY_S });
    }
  }
}

// Manual recovery from dead_letter: a new delivery generation, at most
// LIMITS.maxRetryRounds rounds. Messages of earlier generations become stale.
export async function manualRetry(env, settings, operationId) {
  const db = env.PRODUCT_DB;
  const row = await operation(db, operationId);
  if (row === null) return { status: 404, body: { error: "not_found" } };
  if (row.state !== "dead_letter") return { status: 409, body: { error: "not_dead_letter" } };
  if (!settings.executionConfigured) return { status: 503, body: { error: "execution_unconfigured" } };
  if (row.retry_rounds >= LIMITS.maxRetryRounds) return { status: 409, body: { error: "retry_exhausted" } };
  const at = now();
  const update = await db
    .prepare(
      `UPDATE operations SET state = 'admitted', delivery_generation = delivery_generation + 1,
         retry_rounds = retry_rounds + 1, send_attempts = 1, next_send_at = ?, reason = NULL,
         enqueued_at = NULL, version = version + 1, updated_at = ?
       WHERE operation_id = ? AND state = 'dead_letter' AND version = ? AND retry_rounds < ? RETURNING operation_id`,
    )
    .bind(at + backoff(settings, 1), at, operationId, row.version, LIMITS.maxRetryRounds)
    .run();
  if (rowsChanged(update) !== 1) return { status: 409, body: { error: "retry_conflict" } };
  await record(db, { operationId, kind: "manual_retry", detail: { generation: row.delivery_generation + 1 }, at });
  await sendDelivery(env, await operation(db, operationId));
  return { status: 202, operation: await operation(db, operationId) };
}

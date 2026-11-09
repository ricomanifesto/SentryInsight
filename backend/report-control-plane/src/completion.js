// Completion by pull: read the execution receipt for a submitted operation,
// project its status, and complete only after every artifact part has been
// fetched, hashed and stored immutably. The operation update and the artifact
// row are one batch, and the row is written only if the update applied.

import { LIMITS, SCHEMAS } from "./config.js";
import { now, record, rowsChanged } from "./db.js";
import { fault } from "./faults.js";
import { HEX64, ID_TOKEN, REASON, artifactDigest, comparePaths, pathSegments } from "./identity.js";
import { fetchPart, readExecution } from "./execution-client.js";
import { putImmutable, SnapshotConflict } from "./admission.js";
import { randomToken, sha256Hex, utf8 } from "./util.js";

const STATES = new Set(["queued", "running", "waiting_retry", "succeeded", "failed", "unknown"]);

export class Rejected extends Error {
  constructor(token) {
    super(token);
    this.token = token;
  }
}

function keys(value, expected) {
  return (
    value !== null &&
    typeof value === "object" &&
    !Array.isArray(value) &&
    Object.keys(value).sort().join(",") === [...expected].sort().join(",")
  );
}

const count = (v) => Number.isInteger(v) && v >= 0;

// Structural validation; returns a reason token or null.
export function receiptProblem(r) {
  if (!keys(r, ["schema", "operation_id", "execution_id", "binding_id", "state", "reason", "attempts", "budget", "articles", "artifact"])) {
    return "receipt_invalid";
  }
  if (
    r.schema !== SCHEMAS.receipt ||
    !HEX64.test(r.operation_id ?? "") ||
    typeof r.execution_id !== "string" ||
    !ID_TOKEN.test(r.execution_id) ||
    !HEX64.test(r.binding_id ?? "") ||
    !STATES.has(r.state) ||
    !(r.reason === null || (typeof r.reason === "string" && REASON.test(r.reason))) ||
    !keys(r.attempts, ["used", "limit"]) ||
    !count(r.attempts.used) ||
    !count(r.attempts.limit) ||
    !keys(r.budget, ["reserved", "limit"]) ||
    !(r.budget.reserved === null || count(r.budget.reserved)) ||
    !count(r.budget.limit) ||
    !keys(r.articles, ["admitted_count", "executed"]) ||
    !count(r.articles.admitted_count) ||
    !Array.isArray(r.articles.executed) ||
    r.articles.executed.length > LIMITS.articles ||
    !r.articles.executed.every(
      (a) => keys(a, ["article_key", "content_sha256"]) && typeof a.article_key === "string" && HEX64.test(a.content_sha256 ?? ""),
    )
  ) {
    return "receipt_invalid";
  }
  if (r.artifact !== null && !keys(r.artifact, ["accepted_output_sha256", "sha256", "file_count", "total_bytes", "files"])) {
    return "receipt_invalid";
  }
  return null;
}

export async function checkArtifact(artifact) {
  const { files } = artifact;
  if (!HEX64.test(artifact.sha256 ?? "") || !HEX64.test(artifact.accepted_output_sha256 ?? "")) throw new Rejected("artifact_receipt_invalid");
  if (artifact.accepted_output_sha256 !== artifact.sha256) throw new Rejected("artifact_accepted_mismatch");
  if (!Array.isArray(files) || files.length === 0 || files.length > LIMITS.artifactFiles) throw new Rejected("artifact_count_mismatch");
  if (!count(artifact.file_count) || artifact.file_count !== files.length) throw new Rejected("artifact_count_mismatch");
  let total = 0;
  const seen = new Set();
  for (const [i, file] of files.entries()) {
    if (!keys(file, ["path", "sha256", "bytes"]) || !HEX64.test(file.sha256 ?? "") || !count(file.bytes)) {
      throw new Rejected("artifact_receipt_invalid");
    }
    if (pathSegments(file.path) === null) throw new Rejected("artifact_path_invalid");
    if (seen.has(file.path)) throw new Rejected("artifact_path_duplicate");
    seen.add(file.path);
    if (i > 0 && comparePaths(files[i - 1].path, file.path) >= 0) throw new Rejected("artifact_order_invalid");
    if (file.bytes > LIMITS.artifactFileBytes) throw new Rejected("artifact_size_mismatch");
    total += file.bytes;
  }
  if (total > LIMITS.artifactTotalBytes || !count(artifact.total_bytes) || artifact.total_bytes !== total) {
    throw new Rejected("artifact_size_mismatch");
  }
  if ((await artifactDigest(files)) !== artifact.sha256) throw new Rejected("artifact_digest_mismatch");
}

async function checkArticles(db, row, articles) {
  const { results } = await db
    .prepare("SELECT article_key, content_sha256 FROM operation_articles WHERE operation_id = ?")
    .bind(row.operation_id)
    .all();
  if (articles.admitted_count !== results.length) throw new Rejected("artifact_articles_invalid");
  const admitted = new Set(results.map((a) => `${a.article_key}\n${a.content_sha256}`));
  const executed = new Set();
  for (const a of articles.executed) {
    const key = `${a.article_key}\n${a.content_sha256}`;
    if (!admitted.has(key) || executed.has(a.article_key)) throw new Rejected("artifact_articles_invalid");
    executed.add(a.article_key);
  }
  if (executed.size === 0) throw new Rejected("artifact_articles_invalid");
  return executed.size;
}

export function manifestBytes(artifact) {
  return utf8(
    JSON.stringify({
      schema: SCHEMAS.manifest,
      artifact_sha256: artifact.sha256,
      file_count: artifact.file_count,
      total_bytes: artifact.total_bytes,
      files: artifact.files.map((f) => ({ path: f.path, sha256: f.sha256, bytes: f.bytes })),
    }),
  );
}

// Terminal failure of a submitted operation; the execution run is untouched.
async function fail(db, row, reason, kind, token) {
  const at = now();
  const result = await db
    .prepare(
      `UPDATE operations SET state = 'failed', reason = ?, version = version + 1, updated_at = ?
       WHERE operation_id = ? AND state = 'submitted' AND version = ? RETURNING operation_id`,
    )
    .bind(reason, at, row.operation_id, row.version)
    .run();
  const applied = rowsChanged(result) === 1;
  if (applied) await record(db, { operationId: row.operation_id, kind, token, at });
  return applied ? kind : "stale";
}

function reject(db, row, token) {
  return fail(db, row, "artifact_rejected", "artifact_rejected", token);
}

async function complete(env, settings, row, receipt) {
  const db = env.PRODUCT_DB;
  const artifact = receipt.artifact;
  let executedCount;
  const parts = [];
  try {
    executedCount = await checkArticles(db, row, receipt.articles);
    await checkArtifact(artifact);
    for (const file of artifact.files) {
      const part = await fetchPart(env, settings, row.operation_id, file.path, file.bytes + 1);
      if (part.kind === "transient") {
        await record(db, { operationId: row.operation_id, kind: "artifact_fetch_transient", at: now() });
        return "retry";
      }
      if (part.kind === "missing") throw new Rejected("artifact_part_missing");
      if (part.kind === "oversized" || part.bytes.byteLength !== file.bytes) throw new Rejected("artifact_size_mismatch");
      if ((await sha256Hex(part.bytes)) !== file.sha256) throw new Rejected("artifact_part_mismatch");
      parts.push({ file, bytes: part.bytes });
    }
    for (const { file, bytes } of parts) {
      await putImmutable(env.ARTIFACTS, `artifacts/${artifact.sha256}/files/${file.path}`, bytes, file.sha256);
    }
  } catch (error) {
    if (error instanceof Rejected) return reject(db, row, error.token);
    if (error instanceof SnapshotConflict) return reject(db, row, "artifact_object_conflict");
    throw error;
  }
  const manifest = manifestBytes(artifact);
  const manifestSha = await sha256Hex(manifest);
  try {
    await putImmutable(env.ARTIFACTS, `artifacts/${artifact.sha256}/manifest.json`, manifest, manifestSha);
  } catch (error) {
    if (error instanceof SnapshotConflict) return reject(db, row, "artifact_object_conflict");
    throw error;
  }
  await fault(env, "before_completion_batch");

  const at = now();
  // The nonce exists only if this caller's own update applied: a stale caller
  // that sees another caller's completed row writes neither the artifact row
  // nor a second completion event.
  const nonce = randomToken();
  const done = "operation_id = ? AND state = 'completed' AND transition_nonce = ?";
  const results = await db.batch([
    db
      .prepare(
        `UPDATE operations SET state = 'completed', artifact_sha256 = ?, executed_count = ?, run_state = 'succeeded',
           reason = NULL, transition_nonce = ?, version = version + 1, updated_at = ?
         WHERE operation_id = ? AND state = 'submitted' AND execution_id = ? AND binding_id = ? AND version = ?
         RETURNING operation_id`,
      )
      .bind(artifact.sha256, executedCount, nonce, at, row.operation_id, row.execution_id, row.binding_id, row.version),
    db
      .prepare(
        `INSERT INTO artifacts (artifact_sha256, first_operation_id, file_count, total_bytes, manifest_sha256, verified_at)
         SELECT ?, ?, ?, ?, ?, ? WHERE EXISTS (SELECT 1 FROM operations WHERE ${done})
         ON CONFLICT (artifact_sha256) DO NOTHING`,
      )
      .bind(artifact.sha256, row.operation_id, artifact.file_count, artifact.total_bytes, manifestSha, at, row.operation_id, nonce),
    db
      .prepare(
        `INSERT INTO events (operation_id, kind, token, detail, at)
         SELECT ?, 'completed', NULL, ?, ? WHERE EXISTS (SELECT 1 FROM operations WHERE ${done})`,
      )
      .bind(row.operation_id, JSON.stringify({ files: artifact.file_count, executed: executedCount }), at, row.operation_id, nonce),
    // Which admitted articles the execution side ran; the rest were excluded
    // by its policy. Written under the same nonce as the completion.
    db
      .prepare(
        `UPDATE operation_articles
           SET executed = CASE WHEN article_key IN (SELECT value FROM json_each(?)) THEN 1 ELSE 0 END
         WHERE operation_id = ? AND EXISTS (SELECT 1 FROM operations WHERE ${done})`,
      )
      .bind(JSON.stringify(receipt.articles.executed.map((a) => a.article_key)), row.operation_id, row.operation_id, nonce),
  ]);
  return rowsChanged(results[0]) === 1 ? "completed" : "stale";
}

async function project(db, row, receipt) {
  const values = [receipt.state, receipt.reason, receipt.attempts.used, receipt.attempts.limit, receipt.budget.reserved, receipt.budget.limit];
  const current = [row.run_state, row.run_reason, row.attempts_used, row.attempts_limit, row.budget_reserved, row.budget_limit];
  if (values.every((v, i) => v === current[i])) return row;
  const at = now();
  const result = await db
    .prepare(
      `UPDATE operations SET run_state = ?, run_reason = ?, attempts_used = ?, attempts_limit = ?,
         budget_reserved = ?, budget_limit = ?, version = version + 1, updated_at = ?
       WHERE operation_id = ? AND state = 'submitted' AND version = ? RETURNING operation_id`,
    )
    .bind(...values, at, row.operation_id, row.version)
    .run();
  if (rowsChanged(result) !== 1) return null;
  return { ...row, run_state: values[0], run_reason: values[1], version: row.version + 1 };
}

// One status pull for a submitted operation. Returns a fixed outcome token.
export async function pullStatus(env, settings, row) {
  const db = env.PRODUCT_DB;
  const read = await readExecution(env, settings, row.operation_id, row.fingerprint, row.binding_id);
  if (read.kind === "transient" || read.kind === "unknown") return read.kind;
  if (read.kind === "refused") return fail(db, row, read.reason, "failed", read.reason);
  if (read.kind === "malformed") return reject(db, row, "receipt_invalid");
  const receipt = read.receipt;
  const problem = receiptProblem(receipt);
  if (problem !== null) return reject(db, row, problem);
  if (receipt.operation_id !== row.operation_id || receipt.execution_id !== row.execution_id || receipt.binding_id !== row.binding_id) {
    return reject(db, row, "receipt_identity_mismatch");
  }
  const projected = await project(db, row, receipt);
  if (projected === null) return "stale";
  if (receipt.state === "failed") {
    const reason = receipt.reason ?? "execution_failed";
    return fail(db, projected, reason, "failed", reason);
  }
  if (receipt.state === "succeeded") {
    // The contract carries an artifact only once the execution side has
    // verified it, so success without one is contradictory, not pending.
    if (receipt.artifact === null) return reject(db, projected, "receipt_success_without_artifact");
    return complete(env, settings, projected, receipt);
  }
  return "pending";
}

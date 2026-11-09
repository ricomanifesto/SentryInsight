// Projection: recording runs that the authoritative producer already
// completed, so their history can be read and exported here.
//
// The producer (the report workflow) stays the authority for generation and
// publication. It uploads immutable bytes first (the run's admission-shaped
// source snapshot and its report files, each under its own SHA-256), then
// posts one projection naming them. The Worker re-verifies every byte, stores
// the snapshot and artifact immutably, and writes the run in one D1 batch. A
// repeated projection is the same operation; a reused source revision with
// other bytes is a recorded conflict. Nothing here generates or publishes.
//
// A deployment the producer's publisher completed is posted as an
// observation. It may arrive before or after its run; whichever is written
// second attaches the publication, and both writes are idempotent.

import { putImmutable, recordConflict, SnapshotConflict } from "./admission.js";
import { PROJECTION_LIMITS, SCHEMAS } from "./config.js";
import { checkArtifact, manifestBytes, Rejected } from "./completion.js";
import { event, isConstraintError, now, operation, rowsChanged } from "./db.js";
import { fault } from "./faults.js";
import { HEX64, ID_TOKEN, REASON, SOURCE_REVISION, TOKEN, artifactDigest, operationId as deriveOperationId, publicationId } from "./identity.js";
import { RequestRefused, parseAdmission, validPublishedAt } from "./request.js";
import { JsonRefused, decodeStrictJson } from "./strict-json.js";
import { sha256Hex } from "./util.js";

const COMMIT = /^[0-9a-f]{40}$/;
const OUTCOMES = new Set(["succeeded", "failed"]);

export class ProjectionRefused extends Error {
  constructor(status, reason) {
    super(reason);
    this.status = status;
    this.reason = reason;
  }
}

const refuse = (reason, status = 422) => {
  throw new ProjectionRefused(status, reason);
};

function exactKeys(value, keys) {
  if (value === null || typeof value !== "object" || Array.isArray(value)) refuse("projection_malformed");
  const present = Object.keys(value).sort().join(",");
  if (present !== [...keys].sort().join(",")) refuse("projection_malformed");
}

function decode(bytes, limit) {
  if (bytes.byteLength === 0 || bytes.byteLength > limit) refuse("projection_malformed");
  try {
    return decodeStrictJson(bytes);
  } catch (error) {
    if (error instanceof JsonRefused) refuse("projection_malformed");
    throw error;
  }
}

// Store one immutable blob under its own digest.
export async function putBlob(env, sha, bytes) {
  if ((await sha256Hex(bytes)) !== sha) return { status: 422, body: { error: "blob_digest_mismatch" } };
  try {
    const stored = await putImmutable(env.ARTIFACTS, `blobs/${sha}`, bytes, sha);
    return { status: stored === "created" ? 201 : 200, body: { sha256: sha, bytes: bytes.byteLength } };
  } catch (error) {
    if (error instanceof SnapshotConflict) return { status: 409, body: { error: "blob_conflict" } };
    throw error;
  }
}

async function readBlob(env, sha, expectedBytes = null) {
  const object = await env.ARTIFACTS.get(`blobs/${sha}`);
  if (object === null) refuse("blob_missing", 409);
  const bytes = new Uint8Array(await object.arrayBuffer());
  if ((await sha256Hex(bytes)) !== sha || (expectedBytes !== null && bytes.byteLength !== expectedBytes)) refuse("blob_mismatch", 409);
  return bytes;
}

export function parseProjection(bytes) {
  const value = decode(bytes, PROJECTION_LIMITS.projectionBytes);
  exactKeys(value, ["schema", "pipeline", "policy_id", "source_revision", "snapshot_sha256", "run", "artifact"]);
  if (value.schema !== SCHEMAS.projection) refuse("schema_unsupported");
  if (typeof value.pipeline !== "string" || !TOKEN.test(value.pipeline)) refuse("pipeline_invalid");
  if (typeof value.policy_id !== "string" || !TOKEN.test(value.policy_id)) refuse("policy_invalid");
  if (typeof value.source_revision !== "string" || !SOURCE_REVISION.test(value.source_revision) || value.source_revision.startsWith("schedule:")) {
    refuse("source_revision_invalid");
  }
  if (typeof value.snapshot_sha256 !== "string" || !HEX64.test(value.snapshot_sha256)) refuse("snapshot_invalid");
  const run = value.run;
  exactKeys(run, ["execution_id", "source_commit", "outcome", "reason", "executed_links", "completed_at"]);
  if (typeof run.execution_id !== "string" || !ID_TOKEN.test(run.execution_id)) refuse("run_invalid");
  if (!(run.source_commit === null || (typeof run.source_commit === "string" && COMMIT.test(run.source_commit)))) refuse("run_invalid");
  if (!OUTCOMES.has(run.outcome)) refuse("run_invalid");
  if (!(run.reason === null || (typeof run.reason === "string" && REASON.test(run.reason)))) refuse("run_invalid");
  if (!(run.completed_at === null || (typeof run.completed_at === "string" && validPublishedAt(run.completed_at)))) refuse("run_invalid");
  if (!(run.executed_links === null || (Array.isArray(run.executed_links) && run.executed_links.length <= PROJECTION_LIMITS.articles && run.executed_links.every((l) => typeof l === "string")))) {
    refuse("run_invalid");
  }
  if (run.outcome === "succeeded" && (value.artifact === null || run.reason !== null || run.source_commit === null)) refuse("run_inconsistent");
  if (run.outcome === "failed" && (value.artifact !== null || run.reason === null)) refuse("run_inconsistent");
  if (value.artifact !== null) {
    exactKeys(value.artifact, ["files"]);
    if (!Array.isArray(value.artifact.files)) refuse("artifact_invalid");
  }
  return value;
}

// The run as the producer reported it: the operation id, its terminal state
// and the verified artifact listing.
async function described(projection, files) {
  const fingerprint = projection.snapshot_sha256;
  const id = await deriveOperationId(projection.pipeline, projection.policy_id, fingerprint);
  if (files === null) return { id, fingerprint, artifact: null };
  const listing = files.map((f) => ({ path: f.path, sha256: f.sha256, bytes: f.bytes }));
  const digest = await artifactDigest(listing);
  const artifact = {
    accepted_output_sha256: digest,
    sha256: digest,
    file_count: listing.length,
    total_bytes: listing.reduce((n, f) => n + (Number.isInteger(f.bytes) ? f.bytes : 0), 0),
    files: listing,
  };
  try {
    await checkArtifact(artifact);
  } catch (error) {
    if (error instanceof Rejected) refuse(error.token);
    throw error;
  }
  return { id, fingerprint, artifact };
}

// A replay must repeat every recorded fact of the run: its state, identity,
// reason, artifact and per-article outcomes. Anything else is a conflict, never
// a silent acknowledgement of different history.
async function sameRun(db, existing, projection, artifact) {
  const succeeded = projection.run.outcome === "succeeded";
  if (
    existing.origin !== "project" ||
    existing.state !== (succeeded ? "completed" : "failed") ||
    existing.execution_id !== projection.run.execution_id ||
    existing.run_id !== projection.run.source_commit ||
    existing.reason !== projection.run.reason ||
    existing.artifact_sha256 !== (artifact?.sha256 ?? null) ||
    existing.source_revision !== projection.source_revision
  ) {
    return false;
  }
  const { results } = await db
    .prepare("SELECT article_key, executed FROM operation_articles WHERE operation_id = ?")
    .bind(existing.operation_id)
    .all();
  const links = projection.run.executed_links;
  const expected = !succeeded || links === null ? null : new Set(links);
  if (expected !== null && expected.size !== links.length) return false;
  if (expected !== null && [...expected].some((link) => !results.some((r) => r.article_key === link))) return false;
  return results.every((r) => r.executed === (expected === null ? null : expected.has(r.article_key) ? 1 : 0));
}

// Attach every recorded deployment observation of a projected run's commit.
async function attachObservations(db, op) {
  if (op.state !== "completed" || op.run_id === null) return 0;
  const { results } = await db
    .prepare("SELECT * FROM publication_observations WHERE pipeline = ? AND source_commit = ? ORDER BY target")
    .bind(op.pipeline, op.run_id)
    .all();
  let attached = 0;
  for (const observation of results) attached += await recordPublication(db, op, observation);
  return attached;
}

async function recordPublication(db, op, observation) {
  const id = await publicationId(observation.target, op.artifact_sha256);
  const at = now();
  const receipt = JSON.stringify({ authority: "observed", observed_at: observation.observed_at, source_commit: observation.source_commit });
  const [inserted] = await db.batch([
    db
      .prepare(
        `INSERT INTO publications (publication_id, target, artifact_sha256, operation_id, candidate_seq, state, receipt, created_at, updated_at)
         VALUES (?, ?, ?, ?, ?, 'published', ?, ?, ?) ON CONFLICT (publication_id) DO NOTHING RETURNING publication_id`,
      )
      .bind(id, observation.target, op.artifact_sha256, op.operation_id, op.seq, receipt, at, at),
    db
      .prepare(
        `INSERT INTO events (operation_id, subject, kind, token, detail, at)
         SELECT ?, ?, 'publication_observed', NULL, ?, ? WHERE changes() = 1`,
      )
      .bind(op.operation_id, id, JSON.stringify({ target: observation.target }), at),
  ]);
  return rowsChanged(inserted);
}

export async function project(env, principal, bytes) {
  const db = env.PRODUCT_DB;
  const projection = parseProjection(bytes);
  const binding = await db.prepare("SELECT * FROM pipelines WHERE pipeline = ?").bind(projection.pipeline).first();
  if (binding === null || binding.state !== "active") refuse("pipeline_unavailable");
  if (binding.mode !== "project") refuse("pipeline_not_projection");
  if (binding.policy_id !== projection.policy_id) refuse("policy_unsupported");

  const { id, fingerprint, artifact } = await described(projection, projection.artifact?.files ?? null);
  const existing = await operation(db, id);
  if (existing !== null) {
    if (!(await sameRun(db, existing, projection, artifact))) refuse("projection_conflict", 409);
    await attachObservations(db, existing);
    return { status: 200, operation: await operation(db, id) };
  }

  // Re-verify and parse the snapshot exactly as an admission, with the
  // projection's bounds; it must name the same pipeline, policy and revision.
  const snapshot = await readBlob(env, fingerprint);
  let parsed;
  try {
    parsed = await parseAdmission(snapshot, PROJECTION_LIMITS);
  } catch (error) {
    if (error instanceof RequestRefused) refuse(`snapshot_${error.reason}`.slice(0, 64));
    throw error;
  }
  if (parsed.pipeline !== projection.pipeline || parsed.policyId !== projection.policy_id || parsed.sourceRevision !== projection.source_revision) {
    refuse("snapshot_mismatch");
  }
  const keys = new Set(parsed.articles.map((a) => a.article_key));
  const executed = projection.run.executed_links === null ? null : new Set(projection.run.executed_links);
  if (executed !== null && (executed.size !== projection.run.executed_links.length || ![...executed].every((k) => keys.has(k)))) {
    refuse("executed_links_invalid");
  }

  // Immutable bytes first; an orphan is harmless and a retry reuses it.
  try {
    await putImmutable(env.ARTIFACTS, `snapshots/${fingerprint}`, snapshot, fingerprint);
    if (artifact !== null) {
      for (const file of artifact.files) {
        const part = await readBlob(env, file.sha256, file.bytes);
        await putImmutable(env.ARTIFACTS, `artifacts/${artifact.sha256}/files/${file.path}`, part, file.sha256);
      }
    }
  } catch (error) {
    if (error instanceof SnapshotConflict) refuse("object_conflict", 409);
    throw error;
  }
  let manifestSha = null;
  if (artifact !== null) {
    const manifest = manifestBytes(artifact);
    manifestSha = await sha256Hex(manifest);
    try {
      await putImmutable(env.ARTIFACTS, `artifacts/${artifact.sha256}/manifest.json`, manifest, manifestSha);
    } catch (error) {
      if (error instanceof SnapshotConflict) refuse("object_conflict", 409);
      throw error;
    }
  }

  await fault(env, "before_projection_batch");
  const at = now();
  const succeeded = projection.run.outcome === "succeeded";
  const statements = [
    db
      .prepare("INSERT INTO snapshots (fingerprint, bytes, created_at) VALUES (?, ?, ?) ON CONFLICT (fingerprint) DO NOTHING")
      .bind(fingerprint, snapshot.byteLength, at),
    db
      .prepare(
        `INSERT INTO operations (operation_id, pipeline, policy_id, binding_id, source_revision, fingerprint, principal, state,
           send_attempts, next_send_at, execution_id, run_id, run_state, run_reason, artifact_sha256, executed_count, reason,
           origin, created_at, updated_at)
         VALUES (?, ?, ?, ?, ?, ?, ?, ?, 0, 0, ?, ?, ?, ?, ?, ?, ?, 'project', ?, ?)`,
      )
      .bind(
        id, projection.pipeline, projection.policy_id, binding.binding_id, projection.source_revision, fingerprint, principal,
        succeeded ? "completed" : "failed", projection.run.execution_id, projection.run.source_commit,
        succeeded ? "succeeded" : "failed", projection.run.reason, artifact?.sha256 ?? null,
        executed === null ? null : executed.size, projection.run.reason, at, at,
      ),
  ];
  parsed.articles.forEach((article, position) => {
    statements.push(
      db
        .prepare(
          `INSERT INTO article_revisions (article_key, content_sha256, title, source, first_operation_id, created_at,
             content_kind, content_bytes, published_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?) ON CONFLICT (article_key, content_sha256) DO NOTHING`,
        )
        .bind(article.article_key, article.content_sha256, article.title, article.source, id, at,
          article.content_kind, article.content_bytes, article.published_at),
      db
        .prepare("INSERT INTO operation_articles (operation_id, position, article_key, content_sha256, executed) VALUES (?, ?, ?, ?, ?)")
        .bind(id, position, article.article_key, article.content_sha256, !succeeded || executed === null ? null : executed.has(article.article_key) ? 1 : 0),
    );
  });
  if (artifact !== null) {
    statements.push(
      db
        .prepare(
          `INSERT INTO artifacts (artifact_sha256, first_operation_id, file_count, total_bytes, manifest_sha256, verified_at)
           VALUES (?, ?, ?, ?, ?, ?) ON CONFLICT (artifact_sha256) DO NOTHING`,
        )
        .bind(artifact.sha256, id, artifact.file_count, artifact.total_bytes, manifestSha, at),
    );
  }
  statements.push(
    event(db, {
      operationId: id,
      kind: "projected",
      token: projection.run.outcome,
      detail: { articles: parsed.articles.length, executed: executed?.size ?? null, files: artifact?.file_count ?? 0 },
      at,
    }),
  );
  try {
    await db.batch(statements);
  } catch (error) {
    if (!isConstraintError(error)) throw error;
    const same = await operation(db, id);
    if (same !== null) {
      if (!(await sameRun(db, same, projection, artifact))) refuse("projection_conflict", 409);
      return { status: 200, operation: same };
    }
    const conflict = await db
      .prepare("SELECT operation_id FROM operations WHERE pipeline = ? AND source_revision = ?")
      .bind(projection.pipeline, projection.source_revision)
      .first();
    if (conflict !== null) {
      await recordConflict(db, { pipeline: projection.pipeline, sourceRevision: projection.source_revision, fingerprint, existing: conflict.operation_id });
      return { status: 409, body: { error: "source_revision_conflict", operation_id: conflict.operation_id } };
    }
    throw error;
  }
  const row = await operation(db, id);
  await attachObservations(db, row);
  return { status: 201, operation: await operation(db, id) };
}

export function parseObservation(bytes) {
  const value = decode(bytes, 4096);
  exactKeys(value, ["schema", "pipeline", "source_commit", "target", "observed_at"]);
  if (value.schema !== SCHEMAS.observation) refuse("schema_unsupported");
  if (typeof value.pipeline !== "string" || !TOKEN.test(value.pipeline)) refuse("pipeline_invalid");
  if (typeof value.source_commit !== "string" || !COMMIT.test(value.source_commit)) refuse("observation_invalid");
  if (typeof value.target !== "string" || !TOKEN.test(value.target)) refuse("observation_invalid");
  if (typeof value.observed_at !== "string" || !validPublishedAt(value.observed_at)) refuse("observation_invalid");
  return value;
}

// Record a deployment of a source commit and attach it to any projected run
// of that commit. The first observation of a (commit, target) pair is kept.
export async function observe(env, bytes) {
  const db = env.PRODUCT_DB;
  const observation = parseObservation(bytes);
  const binding = await db.prepare("SELECT * FROM pipelines WHERE pipeline = ?").bind(observation.pipeline).first();
  if (binding === null || binding.mode !== "project") refuse("pipeline_not_projection");
  await db
    .prepare(
      `INSERT INTO publication_observations (pipeline, source_commit, target, observed_at, recorded_at)
       VALUES (?, ?, ?, ?, ?) ON CONFLICT (pipeline, source_commit, target) DO NOTHING`,
    )
    .bind(observation.pipeline, observation.source_commit, observation.target, observation.observed_at, now())
    .run();
  const kept = await db
    .prepare("SELECT * FROM publication_observations WHERE pipeline = ? AND source_commit = ? AND target = ?")
    .bind(observation.pipeline, observation.source_commit, observation.target)
    .first();
  const { results: runs } = await db
    .prepare("SELECT * FROM operations WHERE pipeline = ? AND run_id = ? AND origin = 'project' AND state = 'completed' ORDER BY seq")
    .bind(observation.pipeline, observation.source_commit)
    .all();
  for (const op of runs) await recordPublication(db, op, kept);
  return { status: runs.length === 0 ? 202 : 200, body: { observed_at: kept.observed_at, runs: runs.map((r) => r.operation_id) } };
}

// The research export: a bounded, read-only change feed over product history
// for downstream consumers such as the newsletter. It never writes.
//
// The cursor is an export_changes id. Triggers write a change row in the same
// statement as every change a run record reflects (migration 0004), so a
// change can never be committed without advancing past the cursor. A page
// names each operation changed after the cursor and emits two kinds of record:
//
// - source_revision: one immutable admitted article revision. Its fields are
//   derived in commit order (rowid), so a replay yields identical records.
// - run: the exported state of one operation, read in one D1 batch (a single
//   transaction), so its fields and its record_version (the newest change id
//   for that operation) come from one committed state. Equal versions carry
//   equal content (record_sha256).
//
// A consumer upserts by record_id, ignores a record whose record_sha256 it
// already holds, and never replaces a run with a lower record_version.

import { SCHEMAS } from "./config.js";
import { HEX64 } from "./identity.js";
import { contentKind } from "./request.js";
import { JsonRefused, decodeStrictJson } from "./strict-json.js";
import { sha256Hex } from "./util.js";

export const EXPORT_LIMITS = Object.freeze({ defaultRuns: 10, maxRuns: 25, eventChunk: 200, maxEventsScanned: 2000, conflicts: 50 });
const MAX_CURSOR = Number.MAX_SAFE_INTEGER;
// SHA-256 of empty content; rows admitted before content_bytes existed are
// recognised as metadata-only by it.
const EMPTY_SHA256 = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855";

export class ExportRefused extends Error {
  constructor(reason) {
    super(reason);
    this.reason = reason;
  }
}

// ?after=<event id>&limit=<runs>; anything else is refused before any read.
export function parseExportQuery(search) {
  const params = new URLSearchParams(search);
  const seen = new Set();
  for (const key of params.keys()) {
    if (!["after", "limit"].includes(key) || seen.has(key)) throw new ExportRefused("export_query_invalid");
    seen.add(key);
  }
  const integer = (value, min, max, fallback) => {
    if (value === null) return fallback;
    if (!/^[0-9]{1,16}$/.test(value)) throw new ExportRefused("export_query_invalid");
    const n = Number(value);
    if (n < min || n > max) throw new ExportRefused("export_query_invalid");
    return n;
  };
  return {
    after: integer(params.get("after"), 0, MAX_CURSOR, 0),
    limit: integer(params.get("limit"), 1, EXPORT_LIMITS.maxRuns, EXPORT_LIMITS.defaultRuns),
  };
}

const iso = (ms) => (ms === null || ms === undefined ? null : new Date(ms).toISOString());

// The operations changed after the cursor, in change order. Returns the
// cursor of the last change accounted for.
export async function touchedOperations(db, after, limit, limits = EXPORT_LIMITS) {
  const operations = [];
  const seen = new Set();
  let cursor = after;
  let scanned = 0;
  for (;;) {
    const { results } = await db
      .prepare(
        "SELECT id, operation_id FROM export_changes WHERE id > ? ORDER BY id LIMIT ?",
      )
      .bind(cursor, limits.eventChunk)
      .all();
    for (const event of results) {
      const id = event.operation_id;
      if (id !== null && !seen.has(id)) {
        if (operations.length === limit) return { operations, cursor, hasMore: true };
        seen.add(id);
        operations.push(id);
      }
      cursor = event.id;
      scanned += 1;
    }
    if (results.length < limits.eventChunk) return { operations, cursor, hasMore: false };
    if (scanned >= limits.maxEventsScanned) return { operations, cursor, hasMore: true };
  }
}

export function sourceRecordId(articleKeySha, contentSha) {
  return `sentryinsight:source:${articleKeySha}:${contentSha}`;
}

const runRecordId = (operationId) => `sentryinsight:run:${operationId}`;

async function sealed(record) {
  return { ...record, record_sha256: await sha256Hex(JSON.stringify(record)) };
}

function evidenceKind(row) {
  if (row.content_bytes === 0 || (row.content_bytes === null && row.content_sha256 === EMPTY_SHA256)) return "metadata_only";
  if (row.content_kind === "article") return "full_text";
  if (row.content_kind === "feed") return "excerpt";
  return "unspecified";
}

// One operation's state, read in one batch so every part reflects one commit.
function runStatements(db, operationId) {
  return [
    db.prepare("SELECT * FROM operations WHERE operation_id = ?").bind(operationId),
    db.prepare("SELECT max(id) AS v FROM export_changes WHERE operation_id = ?").bind(operationId),
    // Each admitted article with its revision facts, all in commit order.
    db
      .prepare(
        `SELECT oa.position, oa.executed, r.article_key, r.content_sha256, r.title, r.source, r.content_kind,
           r.content_bytes, r.first_operation_id, r.created_at, r.published_at,
           (SELECT count(*) FROM article_revisions x WHERE x.article_key = r.article_key AND x.rowid < r.rowid) + 1 AS revision_index,
           (SELECT x.content_sha256 FROM article_revisions x WHERE x.article_key = r.article_key AND x.rowid < r.rowid
              ORDER BY x.rowid DESC LIMIT 1) AS previous_sha256,
           (SELECT x.article_key FROM article_revisions x WHERE x.content_sha256 = r.content_sha256
              ORDER BY x.rowid LIMIT 1) AS first_key,
           o.fingerprint AS retained_snapshot, f.position AS retained_position
         FROM operation_articles oa
           JOIN article_revisions r ON r.article_key = oa.article_key AND r.content_sha256 = oa.content_sha256
           LEFT JOIN operations o ON o.operation_id = r.first_operation_id
           LEFT JOIN operation_articles f ON f.operation_id = r.first_operation_id AND f.article_key = r.article_key
         WHERE oa.operation_id = ? ORDER BY oa.position`,
      )
      .bind(operationId),
    db
      .prepare("SELECT a.* FROM operations o JOIN artifacts a ON a.artifact_sha256 = o.artifact_sha256 WHERE o.operation_id = ?")
      .bind(operationId),
    // Which publication is a target's current last-good changes with another
    // operation's events, so it is not part of this record; a consumer orders
    // a target's published runs by admission_seq.
    db.prepare("SELECT * FROM publications WHERE operation_id = ? ORDER BY target").bind(operationId),
    db
      .prepare(
        `SELECT source_revision, refused_fingerprint, observed_at FROM identity_conflicts
         WHERE existing_operation_id = ? ORDER BY observed_at, refused_fingerprint LIMIT ?`,
      )
      .bind(operationId, EXPORT_LIMITS.conflicts),
  ];
}

async function sourceRecord(row) {
  const kind = evidenceKind(row);
  const keySha = await sha256Hex(row.article_key);
  return sealed({
    schema: SCHEMAS.export,
    record_type: "source_revision",
    record_id: sourceRecordId(keySha, row.content_sha256),
    product: "sentryinsight",
    canonical_url: row.article_key,
    article_key_sha256: keySha,
    publisher: row.source,
    title: row.title,
    content_sha256: row.content_sha256,
    revision: { index: row.revision_index, previous_content_sha256: row.previous_sha256 },
    evidence: {
      kind,
      content_kind: row.content_kind,
      content_bytes: row.content_bytes,
      retained:
        kind === "metadata_only" || row.retained_snapshot === null || row.retained_position === null
          ? null
          : {
              snapshot_sha256: row.retained_snapshot,
              position: row.retained_position,
              fetch: `/v1/export/sources/${row.retained_snapshot}/${row.retained_position}`,
            },
    },
    times: { published_at: row.published_at ?? null, captured_at: iso(row.created_at) },
    first_seen_run_id: runRecordId(row.first_operation_id),
    // Identical text under another URL is one source seen twice, not
    // corroboration. Metadata-only records carry no text to compare.
    independence:
      kind === "metadata_only"
        ? { status: "not_applicable", same_content_first_url: null }
        : row.first_key === row.article_key
          ? { status: "first_seen", same_content_first_url: null }
          : { status: "duplicate_content", same_content_first_url: row.first_key },
  });
}

const OUTCOMES = {
  admitted: "in_progress",
  enqueued: "in_progress",
  submitting: "in_progress",
  submitted: "in_progress",
  completed: "succeeded",
  failed: "failed",
  dead_letter: "incomplete",
};

// Every exported publication state is entered together with an audit event.
// A bare intent has none and is not exported until it is claimed. A
// superseded publication's effect was never observed, so it stays uncertain.
const PUBLICATION_STATES = {
  claimed: "pending",
  unresolved: "uncertain",
  superseded: "uncertain",
  published: "published",
  refused: "refused",
  conflict: "refused_by_publisher",
};
const PUBLICATION_REASONS = new Set(["refused", "conflict"]);

// A projected publication carries the time its deployment was observed; a
// publication made through the publisher carries none.
function observedAt(p) {
  if (p.state !== "published" || !p.receipt) return null;
  const receipt = JSON.parse(p.receipt);
  return receipt.authority === "observed" && typeof receipt.observed_at === "string" ? receipt.observed_at : null;
}

function runRecord(op, version, articles, artifact, publications, conflicts, sourceIds) {
  const outcome = OUTCOMES[op.state];
  const terminal = outcome === "succeeded" || outcome === "failed";
  const exported = publications
    .filter((p) => p.state in PUBLICATION_STATES)
    .map((p) => ({
      target: p.target,
      publication_id: p.publication_id,
      state: PUBLICATION_STATES[p.state],
      reason: PUBLICATION_REASONS.has(p.state) ? p.reason : null,
      observed_at: observedAt(p),
    }));
  return sealed({
    schema: SCHEMAS.export,
    record_type: "run",
    record_id: runRecordId(op.operation_id),
    record_version: version ?? 0,
    product: "sentryinsight",
    pipeline: op.pipeline,
    policy_id: op.policy_id,
    run: {
      operation_id: op.operation_id,
      origin: op.origin,
      source_commit: op.origin === "project" ? op.run_id : null,
      admission_seq: op.seq,
      source_revision: op.source_revision,
      snapshot_sha256: op.fingerprint,
      admitted_at: iso(op.created_at),
      outcome,
      reason: outcome === "in_progress" ? null : op.reason,
      execution:
        op.execution_id === null
          ? null
          : {
              execution_id: op.execution_id,
              run_id: op.run_id,
              run_state: terminal ? op.run_state : null,
              run_reason: terminal ? op.run_reason : null,
              attempts: terminal && op.attempts_used !== null ? { used: op.attempts_used, limit: op.attempts_limit } : null,
            },
    },
    sources: articles.map((a, i) => ({
      source_record_id: sourceIds[i],
      position: a.position,
      outcome: outcome !== "succeeded" ? "not_reported" : a.executed === 1 ? "executed" : a.executed === 0 ? "excluded" : "not_reported",
    })),
    artifact:
      artifact === undefined
        ? null
        : {
            sha256: artifact.artifact_sha256,
            manifest_sha256: artifact.manifest_sha256,
            file_count: artifact.file_count,
            total_bytes: artifact.total_bytes,
            verified_at: iso(artifact.verified_at),
          },
    publications: exported,
    report_published: exported.some((p) => p.state === "published"),
    identity_conflicts: conflicts.map((c) => ({
      source_revision: c.source_revision,
      refused_snapshot_sha256: c.refused_fingerprint,
      observed_at: iso(c.observed_at),
    })),
    // Generated findings live inside the report artifact, which this store
    // verifies by digest but does not interpret.
    derived_claims: { status: "not_exported", reason: "artifact_not_interpreted" },
  });
}

export async function exportPage(db, { after, limit }, limits = EXPORT_LIMITS) {
  const { operations, cursor, hasMore } = await touchedOperations(db, after, limit, limits);
  const records = [];
  const emitted = new Map();
  for (const operationId of operations) {
    const [op, version, articles, artifact, publications, conflicts] = (await db.batch(runStatements(db, operationId))).map((r) => r.results);
    if (op.length === 0) continue;
    const sourceIds = [];
    for (const row of articles) {
      const cacheKey = `${row.article_key}\n${row.content_sha256}`;
      if (!emitted.has(cacheKey)) {
        const record = await sourceRecord(row);
        emitted.set(cacheKey, record.record_id);
        records.push(record);
      }
      sourceIds.push(emitted.get(cacheKey));
    }
    records.push(await runRecord(op[0], version[0]?.v, articles, artifact[0], publications, conflicts, sourceIds));
  }
  const earliest = await db.prepare("SELECT created_at FROM operations ORDER BY seq LIMIT 1").first();
  const until = iso(earliest?.created_at);
  return {
    schema: SCHEMAS.exportPage,
    product: "sentryinsight",
    after,
    next_cursor: cursor,
    has_more: hasMore,
    coverage: {
      earliest_admitted_at: until,
      gaps: [{ kind: "before_first_admission", until, detail: "history before this store's first admission is not captured" }],
    },
    records,
  };
}

// One retained article from an admitted snapshot, or from the refused bytes of
// a recorded identity conflict, re-verified against its digest. Returns
// {status, body}.
export async function retainedSource(env, snapshot, position) {
  if (!HEX64.test(snapshot) || !Number.isInteger(position) || position < 0) return { status: 404, body: { error: "not_found" } };
  const known = await env.PRODUCT_DB
    .prepare(
      `SELECT 1 AS known FROM snapshots WHERE fingerprint = ?
       UNION ALL SELECT 1 FROM identity_conflicts WHERE refused_fingerprint = ? LIMIT 1`,
    )
    .bind(snapshot, snapshot)
    .first();
  if (known === null) return { status: 404, body: { error: "not_found" } };
  const object = await env.ARTIFACTS.get(`snapshots/${snapshot}`);
  if (object === null) return { status: 404, body: { error: "retained_content_unavailable" } };
  const bytes = new Uint8Array(await object.arrayBuffer());
  if ((await sha256Hex(bytes)) !== snapshot) return { status: 409, body: { error: "retained_content_mismatch" } };
  let value;
  try {
    value = decodeStrictJson(bytes);
  } catch (error) {
    if (error instanceof JsonRefused) return { status: 409, body: { error: "retained_content_malformed" } };
    throw error;
  }
  const record = Array.isArray(value?.articles) ? value.articles[position] : undefined;
  if (record === undefined) return { status: 404, body: { error: "not_found" } };
  if (record === null || typeof record !== "object" || typeof record.content !== "string" || typeof record.link !== "string") {
    return { status: 409, body: { error: "retained_content_malformed" } };
  }
  return {
    status: 200,
    body: {
      schema: SCHEMAS.exportSource,
      snapshot_sha256: snapshot,
      position,
      canonical_url: record.link,
      content_sha256: await sha256Hex(record.content),
      content_kind: contentKind(record.content_kind),
      content: record.content,
    },
  };
}

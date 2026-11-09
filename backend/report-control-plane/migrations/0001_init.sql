-- Product authority for the report control plane.
--
-- Every state change is a conditional UPDATE on a version, a delivery
-- generation or an owner token, and a writer that observes zero changed rows
-- performs no external action. Times are Unix epoch milliseconds.

CREATE TABLE pipelines (
  pipeline TEXT PRIMARY KEY,
  policy_id TEXT NOT NULL,
  binding_id TEXT NOT NULL CHECK (length(binding_id) = 64),
  state TEXT NOT NULL CHECK (state IN ('active', 'retired')),
  updated_at INTEGER NOT NULL
);

CREATE TABLE snapshots (
  fingerprint TEXT PRIMARY KEY CHECK (length(fingerprint) = 64),
  bytes INTEGER NOT NULL,
  created_at INTEGER NOT NULL
);

-- seq is the admission order and the only order used for staleness;
-- operation_id is the identity; (pipeline, source_revision) detects reuse.
CREATE TABLE operations (
  seq INTEGER PRIMARY KEY AUTOINCREMENT,
  operation_id TEXT NOT NULL UNIQUE CHECK (length(operation_id) = 64),
  pipeline TEXT NOT NULL,
  policy_id TEXT NOT NULL,
  binding_id TEXT NOT NULL,
  source_revision TEXT NOT NULL,
  fingerprint TEXT NOT NULL,
  principal TEXT NOT NULL,
  state TEXT NOT NULL CHECK (state IN (
    'admitted', 'enqueued', 'submitting', 'submitted', 'completed', 'failed', 'dead_letter'
  )),
  version INTEGER NOT NULL DEFAULT 1,
  delivery_generation INTEGER NOT NULL DEFAULT 1,
  retry_rounds INTEGER NOT NULL DEFAULT 0,
  send_attempts INTEGER NOT NULL DEFAULT 0,
  next_send_at INTEGER NOT NULL,
  enqueued_at INTEGER,
  claim_token TEXT,
  claim_expires_at INTEGER,
  execution_id TEXT,
  run_id TEXT,
  run_state TEXT,
  run_reason TEXT,
  attempts_used INTEGER,
  attempts_limit INTEGER,
  budget_reserved INTEGER,
  budget_limit INTEGER,
  artifact_sha256 TEXT,
  executed_count INTEGER,
  reason TEXT,
  created_at INTEGER NOT NULL,
  updated_at INTEGER NOT NULL,
  UNIQUE (pipeline, source_revision)
);

CREATE INDEX operations_by_state ON operations (state, next_send_at);

-- Immutable article revisions: a changed content is a new row, never an update.
CREATE TABLE article_revisions (
  article_key TEXT NOT NULL,
  content_sha256 TEXT NOT NULL CHECK (length(content_sha256) = 64),
  title TEXT NOT NULL,
  source TEXT,
  first_operation_id TEXT NOT NULL,
  created_at INTEGER NOT NULL,
  PRIMARY KEY (article_key, content_sha256)
);

CREATE TABLE operation_articles (
  operation_id TEXT NOT NULL,
  position INTEGER NOT NULL,
  article_key TEXT NOT NULL,
  content_sha256 TEXT NOT NULL,
  PRIMARY KEY (operation_id, position),
  UNIQUE (operation_id, article_key)
);

CREATE INDEX operation_articles_by_key ON operation_articles (article_key, content_sha256);

CREATE TABLE artifacts (
  artifact_sha256 TEXT PRIMARY KEY CHECK (length(artifact_sha256) = 64),
  first_operation_id TEXT NOT NULL,
  file_count INTEGER NOT NULL,
  total_bytes INTEGER NOT NULL,
  manifest_sha256 TEXT NOT NULL,
  verified_at INTEGER NOT NULL
);

CREATE TABLE publications (
  publication_id TEXT PRIMARY KEY CHECK (length(publication_id) = 64),
  target TEXT NOT NULL,
  artifact_sha256 TEXT NOT NULL,
  operation_id TEXT NOT NULL,
  candidate_seq INTEGER NOT NULL,
  state TEXT NOT NULL CHECK (state IN (
    'intent', 'claimed', 'unresolved', 'published', 'conflict', 'refused', 'superseded'
  )),
  claim_token TEXT,
  attempts INTEGER NOT NULL DEFAULT 0,
  receipt TEXT,
  reason TEXT,
  created_at INTEGER NOT NULL,
  updated_at INTEGER NOT NULL
);

-- The target names its active publication and its last-good revision.
-- coupling_nonce is a fresh value written by each coupled target update (a
-- settlement or a release); the publication update in the same batch
-- requires it, so it applies exactly when the target update did.
CREATE TABLE targets (
  target TEXT PRIMARY KEY,
  last_good_artifact TEXT,
  last_good_operation TEXT,
  last_good_seq INTEGER NOT NULL DEFAULT 0,
  last_good_publication_id TEXT,
  remote_version INTEGER NOT NULL DEFAULT 0,
  active_publication_id TEXT,
  claim_token TEXT,
  claim_expires_at INTEGER,
  coupling_nonce TEXT,
  updated_at INTEGER NOT NULL
);

CREATE TABLE schedules (
  schedule_id TEXT PRIMARY KEY,
  pipeline TEXT NOT NULL,
  policy_id TEXT NOT NULL,
  state TEXT NOT NULL CHECK (state IN ('active', 'paused')),
  pending_bundle_sha256 TEXT,
  last_admitted_fingerprint TEXT,
  last_fired_at INTEGER,
  updated_at INTEGER NOT NULL
);

-- Append-only audit of fixed tokens; detail is a small JSON of ids and counts.
CREATE TABLE events (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  operation_id TEXT,
  subject TEXT,
  kind TEXT NOT NULL,
  token TEXT,
  detail TEXT,
  at INTEGER NOT NULL
);

CREATE INDEX events_by_operation ON events (operation_id, id);

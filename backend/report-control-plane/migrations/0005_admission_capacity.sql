-- Reservations precede R2 writes and are never automatically released. They
-- bound new execute admissions, including conflicts and interrupted attempts.
-- Existing data is preserved even when its conservative total exceeds a cap.
CREATE TABLE admission_snapshots (
  fingerprint TEXT PRIMARY KEY CHECK (length(fingerprint) = 64),
  bytes INTEGER NOT NULL CHECK (bytes >= 0),
  principal TEXT,
  created_at INTEGER NOT NULL
);
CREATE TABLE admission_reservations (
  operation_id TEXT PRIMARY KEY,
  pipeline TEXT NOT NULL,
  source_revision TEXT,
  fingerprint TEXT NOT NULL CHECK (length(fingerprint) = 64),
  principal TEXT,
  state TEXT NOT NULL CHECK (state IN ('reserved', 'admitted', 'identity_conflict')),
  created_at INTEGER NOT NULL
);

INSERT INTO admission_reservations (operation_id, pipeline, source_revision, fingerprint, principal, state, created_at)
  SELECT operation_id, pipeline, source_revision, fingerprint, principal, 'admitted', created_at FROM operations WHERE origin = 'execute';
-- A legacy refused identity has no operation id of its own. Its stable local
-- reservation key cannot collide with a new SHA-256 operation identity.
INSERT INTO admission_reservations (operation_id, pipeline, source_revision, fingerprint, state, created_at)
  SELECT 'legacy-conflict:' || c.rowid, c.pipeline, c.source_revision, c.refused_fingerprint, 'identity_conflict', c.observed_at
  FROM identity_conflicts c JOIN operations o ON o.operation_id = c.existing_operation_id WHERE o.origin = 'execute';

INSERT INTO admission_snapshots (fingerprint, bytes, created_at)
  SELECT s.fingerprint, s.bytes, s.created_at FROM snapshots s
  WHERE EXISTS (SELECT 1 FROM admission_reservations r WHERE r.fingerprint = s.fingerprint)
     OR EXISTS (SELECT 1 FROM schedules q WHERE q.pending_bundle_sha256 = s.fingerprint);
-- Conflicts and staged bundles did not keep their byte lengths. Charge the
-- full 1 MiB execute-request limit rather than undercounting their objects.
INSERT INTO admission_snapshots (fingerprint, bytes, created_at)
  SELECT fingerprint, 1048576, min(created_at) FROM admission_reservations GROUP BY fingerprint
  ON CONFLICT (fingerprint) DO NOTHING;
INSERT INTO admission_snapshots (fingerprint, bytes, created_at)
  SELECT pending_bundle_sha256, 1048576, min(updated_at) FROM schedules WHERE pending_bundle_sha256 IS NOT NULL
  GROUP BY pending_bundle_sha256 ON CONFLICT (fingerprint) DO NOTHING;

-- New audit facts name the authenticated principal explicitly. Historical
-- attribution is unknown and remains NULL, never inferred from a reason token.
ALTER TABLE identity_conflicts ADD COLUMN principal TEXT;
ALTER TABLE events ADD COLUMN principal TEXT;
-- Source staging updates one operator-managed schedule row. Replaying a
-- retained bundle must not append an event on every authenticated call.
ALTER TABLE schedules ADD COLUMN staged_by TEXT;
ALTER TABLE schedules ADD COLUMN staging_count INTEGER NOT NULL DEFAULT 0;
ALTER TABLE schedules ADD COLUMN staged_at INTEGER;

-- Bounded aggregate diagnostics: 256 distinct principal/reason cells plus
-- one overflow cell. No request body, bearer token or arbitrary client label.
CREATE TABLE admission_refusals (
  audit_key TEXT PRIMARY KEY,
  principal TEXT NOT NULL,
  reason TEXT NOT NULL,
  occurrences INTEGER NOT NULL,
  operation_id TEXT,
  subject TEXT,
  first_at INTEGER NOT NULL,
  last_at INTEGER NOT NULL
);

-- The export's change log and the projection of accepted outputs.
--
-- export_changes is written by triggers in the same statement as every change
-- an exported run record reflects, so no code path can change a run without
-- advancing its version: a change is committed together with its log row or
-- not at all. The export cursor and each run's record_version are ids here.
-- Trigger bodies stay on one line for the migration splitter.
CREATE TABLE export_changes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  operation_id TEXT NOT NULL,
  at INTEGER NOT NULL
);
CREATE INDEX export_changes_by_operation ON export_changes (operation_id, id);

-- Who established a publication: the publisher, which publishes an artifact
-- to a target (one row per target and artifact, true of every run with that
-- artifact), or an observation of the producer's deployment, which belongs to
-- one run and target only.
ALTER TABLE publications ADD COLUMN authority TEXT NOT NULL DEFAULT 'publisher' CHECK (authority IN ('publisher', 'observed'));
CREATE INDEX publications_by_artifact ON publications (artifact_sha256);
CREATE INDEX operations_by_artifact ON operations (artifact_sha256);

CREATE TRIGGER export_operation_inserted AFTER INSERT ON operations BEGIN INSERT INTO export_changes (operation_id, at) VALUES (NEW.operation_id, NEW.updated_at); END;
CREATE TRIGGER export_operation_updated AFTER UPDATE ON operations BEGIN INSERT INTO export_changes (operation_id, at) VALUES (NEW.operation_id, NEW.updated_at); END;
-- A publisher publication changes the record of every completed run with its
-- artifact; an observed one changes only its own run's record.
CREATE TRIGGER export_publication_inserted AFTER INSERT ON publications BEGIN INSERT INTO export_changes (operation_id, at) SELECT NEW.operation_id, NEW.updated_at UNION SELECT operation_id, NEW.updated_at FROM operations WHERE NEW.authority = 'publisher' AND artifact_sha256 = NEW.artifact_sha256 AND state = 'completed'; END;
CREATE TRIGGER export_publication_updated AFTER UPDATE ON publications BEGIN INSERT INTO export_changes (operation_id, at) SELECT NEW.operation_id, NEW.updated_at UNION SELECT operation_id, NEW.updated_at FROM operations WHERE NEW.authority = 'publisher' AND artifact_sha256 = NEW.artifact_sha256 AND state = 'completed'; END;
CREATE TRIGGER export_conflict_inserted AFTER INSERT ON identity_conflicts BEGIN INSERT INTO export_changes (operation_id, at) VALUES (NEW.existing_operation_id, NEW.observed_at); END;
CREATE TRIGGER export_article_marked AFTER UPDATE OF executed ON operation_articles BEGIN INSERT INTO export_changes (operation_id, at) VALUES (NEW.operation_id, 0); END;

-- Operations written before this migration enter the log once, in admission
-- order, so a full export still reaches them.
INSERT INTO export_changes (operation_id, at) SELECT operation_id, updated_at FROM operations ORDER BY seq;

-- A pipeline either hands admissions to the execution service ('execute') or
-- records runs the authoritative producer already completed ('project').
ALTER TABLE pipelines ADD COLUMN mode TEXT NOT NULL DEFAULT 'execute' CHECK (mode IN ('execute', 'project'));

-- How a run entered this store, fixed at insert: executed through the
-- execution service, or projected from the authoritative producer's output.
ALTER TABLE operations ADD COLUMN origin TEXT NOT NULL DEFAULT 'execute' CHECK (origin IN ('execute', 'project'));

-- A projected run's identity beyond its operation id: the SHA-256 of its
-- complete accepted projection record (contracts/projection.md). A replay is
-- the same run only when this is equal.
ALTER TABLE operations ADD COLUMN facts_sha256 TEXT CHECK (facts_sha256 IS NULL OR length(facts_sha256) = 64);

-- Why a source the run read was not executed, when the producer reported it.
ALTER TABLE operation_articles ADD COLUMN exclusion TEXT CHECK (exclusion IS NULL OR exclusion IN ('filtered', 'review_required', 'source_rejected'));

-- The producer's own publication time for the article, when it supplied one
-- (RFC 3339, UTC). Unknown stays NULL.
ALTER TABLE article_revisions ADD COLUMN published_at TEXT;

-- A deployment of a source commit observed by the producer's own publisher.
-- It may arrive before or after the run is projected; whichever is written
-- second attaches the publication, and both writes are idempotent.
CREATE TABLE publication_observations (
  pipeline TEXT NOT NULL,
  source_commit TEXT NOT NULL CHECK (length(source_commit) = 40),
  target TEXT NOT NULL,
  observed_at TEXT NOT NULL,
  recorded_at INTEGER NOT NULL,
  PRIMARY KEY (pipeline, source_commit, target)
);

-- Where each bounded sweep (status pull, publication repair, scheduled
-- admission) resumes, so rows that stay eligible cannot starve later ones.
CREATE TABLE sweep_cursors (
  name TEXT PRIMARY KEY,
  after_seq INTEGER NOT NULL
);

-- A projected run's source commit is kept in run_id; publication observations
-- find the run by it.
CREATE INDEX operations_by_run ON operations (pipeline, run_id);

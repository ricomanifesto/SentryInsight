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

CREATE TRIGGER export_operation_inserted AFTER INSERT ON operations BEGIN INSERT INTO export_changes (operation_id, at) VALUES (NEW.operation_id, NEW.updated_at); END;
CREATE TRIGGER export_operation_updated AFTER UPDATE ON operations BEGIN INSERT INTO export_changes (operation_id, at) VALUES (NEW.operation_id, NEW.updated_at); END;
CREATE TRIGGER export_publication_inserted AFTER INSERT ON publications BEGIN INSERT INTO export_changes (operation_id, at) VALUES (NEW.operation_id, NEW.updated_at); END;
CREATE TRIGGER export_publication_updated AFTER UPDATE ON publications BEGIN INSERT INTO export_changes (operation_id, at) VALUES (NEW.operation_id, NEW.updated_at); END;
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

-- A projected run's source commit is kept in run_id; publication observations
-- find the run by it.
CREATE INDEX operations_by_run ON operations (pipeline, run_id);

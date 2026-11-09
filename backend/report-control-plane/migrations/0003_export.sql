-- Facts the research export needs that the first schema did not keep.
--
-- content_kind is the admitted record's own coverage label, kept only when it
-- is one the product defines ('feed' or 'article'); anything else is 'other'
-- and an absent label stays NULL. content_bytes is the UTF-8 length of the
-- admitted content, so an empty record is visibly metadata-only.
ALTER TABLE article_revisions ADD COLUMN content_kind TEXT
  CHECK (content_kind IS NULL OR content_kind IN ('feed', 'article', 'other'));
ALTER TABLE article_revisions ADD COLUMN content_bytes INTEGER;

-- Whether the execution side reported the article as executed. NULL until the
-- operation completes; 0 means excluded by the execution side's policy.
ALTER TABLE operation_articles ADD COLUMN executed INTEGER CHECK (executed IS NULL OR executed IN (0, 1));

-- A refused reuse of a source revision label with different bytes. The
-- refused bytes stay in R2 under their own digest, so the conflicting content
-- is retained and visible instead of silently dropped. observation_nonce is
-- written only by the insert that created the row; the audit event in the same
-- batch requires it, so repeats record one event.
CREATE TABLE identity_conflicts (
  pipeline TEXT NOT NULL,
  source_revision TEXT NOT NULL,
  refused_fingerprint TEXT NOT NULL CHECK (length(refused_fingerprint) = 64),
  existing_operation_id TEXT NOT NULL,
  observation_nonce TEXT NOT NULL,
  observed_at INTEGER NOT NULL,
  PRIMARY KEY (pipeline, source_revision, refused_fingerprint)
);

CREATE INDEX identity_conflicts_by_operation ON identity_conflicts (existing_operation_id);

-- The export orders revisions by rowid, which is commit order here: D1 has
-- one writer and revisions are never deleted. The Worker clock is not, since
-- a batch can commit after a later-stamped one. An index on content alone
-- keeps equal digests in rowid order.
CREATE INDEX article_revisions_by_content ON article_revisions (content_sha256);
-- Publication events name their publication as the subject.
CREATE INDEX events_by_subject ON events (subject, id);
CREATE INDEX publications_by_operation ON publications (operation_id);
CREATE INDEX identity_conflicts_by_refused ON identity_conflicts (refused_fingerprint);

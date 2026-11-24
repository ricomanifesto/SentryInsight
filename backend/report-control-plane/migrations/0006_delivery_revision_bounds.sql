-- A won delivery claim consumes one durable attempt in its generation.
-- Existing in-flight rows start at zero: incomplete evidence leaves their
-- dead-letter notifications advisory and the bounded sweeper repairs them.
ALTER TABLE operations ADD COLUMN delivery_attempts INTEGER NOT NULL DEFAULT 0 CHECK (delivery_attempts >= 0);

-- A single-key index stores equal keys in implicit rowid (commit) order.
-- The composite revision primary key orders by digest instead, forcing a
-- sort for predecessor lookup and filtering every revision for range counts.
CREATE INDEX article_revisions_by_key_order ON article_revisions (article_key);

-- Revision facts are immutable and owned by the database, so every producer
-- uses the same commit order and export need not recount an article's history.
ALTER TABLE article_revisions ADD COLUMN revision_index INTEGER NOT NULL DEFAULT 0 CHECK (revision_index >= 0);
ALTER TABLE article_revisions ADD COLUMN previous_content_sha256 TEXT;
WITH revision_facts AS MATERIALIZED (
  SELECT rowid AS revision_rowid,
    row_number() OVER (PARTITION BY article_key ORDER BY rowid) AS ordinal,
    lag(content_sha256) OVER (PARTITION BY article_key ORDER BY rowid) AS predecessor
  FROM article_revisions
)
UPDATE article_revisions SET
  revision_index = (SELECT ordinal FROM revision_facts WHERE revision_rowid = article_revisions.rowid),
  previous_content_sha256 = (SELECT predecessor FROM revision_facts WHERE revision_rowid = article_revisions.rowid);

-- A single predecessor lookup is bounded by the key/rowid index. The trigger
-- runs inside the inserting statement, before another reader sees the row.
CREATE TRIGGER article_revision_ordered AFTER INSERT ON article_revisions BEGIN
  UPDATE article_revisions SET
    revision_index = coalesce((
      SELECT x.revision_index FROM article_revisions x INDEXED BY article_revisions_by_key_order
      WHERE x.article_key = NEW.article_key AND x.rowid < NEW.rowid ORDER BY x.rowid DESC LIMIT 1
    ), 0) + 1,
    previous_content_sha256 = (
      SELECT x.content_sha256 FROM article_revisions x INDEXED BY article_revisions_by_key_order
      WHERE x.article_key = NEW.article_key AND x.rowid < NEW.rowid ORDER BY x.rowid DESC LIMIT 1
    )
  WHERE rowid = NEW.rowid; END;

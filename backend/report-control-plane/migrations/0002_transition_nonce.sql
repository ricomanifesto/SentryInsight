-- A fresh value written by the completion update itself. The artifact row
-- and the completion event in the same batch require it, so they are written
-- only by the caller whose own update applied, never by a stale caller that
-- observes another caller's completed row.
ALTER TABLE operations ADD COLUMN transition_nonce TEXT;

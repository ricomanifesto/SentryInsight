import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { DatabaseSync } from "node:sqlite";
import { test } from "node:test";

test("capacity migration conservatively accounts legacy references without inventing principals", () => {
  const db = new DatabaseSync(":memory:");
  try {
    for (const file of ["0001_init.sql", "0002_transition_nonce.sql", "0003_export.sql", "0004_projection.sql"]) {
      db.exec(readFileSync(new URL(`../migrations/${file}`, import.meta.url), "utf8"));
    }
    db.exec(`INSERT INTO operations (operation_id, pipeline, policy_id, binding_id, source_revision, fingerprint,
      principal, state, next_send_at, created_at, updated_at) VALUES ('${"1".repeat(64)}', 'reports', 'standard',
      '${"2".repeat(64)}', 'legacy', '${"3".repeat(64)}', 'manual', 'admitted', 0, 1, 1);
      INSERT INTO snapshots VALUES ('${"3".repeat(64)}', 123, 1);
      INSERT INTO identity_conflicts VALUES ('reports', 'legacy', '${"4".repeat(64)}', '${"1".repeat(64)}', 'nonce', 2);
      INSERT INTO schedules (schedule_id, pipeline, policy_id, state, pending_bundle_sha256, updated_at)
        VALUES ('daily', 'reports', 'standard', 'active', '${"5".repeat(64)}', 3);
      INSERT INTO events (kind, at) VALUES ('legacy', 1);`);
    db.exec(readFileSync(new URL("../migrations/0005_admission_capacity.sql", import.meta.url), "utf8"));
    const snapshots = db.prepare("SELECT bytes FROM admission_snapshots ORDER BY fingerprint").all();
    assert.deepEqual(snapshots.map((r) => r.bytes), [123, 1024 * 1024, 1024 * 1024]);
    const reservations = db.prepare("SELECT principal, state FROM admission_reservations ORDER BY operation_id").all();
    assert.equal(reservations.length, 2);
    assert.deepEqual(reservations.map((r) => r.state).sort(), ["admitted", "identity_conflict"]);
    assert.equal(reservations.find((r) => r.state === "admitted").principal, "manual");
    assert.equal(reservations.find((r) => r.state === "identity_conflict").principal, null);
    assert.equal(db.prepare("SELECT principal FROM identity_conflicts").get().principal, null);
    assert.equal(db.prepare("SELECT principal FROM events WHERE kind = 'legacy'").get().principal, null);
  } finally { db.close(); }
});

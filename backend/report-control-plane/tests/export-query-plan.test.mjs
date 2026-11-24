// Revision facts preserve commit order while unrelated history uses no scan.
import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { DatabaseSync } from "node:sqlite";
import { readFile } from "node:fs/promises";
import { PACKAGE_ROOT } from "../local/stack.mjs";
import path from "node:path";
import test from "node:test";
import { exportPage } from "../src/export.js";
import { seedOperation, sqliteDb } from "./support/sqlite-db.mjs";

const sha = (s) => createHash("sha256").update(s).digest("hex");

test("revision lookup uses article-key and rowid range indexes with unchanged revision facts", async () => {
  const db = await sqliteDb();
  try {
    const add = db.sqlite.prepare("INSERT INTO article_revisions (article_key, content_sha256, title, first_operation_id, created_at, content_bytes) VALUES (?, ?, 'Synthetic', ?, ?, 1)");
    for (let i = 0; i < 1000; i += 1) add.run(`https://example.test/unrelated/${i}`, sha(`unrelated-${i}`), sha("unrelated"), i);
    const key = "https://example.test/revised";
    for (let i = 0; i < 3; i += 1) {
      const id = sha(`operation-${i}`);
      seedOperation(db, id, { state: "failed" });
      add.run(key, sha(`content-${i}`), id, 3 - i); // clocks run opposite commit order
      db.sqlite.prepare("INSERT INTO operation_articles (operation_id, position, article_key, content_sha256) VALUES (?, 0, ?, ?)").run(id, key, sha(`content-${i}`));
    }
    const page = await exportPage(db, { after: 0, limit: 25 });
    const revisions = page.records.filter((r) => r.record_type === "source_revision");
    assert.deepEqual(revisions.map((r) => r.revision), [
      { index: 1, previous_content_sha256: null },
      { index: 2, previous_content_sha256: sha("content-0") },
      { index: 3, previous_content_sha256: sha("content-1") },
    ]);
    const query = db.queries.find((sql) => sql.includes("AS revision_index"));
    const plan = db.sqlite.prepare(`EXPLAIN QUERY PLAN ${query}`).all(sha("operation-2")).map((r) => r.detail);
    const revisionLookups = plan.filter((detail) => /\bx\b/.test(detail));
    assert.doesNotMatch(query, /SELECT count\(\*\) FROM article_revisions/, "export reads stored ordinals without walking revision history");
    assert.equal(revisionLookups.length, 1, "only indexed same-content provenance lookup remains correlated");
    assert.ok(!plan.some((detail) => /SCAN x|TEMP B-TREE/.test(detail)), plan.join("\n"));
  } finally { db.sqlite.close(); }
});


test("historical backfill and future insert triggers keep exact rowid revision order", async () => {
  const sqlite = new DatabaseSync(":memory:");
  try {
    for (const file of ["0001_init.sql", "0002_transition_nonce.sql", "0003_export.sql", "0004_projection.sql"]) {
      sqlite.exec(await readFile(path.join(PACKAGE_ROOT, "migrations", file), "utf8"));
    }
    const insert = sqlite.prepare("INSERT INTO article_revisions (article_key, content_sha256, title, first_operation_id, created_at) VALUES (?, ?, 'Synthetic', ?, ?)");
    for (const [key, content, clock] of [["A", "first", 9], ["B", "other", 5], ["A", "second", 2], ["A", "third", 0]]) insert.run(key, sha(content), sha("operation"), clock);
    sqlite.exec(await readFile(path.join(PACKAGE_ROOT, "migrations/0006_delivery_revision_bounds.sql"), "utf8"));
    const facts = () => sqlite.prepare("SELECT article_key, revision_index, previous_content_sha256 FROM article_revisions ORDER BY rowid").all().map((r) => ({ ...r }));
    assert.deepEqual(facts(), [
      { article_key: "A", revision_index: 1, previous_content_sha256: null },
      { article_key: "B", revision_index: 1, previous_content_sha256: null },
      { article_key: "A", revision_index: 2, previous_content_sha256: sha("first") },
      { article_key: "A", revision_index: 3, previous_content_sha256: sha("second") },
    ]);
    insert.run("A", sha("fourth"), sha("operation"), -1);
    assert.deepEqual(facts().at(-1), { article_key: "A", revision_index: 4, previous_content_sha256: sha("third") });
    const replay = sqlite.prepare("INSERT INTO article_revisions (article_key, content_sha256, title, first_operation_id, created_at) VALUES ('A', ?, 'Synthetic', ?, 100) ON CONFLICT DO NOTHING");
    replay.run(sha("fourth"), sha("operation"));
    assert.equal(facts().length, 5);
  } finally { sqlite.close(); }
});

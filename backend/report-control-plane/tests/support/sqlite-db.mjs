// In-process SQLite adapter for unit contracts; integration suites use D1.
import { DatabaseSync } from "node:sqlite";
import { readdir, readFile } from "node:fs/promises";
import { PACKAGE_ROOT } from "../../local/stack.mjs";
import path from "node:path";

export async function sqliteDb() {
  const sqlite = new DatabaseSync(":memory:");
  for (const file of (await readdir(path.join(PACKAGE_ROOT, "migrations"))).filter((f) => /^\d{4}_.*\.sql$/.test(f)).sort()) {
    sqlite.exec(await readFile(path.join(PACKAGE_ROOT, "migrations", file), "utf8"));
  }
  const queries = [];
  const db = {
    sqlite, queries,
    prepare(sql) {
      queries.push(sql);
      let values = [];
      return {
        sql,
        bind(...params) { values = params; return this; },
        async all() { return { results: sqlite.prepare(sql).all(...values).map((r) => ({ ...r })) }; },
        async first() { const row = sqlite.prepare(sql).get(...values); return row ? { ...row } : null; },
        async run() {
          const statement = sqlite.prepare(sql);
          return { results: statement.columns().length ? statement.all(...values).map((r) => ({ ...r })) : (statement.run(...values), []) };
        },
      };
    },
    async batch(statements) { return Promise.all(statements.map((s) => s.all())); },
  };
  return db;
}

export function seedOperation(db, id, overrides = {}) {
  const values = { operation_id: id, pipeline: "reports", policy_id: "standard", binding_id: "b".repeat(64), source_revision: id, fingerprint: "f".repeat(64), principal: "synthetic", state: "enqueued", next_send_at: 0, created_at: 1, updated_at: 1, ...overrides };
  db.sqlite.prepare(`INSERT INTO operations (${Object.keys(values).join(",")}) VALUES (${Object.keys(values).map(() => "?").join(",")})`).run(...Object.values(values));
}

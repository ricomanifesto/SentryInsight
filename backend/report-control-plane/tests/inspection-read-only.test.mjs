// Native read-only connection and authorizer checks against a disposable file.
import assert from "node:assert/strict";
import { createHash, createHmac } from "node:crypto";
import { DatabaseSync } from "node:sqlite";
import { mkdtemp, mkdir, readFile } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";

const moduleUrl = new URL("../local/read-only-db.mjs", import.meta.url);

test("inspection uses a native read-only connection to exactly the configured D1 database", async () => {
  const { openInspectionDatabase, inspectionDatabasePath, ReadOnlyRefused } = await import(moduleUrl);
  const root = await mkdtemp(path.join(os.tmpdir(), "rcp-read-only-"));
  const namespace = "report-control-plane";
  const uniqueKey = "miniflare-D1DatabaseObject";
  const key = createHash("sha256").update(uniqueKey).digest();
  const first = createHmac("sha256", key).update(namespace).digest().subarray(0, 16);
  const last = createHmac("sha256", key).update(first).digest().subarray(0, 16);
  const expected = path.join(root, "d1", uniqueKey, `${Buffer.concat([first, last]).toString("hex")}.sqlite`);
  assert.equal(inspectionDatabasePath(root, namespace), expected);
  await mkdir(path.dirname(expected), { recursive: true });
  const writer = new DatabaseSync(expected);
  writer.exec("CREATE TABLE records (id INTEGER PRIMARY KEY, value TEXT)");
  writer.prepare("INSERT INTO records (value) VALUES (?)").run("Synthetic Unicode café 😀");
  const reader = openInspectionDatabase(root, namespace);
  try {
    assert.deepEqual(reader.query("SELECT id, value FROM records WHERE id = ?", [1]), [{ id: 1, value: "Synthetic Unicode café 😀" }]);
    assert.deepEqual(reader.query("WITH selected AS (SELECT value FROM records) SELECT * FROM selected", []), [{ value: "Synthetic Unicode café 😀" }]);
    assert.deepEqual(reader.query("SELECT ? AS flag, X'0102' AS bytes", [true]), [{ flag: 1, bytes: [1, 2] }]);
    assert.throws(() => reader.query("UPDATE records SET value = ? WHERE id = ?", ["changed", 1]), ReadOnlyRefused);
    assert.equal(writer.prepare("SELECT value FROM records WHERE id = 1").get().value, "Synthetic Unicode café 😀");
    writer.prepare("INSERT INTO records (value) VALUES (?)").run("new committed row");
    assert.equal(reader.query("SELECT count(*) AS n FROM records", [])[0].n, 2, "inspection sees new commits while worker writes remain available");
    const source = await readFile(fileURLToPath(moduleUrl), "utf8");
    assert.match(source, /new DatabaseSync\([^\n]*\{ readOnly: true/);
    assert.match(source, /setAuthorizer/);
    assert.doesNotMatch(source, /SQLITE_(?:ATTACH|DETACH|PRAGMA)\s*[,\]]/);
  } finally { reader.close(); writer.close(); }
  assert.throws(() => openInspectionDatabase(root, "another-database"), "read-only open cannot create or select another existing file through query parameters");
});

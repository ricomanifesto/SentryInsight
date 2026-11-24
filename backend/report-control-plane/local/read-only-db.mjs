// Local inspection requires Node >=24.10 (native SQLite authorizers).
// Miniflare 4's D1 namespace layout is deliberately isolated here: derive the
// one configured database filename, never discover or accept arbitrary files.
import { createHash, createHmac } from "node:crypto";
import { DatabaseSync, constants } from "node:sqlite";
import path from "node:path";

const NAMESPACE = "miniflare-D1DatabaseObject";
const ALLOWED = new Set([constants.SQLITE_SELECT, constants.SQLITE_READ, constants.SQLITE_FUNCTION, constants.SQLITE_RECURSIVE]);
export class ReadOnlyRefused extends Error {}

export function inspectionDatabasePath(persistDir, databaseId) {
  const key = createHash("sha256").update(NAMESPACE).digest();
  const first = createHmac("sha256", key).update(databaseId).digest().subarray(0, 16);
  const last = createHmac("sha256", key).update(first).digest().subarray(0, 16);
  return path.join(persistDir, "d1", NAMESPACE, `${Buffer.concat([first, last]).toString("hex")}.sqlite`);
}

export function openInspectionDatabase(persistDir, databaseId) {
  const db = new DatabaseSync(inspectionDatabasePath(persistDir, databaseId), { readOnly: true, allowExtension: false });
  if (typeof db.setAuthorizer !== "function") {
    db.close();
    throw new Error("local inspection requires Node >=24.10 with SQLite authorizer support");
  }
  let refused = false;
  db.setAuthorizer((action, _arg1, arg2) => {
    // Read-only main DB permissions are the primary boundary. The authorizer
    // also refuses attachments, connection changes, writes to TEMP, and
    // extension loading, so a query cannot switch its storage authority.
    if (!ALLOWED.has(action) || (action === constants.SQLITE_FUNCTION && arg2 === "load_extension")) {
      refused = true;
      return constants.SQLITE_DENY;
    }
    return constants.SQLITE_OK;
  });
  return {
    query(sql, params = []) {
      if (typeof sql !== "string" || !Array.isArray(params)) throw new ReadOnlyRefused();
      refused = false;
      try {
        const values = params.map((value) => typeof value === "boolean" ? Number(value) : value);
        return db.prepare(sql).all(...values).map((row) => Object.fromEntries(
          Object.entries(row).map(([key, value]) => [key, ArrayBuffer.isView(value) ? Array.from(value) : value]),
        ));
      } catch (error) {
        if (refused) throw new ReadOnlyRefused();
        throw error;
      }
    },
    close() { db.close(); },
  };
}

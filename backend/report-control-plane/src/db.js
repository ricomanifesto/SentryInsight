// D1 helpers. D1 batch is the only transactional unit used anywhere.

export function now() {
  return Date.now();
}

export function event(db, { operationId = null, subject = null, kind, token = null, detail = null, at }) {
  return db
    .prepare("INSERT INTO events (operation_id, subject, kind, token, detail, at) VALUES (?, ?, ?, ?, ?, ?)")
    .bind(operationId, subject, kind, token, detail === null ? null : JSON.stringify(detail), at);
}

export function record(db, fields) {
  return event(db, fields).run();
}

export function operation(db, operationId) {
  return db.prepare("SELECT * FROM operations WHERE operation_id = ?").bind(operationId).first();
}

export function isConstraintError(error) {
  return /constraint/i.test(String(error?.message ?? error));
}

export class InvariantViolation extends Error {}

// Rows a guarded statement changed itself. D1's meta.changes also counts rows
// written by triggers (migration 0004 logs every run change through them), so
// every guarded statement ends in RETURNING and is counted by its rows.
export function rowsChanged(result) {
  return result.results.length;
}

// A coupled batch either changes every guarded row or none: anything else is
// an invariant violation, never a partial success.
export function allOrNone(results, count) {
  const changes = results.slice(0, count).map(rowsChanged);
  if (changes.every((c) => c === 1)) return true;
  if (changes.every((c) => c === 0)) return false;
  throw new InvariantViolation(`changes ${changes.join(",")}`);
}

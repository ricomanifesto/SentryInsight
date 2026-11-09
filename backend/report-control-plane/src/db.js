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

// The next bounded batch from `select`, resuming after the cursor `name` and
// wrapping to the start, so rows that stay eligible cannot starve later ones.
// `select` takes (after, upTo, limit) bounds on an increasing `cursor_key`.
export async function rotatingBatch(db, name, select, limit) {
  const cursor = await db.prepare("SELECT after_seq FROM sweep_cursors WHERE name = ?").bind(name).first();
  const after = cursor?.after_seq ?? 0;
  const { results: tail } = await db.prepare(select).bind(after, Number.MAX_SAFE_INTEGER, limit).all();
  const { results: head } = tail.length < limit ? await db.prepare(select).bind(0, after, limit - tail.length).all() : { results: [] };
  const batch = [...tail, ...head];
  if (batch.length > 0) {
    await db
      .prepare("INSERT INTO sweep_cursors (name, after_seq) VALUES (?, ?) ON CONFLICT (name) DO UPDATE SET after_seq = excluded.after_seq")
      .bind(name, batch[batch.length - 1].cursor_key)
      .run();
  }
  return batch;
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

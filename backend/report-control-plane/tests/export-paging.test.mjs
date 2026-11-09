// The export cursor across chunk, run-limit and scan-cap boundaries, against
// an in-memory event log (the paging query is the only database call).
import assert from "node:assert/strict";
import test from "node:test";
import { touchedOperations } from "../src/export.js";

// Events 1..n; most name an operation (some repeatedly), some name none.
function log(n, seed) {
  let state = seed;
  const random = () => (state = (state * 1103515245 + 12345) % 2 ** 31) / 2 ** 31;
  return Array.from({ length: n }, (_, i) => ({ id: i + 1, operation_id: random() < 0.2 ? null : `op-${Math.floor(random() * 15)}` }));
}

function fakeDb(events) {
  return {
    prepare() {
      return {
        bind(after, chunk) {
          return { all: async () => ({ results: events.filter((e) => e.id > after).slice(0, chunk) }) };
        },
      };
    },
  };
}

test("every event's operation is listed by the page that accounts for it; cursors advance to the end", async () => {
  for (const [n, seed] of [[0, 1], [1, 2], [7, 3], [40, 4], [41, 5], [97, 6]]) {
    const events = log(n, seed);
    for (const limits of [{ eventChunk: 1, maxEventsScanned: 1 }, { eventChunk: 4, maxEventsScanned: 8 }, { eventChunk: 5, maxEventsScanned: 7 }, { eventChunk: 200, maxEventsScanned: 2000 }]) {
      for (const limit of [1, 2, 3, 25]) {
        const label = JSON.stringify({ n, seed, limits, limit });
        const db = fakeDb(events);
        let after = 0;
        const accounted = new Map();
        for (let page = 0; ; page += 1) {
          assert.ok(page < 1000, label);
          const { operations, cursor, hasMore } = await touchedOperations(db, after, limit, limits);
          assert.ok(operations.length <= limit, label);
          assert.equal(new Set(operations).size, operations.length, label);
          assert.ok(cursor >= after, label);
          for (const e of events.filter((x) => x.id > after && x.id <= cursor)) {
            assert.ok(!accounted.has(e.id), `${label} event ${e.id} twice`);
            accounted.set(e.id, true);
            if (e.operation_id !== null) assert.ok(operations.includes(e.operation_id), `${label} event ${e.id} lost`);
          }
          if (!hasMore) {
            assert.equal(cursor, events.length === 0 ? after : events[events.length - 1].id, label);
            break;
          }
          assert.ok(cursor > after || operations.length > 0, `${label} no progress`);
          after = cursor;
        }
        assert.equal(accounted.size, events.length, label);
      }
    }
  }
});

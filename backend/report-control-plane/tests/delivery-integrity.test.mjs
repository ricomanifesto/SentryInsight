// Handler contracts verify durable corroboration without injecting Queue messages.
import assert from "node:assert/strict";
import test from "node:test";
import { handleDeadLetter, handleDelivery, manualRetry } from "../src/delivery.js";
import { LIMITS } from "../src/config.js";
import { seedOperation, sqliteDb } from "./support/sqlite-db.mjs";

const settings = { executionConfigured: true, QUEUE_RETRY_DELAY_S: 1, claimMs: 1000, SEND_BACKOFF_BASE_MS: 10 };
const id = "a".repeat(64);
const body = { operation_id: id, generation: 1 };

test("dead-letter disposition needs a durable exhausted attempt budget", async () => {
  const db = await sqliteDb();
  try {
    seedOperation(db, id, { send_attempts: 1 });
    const before = await db.prepare("SELECT * FROM operations").first();
    await handleDeadLetter({ PRODUCT_DB: db }, settings, body);
    assert.deepEqual(await db.prepare("SELECT * FROM operations").first(), before, "an incomplete delivery budget is advisory");
    assert.equal((await db.prepare("SELECT count(*) AS n FROM events WHERE kind = 'dead_letter'").first()).n, 0);
  } finally { db.sqlite.close(); }
});

test("unbound and repeated advisory notifications have bounded audit storage", async () => {
  const db = await sqliteDb();
  try {
    await handleDeadLetter({ PRODUCT_DB: db }, settings, body);
    assert.equal((await db.prepare("SELECT count(*) AS n FROM events").first()).n, 0, "no event may name an absent operation");
    seedOperation(db, id, { send_attempts: 1 });
    for (let i = 0; i < 5; i += 1) await handleDeadLetter({ PRODUCT_DB: db }, settings, { ...body, generation: i + 1 });
    assert.equal((await db.prepare("SELECT count(*) AS n FROM events").first()).n, 1);
  } finally { db.sqlite.close(); }
});

test("current exhausted generations settle, while live claims and terminal decisions remain intact", async () => {
  for (const exhausted of [{ send_attempts: LIMITS.maxSendAttempts }, { delivery_attempts: LIMITS.maxDeliveryAttempts }]) {
    const db = await sqliteDb();
    try {
      seedOperation(db, id, exhausted);
      await handleDeadLetter({ PRODUCT_DB: db }, settings, body);
      assert.equal((await db.prepare("SELECT * FROM operations").first()).state, "dead_letter");
      const retried = await manualRetry({ PRODUCT_DB: db, ADMISSIONS: { send: async () => {} } }, settings, id);
      assert.equal(retried.status, 202);
      assert.equal(retried.operation.delivery_attempts, 0, "a manual generation atomically resets its attempt budget");
    } finally { db.sqlite.close(); }
  }
  for (const overrides of [
    { state: "submitting", claim_token: "owned", claim_expires_at: Date.now() + 60_000 },
    { state: "submitted" }, { state: "completed" }, { delivery_generation: 2 },
  ]) {
    const db = await sqliteDb();
    try {
      seedOperation(db, id, { send_attempts: LIMITS.maxSendAttempts, ...overrides });
      const before = await db.prepare("SELECT * FROM operations").first();
      await handleDeadLetter({ PRODUCT_DB: db }, settings, body);
      assert.deepEqual(await db.prepare("SELECT * FROM operations").first(), before);
    } finally { db.sqlite.close(); }
  }
});

test("a won main-delivery claim durably increments its generation attempt budget", async () => {
  const db = await sqliteDb();
  try {
    seedOperation(db, id);
    await handleDelivery({ PRODUCT_DB: db, ARTIFACTS: { get: async () => null } }, settings, body);
    const row = await db.prepare("SELECT * FROM operations").first();
    assert.equal(row.delivery_attempts, 1);
    assert.equal(row.state, "failed");
    await handleDelivery({ PRODUCT_DB: db }, settings, body);
    assert.equal((await db.prepare("SELECT * FROM operations").first()).delivery_attempts, 1, "a settled duplicate cannot consume a new attempt");
  } finally { db.sqlite.close(); }
});

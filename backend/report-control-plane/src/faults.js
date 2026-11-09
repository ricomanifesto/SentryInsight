// Test-only interruption points. Inert unless the stack sets TEST_FAULTS to
// "enabled" and the harness has created a test_faults table; a deployed
// configuration sets neither.

import { sleep } from "./util.js";

export class FaultInjected extends Error {}

export async function fault(env, point) {
  if (env.TEST_FAULTS !== "enabled") return;
  const db = env.PRODUCT_DB;
  const row = await db
    .prepare("SELECT remaining, mode, delay_ms FROM test_faults WHERE point = ?")
    .bind(point)
    .first();
  if (row === null || row.remaining <= 0) return;
  const taken = await db
    .prepare("UPDATE test_faults SET remaining = remaining - 1, fired = fired + 1 WHERE point = ? AND remaining = ?")
    .bind(point, row.remaining)
    .run();
  if (taken.meta.changes !== 1) return;
  if (row.mode === "delay") {
    await sleep(row.delay_ms);
    return;
  }
  throw new FaultInjected(point);
}

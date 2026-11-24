// Defensive boundary contracts use synthetic values and mocked transports only.
import assert from "node:assert/strict";
import test from "node:test";
import { ConfigInvalid, settings } from "../src/config.js";
import { fetchPart, readExecution, submitExecution } from "../src/execution-client.js";
import { observePublication, postPublication } from "../src/publisher-client.js";
import { readBounded, TooLarge } from "../src/util.js";

const TOKEN = "synthetic-upstream-token";
const options = { EXECUTION_URL: "https://execution.example.test", EXECUTION_TOKEN: TOKEN, PUBLISHER_URL: "https://publisher.example.test", PUBLISHER_TOKEN: TOKEN, CALL_TIMEOUT_MS: 1000 };

test("authenticated upstreams require HTTPS except numeric loopback development", () => {
  for (const role of ["EXECUTION", "PUBLISHER"]) {
    for (const url of ["http://service.example.test", "http://192.0.2.10", "https://user:pass@service.example.test", "http://localhost.example.test"]) {
      assert.throws(() => settings({ [`${role}_URL`]: url, [`${role}_TOKEN`]: TOKEN }), ConfigInvalid, url);
    }
    for (const url of ["https://service.example.test/base", "http://127.0.0.1:9000", "http://[::1]:9000"]) {
      assert.equal(settings({ [`${role}_URL`]: url, [`${role}_TOKEN`]: TOKEN })[`${role.toLowerCase()}Configured`], true, url);
    }
  }
});

test("every authenticated upstream request refuses redirect following", async () => {
  const original = globalThis.fetch;
  const calls = [];
  globalThis.fetch = async (url, init) => {
    calls.push({ url, init });
    return new Response("{}", { status: 503 });
  };
  try {
    const row = { operation_id: "a".repeat(64), fingerprint: "b".repeat(64), binding_id: "c".repeat(64) };
    const publication = { publication_id: "d".repeat(64), target: "site", artifact_sha256: "e".repeat(64), candidate_seq: 1 };
    await submitExecution({}, options, row, new Uint8Array([1]));
    await readExecution({}, options, row.operation_id, row.fingerprint, row.binding_id);
    await fetchPart({}, options, row.operation_id, "index.md", 2);
    await observePublication(options, publication);
    await postPublication(options, publication, 0);
  } finally {
    globalThis.fetch = original;
  }
  assert.equal(calls.length, 5);
  for (const { url, init } of calls) {
    assert.equal(init.redirect, "manual", url);
    assert.equal(new Headers(init.headers).get("authorization"), `Bearer ${TOKEN}`);
  }
});

test("bounded reader copies tiny chunks as they arrive with fixed bookkeeping", async () => {
  const count = 32 * 1024;
  const reused = new Uint8Array(1);
  let at = 0;
  let released = false;
  const stream = { getReader: () => ({
    async read() {
      if (at === count) return { done: true };
      reused[0] = at++ % 251;
      return { value: reused, done: false };
    },
    releaseLock() { released = true; },
  }) };
  const actual = await readBounded(stream, count);
  assert.equal(actual.length, count);
  assert.equal(actual.every((value, i) => value === i % 251), true, "chunks are copied before their backing storage is reused");
  assert.equal(released, true);
});

test("bounded reader accepts the exact byte bound and cancels oversize input", async () => {
  const body = (chunks) => new ReadableStream({ start(controller) { for (const chunk of chunks) controller.enqueue(chunk); controller.close(); } });
  assert.deepEqual(await readBounded(null, 0), new Uint8Array());
  assert.deepEqual(await readBounded(body([new Uint8Array(), new Uint8Array([1, 2]), new Uint8Array([3])]), 3), new Uint8Array([1, 2, 3]));
  let cancelled = false;
  const over = new ReadableStream({ start(controller) { controller.enqueue(new Uint8Array(4)); }, cancel() { cancelled = true; } });
  await assert.rejects(readBounded(over, 3), TooLarge);
  assert.equal(cancelled, true);
  assert.equal(over.locked, false);
});

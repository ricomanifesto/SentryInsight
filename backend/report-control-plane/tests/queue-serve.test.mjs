// The runner (local/serve.mjs) with configured queue names: its ready file
// reports the effective names, the authenticated /queue-dispatch inspection
// guard admits exactly those names and refuses the defaults as unknown, and
// invalid names stop the runner before it is ready. One owned runner at a
// time; each is stopped through its own handle and its engine children are
// confirmed gone.
import assert from "node:assert/strict";
import { execFile, spawn } from "node:child_process";
import { mkdtemp, readFile, writeFile } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import test from "node:test";
import { promisify } from "node:util";
import { PACKAGE_ROOT } from "../local/stack.mjs";
import { miniflareModule, sleep } from "./support/harness.mjs";

const run = promisify(execFile);
const NAMES = { admissions: "serve-admission-jobs", dead: "serve-admission-jobs-dead" };
const TOKEN = "synthetic-inspection-token-0123456789";

async function runner(vars) {
  const root = await mkdtemp(path.join(process.env.REPORT_CONTROL_TEST_ROOT ?? os.tmpdir(), "rcp-serve-"));
  const file = (name) => path.join(root, name);
  await writeFile(file("token"), TOKEN);
  await writeFile(file("vars.json"), JSON.stringify({
    AUTH_PRINCIPALS: "[]",
    EXECUTION_URL: "http://127.0.0.1:9",
    EXECUTION_TOKEN: "synthetic-execution-token",
    PUBLISHER_URL: "http://127.0.0.1:9",
    PUBLISHER_TOKEN: "synthetic-publisher-token",
    ...vars,
  }));
  await writeFile(file("config.json"), JSON.stringify({
    miniflare_module: miniflareModule(),
    persist_dir: file("persist"),
    port: 0,
    vars_file: file("vars.json"),
    inspect_port: 0,
    inspect_token_file: file("token"),
    ready_file: file("ready.json"),
    test_faults: false,
    queue: { retryDelay: 1, maxRetries: 2 },
  }));
  const child = spawn(process.execPath, [path.join(PACKAGE_ROOT, "local/serve.mjs"), "--config", file("config.json")], {
    env: { PATH: process.env.PATH, HOME: process.env.HOME, TMPDIR: process.env.TMPDIR },
    stdio: ["ignore", "pipe", "pipe"],
  });
  let stderr = "";
  child.stderr.on("data", (c) => (stderr += c));
  let gone = false;
  const exited = new Promise((resolve) => child.on("exit", (code, signal) => resolve({ code, signal })));
  exited.then(() => (gone = true));
  // Ready, or null once the runner has exited without becoming ready.
  let ready = null;
  for (let i = 0; i < 300 && ready === null && !gone; i += 1) {
    try {
      ready = JSON.parse(await readFile(file("ready.json"), "utf8"));
    } catch {
      await sleep(100);
    }
  }
  if (ready === null && !gone) {
    child.kill("SIGTERM");
    await exited;
    throw new Error("runner not ready");
  }
  return { child, ready, exited, stderr: () => stderr, file };
}

const alive = async (pid) => (await run("/bin/ps", ["-p", String(pid)]).then(() => true, () => false));

test("the runner dispatches only the configured names, refuses the defaults and stops cleanly", async () => {
  const { child, ready, exited } = await runner({ ADMISSIONS_QUEUE_NAME: NAMES.admissions, DEAD_LETTER_QUEUE_NAME: NAMES.dead });
  try {
    assert.ok(ready, "ready");
    assert.deepEqual(ready.queues, NAMES);
    const inspect = (body, token = TOKEN) =>
      fetch(`${ready.inspect_url}/queue-dispatch`, { method: "POST", headers: { authorization: `Bearer ${token}` }, body: JSON.stringify(body) });
    const malformed = [{ id: "m1", body: null }]; // acknowledged by either handler, with no effect
    for (const queue of [NAMES.admissions, NAMES.dead]) {
      const response = await inspect({ queue, messages: malformed });
      assert.equal(response.status, 200, queue);
      const result = await response.json();
      assert.deepEqual([result.outcome, result.explicitAcks], ["ok", ["m1"]], queue);
    }
    for (const queue of ["report-admissions", "report-admissions-dead", "other-queue"]) {
      const response = await inspect({ queue, messages: malformed });
      assert.deepEqual([response.status, await response.json()], [400, { error: "queue" }], queue);
    }
    const unauthenticated = await inspect({ queue: NAMES.admissions, messages: malformed }, "wrong-token-0123456789");
    assert.equal(unauthenticated.status, 401);
    const sql = await fetch(`${ready.inspect_url}/sql`, {
      method: "POST",
      headers: { authorization: `Bearer ${TOKEN}` },
      body: JSON.stringify({ sql: "SELECT count(*) AS n FROM events" }),
    });
    assert.deepEqual((await sql.json()).results, [{ n: 0 }], "the malformed messages recorded nothing");
  } finally {
    const engine = (await run("/usr/bin/pgrep", ["-P", String(child.pid)]).catch(() => ({ stdout: "" }))).stdout.split(/\s+/).filter(Boolean);
    child.kill("SIGTERM");
    const stopped = await exited;
    console.log(JSON.stringify({ runner_stop: stopped, engine_children: engine.length }));
    assert.ok(engine.length > 0, "the engine ran as the runner's child");
    for (const pid of engine) assert.equal(await alive(pid), false, `engine child ${pid} is gone`);
    await assert.rejects(fetch(ready.url), "the Worker listener is closed");
    await assert.rejects(fetch(`${ready.inspect_url}/sql`), "the inspection listener is closed");
  }
});

test("invalid queue names stop the runner before it is ready", async () => {
  for (const vars of [{ ADMISSIONS_QUEUE_NAME: "Upper" }, { ADMISSIONS_QUEUE_NAME: "same", DEAD_LETTER_QUEUE_NAME: "same" }]) {
    const { child, ready, exited, stderr, file } = await runner(vars);
    if (ready !== null) {
      // A runner that accepted the names is stopped here, then the case fails.
      child.kill("SIGTERM");
      await exited;
      assert.fail(`the runner became ready with ${JSON.stringify(vars)}`);
    }
    const stopped = await exited;
    assert.equal(stopped.code, 1);
    assert.match(stderr(), /serve failed: queue_names/);
    await assert.rejects(readFile(file("ready.json")), "no ready file");
  }
});

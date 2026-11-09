// Queue names without an engine: the resolver's defaults and grammar (Q1 to
// Q3), one topology for the Worker and the local stack (Q9), the declared
// deployment defaults, and refusal before any engine starts.
import assert from "node:assert/strict";
import { mkdtemp, readdir, readFile } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import test from "node:test";
import { ConfigInvalid, QUEUES, queueNames, settings } from "../src/config.js";
import { BINDINGS, QUEUES as STACK_QUEUES, PACKAGE_ROOT, startStack, workerOptions } from "../local/stack.mjs";
import { miniflareModule } from "./support/harness.mjs";

const NAMES = { admissions: "review-admission-jobs", dead: "review-admission-jobs-dead" };
const named = (names) => ({ ADMISSIONS_QUEUE_NAME: names.admissions, DEAD_LETTER_QUEUE_NAME: names.dead });
const BASE = {
  EXECUTION_URL: "http://127.0.0.1:9",
  EXECUTION_TOKEN: "synthetic-execution-token",
  PUBLISHER_URL: "http://127.0.0.1:9",
  PUBLISHER_TOKEN: "synthetic-publisher-token",
};
const refused = (env) => assert.throws(() => queueNames(env), (e) => e instanceof ConfigInvalid && e.message === "queue_names", JSON.stringify(env));

test("Q1 absent variables give the unchanged defaults, through the resolver and the settings", () => {
  assert.deepEqual({ ...queueNames({}) }, { admissions: "report-admissions", dead: "report-admissions-dead" });
  assert.deepEqual({ ...queueNames({}) }, { ...QUEUES });
  assert.deepEqual({ ...settings(BASE).queues }, { ...QUEUES });
  assert.deepEqual({ ...settings({ ...BASE, ...named(NAMES) }).queues }, NAMES);
  assert.equal(STACK_QUEUES, QUEUES, "the stack's default export is the same object");
});

test("Q2 well-formed names are accepted at the grammar's edges", () => {
  for (const name of ["a", "0", "a-b", "q1", "x".repeat(63), `a${"-".repeat(61)}b`]) {
    assert.equal(queueNames({ ADMISSIONS_QUEUE_NAME: name }).admissions, name, name);
  }
});

test("Q2 malformed names and shapes are refused, on either variable and through the settings", () => {
  const bad = ["", " report-admissions", "report-admissions ", "report admissions", "Report-Admissions", "REPORT", "report_admissions", "report.admissions",
    "-jobs", "jobs-", "x".repeat(64), "jobs\n", "jöbs", "jobs/dead", 7, 0, null, true, {}, [], ["jobs"]];
  for (const value of bad) {
    refused({ ADMISSIONS_QUEUE_NAME: value });
    refused({ DEAD_LETTER_QUEUE_NAME: value });
    assert.throws(() => settings({ ...BASE, ADMISSIONS_QUEUE_NAME: value }), ConfigInvalid);
  }
});

test("Q3 identical or ambiguous names are refused", () => {
  refused({ ADMISSIONS_QUEUE_NAME: "same-queue", DEAD_LETTER_QUEUE_NAME: "same-queue" });
  refused({ ADMISSIONS_QUEUE_NAME: QUEUES.dead }); // equals the dead-letter default
  refused({ DEAD_LETTER_QUEUE_NAME: QUEUES.admissions }); // equals the admission default
  refused({ ADMISSIONS_QUEUE_NAME: "Review-Admission-Jobs", DEAD_LETTER_QUEUE_NAME: "review-admission-jobs" }); // case only
  refused({ ADMISSIONS_QUEUE_NAME: "review-admission-jobs ", DEAD_LETTER_QUEUE_NAME: "review-admission-jobs" }); // whitespace only
});

test("Q9 the stack's producer, consumers and dead-letter link are the resolver's names", () => {
  for (const vars of [{}, named(NAMES)]) {
    const names = queueNames(vars);
    const options = workerOptions({ vars, queue: { retryDelay: 1 } });
    assert.deepEqual(options.queueProducers, { [BINDINGS.queue]: names.admissions });
    assert.deepEqual(Object.keys(options.queueConsumers).sort(), [names.admissions, names.dead].sort());
    assert.equal(options.queueConsumers[names.admissions].deadLetterQueue, names.dead);
    assert.equal(options.queueConsumers[names.admissions].maxRetries, 2, "three delivery attempts");
    assert.equal(options.bindings, vars);
  }
  // The test-only Worker variables never move the topology.
  const split = workerOptions({ vars: named(NAMES), workerVars: { ADMISSIONS_QUEUE_NAME: "other-name" } });
  assert.deepEqual(split.queueProducers, { [BINDINGS.queue]: NAMES.admissions });
  assert.deepEqual(split.bindings, { ADMISSIONS_QUEUE_NAME: "other-name" });
  assert.throws(() => workerOptions({ vars: { DEAD_LETTER_QUEUE_NAME: QUEUES.admissions } }), ConfigInvalid);
});

test("Q9 the declared deployment topology and its variables are the code defaults", async () => {
  const toml = await readFile(path.join(PACKAGE_ROOT, "wrangler.toml"), "utf8");
  assert.match(toml, new RegExp(`binding = "${BINDINGS.queue}"\\nqueue = "${QUEUES.admissions}"`));
  assert.equal([...toml.matchAll(/^queue = "([^"]+)"$/gm)].map((m) => m[1]).sort().join(","), [QUEUES.admissions, QUEUES.admissions, QUEUES.dead].sort().join(","));
  assert.match(toml, new RegExp(`dead_letter_queue = "${QUEUES.dead}"`));
  assert.match(toml, new RegExp(`^ADMISSIONS_QUEUE_NAME = "${QUEUES.admissions}"$`, "m"));
  assert.match(toml, new RegExp(`^DEAD_LETTER_QUEUE_NAME = "${QUEUES.dead}"$`, "m"));
});

test("Q2 Q3 the local stack refuses invalid names before any engine starts or any state is written", async () => {
  const root = await mkdtemp(path.join(process.env.REPORT_CONTROL_TEST_ROOT ?? os.tmpdir(), "rcp-names-"));
  for (const vars of [{ ADMISSIONS_QUEUE_NAME: "Bad Name" }, { ADMISSIONS_QUEUE_NAME: "same", DEAD_LETTER_QUEUE_NAME: "same" }]) {
    await assert.rejects(
      startStack({ miniflareModule: miniflareModule(), persistDir: root, vars: { ...BASE, ...vars } }),
      (e) => e instanceof ConfigInvalid && e.message === "queue_names",
    );
  }
  assert.deepEqual(await readdir(root), [], "no persisted state was created");
});

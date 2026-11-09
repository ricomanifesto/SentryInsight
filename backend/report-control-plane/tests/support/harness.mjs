// Test harness: one local stack per test file (real local D1, R2 and Queue),
// the fake execution service, the durable fake publisher and synthetic tokens.
// Authoritative reads go to D1 and R2 through the binding API, the fakes'
// counters and the publisher's state file; never through the Worker's routes.

import { createHash, randomBytes } from "node:crypto";
import { mkdtemp, mkdir } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { startStack } from "../../local/stack.mjs";
import { startFakeExecution } from "./fake-execution.mjs";
import { readState, startPublisher } from "./durable-publisher.mjs";

const sha = (data) => createHash("sha256").update(data).digest("hex");
export const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
export const ADMISSION = "report-control-plane/admission/1";
export const BUNDLE = "report-control-plane/source-bundle/1";
export const BINDING = sha("synthetic binding one");
export const OTHER_BINDING = sha("synthetic binding two");

export function miniflareModule() {
  const value = process.env.MINIFLARE_MODULE;
  if (!value) throw new Error("set MINIFLARE_MODULE to the installed miniflare dist/src/index.js");
  return value;
}

export function article(n, content = `Synthetic article ${n} content.`) {
  return { title: `Synthetic article ${n}`, link: `https://example.test/articles/${n}`, source: "Example Source", content };
}

export function admission(sourceRevision, articles = [article(1)], extra = {}) {
  return { schema: ADMISSION, pipeline: "reports", policy_id: "standard", source_revision: sourceRevision, articles, ...extra };
}

function token() {
  return randomBytes(24).toString("hex");
}

// `omit` names variables to leave unset, such as an unconfigured dependency.
export async function setup({ vars = {}, testFaults = true, persistDir = null, queue = {}, omit = [] } = {}) {
  const root = await mkdtemp(path.join(process.env.REPORT_CONTROL_TEST_ROOT ?? os.tmpdir(), "rcp-"));
  const tokens = { manual: token(), event: token(), reader: token(), publisher: token(), operator: token(), exporter: token(), projector: token() };
  const principals = [
    { principal: "manual", roles: ["admit", "read"], token_sha256: sha(tokens.manual) },
    { principal: "event", roles: ["admit"], token_sha256: sha(tokens.event) },
    { principal: "reader", roles: ["read"], token_sha256: sha(tokens.reader) },
    { principal: "publisher", roles: ["publish", "read"], token_sha256: sha(tokens.publisher) },
    { principal: "operator", roles: ["operate", "read", "admit"], token_sha256: sha(tokens.operator) },
    { principal: "exporter", roles: ["export"], token_sha256: sha(tokens.exporter) },
    { principal: "projector", roles: ["project"], token_sha256: sha(tokens.projector) },
  ];
  const executionToken = token();
  const publisherToken = token();
  const execution = await startFakeExecution({ token: executionToken, bindings: [BINDING] });
  const publisherState = path.join(root, "publisher.json");
  const publisher = await startPublisher({ stateFile: publisherState, token: publisherToken });
  const persist = persistDir ?? path.join(root, "persist");
  await mkdir(persist, { recursive: true });
  const allVars = {
    AUTH_PRINCIPALS: JSON.stringify(principals),
    EXECUTION_URL: execution.url,
    EXECUTION_TOKEN: executionToken,
    PUBLISHER_URL: publisher.url,
    PUBLISHER_TOKEN: publisherToken,
    CALL_TIMEOUT_MS: "2000",
    CLAIM_MARGIN_MS: "500",
    SEND_BACKOFF_BASE_MS: "200",
    ENQUEUED_STALE_MS: "3000",
    PUBLICATION_CLAIM_MS: "1500",
    QUEUE_RETRY_DELAY_S: "1",
    ...vars,
  };
  for (const name of omit) delete allVars[name];
  // workerVars (tests only) are variables the Worker sees on top of allVars
  // while the topology still follows allVars; see workerOptions.
  const start = (workerVars) =>
    startStack({
      miniflareModule: miniflareModule(),
      persistDir: persist,
      vars: allVars,
      workerVars: workerVars && { ...allVars, ...workerVars },
      testFaults,
      queue: { retryDelay: 1, ...queue },
    });
  const env = { root, persist, tokens, execution, publisher, publisherState, stack: await start() };

  env.call = async (method, route, who, body, headers = {}) => {
    const init = { method, headers: { ...headers } };
    if (who) init.headers.authorization = `Bearer ${tokens[who] ?? who}`;
    if (body !== undefined) init.body = typeof body === "string" || body instanceof Uint8Array ? body : JSON.stringify(body);
    const response = await fetch(`${env.stack.url}${route}`, init);
    const text = await response.text();
    let value = null;
    try {
      value = JSON.parse(text);
    } catch {
      value = text;
    }
    return { status: response.status, body: value };
  };
  env.admit = (body, who = "manual") => env.call("POST", "/v1/operations", who, body);
  env.status = (id) => env.call("GET", `/v1/operations/${id}`, "reader");
  env.publish = (id, target = "site") => env.call("POST", `/v1/operations/${id}/publish`, "publisher", { target });
  env.reconcile = () => env.call("POST", "/v1/reconcile", "operator");
  env.exportPage = (after = 0, limit) =>
    env.call("GET", `/v1/export?after=${after}${limit === undefined ? "" : `&limit=${limit}`}`, "exporter");
  // Every page from a cursor, in order; the records and the final cursor.
  env.exportAll = async (after = 0, limit) => {
    const records = [];
    let cursor = after;
    for (let page = 0; page < 1000; page += 1) {
      const response = await env.exportPage(cursor, limit);
      if (response.status !== 200) throw new Error(`export ${response.status} ${JSON.stringify(response.body)}`);
      records.push(...response.body.records);
      cursor = response.body.next_cursor;
      if (!response.body.has_more) return { records, cursor };
    }
    throw new Error("export did not finish");
  };
  env.q = async (sql, ...params) => (await env.stack.db.prepare(sql).bind(...params).all()).results;
  env.one = async (sql, ...params) => (await env.q(sql, ...params))[0];
  env.r2 = async (prefix = "") => (await env.stack.bucket.list({ prefix })).objects.map((o) => ({ key: o.key, size: o.size }));
  env.fault = (point, remaining = 1, mode = "throw", delayMs = 0) =>
    env.stack.db
      .prepare(
        `INSERT INTO test_faults (point, remaining, mode, delay_ms) VALUES (?, ?, ?, ?)
         ON CONFLICT (point) DO UPDATE SET remaining = excluded.remaining, mode = excluded.mode, delay_ms = excluded.delay_ms`,
      )
      .bind(point, remaining, mode, delayMs)
      .run();
  env.publisherState = () => readState(publisherState);
  env.publisherControl = async (body) => {
    const response = await fetch(`${publisher.url}/__control`, {
      method: "POST",
      headers: { authorization: `Bearer ${publisherToken}` },
      body: JSON.stringify(body),
    });
    if (response.status !== 200) throw new Error(`publisher control ${response.status}`);
  };
  env.counts = async () => ({
    operations: (await env.one("SELECT count(*) AS n FROM operations")).n,
    max_seq: (await env.one("SELECT coalesce(max(seq), 0) AS n FROM operations")).n,
    snapshots: (await env.one("SELECT count(*) AS n FROM snapshots")).n,
    article_revisions: (await env.one("SELECT count(*) AS n FROM article_revisions")).n,
    operation_articles: (await env.one("SELECT count(*) AS n FROM operation_articles")).n,
    artifacts: (await env.one("SELECT count(*) AS n FROM artifacts")).n,
    r2: (await env.r2()).length,
    jobs: execution.jobCount(),
  });
  env.waitFor = async (check, { timeout = 15000, every = 100 } = {}) => {
    const deadline = Date.now() + timeout;
    for (;;) {
      const value = await check();
      if (value) return value;
      if (Date.now() > deadline) throw new Error("waitFor timed out");
      await sleep(every);
    }
  };
  env.row = (id) => env.one("SELECT * FROM operations WHERE operation_id = ?", id);
  env.waitState = (id, state, options) => env.waitFor(async () => ((await env.row(id))?.state === state ? env.row(id) : null), options);
  // Restart on the same persisted state, optionally with changed variables.
  env.restart = async (vars = {}, { workerVars } = {}) => {
    await env.stack.dispose();
    Object.assign(allVars, vars);
    env.stack = await start(workerVars);
  };
  env.stop = async () => {
    await env.stack.dispose();
    await execution.close();
    await publisher.close();
  };
  const seeded = await env.call("PUT", "/v1/pipelines/reports", "operator", { policy_id: "standard", binding_id: BINDING, state: "active" });
  if (seeded.status !== 200) throw new Error(`pipeline seed failed: ${seeded.status}`);
  return env;
}

// Admit and wait for the consumer to record the submission.
export async function admitted(env, body, who = "manual") {
  const response = await env.admit(body, who);
  if (![200, 201].includes(response.status)) throw new Error(`admission ${response.status} ${JSON.stringify(response.body)}`);
  const id = response.body.operation.operation_id;
  await env.waitState(id, "submitted");
  return id;
}

export const REPORT_FILES = {
  "index.html": "<html>synthetic report</html>\n",
  "reports/2026-01-01.md": "# Synthetic report\n",
  "reports/latest.json": "{\"latest\": true}\n",
};

// Drive one operation to completed with the given files.
export async function completed(env, body, files = REPORT_FILES, who = "manual") {
  const id = await admitted(env, body, who);
  env.execution.succeed(id, files);
  await env.reconcile();
  await env.waitState(id, "completed");
  return id;
}

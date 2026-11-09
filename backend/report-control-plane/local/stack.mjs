// Local stack on the installed Miniflare/workerd API: real local D1, R2 and
// Queue bindings, the cron handler, persistence under one directory and a
// numeric loopback listener. No account, remote binding or cf metadata fetch
// (cf is false). The Miniflare module path is supplied by the caller.

import { readdir, readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { QUEUES, queueNames } from "../src/config.js";

const here = path.dirname(fileURLToPath(import.meta.url));
export const PACKAGE_ROOT = path.resolve(here, "..");
const SOURCE = path.join(PACKAGE_ROOT, "src");
const MIGRATIONS = path.join(PACKAGE_ROOT, "migrations");

export const BINDINGS = { db: "PRODUCT_DB", artifacts: "ARTIFACTS", queue: "ADMISSIONS" };
// The default queue names, kept here for existing callers; the effective
// names always come from queueNames over the variables.
export { QUEUES };
export const COMPATIBILITY_DATE = "2025-06-01";

const TEST_FAULTS_TABLE = `CREATE TABLE IF NOT EXISTS test_faults (
  point TEXT PRIMARY KEY, remaining INTEGER NOT NULL, mode TEXT NOT NULL,
  delay_ms INTEGER NOT NULL DEFAULT 0, fired INTEGER NOT NULL DEFAULT 0)`;

export function splitSql(text) {
  return text
    .split("\n")
    .filter((line) => !line.trimStart().startsWith("--"))
    .join("\n")
    .split(/;\s*(?:\n|$)/)
    .map((s) => s.trim())
    .filter(Boolean);
}

// Apply each migration file once, atomically, recording it in d1_migrations.
export async function applyMigrations(db) {
  await db.exec("CREATE TABLE IF NOT EXISTS d1_migrations (name TEXT PRIMARY KEY, applied_at INTEGER NOT NULL)");
  const applied = new Set((await db.prepare("SELECT name FROM d1_migrations").all()).results.map((r) => r.name));
  const files = (await readdir(MIGRATIONS)).filter((f) => /^\d{4}_[a-z0-9_]+\.sql$/.test(f)).sort();
  const done = [];
  for (const file of files) {
    if (applied.has(file)) continue;
    const statements = splitSql(await readFile(path.join(MIGRATIONS, file), "utf8")).map((s) => db.prepare(s));
    statements.push(db.prepare("INSERT INTO d1_migrations (name, applied_at) VALUES (?, ?)").bind(file, Date.now()));
    await db.batch(statements);
    done.push(file);
  }
  return done;
}

// The topology follows the same resolver over the same variables the Worker
// reads, so the producer, the consumers, the dead-letter link and the
// handler's dispatch cannot drift apart. Invalid names refuse here, before an
// engine starts. `workerVars`, when given, replaces only the variables the
// Worker sees: tests use it to model a deployment whose declared queues and
// variables disagree; the runner never passes it.
export function workerOptions({ vars, queue = {}, workerVars = vars }) {
  const names = queueNames(vars);
  return {
    modules: true,
    modulesRoot: SOURCE,
    scriptPath: path.join(SOURCE, "index.js"),
    modulesRules: [{ type: "ESModule", include: ["**/*.js"] }],
    compatibilityDate: COMPATIBILITY_DATE,
    bindings: workerVars,
    d1Databases: { [BINDINGS.db]: "report-control-plane" },
    r2Buckets: [BINDINGS.artifacts],
    queueProducers: { [BINDINGS.queue]: names.admissions },
    queueConsumers: {
      [names.admissions]: {
        maxBatchSize: queue.maxBatchSize ?? 5,
        maxBatchTimeout: queue.maxBatchTimeout ?? 1,
        maxRetries: queue.maxRetries ?? 2,
        deadLetterQueue: names.dead,
        retryDelay: queue.retryDelay ?? 5,
      },
      [names.dead]: { maxBatchSize: 5, maxBatchTimeout: 1 },
    },
  };
}

export async function startStack({ miniflareModule, persistDir, port = 0, vars, workerVars, queue, testFaults = false, logLevel = "WARN" }) {
  const faults = testFaults ? { TEST_FAULTS: "enabled" } : {};
  const options = workerOptions({ vars: { ...vars, ...faults }, workerVars: workerVars && { ...workerVars, ...faults }, queue });
  const { Miniflare, Log, LogLevel } = await import(pathToFileURL(miniflareModule).href);
  const mf = new Miniflare({
    host: "127.0.0.1",
    port,
    cf: false,
    log: new Log(LogLevel[logLevel]),
    d1Persist: path.join(persistDir, "d1"),
    r2Persist: path.join(persistDir, "r2"),
    ...options,
  });
  const url = await mf.ready;
  const db = await mf.getD1Database(BINDINGS.db);
  const bucket = await mf.getR2Bucket(BINDINGS.artifacts);
  const migrations = await applyMigrations(db);
  if (testFaults) await db.exec(TEST_FAULTS_TABLE.replace(/\n\s*/g, " "));
  const worker = await mf.getWorker();
  return {
    url: url.href.replace(/\/$/, ""),
    mf,
    db,
    bucket,
    worker,
    migrations,
    queues: queueNames(vars),
    async dispose() {
      await mf.dispose();
    },
  };
}

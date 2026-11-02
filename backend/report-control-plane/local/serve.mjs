#!/usr/bin/env node
// Run the local stack as an owned child process, plus a loopback inspection
// endpoint that reads D1 and R2 through the binding API directly, never
// through the Worker's own routes. On SIGTERM or SIGINT the engine's own exit
// hook disposes the workerd runtime and exits with 128 + the signal number.
//
// Usage: node local/serve.mjs --config <file.json>
// The config names the Miniflare module, a persist directory, the variables
// file, the ports and the inspection token file; see local/config.example.json.

import { readFile, writeFile } from "node:fs/promises";
import { createServer } from "node:http";
import { createHash, timingSafeEqual } from "node:crypto";
import { startStack } from "./stack.mjs";

const READ_ONLY = /^\s*(SELECT|WITH)\b[^;]*$/is;
const KEYS = ["miniflare_module", "persist_dir", "port", "vars_file", "inspect_port", "inspect_token_file", "ready_file", "test_faults", "queue"];

function argument(name) {
  const at = process.argv.indexOf(name);
  return at === -1 ? null : process.argv[at + 1];
}

async function loadConfig(file) {
  const config = JSON.parse(await readFile(file, "utf8"));
  const unknown = Object.keys(config).filter((k) => !KEYS.includes(k));
  if (unknown.length) throw new Error(`unknown config keys: ${unknown.join(",")}`);
  for (const key of ["miniflare_module", "persist_dir", "vars_file", "inspect_token_file", "ready_file"]) {
    if (typeof config[key] !== "string" || !config[key].startsWith("/")) throw new Error(`${key} must be an absolute path`);
  }
  return config;
}

function readBody(request, limit = 1 << 20) {
  return new Promise((resolve, reject) => {
    const chunks = [];
    let total = 0;
    request.on("data", (chunk) => {
      total += chunk.length;
      if (total > limit) reject(new Error("too large"));
      else chunks.push(chunk);
    });
    request.on("end", () => resolve(Buffer.concat(chunks)));
    request.on("error", reject);
  });
}

function send(response, status, value) {
  const body = Buffer.isBuffer(value) ? value : Buffer.from(JSON.stringify(value));
  response.writeHead(status, { "content-type": Buffer.isBuffer(value) ? "application/octet-stream" : "application/json" });
  response.end(body);
}

async function main() {
  const config = await loadConfig(argument("--config"));
  const vars = JSON.parse(await readFile(config.vars_file, "utf8"));
  const tokenDigest = createHash("sha256").update((await readFile(config.inspect_token_file, "utf8")).trim()).digest();
  const stack = await startStack({
    miniflareModule: config.miniflare_module,
    persistDir: config.persist_dir,
    port: config.port ?? 0,
    vars,
    queue: config.queue,
    testFaults: config.test_faults === true,
  });

  const inspect = createServer(async (request, response) => {
    try {
      const presented = /^Bearer (\S+)$/.exec(request.headers.authorization ?? "")?.[1] ?? "";
      const digest = createHash("sha256").update(presented).digest();
      if (!timingSafeEqual(digest, tokenDigest)) return send(response, 401, { error: "unauthenticated" });
      const url = new URL(request.url, "http://127.0.0.1");
      if (request.method === "POST" && url.pathname === "/sql") {
        const { sql, params = [] } = JSON.parse(await readBody(request));
        if (!READ_ONLY.test(sql)) return send(response, 400, { error: "read_only" });
        const { results } = await stack.db.prepare(sql).bind(...params).all();
        return send(response, 200, { results });
      }
      if (request.method === "GET" && url.pathname === "/r2") {
        const prefix = url.searchParams.get("prefix") ?? "";
        const objects = [];
        let cursor;
        do {
          const page = await stack.bucket.list({ prefix, cursor });
          for (const o of page.objects) {
            const head = await stack.bucket.head(o.key);
            const sha = head?.checksums?.sha256 ? Buffer.from(head.checksums.sha256).toString("hex") : null;
            objects.push({ key: o.key, size: o.size, sha256: sha });
          }
          cursor = page.truncated ? page.cursor : undefined;
        } while (cursor);
        return send(response, 200, { objects });
      }
      if (request.method === "GET" && url.pathname === "/r2/object") {
        const object = await stack.bucket.get(url.searchParams.get("key") ?? "");
        if (object === null) return send(response, 404, { error: "not_found" });
        return send(response, 200, Buffer.from(await object.arrayBuffer()));
      }
      if (request.method === "POST" && url.pathname === "/scheduled") {
        const result = await stack.worker.scheduled({ cron: "*/5 * * * *" });
        return send(response, 200, { outcome: result.outcome });
      }
      if (request.method === "POST" && url.pathname === "/queue-dispatch") {
        const { queue, messages } = JSON.parse(await readBody(request));
        // Only the stack's effective queue names are dispatched.
        if (!Object.values(stack.queues).includes(queue)) return send(response, 400, { error: "queue" });
        const result = await stack.worker.queue(
          queue,
          messages.map((m, i) => ({ id: m.id ?? `dispatch-${Date.now()}-${i}`, timestamp: new Date(), body: m.body, attempts: m.attempts ?? 1 })),
        );
        return send(response, 200, {
          outcome: result.outcome,
          ackAll: result.ackAll,
          retryBatch: result.retryBatch,
          explicitAcks: result.explicitAcks,
          retryMessages: result.retryMessages,
        });
      }
      if (request.method === "POST" && url.pathname === "/faults" && config.test_faults === true) {
        const { point, remaining, mode = "throw", delay_ms = 0 } = JSON.parse(await readBody(request));
        await stack.db
          .prepare(
            `INSERT INTO test_faults (point, remaining, mode, delay_ms) VALUES (?, ?, ?, ?)
             ON CONFLICT (point) DO UPDATE SET remaining = excluded.remaining, mode = excluded.mode, delay_ms = excluded.delay_ms`,
          )
          .bind(point, remaining, mode, delay_ms)
          .run();
        return send(response, 200, { point, remaining });
      }
      return send(response, 404, { error: "not_found" });
    } catch (error) {
      return send(response, 500, { error: "inspect_failed", detail: String(error.message ?? error).slice(0, 200) });
    }
  });
  await new Promise((resolve) => inspect.listen(config.inspect_port ?? 0, "127.0.0.1", resolve));

  let stopping = false;
  const stop = async () => {
    if (stopping) return;
    stopping = true;
    inspect.close();
    await stack.dispose();
    process.exit(0);
  };
  process.on("SIGTERM", stop);
  process.on("SIGINT", stop);

  const ready = {
    url: stack.url,
    inspect_url: `http://127.0.0.1:${inspect.address().port}`,
    pid: process.pid,
    migrations: stack.migrations,
    queues: stack.queues,
  };
  await writeFile(config.ready_file, JSON.stringify(ready));
  process.stdout.write(`${JSON.stringify(ready)}\n`);
}

main().catch((error) => {
  process.stderr.write(`serve failed: ${String(error.message ?? error)}\n`);
  process.exit(1);
});

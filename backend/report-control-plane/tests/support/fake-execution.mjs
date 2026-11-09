// In-process fake execution service implementing the public contract.
//
// Admission is idempotent per operation and binding, and converges on one job
// for byte-identical article records under one binding, so overlapping or
// repeated submissions create at most one job. Tests drive outcomes and
// faults directly and read counters from this object, never via the Worker.

import { createHash } from "node:crypto";
import { createServer } from "node:http";

const sha = (data) => createHash("sha256").update(data).digest("hex");
const SCHEMA = "execution-receipt/1";

// The execution side's file order: by path segments.
export function segmentOrder(a, b) {
  const x = a.split("/");
  const y = b.split("/");
  for (let i = 0; i < Math.min(x.length, y.length); i += 1) if (x[i] !== y[i]) return x[i] < y[i] ? -1 : 1;
  return x.length - y.length;
}

export function artifactOf(files) {
  const list = Object.entries(files)
    .map(([path, bytes]) => ({ path, sha256: sha(bytes), bytes: Buffer.byteLength(bytes) }))
    .sort((a, b) => segmentOrder(a.path, b.path));
  const digest = sha(list.map((f) => `${f.path}\0${f.sha256}\n`).join(""));
  return {
    accepted_output_sha256: digest,
    sha256: digest,
    file_count: list.length,
    total_bytes: list.reduce((n, f) => n + f.bytes, 0),
    files: list,
  };
}

function readAll(request) {
  return new Promise((resolve, reject) => {
    const chunks = [];
    request.on("data", (c) => chunks.push(c));
    request.on("end", () => resolve(Buffer.concat(chunks)));
    request.on("error", reject);
  });
}

export async function startFakeExecution({ token, bindings }) {
  const digest = sha(token);
  const served = new Set(bindings);
  const jobs = new Map(); // job key -> job
  const operations = new Map(); // operation id -> job key
  const counters = { submits: 0, jobsCreated: 0, receiptReads: 0, partReads: 0, rebuilt: 0 };
  const received = new Map(); // snapshot sha256 -> bytes, kept apart from the mapping
  const plan = { holdSubmitMs: [], dropSubmitResponses: 0, submitStatus: [] };

  const server = createServer(async (request, response) => {
    const presented = /^Bearer (\S+)$/.exec(request.headers.authorization ?? "")?.[1] ?? "";
    if (sha(presented) !== digest) {
      response.writeHead(401, { "content-type": "application/json" });
      return response.end(JSON.stringify({ reason: "unauthenticated" }));
    }
    const url = new URL(request.url, "http://127.0.0.1");
    const reply = (status, value) => {
      response.writeHead(status, { "content-type": "application/json" });
      response.end(JSON.stringify(value));
    };
    if (request.method === "POST" && url.pathname === "/executions") {
      counters.submits += 1;
      const bytes = await readAll(request);
      const operationId = request.headers["x-operation-id"];
      const binding = request.headers["x-binding-id"];
      if (sha(bytes) !== request.headers["x-snapshot-sha256"]) return reply(422, { reason: "snapshot_invalid", terminal: true });
      if (!served.has(binding)) return reply(409, { reason: "binding_mismatch", terminal: true });
      const scripted = plan.submitStatus.shift();
      if (scripted) return reply(scripted, { reason: "unavailable" });
      const hold = plan.holdSubmitMs.shift();
      if (hold) await new Promise((r) => setTimeout(r, hold));
      received.set(sha(bytes), bytes);
      const snapshot = JSON.parse(bytes.toString("utf8"));
      const articles = snapshot.articles.map((a) => ({ article_key: a.link, content_sha256: sha(a.content) }));
      const key = sha(`${binding}\n${JSON.stringify(snapshot.articles)}`);
      if (!jobs.has(key)) {
        counters.jobsCreated += 1;
        jobs.set(key, {
          execution_id: `exec-${key.slice(0, 24)}`,
          run_id: `run-${key.slice(24, 48)}`,
          binding_id: binding,
          state: "queued",
          reason: null,
          attempts: { used: 0, limit: 3 },
          budget: { reserved: 0, limit: 3 },
          admitted: articles.length,
          executed: articles,
          artifact: null,
          files: {},
        });
      }
      operations.set(operationId, key);
      const job = jobs.get(key);
      if (plan.dropSubmitResponses > 0) {
        plan.dropSubmitResponses -= 1;
        request.socket.destroy();
        return;
      }
      return reply(201, { operation_id: operationId, execution_id: job.execution_id, run_id: job.run_id, binding_id: binding, state: job.state });
    }
    const status = /^\/executions\/([0-9a-f]{64})$/.exec(url.pathname);
    if (request.method === "GET" && status) {
      counters.receiptReads += 1;
      // A lost mapping is rebuilt from the identities the caller sends, never
      // by creating a job.
      const snapshotSha = request.headers["x-snapshot-sha256"];
      const binding = request.headers["x-binding-id"];
      if (!operations.has(status[1]) && received.has(snapshotSha) && served.has(binding)) {
        const articles = JSON.parse(received.get(snapshotSha).toString("utf8")).articles;
        const key = sha(`${binding}\n${JSON.stringify(articles)}`);
        if (jobs.has(key)) {
          operations.set(status[1], key);
          counters.rebuilt += 1;
        }
      }
      const key = operations.get(status[1]);
      if (!key) return reply(404, { reason: "unknown" });
      const job = jobs.get(key);
      if (job.rawReceipt) {
        response.writeHead(200, { "content-type": "application/json" });
        return response.end(job.rawReceipt);
      }
      return reply(200, {
        schema: SCHEMA,
        operation_id: status[1],
        execution_id: job.execution_id,
        binding_id: job.binding_id,
        state: job.state,
        reason: job.reason,
        attempts: job.attempts,
        budget: job.budget,
        articles: { admitted_count: job.admitted, executed: job.executed },
        artifact: job.artifact,
      });
    }
    const part = /^\/executions\/([0-9a-f]{64})\/artifact\/(.+)$/.exec(url.pathname);
    if (request.method === "GET" && part) {
      counters.partReads += 1;
      const key = operations.get(part[1]);
      const path = part[2].split("/").map(decodeURIComponent).join("/");
      const job = key ? jobs.get(key) : null;
      if (!job || !(path in job.files)) return reply(404, { reason: "missing" });
      response.writeHead(200, { "content-type": "application/octet-stream" });
      return response.end(job.files[path]);
    }
    reply(404, { reason: "not_found" });
  });
  await new Promise((resolve) => server.listen(0, "127.0.0.1", resolve));

  return {
    url: `http://127.0.0.1:${server.address().port}`,
    counters,
    plan,
    served,
    jobFor(operationId) {
      return jobs.get(operations.get(operationId));
    },
    jobCount: () => jobs.size,
    loseMapping(operationId) {
      operations.delete(operationId);
    },
    // Report success with these files; ``mutate`` may alter the receipt's
    // artifact or the served bytes to model a wrong or stale artifact.
    succeed(operationId, files, mutate) {
      const job = this.jobFor(operationId);
      job.state = "succeeded";
      job.attempts = { used: 1, limit: 3 };
      job.budget = { reserved: 1, limit: 3 };
      job.files = { ...files };
      job.artifact = artifactOf(files);
      if (mutate) mutate(job);
    },
    fail(operationId, reason) {
      const job = this.jobFor(operationId);
      job.state = "failed";
      job.reason = reason;
    },
    close: () => new Promise((resolve) => server.close(resolve)),
  };
}

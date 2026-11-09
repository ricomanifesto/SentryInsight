#!/usr/bin/env node
// Durable fake publisher implementing the publisher contract.
//
// State lives in one JSON file replaced atomically, and every effect is
// applied under one in-process lock: an effect applies only when no receipt
// exists for the publication, the caller's expected remote version equals the
// target's current version, and the candidate sequence is greater than the
// target's current one. Otherwise the existing receipt is returned (no effect)
// or 409 (no effect). Test controls can drop the acknowledgement after an
// effect or hold a request before it is applied. Effect counts and receipts
// are read from the state file, never through the caller.
//
// Usage: node durable-publisher.mjs --state <file> --token-file <file> --ready-file <file> [--port N]

import { createHash, timingSafeEqual } from "node:crypto";
import { readFile, rename, writeFile } from "node:fs/promises";
import { createServer } from "node:http";
import { pathToFileURL } from "node:url";

const EMPTY = { targets: {}, receipts: {}, effects: [], controls: { drop_ack: [], hold_ms: {} } };
const PUBLICATION = /^\/publications\/([0-9a-f]{64})$/;

export async function readState(file) {
  try {
    return JSON.parse(await readFile(file, "utf8"));
  } catch (error) {
    if (error.code === "ENOENT") return structuredClone(EMPTY);
    throw error;
  }
}

async function writeState(file, state) {
  const temporary = `${file}.${process.pid}.tmp`;
  await writeFile(temporary, JSON.stringify(state, null, 1));
  await rename(temporary, file);
}

function body(request, limit = 16 * 1024) {
  return new Promise((resolve, reject) => {
    const chunks = [];
    let total = 0;
    request.on("data", (c) => {
      total += c.length;
      if (total > limit) reject(new Error("too large"));
      else chunks.push(c);
    });
    request.on("end", () => resolve(Buffer.concat(chunks).toString("utf8")));
    request.on("error", reject);
  });
}

function reply(response, status, value) {
  response.writeHead(status, { "content-type": "application/json" });
  response.end(JSON.stringify(value));
}

export async function startPublisher({ stateFile, token, port = 0 }) {
  const digest = createHash("sha256").update(token).digest();
  let chain = Promise.resolve();
  const locked = (work) => {
    const next = chain.then(work, work);
    chain = next.catch(() => {});
    return next;
  };

  const server = createServer(async (request, response) => {
    try {
      const presented = /^Bearer (\S+)$/.exec(request.headers.authorization ?? "")?.[1] ?? "";
      if (!timingSafeEqual(createHash("sha256").update(presented).digest(), digest)) {
        return reply(response, 401, { error: "unauthenticated" });
      }
      const url = new URL(request.url, "http://127.0.0.1");
      if (url.pathname === "/__state" && request.method === "GET") return reply(response, 200, await readState(stateFile));
      if (url.pathname === "/__control" && request.method === "POST") {
        const control = JSON.parse(await body(request));
        await locked(async () => {
          const state = await readState(stateFile);
          if (Array.isArray(control.drop_ack)) state.controls.drop_ack.push(...control.drop_ack);
          if (control.hold_ms && typeof control.hold_ms === "object") Object.assign(state.controls.hold_ms, control.hold_ms);
          await writeState(stateFile, state);
        });
        return reply(response, 200, { ok: true });
      }
      const match = PUBLICATION.exec(url.pathname);
      if (match === null) return reply(response, 404, { error: "not_found" });
      const id = match[1];
      if (request.method === "GET") {
        const state = await readState(stateFile);
        return state.receipts[id] ? reply(response, 200, state.receipts[id]) : reply(response, 404, { error: "not_found" });
      }
      if (request.method !== "POST") return reply(response, 405, { error: "method_not_allowed" });
      const value = JSON.parse(await body(request));
      const { target, artifact_sha256: artifact, expected_remote: expected, candidate_seq: seq } = value;
      if (
        typeof target !== "string" ||
        !/^[0-9a-f]{64}$/.test(artifact ?? "") ||
        !Number.isInteger(expected) ||
        !Number.isInteger(seq) ||
        Object.keys(value).length !== 4
      ) {
        return reply(response, 400, { error: "invalid" });
      }
      // A hold delays this request before its effect is attempted; it is
      // consumed by the request it delays.
      const hold = await locked(async () => {
        const state = await readState(stateFile);
        const ms = state.controls.hold_ms[id];
        if (ms) {
          delete state.controls.hold_ms[id];
          await writeState(stateFile, state);
        }
        return ms;
      });
      if (hold) await new Promise((r) => setTimeout(r, hold));
      const outcome = await locked(async () => {
        const state = await readState(stateFile);
        if (state.receipts[id]) return { status: 200, receipt: state.receipts[id], effect: false };
        const remote = state.targets[target] ?? { version: 0, candidate_seq: 0, publication_id: null, artifact_sha256: null };
        if (remote.version !== expected) return { status: 409, error: "remote_changed" };
        if (seq <= remote.candidate_seq) return { status: 409, error: "stale_candidate" };
        const receipt = {
          publication_id: id,
          receipt_id: `receipt-${id.slice(0, 24)}`,
          target,
          artifact_sha256: artifact,
          remote_version: remote.version + 1,
          candidate_seq: seq,
        };
        state.targets[target] = { version: remote.version + 1, candidate_seq: seq, publication_id: id, artifact_sha256: artifact };
        state.receipts[id] = receipt;
        state.effects.push({ publication_id: id, target, artifact_sha256: artifact, remote_version: remote.version + 1, at: Date.now() });
        const drop = state.controls.drop_ack.indexOf(id);
        if (drop !== -1) state.controls.drop_ack.splice(drop, 1);
        await writeState(stateFile, state);
        return { status: 201, receipt, effect: true, dropAck: drop !== -1 };
      });
      if (outcome.dropAck) {
        request.socket.destroy();
        return;
      }
      if (outcome.error) return reply(response, outcome.status, { error: outcome.error });
      return reply(response, outcome.status, outcome.receipt);
    } catch {
      return reply(response, 500, { error: "publisher_error" });
    }
  });
  await new Promise((resolve) => server.listen(port, "127.0.0.1", resolve));
  return {
    url: `http://127.0.0.1:${server.address().port}`,
    close: () => new Promise((resolve) => server.close(resolve)),
  };
}

async function main() {
  const arg = (name) => {
    const at = process.argv.indexOf(name);
    return at === -1 ? null : process.argv[at + 1];
  };
  const token = (await readFile(arg("--token-file"), "utf8")).trim();
  const publisher = await startPublisher({ stateFile: arg("--state"), token, port: Number(arg("--port") ?? 0) });
  const ready = { url: publisher.url, pid: process.pid };
  await writeFile(arg("--ready-file"), JSON.stringify(ready));
  const stop = async () => {
    await publisher.close();
    process.exit(0);
  };
  process.on("SIGTERM", stop);
  process.on("SIGINT", stop);
}

if (import.meta.url === pathToFileURL(process.argv[1]).href) {
  main().catch((error) => {
    process.stderr.write(`publisher failed: ${String(error.message ?? error)}\n`);
    process.exit(1);
  });
}

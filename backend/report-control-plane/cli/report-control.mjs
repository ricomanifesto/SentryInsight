#!/usr/bin/env node
// Command-line client for the report control plane's product API.
//
// Environment: REPORT_CONTROL_URL (the Worker's base URL) and
// REPORT_CONTROL_TOKEN_FILE (a file holding one bearer token). Output is JSON.
//
//   admit <request.json>                     submit an admission request
//   status <operation_id>                    sanitized operation status
//   publish <operation_id> <target>          publish a completed operation
//   retry <operation_id>                     manual retry from dead_letter
//   reconcile                                run the sweeper once
//   target <target>                          last-good publication
//   artifact <artifact_sha256> <out_dir>     download and verify an accepted artifact
//   stage <schedule_id> <bundle.json>        stage a source bundle
//   set-pipeline <pipeline> <policy> <binding_id> <active|retired>
//   set-schedule <schedule_id> <pipeline> <policy> <active|paused>

import { createHash } from "node:crypto";
import { mkdir, readFile, writeFile } from "node:fs/promises";
import path from "node:path";

const sha = (data) => createHash("sha256").update(data).digest("hex");
const SEGMENT = /^[A-Za-z0-9._-]+$/;

function fail(message, code = 2) {
  process.stderr.write(`${JSON.stringify({ error: message })}\n`);
  process.exit(code);
}

async function client() {
  const base = process.env.REPORT_CONTROL_URL;
  const tokenFile = process.env.REPORT_CONTROL_TOKEN_FILE;
  if (!base || !tokenFile) fail("set REPORT_CONTROL_URL and REPORT_CONTROL_TOKEN_FILE");
  const token = (await readFile(tokenFile, "utf8")).trim();
  return async (method, route, body) => {
    const response = await fetch(`${base.replace(/\/$/, "")}${route}`, {
      method,
      headers: { authorization: `Bearer ${token}` },
      body,
      signal: AbortSignal.timeout(60_000),
    });
    return response;
  };
}

async function printJson(response) {
  const text = await response.text();
  process.stdout.write(`${text}\n`);
  return response.status < 400 ? 0 : 1;
}

function safePath(relative) {
  const segments = relative.split("/");
  if (relative.length > 200 || !segments.every((s) => SEGMENT.test(s) && s !== "." && s !== "..")) fail("unsafe artifact path");
  return segments;
}

// Download every listed file, verify each digest and the artifact digest,
// then write the files under out_dir/<artifact_sha256>/.
async function artifact(call, sha256, outDir) {
  if (!/^[0-9a-f]{64}$/.test(sha256)) fail("artifact id must be 64 lowercase hex characters");
  const manifestResponse = await call("GET", `/v1/artifacts/${sha256}`);
  if (manifestResponse.status !== 200) return printJson(manifestResponse);
  const manifest = await manifestResponse.json();
  const files = [];
  for (const entry of manifest.files) {
    const segments = safePath(entry.path);
    const response = await call("GET", `/v1/artifacts/${sha256}/files/${segments.map(encodeURIComponent).join("/")}`);
    if (response.status !== 200) fail(`missing ${entry.path}`, 1);
    const bytes = Buffer.from(await response.arrayBuffer());
    if (bytes.length !== entry.bytes || sha(bytes) !== entry.sha256) fail(`digest mismatch ${entry.path}`, 1);
    files.push({ entry, segments, bytes });
  }
  const digest = sha(manifest.files.map((f) => `${f.path}\0${f.sha256}\n`).join(""));
  if (digest !== sha256 || manifest.artifact_sha256 !== sha256) fail("artifact digest mismatch", 1);
  const root = path.resolve(outDir, sha256);
  for (const { segments, bytes } of files) {
    const target = path.join(root, ...segments);
    if (!target.startsWith(root + path.sep)) fail("unsafe artifact path");
    await mkdir(path.dirname(target), { recursive: true });
    await writeFile(target, bytes);
  }
  process.stdout.write(`${JSON.stringify({ artifact_sha256: sha256, verified: true, files: files.length, directory: root })}\n`);
  return 0;
}

async function main() {
  const [command, ...args] = process.argv.slice(2);
  const call = await client();
  const json = (value) => JSON.stringify(value);
  switch (command) {
    case "admit":
      return printJson(await call("POST", "/v1/operations", await readFile(args[0])));
    case "status":
      return printJson(await call("GET", `/v1/operations/${args[0]}`));
    case "publish":
      return printJson(await call("POST", `/v1/operations/${args[0]}/publish`, json({ target: args[1] })));
    case "retry":
      return printJson(await call("POST", `/v1/operations/${args[0]}/retry`));
    case "reconcile":
      return printJson(await call("POST", "/v1/reconcile"));
    case "target":
      return printJson(await call("GET", `/v1/targets/${args[0]}`));
    case "artifact":
      return artifact(call, args[0], args[1]);
    case "stage":
      return printJson(await call("PUT", `/v1/schedules/${args[0]}/sources`, await readFile(args[1])));
    case "set-pipeline":
      return printJson(await call("PUT", `/v1/pipelines/${args[0]}`, json({ policy_id: args[1], binding_id: args[2], state: args[3] })));
    case "set-schedule":
      return printJson(await call("PUT", `/v1/schedules/${args[0]}`, json({ pipeline: args[1], policy_id: args[2], state: args[3] })));
    default:
      fail("unknown command; see the header of cli/report-control.mjs");
  }
  return 2;
}

main().then(
  (code) => process.exit(code),
  (error) => fail(String(error.message ?? error), 1),
);

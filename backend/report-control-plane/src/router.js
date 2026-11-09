// HTTP routes. Authentication and request validation run before any binding
// call; refusals carry fixed reason tokens.

import { admit, putImmutable } from "./admission.js";
import { authenticate } from "./auth.js";
import { ConfigInvalid, LIMITS, settings as readSettings } from "./config.js";
import { now, operation, record } from "./db.js";
import { manualRetry } from "./delivery.js";
import { ExportRefused, exportPage, parseExportQuery, retainedSource } from "./export.js";
import { HEX64, TOKEN, pathSegments } from "./identity.js";
import { publish, targetView } from "./publication.js";
import { RequestRefused, parseAdmission, parseBundle } from "./request.js";
import { operationStatus } from "./status.js";
import { reconcile } from "./sweeper.js";
import { JsonRefused, decodeStrictJson } from "./strict-json.js";
import { TooLarge, json, readBounded, refusal, sha256Hex } from "./util.js";

const ROUTES = [
  ["POST", /^\/v1\/operations$/, "admit", admitRoute],
  ["GET", /^\/v1\/operations\/([0-9a-f]{64})$/, "read", statusRoute],
  ["POST", /^\/v1\/operations\/([0-9a-f]{64})\/publish$/, "publish", publishRoute],
  ["POST", /^\/v1\/operations\/([0-9a-f]{64})\/retry$/, "admit", retryRoute],
  ["POST", /^\/v1\/reconcile$/, "operate", reconcileRoute],
  ["GET", /^\/v1\/targets\/([a-z0-9][a-z0-9._-]{0,63})$/, "read", targetRoute],
  ["GET", /^\/v1\/artifacts\/([0-9a-f]{64})$/, "read", manifestRoute],
  ["GET", /^\/v1\/artifacts\/([0-9a-f]{64})\/files\/(.+)$/, "read", artifactFileRoute],
  ["PUT", /^\/v1\/pipelines\/([a-z0-9][a-z0-9._-]{0,63})$/, "operate", pipelineRoute],
  ["PUT", /^\/v1\/schedules\/([a-z0-9][a-z0-9._-]{0,63})$/, "operate", scheduleRoute],
  ["PUT", /^\/v1\/schedules\/([a-z0-9][a-z0-9._-]{0,63})\/sources$/, "admit", sourcesRoute],
  ["GET", /^\/v1\/export$/, "export", exportRoute],
  ["GET", /^\/v1\/export\/sources\/([0-9a-f]{64})\/(0|[1-9][0-9]{0,2})$/, "export", exportSourceRoute],
];

async function exportRoute({ request, env }) {
  let query;
  try {
    query = parseExportQuery(new URL(request.url).search);
  } catch (error) {
    if (error instanceof ExportRefused) throw new RequestRefused(error.reason);
    throw error;
  }
  return json(200, await exportPage(env.PRODUCT_DB, query));
}

async function exportSourceRoute({ env, match }) {
  const outcome = await retainedSource(env, match[1], Number(match[2]));
  return json(outcome.status, outcome.body);
}

async function body(request) {
  return readBounded(request.body, LIMITS.bodyBytes);
}

async function smallJson(request, keys) {
  let value;
  try {
    value = decodeStrictJson(await readBounded(request.body, 4096));
  } catch (error) {
    if (error instanceof JsonRefused || error instanceof TooLarge) throw new RequestRefused("request_malformed");
    throw error;
  }
  if (value === null || typeof value !== "object" || Array.isArray(value) || Object.keys(value).sort().join(",") !== [...keys].sort().join(",")) {
    throw new RequestRefused("request_malformed");
  }
  return value;
}

async function admitRoute({ request, env, settings, principal }) {
  const bytes = await body(request);
  const parsed = await parseAdmission(bytes);
  const outcome = await admit(env, settings, { ...parsed, principal, bytes, fingerprint: await sha256Hex(bytes) });
  if (outcome.operation) return json(outcome.status, await operationStatus(env.PRODUCT_DB, outcome.operation));
  return json(outcome.status, outcome.body);
}

async function statusRoute({ env, match }) {
  const row = await operation(env.PRODUCT_DB, match[1]);
  if (row === null) return refusal(404, "not_found");
  return json(200, await operationStatus(env.PRODUCT_DB, row));
}

async function publishRoute({ request, env, settings, match }) {
  const { target } = await smallJson(request, ["target"]);
  if (typeof target !== "string" || !TOKEN.test(target)) throw new RequestRefused("target_invalid");
  const row = await operation(env.PRODUCT_DB, match[1]);
  if (row === null) return refusal(404, "not_found");
  const outcome = await publish(env, settings, row, target);
  return json(outcome.status, outcome.body);
}

async function retryRoute({ env, settings, match }) {
  const outcome = await manualRetry(env, settings, match[1]);
  if (outcome.operation) return json(outcome.status, await operationStatus(env.PRODUCT_DB, outcome.operation));
  return json(outcome.status, outcome.body);
}

async function reconcileRoute({ env, settings }) {
  return json(200, { counts: await reconcile(env, settings, "manual") });
}

async function targetRoute({ env, match }) {
  const row = await env.PRODUCT_DB.prepare("SELECT * FROM targets WHERE target = ?").bind(match[1]).first();
  if (row === null) return refusal(404, "not_found");
  return json(200, { target: targetView(row) });
}

async function verifiedArtifact(env, sha) {
  return env.PRODUCT_DB.prepare("SELECT * FROM artifacts WHERE artifact_sha256 = ?").bind(sha).first();
}

async function manifestRoute({ env, match }) {
  if ((await verifiedArtifact(env, match[1])) === null) return refusal(404, "not_found");
  const object = await env.ARTIFACTS.get(`artifacts/${match[1]}/manifest.json`);
  if (object === null) return refusal(404, "not_found");
  return new Response(object.body, { headers: { "content-type": "application/json", "cache-control": "no-store" } });
}

async function artifactFileRoute({ env, match }) {
  let path;
  try {
    path = decodeURIComponent(match[2]);
  } catch {
    return refusal(404, "not_found");
  }
  if (pathSegments(path) === null || (await verifiedArtifact(env, match[1])) === null) return refusal(404, "not_found");
  const object = await env.ARTIFACTS.get(`artifacts/${match[1]}/files/${path}`);
  if (object === null) return refusal(404, "not_found");
  return new Response(object.body, {
    headers: { "content-type": "application/octet-stream", "cache-control": "no-store", "x-content-sha256": object.checksums.sha256 ? [...new Uint8Array(object.checksums.sha256)].map((b) => b.toString(16).padStart(2, "0")).join("") : "" },
  });
}

async function pipelineRoute({ request, env, match, principal }) {
  const value = await smallJson(request, ["policy_id", "binding_id", "state"]);
  if (!TOKEN.test(value.policy_id ?? "") || !HEX64.test(value.binding_id ?? "") || !["active", "retired"].includes(value.state)) {
    throw new RequestRefused("pipeline_invalid");
  }
  const at = now();
  await env.PRODUCT_DB.batch([
    env.PRODUCT_DB
      .prepare(
        `INSERT INTO pipelines (pipeline, policy_id, binding_id, state, updated_at) VALUES (?, ?, ?, ?, ?)
         ON CONFLICT (pipeline) DO UPDATE SET policy_id = excluded.policy_id, binding_id = excluded.binding_id,
           state = excluded.state, updated_at = excluded.updated_at`,
      )
      .bind(match[1], value.policy_id, value.binding_id, value.state, at),
    env.PRODUCT_DB
      .prepare("INSERT INTO events (subject, kind, token, detail, at) VALUES (?, 'pipeline_set', ?, ?, ?)")
      .bind(match[1], value.state, JSON.stringify({ binding_id: value.binding_id, by: principal }), at),
  ]);
  return json(200, { pipeline: match[1], ...value });
}

async function scheduleRoute({ request, env, match }) {
  const value = await smallJson(request, ["pipeline", "policy_id", "state"]);
  if (!TOKEN.test(value.pipeline ?? "") || !TOKEN.test(value.policy_id ?? "") || !["active", "paused"].includes(value.state)) {
    throw new RequestRefused("schedule_invalid");
  }
  await env.PRODUCT_DB
    .prepare(
      `INSERT INTO schedules (schedule_id, pipeline, policy_id, state, updated_at) VALUES (?, ?, ?, ?, ?)
       ON CONFLICT (schedule_id) DO UPDATE SET pipeline = excluded.pipeline, policy_id = excluded.policy_id,
         state = excluded.state, updated_at = excluded.updated_at`,
    )
    .bind(match[1], value.pipeline, value.policy_id, value.state, now())
    .run();
  return json(200, { schedule_id: match[1], ...value });
}

// Stage a source bundle for the next scheduled admission. The bundle is a
// local stand-in for an upstream digest; nothing is fetched.
async function sourcesRoute({ request, env, match }) {
  const bytes = await body(request);
  await parseBundle(bytes);
  const fingerprint = await sha256Hex(bytes);
  const schedule = await env.PRODUCT_DB.prepare("SELECT schedule_id FROM schedules WHERE schedule_id = ?").bind(match[1]).first();
  if (schedule === null) return refusal(404, "not_found");
  await putImmutable(env.ARTIFACTS, `snapshots/${fingerprint}`, bytes, fingerprint);
  await env.PRODUCT_DB
    .prepare("UPDATE schedules SET pending_bundle_sha256 = ?, updated_at = ? WHERE schedule_id = ?")
    .bind(fingerprint, now(), match[1])
    .run();
  await record(env.PRODUCT_DB, { subject: match[1], kind: "schedule_staged", token: null, detail: { bundle: fingerprint }, at: now() });
  return json(202, { schedule_id: match[1], pending_bundle_sha256: fingerprint });
}

export async function route(request, env) {
  const url = new URL(request.url);
  if (url.pathname === "/healthz" && request.method === "GET") return json(200, { status: "ok" });
  const found = ROUTES.find(([method, pattern]) => method === request.method && pattern.test(url.pathname));
  if (!found) {
    const known = ROUTES.some(([, pattern]) => pattern.test(url.pathname));
    return refusal(known ? 405 : 404, known ? "method_not_allowed" : "not_found");
  }
  const [, pattern, role, handler] = found;
  try {
    const auth = await authenticate(request, env, role);
    if (auth.status) return refusal(auth.status, auth.reason);
    const settings = readSettings(env);
    return await handler({ request, env, settings, principal: auth.principal, match: pattern.exec(url.pathname) });
  } catch (error) {
    if (error instanceof ConfigInvalid) return refusal(503, "config_invalid");
    if (error instanceof RequestRefused) return refusal(422, error.reason);
    if (error instanceof TooLarge) return refusal(413, "request_too_large");
    throw error;
  }
}

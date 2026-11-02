// Client for the generic execution service. Every call carries a bearer token
// and a deadline; every response is bounded and parsed strictly. Outcomes are
// fixed tokens, never upstream text.

import { LIMITS } from "./config.js";
import { HEX64, ID_TOKEN, REASON } from "./identity.js";
import { JsonRefused, decodeStrictJson } from "./strict-json.js";
import { TooLarge, readBounded } from "./util.js";

function headers(settings, extra = {}) {
  return { authorization: `Bearer ${settings.EXECUTION_TOKEN}`, ...extra };
}

async function boundedJson(response, limit) {
  try {
    return decodeStrictJson(await readBounded(response.body, limit));
  } catch (error) {
    if (error instanceof JsonRefused || error instanceof TooLarge) return undefined;
    throw error;
  }
}

function terminal(status, body) {
  const reason = body && typeof body.reason === "string" && REASON.test(body.reason) ? body.reason : "execution_refused";
  if (status === 401 || status === 403) return { kind: "refused", reason: "execution_auth_rejected" };
  if (body && body.terminal === true) return { kind: "refused", reason };
  return null;
}

// POST /executions: idempotent per operation and binding.
export async function submitExecution(env, settings, row, bytes) {
  let response;
  try {
    response = await fetch(`${settings.EXECUTION_URL}/executions`, {
      method: "POST",
      headers: headers(settings, {
        "content-type": "application/octet-stream",
        "x-operation-id": row.operation_id,
        "x-snapshot-sha256": row.fingerprint,
        "x-binding-id": row.binding_id,
      }),
      body: bytes,
      signal: AbortSignal.timeout(settings.CALL_TIMEOUT_MS),
    });
  } catch {
    return { kind: "transient", reason: "execution_unreachable" };
  }
  const body = await boundedJson(response, LIMITS.receiptBytes).catch(() => undefined);
  if (response.status >= 200 && response.status < 300) {
    if (
      body &&
      body.operation_id === row.operation_id &&
      typeof body.execution_id === "string" &&
      ID_TOKEN.test(body.execution_id) &&
      typeof body.run_id === "string" &&
      ID_TOKEN.test(body.run_id) &&
      typeof body.state === "string" &&
      REASON.test(body.state)
    ) {
      if (body.binding_id !== row.binding_id) return { kind: "refused", reason: "execution_binding_mismatch" };
      return { kind: "accepted", executionId: body.execution_id, runId: body.run_id, state: body.state };
    }
    return { kind: "transient", reason: "execution_response_invalid" };
  }
  return terminal(response.status, body) ?? { kind: "transient", reason: "execution_unavailable" };
}

// GET /executions/{operation_id}: the execution receipt. The operation's
// snapshot digest and binding travel with the read, so a service that lost
// its own operation mapping can rebuild it without any new submission.
export async function readExecution(env, settings, operationId, snapshotSha256, bindingId) {
  let response;
  try {
    response = await fetch(`${settings.EXECUTION_URL}/executions/${operationId}`, {
      headers: headers(settings, { "x-snapshot-sha256": snapshotSha256, "x-binding-id": bindingId }),
      signal: AbortSignal.timeout(settings.CALL_TIMEOUT_MS),
    });
  } catch {
    return { kind: "transient", reason: "execution_unreachable" };
  }
  const body = await boundedJson(response, LIMITS.receiptBytes).catch(() => undefined);
  if (response.status === 200) {
    if (body === undefined) return { kind: "malformed" };
    return { kind: "receipt", receipt: body };
  }
  if (response.status === 404) return { kind: "unknown" };
  return terminal(response.status, body) ?? { kind: "transient", reason: "execution_unavailable" };
}

// GET /executions/{operation_id}/artifact/{path}: raw bytes, bounded.
export async function fetchPart(env, settings, operationId, path, expectedBytes) {
  let response;
  try {
    response = await fetch(
      `${settings.EXECUTION_URL}/executions/${operationId}/artifact/${path.split("/").map(encodeURIComponent).join("/")}`,
      { headers: headers(settings), signal: AbortSignal.timeout(settings.CALL_TIMEOUT_MS) },
    );
  } catch {
    return { kind: "transient" };
  }
  if (response.status === 404) {
    await response.body?.cancel().catch(() => {});
    return { kind: "missing" };
  }
  if (response.status !== 200) {
    await response.body?.cancel().catch(() => {});
    return { kind: "transient" };
  }
  try {
    return { kind: "bytes", bytes: await readBounded(response.body, Math.min(expectedBytes, LIMITS.artifactFileBytes)) };
  } catch (error) {
    if (error instanceof TooLarge) return { kind: "oversized" };
    return { kind: "transient" };
  }
}

export function validOperationId(value) {
  return typeof value === "string" && HEX64.test(value);
}

// Client for the publisher contract: observe by publication id, and publish
// with the publisher-side fence (expected remote version and a candidate
// sequence that must increase). Outcomes are fixed kinds.

import { HEX64, ID_TOKEN } from "./identity.js";
import { JsonRefused, decodeStrictJson } from "./strict-json.js";
import { TooLarge, readBounded } from "./util.js";

const RECEIPT_BYTES = 16 * 1024;

function validReceipt(body, publication) {
  return (
    body !== null &&
    typeof body === "object" &&
    Object.keys(body).sort().join(",") === "artifact_sha256,candidate_seq,publication_id,receipt_id,remote_version,target" &&
    body.publication_id === publication.publication_id &&
    body.target === publication.target &&
    body.artifact_sha256 === publication.artifact_sha256 &&
    HEX64.test(body.artifact_sha256) &&
    typeof body.receipt_id === "string" &&
    ID_TOKEN.test(body.receipt_id) &&
    Number.isInteger(body.remote_version) &&
    body.remote_version >= 1 &&
    Number.isInteger(body.candidate_seq)
  );
}

async function parse(response) {
  try {
    return decodeStrictJson(await readBounded(response.body, RECEIPT_BYTES));
  } catch (error) {
    if (error instanceof JsonRefused || error instanceof TooLarge) return undefined;
    throw error;
  }
}

function headers(settings, extra = {}) {
  return { authorization: `Bearer ${settings.PUBLISHER_TOKEN}`, ...extra };
}

export async function observePublication(settings, publication) {
  let response;
  try {
    response = await fetch(`${settings.PUBLISHER_URL}/publications/${publication.publication_id}`, {
      headers: headers(settings),
      signal: AbortSignal.timeout(settings.CALL_TIMEOUT_MS),
    });
  } catch {
    return { kind: "transient" };
  }
  if (response.status === 404) {
    await response.body?.cancel().catch(() => {});
    return { kind: "none" };
  }
  const body = await parse(response).catch(() => undefined);
  if (response.status === 200 && validReceipt(body, publication)) return { kind: "receipt", receipt: body };
  return { kind: "transient" };
}

export async function postPublication(settings, publication, expectedRemote) {
  let response;
  try {
    response = await fetch(`${settings.PUBLISHER_URL}/publications/${publication.publication_id}`, {
      method: "POST",
      headers: headers(settings, { "content-type": "application/json" }),
      body: JSON.stringify({
        target: publication.target,
        artifact_sha256: publication.artifact_sha256,
        expected_remote: expectedRemote,
        candidate_seq: publication.candidate_seq,
      }),
      signal: AbortSignal.timeout(settings.CALL_TIMEOUT_MS),
    });
  } catch {
    return { kind: "transient" };
  }
  const body = await parse(response).catch(() => undefined);
  if ((response.status === 200 || response.status === 201) && validReceipt(body, publication)) {
    return { kind: "receipt", receipt: body };
  }
  if (response.status === 409) {
    const reason = body && typeof body.error === "string" && /^[a-z_]{1,32}$/.test(body.error) ? body.error : "publisher_conflict";
    return { kind: "conflict", reason };
  }
  return { kind: "transient" };
}

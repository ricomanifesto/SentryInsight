// Small shared helpers. Nothing here touches a binding.

const encoder = new TextEncoder();

export function utf8(text) {
  return encoder.encode(text);
}

export function hex(buffer) {
  return [...new Uint8Array(buffer)].map((b) => b.toString(16).padStart(2, "0")).join("");
}

export async function sha256Hex(data) {
  const bytes = typeof data === "string" ? utf8(data) : data;
  return hex(await crypto.subtle.digest("SHA-256", bytes));
}

// Equal-length hex strings compared without an early exit.
export function sameHex(a, b) {
  if (typeof a !== "string" || typeof b !== "string" || a.length !== b.length) return false;
  let difference = 0;
  for (let i = 0; i < a.length; i += 1) difference |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return difference === 0;
}

export function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

export function json(status, body, headers = {}) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { "content-type": "application/json", "cache-control": "no-store", ...headers },
  });
}

export function refusal(status, reason) {
  return json(status, { error: reason });
}

export class TooLarge extends Error {}

// Read a body without trusting Content-Length, stopping one byte past the limit.
export async function readBounded(stream, limit) {
  if (stream === null) return new Uint8Array(0);
  const reader = stream.getReader();
  const chunks = [];
  let total = 0;
  for (;;) {
    const { done, value } = await reader.read();
    if (done) break;
    total += value.byteLength;
    if (total > limit) {
      await reader.cancel().catch(() => {});
      throw new TooLarge();
    }
    chunks.push(value);
  }
  const bytes = new Uint8Array(total);
  let offset = 0;
  for (const chunk of chunks) {
    bytes.set(chunk, offset);
    offset += chunk.byteLength;
  }
  return bytes;
}

export function randomToken() {
  return crypto.randomUUID();
}

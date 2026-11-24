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
  // Copy on arrival: retaining every chunk makes bookkeeping scale with
  // chunk count and can pin much larger backing buffers than their views.
  let bytes = new Uint8Array(Math.min(limit, 64 * 1024));
  let total = 0;
  try {
    for (;;) {
      const { done, value } = await reader.read();
      if (done) break;
      const next = total + value.byteLength;
      if (next > limit) {
        await reader.cancel().catch(() => {});
        throw new TooLarge();
      }
      if (next > bytes.length) {
        const grown = new Uint8Array(Math.min(limit, Math.max(next, bytes.length * 2)));
        grown.set(bytes.subarray(0, total));
        bytes = grown;
      }
      bytes.set(value, total);
      total = next;
    }
    return total === bytes.length ? bytes : bytes.slice(0, total);
  } finally {
    reader.releaseLock();
  }
}

export function randomToken() {
  return crypto.randomUUID();
}

// Bearer authentication against SHA-256 digests held in configuration.
// Runs before any binding call; the raw token is never stored or logged.

import { HEX64, TOKEN } from "./identity.js";
import { ConfigInvalid } from "./config.js";
import { sameHex, sha256Hex } from "./util.js";

// `export` reads the research export and nothing else; it is the only role a
// downstream consumer such as the newsletter needs. `project` records runs the
// authoritative producer already completed, and nothing else.
export const ROLES = Object.freeze(["admit", "read", "publish", "operate", "export", "project"]);
const BEARER = /^Bearer ([\x21-\x7e]{16,512})$/;

// AUTH_PRINCIPALS: [{"principal": "manual", "roles": ["admit", "read"], "token_sha256": "<hex>"}]
export function principals(env) {
  let list;
  try {
    list = JSON.parse(env.AUTH_PRINCIPALS ?? "");
  } catch {
    throw new ConfigInvalid("AUTH_PRINCIPALS");
  }
  if (!Array.isArray(list) || list.length === 0 || list.length > 32) throw new ConfigInvalid("AUTH_PRINCIPALS");
  const names = new Set();
  const digests = new Set();
  for (const entry of list) {
    const keys = entry && typeof entry === "object" ? Object.keys(entry).sort().join(",") : "";
    if (
      keys !== "principal,roles,token_sha256" ||
      !TOKEN.test(entry.principal) ||
      entry.principal === "scheduler" ||
      !HEX64.test(entry.token_sha256) ||
      !Array.isArray(entry.roles) ||
      entry.roles.length === 0 ||
      !entry.roles.every((role) => ROLES.includes(role)) ||
      names.has(entry.principal) ||
      digests.has(entry.token_sha256)
    ) {
      throw new ConfigInvalid("AUTH_PRINCIPALS");
    }
    names.add(entry.principal);
    digests.add(entry.token_sha256);
  }
  return list;
}

// Returns {principal} for an allowed caller, or {status, reason} to refuse.
export async function authenticate(request, env, role) {
  const list = principals(env);
  const match = BEARER.exec(request.headers.get("authorization") ?? "");
  if (match === null) return { status: 401, reason: "unauthenticated" };
  const digest = await sha256Hex(match[1]);
  let found = null;
  for (const entry of list) {
    if (sameHex(digest, entry.token_sha256)) found = entry;
  }
  if (found === null) return { status: 401, reason: "unauthenticated" };
  if (!found.roles.includes(role)) return { status: 403, reason: "forbidden" };
  return { principal: found.principal };
}

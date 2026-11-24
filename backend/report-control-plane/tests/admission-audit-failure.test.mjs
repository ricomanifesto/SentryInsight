import assert from "node:assert/strict";
import { test } from "node:test";
import { createHash } from "node:crypto";
import { route } from "../src/router.js";

const token = "synthetic-admission-token-123456";
const auth = JSON.stringify([{ principal: "manual", roles: ["admit"], token_sha256: createHash("sha256").update(token).digest("hex") }]);
const request = () => new Request("https://example.test/v1/operations", {
  method: "POST", headers: { authorization: `Bearer ${token}` },
  body: JSON.stringify({ schema: "unsupported", pipeline: "reports", policy_id: "standard", source_revision: "synthetic", articles: [] }),
});

test("invalid configuration refuses admission before any D1 audit call", async () => {
  let calls = 0;
  const env = { AUTH_PRINCIPALS: auth, CALL_TIMEOUT_MS: "invalid", PRODUCT_DB: { prepare() { calls += 1; throw new Error("unavailable"); } } };
  const response = await route(request(), env);
  assert.equal(response.status, 503);
  assert.equal((await response.json()).error, "config_invalid");
  assert.equal(calls, 0);
});

test("an unavailable audit store preserves the authenticated validation refusal", async () => {
  const env = { AUTH_PRINCIPALS: auth, PRODUCT_DB: { prepare() { throw new Error("unavailable"); } } };
  const response = await route(request(), env);
  assert.equal(response.status, 422);
  assert.equal((await response.json()).error, "schema_unsupported");
});

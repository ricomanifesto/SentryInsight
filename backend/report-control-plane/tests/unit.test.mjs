// Pure functions: strict JSON, identities and the artifact path rules.
import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import test from "node:test";
import { comparePaths, operationId, pathSegments, publicationId, artifactDigest } from "../src/identity.js";
import { JsonRefused, decodeStrictJson, parseStrictJson } from "../src/strict-json.js";
import { parseAdmission, RequestRefused } from "../src/request.js";
import { splitSql } from "../local/stack.mjs";

const sha = (s) => createHash("sha256").update(s).digest("hex");
const enc = (s) => new TextEncoder().encode(s);

test("strict JSON refuses duplicate keys, trailing data, a BOM and invalid UTF-8", () => {
  assert.deepEqual(parseStrictJson('{"a": [1, {"b": null}], "c": "x"}'), { a: [1, { b: null }], c: "x" });
  for (const text of ['{"a": 1, "a": 2}', '{"a": {"b": 1, "b": 1}}', "{} x", "[1,]", '{"a" 1}', "01"]) {
    assert.throws(() => parseStrictJson(text), JsonRefused, text);
  }
  assert.throws(() => decodeStrictJson(new Uint8Array([0xef, 0xbb, 0xbf, 0x7b, 0x7d])), JsonRefused);
  assert.throws(() => decodeStrictJson(new Uint8Array([0x7b, 0xff, 0x7d])), JsonRefused);
  assert.throws(() => parseStrictJson("[".repeat(40) + "]".repeat(40)), JsonRefused);
});

test("identities hash a fixed ASCII string of validated tokens", async () => {
  const fp = sha("bytes");
  assert.equal(await operationId("reports", "standard", fp), sha(`report-control-plane/1\nreports\nstandard\n${fp}`));
  assert.equal(await publicationId("site", fp), sha(`report-control-plane/publication/1\nsite\n${fp}`));
});

test("artifact paths are relative ASCII segments", () => {
  for (const good of ["index.html", "reports/2026/x.md", "a-b_c.d/e"]) assert.ok(pathSegments(good), good);
  for (const bad of ["", "/abs", "../up", "a/../b", "a//b", "a/./b", "a\\b", "a\0b", "é.md", "x".repeat(201), "a b"]) {
    assert.equal(pathSegments(bad), null, JSON.stringify(bad));
  }
});

test("canonical order is by segment, which differs from whole-string order", () => {
  const paths = ["a-c", "a/b", "a"];
  assert.deepEqual([...paths].sort(), ["a", "a-c", "a/b"]);
  assert.deepEqual([...paths].sort(comparePaths), ["a", "a/b", "a-c"]);
});

test("artifact digest is path, NUL, hex digest and newline per file", async () => {
  const files = [{ path: "a/b", sha256: sha("1") }, { path: "a-c", sha256: sha("2") }];
  assert.equal(await artifactDigest(files), sha(`a/b\0${sha("1")}\na-c\0${sha("2")}\n`));
});

test("admission requests are refused on unknown fields, duplicates and bounds", async () => {
  const base = { schema: "report-control-plane/admission/1", pipeline: "reports", policy_id: "standard", source_revision: "r1" };
  const article = { title: "T", link: "https://example.test/a", content: "c" };
  const ok = await parseAdmission(enc(JSON.stringify({ ...base, articles: [article] })));
  assert.equal(ok.articles[0].content_sha256, sha("c"));
  const refusals = [
    [{ ...base, articles: [article], extra: 1 }, "field_unknown"],
    [{ ...base, articles: [{ ...article, extra: 1 }] }, "article_field_unknown"],
    [{ ...base, articles: [article, article] }, "article_duplicate_key"],
    [{ ...base, articles: [] }, "articles_invalid"],
    [{ ...base, source_revision: "schedule:x", articles: [article] }, "source_revision_reserved"],
    [{ ...base, articles: [{ ...article, link: "ftp://x" }] }, "article_invalid"],
    [{ ...base, articles: [{ ...article, content: "x".repeat(70000) }] }, "article_invalid"],
    [{ ...base, schema: "other/1", articles: [article] }, "schema_unsupported"],
  ];
  for (const [value, reason] of refusals) {
    await assert.rejects(parseAdmission(enc(JSON.stringify(value))), (e) => e instanceof RequestRefused && e.reason === reason, reason);
  }
  const duplicateKey = `{"schema":"report-control-plane/admission/1","pipeline":"reports","pipeline":"x","policy_id":"standard","source_revision":"r","articles":[]}`;
  await assert.rejects(parseAdmission(enc(duplicateKey)), (e) => e.reason === "request_malformed");
});

test("migration SQL splits into whole statements", () => {
  assert.deepEqual(splitSql("-- c\nCREATE TABLE a (x TEXT);\n\nCREATE INDEX i ON a (x);\n"), ["CREATE TABLE a (x TEXT)", "CREATE INDEX i ON a (x)"]);
});

// Run identity is the digest of the complete accepted projection record: the
// strict parser is the only definition of that record, and every leaf of it
// is in the digest. There is no separate list of compared fields to forget.
test("the projection facts digest covers every accepted field, and nothing else can be accepted", async () => {
  const { canonicalJson, factsDigest, parseProjection, ProjectionRefused } = await import("../src/projection.js");
  const request = {
    schema: "report-control-plane/projection/1",
    pipeline: "reports",
    policy_id: "production",
    source_revision: "actions:1:1",
    snapshot_sha256: sha("snapshot"),
    run: {
      execution_id: "actions-run-1-1",
      source_commit: sha("commit").slice(0, 40),
      outcome: "succeeded",
      reason: null,
      source_outcomes: { "https://example.test/a": "executed", "https://example.test/b": "source_rejected" },
    },
    artifact: { files: [{ path: "index.md", sha256: sha("report"), bytes: 9 }] },
  };
  const parsed = parseProjection(enc(JSON.stringify(request)));
  assert.deepEqual(JSON.parse(canonicalJson(parsed)), parsed, "the canonical record is the whole parsed request");
  assert.equal(canonicalJson({ b: 1, a: { d: 2, c: [3] } }), '{"a":{"c":[3],"d":2},"b":1}');
  const digest = await factsDigest(parsed);
  assert.equal(await factsDigest(JSON.parse(JSON.stringify(parsed))), digest, "key order does not matter");

  // Every leaf, found generically, changes the digest when it changes.
  const leaves = [];
  const walk = (value, path) => {
    if (value !== null && typeof value === "object") {
      for (const [key, item] of Object.entries(value)) walk(item, [...path, key]);
    } else leaves.push(path);
  };
  walk(parsed, []);
  assert.ok(leaves.some((p) => p.join(".") === "run.reason") && leaves.some((p) => p[1] === "source_outcomes"));
  for (const path of leaves) {
    const changed = structuredClone(parsed);
    const holder = path.slice(0, -1).reduce((v, k) => v[k], changed);
    const key = path[path.length - 1];
    holder[key] = holder[key] === null ? "x" : typeof holder[key] === "number" ? holder[key] + 1 : `${holder[key]}x`;
    assert.notEqual(await factsDigest(changed), digest, path.join("."));
  }

  // An extra key at any object level, completed_at included, is refused, so
  // an accepted request never carries a fact the digest does not see.
  const objects = [[], ["run"], ["artifact"], ["artifact", "files", 0]];
  for (const path of objects) {
    for (const extra of ["completed_at", "note"]) {
      const widened = structuredClone(request);
      path.reduce((v, k) => v[k], widened)[extra] = "2026-11-08T12:00:00Z";
      assert.throws(() => parseProjection(enc(JSON.stringify(widened))), (e) => e instanceof ProjectionRefused && e.reason === "projection_malformed", `${path.join(".")}.${extra}`);
    }
  }
  const unknown = structuredClone(request);
  unknown.run.source_outcomes["https://example.test/a"] = "skipped";
  assert.throws(() => parseProjection(enc(JSON.stringify(unknown))), ProjectionRefused);
});

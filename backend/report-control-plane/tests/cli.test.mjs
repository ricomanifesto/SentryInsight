// The CLI drives a complete flow and downloads a verified artifact; the
// declared deployment bindings match the local stack.
import assert from "node:assert/strict";
import { execFile } from "node:child_process";
import { readFile, writeFile } from "node:fs/promises";
import path from "node:path";
import { after, before, test } from "node:test";
import { promisify } from "node:util";
import { fileURLToPath } from "node:url";
import { BINDINGS, QUEUES, COMPATIBILITY_DATE } from "../local/stack.mjs";
import { REPORT_FILES, admission, article, setup } from "./support/harness.mjs";

const run = promisify(execFile);
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
let env;
before(async () => {
  env = await setup();
});
after(async () => {
  await env.stop();
});

async function cli(who, ...args) {
  const tokenFile = path.join(env.root, `token-${who}`);
  await writeFile(tokenFile, env.tokens[who]);
  try {
    const { stdout } = await run(process.execPath, [path.join(root, "cli/report-control.mjs"), ...args], {
      env: { PATH: process.env.PATH, REPORT_CONTROL_URL: env.stack.url, REPORT_CONTROL_TOKEN_FILE: tokenFile },
    });
    return { code: 0, out: JSON.parse(stdout) };
  } catch (error) {
    return { code: error.code, out: error.stdout ? JSON.parse(error.stdout) : null, err: error.stderr };
  }
}

test("the CLI admits, reports status, publishes and downloads a verified artifact", async () => {
  const request = path.join(env.root, "request.json");
  await writeFile(request, JSON.stringify(admission("cli-1", [article(1)])));
  const admitted = await cli("manual", "admit", request);
  assert.equal(admitted.code, 0);
  const id = admitted.out.operation.operation_id;
  await env.waitState(id, "submitted");
  env.execution.succeed(id, REPORT_FILES);
  assert.equal((await cli("operator", "reconcile")).code, 0);
  const status = await cli("manual", "status", id);
  assert.equal(status.out.operation.state, "completed");
  const sha = status.out.operation.artifact_sha256;
  const published = await cli("publisher", "publish", id, "site-cli");
  assert.equal(published.out.publication.state, "published");
  const out = path.join(env.root, "download");
  const download = await cli("reader", "artifact", sha, out);
  assert.equal(download.code, 0);
  assert.equal(download.out.verified, true);
  for (const [file, content] of Object.entries(REPORT_FILES)) {
    assert.equal(await readFile(path.join(out, sha, file), "utf8"), content);
  }
  assert.equal((await cli("reader", "target", "site-cli")).out.target.last_good.artifact_sha256, sha);
});

test("the declared deployment bindings match the local stack", async () => {
  const toml = await readFile(path.join(root, "wrangler.toml"), "utf8");
  assert.match(toml, new RegExp(`binding = "${BINDINGS.db}"`));
  assert.match(toml, new RegExp(`binding = "${BINDINGS.artifacts}"`));
  assert.match(toml, new RegExp(`binding = "${BINDINGS.queue}"\\nqueue = "${QUEUES.admissions}"`));
  assert.match(toml, new RegExp(`dead_letter_queue = "${QUEUES.dead}"`));
  assert.match(toml, new RegExp(`compatibility_date = "${COMPATIBILITY_DATE}"`));
  assert.doesNotMatch(toml, /^\s*(account_id|routes?|workers_dev)\s*=|remote\s*=\s*true/m);
});

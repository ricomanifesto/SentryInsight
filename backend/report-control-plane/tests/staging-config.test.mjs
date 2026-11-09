// The staging declaration: its queue variables name exactly the queues it
// declares, the names pass the Worker's own grammar, the bindings are the
// code's, and no secret is declared as a plain variable.
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";
import { BINDINGS, queueNames } from "../src/config.js";

const PACKAGE_ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");

test("the staging declaration is consistent with the Worker's own configuration rules", async () => {
  const toml = await readFile(path.join(PACKAGE_ROOT, "wrangler.staging.toml"), "utf8");
  const value = (key) => toml.match(new RegExp(`^${key} = "([^"]+)"$`, "m"))?.[1];
  const names = queueNames({ ADMISSIONS_QUEUE_NAME: value("ADMISSIONS_QUEUE_NAME"), DEAD_LETTER_QUEUE_NAME: value("DEAD_LETTER_QUEUE_NAME") });
  assert.match(toml, new RegExp(`binding = "${BINDINGS.queue}"\\nqueue = "${names.admissions}"`));
  assert.deepEqual([...toml.matchAll(/^queue = "([^"]+)"$/gm)].map((m) => m[1]).sort(), [names.admissions, names.admissions, names.dead].sort());
  assert.match(toml, new RegExp(`dead_letter_queue = "${names.dead}"`));
  assert.match(toml, new RegExp(`binding = "${BINDINGS.db}"`));
  assert.match(toml, new RegExp(`binding = "${BINDINGS.artifacts}"`));
  assert.match(toml, /^database_id = "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"$/m);
  assert.doesNotMatch(toml, /^database_id = "00000000-/m, "the staging file names a real database");
  const vars = toml.slice(toml.indexOf("[vars]"));
  for (const secret of ["AUTH_PRINCIPALS", "EXECUTION_URL", "EXECUTION_TOKEN", "PUBLISHER_URL", "PUBLISHER_TOKEN"]) {
    assert.doesNotMatch(vars, new RegExp(`^${secret} =`, "m"), secret);
  }
});

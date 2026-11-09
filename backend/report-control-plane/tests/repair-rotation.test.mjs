// Publication repair rotates: candidates that stay unobservable cannot keep a
// newer unresolved publication from being settled.
import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { after, before, test } from "node:test";
import { REPORT_FILES, admission, article, completed, setup } from "./support/harness.mjs";

let env;
before(async () => {
  env = await setup();
});
after(async () => {
  await env.stop();
});

const sha = (data) => createHash("sha256").update(data).digest("hex");

test("a newer unresolved publication settles although older superseded ones never can", async () => {
  const at = Date.now();
  await env.stack.db.prepare("INSERT INTO targets (target, updated_at) VALUES ('site-stale', ?)").bind(at).run();
  for (let n = 0; n < 20; n += 1) {
    await env.stack.db
      .prepare(
        `INSERT INTO publications (publication_id, target, artifact_sha256, operation_id, candidate_seq, state, created_at, updated_at)
         VALUES (?, 'site-stale', ?, ?, 0, 'superseded', ?, ?)`,
      )
      .bind(sha(`stale ${n}`), sha(`artifact ${n}`), sha(`operation ${n}`), at, at)
      .run();
  }
  const id = await completed(env, admission("repair-newer", [article(7500)]), { ...REPORT_FILES, "index.html": "newer\n" });
  const artifact = (await env.row(id)).artifact_sha256;
  const p = sha(`report-control-plane/publication/1\nsite-newer\n${artifact}`);
  await env.publisherControl({ drop_ack: [p] });
  assert.equal((await env.publish(id, "site-newer")).body.publication.state, "unresolved");
  for (let sweep = 0; sweep < 2 && (await env.one("SELECT state FROM publications WHERE publication_id = ?", p)).state !== "published"; sweep += 1) {
    await env.reconcile();
  }
  assert.equal((await env.one("SELECT state FROM publications WHERE publication_id = ?", p)).state, "published", "settled within two sweeps");
});

// Sanitized product status: states, versions, ids, digests, counts and fixed
// reason tokens. No paths, hosts or upstream messages.

import { publicationView, runPublications, targetView } from "./publication.js";

export function operationView(row) {
  return {
    operation_id: row.operation_id,
    seq: row.seq,
    pipeline: row.pipeline,
    policy_id: row.policy_id,
    binding_id: row.binding_id,
    source_revision: row.source_revision,
    fingerprint: row.fingerprint,
    principal: row.principal,
    state: row.state,
    version: row.version,
    delivery_generation: row.delivery_generation,
    retry_rounds: row.retry_rounds,
    send_attempts: row.send_attempts,
    reason: row.reason,
    execution: row.execution_id
      ? {
          execution_id: row.execution_id,
          run_id: row.run_id,
          run_state: row.run_state,
          run_reason: row.run_reason,
          attempts: { used: row.attempts_used, limit: row.attempts_limit },
          budget: { reserved: row.budget_reserved, limit: row.budget_limit },
        }
      : null,
    artifact_sha256: row.artifact_sha256,
    executed_count: row.executed_count,
  };
}

export async function operationStatus(db, row) {
  const [{ results: publications }, { results: articles }] = await Promise.all([
    // The same run publications as the export: shared by artifact only when
    // the publisher made them, an observation only on its own run.
    runPublications(db, row.operation_id, "candidate").all(),
    db.prepare("SELECT count(*) AS n FROM operation_articles WHERE operation_id = ?").bind(row.operation_id).all(),
  ]);
  const targets = [];
  for (const target of new Set(publications.map((p) => p.target))) {
    targets.push(targetView(await db.prepare("SELECT * FROM targets WHERE target = ?").bind(target).first()));
  }
  return {
    operation: { ...operationView(row), admitted_articles: articles[0].n },
    publications: publications.map(publicationView),
    targets,
  };
}

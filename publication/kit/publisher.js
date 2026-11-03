// Serialized source-to-artifact publisher.
//
// Every invocation first resumes whatever the current artifact tip still
// needs (state record, serving proof, downstream delivery), then handles its
// own request. The artifact branch advances only by compare-and-set past a
// terminal tip: no tip, a pre-boundary tip, a tip proved serving, or a tip
// whose provider failure an operator attested. Anything else is a hold, never
// a timeout. Once a proof-on release exists (the proof boundary), proof-off
// releases can never advance again and rollbacks may only target a release
// commit that was proved serving.
//
// Stages per artifact commit: released -> serving | verification-failed, with
// side records held, superseded, rejected, failed-attested and
// alias-regressed. Status belongs to the exact commit (release_ref): a later
// commit with the same release key, such as a repeated rollback, is proved
// on its own. Digest delivery records per consumer: pending -> sending ->
// sent | failed, plus ineligible, not-applicable, superseded and uncertain.
// Before every send the publisher re-establishes that the release is still
// the artifact tip, still proved at the production origin, and that main
// still grants active authority; otherwise delivery is held.
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');

const { inventoryOfDir, sha256 } = require('./canonical');
const { loadSiteConfig } = require('./config');
const { buildArtifactTree, extractPayload } = require('./artifact');
const { CompareAndSetLost, createGit } = require('./git');
const { proveServing } = require('./proof');
const { LAYOUT, SHA1, buildDescriptor, parseDescriptor } = require('./release');
const { createStore } = require('./store');

const RELEASE_STAGES = new Set(['released', 'serving', 'verification-failed', 'failed-attested', 'alias-regressed']);
const TERMINAL_DELIVERY = new Set(['sent', 'ineligible', 'not-applicable', 'superseded']);
const MAX_ADVANCE_ATTEMPTS = 5;

function createPublisher({
  repoRoot,
  remote,
  config,
  buildPayload,
  fetchUrl,
  dispatch,
  readMainHeadPublication,
  readPublication,
  contentIdentityAt,
  proofAttempts = 6,
  proofBaseDelayMs = 10000,
  sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms)),
  now = () => new Date(),
  gitEnv = process.env,
  hooks = {},
  log = () => {},
}) {
  const git = createGit(repoRoot, { env: gitEnv });
  const branch = config.artifact_branch;
  const store = createStore({ git, remote, branch: config.state_branch, site: config.site, now });
  const consumers = config.consumers || [];

  const publicationAt = readPublication || ((revision) => {
    const text = git.showFile(revision, 'publication/site.json', { encoding: 'utf8' });
    if (!text) throw new Error(`publication/site.json is missing at ${revision}`);
    return loadSiteConfig(text).publication;
  });
  const identityAt = contentIdentityAt || (async (revision) => (await buildPayload({ sourceRevision: revision })).contentIdentity);

  // Artifact branch history, oldest first, from the release trailers that
  // every artifact commit carries.
  function history(tip) {
    if (!tip) return [];
    const output = git.run(['log', '--first-parent', '--reverse', '--format=%H%x1f%B%x1e', tip]);
    return output.split('\x1e').map((chunk) => chunk.trim()).filter(Boolean).map((chunk) => {
      const [commit, body] = chunk.split('\x1f');
      const trailer = (name) => body.match(new RegExp(`^${name}: (\\S+)$`, 'm'))?.[1];
      return {
        commit,
        releaseKey: trailer('Release-Key'),
        kind: trailer('Kind'),
        sourceRevision: trailer('Source-Revision'),
        payloadDigest: trailer('Payload-Digest'),
        proof: trailer('Proof'),
      };
    });
  }

  async function readContext() {
    const tip = git.fetchBranch(remote, branch);
    const entries = history(tip);
    const { records } = await store.read();
    return { tip, entries, records, boundary: entries.find((entry) => entry.proof === 'on') || null };
  }

  const recordsFor = (records, commit) => records.filter((record) => record.release_ref === commit);

  function releaseStatus(records, entry) {
    if (!entry) return 'none';
    if (entry.proof === 'off') return 'pre-boundary';
    const stages = recordsFor(records, entry.commit).map((record) => record.stage).filter((stage) => RELEASE_STAGES.has(stage));
    if (stages.includes('failed-attested')) return 'failed-attested';
    if (stages.includes('alias-regressed')) return 'alias-regressed';
    if (stages.includes('serving')) return 'serving';
    if (stages.includes('verification-failed')) return 'verification-failed';
    if (stages.includes('released')) return 'released';
    return 'unrecorded';
  }

  const isTerminal = (status) => ['none', 'pre-boundary', 'serving', 'failed-attested', 'alias-regressed'].includes(status);

  function descriptorOf(commit) {
    const bytes = git.showFile(commit, LAYOUT.descriptor);
    if (!bytes) throw new Error(`${commit} has no release descriptor`);
    return { bytes, descriptor: parseDescriptor(bytes) };
  }

  function payloadEntriesOf(commit) {
    const entries = git.listTree(commit).filter((entry) => entry.path.startsWith(LAYOUT.payloadPrefix));
    const blobs = git.readBlobs(entries.map((entry) => entry.oid));
    return entries.map((entry, index) => ({
      path: entry.path.slice(LAYOUT.payloadPrefix.length),
      sha256: sha256(blobs[index]),
      bytes: blobs[index].length,
    }));
  }

  const record = (records) => store.append(() => records);

  async function prove(entry, attempts = proofAttempts) {
    const { bytes } = descriptorOf(entry.commit);
    return proveServing({
      config,
      release: { releaseKey: entry.releaseKey, releaseRef: entry.commit, descriptorBytes: bytes, payloadEntries: payloadEntriesOf(entry.commit) },
      fetchUrl,
      attempts,
      baseDelayMs: proofBaseDelayMs,
      sleep,
      now,
    });
  }

  async function recordProof(entry) {
    const proof = await prove(entry);
    await record([{
      stage: proof.ok ? 'serving' : 'verification-failed',
      release_key: entry.releaseKey,
      release_ref: entry.commit,
      proof,
    }]);
    log(`${entry.releaseKey}: ${proof.ok ? 'serving' : `verification failed: ${proof.failures.join('; ')}`}`);
    return proof;
  }

  // ----- downstream delivery (sites with consumers) -----

  function deliveryStatuses(records, releaseKey, consumer) {
    return records.filter((r) => r.stage === 'delivery' && r.release_key === releaseKey && r.consumer === consumer).map((r) => r.status);
  }

  function lastDelivered(records, consumer) {
    let value = null;
    for (const r of records) {
      if (r.stage === 'seed' && r.consumer === consumer) value = r.last_delivered;
      if (r.stage === 'delivery' && r.consumer === consumer && r.status === 'sent') value = r.digest_content_digest;
    }
    return value;
  }

  // Why a send for this release may not happen now, or null. Checked at each
  // external send: the artifact tip, the current main authority and a fresh
  // single-attempt proof at the production origin.
  async function sendBlocker(entry) {
    const tip = git.fetchBranch(remote, branch);
    if (tip !== entry.commit) return `artifact branch moved to ${tip}`;
    const mainHead = await readMainHeadPublication();
    if (mainHead?.mode !== 'active') return `main head publication is ${mainHead?.mode ?? 'unknown'}`;
    const proof = await prove(entry, 1);
    if (!proof.ok) return `release is not proved serving now: ${proof.failures[0]}`;
    return null;
  }

  async function deliver(ctx, entry) {
    if (consumers.length === 0) return { status: 'no-consumers' };
    if (hooks.beforeDelivery) await hooks.beforeDelivery();
    const { descriptor } = descriptorOf(entry.commit);
    let { records } = await store.read();

    // An older release whose delivery never completed is superseded: the
    // newer release is compared against the same last delivered content.
    const supersede = [];
    for (const older of ctx.entries.slice(0, -1)) {
      for (const consumer of consumers) {
        const statuses = deliveryStatuses(records, older.releaseKey, consumer.name);
        if (statuses.length > 0 && !TERMINAL_DELIVERY.has(statuses.at(-1))) {
          supersede.push({ stage: 'delivery', release_key: older.releaseKey, consumer: consumer.name, status: 'superseded', by: entry.releaseKey });
        }
      }
    }
    if (supersede.length > 0) records = (await record(supersede)).records;

    if (descriptor.kind === 'rollback') {
      const additions = consumers
        .filter((consumer) => deliveryStatuses(records, entry.releaseKey, consumer.name).length === 0)
        .map((consumer) => ({ stage: 'delivery', release_key: entry.releaseKey, consumer: consumer.name, status: 'not-applicable' }));
      if (additions.length > 0) await record(additions);
      return { status: 'not-applicable' };
    }
    if (descriptor.publication_mode.mode !== 'active') return { status: 'legacy-notifier' };
    const mainHead = await readMainHeadPublication();
    if (mainHead?.mode !== 'active') {
      await record([{ stage: 'delivery-summary', release_key: entry.releaseKey, status: 'awaiting-authority', main_head_mode: mainHead?.mode ?? null }]);
      return { status: 'awaiting-authority' };
    }

    const identity = descriptor.content_identity;
    const payload = {
      schema: 'sentrydigest-release/v1',
      site: config.site,
      release_key: entry.releaseKey,
      release_ref: entry.commit,
      source_revision: descriptor.source_revision,
      payload_digest: descriptor.payload_digest,
      digest_content_digest: identity.digest_content_digest,
      feed_sha256: identity.feed_sha256,
      news_data_sha256: identity.news_data_sha256,
    };
    const base = { stage: 'delivery', release_key: entry.releaseKey };
    let failed = false;
    for (const consumer of consumers) {
      ({ records } = await store.read());
      const statuses = deliveryStatuses(records, entry.releaseKey, consumer.name);
      const latest = statuses.at(-1);
      if (TERMINAL_DELIVERY.has(latest)) continue;
      if (latest === undefined && lastDelivered(records, consumer.name) === identity.digest_content_digest) {
        await record([{ ...base, consumer: consumer.name, status: 'ineligible', digest_content_digest: identity.digest_content_digest }]);
        continue;
      }
      const blocker = await sendBlocker(entry);
      if (blocker) {
        await record([{ stage: 'delivery-summary', release_key: entry.releaseKey, release_ref: entry.commit, status: 'held', reason: blocker }]);
        log(`${entry.releaseKey}: delivery held: ${blocker}`);
        return { status: 'held', reason: blocker };
      }
      if (latest === undefined) {
        await record([{ ...base, consumer: consumer.name, status: 'pending' }]);
      } else if (latest === 'sending') {
        // The provider call may or may not have happened; resend (at least once).
        await record([{ ...base, consumer: consumer.name, status: 'uncertain' }]);
      }
      await record([{ ...base, consumer: consumer.name, status: 'sending' }]);
      try {
        await dispatch(consumer, payload);
      } catch (error) {
        failed = true;
        await record([{ ...base, consumer: consumer.name, status: 'failed', reason: error.message }]);
        continue;
      }
      if (hooks.afterDispatch) await hooks.afterDispatch(consumer);
      await record([{ ...base, consumer: consumer.name, status: 'sent', digest_content_digest: identity.digest_content_digest }]);
    }
    const status = failed ? 'partial' : 'delivered';
    await record([{ stage: 'delivery-summary', release_key: entry.releaseKey, status }]);
    return { status };
  }

  // ----- releases -----

  async function stagePayload(sourceRevision, publication) {
    const { payloadDir, contentIdentity } = await buildPayload({ sourceRevision });
    const entries = inventoryOfDir(payloadDir);
    const built = buildDescriptor({
      config,
      kind: 'release',
      sourceRevision,
      sourceCommittedAt: new Date(git.commitDate(sourceRevision)).toISOString(),
      publicationMode: publication,
      payloadEntries: entries,
      contentIdentity,
    });
    return { ...built, payloadDir, entries };
  }

  function commitMessage(built, treeDigest) {
    const d = built.descriptor;
    return [
      `Release ${d.site} ${d.kind} of ${d.source_revision.slice(0, 12)}`,
      '',
      `Release-Key: ${built.releaseKey}`,
      `Kind: ${d.kind}`,
      `Source-Revision: ${d.source_revision}`,
      `Payload-Digest: ${d.payload_digest}`,
      `Tree-Digest: ${treeDigest}`,
      `Proof: ${d.publication_mode.proof}`,
      '',
    ].join('\n');
  }

  // Advances the artifact branch with a built release if the tip is terminal.
  async function advance(ctx, built, { sourceRevision }) {
    const status = releaseStatus(ctx.records, ctx.entries.at(-1));
    if (!isTerminal(status)) {
      await record([{ stage: 'held', release_key: built.releaseKey, source_revision: sourceRevision, tip_release_key: ctx.entries.at(-1).releaseKey, tip_status: status }]);
      return { outcome: 'held', release_key: built.releaseKey, tip_status: status };
    }
    const tree = buildArtifactTree({ payloadDir: built.payloadDir, descriptorBytes: built.bytes });
    const commit = git.commitFiles(tree.files, { parent: ctx.tip, message: commitMessage(built, tree.treeDigest) });
    if (hooks.beforeArtifactPush) await hooks.beforeArtifactPush();
    git.pushBranch(remote, commit, branch, ctx.tip);
    if (hooks.afterArtifactPush) await hooks.afterArtifactPush();
    await record([{
      stage: 'released',
      release_key: built.releaseKey,
      release_ref: commit,
      kind: built.descriptor.kind,
      source_revision: sourceRevision,
      payload_digest: built.payloadDigest,
      tree_digest: tree.treeDigest,
      proof: built.descriptor.publication_mode.proof,
    }]);
    const entry = { commit, releaseKey: built.releaseKey, proof: built.descriptor.publication_mode.proof };
    if (entry.proof === 'off') return { outcome: 'released', release_key: built.releaseKey, release_ref: commit };
    const proof = await recordProof(entry);
    if (proof.ok) await deliver(await readContext(), entry);
    return { outcome: proof.ok ? 'serving' : 'verification-failed', release_key: built.releaseKey, release_ref: commit, proof };
  }

  async function rollbackRelease(ctx, target, reason) {
    const top = ctx.entries.at(-1);
    const scratch = fs.mkdtempSync(path.join(os.tmpdir(), 'publication-rollback-'));
    try {
      const payloadDir = extractPayload(git, target.commit, scratch);
      const { descriptor } = descriptorOf(target.commit);
      const built = buildDescriptor({
        config,
        kind: 'rollback',
        sourceRevision: descriptor.source_revision,
        sourceCommittedAt: descriptor.source_committed_at,
        publicationMode: descriptor.publication_mode,
        payloadEntries: inventoryOfDir(payloadDir),
        contentIdentity: descriptor.content_identity,
        rollbackOf: target.releaseKey,
        reason,
      });
      // The same rollback already sits at the tip: a retry is a no-op, never
      // a second commit.
      if (top && top.releaseKey === built.releaseKey) {
        return { outcome: 'no-op', release_key: built.releaseKey, release_ref: top.commit };
      }
      return await advance(ctx, { ...built, payloadDir }, { sourceRevision: descriptor.source_revision });
    } finally {
      fs.rmSync(scratch, { recursive: true, force: true });
    }
  }

  // Completes whatever the current tip still needs.
  async function resumeTip(ctx) {
    const entry = ctx.entries.at(-1);
    if (!entry) return { outcome: 'none' };
    if (!recordsFor(ctx.records, entry.commit).some((r) => r.stage === 'released')) {
      // Crash after the push and before the state record: the tip is the release.
      await record([{ stage: 'released', release_key: entry.releaseKey, release_ref: entry.commit, kind: entry.kind, source_revision: entry.sourceRevision, payload_digest: entry.payloadDigest, proof: entry.proof, recovered: true }]);
      ctx.records = (await store.read()).records;
    }
    const status = releaseStatus(ctx.records, entry);
    if (status === 'pre-boundary' || status === 'failed-attested') return { outcome: status };
    if (status === 'serving' || status === 'alias-regressed') {
      if (ctx.records.some((r) => r.stage === 'failed-attested')) {
        const regressed = await detectRegression(ctx, entry);
        if (regressed) return regressed;
      }
      const delivery = await deliver(ctx, entry);
      return { outcome: 'serving', delivery };
    }
    const proof = await recordProof(entry);
    if (!proof.ok) return { outcome: 'verification-failed', proof };
    const delivery = await deliver(await readContext(), entry);
    return { outcome: 'serving', proof, delivery };
  }

  // After an operator attested a provider failure, the origin may later serve
  // that failed release over a newer proved one. That regression is repaired
  // by republishing the newest proved payload as a rollback release.
  async function detectRegression(ctx, entry) {
    let served;
    try {
      const response = await fetchUrl(`${config.origins[config.site].production}${LAYOUT.descriptor}`);
      served = JSON.parse(Buffer.from(response.body).toString('utf8')).release_key;
    } catch {
      return null;
    }
    const attested = new Set(ctx.records.filter((r) => r.stage === 'failed-attested').map((r) => r.release_key));
    if (served === entry.releaseKey || !attested.has(served)) return null;
    await record([{ stage: 'alias-regressed', release_key: entry.releaseKey, release_ref: entry.commit, served_release_key: served }]);
    const repair = await rollbackRelease(await readContext(), entry, 'alias-regressed');
    return { outcome: 'alias-regressed', served_release_key: served, repair };
  }

  async function resume() {
    const ctx = await readContext();
    return { tip: await resumeTip(ctx) };
  }

  async function publish({ sourceRevision }) {
    if (!SHA1.test(sourceRevision || '')) throw new Error('source revision must be a full commit id');
    git.run(['cat-file', '-e', `${sourceRevision}^{commit}`]);
    const publication = publicationAt(sourceRevision);

    for (let attempt = 1; attempt <= MAX_ADVANCE_ATTEMPTS; attempt += 1) {
      const tipResult = await resumeTip(await readContext());
      // Resuming may have recorded proof or delivery, or moved the tip.
      const ctx = await readContext();

      if (publication.mode === 'disabled') {
        const built = await stagePayload(sourceRevision, publication);
        return { outcome: 'disabled', release_key: built.releaseKey, payload_digest: built.payloadDigest, tip: tipResult };
      }
      let built;
      try {
        built = await stagePayload(sourceRevision, publication);
      } catch (error) {
        await record([{ stage: 'rejected', source_revision: sourceRevision, reason: error.message }]);
        return { outcome: 'rejected', reason: error.message, tip: tipResult };
      }
      const top = ctx.entries.at(-1);
      if (top && top.releaseKey === built.releaseKey) {
        return { outcome: 'no-op', release_key: built.releaseKey, release_ref: ctx.tip, tip: tipResult };
      }
      if (top && top.sourceRevision !== sourceRevision && git.isAncestor(sourceRevision, top.sourceRevision)) {
        await record([{ stage: 'superseded', release_key: built.releaseKey, source_revision: sourceRevision, by: top.releaseKey }]);
        return { outcome: 'superseded', release_key: built.releaseKey, tip: tipResult };
      }
      if (ctx.boundary && publication.proof === 'off') {
        const reason = 'publication proof is off after the proof boundary; proof-off releases can no longer advance';
        await record([{ stage: 'rejected', release_key: built.releaseKey, source_revision: sourceRevision, reason }]);
        return { outcome: 'rejected', reason, tip: tipResult };
      }
      try {
        return { ...(await advance(ctx, built, { sourceRevision })), tip: tipResult };
      } catch (error) {
        if (!(error instanceof CompareAndSetLost)) throw error;
        log(`artifact branch moved; re-reading (${error.message})`);
      }
    }
    throw new Error(`${branch} kept moving; gave up after ${MAX_ADVANCE_ATTEMPTS} attempts`);
  }

  async function rollback({ targetReleaseKey, reason }) {
    if (!reason) throw new Error('a rollback needs a reason');
    for (let attempt = 1; attempt <= MAX_ADVANCE_ATTEMPTS; attempt += 1) {
      const ctx = await readContext();
      await resumeTip(ctx);
      const fresh = await readContext();
      // The target must be a commit of that release proved serving and never
      // attested as a provider failure: an accepted, last-good payload.
      const candidates = fresh.entries.filter((entry) => entry.releaseKey === targetReleaseKey);
      if (candidates.length === 0) throw new Error(`release ${targetReleaseKey} is not on the artifact branch`);
      if (candidates.some((entry) => entry.proof !== 'on')) throw new Error(`release ${targetReleaseKey} is pre-boundary and cannot be a rollback target`);
      const proved = (entry) => {
        const stages = recordsFor(fresh.records, entry.commit).map((record) => record.stage);
        return stages.includes('serving') && !stages.includes('failed-attested');
      };
      const target = candidates.findLast(proved);
      if (!target) throw new Error(`release ${targetReleaseKey} was never proved serving and cannot be a rollback target`);
      try {
        return await rollbackRelease(fresh, target, reason);
      } catch (error) {
        if (!(error instanceof CompareAndSetLost)) throw error;
      }
    }
    throw new Error(`${branch} kept moving; gave up after ${MAX_ADVANCE_ATTEMPTS} attempts`);
  }

  // Operator attestation that the provider build of the tip failed terminally.
  async function resolve({ releaseKey, attestation }) {
    if (!attestation || !String(attestation).trim()) throw new Error('an operator attestation is required');
    const ctx = await readContext();
    const top = ctx.entries.at(-1);
    if (!top || top.releaseKey !== releaseKey) throw new Error(`release ${releaseKey} is not the artifact tip`);
    const status = releaseStatus(ctx.records, top);
    if (!['released', 'verification-failed', 'unrecorded'].includes(status)) {
      throw new Error(`release ${releaseKey} is ${status}; only an unproved tip can be attested as failed`);
    }
    await record([{ stage: 'failed-attested', release_key: releaseKey, release_ref: top.commit, attestation: String(attestation) }]);
    return { outcome: 'failed-attested', release_key: releaseKey };
  }

  // Activation seed: per consumer, the Digest commit of the last legacy
  // dispatch the Actions history shows as delivered, or "none".
  async function seed({ consumers: seeds, attestation }) {
    if (!attestation || !String(attestation).trim()) throw new Error('an attestation of the legacy dispatch history is required');
    const additions = [];
    for (const [name, revision] of Object.entries(seeds || {})) {
      if (!consumers.some((consumer) => consumer.name === name)) throw new Error(`${name} is not a configured consumer`);
      if (revision === 'none') {
        additions.push({ stage: 'seed', consumer: name, last_delivered: null, digest_revision: null, attestation });
      } else {
        if (!SHA1.test(revision)) throw new Error(`seed revision for ${name} must be a full commit id or none`);
        const identity = await identityAt(revision);
        additions.push({ stage: 'seed', consumer: name, last_delivered: identity.digest_content_digest, digest_revision: revision, attestation });
      }
    }
    if (additions.length === 0) throw new Error('no consumers to seed');
    await record(additions);
    return { outcome: 'seeded', consumers: additions.map((a) => a.consumer) };
  }

  async function readState() {
    const { records } = await store.read();
    return { records, tip: git.fetchBranch(remote, branch) };
  }

  return { publish, readState, resolve, resume, rollback, seed };
}

module.exports = { createPublisher };

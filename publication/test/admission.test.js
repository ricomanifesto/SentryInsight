const assert = require('node:assert/strict');
const childProcess = require('node:child_process');
const fs = require('node:fs');
const path = require('node:path');
const test = require('node:test');

const { createAdmission, findAdmissionReport, snapshotFeedUrl } = require('../kit/admission');
const { canonicalJson } = require('../kit/canonical');
const { loadSiteConfig } = require('../kit/config');
const { createGit } = require('../kit/git');
const { LAYOUT, buildDescriptor } = require('../kit/release');
const { GIT_ENV, git, sha256, siteConfig, tempDir } = require('./helpers');
const { createWorld } = require('./world');

const FEED = Buffer.from('<?xml version="1.0"?><rss version="2.0"><channel><title>Digest</title></channel></rss>\n');
const NEWS = '[{"link":"https://example.com/a","title":"A"}]\n';
const DIGEST_ORIGIN = 'https://sentrydigest.ricomanifesto.com/';
const DIGEST_CONFIG = loadSiteConfig(siteConfig());

// A SentryDigest release as its production origin serves it: the complete
// release descriptor, the adapter's build receipt, and the event the
// publisher sends for it.
function digestRelease({ releaseRef = '2'.repeat(40), sourceRevision = '3'.repeat(40), feed = FEED, news = NEWS } = {}) {
  const contentIdentity = {
    digest_content_digest: sha256(news),
    feed_sha256: sha256(feed),
    news_data_sha256: sha256(news),
    newest_issue_date: '2026-01-02',
  };
  const built = buildDescriptor({
    config: DIGEST_CONFIG,
    kind: 'release',
    sourceRevision,
    sourceCommittedAt: '2026-01-02T00:00:00.000Z',
    publicationMode: { mode: 'active', proof: 'on' },
    payloadEntries: [
      { path: 'feed.xml', sha256: sha256(feed), bytes: feed.length },
      { path: 'news-data.json', sha256: sha256(news), bytes: Buffer.byteLength(news) },
    ],
    contentIdentity,
  });
  const receipt = Buffer.from(canonicalJson({
    schema_version: 1,
    repository: 'ricomanifesto/SentryDigest',
    git_ref: 'vercel-production',
    git_commit_sha: releaseRef,
    environment: 'production',
    production_host: 'sentrydigest.ricomanifesto.com',
    release_key: built.releaseKey,
  }));
  const event = {
    schema: 'sentrydigest-release/v1',
    site: 'SentryDigest',
    release_key: built.releaseKey,
    release_ref: releaseRef,
    source_revision: sourceRevision,
    payload_digest: built.payloadDigest,
    digest_content_digest: contentIdentity.digest_content_digest,
    feed_sha256: contentIdentity.feed_sha256,
    news_data_sha256: contentIdentity.news_data_sha256,
  };
  return { event, descriptorBytes: built.bytes, receipt, feed };
}

function consumerRepo(t) {
  const root = tempDir(t, 'admission-world-');
  const remote = path.join(root, 'remote.git');
  const repo = path.join(root, 'consumer');
  git(root, 'init', '--quiet', '--bare', remote);
  fs.mkdirSync(repo);
  git(repo, 'init', '--quiet', '--initial-branch=main');
  git(repo, 'remote', 'add', 'origin', remote);
  fs.writeFileSync(path.join(repo, 'README.md'), 'consumer\n');
  git(repo, 'add', '--all');
  git(repo, 'commit', '--quiet', '-m', 'init');
  git(repo, 'push', '--quiet', 'origin', 'HEAD:refs/heads/main');
  return { repo, remote };
}

function consumerWorld(t, consumer = 'SentryInsight') {
  const { repo, remote } = consumerRepo(t);
  const world = {
    snapshots: new Map(),
    fetched: [],
    recovered: new Set(),
    release: digestRelease(),
  };
  world.serving = world.release;
  world.snapshot = (release, bytes = release.feed) => world.snapshots.set(snapshotFeedUrl(release.event.release_ref), bytes);
  world.snapshot(world.release);
  world.fetchUrl = async (url) => {
    world.fetched.push(url);
    if (url === `${DIGEST_ORIGIN}${LAYOUT.descriptor}` || url === `${DIGEST_ORIGIN}${LAYOUT.receipt}`) {
      if (world.serving === null) throw new Error('ENOTFOUND');
      const body = url.endsWith(LAYOUT.descriptor) ? world.serving.descriptorBytes : world.serving.receipt;
      return { status: 200, headers: new Map(), body };
    }
    if (world.snapshots.has(url)) return { status: 200, headers: new Map(), body: world.snapshots.get(url) };
    return { status: 404, headers: new Map(), body: Buffer.from('404: Not Found') };
  };
  world.admission = (overrides = {}) => createAdmission({
    repoRoot: repo,
    remote,
    config: loadSiteConfig(siteConfig({ site: consumer, repository: `ricomanifesto/${consumer}` })),
    consumer,
    fetchUrl: world.fetchUrl,
    findRecoveredReport: async (key) => world.recovered.has(key),
    gitEnv: GIT_ENV,
    bindingAttempts: 2,
    sleep: async () => {},
    ...overrides,
  });
  world.records = async () => (await world.admission().readState()).records;
  return world;
}

const dispatch = (payload, run = 1, extra = {}) => ({
  eventName: 'repository_dispatch', payload, runId: String(run), runAttempt: '1', readmit: false, ...extra,
});
const scheduled = (run, extra = {}) => ({ eventName: 'schedule', payload: null, runId: String(run), runAttempt: '1', readmit: false, ...extra });

test('a new-shape event is bound to the commit-addressed snapshot before admission', async (t) => {
  const world = consumerWorld(t);
  const { event } = world.release;
  const decision = await world.admission().admit(dispatch(event));
  assert.equal(decision.decision, 'admitted');
  assert.equal(decision.feed_url, `https://raw.githubusercontent.com/ricomanifesto/SentryDigest/${'2'.repeat(40)}/site/feed.xml`);
  assert.equal(decision.binding, 'feed-bytes');
  assert.equal(decision.admission_key, `digest:${'3'.repeat(40)}`);
  assert.ok(!world.fetched.some((url) => url.endsWith('/feed.xml') && !url.includes('raw.githubusercontent.com')));
  const record = (await world.records()).at(-1);
  assert.equal(record.stage, 'admitted');
  assert.equal(record.release_key, event.release_key);
});

test('malformed identity, foreign site and unsafe snapshot inputs are rejected without fetching', async (t) => {
  const world = consumerWorld(t);
  const { event } = world.release;
  for (const payload of [
    { ...event, release_key: 'xyz' },
    { ...event, release_ref: 'main' },
    { ...event, site: 'Other' },
    { ...event, feed_sha256: undefined },
    { ...event, feed_url: 'https://evil.invalid/feed.xml' },
  ]) {
    const decision = await world.admission().admit(dispatch(payload));
    assert.equal(decision.decision, 'rejected-invalid', JSON.stringify(payload));
    assert.equal(decision.exit_code, 1);
  }
  assert.deepEqual(world.fetched, []);
});

test('an event whose identity differs from the serving descriptor and receipt is rejected before any claim', async (t) => {
  const world = consumerWorld(t);
  const { event } = world.release;
  const alternateFeed = Buffer.from('<rss>alternate</rss>\n');
  const alternateRef = 'a'.repeat(40);
  world.snapshots.set(snapshotFeedUrl(alternateRef), alternateFeed);
  for (const [name, payload] of [
    ['source revision', { ...event, source_revision: 'b'.repeat(40) }],
    ['artifact commit and feed', { ...event, release_ref: alternateRef, feed_sha256: sha256(alternateFeed) }],
    ['artifact commit', { ...event, release_ref: alternateRef }],
    ['payload digest', { ...event, payload_digest: 'c'.repeat(64) }],
    ['content digest', { ...event, digest_content_digest: 'd'.repeat(64) }],
    ['news digest', { ...event, news_data_sha256: 'e'.repeat(64) }],
  ]) {
    const decision = await world.admission().admit(dispatch(payload, 7));
    assert.equal(decision.decision, 'rejected-inconsistent', name);
    assert.equal(decision.exit_code, 1, name);
    assert.equal(decision.feed_url, undefined, name);
  }
  assert.ok((await world.records()).every((record) => record.stage !== 'admitted'));

  // A receipt that names another artifact commit also breaks the binding.
  world.serving = { ...world.release, receipt: digestRelease({ releaseRef: alternateRef }).receipt };
  assert.equal((await world.admission().admit(dispatch(event, 8))).decision, 'rejected-inconsistent');
  world.serving = world.release;
  assert.equal((await world.admission().admit(dispatch(event, 9))).decision, 'admitted');
});

test('duplicates, replays and same-content events are skipped without paid work', async (t) => {
  const world = consumerWorld(t);
  const first = await world.admission().admit(dispatch(world.release.event, 1));
  await world.admission().invoked({ admissionKey: first.admission_key, runId: '1' });
  await world.admission().complete({ admissionKey: first.admission_key, runId: '1', outcome: 'published', binding: 'feed-bytes' });

  assert.equal((await world.admission().admit(dispatch(world.release.event, 2))).decision, 'skipped-duplicate');

  const sameContent = digestRelease({ releaseRef: '8'.repeat(40), sourceRevision: '9'.repeat(40) });
  world.serving = sameContent;
  world.snapshot(sameContent);
  assert.equal((await world.admission().admit(dispatch(sameContent.event, 3))).decision, 'skipped-duplicate-content');
});

test('a retry of a completed run starts no new work; a pre-invocation stop stays recoverable', async (t) => {
  const world = consumerWorld(t);
  const done = await world.admission().admit(scheduled(100));
  await world.admission().invoked({ admissionKey: done.admission_key, runId: '100' });
  await world.admission().complete({ admissionKey: done.admission_key, runId: '100', outcome: 'published', binding: 'none' });
  const retry = await world.admission().admit({ ...scheduled(100), runAttempt: '2' });
  assert.equal(retry.decision, 'skipped-duplicate');
  await assert.rejects(world.admission().invoked({ admissionKey: done.admission_key, runId: '100' }), /not claimed by run 100/);

  const evented = await world.admission().admit(dispatch(world.release.event, 101));
  await world.admission().invoked({ admissionKey: evented.admission_key, runId: '101' });
  await world.admission().complete({ admissionKey: evented.admission_key, runId: '101', outcome: 'unchanged', binding: 'feed-bytes' });
  assert.equal((await world.admission().admit({ ...dispatch(world.release.event, 101), runAttempt: '2' })).decision, 'skipped-duplicate');

  // Stopped after admission and before invocation: no paid work happened, so
  // the claim is released and the re-run attempt admits again.
  const stopped = await world.admission().admit(scheduled(102));
  assert.equal(await world.admission().complete({ admissionKey: stopped.admission_key, runId: '102', outcome: 'failed' }), 'abandoned');
  const rerun = await world.admission().admit({ ...scheduled(102), runAttempt: '2' });
  assert.equal(rerun.decision, 'admitted');
});

test('distinct releases cannot both claim the same in-flight content', async (t) => {
  const world = consumerWorld(t);
  const a = await world.admission().admit(dispatch(world.release.event, 1));
  assert.equal(a.decision, 'admitted');

  // The origin advances to release B with the same semantic content before
  // A's run invokes the generator.
  const b = digestRelease({ releaseRef: '8'.repeat(40), sourceRevision: '9'.repeat(40) });
  world.serving = b;
  world.snapshot(b);
  const second = await world.admission().admit(dispatch(b.event, 2));
  assert.equal(second.decision, 'skipped-duplicate-content');
  await assert.rejects(world.admission().invoked({ admissionKey: `digest:${'9'.repeat(40)}`, runId: '2' }), /not claimed by run 2/);
  await world.admission().invoked({ admissionKey: a.admission_key, runId: '1' });
  assert.equal((await world.admission().admit(dispatch(b.event, 3))).decision, 'uncertain');
  const invoked = (await world.records()).filter((record) => record.stage === 'invoked');
  assert.deepEqual(invoked.map((record) => record.admission_key), [a.admission_key]);
});

test('a same-content claim that races another release is decided again at the claim', async (t) => {
  const world = consumerWorld(t);
  const b = digestRelease({ releaseRef: '8'.repeat(40), sourceRevision: '9'.repeat(40) });
  world.snapshot(b);
  const hooks = {};
  let raced = null;
  hooks.beforeClaim = async () => {
    delete hooks.beforeClaim;
    // Between A's checks and its compare-and-set claim, the origin moves to
    // B and B's run claims the same content.
    world.serving = b;
    raced = await world.admission().admit(dispatch(b.event, 2));
  };
  const a = await world.admission({ hooks }).admit(dispatch(world.release.event, 1));
  assert.equal(raced.decision, 'admitted');
  assert.equal(a.decision, 'skipped-duplicate-content');
  const admitted = (await world.records()).filter((record) => record.stage === 'admitted');
  assert.deepEqual(admitted.map((record) => record.admission_key), [`digest:${'9'.repeat(40)}`]);
});

test('staleness and binding failures stop the event before any claim', async (t) => {
  const world = consumerWorld(t);
  const { event } = world.release;
  world.serving = digestRelease({ sourceRevision: 'f'.repeat(40) });
  assert.equal((await world.admission().admit(dispatch(event, 1))).decision, 'superseded-by-origin');

  world.serving = null;
  assert.equal((await world.admission().admit(dispatch(event, 2))).decision, 'binding-unavailable');

  world.serving = world.release;
  world.snapshot(world.release, Buffer.from('<rss>changed</rss>'));
  const mismatch = await world.admission().admit(dispatch(event, 3));
  assert.equal(mismatch.decision, 'binding-failed');
  assert.equal(mismatch.feed_url, undefined);

  world.snapshots.clear();
  const missing = await world.admission().admit(dispatch(event, 4));
  assert.equal(missing.decision, 'binding-failed');
  assert.ok(!world.fetched.includes('https://ricomanifesto.github.io/SentryDigest/feed.xml'));
  assert.ok((await world.records()).every((record) => record.stage !== 'admitted'));
});

test('the mutable feed may change after admission; the generator still receives the accepted snapshot', async (t) => {
  const world = consumerWorld(t);
  const { event } = world.release;
  const decision = await world.admission().admit(dispatch(event, 1));
  world.snapshots.set('https://ricomanifesto.github.io/SentryDigest/feed.xml', Buffer.from('<rss>newer</rss>'));
  world.snapshots.set('https://sentrydigest.ricomanifesto.com/feed.xml', Buffer.from('<rss>newer</rss>'));
  assert.equal(decision.feed_url, snapshotFeedUrl('2'.repeat(40)));
  const resumed = await world.admission().admit(dispatch(event, 1));
  assert.equal(resumed.decision, 'admitted');
  assert.equal(resumed.feed_url, decision.feed_url);
});

test('two concurrent claimants for the same Digest commit admit exactly one, across payload shapes', async (t) => {
  const world = consumerWorld(t);
  const results = await Promise.all([
    world.admission().admit(dispatch(world.release.event, 10)),
    world.admission().admit(dispatch({ ref: 'refs/heads/main', sha: '3'.repeat(40) }, 11)),
  ]);
  assert.deepEqual(results.map((result) => result.decision).sort(), ['admitted', 'skipped-duplicate']);
  const admitted = (await world.records()).filter((record) => record.stage === 'admitted');
  assert.equal(admitted.length, 1);
  assert.equal(admitted[0].admission_key, `digest:${'3'.repeat(40)}`);
});

test('a legacy-shape event is a wake-up without binding', async (t) => {
  const world = consumerWorld(t);
  const decision = await world.admission().admit(dispatch({ ref: 'refs/heads/main', sha: 'a'.repeat(40) }));
  assert.equal(decision.decision, 'admitted');
  assert.equal(decision.binding, 'none');
  assert.equal(decision.feed_url, undefined);
  assert.deepEqual(world.fetched, []);
  assert.equal((await world.admission().admit(dispatch({ ref: 'x', sha: 'not-a-sha' }, 2))).decision, 'rejected-invalid');
});

test('scheduled and manual runs keep their intent even when the content was analyzed before', async (t) => {
  const world = consumerWorld(t);
  const evented = await world.admission().admit(dispatch(world.release.event, 1));
  await world.admission().invoked({ admissionKey: evented.admission_key, runId: '1' });
  await world.admission().complete({ admissionKey: evented.admission_key, runId: '1', outcome: 'published', binding: 'feed-bytes' });

  const daily = await world.admission().admit(scheduled(2));
  assert.equal(daily.decision, 'admitted');
  assert.equal(daily.admission_key, 'run:2');
  assert.equal(daily.feed_url, undefined);
  const manual = await world.admission().admit({ ...scheduled(3), eventName: 'workflow_dispatch' });
  assert.equal(manual.decision, 'admitted');
});

test('a re-run attempt resumes its own record; an earlier pre-invocation stop is safe', async (t) => {
  const world = consumerWorld(t);
  const first = await world.admission().admit(scheduled(5));
  const rerun = await world.admission().admit({ ...scheduled(5), runAttempt: '2' });
  assert.equal(rerun.decision, 'admitted');
  assert.equal(rerun.resumed, true);
  assert.equal(rerun.admission_key, first.admission_key);

  // Run 5 stopped before invoking; the next run is not blocked by it.
  assert.equal((await world.admission().admit(scheduled(6))).decision, 'admitted');
});

test('a recovered bound report keeps its content identity, so the same content is not generated again', async (t) => {
  const world = consumerWorld(t);
  const { event } = world.release;
  const a = await world.admission().admit(dispatch(event, 50));
  await world.admission().invoked({ admissionKey: a.admission_key, runId: '50' });
  world.recovered.add(a.admission_key);

  // Release B serves the same analyzed content under another source; its
  // admission recovers A's report first, then must see A's content.
  const b = digestRelease({ releaseRef: '8'.repeat(40), sourceRevision: '9'.repeat(40) });
  world.serving = b;
  world.snapshot(b);
  const next = await world.admission().admit(dispatch(b.event, 51));
  assert.equal(next.decision, 'skipped-duplicate-content');
  await assert.rejects(world.admission().invoked({ admissionKey: `digest:${'9'.repeat(40)}`, runId: '51' }), /not claimed by run 51/);

  const recovered = (await world.records()).find((record) => record.stage === 'completed' && record.outcome === 'recovered');
  assert.equal(recovered.admission_key, a.admission_key);
  assert.equal(recovered.digest_content_digest, event.digest_content_digest);
  assert.equal(recovered.release_key, event.release_key);
  assert.equal(recovered.binding, 'feed-bytes');

  // A new scheduled intent is not deduplicated by content.
  const daily = await world.admission().admit(scheduled(52));
  assert.equal(daily.decision, 'admitted');
  await world.admission().invoked({ admissionKey: daily.admission_key, runId: '52' });
});

test('an unresolved invocation stops an already-admitted claim at the invocation boundary', async (t) => {
  const world = consumerWorld(t, 'GRCInsight');
  // Both intents are admitted before either starts.
  const first = await world.admission().admit(scheduled(60));
  const second = await world.admission().admit({ ...scheduled(61), eventName: 'workflow_dispatch' });
  assert.equal(first.decision, 'admitted');
  assert.equal(second.decision, 'admitted');

  await world.admission().invoked({ admissionKey: first.admission_key, runId: '60' });
  await assert.rejects(world.admission().invoked({ admissionKey: second.admission_key, runId: '61' }), /run:60 has an unresolved invocation/);
  let records = await world.records();
  assert.deepEqual(records.filter((record) => record.stage === 'invoked').map((record) => record.admission_key), ['run:60']);
  // The refused claim is released: no paid work started under it.
  assert.equal(records.filter((record) => record.admission_key === 'run:61').at(-1).stage, 'abandoned');

  // The running claim may still record its report handle.
  await world.admission().invoked({ admissionKey: first.admission_key, runId: '60', handle: 'report-60' });
  await world.admission().complete({ admissionKey: first.admission_key, runId: '60', outcome: 'published', binding: 'none' });

  // After a conclusive completion a new intent starts normally.
  const later = await world.admission().admit(scheduled(62));
  await world.admission().invoked({ admissionKey: later.admission_key, runId: '62' });
  await world.admission().complete({ admissionKey: later.admission_key, runId: '62', outcome: 'failed' });

  // After explicit readmission of the unresolved run, a new intent starts too.
  const readmitted = await world.admission().admit({ ...scheduled(63), eventName: 'workflow_dispatch', readmit: true });
  assert.equal(readmitted.decision, 'admitted');
  await world.admission().invoked({ admissionKey: readmitted.admission_key, runId: '63' });
  records = await world.records();
  assert.ok(records.some((record) => record.stage === 'readmitted' && record.admission_key === 'run:62'));
});

test('only the run holding a claim may start generation, and never after its claim was released', async (t) => {
  const world = consumerWorld(t);
  const claim = await world.admission().admit(scheduled(1));
  await assert.rejects(world.admission().invoked({ admissionKey: claim.admission_key, runId: '2' }), /not claimed by run 2/);
  await world.admission().invoked({ admissionKey: claim.admission_key, runId: '1' });
  await world.admission().admit(scheduled(3, { readmit: true }));
  await assert.rejects(world.admission().invoked({ admissionKey: claim.admission_key, runId: '1' }), /not claimed by run 1/);
  await assert.rejects(world.admission().complete({ admissionKey: claim.admission_key, runId: '1', outcome: 'published' }), /not in flight/);
});

test('Insight: an uncertain invocation is recovered from a bound report or held until readmitted', async (t) => {
  const world = consumerWorld(t, 'SentryInsight');
  const crashed = await world.admission().admit(scheduled(1));
  await world.admission().invoked({ admissionKey: crashed.admission_key, runId: '1' });

  const blocked = await world.admission().admit(scheduled(2));
  assert.equal(blocked.decision, 'uncertain');
  assert.equal(blocked.exit_code, 0);
  assert.equal(blocked.uncertain_key, crashed.admission_key);
  const rerunSame = await world.admission().admit({ ...scheduled(1), runAttempt: '2' });
  assert.equal(rerunSame.decision, 'uncertain');

  world.recovered.add(crashed.admission_key);
  const proceeds = await world.admission().admit(scheduled(3));
  assert.equal(proceeds.decision, 'admitted');
  assert.ok((await world.records()).some((record) => record.admission_key === crashed.admission_key && record.stage === 'completed' && record.outcome === 'recovered'));

  const second = await world.admission().admit(scheduled(4));
  await world.admission().invoked({ admissionKey: second.admission_key, runId: '4' });
  assert.equal((await world.admission().admit(scheduled(7))).decision, 'uncertain');
  const readmitted = await world.admission().admit(scheduled(8, { readmit: true }));
  assert.equal(readmitted.decision, 'admitted');
  assert.ok((await world.records()).some((record) => record.admission_key === second.admission_key && record.stage === 'readmitted'));
});

test('a cancelled or failed generation after invocation stays uncertain until recovery or readmission', async (t) => {
  const world = consumerWorld(t, 'SentryInsight');
  for (const [run, outcome] of [[30, 'cancelled'], [40, 'failed']]) {
    const claim = await world.admission().admit(scheduled(run));
    await world.admission().invoked({ admissionKey: claim.admission_key, runId: String(run) });
    assert.equal(await world.admission().complete({ admissionKey: claim.admission_key, runId: String(run), outcome }), 'unresolved');
    const next = await world.admission().admit(scheduled(run + 1));
    assert.equal(next.decision, 'uncertain', outcome);
    assert.equal(next.uncertain_key, claim.admission_key);
    assert.equal((await world.admission().admit({ ...scheduled(run), runAttempt: '2' })).decision, 'uncertain');
    assert.equal((await world.admission().admit(scheduled(run + 2, { readmit: true }))).decision, 'admitted');
    await world.admission().complete({ admissionKey: `run:${run + 2}`, runId: String(run + 2), outcome: 'failed' });
  }
  const records = await world.records();
  assert.ok(records.some((record) => record.stage === 'unresolved' && record.outcome === 'cancelled'));
  assert.ok(!records.some((record) => record.stage === 'completed' && ['cancelled', 'failed'].includes(record.outcome)));
});

test('GRC: an uncertain invocation with a report handle is re-attached, without one it is held', async (t) => {
  const world = consumerWorld(t, 'GRCInsight');
  const invoked = await world.admission().admit(dispatch(world.release.event, 1));
  await world.admission().invoked({ admissionKey: invoked.admission_key, runId: '1' });
  await world.admission().invoked({ admissionKey: invoked.admission_key, runId: '1', handle: 'report-123' });

  const reattach = await world.admission().admit(scheduled(2));
  assert.equal(reattach.decision, 'reattach');
  assert.equal(reattach.reattach_handle, 'report-123');
  assert.equal(reattach.admission_key, invoked.admission_key);
  assert.equal(reattach.feed_url, snapshotFeedUrl('2'.repeat(40)));
  await world.admission().complete({ admissionKey: invoked.admission_key, runId: '2', outcome: 'published', binding: 'feed-bytes' });

  const noHandle = await world.admission().admit(scheduled(3));
  await world.admission().invoked({ admissionKey: noHandle.admission_key, runId: '3' });
  const other = digestRelease({ sourceRevision: 'b'.repeat(40), news: '[{"id":"other"}]\n' });
  world.serving = other;
  const held = await world.admission().admit(dispatch(other.event, 4));
  assert.equal(held.decision, 'uncertain');
  assert.equal((await world.admission().admit(scheduled(5, { readmit: true }))).decision, 'admitted');
});

test('GRC: explicit readmission releases a saved handle that can no longer be retrieved', async (t) => {
  const world = consumerWorld(t, 'GRCInsight');
  const claim = await world.admission().admit(scheduled(1));
  await world.admission().invoked({ admissionKey: claim.admission_key, runId: '1', handle: 'report-gone' });
  // Without an explicit readmission the handle is re-attached, never released.
  assert.equal((await world.admission().admit(scheduled(2))).decision, 'reattach');
  assert.equal((await world.admission().admit(scheduled(3))).decision, 'reattach');

  const readmitted = await world.admission().admit(scheduled(4, { readmit: true }));
  assert.equal(readmitted.decision, 'admitted');
  assert.equal(readmitted.admission_key, 'run:4');
  const released = (await world.records()).find((record) => record.stage === 'readmitted');
  assert.equal(released.admission_key, claim.admission_key);
  assert.equal(released.abandoned_handle, 'report-gone');
});

test('recovered-report evidence needs the exact key, the report path and the bound feed', async (t) => {
  const { repo } = consumerRepo(t);
  const repoGit = createGit(repo, { env: GIT_ENV });
  const feed = snapshotFeedUrl('2'.repeat(40));
  const digestKey = `digest:${'3'.repeat(40)}`;
  const commit = (files, message) => {
    for (const [name, text] of Object.entries(files)) fs.writeFileSync(path.join(repo, name), text);
    git(repo, 'add', '--all');
    git(repo, 'commit', '--quiet', '-m', message);
    return git(repo, 'rev-parse', 'HEAD');
  };
  const find = (key, feedUrl) => findAdmissionReport({ git: repoGit, ref: 'HEAD', key, feedUrl, reportPath: 'index.md' });

  commit({ 'index.md': 'report 12\n' }, 'Update exploitation report [automated]\n\nAdmission-Key: run:12\nAdmission-Feed: none');
  commit({ 'notes.md': 'x\n' }, 'Unrelated\n\nAdmission-Key: run:1\nAdmission-Feed: none');
  commit({ 'index.md': 'mentions\n' }, 'Mentions Admission-Key: run:1 in prose\n\nSee Admission-Key: run:1 above.');
  assert.equal(find('run:1'), null);
  assert.ok(find('run:12'));

  commit({ 'index.md': 'other feed\n' }, `Update exploitation report [automated]\n\nAdmission-Key: ${digestKey}\nAdmission-Feed: ${snapshotFeedUrl('8'.repeat(40))}`);
  assert.equal(find(digestKey, feed), null);
  const bound = commit({ 'index.md': 'bound report\n' }, `Update exploitation report [automated]\n\nAdmission-Key: ${digestKey}\nAdmission-Feed: ${feed}`);
  assert.equal(find(digestKey, feed), bound);
  assert.equal(find('run:1'), null);
});

test('a real published release event is admitted, and a mixed identity against it is rejected', async (t) => {
  const ACTIVE = { mode: 'active', proof: 'on' };
  const digest = createWorld(t, { publication: ACTIVE });
  const source = digest.commitSource(digest.payload, ACTIVE);
  await digest.publisher().publish({ sourceRevision: source });
  digest.deploy();
  await digest.publisher().resume();
  const event = digest.dispatched.find((entry) => entry.consumer === 'SentryInsight').payload;

  // Raw snapshots resolve against the artifact remote, plus one alternate
  // commit whose feed bytes match an alternate hash.
  const raw = 'https://raw.githubusercontent.com/ricomanifesto/SentryDigest/';
  const alternateRef = 'a'.repeat(40);
  const alternateFeed = Buffer.from('<rss>alternate</rss>\n');
  const fetchUrl = async (url) => {
    if (url === snapshotFeedUrl(alternateRef)) return { status: 200, headers: new Map(), body: alternateFeed };
    if (url.startsWith(raw)) {
      const [ref, ...rest] = url.slice(raw.length).split('/');
      const shown = childProcess.spawnSync('git', ['show', `${ref}:${rest.join('/')}`], { cwd: digest.remote, env: GIT_ENV });
      return shown.status === 0 ? { status: 200, headers: new Map(), body: shown.stdout } : { status: 404, headers: new Map(), body: Buffer.from('') };
    }
    return digest.served.fetchUrl(url);
  };
  const world = consumerWorld(t);
  const admitted = await world.admission({ fetchUrl }).admit(dispatch(event, 1));
  assert.equal(admitted.decision, 'admitted');
  assert.equal(admitted.feed_url, snapshotFeedUrl(digest.remoteTip('vercel-production')));

  const mixed = { ...event, source_revision: 'b'.repeat(40), release_ref: alternateRef, feed_sha256: sha256(alternateFeed) };
  const rejected = await consumerWorld(t).admission({ fetchUrl }).admit(dispatch(mixed, 2));
  assert.equal(rejected.decision, 'rejected-inconsistent');
  assert.equal(rejected.exit_code, 1);
});

const requestIdentity = (key, runId = '800', extra = {}) => ({
  admissionKey: key, runId, revision: 'a'.repeat(40), requestSha256: 'b'.repeat(64), limit: 3, ...extra,
});
async function requestWorld(t) {
  const world = consumerWorld(t);
  const claim = await world.admission().admit({ eventName: 'workflow_dispatch', payload: {}, runId: '800', runAttempt: '1' });
  await world.admission().invoked({ admissionKey: claim.admission_key, runId: '800' });
  return { world, bound: requestIdentity(claim.admission_key) };
}

test('request budget survives new callers and caps all attempts, not each process', async (t) => {
  const { world, bound } = await requestWorld(t);
  for (let attempt = 1; attempt <= 3; attempt += 1) {
    const reservation = await world.admission().reserveRequest(bound);
    assert.equal(reservation.attempt, attempt);
    await world.admission().finishRequest({ ...bound, ...reservation, disposition: 'retryable_rejection', retryAfterSeconds: 0 });
  }
  await assert.rejects(world.admission().reserveRequest(bound), /exhausted/);
  assert.equal((await world.records()).filter((r) => r.stage === 'request_reserved').length, 3);
});

test('only one concurrent caller reserves an attempt and missing completion stays held', async (t) => {
  const { world, bound } = await requestWorld(t);
  const results = await Promise.allSettled([world.admission().reserveRequest(bound), world.admission().reserveRequest(bound)]);
  assert.equal(results.filter((r) => r.status === 'fulfilled').length, 1);
  assert.equal(results.filter((r) => r.status === 'rejected').length, 1);
  await assert.rejects(world.admission().reserveRequest(bound), /held/);
  assert.equal((await world.records()).filter((r) => r.stage === 'request_reserved').length, 1);
});

test('request identity, total cap, run ownership and source cannot change after reservation', async (t) => {
  const { world, bound } = await requestWorld(t);
  const reservation = await world.admission().reserveRequest(bound);
  await world.admission().finishRequest({ ...bound, ...reservation, disposition: 'retryable_rejection', retryAfterSeconds: 0 });
  for (const extra of [{ requestSha256: 'c'.repeat(64) }, { revision: 'd'.repeat(40) }, { limit: 2 }, { runId: '801' }]) {
    await assert.rejects(world.admission().reserveRequest({ ...bound, ...extra }), /identity|owned/);
  }
});

test('terminal, uncertain and deferred request dispositions never permit replay', async (t) => {
  for (const disposition of ['response_received', 'permanent_rejection', 'uncertain', 'deferred_rejection']) {
    await t.test(disposition, async (sub) => {
      const { world, bound } = await requestWorld(sub);
      const reservation = await world.admission().reserveRequest(bound);
      await world.admission().finishRequest({ ...bound, ...reservation, disposition, retryAfterSeconds: 0 });
      await assert.rejects(world.admission().reserveRequest(bound), /held/);
      await assert.rejects(world.admission().finishRequest({ ...bound, ...reservation, disposition: 'retryable_rejection', retryAfterSeconds: 0 }), /not owned/);
    });
  }
});

test('request Retry-After survives a restart and cannot be ignored', async (t) => {
  const { world, bound } = await requestWorld(t);
  let at = new Date('2026-11-03T00:00:00Z');
  const actor = () => world.admission({ now: () => at });
  const reservation = await actor().reserveRequest(bound);
  await actor().finishRequest({ ...bound, ...reservation, disposition: 'retryable_rejection', retryAfterSeconds: 20 });
  await assert.rejects(actor().reserveRequest(bound), /delay not elapsed/);
  at = new Date('2026-11-03T00:00:21Z');
  assert.equal((await actor().reserveRequest(bound)).attempt, 2);
});

test('stale reservation tokens and invalid finish metadata cannot release budget', async (t) => {
  const { world, bound } = await requestWorld(t);
  const reservation = await world.admission().reserveRequest(bound);
  for (const extra of [{ token: 'c'.repeat(32) }, { attempt: 2 }, { disposition: 'private-answer' }, { retryAfterSeconds: Infinity }]) {
    await assert.rejects(world.admission().finishRequest({ ...bound, ...reservation, disposition: 'retryable_rejection', retryAfterSeconds: 0, ...extra }));
  }
  await assert.rejects(world.admission().reserveRequest(bound), /held/);
});

test('later workflow or explicit readmission does not reset prior request budget', async (t) => {
  const { world, bound } = await requestWorld(t);
  await world.admission().reserveRequest(bound);
  const next = await world.admission().admit({ eventName: 'workflow_dispatch', payload: {}, runId: '801', runAttempt: '1' });
  assert.equal(next.decision, 'uncertain');
  await assert.rejects(world.admission().reserveRequest({ ...bound, runId: '801' }), /owned/);
  await world.admission().admit({ eventName: 'workflow_dispatch', payload: {}, runId: '802', runAttempt: '1', readmit: true });
  await assert.rejects(world.admission().reserveRequest(bound), /owned/);
});

test('trusted readmission creates a new digest episode without reviving stale request tokens', async (t) => {
  const world = consumerWorld(t);
  const digest = { sha: '8'.repeat(40), ref: 'refs/heads/main' };
  const original = await world.admission().admit(dispatch(digest, 800));
  await world.admission().invoked({ admissionKey: original.admission_key, runId: '800' });
  const oldBound = requestIdentity(original.admission_key);
  const oldReservation = await world.admission().reserveRequest(oldBound);
  // This is the real workflow shape: explicit manual readmission, followed by a
  // later Digest delivery, not an invented caller ID or a reset inside a client.
  const manual = await world.admission().admit({ eventName: 'workflow_dispatch', payload: {}, runId: '801', runAttempt: '1', readmit: true });
  assert.equal(manual.decision, 'admitted');
  await world.admission().invoked({ admissionKey: manual.admission_key, runId: '801' });
  await world.admission().complete({ admissionKey: manual.admission_key, runId: '801', outcome: 'unchanged' });
  const admitted = await world.admission().admit(dispatch(digest, 802));
  assert.equal(admitted.decision, 'admitted');
  await world.admission().invoked({ admissionKey: admitted.admission_key, runId: '802' });
  const bound = requestIdentity(admitted.admission_key, '802');
  const fresh = await world.admission().reserveRequest(bound);
  assert.equal(fresh.attempt, 1);
  await assert.rejects(world.admission().finishRequest({ ...oldBound, ...oldReservation, disposition: 'retryable_rejection', retryAfterSeconds: 0 }), /not owned/);
  await assert.rejects(world.admission().finishRequest({ ...bound, ...oldReservation, disposition: 'retryable_rejection', retryAfterSeconds: 0 }), /not owned/);
  await world.admission().finishRequest({ ...bound, ...fresh, disposition: 'retryable_rejection', retryAfterSeconds: 0 });
  await world.admission().invoked({ admissionKey: bound.admissionKey, runId: '802' });
  assert.equal((await world.admission().reserveRequest(bound)).attempt, 2);
  const records = await world.records();
  assert.ok(records.some((r) => r.stage === 'request_reserved' && r.token === oldReservation.token));
});

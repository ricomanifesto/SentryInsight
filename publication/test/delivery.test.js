const assert = require('node:assert/strict');
const test = require('node:test');

const { createWorld } = require('./world');

const ACTIVE = { mode: 'active', proof: 'on' };
const PREPARE = { mode: 'prepare', proof: 'on' };

async function servedRelease(world, files, publication = ACTIVE, message = 'release') {
  const source = world.commitSource(files, publication, message);
  const result = await world.publisher().publish({ sourceRevision: source });
  world.deploy();
  const resumed = await world.publisher().resume();
  return { source, result, resumed };
}

function deliveryRecords(records, releaseKey) {
  return records.filter((record) => record.stage === 'delivery' && record.release_key === releaseKey);
}

function lastStatus(records, releaseKey, consumer) {
  return deliveryRecords(records, releaseKey).filter((record) => record.consumer === consumer).at(-1)?.status;
}

test('a serving active release is delivered once to each consumer with the bound identity', async (t) => {
  const world = createWorld(t, { publication: ACTIVE });
  const { result } = await servedRelease(world, world.payload);
  assert.deepEqual(world.dispatched.map((entry) => entry.consumer).sort(), ['GRCInsight', 'SentryInsight']);
  const payload = world.dispatched[0].payload;
  assert.deepEqual(Object.keys(payload).sort(), [
    'digest_content_digest', 'feed_sha256', 'news_data_sha256', 'payload_digest', 'release_key',
    'release_ref', 'schema', 'site', 'source_revision',
  ]);
  assert.equal(payload.release_key, result.release_key);
  assert.equal(payload.release_ref, world.remoteTip('vercel-production'));
  const records = await world.records();
  assert.equal(lastStatus(records, result.release_key, 'SentryInsight'), 'sent');
  assert.equal(lastStatus(records, result.release_key, 'GRCInsight'), 'sent');

  await world.publisher().resume();
  assert.equal(world.dispatched.length, 2);
});

test('a hosting-only release is ineligible and a same-link content correction is eligible', async (t) => {
  const world = createWorld(t, { publication: ACTIVE });
  await servedRelease(world, world.payload);
  world.dispatched.length = 0;

  const hosting = await servedRelease(world, { 'index.html': '<!doctype html><title>restyled</title>\n' }, ACTIVE, 'hosting');
  assert.equal(world.dispatched.length, 0);
  assert.equal(lastStatus(await world.records(), hosting.result.release_key, 'SentryInsight'), 'ineligible');

  const corrected = await servedRelease(world, { 'news-data.json': '[{"link":"https://example.com/a","title":"Corrected title"}]\n' }, ACTIVE, 'correction');
  assert.deepEqual(world.dispatched.map((entry) => entry.consumer).sort(), ['GRCInsight', 'SentryInsight']);
  assert.equal(lastStatus(await world.records(), corrected.result.release_key, 'GRCInsight'), 'sent');
});

test('a rollback release records not-applicable and wakes no consumer', async (t) => {
  const world = createWorld(t, { publication: ACTIVE });
  const first = await servedRelease(world, world.payload);
  await servedRelease(world, { 'news-data.json': '[{"id":2}]\n' }, ACTIVE, 'second');
  world.dispatched.length = 0;

  const rolled = await world.publisher().rollback({ targetReleaseKey: first.result.release_key, reason: 'operator' });
  world.deploy();
  await world.publisher().resume();
  assert.equal(world.dispatched.length, 0);
  const records = await world.records();
  assert.equal(lastStatus(records, rolled.release_key, 'SentryInsight'), 'not-applicable');
  assert.equal(lastStatus(records, rolled.release_key, 'GRCInsight'), 'not-applicable');
});

test('an uncertain send is resent and a partial delivery resumes only the missing consumer', async (t) => {
  const world = createWorld(t, { publication: ACTIVE });
  let calls = 0;
  world.hooks.dispatch = (consumer) => {
    calls += 1;
    if (consumer.name === 'GRCInsight') throw new Error('dispatch rejected: 502');
  };
  const { result } = await servedRelease(world, world.payload);
  let records = await world.records();
  assert.equal(lastStatus(records, result.release_key, 'SentryInsight'), 'sent');
  assert.equal(lastStatus(records, result.release_key, 'GRCInsight'), 'failed');
  assert.ok(records.some((record) => record.stage === 'delivery-summary' && record.release_key === result.release_key && record.status === 'partial'));

  world.hooks.dispatch = (consumer) => {
    calls += 1;
    if (consumer.name === 'SentryInsight') throw new Error('Insight must not be resent');
  };
  world.dispatched.length = 0;
  await world.publisher().resume();
  assert.deepEqual(world.dispatched.map((entry) => entry.consumer), ['GRCInsight']);
  records = await world.records();
  assert.equal(lastStatus(records, result.release_key, 'GRCInsight'), 'sent');

  // A crash between the provider call and the sent record leaves "sending":
  // the next run records it as uncertain and sends again (at least once).
  const crash = createWorld(t, { publication: ACTIVE });
  crash.hooks.afterDispatch = (consumer) => {
    if (consumer.name === 'SentryInsight') throw new Error('crashed after dispatch');
  };
  const source = crash.commitSource(crash.payload, ACTIVE);
  const released = await crash.publisher().publish({ sourceRevision: source });
  crash.deploy();
  await assert.rejects(crash.publisher().resume(), /crashed after dispatch/);
  assert.equal(lastStatus(await crash.records(), released.release_key, 'SentryInsight'), 'sending');
  delete crash.hooks.afterDispatch;
  await crash.publisher().resume();
  const after = deliveryRecords(await crash.records(), released.release_key).filter((record) => record.consumer === 'SentryInsight');
  assert.deepEqual(after.map((record) => record.status), ['pending', 'sending', 'uncertain', 'sending', 'sent']);
  assert.equal(crash.dispatched.filter((entry) => entry.consumer === 'SentryInsight').length, 2);
});

function lastSummary(records, releaseKey) {
  return records.filter((record) => record.stage === 'delivery-summary' && record.release_key === releaseKey).at(-1);
}

test('a partial delivery is held while the origin is unavailable and resumes only the missing consumer', async (t) => {
  const world = createWorld(t, { publication: ACTIVE });
  world.hooks.dispatch = (consumer) => {
    if (consumer.name === 'GRCInsight') throw new Error('dispatch rejected: 502');
  };
  const { result } = await servedRelease(world, world.payload);
  assert.equal(lastStatus(await world.records(), result.release_key, 'GRCInsight'), 'failed');

  // The origin disappears; the old serving record must not authorize a send.
  delete world.hooks.dispatch;
  world.served = null;
  world.dispatched.length = 0;
  const offline = await world.publisher().resume();
  assert.equal(offline.tip.delivery.status, 'held');
  assert.deepEqual(world.dispatched, []);
  assert.equal(lastSummary(await world.records(), result.release_key).status, 'held');
  assert.equal(lastStatus(await world.records(), result.release_key, 'GRCInsight'), 'failed');

  world.deploy();
  const restored = await world.publisher().resume();
  assert.equal(restored.tip.delivery.status, 'delivered');
  assert.deepEqual(world.dispatched.map((entry) => entry.consumer), ['GRCInsight']);
});

test('a partial delivery is held while the origin serves another release', async (t) => {
  const world = createWorld(t, { publication: ACTIVE });
  const first = await servedRelease(world, world.payload, ACTIVE, 'first');
  const firstCommit = first.result.release_ref;
  world.hooks.dispatch = (consumer) => {
    if (consumer.name === 'GRCInsight') throw new Error('dispatch rejected: 502');
  };
  const second = await servedRelease(world, { 'news-data.json': '[{"id":"second"}]\n' }, ACTIVE, 'second');
  assert.equal(lastStatus(await world.records(), second.result.release_key, 'GRCInsight'), 'failed');

  delete world.hooks.dispatch;
  world.deploy(firstCommit);
  world.dispatched.length = 0;
  const moved = await world.publisher().resume();
  assert.equal(moved.tip.delivery.status, 'held');
  assert.deepEqual(world.dispatched, []);

  world.deploy();
  await world.publisher().resume();
  assert.deepEqual(world.dispatched.map((entry) => entry.payload.release_key), [second.result.release_key]);
});

test('an authority change between consumers holds the remaining sends', async (t) => {
  const world = createWorld(t, { publication: ACTIVE });
  world.hooks.dispatch = (consumer) => {
    if (consumer.name === 'SentryInsight') world.mainHeadPublication = { mode: 'prepare', proof: 'on' };
  };
  const { result } = await servedRelease(world, world.payload);
  assert.deepEqual(world.dispatched.map((entry) => entry.consumer), ['SentryInsight']);
  let records = await world.records();
  assert.equal(lastStatus(records, result.release_key, 'GRCInsight'), undefined);
  assert.equal(lastSummary(records, result.release_key).status, 'held');

  delete world.hooks.dispatch;
  world.mainHeadPublication = null;
  await world.publisher().resume();
  assert.deepEqual(world.dispatched.map((entry) => entry.consumer), ['SentryInsight', 'GRCInsight']);
  records = await world.records();
  assert.equal(lastStatus(records, result.release_key, 'GRCInsight'), 'sent');
});

test('a newer serving release supersedes an older incomplete delivery and is delivered once', async (t) => {
  const world = createWorld(t, { publication: ACTIVE });
  world.hooks.dispatch = (consumer) => {
    if (consumer.name === 'GRCInsight') throw new Error('dispatch rejected: 502');
  };
  const a = world.commitSource(world.payload, ACTIVE, 'A');
  const releaseA = await world.publisher().publish({ sourceRevision: a });
  world.deploy();
  await world.publisher().resume();

  const b = world.commitSource({ 'news-data.json': '[{"id":"b"}]\n' }, ACTIVE, 'B');
  const releaseB = await world.publisher().publish({ sourceRevision: b });
  assert.equal(releaseB.outcome, 'verification-failed');
  delete world.hooks.dispatch;
  world.deploy();
  await world.publisher().resume();

  const records = await world.records();
  assert.equal(lastStatus(records, releaseA.release_key, 'SentryInsight'), 'sent');
  assert.equal(lastStatus(records, releaseA.release_key, 'GRCInsight'), 'superseded');
  assert.equal(lastStatus(records, releaseB.release_key, 'SentryInsight'), 'sent');
  assert.equal(lastStatus(records, releaseB.release_key, 'GRCInsight'), 'sent');
  const grc = world.dispatched.filter((entry) => entry.consumer === 'GRCInsight');
  assert.deepEqual(grc.map((entry) => entry.payload.release_key), [releaseB.release_key]);
});

test('delivery waits for active authority at both the release and the current main head', async (t) => {
  const world = createWorld(t, { publication: PREPARE });
  const { result } = await servedRelease(world, world.payload, PREPARE);
  assert.equal(world.dispatched.length, 0);
  assert.equal(lastStatus(await world.records(), result.release_key, 'SentryInsight'), undefined);

  const active = createWorld(t, { publication: ACTIVE });
  active.mainHeadPublication = PREPARE;
  const activeRelease = await servedRelease(active, active.payload);
  assert.equal(active.dispatched.length, 0);
  const records = await active.records();
  assert.ok(records.some((record) => record.stage === 'delivery-summary' && record.release_key === activeRelease.result.release_key && record.status === 'awaiting-authority'));

  active.mainHeadPublication = null;
  await active.publisher().resume();
  assert.equal(active.dispatched.length, 2);
});

test('the attested seed wakes only a consumer whose last legacy notification failed', async (t) => {
  const world = createWorld(t, { publication: ACTIVE });
  const legacy = world.commitSource(world.payload, PREPARE, 'last legacy dispatch');
  await assert.rejects(world.publisher().seed({ consumers: { SentryInsight: legacy }, attestation: '' }), /attestation/);
  await assert.rejects(world.publisher().seed({ consumers: { Unknown: 'none' }, attestation: 'x' }), /consumer/);
  await world.publisher().seed({
    consumers: { SentryInsight: legacy, GRCInsight: 'none' },
    attestation: 'Actions history: Insight dispatch run succeeded; GRC dispatch failed',
  });

  await servedRelease(world, {}, ACTIVE, 'activation');
  assert.deepEqual(world.dispatched.map((entry) => entry.consumer), ['GRCInsight']);
});

test('a missed publisher invocation is recovered by the next ordinary run', async (t) => {
  const world = createWorld(t, { publication: ACTIVE });
  const source = world.commitSource(world.payload, ACTIVE);
  world.hooks.beforeDelivery = () => { throw new Error('runner lost'); };
  await world.publisher().publish({ sourceRevision: source });
  world.deploy();
  await assert.rejects(world.publisher().resume(), /runner lost/);
  assert.equal(world.dispatched.length, 0);

  delete world.hooks.beforeDelivery;
  const noChange = await world.publisher().publish({ sourceRevision: source });
  assert.equal(noChange.outcome, 'no-op');
  assert.equal(world.dispatched.length, 2);
});

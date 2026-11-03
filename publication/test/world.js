// A disposable publication world: a source repository, a file-transport bare
// remote holding the artifact and state branches, and a fake provider that
// builds the remote artifact tip with the real adapter and serves the result.
const childProcess = require('node:child_process');
const fs = require('node:fs');
const path = require('node:path');

const { inventoryOfDir } = require('../kit/canonical');
const { loadSiteConfig } = require('../kit/config');
const { LAYOUT } = require('../kit/release');
const { createPublisher } = require('../kit/publisher');
const { GIT_ENV, PAYLOAD, fakeOrigin, git, sha256, siteConfig, tempDir, writeFiles } = require('./helpers');

function createWorld(t, { publication = { mode: 'prepare', proof: 'off' }, configOverrides = {} } = {}) {
  const root = tempDir(t, 'publication-world-');
  const source = path.join(root, 'source');
  const remote = path.join(root, 'remote.git');
  fs.mkdirSync(source);
  git(root, 'init', '--quiet', '--bare', remote);
  git(source, 'init', '--quiet', '--initial-branch=main');
  git(source, 'remote', 'add', 'origin', remote);

  const world = {
    root,
    source,
    remote,
    served: null,
    dispatched: [],
    mainHeadPublication: null,
    failBuild: null,
    hooks: {},
  };

  world.commitSource = (files, publicationState = publication, message = 'source') => {
    writeFiles(source, Object.fromEntries(Object.entries(files).map(([p, c]) => [`public/${p}`, c])));
    fs.mkdirSync(path.join(source, 'publication'), { recursive: true });
    fs.writeFileSync(
      path.join(source, 'publication', 'site.json'),
      `${JSON.stringify(siteConfig({ ...configOverrides, publication: publicationState }), null, 2)}\n`,
    );
    git(source, 'add', '--all');
    git(source, 'commit', '--quiet', '--allow-empty', '-m', message);
    git(source, 'push', '--quiet', 'origin', 'HEAD:refs/heads/main');
    return git(source, 'rev-parse', 'HEAD');
  };

  // Validated payload build for a source revision (a stand-in for the
  // repository's static builder, which has its own tests).
  world.buildPayload = async ({ sourceRevision }) => {
    if (world.failBuild) throw new Error(world.failBuild);
    const dir = fs.mkdtempSync(path.join(root, 'payload-'));
    const archive = childProcess.execFileSync('git', ['archive', '--format=tar', sourceRevision, 'public'], { cwd: source, env: GIT_ENV });
    childProcess.execFileSync('tar', ['-x', '-C', dir, '--strip-components=1'], { input: archive });
    const news = fs.readFileSync(path.join(dir, 'news-data.json'));
    return {
      payloadDir: dir,
      contentIdentity: {
        digest_content_digest: sha256(news),
        feed_sha256: sha256(fs.readFileSync(path.join(dir, 'feed.xml'))),
        news_data_sha256: sha256(news),
        newest_issue_date: '2026-01-02',
      },
    };
  };

  // The provider builds the artifact tip (or a given commit) with the adapter
  // and the alias starts serving it.
  world.deploy = (commit = world.remoteTip('vercel-production'), env = {}) => {
    const dir = fs.mkdtempSync(path.join(root, 'deployment-'));
    const archive = childProcess.execFileSync('git', ['archive', '--format=tar', commit], { cwd: remote, env: GIT_ENV });
    childProcess.execFileSync('tar', ['-x', '-C', dir], { input: archive });
    const run = childProcess.spawnSync(process.execPath, [path.join(dir, ...LAYOUT.adapter.split('/'))], {
      cwd: dir,
      encoding: 'utf8',
      env: {
        PATH: process.env.PATH,
        VERCEL_ENV: 'production',
        VERCEL_GIT_COMMIT_REF: 'vercel-production',
        VERCEL_GIT_COMMIT_SHA: commit,
        VERCEL_GIT_REPO_OWNER: 'ricomanifesto',
        VERCEL_GIT_REPO_SLUG: 'SentryDigest',
        VERCEL_PROJECT_PRODUCTION_URL: 'sentrydigest.ricomanifesto.com',
        ...env,
      },
    });
    if (run.status !== 0) throw new Error(`adapter failed: ${run.stderr}`);
    world.served = fakeOrigin(path.join(dir, '.vercel', 'output'));
    return dir;
  };

  world.remoteTip = (branch) => {
    const out = childProcess.spawnSync('git', ['rev-parse', '--verify', '--quiet', `refs/heads/${branch}`], { cwd: remote, encoding: 'utf8' });
    return out.status === 0 ? out.stdout.trim() : null;
  };

  world.branchCommits = (branch) => {
    const tip = world.remoteTip(branch);
    return tip ? git(remote, 'rev-list', '--reverse', tip).split('\n') : [];
  };

  world.readDescriptor = (commit) => JSON.parse(git(remote, 'show', `${commit}:${LAYOUT.descriptor}`));

  world.publisher = (overrides = {}) => createPublisher({
    repoRoot: source,
    remote,
    config: loadSiteConfig(siteConfig({ ...configOverrides, publication })),
    buildPayload: world.buildPayload,
    fetchUrl: async (url) => {
      if (!world.served) throw new Error('ECONNREFUSED');
      return world.served.fetchUrl(url);
    },
    dispatch: async (consumer, payload) => {
      if (world.hooks.dispatch) await world.hooks.dispatch(consumer, payload);
      world.dispatched.push({ consumer: consumer.name, payload });
    },
    readMainHeadPublication: async () => world.mainHeadPublication || readPublicationAt(source, 'HEAD'),
    proofAttempts: 1,
    sleep: async () => {},
    gitEnv: GIT_ENV,
    hooks: world.hooks,
    ...overrides,
  });

  world.records = async () => (await world.publisher().readState()).records;
  world.payload = PAYLOAD;
  return world;
}

function readPublicationAt(source, revision) {
  return JSON.parse(git(source, 'show', `${revision}:publication/site.json`)).publication;
}

function payloadInventory(dir) {
  return inventoryOfDir(dir);
}

module.exports = { createWorld, payloadInventory };

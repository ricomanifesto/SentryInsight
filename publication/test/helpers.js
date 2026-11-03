// Shared fixtures for the publication tests: temporary directories, local Git
// repositories with a file-transport remote, and a fake production origin that
// serves an adapter output directory. Nothing here touches a network remote.
const childProcess = require('node:child_process');
const crypto = require('node:crypto');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');

const GIT_ENV = {
  ...process.env,
  GIT_CONFIG_GLOBAL: os.devNull,
  GIT_CONFIG_NOSYSTEM: '1',
  GIT_AUTHOR_NAME: 'Fixture',
  GIT_AUTHOR_EMAIL: 'fixture@example.invalid',
  GIT_COMMITTER_NAME: 'Fixture',
  GIT_COMMITTER_EMAIL: 'fixture@example.invalid',
};

function tempDir(t, prefix) {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), prefix));
  t.after(() => fs.rmSync(dir, { recursive: true, force: true }));
  return fs.realpathSync(dir);
}

function git(cwd, ...args) {
  return childProcess.execFileSync('git', args, { cwd, env: GIT_ENV, encoding: 'utf8' }).trim();
}

function writeFiles(root, files) {
  for (const [relativePath, contents] of Object.entries(files)) {
    const target = path.join(root, ...relativePath.split('/'));
    fs.mkdirSync(path.dirname(target), { recursive: true });
    fs.writeFileSync(target, contents);
  }
}

function sha256(value) {
  return crypto.createHash('sha256').update(value).digest('hex');
}

function siteConfig(overrides = {}) {
  return {
    schema_version: 1,
    site: 'SentryDigest',
    repository: 'ricomanifesto/SentryDigest',
    origins: {
      SentryDigest: {
        legacy: 'https://ricomanifesto.github.io/SentryDigest/',
        production: 'https://sentrydigest.ricomanifesto.com/',
        emitted: 'legacy',
      },
      SentryInsight: {
        legacy: 'https://ricomanifesto.github.io/SentryInsight/',
        production: 'https://sentryinsight.ricomanifesto.com/',
        emitted: 'legacy',
      },
      GRCInsight: {
        legacy: 'https://ricomanifesto.github.io/GRCInsight/',
        production: 'https://grcinsight.ricomanifesto.com/',
        emitted: 'legacy',
      },
    },
    publication: { mode: 'prepare', proof: 'on' },
    artifact_branch: 'vercel-production',
    state_branch: 'publication-state',
    payload_builder: ['node', 'scripts/build-static-artifact.js'],
    proof_samples: {
      machine_endpoint: 'feed.xml',
      sitemap: 'sitemap.xml',
      asset: 'assets/icon.svg',
      dated_archive: '^archive/\\d{4}-\\d{2}-\\d{2}/index\\.html$',
    },
    consumers: [
      { name: 'SentryInsight', repository: 'ricomanifesto/SentryInsight', event_type: 'sentrydigest-updated' },
      { name: 'GRCInsight', repository: 'ricomanifesto/GRCInsight', event_type: 'sentrydigest-updated' },
    ],
    ...overrides,
  };
}

const PAYLOAD = {
  'index.html': '<!doctype html><title>SentryDigest</title>\n',
  'feed.xml': '<?xml version="1.0"?><rss version="2.0"><channel></channel></rss>\n',
  'news-data.json': '[]\n',
  'sitemap.xml': '<?xml version="1.0"?><urlset></urlset>\n',
  'assets/icon.svg': '<svg xmlns="http://www.w3.org/2000/svg"></svg>\n',
  'archive/index.html': '<!doctype html><title>Archive</title>\n',
  'archive/2026-01-01/index.html': '<!doctype html><title>One</title>\n',
  'archive/2026-01-02/index.html': '<!doctype html><title>Two</title>\n',
  LICENSE: 'MIT License\n',
};

// Serves an adapter output directory the way the provider would: files from
// .vercel/output/static plus the configured directory routes. Paths missing
// from the output return 404.
function fakeOrigin(outputDir, { origin = 'https://sentrydigest.ricomanifesto.com/', overrides = {} } = {}) {
  const staticDir = path.join(outputDir, 'static');
  const config = JSON.parse(fs.readFileSync(path.join(outputDir, 'config.json'), 'utf8'));
  const requests = [];
  const respond = (status, body, headers = {}) => ({
    status,
    headers: new Map(Object.entries({ 'cache-control': 'public, max-age=0, must-revalidate', ...headers })),
    body: Buffer.from(body),
  });
  async function fetchUrl(url) {
    requests.push(url);
    if (overrides[url]) return overrides[url]();
    if (!url.startsWith(origin)) throw new Error(`unexpected host for ${url}`);
    let pathname = `/${url.slice(origin.length)}`;
    for (const route of config.routes) {
      if (!route.src) continue;
      if (new RegExp(route.src).test(pathname)) {
        if (route.status === 308) return respond(308, '', { location: route.headers.Location });
        if (route.dest) {
          pathname = route.dest;
          break;
        }
      }
    }
    const filePath = path.join(staticDir, ...pathname.slice(1).split('/'));
    if (!pathname.slice(1) || !fs.existsSync(filePath) || !fs.statSync(filePath).isFile()) return respond(404, 'Not found');
    const relative = pathname.slice(1);
    const contentType = config.overrides?.[relative]?.contentType || 'text/html; charset=utf-8';
    return respond(200, fs.readFileSync(filePath), { 'content-type': contentType });
  }
  return { fetchUrl, requests };
}

module.exports = { GIT_ENV, PAYLOAD, fakeOrigin, git, sha256, siteConfig, tempDir, writeFiles };

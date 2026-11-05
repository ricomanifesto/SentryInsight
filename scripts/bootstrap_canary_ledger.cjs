// Separate, explicitly approved first initialization. No model key or send grant.
'use strict';
const fs = require('node:fs');
const path = require('node:path');
const { createGit } = require('../publication/kit/git');
const { bootstrapStore } = require('../publication/kit/store');
const { sha256 } = require('../publication/kit/canonical');
const { ledgerIdentity } = require('./sentry_canary_owner.cjs');
const ROOT = path.resolve(__dirname, '..');
const BRANCH = 'publication-admission';
const refused = () => { throw new Error('Admission initialization refused'); };
const need = (value) => { if (!value) refused(); };

async function initialize({ git, manifestBytes, expectedCommit, expectedManifest, confirm = false, now }) {
  need(confirm === true && /^[a-f0-9]{40}$/.test(expectedCommit || '')
    && /^[a-f0-9]{64}$/.test(expectedManifest || '') && sha256(manifestBytes) === expectedManifest);
  const raw = JSON.parse(manifestBytes.toString('utf8'));
  need(raw.source_role === 'reviewed_canary_candidate' && /^[a-f0-9]{40}$/.test(raw.production_main || ''));
  const identity = ledgerIdentity(raw);
  need(git.run(['rev-parse', 'HEAD']) === expectedCommit && git.run(['status', '--porcelain']) === '');
  need(git.run(['remote', 'get-url', 'origin']) === 'https://github.com/ricomanifesto/SentryInsight.git');
  need(git.run(['ls-remote', 'origin', 'refs/heads/main']).split(/\s+/)[0] === raw.production_main);
  const result = await bootstrapStore({ git, remote: 'origin', branch: BRANCH, site: 'SentryInsight',
    scopeSha256: identity.scope_sha256, now });
  return { status: 'initialized', root_oid: result.rootOid, marker_sha256: result.markerSha256,
    initialization_id: identity.initialization_id };
}

async function main(args = process.argv.slice(2)) {
  let result;
  try {
    need(args.length === 5 && args[0] === '--expected-commit' && args[2] === '--expected-manifest'
      && args[4] === '--initialize-public-ledger');
    // Retain only fixed Git controls. No model/AWS key, HOME, proxy, debug or
    // arbitrary command configuration is forwarded to any child process.
    const env = { PATH: '/usr/bin:/bin:/opt/homebrew/bin', GIT_CONFIG_GLOBAL: '/dev/null',
      GIT_CONFIG_SYSTEM: '/dev/null', GIT_NO_LAZY_FETCH: '1', GIT_ALLOW_PROTOCOL: 'https',
      GIT_TERMINAL_PROMPT: '0', GIT_AUTHOR_NAME: 'SentryInsight admission',
      GIT_AUTHOR_EMAIL: 'actions@users.noreply.github.com', GIT_COMMITTER_NAME: 'SentryInsight admission',
      GIT_COMMITTER_EMAIL: 'actions@users.noreply.github.com' };
    result = await initialize({ git: createGit(ROOT, { env, timeoutMs: 30000 }),
      manifestBytes: fs.readFileSync(path.join(ROOT, 'config/full-feed-canary.json')),
      expectedCommit: args[1], expectedManifest: args[3], confirm: true });
  } catch (error) {
    result = { status: error?.message === 'Admission initialization unknown' ? 'initialization_unknown' : 'initialization_refused' };
    if (result.status === 'initialization_unknown' && /^[a-f0-9]{40}$/.test(error.proposedRootOid || '')
        && /^[a-f0-9]{64}$/.test(error.proposedMarkerSha256 || '')) {
      result.proposed_root_oid = error.proposedRootOid;
      result.proposed_marker_sha256 = error.proposedMarkerSha256;
    }
    process.exitCode = 1;
  }
  process.stdout.write(`${JSON.stringify(result)}\n`);
}
module.exports = { initialize, main };
if (require.main === module) {
  process.stdout.on('error', () => { process.exitCode = 1; });
  main().catch(() => { process.exitCode = 1; });
}

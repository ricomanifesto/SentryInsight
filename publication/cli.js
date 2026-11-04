#!/usr/bin/env node
// Command-line entry for the publication workflows.
//
//   publish  --source <commit>          build, release and prove one source
//   resume                              complete the current tip only
//   rollback --target <release_key> --reason <text>
//   resolve  --release <release_key> --attestation <text>
//   seed     --consumer <name>=<commit|none> ... --attestation <text>
//   authority                           publication mode at the remote main head
//   admit    --event-name <name> --event-path <file> --run-id <id> --run-attempt <n> [--readmit true]
//   invoked  --key <admission_key> --run-id <id> [--handle <id>]
//   complete --key <admission_key> --run-id <id> --outcome <outcome> [--binding <level>]
//
// Results are printed as JSON and, inside GitHub Actions, written as step
// outputs and to the step summary. Every network call is anonymous except the
// downstream dispatch, which uses the repository's existing dispatch secret.
'use strict';

const childProcess = require('node:child_process');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');

const { createAdmission, findAdmissionReport } = require('./kit/admission');
const { loadSiteConfig, readSiteConfig } = require('./kit/config');
const { contentIdentityFor, digestContentAt } = require('./kit/content');
const { createGit } = require('./kit/git');
const { createPublisher } = require('./kit/publisher');

const REPO_ROOT = path.resolve(__dirname, '..');
const REMOTE = 'origin';
const FETCH_TIMEOUT_MS = 30000;
// The canonical report each consumer commits with its admission trailers.
const REPORT_PATHS = { SentryInsight: 'index.md', GRCInsight: 'site/index.md' };

function parseArgs(argv) {
  const [command, ...rest] = argv;
  const options = { consumer: [] };
  for (let index = 0; index < rest.length; index += 2) {
    const name = rest[index];
    const value = rest[index + 1];
    if (!name?.startsWith('--') || value === undefined) throw new Error(`usage: cli.js <command> --option value ...; bad argument ${name}`);
    const key = name.slice(2).replace(/-/g, '_');
    if (key === 'consumer') options.consumer.push(value);
    else options[key] = value;
  }
  return { command, options };
}

async function fetchUrl(url) {
  const response = await fetch(url, { redirect: 'manual', signal: AbortSignal.timeout(FETCH_TIMEOUT_MS) });
  return { status: response.status, headers: response.headers, body: Buffer.from(await response.arrayBuffer()) };
}

function buildPayloadWith(config) {
  const scratchDirs = [];
  const build = async ({ sourceRevision }) => {
    const scratch = fs.mkdtempSync(path.join(os.tmpdir(), 'publication-payload-'));
    scratchDirs.push(scratch);
    const [program, ...args] = config.payload_builder;
    const result = childProcess.spawnSync(program, [
      ...args,
      '--source', REPO_ROOT,
      '--revision', sourceRevision,
      '--output', path.join(scratch, 'store'),
      '--receipts', path.join(scratch, 'receipts'),
    ], { cwd: REPO_ROOT, encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] });
    if (result.status !== 0) {
      throw new Error(`payload build failed: ${String(result.stderr || result.error || '').trim().split('\n').slice(-3).join(' | ')}`);
    }
    const pointer = JSON.parse(fs.readFileSync(path.join(scratch, 'store', 'current.json'), 'utf8'));
    const payloadDir = path.join(scratch, 'store', pointer.build, 'artifact');
    return { payloadDir, contentIdentity: contentIdentityFor({ site: config.site, payloadDir, repoRoot: REPO_ROOT }) };
  };
  build.cleanup = () => scratchDirs.forEach((dir) => fs.rmSync(dir, { recursive: true, force: true }));
  return build;
}

function mainHeadPublication(git) {
  git.run(['fetch', '--quiet', '--no-tags', REMOTE, '+refs/heads/main:refs/publication/remote/main']);
  const text = git.showFile('refs/publication/remote/main', 'publication/site.json', { encoding: 'utf8' });
  if (!text) return { mode: 'disabled', proof: 'off' };
  return loadSiteConfig(text).publication;
}

async function dispatchRelease(consumer, payload) {
  const token = process.env.REPO_ACCESS_TOKEN;
  if (!token) throw new Error('REPO_ACCESS_TOKEN is not available for the downstream dispatch');
  const response = await fetch(`https://api.github.com/repos/${consumer.repository}/dispatches`, {
    method: 'POST',
    headers: {
      Accept: 'application/vnd.github+json',
      Authorization: `Bearer ${token}`,
      'Content-Type': 'application/json',
      'X-GitHub-Api-Version': '2022-11-28',
    },
    body: JSON.stringify({ event_type: consumer.event_type, client_payload: payload }),
    signal: AbortSignal.timeout(FETCH_TIMEOUT_MS),
  });
  if (response.status !== 204) throw new Error(`dispatch to ${consumer.repository} returned ${response.status}`);
}

function writeOutputs(values) {
  const lines = Object.entries(values)
    .filter(([, value]) => value !== undefined && value !== null && typeof value !== 'object')
    .map(([key, value]) => `${key}=${String(value).replace(/\n/g, ' ')}`);
  if (process.env.GITHUB_OUTPUT) fs.appendFileSync(process.env.GITHUB_OUTPUT, `${lines.join('\n')}\n`);
  if (process.env.GITHUB_STEP_SUMMARY) {
    fs.appendFileSync(process.env.GITHUB_STEP_SUMMARY, `### Publication\n\n${lines.map((line) => `- \`${line}\``).join('\n')}\n`);
  }
  process.stdout.write(`${JSON.stringify(values)}\n`);
}

async function main() {
  const { command, options } = parseArgs(process.argv.slice(2));
  const config = readSiteConfig(REPO_ROOT);
  const git = createGit(REPO_ROOT);

  if (['admit', 'invoked', 'complete', 'request-reserve', 'request-finish'].includes(command)) {
    const admission = createAdmission({
      repoRoot: REPO_ROOT,
      remote: REMOTE,
      config,
      consumer: config.site,
      fetchUrl,
      // A recovered report is a main commit that changed the canonical report
      // and carries exactly this admission key and its feed binding.
      findRecoveredReport: async (key, admitted) => {
        git.run(['fetch', '--quiet', '--no-tags', REMOTE, '+refs/heads/main:refs/publication/remote/main']);
        return Boolean(findAdmissionReport({
          git,
          ref: 'refs/publication/remote/main',
          key,
          feedUrl: admitted.feed_url,
          reportPath: REPORT_PATHS[config.site],
        }));
      },
    });
    if (command === 'request-reserve' || command === 'request-finish') {
      if (git.run(['rev-parse', 'HEAD']).trim() !== options.revision) throw new Error('request source revision mismatch');
      const args = { admissionKey: options.key, runId: options.run_id, revision: options.revision,
        requestSha256: options.request_sha256, limit: Number(options.limit) };
      const result = command === 'request-reserve' ? await admission.reserveRequest(args)
        : await admission.finishRequest({ ...args, attempt: Number(options.attempt), token: options.token, disposition: options.disposition, retryAfterSeconds: Number(options.retry_after) });
      // The Python bridge consumes this bounded response. Do not copy opaque
      // reservation handles into Actions outputs or step summaries.
      process.stdout.write(`${JSON.stringify(result)}\n`);
      return;
    }
    if (command === 'admit') {
      const payload = JSON.parse(fs.readFileSync(options.event_path, 'utf8')).client_payload ?? null;
      const decision = await admission.admit({
        eventName: options.event_name,
        payload,
        runId: options.run_id,
        runAttempt: options.run_attempt,
        readmit: options.readmit === 'true',
      });
      writeOutputs(decision);
      process.exitCode = decision.exit_code;
      return;
    }
    let recorded = command;
    if (command === 'invoked') await admission.invoked({ admissionKey: options.key, runId: options.run_id, handle: options.handle });
    else recorded = await admission.complete({ admissionKey: options.key, runId: options.run_id, outcome: options.outcome, binding: options.binding });
    writeOutputs({ recorded, admission_key: options.key });
    return;
  }

  if (command === 'authority') {
    writeOutputs({ mode: mainHeadPublication(git).mode });
    return;
  }

  const buildPayload = buildPayloadWith(config);
  const publisher = createPublisher({
    repoRoot: REPO_ROOT,
    remote: REMOTE,
    config,
    buildPayload,
    fetchUrl,
    dispatch: dispatchRelease,
    readMainHeadPublication: async () => mainHeadPublication(git),
    contentIdentityAt: async (revision) => digestContentAt(git, REPO_ROOT, revision),
    log: (message) => process.stderr.write(`${message}\n`),
  });
  try {
    let result;
    if (command === 'publish') result = await publisher.publish({ sourceRevision: options.source });
    else if (command === 'resume') result = await publisher.resume();
    else if (command === 'rollback') result = await publisher.rollback({ targetReleaseKey: options.target, reason: options.reason });
    else if (command === 'resolve') result = await publisher.resolve({ releaseKey: options.release, attestation: options.attestation });
    else if (command === 'seed') {
      const consumers = Object.fromEntries(options.consumer.map((pair) => pair.split('=')));
      result = await publisher.seed({ consumers, attestation: options.attestation });
    } else throw new Error(`unknown command ${command}`);
    const tip = result.tip || {};
    writeOutputs({
      outcome: result.outcome ?? tip.outcome,
      release_key: result.release_key,
      release_ref: result.release_ref,
      reason: result.reason,
      tip_outcome: tip.outcome,
    });
    // A hold, a supersession or a pending verification is reported, not a
    // failure of the calling workflow; a rejected source is a failure.
    if (result.outcome === 'rejected') process.exitCode = 1;
  } finally {
    buildPayload.cleanup();
  }
}

main().catch((error) => {
  process.stderr.write(`publication failed: ${error.message}\n`);
  process.exitCode = 1;
});

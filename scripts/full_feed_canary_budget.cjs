// Disposable local-file CAS rehearsal only. No remote/activation/key interface.
'use strict';
const fs = require('node:fs');
const path = require('node:path');
const readline = require('node:readline');
const cp = require('node:child_process');
const { createAdmission } = require('../publication/kit/admission');
const { DailyPilot } = require('../publication/kit/daily-pilot');
const { readSiteConfig } = require('../publication/kit/config');
const deny = () => { throw new Error('Offline canary refused'); };
globalThis.fetch = deny;
for (const [name, fields] of [['net', ['connect','createConnection']], ['tls',['connect']], ['http',['request','get']], ['https',['request','get']], ['http2',['connect']], ['dgram',['createSocket']], ['dns',['lookup','resolve']], ['dns/promises',['lookup','resolve']]]) {
  const api = require(`node:${name}`); for (const field of fields) api[field] = deny;
}
require('node:net').Socket.prototype.connect = deny;
function need(value) { if (!value) deny(); }
function exact(v, fields) { need(v && Object.keys(v).sort().join(',') === [...fields].sort().join(',')); }
const envNames = ['PATH','GIT_CONFIG_GLOBAL','GIT_CONFIG_SYSTEM','GIT_ALLOW_PROTOCOL','GIT_TERMINAL_PROMPT','GIT_AUTHOR_NAME','GIT_AUTHOR_EMAIL','GIT_COMMITTER_NAME','GIT_COMMITTER_EMAIL'];
// Darwin may add this noncredential encoding setting even to env -i children.
delete process.env.__CF_USER_TEXT_ENCODING;
need(Object.keys(process.env).every((name)=>envNames.includes(name))
  && process.env.GIT_ALLOW_PROTOCOL==='file' && process.env.GIT_CONFIG_GLOBAL==='/dev/null'
  && process.env.GIT_CONFIG_SYSTEM==='/dev/null');
const directory = process.argv[2];
need(process.argv.length === 3 && path.isAbsolute(directory));
fs.mkdirSync(directory, { recursive: false, mode: 0o700 });
const worker = path.join(directory, 'worker'), remote = path.join(directory, 'remote.git');
fs.mkdirSync(worker, { mode: 0o700 });
function git(args, cwd = worker) {
  const result = cp.spawnSync('/usr/bin/git', args, { cwd, env: process.env, input: undefined, timeout: 15000, maxBuffer: 8192, stdio: ['ignore','pipe','pipe'] });
  need(result.status === 0); return result.stdout.toString().trim();
}
git(['init','--quiet','--bare',remote], directory);
git(['init','--quiet','--initial-branch=main']);
fs.writeFileSync(path.join(worker, 'fixture'), 'Disposable offline financial rehearsal\n', {mode:0o600});
git(['add','fixture']); git(['commit','--quiet','-m','Offline financial fixture']);
git(['remote','add','origin',remote]);
let admission, grant, physical, requestSha, finished = false;
async function act(value) {
  if (!admission) {
    exact(value, ['operation','revision','sourceSha256','requestSha256','now']); need(value.operation === 'begin');
    need(/^[a-f0-9]{40}$/.test(value.revision) && /^[a-f0-9]{64}$/.test(value.sourceSha256) && /^[a-f0-9]{64}$/.test(value.requestSha256));
    const time = new Date(value.now); need(time.toISOString() === value.now && value.now.slice(0,10) === '2026-11-05');
    const pilot = new DailyPilot({ month:'2026-11', activationStart:'2026-11-05T00:00:00.000Z', opening:{amountMicrousd:0,basisSha256:'0'.repeat(64)} });
    admission = createAdmission({ repoRoot: worker, remote:'origin', config:readSiteConfig(path.resolve(__dirname,'..')), consumer:'SentryInsight', fetchUrl:deny, now:()=>time, productionDailyPilot:pilot, productionSpendPolicy:pilot.policy(value.revision) });
    const owner = {admissionKey:'run:800',runId:'800',runAttempt:'1',revision:value.revision,sourceSha256:value.sourceSha256};
    need((await admission.admit({eventName:'workflow_dispatch',payload:null,runId:'800',runAttempt:'1'})).decision === 'admitted');
    await admission.invoked({admissionKey:owner.admissionKey,runId:owner.runId});
    grant = await admission.productionSpend.reserveOneShotGeneration(owner);
    requestSha = value.requestSha256;
    physical = await admission.productionSpend.beginSend(grant, {operation:'report',requestSha256:requestSha});
    const records = (await admission.readState()).records;
    const original = records.find((r)=>r.stage==='request_reserved');
    need(original && original.token === physical.token && original.limit === 1 && original.request_sha256 === requestSha);
    return {token:physical.token,attempt:1,limit:1,request_sha256:requestSha};
  }
  exact(value, ['operation','receipt']); need(value.operation === 'finish' && !finished); finished = true;
  await admission.productionSpend.finishSend(grant,physical,{outcome:value.receipt===null?'uncertain':'accepted',receipt:value.receipt});
  let blocked = false; try { await admission.productionSpend.beginSend(grant,{operation:'report',requestSha256:requestSha}); } catch (_) { blocked = true; }
  const rows = (await admission.readState()).records;
  return {original_token_shared:rows.filter((r)=>r.stage==='request_reserved').length===1 && rows.find((r)=>r.stage==='request_reserved').token===physical.token,
    second_token_blocked:blocked,physical_limit:1,whole_hold_microusd:rows.find((r)=>r.stage==='spend_reserved').amountMicrousd,
    financial_settled:false,financial_outcome:rows.find((r)=>r.stage==='spend_finished').outcome};
}
(async()=>{
  for await (const line of readline.createInterface({input:process.stdin,crlfDelay:Infinity})) {
    try { need(line.length<=8192); const result = await act(JSON.parse(line)); process.stdout.write(JSON.stringify({ok:result})+'\n'); }
    catch (_) { process.stdout.write('{"error":"refused"}\n'); process.exitCode=1; break; }
  }
})().catch(()=>{process.stdout.write('{"error":"refused"}\n');process.exitCode=1;});

// Closed, disabled-by-default canary owner requiring initialized admission state.
// No provider key is accepted by this process, its environment or protocol.
'use strict';
const fs = require('node:fs'), path = require('node:path'), cp = require('node:child_process');
const readline = require('node:readline'), crypto = require('node:crypto');
const { createAdmission } = require('../publication/kit/admission');
const { DailyPilot } = require('../publication/kit/daily-pilot');
const { OriginalCanaryReplacementDaily, validateReplacement } = require('./original_canary_daily.cjs');
const { readSiteConfig } = require('../publication/kit/config');
const { initializationIdentity } = require('../publication/kit/store');
const ROOT = path.resolve(__dirname, '..');
const fail = () => { throw new Error('Canary authority unavailable'); };
const need = (v) => { if (!v) fail(); };
const exact = (v, keys) => need(v && Object.keys(v).sort().join(',') === [...keys].sort().join(','));
function git(args) {
  const r=cp.spawnSync('/usr/bin/git',args,{cwd:ROOT,env:process.env,timeout:30000,maxBuffer:8192,stdio:['ignore','pipe','pipe']});
  need(r.status===0);return r.stdout.toString().trim();
}
function approved(raw, context, at = new Date()) {
  need(raw.enabled===true && raw.metadata_audience_approved===true && raw.billing_basis==='verified_openrouter_credit_only');
  need(raw.max_output_tokens===32000 && raw.whole_hold_microusd===7251456 && raw.physical_limit===1);
  need(raw.schema_version===1 && raw.source_role==='reviewed_canary_candidate');
  for(const name of ['source_pack_sha256','canonical_request_sha256','wire_sha256'])need(/^[a-f0-9]{64}$/.test(raw[name]||''));
  need(raw.execution_date==='2026-11-05' && at.toISOString().slice(0,10)===raw.execution_date);
  validateReplacement(raw.daily_replacement,{revision:context.GITHUB_SHA,sourceSha256:raw.source_pack_sha256,scopeSha256:raw.data_approval_sha256});
  need(/^[a-f0-9]{64}$/.test(raw.data_approval_sha256||'') && raw.pilot!==null);
  exact(raw.pilot,['month','activationStart','opening']);need(raw.pilot.month==='2026-11' && raw.pilot.opening!==null);
  need(['nonpublish','conditional_publish'].includes(raw.output_fate));
  need(context.GITHUB_ACTIONS==='true' && context.GITHUB_REPOSITORY==='ricomanifesto/SentryInsight'
    && context.GITHUB_ACTOR==='ricomanifesto' && context.GITHUB_EVENT_NAME==='workflow_dispatch'
    && context.GITHUB_REF==='refs/heads/canary/sentry-full-feed-20261105' && context.GITHUB_RUN_ATTEMPT==='1'
    && /^[0-9]{1,20}$/.test(context.GITHUB_RUN_ID||'') && /^[a-f0-9]{40}$/.test(context.GITHUB_SHA||'')
    && context.GITHUB_SHA===context.EXPECTED_COMMIT);
}
function ledgerIdentity(raw) {
  need(raw?.schema_version===1 && raw.metadata_audience_approved===true && raw.pilot && raw.pilot.opening);
  new DailyPilot(raw.pilot);
  return initializationIdentity('SentryInsight',raw.pilot.opening.basisSha256);
}
async function makeOwner(raw, context, dependencies) {
  approved(raw,context,dependencies.now || new Date());
  const { admission }=dependencies;
  let grant=null,physical=null,finished=false,settled=false,completed=false;
  const bound={admissionKey:`run:${context.GITHUB_RUN_ID}`,runId:context.GITHUB_RUN_ID,runAttempt:'1',revision:context.GITHUB_SHA,sourceSha256:raw.source_pack_sha256};
  const step = async (value)=>{
    if (!grant) {
      exact(value,['operation','manifestSha256','sourceSha256','requestSha256']);need(value.operation==='begin');
      need(value.manifestSha256===dependencies.manifestSha256 && value.sourceSha256===raw.source_pack_sha256 && value.requestSha256===raw.canonical_request_sha256);
      need((await admission.admit({eventName:'workflow_dispatch',payload:null,runId:bound.runId,runAttempt:'1'})).decision==='admitted');
      await admission.invoked({admissionKey:bound.admissionKey,runId:bound.runId});
      grant=await admission.productionSpend.reserveOneShotGeneration(bound);
      physical=await admission.productionSpend.beginSend(grant,{operation:'report',requestSha256:raw.canonical_request_sha256});
      return {token:physical.token,attempt:1,limit:1,request_sha256:raw.canonical_request_sha256};
    }
    if (!finished) {
      exact(value,['operation','receipt']);need(value.operation==='finish');finished=true;
      const result=await admission.productionSpend.finishSend(grant,physical,{outcome:value.receipt===null?'uncertain':'accepted',receipt:value.receipt});
      exact(result,['recorded','outcome']);need(result.recorded===true && ['accepted','uncertain'].includes(result.outcome));
      if(result.outcome!=='uncertain') {await admission.productionSpend.settleGeneration(grant,{outcome:'completed'});settled=true;}
      return {financial_settled:settled,financial_outcome:result.outcome};
    }
    exact(value,['operation','outcome']);need(value.operation==='complete' && settled && !completed);
    need(value.outcome==='not-published'||(value.outcome==='published'&&raw.output_fate==='conditional_publish'));completed=true;
    need(await admission.complete({admissionKey:bound.admissionKey,runId:bound.runId,outcome:value.outcome,binding:'none'})==='completed');
    return {recorded:true};
  };
  let blocked=false;
  return async(value)=>{need(!blocked);try{return await step(value);}catch(_){blocked=true;fail();}};
}
module.exports={makeOwner,approved,ledgerIdentity};
if(require.main===module) (async()=>{
  // Check disabled/static/context fences BEFORE Git/auth or admission access.
  const bytes=fs.readFileSync(path.join(ROOT,'config/full-feed-canary.json'));
  const raw=JSON.parse(bytes);approved(raw,process.env);
  delete process.env.__CF_USER_TEXT_ENCODING;
  const allowed=['PATH','GIT_ALLOW_PROTOCOL','GIT_CONFIG_GLOBAL','GIT_CONFIG_SYSTEM','GIT_TERMINAL_PROMPT','GIT_AUTHOR_NAME','GIT_AUTHOR_EMAIL','GIT_COMMITTER_NAME','GIT_COMMITTER_EMAIL','GITHUB_ACTIONS','GITHUB_REPOSITORY','GITHUB_ACTOR','GITHUB_EVENT_NAME','GITHUB_REF','GITHUB_SHA','GITHUB_RUN_ID','GITHUB_RUN_ATTEMPT','EXPECTED_COMMIT'];
  need(Object.keys(process.env).every((name)=>allowed.includes(name)));
  need(process.env.GIT_CONFIG_GLOBAL==='/dev/null' && process.env.GIT_CONFIG_SYSTEM==='/dev/null');
  need(process.env.GIT_ALLOW_PROTOCOL==='https');
  need(git(['rev-parse','HEAD'])===process.env.GITHUB_SHA && git(['status','--porcelain'])==='');
  need(git(['remote','get-url','origin'])==='https://github.com/ricomanifesto/SentryInsight.git');
  need(git(['ls-remote','origin','refs/heads/main']).split(/\s+/)[0]===raw.production_main);
  const daily=new OriginalCanaryReplacementDaily(raw.pilot,raw.daily_replacement,{revision:process.env.GITHUB_SHA,sourceSha256:raw.source_pack_sha256,scopeSha256:raw.data_approval_sha256});
  const admission=createAdmission({repoRoot:ROOT,remote:'origin',config:readSiteConfig(ROOT),consumer:'SentryInsight',fetchUrl:fail,
    requiredInitialization:ledgerIdentity(raw),
    productionDailyPilot:daily,productionSpendPolicy:daily.policy(process.env.GITHUB_SHA)});
  const act=await makeOwner(raw,process.env,{admission,manifestSha256:crypto.createHash('sha256').update(bytes).digest('hex')});
  let blocked=false;
  for await(const line of readline.createInterface({input:process.stdin,crlfDelay:Infinity})) {
    if(blocked) break;
    try{need(line.length<=8192);process.stdout.write(JSON.stringify({ok:await act(JSON.parse(line))})+'\n');}
    catch(_){blocked=true;process.stdout.write('{"error":"persistence_or_authority_unknown"}\n');process.exitCode=1;break;}
  }
})().catch(()=>{process.stdout.write('{"error":"authority_unavailable"}\n');process.exitCode=1;});

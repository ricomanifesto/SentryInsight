// Fixed NO-MODEL operator action. It cannot reserve, finish, settle or send.
'use strict';
const fs=require('node:fs'),path=require('node:path');
const {parseArgs}=require('node:util');
const {canonicalJson,sha256}=require('../publication/kit/canonical');
const {createGit}=require('../publication/kit/git');
const {createStore,initializationIdentity}=require('../publication/kit/store');
const TARGET='run:42022367409', ORIGINAL='42022367409';
const PRIOR='b1d9eedc0d54eacad63fb86e9d24e495a0bdee27';
const HISTORY='15fa3cbc17a03657683b78e7f3eac44d23fb606d5cdbd8d341a3de56139d8894';
const blocked=new WeakSet();
const need=v=>{if(!v)throw new Error('Original readmission refused');};
async function readmitOriginal(store,{historySha256,operatorRunId}){
  need(!blocked.has(store)&&/^[a-f0-9]{64}$/.test(historySha256||'')&&/^[0-9]{1,20}$/.test(operatorRunId||'')&&operatorRunId!==ORIGINAL);
  let produced=false, prior;
  try{
    const result=await store.append(records=>{
      need(Array.isArray(records)&&sha256(canonicalJson(records))===historySha256);
      const latest=new Map();
      for(const row of records)if(row.admission_key&&['admitted','invoked','completed','readmitted','abandoned'].includes(row.stage))latest.set(row.admission_key,row);
      const current=latest.get(TARGET),admitted=records.findLast(r=>r.stage==='admitted'&&r.admission_key===TARGET);
      need(current?.stage==='invoked'&&current.run_id===ORIGINAL&&admitted?.run_id===ORIGINAL&&admitted.run_attempt==='1');
      need([...latest].every(([key,row])=>key===TARGET||!['admitted','invoked'].includes(row.stage)));
      prior=canonicalJson(records);produced=true;
      return {append:[{stage:'readmitted',admission_key:TARGET,run_id:operatorRunId}],value:'original-readmitted'};
    });
    blocked.add(store);
    need(produced&&result?.value==='original-readmitted'&&Array.isArray(result.appended)&&result.appended.length===1);
    const row=result.appended[0];
    need(Object.keys(row).sort().join(',')==='admission_key,at,run_id,stage'&&row.stage==='readmitted'&&row.admission_key===TARGET&&row.run_id===operatorRunId);
    need(typeof row.at==='string'&&new Date(row.at).toISOString()===row.at);
    need(canonicalJson(result.records.slice(0,-1))===prior&&canonicalJson(result.records.at(-1))===canonicalJson(row));
    return {outcome:'readmitted',originalRun:ORIGINAL,priorHistorySha256:historySha256,recordsSha256:sha256(canonicalJson(result.records))};
  }catch(_){
    blocked.add(store);
    throw new Error(produced?'Original readmission unknown':'Original readmission refused');
  }
}

function noAdoptionGit(git,expectedTip=PRIOR){
  let acknowledged=null;
  return {...git,get acknowledgedCommit(){return acknowledged;},
    fetchBranch(remote,branch){need(remote==='origin'&&branch==='publication-admission');const tip=git.fetchBranch(remote,branch);need(tip===expectedTip);return tip;},
    pushBranch(remote,commit,branch,expected){
    need(remote==='origin'&&branch==='publication-admission'&&expected===expectedTip&&/^[a-f0-9]{40}$/.test(commit||''));
    const result=git.run(['push','--quiet','--porcelain',`--force-with-lease=refs/heads/${branch}:${expected}`,remote,`${commit}:refs/heads/${branch}`],{allowFailure:true});
    // No ls-remote adoption after failed acknowledgement and no CAS retry.
    if(result===null)throw new Error('Original readmission unknown');
    acknowledged=commit;
  }};
}

function approved(raw,context,at=new Date()){
  need(raw?.enabled===true&&raw.schema_version===1&&raw.execution_date==='2026-11-05'&&at.toISOString().slice(0,10)===raw.execution_date);
  need(raw.target_admission_key===TARGET&&raw.target_run_id===ORIGINAL&&raw.history_sha256===HISTORY&&raw.prior_tip===PRIOR);
  need(raw.original_source==='4a18f5d42022170694d5d6e2f411a4bfc4903e2c'&&raw.production_main==='5fc68212f1a9772ab56872ad20ad94ccc8322f3e');
  need(/^[a-f0-9]{64}$/.test(raw.approval_scope_sha256||''));
  need(context.GITHUB_ACTIONS==='true'&&context.GITHUB_REPOSITORY==='ricomanifesto/SentryInsight'&&context.GITHUB_ACTOR==='ricomanifesto'&&context.GITHUB_EVENT_NAME==='workflow_dispatch');
  need(context.GITHUB_REF==='refs/heads/canary/sentry-full-feed-20261105'&&context.GITHUB_RUN_ATTEMPT==='1'&&/^[a-f0-9]{40}$/.test(context.GITHUB_SHA||'')&&context.GITHUB_SHA===context.EXPECTED_COMMIT);
  need(/^[0-9]{1,20}$/.test(context.GITHUB_RUN_ID||'')&&context.GITHUB_RUN_ID!==ORIGINAL);
}

module.exports={readmitOriginal,noAdoptionGit,approved};
if(require.main===module)(async()=>{
  const options=parseArgs({options:{'expected-commit':{type:'string'},'expected-readmission':{type:'string'},'readmit-original':{type:'boolean'}}}).values;
  need(options['readmit-original']===true);
  const root=path.resolve(__dirname,'..'),bytes=fs.readFileSync(path.join(root,'config/original-canary-readmission.json')),raw=JSON.parse(bytes);
  need(sha256(bytes)===options['expected-readmission']);
  const context={...process.env,EXPECTED_COMMIT:options['expected-commit']};approved(raw,context);
  delete process.env.__CF_USER_TEXT_ENCODING;
  const allowed=['PATH','GIT_CONFIG_GLOBAL','GIT_CONFIG_SYSTEM','GIT_ALLOW_PROTOCOL','GIT_TERMINAL_PROMPT','GIT_AUTHOR_NAME','GIT_AUTHOR_EMAIL','GIT_COMMITTER_NAME','GIT_COMMITTER_EMAIL','GITHUB_ACTIONS','GITHUB_REPOSITORY','GITHUB_ACTOR','GITHUB_EVENT_NAME','GITHUB_REF','GITHUB_SHA','GITHUB_RUN_ID','GITHUB_RUN_ATTEMPT'];
  need(Object.keys(process.env).every(key=>allowed.includes(key))&&process.env.GIT_CONFIG_GLOBAL==='/dev/null'&&process.env.GIT_CONFIG_SYSTEM==='/dev/null'&&process.env.GIT_ALLOW_PROTOCOL==='https');
  const git=noAdoptionGit(createGit(root,{env:process.env,timeoutMs:30000}));
  need(git.run(['rev-parse','HEAD'])===context.GITHUB_SHA&&git.run(['status','--porcelain'])==='');
  need(git.run(['remote','get-url','origin'])==='https://github.com/ricomanifesto/SentryInsight.git');
  need(git.run(['ls-remote','origin','refs/heads/main']).split(/\s+/)[0]===raw.production_main);
  const store=createStore({git,remote:'origin',branch:'publication-admission',site:'SentryInsight',requiredInitialization:initializationIdentity('SentryInsight',raw.opening_scope_sha256)});
  const result=await readmitOriginal(store,{historySha256:raw.history_sha256,operatorRunId:context.GITHUB_RUN_ID});
  need(/^[a-f0-9]{40}$/.test(git.acknowledgedCommit||''));
  process.stdout.write(JSON.stringify({...result,priorTip:PRIOR,committedTip:git.acknowledgedCommit})+'\n');
})().catch(()=>{process.stdout.write('{"outcome":"readmission_held_or_unknown"}\n');process.exitCode=1;});

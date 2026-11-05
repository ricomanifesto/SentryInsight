'use strict';
const test=require('node:test'), assert=require('node:assert/strict');
const {canonicalJson,sha256}=require('../kit/canonical');
const {readmitOriginal,noAdoptionGit,approved}=require('../../scripts/readmit_original_canary.cjs');
const {CompareAndSetLost}=require('../kit/git');
const target='run:42022367409';
function fixture(){return [
  {stage:'admission_store_initialized',initialization_id:'a'.repeat(64)},
  {stage:'admitted',admission_key:target,run_id:'42022367409',run_attempt:'1'},
  {stage:'invoked',admission_key:target,run_id:'42022367409'},
  {stage:'pilot_daily',day:'2030-01-01',amountMicrousd:7251456},
  {stage:'spend_finished',outcome:'uncertain',receipt:null},
];}
function state(rows=fixture()){
  let calls=0;const saved=[];
  return {saved,get calls(){return calls;},rows,
    async append(decide){calls++;const decision=await decide(rows);const appended=decision.append.map(r=>({...r,at:'2030-01-02T00:00:00.000Z'}));saved.push(...appended);return {value:decision.value,appended,records:[...rows,...appended]};}};
}
function expected(rows){return sha256(canonicalJson(rows));}
test('one fixed readmitted row preserves every old record byte',async()=>{
  const store=state();const before=canonicalJson(store.rows);
  const result=await readmitOriginal(store,{historySha256:expected(store.rows),operatorRunId:'900'});
  assert.equal(result.outcome,'readmitted');assert.equal(store.calls,1);
  assert.equal(canonicalJson(store.rows),before);
  assert.deepEqual(store.saved,[{stage:'readmitted',admission_key:target,run_id:'900',at:'2030-01-02T00:00:00.000Z'}]);
});
for(const kind of ['owner','latest','other','history'])test(`CAS decision refuses changed ${kind}`,async()=>{
  const store=state();const hash=expected(store.rows);
  if(kind==='owner')store.rows[2].run_id='901';
  if(kind==='latest')store.rows.push({stage:'completed',admission_key:target,run_id:'42022367409'});
  if(kind==='other')store.rows.push({stage:'invoked',admission_key:'run:902',run_id:'902'});
  if(kind==='history')store.rows.push({stage:'skipped'});
  await assert.rejects(readmitOriginal(store,{historySha256:hash,operatorRunId:'900'}),/Original readmission refused/);
  assert.equal(store.saved.length,0);
});
test('every CAS callback checks complete original history',async()=>{
  const rows=fixture();let decisions=0;
  const store={async append(decide){await decide(rows);decisions++;rows.push({stage:'skipped'});await decide(rows);decisions++;throw new CompareAndSetLost('private sentinel');}};
  await assert.rejects(readmitOriginal(store,{historySha256:expected(rows),operatorRunId:'900'}),/Original readmission unknown/);
  assert.equal(decisions,1);
});
test('lost ACK never adopts or repeats a mutation',async()=>{
  const rows=fixture();let calls=0;
  const store={async append(decide){calls++;await decide(rows);throw new Error('private sentinel');}};
  await assert.rejects(readmitOriginal(store,{historySha256:expected(rows),operatorRunId:'900'}),e=>e.message==='Original readmission unknown');
  assert.equal(calls,1);
  await assert.rejects(readmitOriginal(store,{historySha256:expected(rows),operatorRunId:'900'}));
  assert.equal(calls,1);
});
test('failed push never invokes generic remote readback/adoption',()=>{
  const calls=[];
  const git=noAdoptionGit({run(args){calls.push(args);return null;}},'a'.repeat(40));
  assert.throws(()=>git.pushBranch('origin','b'.repeat(40),'publication-admission','a'.repeat(40)),/Original readmission unknown/);
  assert.equal(calls.length,1);assert.equal(calls[0][0],'push');
});
test('malformed ACK after decision is latched without another append',async()=>{
  const rows=fixture();let calls=0;
  const store={async append(decide){calls++;await decide(rows);return {value:undefined};}};
  await assert.rejects(readmitOriginal(store,{historySha256:expected(rows),operatorRunId:'900'}),/Original readmission unknown/);
  await assert.rejects(readmitOriginal(store,{historySha256:expected(rows),operatorRunId:'900'}));
  assert.equal(calls,1);
});
test('every fixed read refuses another tip before any commit',()=>{
  const git=noAdoptionGit({fetchBranch(){return 'b'.repeat(40);}},'a'.repeat(40));
  assert.throws(()=>git.fetchBranch('origin','publication-admission'),/Original readmission refused/);
});
test('disabled sidecar and exact target/context gates are independent',()=>{
  const raw=JSON.parse(require('node:fs').readFileSync(require('node:path').join(__dirname,'../../config/original-canary-readmission.json')));
  const context={GITHUB_ACTIONS:'true',GITHUB_REPOSITORY:'ricomanifesto/SentryInsight',GITHUB_ACTOR:'ricomanifesto',GITHUB_EVENT_NAME:'workflow_dispatch',GITHUB_REF:'refs/heads/canary/sentry-full-feed-20261105',GITHUB_RUN_ATTEMPT:'1',GITHUB_SHA:'a'.repeat(40),EXPECTED_COMMIT:'a'.repeat(40),GITHUB_RUN_ID:'900'};
  const now=new Date('2026-11-06T00:00:00Z');
  assert.throws(()=>approved({...raw,enabled:false,approval_scope_sha256:null},context,now));
  const positive={...raw,enabled:true,approval_scope_sha256:'f'.repeat(64)};
  approved(positive,context,now);
  for(const [key,value]of [['target_run_id','901'],['history_sha256','b'.repeat(64)],['prior_tip','c'.repeat(40)],['execution_date','2026-11-05']])assert.throws(()=>approved({...positive,[key]:value},context,now));
  for(const [key,value]of [['GITHUB_ACTOR','other'],['GITHUB_RUN_ID','42022367409'],['GITHUB_REF','refs/heads/main'],['GITHUB_RUN_ATTEMPT','2']])assert.throws(()=>approved(positive,{...context,[key]:value},now));
});

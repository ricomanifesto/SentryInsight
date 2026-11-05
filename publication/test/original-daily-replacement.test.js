'use strict';
const test=require('node:test'),assert=require('node:assert/strict');
const {canonicalJson,sha256}=require('../kit/canonical');
const {DailyPilot}=require('../kit/daily-pilot');
const {ProductionSpendBudget}=require('../kit/production-spend');
const {OriginalCanaryReplacementDaily}=require('../../scripts/original_canary_daily.cjs');
const raw=require('../../config/full-feed-canary.json');
const original=require('./fixtures/original-canary-ledger.json').records;
const copy=v=>JSON.parse(JSON.stringify(v)),revision='a'.repeat(40),at=new Date('2026-11-05T18:00:00.000Z');
const binding=(run='900')=>({admissionKey:`run:${run}`,runId:run,runAttempt:'1',revision,sourceSha256:raw.source_pack_sha256});
function gate(){return new OriginalCanaryReplacementDaily(raw.pilot,raw.daily_replacement,{revision,sourceSha256:raw.source_pack_sha256,scopeSha256:raw.data_approval_sha256});}
function suffix(run='900'){return [
 {stage:'readmitted',admission_key:'run:42022367409',run_id:'899',at:at.toISOString()},
 {stage:'admitted',admission_key:`run:${run}`,run_id:run,run_attempt:'1',event:'workflow_dispatch',binding:'none',at:at.toISOString()},
 {stage:'invoked',admission_key:`run:${run}`,run_id:run,at:at.toISOString()},
];}
function world(){
 let rows=[...copy(original),...suffix()],writes=0;
 const store={async append(decide){const d=await decide(copy(rows));const appended=d.append.map(r=>({...r,at:at.toISOString()}));rows.push(...appended);writes++;return {value:d.value,records:copy(rows),appended};}};
 const make=()=>new ProductionSpendBudget({store,requireOwner:()=>11,policy:gate().policy(revision),dailyGate:gate(),now:()=>at});
 return {store,make,get rows(){return rows;},get writes(){return writes;},set rows(value){rows=value;}};
}
test('ordinary daily policy refuses original consumed day; only fixed closed gate permits one replacement',async()=>{
 const w=world(),baseline=new DailyPilot(raw.pilot);
 assert.throws(()=>baseline.prepare({records:w.rows,bound:binding(),policy:baseline.policy(revision).value,generationToken:'1'.repeat(32),now:at}));
 const before=canonicalJson(original),budget=w.make(),generation=await budget.reserveOneShotGeneration(binding());
 assert.equal(w.rows.filter(r=>r.stage==='pilot_daily').length,2);
 assert.equal(w.rows.filter(r=>r.stage==='pilot_daily').at(-1).day,'2026-11-05');
 assert.equal(w.rows.filter(r=>r.stage==='spend_reserved').reduce((n,r)=>n+r.amountMicrousd,0),14502912);
 assert.equal(canonicalJson(w.rows.slice(0,10)),before);
 const permit=await budget.beginSend(generation,{operation:'report',requestSha256:raw.canonical_request_sha256});
 assert.notEqual(permit.token,original.find(r=>r.stage==='request_reserved').token);
 assert.equal(w.rows.filter(r=>r.stage==='request_reserved').at(-1).limit,1);
 await assert.rejects(budget.beginSend(generation,{operation:'report',requestSha256:raw.canonical_request_sha256}));
 await assert.rejects(w.make().reserveOneShotGeneration(binding('901')));
 assert.equal(w.rows.filter(r=>r.stage==='spend_reserved').length,2);
});
for(let index=0;index<10;index++)test(`every original prefix record is immutable at reservation: ${index}`,async()=>{
 const w=world();w.rows[index].at='2026-11-05T17:59:59.000Z';
 await assert.rejects(w.make().reserveOneShotGeneration(binding()));assert.equal(w.writes,0);
});
for(const kind of ['extra','otherday','duplicate','readmitowner','newowner','newattempt','revision','source','scope','fate'])test(`closed recovery refuses ${kind}`,async()=>{
 const w=world();let bound=binding();
 if(kind==='extra')w.rows.push({stage:'skipped'});
 if(kind==='otherday')w.rows.push({...copy(original.find(r=>r.stage==='pilot_daily')),day:'2026-11-04'});
 if(kind==='duplicate')w.rows.push(copy(original.find(r=>r.stage==='pilot_daily')));
 if(kind==='readmitowner')w.rows[10].run_id='42022367409';
 if(kind==='newowner')w.rows[12].run_id='901';
 if(kind==='newattempt')w.rows[11].run_attempt='2';
 if(kind==='revision')bound={...bound,revision:'b'.repeat(40)};
 if(kind==='source')bound={...bound,sourceSha256:'b'.repeat(64)};
 if(kind==='scope')assert.throws(()=>new OriginalCanaryReplacementDaily(raw.pilot,raw.daily_replacement,{revision,sourceSha256:raw.source_pack_sha256,scopeSha256:'b'.repeat(64)}));
 if(kind==='fate')w.rows[11].binding='feed-bytes';
 if(kind!=='scope')await assert.rejects(w.make().reserveOneShotGeneration(bound));
 assert.equal(w.writes,0);
});
test('reservation CAS loss revalidates all original records rather than trusting preflight',async()=>{
 const w=world();let calls=0;
 w.store.append=async decide=>{calls++;await decide(copy(w.rows));w.rows[5].amountMicrousd=1;return decide(copy(w.rows));};
 await assert.rejects(w.make().reserveOneShotGeneration(binding()));assert.equal(calls,1);assert.equal(w.writes,0);
});
test('lost committed ACK retains both holds and consumed replacement; same instance cannot retry',async()=>{
 const w=world(),append=w.store.append;let count=0;
 w.store.append=async decide=>{count++;await append(decide);throw Error('private sentinel');};
 const b=w.make();await assert.rejects(b.reserveOneShotGeneration(binding()),e=>e.code==='persistence_unknown');
 await assert.rejects(b.reserveOneShotGeneration(binding()));assert.equal(count,1);
 w.store.append=append;await assert.rejects(w.make().reserveOneShotGeneration(binding('901')));
 assert.equal(w.rows.filter(r=>r.stage==='spend_reserved').reduce((n,r)=>n+r.amountMicrousd,0),14502912);
 assert.equal(canonicalJson(w.rows.slice(0,10)),canonicalJson(original));
});
test('simultaneous fresh reservations consume at most one replacement allowance',async()=>{
 const w=world();let tail=Promise.resolve();const append=w.store.append;
 w.store.append=decide=>{const result=tail.then(()=>append(decide));tail=result.catch(()=>{});return result;};
 const result=await Promise.allSettled([w.make().reserveOneShotGeneration(binding()),w.make().reserveOneShotGeneration(binding())]);
 assert.equal(result.filter(r=>r.status==='fulfilled').length,1);
 assert.equal(w.rows.filter(r=>r.stage==='pilot_daily').length,2);
 assert.equal(w.rows.filter(r=>r.stage==='spend_reserved').length,2);
});
test('ordinary later-day reader accepts same-schema history; no unknown pilot stage is added',async()=>{
 const w=world();await w.make().reserveOneShotGeneration(binding());
 assert.ok(w.rows.filter(r=>r.stage.startsWith('pilot_')).every(r=>['pilot_opening','pilot_daily'].includes(r.stage)));
 const next=new DailyPilot(raw.pilot);assert.doesNotThrow(()=>next.prepare({records:w.rows,bound:binding('901'),policy:next.policy(revision).value,generationToken:'c'.repeat(32),now:new Date('2026-11-06T00:00:00.000Z')}));
 assert.equal(sha256(canonicalJson(original)),raw.daily_replacement.prior_history_sha256);
});
test('full original financial records reach real accounting; third full hold cannot fit the unchanged cap',async()=>{
 const w=world(),daily=gate(),prepare=daily.prepare.bind(daily);let observed=false;
 daily.prepare=arguments_=>{const before=canonicalJson(arguments_.records);assert.equal(arguments_.records.length,13);
  assert.equal(sha256(canonicalJson(arguments_.records.slice(0,10))),raw.daily_replacement.prior_history_sha256);
  const result=prepare(arguments_);assert.equal(canonicalJson(arguments_.records),before);observed=true;return result;};
 const b=new ProductionSpendBudget({store:w.store,requireOwner:()=>11,policy:daily.policy(revision),dailyGate:daily,now:()=>at});
 await b.reserveOneShotGeneration(binding());assert.ok(observed);
 const next=new DailyPilot(raw.pilot),later=new ProductionSpendBudget({store:w.store,requireOwner:()=>11,policy:next.policy(revision),dailyGate:next,now:()=>new Date('2026-11-06T00:00:00.000Z')});
 await assert.rejects(later.reserveOneShotGeneration(binding('901')));
 assert.equal(w.rows.filter(r=>r.stage==='spend_reserved').length,2);
});
for(const field of Object.keys(raw.daily_replacement))test(`replacement identity refuses corrupt ${field}`,()=>{
 const changed=copy(raw.daily_replacement);changed[field]=typeof changed[field]==='number'?changed[field]+1:'unrelated';
 assert.throws(()=>new OriginalCanaryReplacementDaily(raw.pilot,changed,{revision,sourceSha256:raw.source_pack_sha256,scopeSha256:raw.data_approval_sha256}));
});

// Closed one-time replacement, not an ordinary daily-policy override.
'use strict';
const {DailyPilot}=require('../publication/kit/daily-pilot');
const {canonicalJson,sha256}=require('../publication/kit/canonical');
const SCOPE='840fe520c883c8cb92929b7285f90feed8b008512386a05a4265fa456374cba5';
const SOURCE='b74eb002a01d5676653ea06f4336e968f2fb012f3e78555b33ebaa5ce6808ce9';
const ORIGINAL='42022367409',DAY='2026-11-05';
const EXPECTED=Object.freeze({version:1,kind:'replace_original_nov5_canary',original_run_id:ORIGINAL,original_day:DAY,
 original_source:'4a18f5d42022170694d5d6e2f411a4bfc4903e2c',
 prior_history_sha256:'15fa3cbc17a03657683b78e7f3eac44d23fb606d5cdbd8d341a3de56139d8894',prior_record_count:10,
 original_daily_sha256:'fbb879840a9715dce333b342fed0d680c491a24b556ff6794058feae202a2be7',
 supersedes_manifest_sha256:'f6e48b09f930f5871dadae0c2755b22412878b008d84908dd8f240c765f8a70b'});
const need=v=>{if(!v)throw Error('Fixed original-day replacement refused');};
const exact=(v,keys)=>need(v&&Object.keys(v).sort().join(',')===[...keys].sort().join(','));
function validateReplacement(value,{revision,sourceSha256,scopeSha256}){
 exact(value,Object.keys(EXPECTED));
 need(canonicalJson(value)===canonicalJson(EXPECTED));
 need(typeof revision==='string'&&/^[a-f0-9]{40}$/.test(revision)&&revision!==EXPECTED.original_source);
 need(sourceSha256===SOURCE&&scopeSha256===SCOPE);
}
function instant(value){
 need(typeof value==='string'&&Number.isFinite(Date.parse(value))&&new Date(value).toISOString()===value&&value.slice(0,10)===DAY);
 return Date.parse(value);
}
class OriginalCanaryReplacementDaily {
 #base;#binding;
 constructor(pilot,replacement,binding){
  validateReplacement(replacement,binding);this.#base=new DailyPilot(pilot);this.#binding={...binding};
 }
 policy(revision){need(revision===this.#binding.revision);return this.#base.policy(revision);}
 prepare({records,bound,policy,generationToken,now}){
  need(Array.isArray(records)&&records.length===13&&now instanceof Date&&Number.isFinite(now.getTime())&&now.toISOString().slice(0,10)===DAY);
  need(bound.revision===this.#binding.revision&&bound.sourceSha256===SOURCE&&bound.runAttempt==='1');
  need(typeof bound.runId==='string'&&/^[0-9]{1,20}$/.test(bound.runId)&&bound.runId!==ORIGINAL&&bound.admissionKey===`run:${bound.runId}`);
  const prefix=records.slice(0,10);
  need(sha256(canonicalJson(prefix))===EXPECTED.prior_history_sha256);
  const prior=prefix.filter(r=>r.stage==='pilot_daily');
  need(prior.length===1&&sha256(canonicalJson(prior[0]))===EXPECTED.original_daily_sha256);
  const [readmitted,admitted,invoked]=records.slice(10);
  exact(readmitted,['stage','admission_key','run_id','at']);
  need(readmitted.stage==='readmitted'&&readmitted.admission_key===`run:${ORIGINAL}`
   &&typeof readmitted.run_id==='string'&&/^[0-9]{1,20}$/.test(readmitted.run_id)
   &&readmitted.run_id!==ORIGINAL&&readmitted.run_id!==bound.runId);
  exact(admitted,['stage','admission_key','run_id','run_attempt','event','binding','at']);
  need(admitted.stage==='admitted'&&admitted.admission_key===bound.admissionKey&&admitted.run_id===bound.runId
   &&admitted.run_attempt==='1'&&admitted.event==='workflow_dispatch'&&admitted.binding==='none');
  exact(invoked,['stage','admission_key','run_id','at']);
  need(invoked.stage==='invoked'&&invoked.admission_key===bound.admissionKey&&invoked.run_id===bound.runId);
  need(instant(readmitted.at)<=instant(admitted.at)&&instant(admitted.at)<=instant(invoked.at)&&instant(invoked.at)<=now.getTime());
  // This exact historical daily row is exempted ONLY from the delegated
  // daily-collision check. No persisted row is removed/changed. The original
  // unfiltered records still reach ProductionSpendBudget's financial replay.
  const dailyView=records.filter(r=>r!==prior[0]);
  return this.#base.prepare({records:dailyView,bound,policy,generationToken,now});
 }
}
module.exports={OriginalCanaryReplacementDaily,validateReplacement};

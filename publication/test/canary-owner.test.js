const assert=require('node:assert/strict'),test=require('node:test');
const {makeOwner,approved,ledgerIdentity}=require('../../scripts/sentry_canary_owner.cjs');
const source=require('../../config/full-feed-canary.json');
function fixture({uncertain=false,lost=false}={}) {
  const events=[];
  const raw={...source,enabled:true,metadata_audience_approved:true,billing_basis:'verified_openrouter_credit_only',data_approval_sha256:'e'.repeat(64),
    pilot:{month:'2026-11',activationStart:'2026-11-05T00:00:00.000Z',opening:{amountMicrousd:0,basisSha256:'f'.repeat(64)}}};
  const context={GITHUB_ACTIONS:'true',GITHUB_REPOSITORY:'ricomanifesto/SentryInsight',GITHUB_ACTOR:'ricomanifesto',GITHUB_EVENT_NAME:'workflow_dispatch',GITHUB_REF:'refs/heads/canary/sentry-full-feed-20261105',GITHUB_RUN_ATTEMPT:'1',GITHUB_RUN_ID:'800',GITHUB_SHA:'a'.repeat(40),EXPECTED_COMMIT:'a'.repeat(40)};
  const now=new Date('2026-11-05T03:04:05.000Z');
  const admission={
    async admit(){events.push('admit');return {decision:'admitted'};},
    async invoked(){events.push('invoked');},
    productionSpend:{
      async reserveOneShotGeneration(binding){events.push('reserve');assert.equal(binding.sourceSha256,source.source_pack_sha256);if(lost)throw Error('hostile-private-sentinel');return {generationToken:'1'.repeat(32)};},
      async beginSend(g,value){events.push('begin');assert.equal(value.requestSha256,source.canonical_request_sha256);return {generationToken:g.generationToken,token:'2'.repeat(32)};},
      async finishSend(){events.push('finish');return {recorded:true,outcome:uncertain?'uncertain':'accepted'};},
      async settleGeneration(){events.push('settle');return {recorded:true};},
    },
    async complete(){events.push('complete');return 'completed';},
  };
  return {raw,context,events,now,admission};
}
const begin={operation:'begin',manifestSha256:'d'.repeat(64),sourceSha256:source.source_pack_sha256,requestSha256:source.canonical_request_sha256};
async function owner(w){return makeOwner(w.raw,w.context,{admission:w.admission,manifestSha256:'d'.repeat(64),now:w.now});}
test('disabled/expired authority never touches admission',async()=>{
  const w=fixture();await assert.rejects(makeOwner({...w.raw,enabled:false},w.context,{admission:w.admission,now:w.now}));
  assert.throws(()=>approved(w.raw,w.context,new Date('2026-11-06T00:00:00.000Z')));assert.deepEqual(w.events,[]);
});
test('paid ledger identity pins stable approved opening scope rather than run or revision',()=>{
  const w=fixture(),identity=ledgerIdentity(w.raw);
  assert.equal(identity.scope_sha256,w.raw.pilot.opening.basisSha256);
  assert.deepEqual(ledgerIdentity({...w.raw,production_main:'b'.repeat(40)}),identity);
  for(const raw of [source,{...w.raw,metadata_audience_approved:false},{...w.raw,pilot:null},
    {...w.raw,pilot:{...w.raw.pilot,opening:null}}])assert.throws(()=>ledgerIdentity(raw));
});
test('producer returns the trusted spending token and settles before completion',async()=>{
  const w=fixture(),act=await owner(w);const permit=await act(begin);assert.equal(permit.token,'2'.repeat(32));assert.equal(permit.limit,1);
  assert.equal((await act({operation:'finish',receipt:{synthetic:true}})).financial_settled,true);
  await act({operation:'complete',outcome:'not-published'});
  assert.deepEqual(w.events,['admit','invoked','reserve','begin','finish','settle','complete']);
  await assert.rejects(act(begin));assert.equal(w.events.filter(x=>x==='begin').length,1);
});
test('unknown spend remains held and cannot complete or rearm',async()=>{
  const w=fixture({uncertain:true}),act=await owner(w);await act(begin);
  assert.equal((await act({operation:'finish',receipt:null})).financial_settled,false);
  await assert.rejects(act({operation:'complete',outcome:'not-published'}));await assert.rejects(act(begin));
  assert.equal(w.events.includes('settle'),false);assert.equal(w.events.includes('complete'),false);
});
test('lost reserve acknowledgement latches before another issuer operation',async()=>{
  const w=fixture({lost:true}),act=await owner(w);await assert.rejects(act(begin));const before=[...w.events];
  await assert.rejects(act(begin));assert.deepEqual(w.events,before);assert.equal(w.events.includes('begin'),false);
});
test('body/source rebind refuses before admission and latches',async()=>{
  const w=fixture(),act=await owner(w);await assert.rejects(act({...begin,requestSha256:'0'.repeat(64)}));
  await assert.rejects(act(begin));assert.deepEqual(w.events,[]);
});

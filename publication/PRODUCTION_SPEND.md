# Disabled production spending primitive

`kit/production-spend.js` adds internal `ProductionSpendPolicy` and
`ProductionSpendBudget` types at the existing append-only CAS/admission ownership
seam. There is no policy configured by default, CLI command, HTTP parameter,
workflow input, transport integration or LIVE option. This is offline preparation,
not runtime-enforced production spending. Selected paid model profiles remain
OFFLINE/mock-only and existing free defaults and publication behavior are unchanged.

Only a future trusted job adapter may construct a policy. Public request bodies,
model replies, reruns and environment/workflow input must not choose it or assert
an authenticated principal. The ledger does not authenticate callers. The
constructor binds the existing invoked admission owner; source-pack manifest
SHA256, source/code revision, run/first-attempt identity, model/provider and
request SHA256 are explicit. Feed admission alone does not bind enriched article
bytes: the future adapter must validate the actual complete source pack.

Policy version1 has explicit UTC period start/end/expiry and positive safe-integer
microUSD generation/period ceilings, the fixed model/provider and closed operation
output/attempt bounds. No active production dollar amount or cadence is supplied.
Absence/disablement/expiry refuse new work. A generation atomically reserves all
operation and physical-attempt allowances in one CAS snapshot. Every send needs
its own durable, uniquely bound token before transport. Suballocations are inside
the whole-generation hold and are not charged again. CAS decisions are pure;
nonces are stable outside the retryable decision. Store CAS retries are not
inference retries. One report operation uses the SAME existing request reservation token and three-attempt replay decisions. The dollar layer does not issue a separate attempt controller. The existing request CLI and client paths keep their original semantics.

## Financial assumptions

Reservations use the full1,048,576 model-context input ceiling, at2microUSD/input
token, plus each approved combined output cap at10microUSD/token, zero request
charge. The maximum model context is a provider-contract assumption, not an
external billing guarantee. It deliberately differs from cl100k/UTF8/context
quality estimates; those estimates do not attest billable tokens or justify a
smaller financial reserve. Complete messages, schema/framing and hidden reasoning
remain included in the future adapter's request/output checks. Reasoning tokens
are a subset of completion tokens and are never charged twice.

For perspective only, full-context Sentry32k output ×3attempts reserves7.251456USD;
GRC8k output ×2operations reserves4.354304USD (16k output ×2=4.514304USD).
These are conservative assumption-based examples, not selected active caps.
Each repository/store enforces its own quota; there is no combined portfolio cap.

`usdToMicrousd` accepts decimal text and rounds UP exactly using integer decimal
arithmetic; it never rounds through a binary float. All JSON monetary values,
products, sums and token counts must remain safe integers. A trusted adapter must
preserve the original decimal semantics when converting a provider receipt.

## Outcomes and one-time settlement

Each receipt has exact fixed fields: resolved model, serving provider/default-tier
metadata (nullable means unavailable), prompt/completion/reasoning/total token
counts, integer cost and a closed `costCoverage` marker. Wrong explicit provider
or tier, incoherent totals, unsupported rates, invalid/bool/float values or an
over-limit charge refuse. Missing accounting is unknown, never zero. Null serving
provider/tier alone is unavailable attestation, not a quality failure or fabricated
endpoint/default proof; complete coherent accounting can still be financially known.

`costCoverage: complete` is ONLY a trusted future adapter assertion that the
validated amount covers the approved application liability. It cannot be copied
from a model reply or inferred from OpenRouter usage.cost alone. BYOK may prioritize
an upstream key and incur separate provider charges/platform fees; no account
lookup, key inspection, billing change or invented disable-BYOK request parameter
is implemented here. Without established full billing basis, mark coverage unknown:
known reported numbers are retained as partial metadata, the entire hold remains,
and continuation/settlement refuse. Synthetic tests' complete-coverage values are
fictional, not evidence about any account.

Only a fully known terminal generation can append one settlement. Actual spend is
derived from its immutable physical receipts, never a caller refund amount. The
CAS record atomically retires unused operation/attempt slots and replaces the hold
with that validated sum exactly once. Duplicate/mismatched settlement or completion
refuses, and settled slots never reopen. A known terminal refusal may retire
unsent later operations; an unknown charge or in-flight send cannot. Earlier retry
or refusal outcomes remain immutable records even if a later response succeeds.

Record outcomes and SETTLE BEFORE admission.complete while the original invoked
owner still holds the claim. Expiry prevents new sends, not recording known
outcomes/settlement. A lost, malformed or ambiguous store acknowledgement latches
that budget instance; it never automatically repeats a write or sends again. A new
instance cannot adopt an old generation handle or re-reserve its admission key.
Restart/readmission/policy ID changes cannot create a fresh financial namespace.
A later adapter must keep admission unresolved on uncertain persistence and
reconcile durable state before any separate operator readmission; this primitive
adds no automatic resume/reconciliation authority.

Pending/sending/uncertain allocations count fully. Unsettled old periods block
rollover, and overlapping/different policy buckets cannot erase holds. Known
settled old periods can roll over only into another explicit UTC policy. This
conservative availability tradeoff can freeze paid work indefinitely after an
unresolved request; later trusted reconciliation is required, not a reset or
report-recovery-as-billing-proof shortcut.

## Remaining runtime boundary

The append-only Git state is PUBLIC operational metadata. Policy caps and validated
usage/cost visibility need owner approval before real use; raw source text, prompts,
answers, reasoning, credentials, private account state and exception text are
excluded. Error messages are fixed. Tests use synthetic data/local file remotes
and deny all network access; no provider, account, credential or cloud action occurs.

A future paid path could reuse a trusted GitHub admission/job context while the
public GRC API stays free-only. Go/async Lambda execution would need a separately
authenticated durable grant/ledger integration. Neither runtime is silently chosen
here; no new database, permission, service or dependency is introduced. Transport
activation, approved real sources/retention, exact runtime admission, billing basis,
period amounts, aggregate portfolio policy and uncertain-write reconciliation
remain separate decisions. Do not describe this module as a live spending guard.

Focused offline checks: `node --test --test-concurrency=1
publication/test/production-spend.test.js publication/test/admission.test.js`.
Use a secret-free environment and deny external networking; no install is needed.

Different generations may bind newer trusted code revisions in the same period.
Only revision is omitted from the historical period financial-terms comparison;
every other policy term stays exact, and all earlier costs/holds are still summed.
The original generation policy/handle/revision remains fully immutable and cannot
be rebound. A store acknowledgement requires a produced, concrete nonundefined
decision and exactly matching returned value shape; an empty or no-decision
acknowledgement is persistence-unknown and latches that owner.
A refusal after a prior decision was produced may follow a committed write or
CAS readback ambiguity; it also latches as persistence-unknown. Only a refusal
before any produced decision is treated as a known pre-mutation refusal.

## Disabled UTC daily pilot

`DailyPilot` prepares the approved 20,000,000 microUSD per UTC-calendar-month
Sentry allocation and the existing 7,251,456 whole-generation hold (32k combined
output, three shared physical attempts). No actual activation date or month is
configured. Missing activation or opening information returns a disabled policy.
The internal constructor has no CLI/workflow input or paid transport path.

The daily claim and opening charge append atomically with the existing generation
reservation. The claimed UTC day never resets after cancellation, failure,
readmission, a new code revision or a known-cost settlement. Source preflight
precedes issuance; a refusal before the atomic reservation creates no day claim.
Cancellation after reservation leaves its day consumed and its money held until a
separately validated terminal outcome/reconciliation. Producer serialization and
workflow cancellation alone are not the durable daily gate. Unresolved generation
holds continue to block month rollover in the same money ledger.

`opening.amountMicrousd` means verified already-incurred spend in that configured
month, after every pre-ledger liability IN THE APPROVED PILOT SCOPE is reconciled.
It cannot represent an unresolved or conservatively estimated hold. Unknown
in-scope obligations, including older-month ones, require `opening: null` and
remain disabled across a calendar boundary. The basis SHA is a trusted owner's
assertion of the approved scope/reconciliation, not proof inferred by this module.
The activation decision must explicitly define the pilot start and whether earlier
separately authorized tests are in scope. Their unknown receipts remain unknown;
excluding them by an explicit new-pilot scope does not reclassify or refund them.
No account-wide audit, credential lookup or real opening value is performed here.

The ordinary daily episode still permits at most the existing three attempts;
this is not a one-send canary executor. A later one-send/no-retry rehearsal must
prove that separate restriction and cannot silently substitute a smaller hold.
Real-data transmission, billing basis, public ledger visibility, transport wiring,
report publication and resumption remain separate release gates.

## Closed one-shot preparation

The internal reserveOneShotGeneration method keeps the ordinary 7,251,456
microUSD hold but durably lowers the SAME original physical reservation limit to
one. It creates no second attempt counter or smaller financial policy. A retryable
or unknown first outcome cannot obtain another token, including after restart.
The ordinary daily reserve remains three attempts. The exact actual provider
label Moonshot AI is retained when present; missing metadata stays unavailable
and reported cost alone does not establish complete billing liability.

The offline full-feed capture helper uses the actual feed parser, source review,
quarantine, model factory and prompt builder. It rejects any changed frozen feed,
performs no article fetching and supplies only a mock HTTP400 to stop before
report production. Its stdout is hashes/counts only. This capture issues no
financial grant and is not yet a complete execution/promotion adapter. Real
source transmission, activated authority, billing proof and explicit output fate
remain required before a real request.

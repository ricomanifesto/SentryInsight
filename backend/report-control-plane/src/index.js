// Worker entry: HTTP routes, the admission Queue consumer, its dead-letter
// consumer and the scheduled handler. Queue batches are dispatched by the
// effective queue names only (queueNames in config.js).

import { ConfigInvalid, settings as readSettings } from "./config.js";
import { now, operation, record } from "./db.js";
import { consume, handleDeadLetter, handleDelivery } from "./delivery.js";
import { fault } from "./faults.js";
import { HEX64 } from "./identity.js";
import { route } from "./router.js";
import { reconcile, scheduledAdmission } from "./sweeper.js";
import { refusal } from "./util.js";

// The operation a well-formed delivery message names, or null.
function namedOperation(body) {
  if (
    body === null ||
    typeof body !== "object" ||
    Object.keys(body).sort().join(",") !== "generation,operation_id" ||
    typeof body.operation_id !== "string" ||
    !HEX64.test(body.operation_id) ||
    !Number.isInteger(body.generation) ||
    body.generation < 1
  ) {
    return null;
  }
  return body.operation_id;
}

// A batch from a queue this Worker does not serve is never acknowledged and
// never reaches a handler. Each message naming a known operation gets one
// fixed-token audit event; neither the queue's name nor the message is
// stored. The whole batch is retried, so the Queue's own bound still owns the
// retries, and a failed diagnostic changes nothing else.
async function unknownQueue(batch, env, settings) {
  try {
    for (const message of batch.messages) {
      const operationId = namedOperation(message.body);
      if (operationId === null) continue;
      await fault(env, "queue_unknown_record");
      if ((await operation(env.PRODUCT_DB, operationId)) !== null) {
        await record(env.PRODUCT_DB, { operationId, kind: "queue_unknown", at: now() });
      }
    }
  } catch {
    // Observability only: the retry below still applies.
  } finally {
    batch.retryAll({ delaySeconds: settings.QUEUE_RETRY_DELAY_S });
  }
}

export default {
  async fetch(request, env) {
    try {
      return await route(request, env);
    } catch {
      return refusal(500, "internal_error");
    }
  },

  async queue(batch, env) {
    let settings;
    try {
      settings = readSettings(env);
    } catch (error) {
      if (!(error instanceof ConfigInvalid)) throw error;
      // The configuration cannot route the batch: retry it, record nothing.
      batch.retryAll();
      return;
    }
    if (batch.queue === settings.queues.dead) {
      await consume(batch, env, settings, async (e, s, body) => {
        await handleDeadLetter(e, s, body);
        return "ack";
      });
      return;
    }
    if (batch.queue === settings.queues.admissions) {
      await consume(batch, env, settings, handleDelivery);
      return;
    }
    await unknownQueue(batch, env, settings);
  },

  async scheduled(controller, env) {
    const settings = readSettings(env);
    await scheduledAdmission(env, settings);
    await reconcile(env, settings, "cron");
  },
};

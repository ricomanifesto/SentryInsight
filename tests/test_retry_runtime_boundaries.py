"""Offline lifecycle regressions for persistence and bounded receipts."""

import asyncio

import httpx
import pytest

from src.core.attempt_budget import AttemptBudgetError, MemoryAttemptBudget
from src.core.failure_receipt import FailureReceiptError, make_receipt, write_receipt
from src.core.opencode_client import parse_model_selection
from src.core.openrouter_client import OpenRouterClient


def test_cancelled_completion_is_uncertain_and_cannot_send_again():
    class CancelledCompletion(MemoryAttemptBudget):
        async def finish(self, *args, **kwargs):
            raise asyncio.CancelledError()

    model = parse_model_selection("openrouter/nvidia/nemotron-3-ultra-550b-a55b:free")
    snapshots = []
    sends = []

    def provider(request):
        sends.append(request)
        return httpx.Response(
            200,
            json={
                "model": model.model_id,
                "choices": [{"message": {"content": "synthetic answer"}}],
            },
        )

    budget = CancelledCompletion()
    client = OpenRouterClient(
        api_key="synthetic",
        attempt_budget=budget,
        transport=httpx.MockTransport(provider),
        on_request=lambda value: snapshots.append(value["state"]),
    )
    arguments = dict(model=model, system_prompt="synthetic", user_prompt="synthetic")
    with pytest.raises(asyncio.CancelledError):
        asyncio.run(client.generate(**arguments))
    assert snapshots == ["reserved", "response_received", "uncertain"]
    assert client.last_request["state"] == "uncertain"
    assert budget.disposition == "reserved"
    with pytest.raises(AttemptBudgetError):
        asyncio.run(client.generate(**arguments))
    assert len(sends) == 1


@pytest.mark.parametrize("existing", [False, True])
def test_oversized_receipt_never_replaces_or_creates_a_file(tmp_path, existing):
    destination = tmp_path / "receipt.json"
    original = None
    if existing:
        write_receipt(destination, make_receipt(None, started=True, environ={}))
        original = destination.read_bytes()
    oversized = make_receipt(
        None, environ={"SENTRYINSIGHT_ADMISSION_KEY": "run:" + "7" * 9000}
    )
    with pytest.raises(FailureReceiptError):
        write_receipt(destination, oversized)
    if existing:
        assert destination.read_bytes() == original
    else:
        assert not destination.exists()
    assert not list(tmp_path.glob(".failure-receipt-*"))

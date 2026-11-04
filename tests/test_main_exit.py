import asyncio
import importlib
import sys
import types
import unittest
import pytest
from unittest.mock import patch


def import_main_with_workflow(result=None, error=None, events=None):
    sys.modules.pop("main", None)
    events = [] if events is None else events

    workflow_module = types.ModuleType("src.core.workflow")

    async def run_exploitation_analysis():
        events.append("workflow")
        if error:
            raise error
        return result

    workflow_module.run_exploitation_analysis = run_exploitation_analysis

    observability_module = types.ModuleType("src.core.observability")
    observability_module.configure_observability = lambda: events.append(
        "observability"
    )

    with patch.dict(
        sys.modules,
        {
            "src.core.observability": observability_module,
            "src.core.workflow": workflow_module,
        },
    ):
        return importlib.import_module("main")


class MainExitTests(unittest.TestCase):
    def test_failed_workflow_exits_nonzero(self):
        main_module = import_main_with_workflow(result={"status": "failed"})

        with self.assertRaises(SystemExit) as context:
            asyncio.run(main_module.main())

        self.assertEqual(context.exception.code, 1)

    def test_workflow_exception_exits_nonzero(self):
        main_module = import_main_with_workflow(error=RuntimeError("boom"))

        with self.assertRaises(SystemExit) as context:
            asyncio.run(main_module.main())

        self.assertEqual(context.exception.code, 1)

    def test_successful_workflow_does_not_exit(self):
        main_module = import_main_with_workflow(result={"status": "completed"})

        asyncio.run(main_module.main())

    def test_entrypoint_configures_observability_before_workflow(self):
        events = []
        main_module = import_main_with_workflow(
            result={"status": "completed"}, events=events
        )

        self.assertEqual(events, [])
        asyncio.run(main_module.main())

        self.assertEqual(events, ["observability", "workflow"])


if __name__ == "__main__":
    unittest.main()


@pytest.fixture(autouse=True)
def isolate_entrypoint_receipts(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("GITHUB_OUTPUT", raising=False)
    monkeypatch.delenv("GITHUB_ACTIONS", raising=False)


def test_ci_entrypoint_refuses_missing_durable_admission(monkeypatch, tmp_path):
    from src.core.failure_receipt import read_receipt

    events = []
    main_module = import_main_with_workflow(
        result={"status": "completed"}, events=events
    )
    monkeypatch.setenv("GITHUB_ACTIONS", "true")
    monkeypatch.delenv("SENTRYINSIGHT_ATTEMPT_STORE", raising=False)
    with pytest.raises(SystemExit):
        asyncio.run(main_module.main())
    assert "workflow" not in events
    receipt = read_receipt(tmp_path / ".sentryinsight-failure.json")
    assert receipt["diagnostic"]["codes"] == ["request_budget_unresolved"]
    assert receipt["retry"]["action"] == "reconcile"

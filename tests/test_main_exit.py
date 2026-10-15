import asyncio
import importlib
import sys
import types
import unittest
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

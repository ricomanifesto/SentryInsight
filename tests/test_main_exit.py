import asyncio
import importlib
import sys
import types
import unittest
from unittest.mock import patch


def import_main_with_workflow(result=None, error=None):
    sys.modules.pop("main", None)

    workflow_module = types.ModuleType("src.core.workflow")

    async def run_exploitation_analysis():
        if error:
            raise error
        return result

    workflow_module.run_exploitation_analysis = run_exploitation_analysis

    rss_module = types.ModuleType("src.services.rss_mcp")
    rss_module.mcp_app = types.SimpleNamespace(run=lambda **_kwargs: None)

    with patch.dict(
        sys.modules,
        {
            "src.core.workflow": workflow_module,
            "src.services.rss_mcp": rss_module,
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


if __name__ == "__main__":
    unittest.main()

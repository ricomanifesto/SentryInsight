from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_workflow_uses_single_sentrydigest_feed_client_boundary():
    workflow_source = (REPO_ROOT / "src/core/workflow.py").read_text(encoding="utf-8")

    assert "SentryDigestFeedClient" in workflow_source
    assert "services.rss_mcp" not in workflow_source
    assert "core.tools" not in workflow_source


def test_removed_duplicate_rss_boundaries_stay_removed():
    assert not (REPO_ROOT / "src/services/rss_mcp.py").exists()
    assert not (REPO_ROOT / "src/core/tools.py").exists()

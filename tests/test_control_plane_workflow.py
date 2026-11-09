"""The report history projection steps never gate generation or deployment."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def workflow(name):
    return (ROOT / ".github" / "workflows" / name).read_text()


def step(text, name):
    start = text.index(f"- name: {name}")
    end = text.find("\n      - name:", start + 1)
    return text[start : end if end != -1 else len(text)]


def test_the_run_is_projected_after_its_outcome_is_recorded_and_never_fails_the_job():
    text = workflow("generate-report.yml")
    generate = step(text, "Generate exploitation report")
    assert "SENTRYINSIGHT_PROJECTION_SNAPSHOT: ${{ runner.temp }}/" in generate
    assert text.index("- name: Record generation outcome") < text.index(
        "- name: Project run into report history"
    )
    project = step(text, "Project run into report history")
    assert "vars.CONTROL_PLANE_URL != ''" in project
    assert "secrets.CONTROL_PLANE_PROJECT_TOKEN" in project
    assert '|| echo "::warning::' in project
    assert "continue-on-error" not in project
    assert "upload-artifact" not in project, "the run snapshot holds article text"


def test_a_deployment_is_observed_only_after_it_succeeded():
    text = workflow("deploy-pages.yml")
    assert text.index("- name: Deploy Pages artifact") < text.index(
        "- name: Record deployment in report history"
    )
    observe = step(text, "Record deployment in report history")
    assert "if: success() && vars.CONTROL_PLANE_URL != ''" in observe
    assert "projection observe" in observe
    assert '|| echo "::warning::' in observe

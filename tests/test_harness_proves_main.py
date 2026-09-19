"""The sandbox's own CI, pinned (DRE-4280).

bureau-harness is the sandbox bureau-pipeline's Integration Harness drives
before the `stable` channel advances: the worker bot pushes a branch, opens a
PR, and the sandbox's real critic and merge gate decide it. `ci.yml` is the
one workflow here that is NOT a pipeline stub — it exists to put a green
check run on every PR head, because the gate fail-closes to `wait` on a head
with no non-review checks (bureau-pipeline `docs/harness.md`).

Before DRE-4280 it fired `on: [push, pull_request]`, so every harness branch
cost two identical runs of the same tree, and the branch-push half never did
anything: the gate wakes only on `workflow_run.event == 'pull_request'`
(bureau-pipeline merge-gate.yml). Measured over 2026-09-01..2026-09-18 that
half was 3,448 runs — 41% of this workflow's own 8,345, 14% of the repo's
24,660; the other 2,990 pushes are to `main` and stay. These tests hold the
file at the scaffold's shape, and hold the runner where it is, so either moves
only by a change that fails here first.
"""

from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[1]
CI = REPO / ".github" / "workflows" / "ci.yml"
MERGE_GATE = REPO / ".github" / "workflows" / "merge-gate.yml"


def workflow(path: Path) -> dict:
    return yaml.safe_load(path.read_text())


def triggers(doc: dict):
    # YAML 1.1 reads a bare `on` key as the boolean True; accept either spelling.
    return doc["on"] if "on" in doc else doc[True]


def test_ci_fires_on_pull_requests_and_pushes_to_main_only():
    on = triggers(workflow(CI))
    assert isinstance(on, dict), (
        f"ci.yml triggers are {on!r} — a bare list fires on every branch push, "
        "duplicating the pull_request run of the same tree"
    )
    assert set(on) == {"pull_request", "push"}, sorted(on)
    assert on["pull_request"] is None or "branches" not in on["pull_request"], (
        "pull_request must stay unrestricted — every harness probe PR needs a "
        "check run on its head"
    )
    assert on["push"] == {"branches": ["main"]}, on["push"]


def test_ci_jobs_stay_on_github_hosted_ubuntu():
    jobs = workflow(CI)["jobs"]
    assert jobs, "ci.yml declares no jobs"
    for name, job in jobs.items():
        assert job.get("runs-on") == "ubuntu-latest", (
            f"job {name!r} runs on {job.get('runs-on')!r}: moving this flood "
            "onto the Mac minis is a decision, not a drive-by"
        )


def test_the_runner_choice_is_explained_where_it_is_made():
    text = CI.read_text()
    head, sep, _ = text.partition("runs-on: ubuntu-latest")
    assert sep, "ci.yml no longer says `runs-on: ubuntu-latest` literally"
    # The comment sits immediately above the line it explains, and names the
    # reason: the mini queue this flood would otherwise drown. Stems, not
    # literals — a faithful reword ("the Mac mini queue", "queues serialise")
    # must still pass; a comment that drops the reason must not.
    above = [l.strip() for l in head.splitlines()[-14:] if l.strip().startswith("#")]
    rationale = " ".join(above).lower()
    assert "mini" in rationale and ("queue" in rationale or "serialis" in rationale), (
        "the comment above runs-on must say why the sandbox stays on "
        "ubuntu-latest — the Mac mini queue it would otherwise flood"
    )


def test_ci_keeps_the_name_the_merge_gate_listens_for():
    ci_name = workflow(CI)["name"]
    listened = triggers(workflow(MERGE_GATE))["workflow_run"]["workflows"]
    assert ci_name in listened, (
        f"ci.yml is named {ci_name!r} but merge-gate.yml wakes on {listened!r}"
    )

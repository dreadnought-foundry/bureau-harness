"""DRE-3145 proof fixture, PR B: this pull request is red on its OWN defect.

It exists to be red. The test below fails on purpose and is not on `main`,
so `test` is green on this branch's merge base. The reconcile sweep's
stale-merge-ref rule must leave this pull request alone ("own"). It must
never merge; it is closed unmerged when the proof is done.
"""


def test_this_pull_request_is_deliberately_broken():
    assert False, "DRE-3145 fixture: PR B's own failure, by design"

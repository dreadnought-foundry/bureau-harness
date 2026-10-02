# DRE-3145 proof fixture, PR A

This pull request is red only because of a fault on `main`. `main` then
fixes it, and the reconcile sweep's stale-merge-ref rule (DRE-3144) should
refresh this branch exactly once.

It carries PR B's head commit on purpose, so the merge gate's stack rule
(DRE-4103) holds it while B stands unapproved. It must never merge, and it
is closed unmerged when the observation is done.

# Integration-harness probe — run pr407-gha-34929149649-1, leg named

Committed by bureau-pipeline's integration harness
(`scripts/harness/`, scenario `gate_paths`) to exercise the live
merge gate. This leg is a worker-authored PR on a dependabot-NAMED branch: the merge
gate must refuse to auto-handle it (only the real dependabot[bot]
earns the dependency policy), post its honest waiting state once,
and otherwise leave it alone. Harness cleanup closes it.

It records nothing and changes no behavior. The harness deletes it
during cleanup; if it is still here, a run crashed mid-flight and
the next run's sweep will remove it.

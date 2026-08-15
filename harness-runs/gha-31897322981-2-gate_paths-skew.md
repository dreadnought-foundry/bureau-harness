# Integration-harness probe — run gha-31897322981-2, leg skew

Committed by bureau-pipeline's integration harness
(`scripts/harness/`, scenario `gate_paths`) to exercise the live
merge gate. This leg is opened deliberately BEHIND its base: the merge gate must update
this branch (as the qa-bot), the follow-up review must pass the
actor allowlists, and the gate then merges normally.

It records nothing and changes no behavior. The harness deletes it
during cleanup; if it is still here, a run crashed mid-flight and
the next run's sweep will remove it.

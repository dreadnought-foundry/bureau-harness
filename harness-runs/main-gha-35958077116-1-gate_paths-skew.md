# Integration-harness probe — run main-gha-35958077116-1, leg skew

Committed by bureau-pipeline's integration harness
(`scripts/harness/`, scenario `gate_paths`) to exercise the live
merge gate. This leg is opened deliberately BEHIND its base: the merge gate must merge it
at the very head it reviewed, without merging the base in first —
freshness is not required and a re-merge would cost a CI run.

It records nothing and changes no behavior. The harness deletes it
during cleanup; if it is still here, a run crashed mid-flight and
the next run's sweep will remove it.

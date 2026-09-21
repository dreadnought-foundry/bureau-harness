# Integration-harness probe — run main-gha-35548141152-1, leg stale

Committed by bureau-pipeline's integration harness
(`scripts/harness/`, scenario `gate_paths`) to exercise the live
merge gate. This leg is after the first approval lands, the harness immediately pushes a
follow-up commit, making that approval stale: the merge gate must
hold until a fresh review covers the new commit.

It records nothing and changes no behavior. The harness deletes it
during cleanup; if it is still here, a run crashed mid-flight and
the next run's sweep will remove it.

Second commit — makes the APPROVE for 477f5f13005a3d63117a64010b25913d6c044b8b stale.

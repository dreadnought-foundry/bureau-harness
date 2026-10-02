"""DRE-3145 proof fixture: a deliberate fault on `main`, for a few minutes.

This file breaks `test` on `main` so that a pull request cut from this
commit goes red on a fault that is not its own. The very next commit on
`main` deletes it. If you are reading this on `main` for longer than a few
minutes, delete the file: it is safe to remove and nothing depends on it.
"""


def test_main_is_deliberately_broken_for_dre_3145():
    assert False, "DRE-3145 fixture: a main-side fault, removed by the next commit"

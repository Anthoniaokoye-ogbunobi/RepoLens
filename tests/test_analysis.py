from repolens.analysis import count_commits

def test_multiple_commits():
    commits = [
    {"message": "Initial commit"},
    {"message": "Add README"},
    {"message": "Fix a bug"}
    ]

    count_commits(commits)
    assert len(commits) == 3


def test_one_commit():
    commits = [
        {"message": "Initial commit"}
    ]

    count_commits(commits)
    assert len(commits) == 1


def test_no_commit():
    commits = []

    count_commits(commits)
    assert len(commits) == 0
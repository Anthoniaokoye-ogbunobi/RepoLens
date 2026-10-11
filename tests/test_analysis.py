from repolens.analysis import count_commits, count_commits_by_author

def test_multiple_commits():
    commits = [
    {"message": "Initial commit"},
    {"message": "Add README"},
    {"message": "Fix a bug"}
    ]

    result = count_commits(commits)
    assert result == 3


def test_one_commit():
    commits = [
        {"message": "Initial commit"}
    ]

    result = count_commits(commits)
    assert result == 1


def test_no_commit():
    commits = []

    result = count_commits(commits)
    assert result == 0


def test_count_commits_by_author():
    commits = [
        {
            "author" : {
                "name" : "Mary",
                "email" : "mary@example.com"
            },
            "message" : "Initial commit"
        },

        {
            "author" : {
                "name" : "Mary",
                "email" : "mary@example.com"
            },
            "message" : "Add README"
        },

        {
            "author" : {
                "name" : "John",
                "email" : "john@example.com"
            },
            "message" : "Fix a bug"
        }
    ]

    commits = count_commits_by_author(commits)

    assert commits == {"John": 1, "Mary": 2}


def test_count_commits_by_single_author():
    commits = [
        {
            "author" : {
                "name" : "Mary",
                "email" : "mary@example.com"
            },
            "message" : "Initial commit"
        },

        {
            "author" : {
                "name" : "Mary",
                "email" : "mary@example.com"
            },
            "message" : "Add README"
        },

        {
            "author" : {
                "name" : "Mary",
                "email" : "mary@example.com"
            },
            "message" : "Fix a bug"
        }
    ]

    result = count_commits_by_author(commits)

    assert result == {"Mary": 3}


def test_count_commits_by_author_with_no_commits():
    commits = []

    result = count_commits_by_author(commits)

    assert result == {}

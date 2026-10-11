from tempfile import TemporaryDirectory
from git import Repo
from pathlib import Path
from repolens.git_history import get_commit_information


def test_get_commit_information():
    with TemporaryDirectory() as directory:
        repo = Repo.init(directory)
        directory = Path(directory)
        file_path = directory / "temporary.txt"
        file_path.write_text("Hello from RepoLens")
        repo.index.add(["temporary.txt"])

        with repo.config_writer() as config:
            config.set_value("user", "name", "John")
            config.set_value("user", "email", "john@example.com")

        commit = repo.index.commit("Initial test commit")

        commits = get_commit_information(repo)
        assert len(commits) == 1
        assert commits[0]["message"].strip() == "Initial test commit"
        assert commits[0]["author"]["name"].strip() == "John"
        assert commits[0]["author"]["email"].strip() == "john@example.com"
        assert commits[0]["hash"] == commit.hexsha
        assert commits[0]["date"] == commit.committed_datetime


def test_get_commit_information_empty_repository():
    with TemporaryDirectory() as directory:
        repo = Repo.init(directory)
        commits = get_commit_information(repo)
        assert commits == []


def test_multiple_commits():
    with TemporaryDirectory() as directory:
        repo = Repo.init(directory)
        directory = Path(directory)
        file_path = directory / "temporary.txt"
        file_path.write_text("Hello from RepoLens")
        repo.index.add(["temporary.txt"])
    
        with repo.config_writer() as config:
            config.set_value("user", "name", "John")
            config.set_value("user", "email", "john@example.com")
    
        commit1 = repo.index.commit("Initial test commit")

        file_path.write_text("Hello again from RepoLens.")
        repo.index.add(["temporary.txt"])

        commit2 = repo.index.commit("Second test commit")

        commits = get_commit_information(repo)

        assert len(commits) == 2
        assert commits[1]["message"].strip() == "Initial test commit"
        assert commits[1]["author"]["name"] == "John"
        assert commits[1]["author"]["email"] == "john@example.com"
        assert commits[1]["hash"] == commit1.hexsha
        assert commits[1]["date"] == commit1.committed_datetime

        assert commits[0]["message"].strip() == "Second test commit"
        assert commits[0]["author"]["name"] == "John"
        assert commits[0]["author"]["email"] == "john@example.com"
        assert commits[0]["hash"] == commit2.hexsha
        assert commits[0]["date"] == commit2.committed_datetime
        
        

        
    
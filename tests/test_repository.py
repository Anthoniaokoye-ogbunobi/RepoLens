from tempfile import TemporaryDirectory
import pytest
from git import Repo
from git.exc import InvalidGitRepositoryError, NoSuchPathError
from repolens.repository import open_repository


def test_open_repository():
    repo = open_repository("/home/chioma_anthonia/RepoLens")
    assert isinstance(repo, Repo)

def test_invalid_repository():
    with TemporaryDirectory() as directory:
        with pytest.raises(InvalidGitRepositoryError):
            open_repository(directory)

def test_non_existent_path():
    with pytest.raises(NoSuchPathError):
        open_repository("/home/chioma_anthonia/non-existent-directory")
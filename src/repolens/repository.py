from git import Repo

def open_repository(path):
    repo = Repo(path)
    return repo 
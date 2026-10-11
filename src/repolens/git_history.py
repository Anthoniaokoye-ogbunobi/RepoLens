def get_commit_information(repo):
    commits_information = []

    if not repo.head.is_valid():
        return commits_information

    for commit in repo.iter_commits():
        commit_info = {
            "hash" : commit.hexsha,
            "message" : commit.message,
            
            "author" : {
                "name" : commit.author.name,
                "email" : commit.author.email
            },

            "date" : commit.committed_datetime
        }
        commits_information.append(commit_info)

    return commits_information
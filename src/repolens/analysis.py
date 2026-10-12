def count_commits(commits):
    return len(commits)


def count_commits_by_author(commits):
    author_count = {}

    for commit in commits:
        author_name = commit["author"]["name"] 
        if author_name in author_count:
            author_count[author_name] += 1
        else:
            author_count[author_name] = 1

    return author_count


def find_most_active_author(author_count):
    if not author_count:
        return None

    return max(author_count, key=author_count.get)
import os
from github import Github

token = os.environ.get("GITHUB_TOKEN")
repo_name = os.environ.get("REPO_NAME")

g = Github(token)
repo = g.get_repo(repo_name)


def check_and_set_repo_visibility(repo, desired_visibility="private"):
    """
       Checks and sets the visibility of a GitHub repository.

       Args:
       - repo (Repository): GitHub repository object obtained from `Github.get_repo`.
       - desired_visibility (str, optional): Desired visibility setting for the repository.
         Possible values: 'public' or 'private'. Defaults to 'private'.

       Exceptions:
       - Handles exceptions when retrieving or modifying repository visibility settings on GitHub.
    """
    try:
        current_visibility = "private" if repo.private else "public"
        print(f"Current repository visibility: {current_visibility}")

        if current_visibility != desired_visibility:
            repo.edit(private=(desired_visibility == "private"))
            print(f"Repository visibility changed to: {desired_visibility}")
        else:
            print("Repository visibility is already set to the desired state.")

    except Exception as e:
        print(f"Failed to check/set repository visibility: {str(e)}")


check_and_set_repo_visibility(repo, "private")

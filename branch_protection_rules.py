import os
from github import Github
from github import GithubException

repo_name = "Roi-Avraham/Cloud-Security"

# Initialize Github instance
g = Github(os.environ.get("GITHUB_TOKEN"))

def check_and_fix_branch_protection(repo_name, branch_name):
    try:
        repo = g.get_repo(repo_name)
        branch = repo.get_branch(branch_name)

        print(f"Checking branch protection for {repo_name}/{branch_name}")

        # Check current protection
        protection = branch.get_protection()

        # Check if pull request reviews are required
        if not protection.required_pull_request_reviews:
            print("Pull request reviews are not required. Fixing...")
            branch.edit_protection(required_approving_review_count=1)
        else:
            print("Pull request reviews are properly configured.")

        # Check if status checks are required
        if not protection.required_status_checks:
            print("Status checks are not required. Fixing...")
            branch.edit_protection(required_status_checks=True)
        else:
            print("Status checks are properly configured.")

        print("Branch protection check and fix completed.")
    except GithubException as e:
        print(f"An error occurred: {e}")
        if e.status == 401:
            print("Authentication failed. Please check your GitHub token.")
        elif e.status == 404:
            print("Repository or branch not found. Please check the repository name and branch.")

# Usage
check_and_fix_branch_protection(repo_name, "main")
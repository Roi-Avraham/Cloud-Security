import os
from github import Github


def check_and_fix_dependency_review(repo, branch_name, access_token):
    """
        Checks and fixes Dependency Review configuration for a GitHub repository branch.

        Args:
        - repo (str): Name of the GitHub repository in the format 'owner/repository'.
        - branch_name (str): Name of the branch to check and fix.
        - access_token (str): Personal access token for GitHub authentication.

        Exceptions:
        - Handles exceptions when retrieving branch protection settings or modifying them on GitHub.
        """
    g = Github(access_token)

    repo = g.get_repo(repo)
    branch = repo.get_branch(branch_name)

    try:
        protection = branch.get_protection()
    except Exception as e:
        print(f"Error retrieving branch protection: {e}")
        return

    # Check for security context
    dependency_review_enabled = False
    required_contexts = protection.required_status_checks.contexts
    for context in required_contexts:
        if context.lower().startswith("security") or context.lower().startswith("vulnerability"):
            dependency_review_enabled = True
            break

    # Print status
    if dependency_review_enabled:
        print("Dependency Review appears to be enabled for this branch.")
    else:
        print("Dependency Review not found in required status checks. Fixing...")

        # Fix by enabling required contexts
        contexts = protection.required_status_checks.contexts + ["security"]
        branch.edit_protection(strict=True, contexts=contexts)

        print("Dependency Review configuration attempted.")


repo = os.getenv("REPO_NAME")
branch_name = os.getenv("BRANCH_NAME")
access_token = os.getenv("GITHUB_TOKEN")

check_and_fix_dependency_review(repo, branch_name, access_token)



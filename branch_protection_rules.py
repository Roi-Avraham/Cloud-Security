import os
from github import Github
from github.GithubException import GithubException

repo_name = os.environ.get("REPO_NAME")
g = Github(os.environ.get("GITHUB_TOKEN"))


def check_and_fix_branch_protection(repo_name, branch_name):
    """
       Checks and fixes branch protection settings for a GitHub repository.

       Parameters:
       - repo_name (str): The name of the GitHub repository.
       - branch_name (str): The name of the branch to check and fix protection settings.

       Exceptions:
       - Handles GitHub exceptions like 401 (authentication failed) and 404 (repository or branch not found).
       - Raises other errors encountered during execution.

    """
    try:
        repo = g.get_repo(repo_name)
        branch = repo.get_branch(branch_name)

        print(f"Checking branch protection for {repo_name}/{branch_name}")

        try:
            protection = branch.get_protection()
            print("Current branch protection settings:")

            pr_reviews = protection.required_pull_request_reviews
            if pr_reviews:
                print(
                    f"- Pull request reviews: Required (Approvals needed: {pr_reviews.required_approving_review_count})")
            else:
                print("- Pull request reviews: Not required")

            print(f"- Enforce on administrators: {protection.enforce_admins}")

            status_checks = protection.required_status_checks
            if status_checks:
                print(f"- Status checks: Required (Strict: {status_checks.strict})")
                print(f"  Contexts: {status_checks.contexts}")
            else:
                print("- Status checks: Not required")

            # Now fix any misconfigured settings
            needs_update = False

            if not pr_reviews or pr_reviews.required_approving_review_count < 1:
                print("\nFixing: Setting required pull request reviews to 1")
                branch.edit_protection(required_approving_review_count=1)
                needs_update = True

            if not protection.enforce_admins:
                print("\nFixing: Enabling enforcement on administrators")
                branch.edit_protection(enforce_admins=True)
                needs_update = True

            if not status_checks:
                print("\nFixing: Enabling required status checks")
                branch.edit_protection(strict=True)
                needs_update = True

            if needs_update:
                print("\nBranch protection has been updated.")
            else:
                print("\nNo fixes needed. Branch protection is correctly configured.")

        except GithubException as e:
            if e.status == 404:
                print("Branch protection not set. Setting up protection rules...")
                branch.edit_protection(
                    required_approving_review_count=1,
                    enforce_admins=True,
                    strict=True,
                    dismiss_stale_reviews=True,
                    require_code_owner_reviews=True
                )
                print("Branch protection has been set up with recommended settings.")
            else:
                raise e

    except GithubException as e:
        print(f"An error occurred: {e}")
        if e.status == 401:
            print("Authentication failed. Please check your GitHub token.")
        elif e.status == 404:
            print("Repository or branch not found. Please check the repository name and branch.")
    except AttributeError as e:
        print(f"AttributeError occurred: {e}")


check_and_fix_branch_protection(repo_name, (os.environ.get("BRANCH_NAME")))

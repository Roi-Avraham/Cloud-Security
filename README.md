# Cloud-Security

Roi Avraham

Answers:

1.b) Five Specific Configurations with Security Impact

1. Branch Protection Rules
   Setup:

   * Require reviews for pull requests before merging.
   * Make sure status checks pass before merging.
   * Limit who can push to the branch.

   How to Check:

   * Use the GitHub API to list and check branch protection rules.

   How to Fix:

   * Automatically set branch protection rules using the GitHub API.

2. Secret Scanning

   Setup:

   * Turn on secret scanning to find exposed secrets in the repository.

   How to Check:

   * Use the GitHub API to verify if secret scanning is enabled.

   How to Fix:

   * Enable secret scanning in the repository settings or via the GitHub API, and address any exposed secrets found.

3. Two-Factor Authentication (2FA) for Collaborators

   Setup:

   * Require all collaborators to use two-factor authentication.

   How to Check:

   * Use the GitHub API to list collaborators and check if they have 2FA enabled.

   How to Fix:

   * Notify users without 2FA and enforce the 2FA requirement through organization policies.

4. Dependency Review and Alerts

   Setup:

   * Enable dependency review and alerts to keep track of vulnerable dependencies.

   How to Check:

   * Use the GitHub API to see if dependency graph and alerts are enabled.

   How to Fix:

   * Turn on dependency review and alerts in the repository settings or via the GitHub API, and update any vulnerable dependencies.

5. Repository Visibility Settings

   Setup:

   Choose who can view your repository:
   * Public: Visible to anyone on the internet.
   * Private: Only visible to you and specified collaborators.
   * Internal: Visible only to members of your organization (for GitHub Enterprise).

   How to Check:

   * Navigate to your repository settings on GitHub.
   * Look for the "Visibility" or "Settings" tab.
   * Verify the current visibility setting displayed.

   How to Fix:

   * Click on the visibility setting.
   * Select the desired option (Public, Private, or Internal).
   * Confirm the change to update the repository's visibility.

Detecting and Fixing Configurations Automatically

To automate the detection and remediation of these configurations, we can use GitHub Actions or scripts that interact with the GitHub API. 

1c) map each of the configurations to one of the compliance categories from NIST:

1. Branch Protection Rules:

* NIST Compliance Category: Configuration Management
  * Explanation: Branch protection rules help ensure that only authorized changes are made to the codebase, 
  which is a key aspect of configuration management.

2. Secret Scanning:

* NIST Compliance Category: System and Information Integrity
  * Explanation: Secret scanning detects and mitigates exposed secrets, helping to maintain the integrity 
  of the system by ensuring sensitive information is not leaked.

3. Two-Factor Authentication (2FA) for Collaborators:

* NIST Compliance Category: Identification and Authentication
  * Explanation: Requiring 2FA enhances the security of user accounts by ensuring 
  that only authorized users can access the repository.
  
4. Dependency Review and Alerts:

* NIST Compliance Category: System and Information Integrity
  * Explanation: Monitoring dependencies for vulnerabilities ensures that the system remains 
  secure by preventing the use of insecure libraries and frameworks.

5. NIST Compliance Category: Access Control 
  * Explanation: Access Control focuses on ensuring that only authorized 
    entities have access to resources and information systems. 
    It encompasses policies, procedures, and mechanisms designed to limit access 
    to information systems and data.

1d) Best Practice Recommendation for Two-Factor Authentication (2FA)

i. What do you recommend as a best practice for this configuration?

  * Enable and enforce two-factor authentication (2FA) for all collaborators on your GitHub repository.
  This adds an extra layer of security by requiring users to verify their identity through a second method(such as 
  a code sent to their mobile device) in addition to their password.

ii. Explain the meaning of this configuration.

 * Two-factor authentication (2FA) is a security process that requires two different forms of identification
   before granting access to an account. In the context of GitHub, this means that even if someone knows my 
   password, they cannot access my account without also having access to the second factor, such as my phone.

iii. What happens when the configuration is not configured according to the best practice, and the risks involved?

 * Without 2FA, my account is only protected by a single password, which can be stolen through various means 
   (e.g., phishing, hacking, or simply guessing weak passwords). If an attacker gains access to a collaborator's 
   account, they can make unauthorized changes to the repository, potentially introducing malicious code, 
   stealing intellectual property, or disrupting project development.

iv. Steps to fix the configuration manually and, if possible, work around these risks in another way.

 * Manual Fix:
    1. Go to GitHub and log in to your account.
    2. Click on your profile picture in the top-right corner and select "Settings".
    3. In the sidebar, click "Security".
    4. Under "Two-factor authentication", click "Enable two-factor authentication".
    5. Follow the instructions to set up 2FA using an authentication app or a hardware security key.
    6. For enforcing 2FA for all collaborators in an organization, go to the organization's settings, 
       click on "Security", and enable the 2FA requirement.
 
 * Workaround: If 2FA cannot be enforced for some reason, use strong,
   unique passwords for each account and consider using a password manager to keep track of them. 
   Regularly monitor account activity for suspicious behavior and set up notifications for 
   important actions in the repository.

v. How will changing the configuration impact working with GitHub?

 * Enabling 2FA will make the login process slightly longer because it requires an additional step. 
   However, it significantly enhances security, reducing the risk of unauthorized access. 
   Collaborators will need to have their second authentication factor (e.g., mobile phone) available when logging in. 
   This change may require some initial adjustment, but the security benefits far outweigh the minor inconvenience.

vi. Related MITRE ATTACK Techniques:
 
  * Technique: T1078 - Valid Accounts
  * This technique involves an attacker using stolen or guessed credentials to gain access to a system. 
    If 2FA is not enabled, an attacker can exploit valid, stolen credentials to access GitHub accounts and repositories.
    When 2FA is not enforced, an attacker who obtains a valid username and password can easily log in to the account and
    perform malicious activities, such as altering code, deleting repositories, or stealing sensitive information. 
    By enabling 2FA, even if the attacker has the credentials, they still cannot access the account without the second 
    factor, thereby preventing unauthorized access and protecting the integrity of your projects.
    By implementing and enforcing 2FA, you add a robust security measure that protects against unauthorized access
    even if passwords are compromised. This proactive step significantly enhances the security of your GitHub 
    repositories and helps safeguard your work against potential attacks.

e) There are 3 scripts: 
 * branch_protection_rules.py: 
   
    Setup:
    - Ensure you have set environment variables:
      - REPO_NAME: Name of the GitHub repository.
      - GITHUB_TOKEN: Personal access token with repository scope.

    Execution:
    - Call check_and_fix_branch_protection(repo_name, branch_name) with appropriate parameters.
    - This script will check the current branch protection settings.
    - If misconfigurations are found (e.g., missing required settings), it will fix them automatically.
    - The script may update branch protection settings, such as requiring pull request reviews, enforcing on administrators,
      and enabling required status checks.

    Impact on GitHub Usage:
    - Running this script may change how branches are protected in your GitHub repository.

<img src="Screenshot 2024-07-09 at 18.52.41 (2).png" alt="Alt text" width="400" height="200">

 
 * dependency_review.py 
    
    Setup:
    - Ensure you have set environment variables:
      - REPO_NAME: Name of the GitHub repository (e.g., 'owner/repository').
      - BRANCH_NAME: Name of the branch to check and fix.
      - GITHUB_TOKEN: Personal access token with 'repo' scope.

    Execution:
      - Call check_and_fix_dependency_review(repo, branch_name, access_token) with appropriate parameters.
      - This script checks if Dependency Review is enabled for the specified branch.
      - If Dependency Review is not configured, it attempts to enable it by adding 'security' to required status checks.
      - Running this script will modify branch protection settings on GitHub to include Dependency Review.

    Impact on GitHub Usage:
      - This script ensures that branches are protected with Dependency Review, which helps identify and fix vulnerabilities in dependencies.
      - It modifies branch protection settings, potentially affecting how pull requests and merges are managed in your GitHub repository.
 
<img src="Screenshot 2024-07-09 at 18.53.54 (2).png" alt="Alt text" width="400" height="200">


* repository_visibility_settings.py
    
   Setup:
  - Ensure you have set environment variables:
    - GITHUB_TOKEN: Personal access token with 'repo' scope.
    - REPO_NAME: Name of the GitHub repository.

  Execution:
  - Call check_and_set_repo_visibility(repo, desired_visibility) with appropriate parameters.
  - This script checks the current visibility of the repository.
  - If the current visibility does not match the desired visibility, it updates the repository visibility.
  - Running this script will change the visibility settings of the GitHub repository.

  Impact on GitHub Usage:
  - Changing repository visibility affects who can view and access the repository.
  - Ensure to review and understand the impact of changing repository visibility on collaboration and security.
  - Public repositories are visible to everyone, while private repositories restrict access to collaborators with permission.

<img src="Screenshot 2024-07-09 at 18.45.23 (2).png" alt="Alt text" width="400" height="200">

2) Managing Misconfigurations in Cloud Infrastructure

a. Framework Description:

This framework helps keep track of and fix mistakes in how cloud services are set up. It works across different types of cloud services like AWS, Azure, Salesforce, and others.

Connecting Services: It connects with cloud services using their tools (like AWS's tools or Salesforce's tools). This lets it check how things are set up.

Managing Settings: It keeps all the important details, like passwords and where things are stored, in one place. This makes it easier to keep everything updated and working right.

Watching How Things Change: It keeps an eye on how services are set up all the time. It does this by asking the services questions and seeing if they match the rules it knows about.

Fixing Problems Automatically: When it sees something wrong, it can fix it right away. This might mean changing a setting or running a special program to make things right.

Telling People About Problems: It sends messages when it finds something wrong. It also keeps a record of what it found and what it did to fix it.

This framework helps make sure cloud services work well and stay safe. It checks things often and fixes problems fast so everything keeps running smoothly.

b. Components in the System

Services: Interfaces with various cloud services using their APIs or SDKs. Each service integration module handles authentication, data retrieval, and remediation tasks specific to the service.

Data Structures: Includes structured representations of service configurations and policies. This may involve JSON, YAML, or database schemas to store and manage configuration states, policies, and remediation scripts.

Databases: Stores metadata, configuration states, logs, and historical data. Utilizes relational databases (e.g., PostgreSQL, MySQL) or NoSQL databases (e.g., MongoDB) depending on scalability and querying needs.


c. Mechanisms for Starting and Watching How Well It Works
Scheduler: It uses a tool like a clock (called cron or Celery) to regularly check and fix things. This might happen at set times, or when something new is added or changed.

Monitoring System: It keeps an eye on how well everything is working. This means checking how fast it gets information and fixes things.

Recording and Numbers: It writes down what happens and counts how well it's doing. This helps see if things are working well and where things might need to change.

These tools help make sure everything keeps running smoothly and fixes problems fast.

d. 
Building in parts means breaking down something complex into reusable pieces. These parts can be used over and over again, which makes it easy to add new features while keeping existing ones functioning properly.

It uses files that store crucial information such as passwords and rules. This setup allows for easy adjustments to how things operate without needing to rewrite code.

The system is resilient and handles errors effectively. For example, if there's a problem communicating with a tool or if something breaks, it tries multiple times to fix the issue before giving up completely.

Security is a priority—it ensures that only authorized people can access and modify important information. It protects sensitive data by encrypting it and restricting access to trusted individuals.

The system provides clear instructions on how to set it up and use it. This could involve improving its functionality or offering training sessions to ensure users understand how to operate it correctly.

Overall, this approach ensures everything functions correctly and remains operational even during unexpected events, maintaining reliability and continuity.















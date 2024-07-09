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

a. Framework Description
The framework is designed to monitor and fix misconfigurations across various cloud services, 
including IaaS (like AWS, Azure), SaaS (like Salesforce, Office 365), and PaaS (like Heroku, Google App Engine). 
Here's how it works:

Service Integration: The framework connects to different cloud services using their APIs. 
This allows it to retrieve data and make changes as needed.

Configuration Management: 
All configuration details, like API tokens and service URLs, are centralized. 
This makes it easy to manage and update these settings.

Monitoring: The system continuously monitors the configurations to detect any issues in 
real-time by comparing the current settings against predefined security policies.

Automated Remediation: When the system detects a misconfiguration, 
it automatically takes steps to fix it, either by using APIs to enforce the correct settings or by running scripts.

Alerting and Reporting: The framework generates alerts and reports about detected issues and the actions taken to fix 
them. These alerts can be sent via email or other monitoring systems.

b. Components in the System
Services: The framework includes modules that interact with each cloud service. 
These modules handle authentication, data retrieval, and remediation tasks specific to each service.

Data Structures: The framework uses structured formats like JSON and YAML to store service configurations, 
policies, and remediation scripts.

Databases: It stores metadata, configuration states, logs, and historical data. 
Depending on the needs, it can use relational databases like PostgreSQL or MySQL, or NoSQL databases like MongoDB.

c. Mechanisms for Initiating and Monitoring Performance
Scheduler: A job scheduler (like cron) initiates periodic checks and remediation tasks based on predefined 
schedules or triggered events (like configuration changes or new deployments).

Monitoring System: The framework includes health checks and performance monitoring for itself. 
It monitors API response times, job execution durations, and system resource usage to ensure everything runs smoothly.

d. Code Structure, Usage, and Other Considerations
Modular Design: The framework is organized into reusable modules for each cloud service integration, 
configuration management, monitoring, and remediation. This makes it easy to add new services and maintain existing ones.

Configuration Files: It uses configuration files (like YAML or JSON) to store service credentials, 
monitoring thresholds, and remediation scripts. This makes it easy to manage and update these settings.

Error Handling and Resilience: The framework includes robust error handling to deal with issues like 
API failures or network problems. It has retry mechanisms to attempt fixes multiple times before giving up.

Security: The framework ensures secure handling of credentials and sensitive data. 
It uses encryption for storing and transmitting credentials and implements role-based access control (RBAC) 
to manage who can access and change different parts of the system.





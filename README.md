# Cloud-Security

Roi Avraham

Answers:

1.b) Five Specific Configurations with Security Impact

1. Branch Protection Rules:

* Configuration: Require pull request reviews before merging, require status checks to pass before merging, and restrict who can push to the branch.
* Detection: Use the GitHub API to list branch protection rules and check for compliance.
* Fix: Automatically apply branch protection rules using the GitHub API.

2. Code Scanning Alerts:

* Configuration: Enable code scanning with GitHub Advanced Security or third-party tools.
* Detection: Use the GitHub API to check if code scanning is enabled and review active alerts.
* Fix: Automate enabling code scanning and fixing identified vulnerabilities through CI/CD pipelines.

3. Secret Scanning:

* Configuration: Enable secret scanning to detect exposed secrets in the repository.
* Detection: Use the GitHub API to verify if secret scanning is enabled.
* Fix: Enable secret scanning through the repository settings or GitHub API, and remediate any found secrets.

4. Two-Factor Authentication (2FA) for Collaborators:

* Configuration: Require all collaborators to enable two-factor authentication.
* Detection: Use the GitHub API to list collaborators and check their 2FA status.
* Fix: Notify users without 2FA and enforce 2FA requirement through organization policies.

5. Dependency Review and Alerts:

* Configuration: Enable dependency review and alerts to monitor vulnerable dependencies.
* Detection: Use the GitHub API to check if dependency graph and alerts are enabled.
* Fix: Enable dependency review and alerts via repository settings or GitHub API, and update vulnerable dependencies.

Detecting and Fixing Configurations Automatically

To automate the detection and remediation of these configurations, you can leverage GitHub Actions or scripts that interact with the GitHub API. Here's an example workflow using GitHub Actions:

1. Setup GitHub Actions:

* Create a .github/workflows/security-checks.yml file in your repository.

2.Define a Workflow for Security Checks:

name: Security Checks

on:
  schedule:
    - cron: '0 0 * * 0'  # Weekly schedule
  workflow_dispatch:

jobs:
  check-security-settings:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Check branch protection rules
      run: |
        curl -H "Authorization: token ${{ secrets.GITHUB_TOKEN }}" \
        https://api.github.com/repos/${{ github.repository }}/branches/main/protection

    - name: Check code scanning alerts
      run: |
        curl -H "Authorization: token ${{ secrets.GITHUB_TOKEN }}" \
        https://api.github.com/repos/${{ github.repository }}/code-scanning/alerts

    - name: Check secret scanning
      run: |
        curl -H "Authorization: token ${{ secrets.GITHUB_TOKEN }}" \
        https://api.github.com/repos/${{ github.repository }}/secret-scanning/alerts

    - name: Check 2FA for collaborators
      run: |
        curl -H "Authorization: token ${{ secrets.GITHUB_TOKEN }}" \
        https://api.github.com/orgs/${{ github.organization }}/members?filter=2fa_disabled

    - name: Check dependency alerts
      run: |
        curl -H "Authorization: token ${{ secrets.GITHUB_TOKEN }}" \
        https://api.github.com/repos/${{ github.repository }}/vulnerability-alerts

3. Remediation Steps:
Based on the output of the checks, use additional steps to enable or configure the required security settings.

1c) map each of the configurations to one of the compliance categories from NIST:

1. Branch Protection Rules:

* NIST Compliance Category: Configuration Management
  * Explanation: Branch protection rules help ensure that only authorized changes are made to the codebase, 
  which is a key aspect of configuration management.

2. Code Scanning Alerts:

* NIST Compliance Category: System and Information Integrity
  * Explanation: Code scanning alerts are designed to identify vulnerabilities and ensure the integrity 
  of the system by preventing insecure code from being deployed.

3. Secret Scanning:

* NIST Compliance Category: System and Information Integrity
  * Explanation: Secret scanning detects and mitigates exposed secrets, helping to maintain the integrity 
  of the system by ensuring sensitive information is not leaked.

4. Two-Factor Authentication (2FA) for Collaborators:

* NIST Compliance Category: Identification and Authentication
  * Explanation: Requiring 2FA enhances the security of user accounts by ensuring 
  that only authorized users can access the repository.

5. Dependency Review and Alerts:

* NIST Compliance Category: System and Information Integrity
  * Explanation: Monitoring dependencies for vulnerabilities ensures that the system remains 
  secure by preventing the use of insecure libraries and frameworks.

1d) Best Practice Recommendation for Two-Factor Authentication (2FA)

i. What do you recommend as a best practice for this configuration?

  * Enable and enforce two-factor authentication (2FA) for all collaborators on your GitHub repository.
  This adds an extra layer of security by requiring users to verify their identity through a second method(such as 
  a code sent to their mobile device) in addition to their password.

ii. Explain the meaning of this configuration.

 * Two-factor authentication (2FA) is a security process that requires two different forms of identification
   before granting access to an account. In the context of GitHub, this means that even if someone knows your 
   password, they cannot access your account without also having access to the second factor, such as your phone or 
   a hardware token.

iii. What happens when the configuration is not configured according to the best practice, and the risks involved?

 * Without 2FA, your account is only protected by a single password, which can be stolen through various means 
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

1e) 


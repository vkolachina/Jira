# User Onboarding/Offboarding Automation

This project automates the process of onboarding and offboarding users for GitHub repositories and organizations, with Jira integration.

## Usage

To onboard a user:
/onboard username org1 org2 owner/repo1 owner/repo2

To offboard a user:
/offboard username org1 org2 owner/repo1 owner/repo2

## Setup

1. Set up the following secrets in your GitHub repository:
   - GITHUB_TOKEN
   - JIRA_API_TOKEN
   - JIRA_BASE_URL
   - JIRA_USER_EMAIL

2. Ensure the GitHub Actions workflow has the necessary permissions to manage repository and organization access.

3. Configure Jira API access and ensure the provided Jira user has the necessary permissions to create and deactivate users.
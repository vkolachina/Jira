import os
import sys
import re
from github_utils import add_user_to_org, add_user_to_repo, remove_user_from_org, remove_user_from_repo
from jira_utils import create_jira_user, deactivate_jira_user


JIRA_BASE_URL = os.getenv('JIRA_BASE_URL')
JIRA_USER_EMAIL = os.getenv('JIRA_USER_EMAIL')
JIRA_API_TOKEN = os.getenv('JIRA_API_TOKEN')

if not all([JIRA_BASE_URL, JIRA_USER_EMAIL, JIRA_API_TOKEN]):
    raise ValueError("One or more Jira environment variables are not set")

def process_command(comment_body):
    command_match = re.match(r'/(\w+)\s+(\S+)\s+(.+)', comment_body)
    if not command_match:
        return "Invalid command format"

    action, username, targets = command_match.groups()
    targets = targets.split()

    if action == 'onboard':
        for target in targets:
            if '/' in target:
                add_user_to_repo(username, target)
            else:
                add_user_to_org(username, target)
        create_jira_user(username)
    elif action == 'offboard':
        for target in targets:
            if '/' in target:
                remove_user_from_repo(username, target)
            else:
                remove_user_from_org(username, target)
        deactivate_jira_user(username)
    else:
        return "Invalid action"

    return f"Successfully processed {action} for {username}"

def main():
    comment_body = os.environ.get('GITHUB_EVENT_COMMENT_BODY')
    if not comment_body:
        print("No comment body found")
        sys.exit(1)

    result = process_command(comment_body)
    print(result)

if __name__ == "__main__":
    main()
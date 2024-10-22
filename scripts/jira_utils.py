import os
from jira import JIRA

JIRA_BASE_URL = os.getenv('JIRA_BASE_URL')
JIRA_USER_EMAIL = os.getenv('JIRA_USER_EMAIL')
JIRA_API_TOKEN = os.getenv('JIRA_API_TOKEN')

jira = JIRA(server=JIRA_BASE_URL, basic_auth=(JIRA_USER_EMAIL, JIRA_API_TOKEN))

def create_jira_user(username):
    user = jira.create_user(username, username + "@example.com", username, "active")
    return user

def deactivate_jira_user(username):
    jira.deactivate_user(username)
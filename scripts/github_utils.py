import os
import requests

GITHUB_API_URL = "https://api.github.com"
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

def github_request(method, url, data=None):
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.request(method, url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()

def add_user_to_org(username, org):
    url = f"{GITHUB_API_URL}/orgs/{org}/memberships/{username}"
    github_request('PUT', url, {"role": "member"})

def add_user_to_repo(username, repo):
    owner, repo_name = repo.split('/')
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo_name}/collaborators/{username}"
    github_request('PUT', url, {"permission": "push"})

def remove_user_from_org(username, org):
    url = f"{GITHUB_API_URL}/orgs/{org}/memberships/{username}"
    github_request('DELETE', url)

def remove_user_from_repo(username, repo):
    owner, repo_name = repo.split('/')
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo_name}/collaborators/{username}"
    github_request('DELETE', url)
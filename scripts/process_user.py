import os
import pandas as pd
from github import Github

def onboard_user(repo, username, email):
    # Add user to the repository
    repo.add_to_collaborators(username, permission='write')
    print(f"Onboarded {username}")

def offboard_user(repo, username):
    # Remove user from the repository
    repo.remove_from_collaborators(username)
    print(f"Offboarded {username}")

def main():
    # Read CSV file
    df = pd.read_csv('users.csv')

    # Authenticate with GitHub
    g = Github(os.getenv('GITHUB_TOKEN'))
    repo = g.get_repo('your_org/your_repo')

    for index, row in df.iterrows():
        if row['action'] == 'onboard':
            onboard_user(repo, row['username'], row['email'])
        elif row['action'] == 'offboard':
            offboard_user(repo, row['username'])

if __name__ == "__main__":
    main()

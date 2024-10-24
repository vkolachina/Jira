import pandas as pd
from github import Github
from ldap3 import Server, Connection, ALL
import os

def read_csv(file_path):
    return pd.read_csv(file_path)

def connect_to_ad(server_address, username, password):
    server = Server(server_address, get_info=ALL)
    conn = Connection(server, username, password, auto_bind=True)
    return conn

def map_users_to_ad(conn, df):
    user_mapping = {}
    for index, row in df.iterrows():
        conn.search('dc=yourdomain,dc=com', f'(sAMAccountName={row["username"]})', attributes=['mail', 'role'])
        if conn.entries:
            user_mapping[row['username']] = {
                'email': conn.entries[0].mail.value,
                'role': conn.entries[0].role.value
            }
    return user_mapping

def onboard_user(repo, username, email, permission='write'):
    repo.add_to_collaborators(username, permission=permission)
    print(f"User {username} with email {email} has been onboarded with {permission} permission.")

def main():
    # Step 1: Read CSV
    df = read_csv('mannequins.csv')

    # Step 2: Connect to Active Directory
    ad_conn = connect_to_ad('your_ad_server', 'your_username', 'your_password')

    # Step 3: Map mannequins to AD
    user_mapping = map_users_to_ad(ad_conn, df)

    # Step 4: Use GitHub API to automate invitations
    g = Github(os.getenv('GITHUB_TOKEN'))
    repo = g.get_repo('your_org/your_repo')

    # Step 5: Onboard users
    for username, info in user_mapping.items():
        try:
            onboard_user(repo, username, info['email'])
        except Exception as e:
            print(f"Failed to onboard {username}: {e}")

if __name__ == "__main__":
    main()

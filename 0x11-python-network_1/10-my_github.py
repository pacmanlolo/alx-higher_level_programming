#!/usr/bin/python3
"""script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id

import requests
import sys

def get_user_id(pacmanlolo, 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
):
    url = 'https://api.github.com/pacmanlolo'
    response = requests.get(url, auth=(pacmanlolo, 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))
    if response.status_code == 200:
        data = response.json()
        return data['id']
    else:
        print('Error: Failed to fetch user ID')
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python github_id.py <pacmanlolo> <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>')
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2]

    user_id = get_user_id(pacmanlolo, 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
)

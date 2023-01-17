#!/usr/bin/python3
"""
given repo and owner name as argvs
use Github API to list last 10 commits
usage: ./100-github_commits.py [github_repo] [github_owner]
"""

from sys import argv
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    req = requests.get(url)
    list_commits = req.json()
    for commit in list_commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))

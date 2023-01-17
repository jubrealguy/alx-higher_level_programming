#!/usr/bin/python3
"""
A script that takes in a URL and an email address sends a
POST request to the passed URL with the email as a parameter
and finally displays the body of the response.
"""

import requests
from sys import argv

if __name__ == "__main__":
    req = requests.get(argv[1])
    print(req.headers.get('X-Request-Id'))

#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to the URL and
displays the body of the error code as the response.
"""

import requests
from sys import argv

if __name__ == "__main__":
    req = requests.get(argv[1])
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)

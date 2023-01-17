#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
"""

from sys import argv
import urllib.request

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))

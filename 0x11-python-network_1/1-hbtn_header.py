#!/usr/bin/python3
"""
A script that takes  in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header of the response
"""

from sys import argv
from urllib.request import urlopen
from urllib.request import Request

if __name__ == "__main__":
    with urlopen(argv[1]) as response:
        val = response.getheader('X-Request-Id')
    print(val)

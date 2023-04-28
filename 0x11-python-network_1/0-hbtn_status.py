#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status and display response
"""

from urllib.request import urlopen

if __name__ == "__main__":
    with urlopen('https://alx-intranet.hbtn.io/status') as response:
        page = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(page)))
        print("\t- content: {}".format(page))
        print("\t- utf8 content: {}".format(page.decode('utf-8')))

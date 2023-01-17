#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status and display response
"""

import urllib.request

if __name__ == "__main__":
    req = urllib.request
    with req.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
#!/usr/bin/python3
"""
A script that fetches https://alx-intranet.hbtn.io/status
using request
"""
import requests

if __name__ == "__main__":
    page = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(page)))
    print("\t- content: {}".format(page))

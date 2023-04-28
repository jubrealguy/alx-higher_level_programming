#!/usr/bin/python3

from urllib.request import urlopen
from sys import argv

with urlopen(argv[1]) as response:
    val = response.getheader('X-Request-Id')
print(val)

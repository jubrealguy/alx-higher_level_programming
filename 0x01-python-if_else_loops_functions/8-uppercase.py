#!/usr/bin/python3
def uppercase(str):
    for alpha in str:
        if (ord(alpha) >= ord('a')) and (ord(alpha) <= ord('z')):
            print("{}".format(chr(ord(alpha) - 32)), end='')
        else:
            print("{}".format(alpha), end='')
    print()

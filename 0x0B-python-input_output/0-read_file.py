#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, mode="r", encoding="Utf-8") as f:
        print(f.read(), end="")

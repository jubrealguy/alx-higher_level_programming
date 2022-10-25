#!/usr/bin/python3
"""
Module 3-write_file
Contains function that writes to a file and returns number of char appended
"""


def append_write(filename="", text=""):
    """writes to txt file and returns number of char appended"""
    with open(filename, mode='a', encoding='utf-8') as f:
        return(f.write(text))

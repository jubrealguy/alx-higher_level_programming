#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b = dict()

    for item in a_dictionary:
        b[item] = a_dictionary[item] * 2

    return b

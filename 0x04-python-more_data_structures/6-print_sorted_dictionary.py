#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    b = list(sorted(a_dictionary))
    for keys in b:
        print(f"{keys}: {a_dictionary[keys]}")

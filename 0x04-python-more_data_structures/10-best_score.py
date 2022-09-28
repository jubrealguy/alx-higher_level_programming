#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        biggest = list(a_dictionary.keys())[0]

        for item in a_dictionary:
            if a_dictionary[item] > a_dictionary[biggest]:
                biggest = item
        return biggest

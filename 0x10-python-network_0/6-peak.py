#!/usr/bin/python3
"""
function that finds the peak of an unsorted integer.
The function will be done recursively for a low conplexity
"""


def find_peak(list_of_integers):
    list_ = list_of_integers
    l = len(list_)
    i = l - 1

    if l == 0:
        return None

    if list_[0] > list_[1]:
        return list_[0]
    if list_[i] > list_[i - 1]:
        return list_[i]

    mid = (0 + i) // 2
    if list_[mid - 1] < list_[mid] and list_[mid + 1] < list_[mid]:
        return list_[mid]

    if list_[mid] < list_[mid-1]:
        return find_peak(list_[0:mid+1])
    elif list_[mid] < list_[mid+1]:
        return find_peak(list_[mid:i+1])
    else:
        return list_[0]

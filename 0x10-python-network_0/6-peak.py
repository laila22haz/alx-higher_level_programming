#!/usr/bin/python3
"""
function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """Find a peak"""
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        return max(list_of_integers)

    for i in range(len(list_of_integers)):
        if (list_of_integers[i] >= list_of_integers[i+1]) and \
           (list_of_integers[i] >= list_of_integers[i-1]):
            return list_of_integers[0]

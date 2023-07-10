#!/usr/bin/python3
"""function that that returns the list"""


def lookup(obj):
    """returns the list of available attributes and methods
       obj : argument
       Return : list
    """

    return (dir(obj))

#!/usr/bin/python3
"""a class check if the object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """Return True in sucsess and False otherwise"""
    return type(obj) is a_class

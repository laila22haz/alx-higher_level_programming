#!/usr/bin/python3
"""a class check if the object is exactly an instance
of the class that inherited from"""


def is_kind_of_class(obj, a_class):
    """Return True in sucsess and False otherwise"""
    return isinstance(obj, a_class)

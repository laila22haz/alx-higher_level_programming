#!/usr/bin/python3
"""a class check if the object is exactly an instance
of the class that inherited (directly or indirectly)"""


def inherits_from(obj, a_class):
    """Return True in sucsess and False otherwise"""
    return issubclass(type(obj), a_class) and type(obj) != a_class

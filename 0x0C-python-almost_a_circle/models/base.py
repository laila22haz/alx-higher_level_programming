#!/usr/bin/python3
"""build a class"""


class Base:
    """this is the base of all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            type(self).id = id
        else:
            type(self).__nb_objects += 1
            type(self).id = type(self).__nb_objects

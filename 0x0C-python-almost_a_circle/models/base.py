#!/usr/bin/python3
"""build a class"""
import json


class Base:
    """this is the base of all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            type(self).id = id
        else:
            type(self).__nb_objects += 1
            type(self).id = type(self).__nb_objects

    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

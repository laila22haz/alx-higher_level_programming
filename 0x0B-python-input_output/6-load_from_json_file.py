#!/usr/bin/python3
"""JSON representation"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file"""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)

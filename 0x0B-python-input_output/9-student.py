#!/usr/bin/python3
# Made by MEGATRON
"""

Contains class Student
that initializes public instance attributes
first_name, last_name, and age,
& has public method to_json that retrieves
its dictionary representation
"""


class Student():
    """
    Public Attributes:
        first_name
        last_name
        age

    Public Methods:
        to_json: retrieves its dictionary representation
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes student with full name & age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns dictionary description with simple data structure
        (list, dictionary, dictionary, str)
        for JSON serialization of an obj
        """
        return self.__dict__

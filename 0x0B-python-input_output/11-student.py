#!/usr/bin/python3
"""

Contains class Student
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

    def to_json(self, attrs=None):
        """
        Returns a dictionary description with simple data structure
        (list, dictionary, dictionary, str)
        for JSON serialization of an obj

        Return:
            Only return dict of attrs given to us
            Return entire dict if no attrs given
        """
        if attrs is None:
            return self.__dict__
        else:
            dic = {}
            for att in attrs:
                if att in self.__dict__.keys():
                    dic[att] = self.__dict__[att]
            return dic

    def reload_from_json(self, json):
        """
        Return:
            Transfer all attributes of json to self
        """
        for k, v in json.items():
            setattr(self, k, v)

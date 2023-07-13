#!/usr/bin/python3
"""build a class"""


Rectangle = __import__('9-rectangly').Rectangle


class Square(Rectangle):
    """class building"""
    def __init__(self, size):
        """initializes size"""
        self.__size = size
        super().integer_validator("size", size)

    def area(self):
        "return the area"
        return self.__width * self.__height

    def __str__(self):
        "return rectangle description"
        return "{[:s]} {:d}/{:d}".format(self.__class__.__name__,
                                         self.__width, self.__height)

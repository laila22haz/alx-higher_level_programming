#!/usr/bin/python3
"""build a class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class building"""
    def __init__(self, width, height):
        self.__width = width
        super().integer_validator("width", width)
        self.__height = height
        super().integer_validator("height", height)

    def area(self):
        "return the area"
        return self.__width * self.__height

    def __str__(self):
        "return rectangle description"
        return "{[:s]} {:d}/{:d}".format(self.__class__.__name__,
                                        self.__width, self.__height)

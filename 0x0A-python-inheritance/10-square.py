#!/usr/bin/python3
"""build a class"""


Rectangle = __import__('9-rectangle').BaseGeometry


class Square(Rectangle):
    """class building"""
    def __init__(self, size):
        self.__size = size
        super().integer_validator("size", size)

    def area(self):
        "return the area"
        return self.__width * self.__height

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
        return self.__width * self.__height

    def str(self):
        print("[Rectangle] {:d}/{:d}".format(self.__width/self.__height))

#!/usr/bin/python3
"""build a class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class building"""
    def __init__(self, width, height):
        self._width = width
        super().integer_validator("width", width)
        self._height = height
        super().integer_validator("height", height)

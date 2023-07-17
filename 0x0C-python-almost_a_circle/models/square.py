#!/usr/bin/python3
"""build class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Sequre Class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialisation of attributes"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """set the size of the Square."""
        self.width = value
        self.height = value


    def __str__(self):
        """str function"""
        class_name = type(self).__name__
        return f"[{class_name}] ({self.id}) {self.x}/{self.y} - {self.width}"


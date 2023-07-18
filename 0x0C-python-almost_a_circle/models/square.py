#!/usr/bin/python3
"""build class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square Class that inherits from Rectangle.

    Attributes:
        id (int): Identifier of the square.
        size (int): Size of the square (equal width and height).
        x (int): x-coordinate of the square's position.
        y (int): y-coordinate of the square's position.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): Size of the square (equal width and height).
            x (int, optional): x-coordinate of the square's position. Defaults to 0.
            y (int, optional): y-coordinate of the square's position. Defaults to 0.
            id (int, optional): Identifier of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the square's attributes with new values.

        Args:
            *args: Variable length argument list. If provided, accepts arguments in the order: id, size, x, y.
            **kwargs: Arbitrary keyword arguments. If provided, accepts arguments as key-value pairs: id=value, size=value, x=value, y=value.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def __str__(self):
        """
        Returns a string representation of the Square.

        The string representation includes the class name, id, x, y, and size of the Square.

        Returns:
            str: String representation of the Square.
        """
        class_name = type(self).__name__
        return f"[{class_name}] ({self.id}) {self.x}/{self.y} - {self.size}"

    def to_dictionary(self):
        """
        Returns the dictionary representation of the Square.

        The dictionary representation includes the id, size, x, and y attributes of the Square.

        Returns:
            dict: Dictionary representation of the Square.
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}


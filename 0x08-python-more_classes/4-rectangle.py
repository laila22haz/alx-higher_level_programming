#!/usr/bin/python3
'''Build a Class'''


class Rectangle:
    '''A class that defines a rectangle'''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        '''property to retrieve the value'''
        return self.__width

    @width.setter
    def width(self, value):
        '''property setter to set it'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''property to retrieve the value'''
        return self.__height

    @height.setter
    def height(self, value):
        '''property setter to set it'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if (self.__width == 0 or self.__height == 0):
            return 0
        else:
            return 2 * (self.__width+self.__height)

    def __str__(self):
        '''print the rectangle with the character #'''
        if self.__height == 0 or self.__width == 0:
            return ("")
        char = []
        for i in range(self.__height):
            [char.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                char.append("\n")
        return ("".join(char))

    def __repr__(self):
        '''print the rectangle with repr function'''
        return ("Rectangle({}, {})".format(self.__width, self.__height))

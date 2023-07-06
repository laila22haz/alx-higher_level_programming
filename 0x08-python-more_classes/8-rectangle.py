#!/usr/bin/python3
'''Build a Class'''


class Rectangle:
    '''A class that defines a rectangle'''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            [char.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                char.append("\n")
        return ("".join(char))

    def __repr__(self):
        '''print the rectangle with repr function'''
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        '''print a message if an instance is deleted'''
        del (self.__height)
        del (self.__width)
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

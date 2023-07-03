#!/usr/bin/python3
'''build a class'''


class Square:
    '''A class Square that defines a square'''
    def __init__(self, size=0):
        '''__init__ intialise the attribute'''
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        '''property to retrieve the value'''
        return self.__size

    @size.setter
    def size(self, value):
        '''property setter to set the value'''
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''method that calcul the square'''
        return self.__size ** 2

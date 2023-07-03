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

    def area(self):
        '''method that calcul the square'''
        return self.__size ** 2

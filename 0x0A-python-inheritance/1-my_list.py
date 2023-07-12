#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """class MyList that inherits from list"""
    def print_sorted(self):
        """function that prints the list, but sorted """
        sorted_list = sorted(self)
        print(sorted_list)

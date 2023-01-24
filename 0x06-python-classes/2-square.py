#!/usr/bin/python3
"""
A class Square with private instance attribute size
that raises an exception if size < 0 or not an integer
"""


class Square:
    """ private instance attr. size that raises error exception """
    def __init__(self, size=0):
        self.__size = size
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

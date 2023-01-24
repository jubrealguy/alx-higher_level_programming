#!/usr/bin/python3
"""
A class square to access and update a private attribute
"""


class Square:
    """ Private instant attribute Size and check errors """
    def __init__(self, size=0):
        self.__size = size

    """Retrieving the size property """
    @property
    def size(self):
        return self.__size

    """ Updating the zsize property to value and checking for errors"""
    @size.setter
    def size(self, value):
        self.__size = value
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    """ Method foir returning area of the square """
    def area(self):
        return self.__size * self.__size

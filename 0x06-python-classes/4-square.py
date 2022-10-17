#!/usr/bin/python3
"""create size function"""


class Square:
    """initialize size"""
    def __init__(self, size=0):
        self.__size = int(size)

    """return size"""
    @property
    def size(self):
        return (self.__size)

    """find root sqr"""
    def area(self):
        return (self.__size * self.__size)

    """add a value"""
    @size.setter
    def size(self, value):
        self.__size = value
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

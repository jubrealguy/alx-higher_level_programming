#!/usr/bin/python3
"""
A class Square with a private instance attribute Size
and a public instance method Area
"""


class Square:
    """
    A private instance attr Size and check for errors"""
    def __init__(self, size=0):
        self.__size = size
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    """Returns the area"""
    def area(self):
        return self.__size * self.__size

#!/usr/bin/python3
"""Return the square"""


class Square:
    """Check for errors"""
    def __init__(self, size=0):
        self.__size = int(size)
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    """Return the square"""
    def area(self):
        return self.__size * self.__size

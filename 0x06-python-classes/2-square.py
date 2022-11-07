#!/usr/bin/python3
"""Creating a Square class with a size value"""


class Square:
    """Create a size value"""
    def __init__(self, size=0):
        self.__size = size
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

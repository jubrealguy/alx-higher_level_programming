#!/usr/bin/python3
"""create squares"""


class Square:
    """initialize size"""
    def __init__(self, size=0):
        self.__size = int(size)

    """return size"""
    @property
    def size(self):
        return (self.__size)

    """return the square"""
    def area(self):
        return (self.__size * self.__size)

    """size"""
    @size.setter
    def size(self, value):
        self.__size = value
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    """print the square"""
    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()

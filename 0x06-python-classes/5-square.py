#!/usr/bin/python3
"""
A class Square that access and updates the private attribute
and print the square
"""


class Square:
    """ Private Instance Attribute Size """
    def __init__(self, size=0):
        self.__size = size

    """ Retrieving the Size property """
    @property
    def size(self):
        return self.__size

    """ Update the size property with value """
    @size.setter
    def size(self, value):
        self.__size = value
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    """ Return the area of the square """
    def area(self):
        return self.__size * self.__size

    """Prints the square with # """
    def my_print(self):
        if self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
        else:
            print()

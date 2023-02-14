#!/usr/bin/python3
"""
A class Square with size attribute and magic methods
"""


class Square:
    """ Private instance attribute """
    def __init__(self, size=0):
        self.size = size

    """ Retrieving the size attribute """
    @property
    def size(self):
        return self.__size

    """ Updating the size attribute and check if type is int """
    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """ Method for area """
    def area(self):
        return self.__size ** 2

    """ Method to check for equality """
    def __eq__(self, other):
        return self.area() == other.area()

    """ Method to check for inequality """
    def __ne__(self, other):
        return self.area() != other.area()

    """ Method to check if an instance is less than another instance """
    def __lt__(self, other):
        return self.area() < other.area()

    """ Method to check if an instance is less or equal to another instance """
    def __le__(self, other):
        return self.area() <= other.area()

    """ Method to check if an instance is greater than another instance """
    def __gt__(self, other):
        return self.area() > other.area()

    """ Method to check if an instance is greater or equals another instance"""
    def __ge__(self, other):
        return self.area() >= other.area()

#!/usr/bin/python3
"""
A class Square with size and position
"""


class Square:
    """ Private instance attribute """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    """ Retrieving Size attribute """
    @property
    def size(self):
        return self.__size

    """ Updating the size attribute and checking if type is int """
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """ Retrieving Position attribute """
    @property
    def position(self):
        return self.__position

    """ Updating position attribute and checking for type as tuple """
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or value[1] < 0 or value[0] < 0\
                or len(value) != 2 or type(value[0])\
                != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    """ Method to get area """
    def area(self):
        return self.__size ** 2

    """ Method that print # in form of the square """
    def my_print(self):
        if self.__size == 0:
            print("")
        for i in range(self.position[1]):
            print("")
        for square in range(self.size):
            print(" " * self.position[0], end="")
            print("#", end="")
            print("")

    """ String representation of the class """
    def __str__(self):
        string = ""
        if self.size == 0:
            return string
        for i in range(self.position[1]):
            string += "\n"
        for square in range(self.size - 1):
            string += " " * self.position[0] + "#" * self.size + "\n"
        string += " " * self.position[0] + "#" * self.size
        return string

#!/usr/bin/python3
"""
A class square prints squarewith # and position with _
"""


class Square:
    """ Private instance attributes """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    """ Retrieving size property """
    @property
    def size(self):
        return self.__size

    """ Updating size property """
    @size.setter
    def size(self, value):
        self.__size = value
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    """ Retrieving position property """
    @property
    def position(self):
        return self.__position

    """ Updating position property """
    @position.setter
    def position(self, value):
        if len(value) != 2 or type(value) is not tuple or \
          value[0] < 0 or value[1] < 0 or \
          type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")

    """ Returns the area of square """
    def area(self):
        return self.__size * self.__size

    """ Prints square with # """
    def my_print(self):
        if self.__size > 0:
            for i in range(self.__size):
                print("_"*self.__position[0], end='')
                for j in range(self.__size):
                    print("#", end='')
                print()
        else:
            print()

#!/usr/bin/python3
"""
A Rectangle that defines a rectangle with private
instance attributes with getter and setter
"""


class Rectangle:
    """ Private instance attributes """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Retrieving width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ Updating value of width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Retrieving height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Updating value of height """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

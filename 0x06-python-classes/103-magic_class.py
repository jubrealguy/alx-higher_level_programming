#!/usr/bin/python3
""" A class MagicClass """
import math


class MagicClass:
    """ Initialize attributes and define methods """
    def __init__(self, radius):
        """ Initializing radius attribute to 0 """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    """ Method to calculate area """
    def area(self):
        return (self.__radius ** 2) * math.pi

    """ Method to calculate Circumference """
    def circumference(self):
        return 2 * math.pi * self.__radius

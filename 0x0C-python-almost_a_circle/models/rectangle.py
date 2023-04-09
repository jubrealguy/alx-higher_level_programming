#!/usr/bin/python3

""" A class Rectangle that inherrits from class Base """

from models.base import Base


class Rectangle(Base):
    """ Rectangle model with four variables: width, height, x, y """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Class instance constructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """ Retriving the width attribute """
    @property
    def width(self):
        return self.__width

    """ Updating the width attribute """
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    """ Retriving the height attribute """
    @property
    def height(self):
        return self.__height

    """ Updating the height attribute """
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    """ Retriving the x attribute """
    @property
    def x(self):
        return self.__x

    """ Updating the x attribute """
    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    """ Retriving the y attribute """
    @property
    def y(self):
        return self.__y

    """ Updating the y attribute """
    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area of the instance """
        return self.__width * self.__height

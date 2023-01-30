#!/usr/bin/python3
"""
A Rectangle that defines a rectangle with private
instance attributes with getter and setter, prints the
shape with # and return the string representation repr
"""


class Rectangle:
    """
    Number of instance of attributes when created and deleted
    print_symbol initialized to # and used as string repr
    """
    number_of_instances = 0
    print_symbol = "#"

    """ Private instance attributes """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    """ Return area of the rectandle """
    def area(self):
        return self.__width * self.__height

    """ Return perimeter of the rectangle """
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    """ Returning the rectamgle with # """
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rec = ""
        for i in range(self.__height):
            if i == self.height - 1:
                rec += (str(self.print_symbol) * self.__width)
            else:
                rec += (str(self.print_symbol) * self.__width) + "\n"
        return rec

    """  Returning a string representation of rectangle instance """
    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    """ Deleting instance of class """
    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

#!/usr/bin/python3

""" A Square model that inherits Rectangle """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ A class square inheriting from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ A class constructor for instance """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ retrieving value for size """
        return self.width

    @size.setter
    def size(self, value):
        """ updating the value for size """
        self.width = value
        self.height = value

    def __str__(self):
        """ A string representation of the instance of the class """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

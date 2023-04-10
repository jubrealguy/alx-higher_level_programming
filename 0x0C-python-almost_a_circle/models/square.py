#!/usr/bin/python3

from models.rectangle import Rectangle

""" A class Square that inherits Rectangle """


class Square(Rectangle):
    """ A class constructor for instance inheriting from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
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

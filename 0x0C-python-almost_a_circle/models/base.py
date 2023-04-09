#!/usr/bin/python3
"""
A class Base
"""


class Base:
    """ Private class attribute """
    __nb_objects = 0
    """ Class instance constructor """
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

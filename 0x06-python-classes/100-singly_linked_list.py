#!/usr/bin/python3
"""
a class Node that defines a node of a singly linked list
"""


class Node:
    """ Private instance attribute """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    """ Retrieving data """
    @property
    def data(self):
        return self.__data

    """ Updating data """
    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = int(value)

    """ Retrieving next node """
    @property
    def next_node(self):
        return self.__next_node

    """ Updating next_node """
    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """ private instance attribute """
    def __init__(self):
        self.__head = None

    def __str__(self):
        """
        string representation of the linked list
        Iterate through the list and return all data in the list
        """
        string = ""
        tmp = self.__head
        while tmp is not None:
            string += str(tmp.data)
            tmp = tmp.next_node
            if tmp is not None:
                string += "\n"
        return string

    def sorted_insert(self, value):
        """ Instert nodes in sorted order """
        new = Node(value)
        if self.__head is None:
            self.__head = new
            return

        tmp = self.__head
        if tmp.data > new.data:
            new.next_node = self.__head
            self.__head = new
            return

        while (tmp.next_node is not None) and (tmp.next_node.data < new.data):
            tmp = tmp.next_node
        new.next_node = tmp.next_node
        tmp.next_node = new
        return

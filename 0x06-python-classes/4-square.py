#!/usr/bin/python3
""""Defines a class Square"""


class Square:
    """"
    This is a class Square that defines a square based on 3-square.py
    """
    def __init__(self, size=0):
        """
        This is a method that initializes/constructs the class
        Args:
            size (int): size of the square
        """
        self.size = size

    @property
    def size(self):
        """
        This is a method that retrieves the size from the property
        and returns the size as value
        return:
            size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This is a method that sets the size of the square
        Args:
            value (int): size of the square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value  # private instance attribute

    def area(self):
        """
        This is a method that returns the current square area
        Args:
            None
        Return:
            area
        """
        return self.__size ** 2

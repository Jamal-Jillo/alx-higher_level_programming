#!/usr/bin/python3
"""
This is a module that defines a class Square
"""


class Square:
    def __init__(self, size=0):
        """
        This is a method that initializes/constructs the class
        Args:
            self - self
            size (int): size of the square
        """
        self.size = size

    @property
    def size(self):
        """
        This is a property that retrieves the size
        return:
            size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """this is a method that sets the size of the square
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

    def my_print(self):
        """
        This is a method that prints in stdout the
        square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print('#' * self.__size)

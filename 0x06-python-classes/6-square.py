#!/usr/bin/python3
"""This is a module that define a class square
"""


class Square:
    """this is a class that defines a square
    Args:
        none
    """
    def __init__(self, size=0, position=(0, 0)):
        """This is a method that initializes the class

        Args:
            size (int): size of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """This is a property that retrieves size
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

    @property
    def position(self):
        """This is a property that sets the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """this is a method that sets the position of the the square

        Args:
            value (int): --
        """
        if type(value) is tuple:
            for i in range(value):
                if i >= 0:
                    self.__position = value  # private instance atrribute
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """This is a method that returns the current square area

        Args:
            None
        Return:
            area
        """
        return self.__size ** 2

    def my_print(self):
        """This is a method that prints in stdout
        the square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print(" ", end="")
                for i in range(self.__size):
                    print("#" * self.__size)

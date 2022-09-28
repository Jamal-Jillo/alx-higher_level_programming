#!/usr/bin/python3
"""A module that contains a class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """sub-class that inherits from Rectangle

    Args:
        Rectangle (_type_): Parent-class
    """

    def __init__(self, size):
        """constructor that holds size

        Args:
            size (_type_):size
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """gets the area of the Square
        """
        return self.__size ** 2

#!/usr/bin/python3
"""this is a module that defines a rectangle based on 0-rectangle.py
    """


class Rectangle:
    """This is a class that defines a rectangle based 0-rectangle"""
    def __init__(self, width=0, height=0):
        """instantiation with optional width and height

        Args:
            width (int, optional): _description_. Defaults to 0.
            height (int, optional): _description_. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width of the rectangle
        """
        return self.__width

    @property
    def height(self):
        """height of the rectangle
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Width setter

        Args:
            value (_type_): _description_
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height setter

        Args:
            value (_type_): _description_
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

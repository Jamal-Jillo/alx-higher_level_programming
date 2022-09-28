#!/usr/bin/python3
"""a module that contains Rectangle class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """subclass that inherits from BaseGeometry

    Args:
        BaseGeometry (_type_): parentclass
    """

    def __init__(self, width, height):
        """constructor that has width and height as instances

        Args:
            width (_type_): width
            height (_type_): height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """gets the area of the shape
        """
        return self.__height * self.__width

    def __str__(self):
        """returns rectangle description
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

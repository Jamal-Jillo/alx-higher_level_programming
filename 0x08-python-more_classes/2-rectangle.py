#!/usr/bin/python3
"""this is a module that defines a rectangle
    """


class Rectangle:
    """this is a class that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """this is a method that defines a rectangle

        Args:
            width (int, optional): _description_. Defaults to 0.
            height (int, optional): _description_. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """this is a method that retrieves the rectangles property
        """
        return self.__width

    @property
    def height(self):
        """this is a method that retrieve the rectangles property
        """
        return self.__height

    @width.setter
    def width(self, value):
        """ this is a method that sets the rectangle property
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """this is a method that sets the retangle property

        Args:
            value (_type_): _description_
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must >= 0")
        self. __height = value

        def area(self):
            """this is a  method that calculates the area

            Returns:
                _type_: _description_
            """
            return self.__width * self.height
        def perimeter(self):
            """ returns rectangle perimiter"""
            if self.__width is 0 or self.__height is 0:
                return 0
            return self.__width * 2 + self.__height * 2   
     
#!/usr/bin/python3
""" Module that contains class
    Rectangle that inherits from Base
"""


from models.base import Base


class Rectangle(Base):
    """Rectangle _summary_

    Arguments:
        Base -- Class that handles Id
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__ Class Constructor

        Arguments:
            width -- width of the rectangle
            height -- height of the rectangle

        Keyword Arguments:
            x -- _description_ (default: {0})
            y -- _description_ (default: {0})
            id -- _description_ (default: {None})
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width Property width
        """
        return self.__width

    @property
    def height(self):
        """height property
        """
        return self.__height

    @property
    def x(self):
        """x property
        """
        return self.__x

    @property
    def y(self):
        """y property
        """
        return self.__y

    @width.setter
    def width(self, value):
        """setter of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height Setter

        Arguments:
            value -- value from property
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """x property

        Arguments:
            value -- of x
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """y property

        Arguments:
            value -- of y
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be  >= 0")
        self.__y = value

    def area(self):
        """area of the rectangle function
        """
        return self.__height * self.__width

    def display(self):
        """display Rectangle using #
        """
        for i in range(self.__height):
            for j in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """__str__ 
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args):
        """update args
        """
        if len(args):
            for i in args:
                if i == 1:
                    self.id = i
                if i == 2:
                    self.width = i
                if i == 3:
                    self.height = i
                if i == 4:
                    self.x = i
                if i == 5:
                    self.y = i

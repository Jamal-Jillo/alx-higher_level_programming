#!/usr/bin/python3
"""This is a module that raises an exception
"""


class BaseGeometry:
    """a class that raises an exception
    """

    def __init__(self):
        """Initializing function
        """
        pass

    def area(self):
        """Exception raised

        Raises:
            Exception: area not implemented
        """
        raise Exception("area() is not implemented")

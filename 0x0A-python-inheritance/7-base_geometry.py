#!/usr/bin/python3
"""A module based on base-geometry
"""


class BaseGeometry:
    """class based on base-geometry
    """

    def __init__(self) -> None:
        """constructor/initializor
        """
        pass

    def area(self):
        """raising an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function that validates 'value'

        Args:
            name (_type_): must be an integer
            value (_type_): must be greater than 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

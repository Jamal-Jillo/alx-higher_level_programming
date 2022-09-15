#!/usr/bin/python3
"""This is a module that contains the class Magicclass
"""


import math


class MagicClass:
    """This is a class that holds the area and the circumference
    """
    def __init__(self, radius=0):
        """This is a method that Initializes/constructs the magicClass
        Args:
            radius (int): radius of a circle Defaults to 0.
        """
        self._MagicClass__radius = 0  # private instance attribute

    def area(self):
        """This is a method that calculates the area of a circle
        """
        return (self._MagicClass__radius ** 2) * math.pi

    def circumference(self):
        """This is a method that calculates the circumference

        Returns:
            circumference
        """
        return (2 * math.pi) * self._MagicClass__radius

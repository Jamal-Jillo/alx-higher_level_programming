#!/usr/bin/python3
"""This module contains a class Square based on 1-square.py"""


class Square:
    """"This class defines a square base on 1-square.py"""
    def __init__(self, size=0):
        """This method initializes/constructs a class Square
        based on 1-square.py
        Args:
            size (int): size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size  # a private instance attribute for size

#!/usr/bin/python3
""" This is a function that returns the list
    available attributes and methods of an object
"""


def lookup(obj):
    """This is  a function that returns the list
    list of a available and methods of an object

    Args:
        obj (_type_):

    Returns:
        _type_: _description_
    """
    return (dir(obj))

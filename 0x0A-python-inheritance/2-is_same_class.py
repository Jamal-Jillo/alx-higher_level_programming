#!/usr/bin/python3
"""Function that checks if the object is exactly
an instance of the specified class
"""


def is_same_class(obj, a_class):
    """Function that checks similarity of object and class

    Args:
        obj (_type_): object
        a_class (_type_): class
    """
    return (type(obj) == a_class)

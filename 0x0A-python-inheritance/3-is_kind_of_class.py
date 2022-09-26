#!/usr/bin/python3
"""Function that checks similarity of object and inherited
    class
"""


def is_kind_of_class(obj, a_class):
    """Above described Function

    Args:
        obj (_type_): object
        a_class (_type_): class inherited
    """
    return (isinstance(obj, a_class))

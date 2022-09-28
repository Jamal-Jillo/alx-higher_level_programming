#!/usr/bin/python3
"""COntains the inherits from function
"""


def inherits_from(obj, a_class):
    """returns true if obj is a subclass pf a_class
    otherwise false

    Args:
        obj (_type_): object
        a_class (_type_): class
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)

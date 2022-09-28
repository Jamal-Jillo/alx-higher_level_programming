#!/usr/bin/python3
"""module that adds contains a class that adds a new attribute
"""


def add_attribute(obj, name, value):
    """Fucntion that checks if an attribute exists

    Args:
        obj (_type_): object
        name (_type_): name
        value (_type_): value
    """
    if isinstance(obj, type):
        setattr(obj, 'name, value')
    else:
        raise TypeError("can't add new attribute")
    #if checker(obj) is True:
    #    setattr(obj, 'name', value)
    #else:
    #    raise TypeError("can't add new attribute")


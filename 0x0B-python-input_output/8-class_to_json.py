#!/usr/bin/python3
""" Module contains:
    class_to_json function that describes objects
"""


def class_to_json(obj):
    """class_to_json Function that returns the dictionary description
    with simple data structure for JSON serialization

    Arguments:
        obj -- An instance of a class
    """
    return obj.__dict__

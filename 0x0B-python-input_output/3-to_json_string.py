#!/usr/bin/python3
""" A module that contains the to_json_string function
    """


import json


def to_json_string(my_obj):
    """to_json_string Returns the JSON representaion
    of an object string

    Arguments:
        my_obj -- object
    """
    return json.dumps(my_obj)

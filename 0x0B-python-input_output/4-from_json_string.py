#!/usr/bin/python3
""" Module that holds from_json_string
    function
"""


import json


def from_json_string(my_str):
    """from_json_string Represents an object by a JSON
    string

    Arguments:
        my_str -- string
    """
    return json.loads(my_str)

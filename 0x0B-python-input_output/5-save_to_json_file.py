#!/usr/bin/python3
""" Module that contains from_json_string
    Function
"""


import json


def from_json_string(my_obj, filename):
    """from_json_string Function that writes an object to
    a txt file using Json representation

    Arguments:
        my_obj -- object
        filename -- filename

    Returns:
        Json representation
    """
    with open(filename, 'w') as file:
        file.write(my_obj)
    return json.dump(my_obj)

#!/usr/bin/python3
""" Module that contains from_json_string
    Function
"""


import json


def save_to_json_file(my_obj, filename):
    """from_json_string Function that writes an object to
    a txt file using Json representation

    Arguments:
        my_obj -- object
        filename -- filename

    Returns:
        Json representation
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)

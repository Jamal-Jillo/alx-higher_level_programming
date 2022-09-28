#!/usr/bin/python3
""" Modulue that contains load_from_json
"""


import json


def load_from_json_file(filename):
    """load_from_json Loads an object from a Json
    file

    Arguments:
        filename -- file name
    """
    with open(filename) as file:
        return json.load(file)

#!/usr/bin/python3
""" Module contains:
    A script that adds args to a python list
    and saves to a list
"""

import json
import sys

# ! Manually tried importing the functions
# def save_to_json_file(my_obj, filename):
#    """from_json_string Function that writes an object to
#    a txt file using Json representation

#    Arguments:
#        my_obj -- object
#        filename -- filename

#    Returns:
#        Json representation
#    """
#    with open(filename, 'w') as file:
#        json.dump(my_obj, file)


# def load_from_json_file(filename):
#    """load_from_json Loads an object from a Json
#    file

#   Arguments:
#   filename -- file name
#   """
#   with open(filename) as file:
#       return json.load(file)


if __name__ == '__main__':
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file =\
        __import__('6-load_from_json_file').load_from_json_file
    #  Line was too long hence the need for front slash

    try:
        data = load_from_json_file('add_item.json')
    except FileNotFoundError:
        data = []
    data.extend(sys.argv[1:])
    save_to_json_file(data, 'add_item.json')

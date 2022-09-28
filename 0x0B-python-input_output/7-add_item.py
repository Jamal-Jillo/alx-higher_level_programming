#!/usr/bin/python3
""" Module contains:
    A script that adds args to a python list
    and saves to a list
"""


import sys


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

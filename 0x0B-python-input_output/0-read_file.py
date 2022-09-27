#!/usr/bin/python3
""" This is a module that holds def read_file(filename="")
"""


def read_file(filename=""):
    """read_file Function that reads a textfile

    Keyword Arguments:
        filename -- name of the file to be read (default: {""})
    """
    with open(filename, 'r') as file:
        print(file.read(), end="")

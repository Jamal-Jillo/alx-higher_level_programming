#!/usr/bin/python3
""" A module that writes a string
"""


def write_file(filename="", text=""):
    """write_file A function that writes and counts the string

    Keyword Arguments:
        filename -- Name of the file (default: {""})
        text -- The string that is being added (default: {""})

    Returns:
        The number of characters written
    """
    with open(filename, 'w') as file:
        file.write(text)
        count = 0
        for c in text:
            count += 1
        return (count)

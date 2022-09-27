#!/usr/bin/python3
""" A module that holds the append_write function
    """


def append_write(filename="", text=""):
    """append_write appends a string to the end of a text file

    Keyword Arguments:
        filename -- txt file (default: {""})
        text -- string (default: {""})
    """
    with open(filename, 'a') as file:
        file.write(text)
        count = 0
        for i in text:
            count += 1
        return (count)

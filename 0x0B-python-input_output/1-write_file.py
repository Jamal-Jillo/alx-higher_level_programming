#!/usr/bin/python3
""" A module that writes a string
"""


def write_file(filename="", text=""):
    with open(filename, 'w') as file:
        file.write(text)
        count = 0
        for c in text:
            count += 1
        return (count)

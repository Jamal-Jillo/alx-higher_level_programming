#!/usr/bin/python3
def remove_char_at(str, n):
    """Remove characters at specified location

    Args:
        str (string)): The string to be changed
        n (char): character to be replaced with

    Returns:
        new_str: The new string
    """
    i = 0
    new_str = ""
    for ch in str:
        if i != n:
            new_str += ch
        i += 1
    return new_str

#!/usr/bin/python3
"""Contains the Mylist class
"""


class MyList(list):
    """This class inherits from list parent class

    Args:
        list (_type_): Parent
    """
    def __init__(self):
        """Initializes the class
        """
        super().__init__

    def print_sorted(self):
        """prints the list
        """
        print(sorted(self))

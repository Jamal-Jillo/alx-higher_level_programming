#!/usr/bin/python3
""" Class Module
"""


class Student:
    """ Student class
    """
    def __init__(self, first_name, last_name, age):
        """__init__ insantiaziation

        Arguments:
            first_name -- _description_
            last_name -- _description_
            age -- _description_
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to_json Retrieves a dictionary representation
        of a student instance

        Keyword Arguments:
            attrs -- attributes (default: {None})
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    new_dict[key] = value
            return new_dict

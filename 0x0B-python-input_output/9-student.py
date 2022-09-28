#!/usr/bin/python3
""" Module contains:
    Class Student
"""


class Student:
    """ Class student
    """

    def __init__(self, first_name, last_name, age):
        """__init__ Instantiation of the class

        Arguments:
            first_name -- first name
            last_name -- last name
            age -- age
        """
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def to_json(self):
        """to_json Retrieves a dictionary
        representation of Student instance
        """
        return Student.__dict__

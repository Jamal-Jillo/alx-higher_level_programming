#!/usr/bin/python3
""" Base class module """


class Base:
    """ Base class Module
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """ __init__ method
        Args:
            id (int): id of the object
        """
        
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

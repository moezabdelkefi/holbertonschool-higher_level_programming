#!/usr/bin/python3
"""define a function inherits_from """


def inherits_from(obj, a_class):
    """ This function first checks if the type of the object
    obj is a subclass of the specified class a_class then checks that obj
    is not exactly an instance of a_class"""
    return issubclass(type(obj), a_class) and type(obj) != a_class

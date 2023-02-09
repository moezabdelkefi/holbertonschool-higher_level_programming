#!/usr/bin/python3
"""define a function class_to_json"""


def class_to_json(obj):
    """ returns the dictionary description with simple data structure"""

    return {key: value for key, value in obj.__dict__.items() if type(value) in (list, dict, str, int, bool)}

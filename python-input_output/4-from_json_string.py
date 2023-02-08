#!/usr/bin/python3
""" defien a function from_json_string"""


import json


def from_json_string(my_str):
    """a function that returns an object"""

    x = json.loads(my_str)
    return x

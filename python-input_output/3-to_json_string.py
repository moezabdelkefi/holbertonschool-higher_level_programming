#!/usr/bin/python3
"""define a function to_json_string"""


def to_json_string(my_obj):
    """f unction that returns the JSON representation of an object"""

    x = json.dumps(my_obj)
    return x

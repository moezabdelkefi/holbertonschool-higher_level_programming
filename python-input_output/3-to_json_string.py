#!/usr/bin/python3
import json
"""define a function to_json_string"""


def to_json_string(my_obj):
    """f unction that returns the JSON representation of an object"""

    x = json.dumps(my_obj)
    return x

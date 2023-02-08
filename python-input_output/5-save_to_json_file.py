#!/usr/bin/python3
""" define a function save_to_json_file"""


import json


def save_to_json_file(my_obj, filename):
    """ a function that writes an Object to a text file"""

    with open(filename, 'w', encoding='utf8') as t:
        t.write(filename)
        t = json.dumps(my_obj)
        return t

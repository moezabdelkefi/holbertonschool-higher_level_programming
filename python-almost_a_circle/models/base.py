#!/usr/bin/python3
"""define a class base"""

import json


class Base:
    """classe base"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        class_name = cls.__name__
        file_name = "{}.json".format(class_name)

        objects = []
        for obj in list_objs:
            objects.append(obj.to_dictionary())

        with open(file_name, "w") as f:
            f.write(cls.to_json_string(objects))

    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or []:
            return []
        else:
            return json.loads(json_string)

#!/usr/bin/python3
""" define a class student"""


class Student:
    """" module class student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ return a dictionary representation of a Student instance"""
        return self.__dict__

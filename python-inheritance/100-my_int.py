#!/usr/bin/python3

"""define a class Myint"""


class MyInt(int):

    """define a class"""
# the __eq__ method is automatically called to
# determine whether the objects are equal or not.
    def __eq__(self, other):
        return int(self) != int(other)

    def __ne__(self, other):
        return int(self) == int(other)

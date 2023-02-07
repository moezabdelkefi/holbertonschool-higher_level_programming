#!/usr/bin/python3
"""define a class Myint"""


class MyInt(int):
    """define a class"""
    def __eq__(self, other):#the __eq__ method is automatically called to determine whether the objects are equal or not.
        return int(self) != int(other)
    
    def __ne__(self, other):
        return int(self) == int(other)

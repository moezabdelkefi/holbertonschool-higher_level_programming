#!/usr/bin/python3
""" define class BaseGeometry"""


class BaseGeometry:
    """creat an empty class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        self.value = value
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """define a class rectangle"""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        if type(height) != int:
            raise TypeError("height must be an integer")
        return None

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def __repr(self):
         return self.__str__()

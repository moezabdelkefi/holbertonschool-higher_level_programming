#!/usr/bin/python3

"""define a class rectangle"""


class Rectangle:
    """represent a rectangle
    raises:
    TypeError: width must be an integer
    ValueError: width must be >= 0
    TypeError: height must be an integer
    ValueError: height must be >= 0

    """

    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        b = self.__width * 2
        c = self.__height * 2
        return (b + c)
    if height == 0 and width == 0:
        perimeter == 0

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = []
        for i in range(self.__height):
            rectangle.append("#" * self.__width)
        return "\n".join(rectangle)
    
    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
    def __del__(self):
        print("Bye rectangle...")

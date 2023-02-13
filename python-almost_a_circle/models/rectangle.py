#!/usr/bin/python3
'''
    define a Class Rectangle
'''


from models.base import Base


class Rectangle(Base):
    """ class Rectangle thata inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__y = y
        self.__x = x
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.setter_validation("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.setter_validation("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.setter_validation("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.setter_validation("y", value)
        self.__y = value

    def setter_validation(self, name, value):
        """Validate the input for the setter methods of the Rectangle class.
         Raises:
        TypeError: If value is not an integer.
        ValueError: If value is <= 0 or < 0 depending on the attribute.
        """

        if type(value) != int:
            raise TypeError(f"{name} must be an integer")

        if name == "width" or name == "height":
            if value <= 0:
                raise ValueError(f"{name} must be > 0")

        if name == "x" or name == "y":
            if value < 0:
                raise ValueError(f"{name} must be >= 0")

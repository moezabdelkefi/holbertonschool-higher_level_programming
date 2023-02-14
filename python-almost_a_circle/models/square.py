#!/usr/bin/python3
""" define a class square that inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):

    """ initialize the attributes of the object"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.size = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]

    def to_dictionary(self):
        """returns the dictionary representation of a square"""

        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y}

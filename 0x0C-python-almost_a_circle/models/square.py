#!/usr/in/python3
'''Define a class square.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Represent a square.'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Initialize a new square.'''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''Set/get size of square.'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        '''Str representaion of a square.'''
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def my_update(self, id=None, size=None, x=None, y=None):
        '''Update my attributes.'''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Update square.'''
        if args:
            self.my_update(*args)
        elif kwargs:
            self.my_update(**kwargs)

    def to_dictionary(self):
        '''Rturns the dictionary representation of a Square.'''
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }

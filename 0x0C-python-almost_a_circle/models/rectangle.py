#!/usr/bin/python3
'''Define Rectangle class.'''
from models.base import Base


class Rectangle(Base):
    '''Represent a rectangle.'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initialize new rectangle.'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''Set/get Rectangle's width.'''
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''Set/get Rectangle's height.'''
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''Set/get x of rectangle.'''
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''Set/get y of rectangle.'''
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''Calculates rectangle's area.'''
        return self.width * self.height

    def display(self):
        '''Print Rectangle instance with #.'''
        L = "\n" * self.y + (" " * self.x + "#" * self.width + "\n")\
            * self.height
        print(L, end="")

    def __str__(self):
        '''Str representation of rectangle.'''
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    def my_update(self, id=None, width=None, height=None, x=None, y=None):
        '''Update attributes with */**args.'''
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Assigns an argument to each attribute.'''
        if args:
            self.my_update(*args)
        elif kwargs:
            self.my_update(**kwargs)

    def to_dictionary(self):
        '''Returns the dictionary representation of a Rectangle.'''
        return {
                "id": self.id,
                "width": self.__width,
                "height": self.__height,
                "x": self.__x,
                "y": self.__y
                }

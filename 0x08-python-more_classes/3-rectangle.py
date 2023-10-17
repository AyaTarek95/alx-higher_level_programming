#!/usr/bin/python3
'''Defines a Rectangle class.'''


class Rectangle:
    '''Represent a Rectangle.'''

    def __init__(self, width=0, height=0):
        '''Initiate a new rectangle.

        Args:
            width (int): the width of rectangle.
            height (int): the height of rectangle.
        '''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''Get/set width of Rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''Get/set height of rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height mush be >= 0')
        self.__height = value

    def area(self):
        '''Return area of Rectangle.'''
        return self.__width * self.__height

    def perimeter(self):
        '''Return perimeter of Rectangle.'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __Str__(self):
        '''Return printable representation of the rectangle.'''
        if self.__width == 0 or self.height == 0:
            return ("")
        newrect = []
        for x in range(self.__height):
            [newrect.append("#") for z in range(self.__width)]
            if x != self.__height - 1:
                newrect.append("\n")
        return ("".join(newrect))

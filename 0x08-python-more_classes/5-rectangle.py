#!/usr/bin/python3
'''Defines a Rectangle class.'''


class Rectangle:
    '''Represent a Rectangle.'''

    def __init__(self, width=0, height=0):
        '''Initiate a new Rectangle.

        Args:
            width (int): the width of rectangle.
            height (int): the height of rectangle.
        '''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''Get/set width of rectangle.'''
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
        '''Get/set height of Rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height mush be >= 0")
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
        '''Return printable representation of the Rectangle.'''
        newrect = []
        if self.__width != 0 and self.__height != 0:
            newrect += "\n".join("#" * self.__width for x in range(self.__height))

        return newrect

    def __repr__(self):
        '''Return string represent the Rectangle.'''
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        '''Print  the message Bye Rectangle.'''
        print("Bye rectangle...")

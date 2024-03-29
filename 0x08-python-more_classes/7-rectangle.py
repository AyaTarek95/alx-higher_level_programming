#!/usr/bin/python3
"""Defines a rectangle class."""


class Rectangle:
    """Represent a Rectangle."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initiate a new rectangle.

        Args:
            width (int): the width of rectangle.
            height (int): the height of rectangle.
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get/set width of rectangle."""
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
        """Get/set height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height mush be >= 0")
        self.__height = value

    def area(self):
        """Return area of rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter of rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return printable representation of the rectangle.

        Print the rectangle with the print_symbol character."""
        if self.width == 0 or self.height == 0:
            return ""

        symbol_list = ""
        for x in range(self.__height):
            for z in range(self.__width):
                symbol_list += str(self.print_symbol)
            if x != self.__height - 1:
                symbol_list += '\n'
        return symbol_list

    def __repr__(self):
        """Return string represent the rectangle."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Print  the message Bye rectangle..."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

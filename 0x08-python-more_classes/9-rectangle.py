#!/usr/bin/python3
"""Defines a rectangle class."""


class Rectangle:
    """Represent a Rectangle."""

    number_of_instances = 0

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

        Print the rectangle with the character '#'.
        """
        newrect = ""
        if self.__width != 0 and self.__height != 0:
            newrect += "\n".join("#" * self.__width
                                 for x in range(self.__height))
        return newrect

    def __repr__(self):
        """Return string represent the rectangle."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Print  the message Bye rectangle..."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size"""
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        if not size >= 0:
            raise ValueError("width must be >= 0")
        return cls(size, size)

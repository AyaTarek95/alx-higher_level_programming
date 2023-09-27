#!/usr/bin/python3

"""create class Square."""

class Square:

    """Represent new Square"""

    def __init__(self, size=0):
        
        """initialize Suare.

        Args:
        size (int): size of new square
        """
        self.size = size

    @property
    def size(self):
        """Get/Set current size of Square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area"""
        return (self.__size ** 2)

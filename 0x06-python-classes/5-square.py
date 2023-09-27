#!/usr/bin/python

"""define class square."""

class Square:

    """represent class square."""

    def __init__(self, size=0):

        """initialize class square.

        Args:
        size (int): current square size.
        """

        self.size = size

    @property
    def size(self):
        """get\set size of square."""
        return self.__size
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return current Square area."""
        return (self.__size ** 2)

    def my_print(self):
        """print in stdout the square with the # character."""
        for x in range(0, self.__size):
            [print("#", end="") for z in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")

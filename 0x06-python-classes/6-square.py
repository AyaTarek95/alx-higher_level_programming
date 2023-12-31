#!/usr/bin/python3

"""Define a class square."""

class Square:
    """Represent a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): the size of the new square.
            position (int, int): the psition of the new sqaure.
        """
        self.size = size
        self.position = position
    
    @property
    def size(self):
        """Get/set the current size of the aquare."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(number, int) for number in value) or
                not all(number >= 0 for number in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return (self.__size ** 2)

    def my_print(self):
        """Prints in stdout the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for x in range(0, self.__position[1])]
        for x in range(0, self.__size):
            [print(" ", end="") for z in range(0, self.__position[0])]
            [print("#", end="") for h in range(0, self.__size)]
            print("")

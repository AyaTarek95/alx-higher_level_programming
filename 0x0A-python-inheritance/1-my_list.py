#!/usr/bin/python3
"""Mylist class."""


class MyList(list):
    """Derived from list."""
    def __init__(self):
        """Initialize the object."""
        super().__init__()

    def print_sorted(self):
        """Print sorted list."""
        print(sorted(self))

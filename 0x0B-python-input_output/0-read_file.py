#!/usr/bin/python3
"""Function that reads a textfile."""

def read_file(filename=""):
    """Read a txt file function."""
    with open(filename, encoding="UTF8") as f:
        print(f.read(), end="")

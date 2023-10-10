#!/usr/bin/python3
"""Define and append function."""


def append_write(filename="", text=""):
    """Function that apend to a file."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

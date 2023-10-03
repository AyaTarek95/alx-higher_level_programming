#!/bin/usr/python3
"""Module of text_indentation methpd."""


def text_indentation(text):
    """print twp lines after  each of these characters: '.', '?' and ':'.

    Args:
        text: string to print.
    Raises:
        TypeError:if text is not str.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for symbol in ".?:":
        text = (symbol + "\n\n").join([line.strip(" ") for line in text.split(symbol)])

    print(text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")

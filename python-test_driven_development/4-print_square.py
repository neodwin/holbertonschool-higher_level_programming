#!/usr/bin/python3
"""
Prints a square with the character #.
"""


def print_square(size):
    """
    size is the size length of the square
    size must be an integer
    Raise a TypeError
    """

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for x in range(size):
        print('#' * size)

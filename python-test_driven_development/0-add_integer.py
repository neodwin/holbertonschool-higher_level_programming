#!/usr/bin/python3
"""
Add intager - function that adds 2 integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats.
    Returns: The sum of a and b, cast to an integer if they are floats.
    Raises: TypeError.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b

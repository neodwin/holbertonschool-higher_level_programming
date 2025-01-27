#!/usr/bin/python3
"""
Module defines a square class with a private instance attribute 'size'.
"""


class Square:
    """
    Class Square that defines a square by: (based on 1-square.py)
    """
    def __init__(self, size=0):
        """
        Initialize a square with size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

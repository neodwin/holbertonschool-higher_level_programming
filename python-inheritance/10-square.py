#!/usr/bin/python3
"""
Module for a rectangle Class.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square that inherits from Rectangle.
    """
    def __init__(self, size):
        """
        Initializes the Rectangle.
        """
        if self.integer_validator("size", size) is None:
            self.__size = size

        super().__init__(size, size)

    def area(self):
        """
        Returns the rectangle area
        """
        return (self.__size * self.__size)

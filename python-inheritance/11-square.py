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

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns the rectangle area.
        """

        return self.__size ** 2

    def __str__(self):
        """
        Returns the square description.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

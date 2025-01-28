#!/usr/bin/python3
"""
Class Rectangle that defines a rectangle.
"""


class Rectangle:
    """
    Class rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle instance.
        """
        self.width = width
        self.height = height

    def __str__(self):
        """
        String conversion.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        string = (('#' * self.__width) + '\n') * self.__height
        return string[:-1]

    @property
    def width(self):
        """
        Width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Width of the rectangle
        """
        if isinstance(value, int) is False:
            raise TypeError("must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Height of the rectangle.
        """
        if isinstance(value, int) is False:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
        Returns the rectangle area.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Returns the rectangle perimeter.
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

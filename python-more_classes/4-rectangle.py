#!/usr/bin/python3
"""
Class Rectangle that defines a rectangle.
"""


class Rectangle:
    """
    Class Rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle instance.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Width of the Rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the rectangle area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the rectangle perimeter.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns the string conversion.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_str = []
        for i in range(self.__height):
            rect_str.append("#" * self.__width)
        return "\n".join(rect_str)

    def __repr__(self):
        """
        Returns a string representation of the rectangle
        to be able to recreate a new instance.
        """
        return f"Rectangle({self.__width}, {self.__height})"

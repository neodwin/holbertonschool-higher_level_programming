#!/usr/bin/python3
"""
class Rectangle that defines a rectangle.
"""


class Rectangle:
    """
    class rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes the Rectangle instance.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        width of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height of the rectangle.
        """
        if isinstance(value, int) is False:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

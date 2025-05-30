#!/usr/bin/python3
"""
class Rectangle that defines a rectangle.
"""


class Rectangle:
    """
    Class Rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle instance.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Width of the rectangle.
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
        Returns the string convertion.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_str = []
        for i in range(self.__height):
            line = "".join(str(self.print_symbol) for _ in range(self.__width))
            rect_str.append(line)
        return "\n".join(rect_str)

    def __repr__(self):
        """
        Returns a string representation of the rectangle
        to be able to recreate a new instance.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Print the message 'Bye rectangle...' when an instance
        of rectangle is deleted and decrement the instance.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

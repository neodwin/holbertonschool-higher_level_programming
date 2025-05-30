#!/usr/bin/python3
"""
Class Rectangle that defines a rectangle.
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
        Returns the string conversion.
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Returns a new Rectangle instance.
        """
        return cls(size, size)

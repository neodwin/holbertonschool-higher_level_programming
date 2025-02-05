#!/usr/bin/env python3
"""
Module defines an abstract class Shape.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract class Shape.
    """
    @abstractmethod
    def area(self):
        """
        The area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        The perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Abstract class Circle.
    """
    def __init__(self, radius):
        """
        Initializes the Circle.
        """
        self.radius = radius

    def area(self):
        """
        Returns the Circle area.
        """
        return math.pi * abs(self.radius) ** 2

    def perimeter(self):
        """
        Returns the Circle perimeter.
        """
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """
    Abstract class Rectangle.
    """
    def __init__(self, width, height):
        """
        Initializes the Rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Returns the Rectangle area.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the Rectangle perimeter.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of the shape.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

#!/usr/bin/python3
"""
Class BaseGeometry
"""


class BaseGeometry:
    """
    BaseGeometry class with public instance methods.
    """

    def area(self):
        """
        Public instance method
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

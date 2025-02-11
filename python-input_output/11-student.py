#!/usr/bin/python3
"""
Class Student that defines a student.
"""


class Student:
    """
    Student class with atributes first name, last name, and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes instance attributes.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        """
        if isinstance(attrs, list):
            if all(isinstance(item, str) for item in attrs):
                filtered_attributes = {}
                for attribute_name in attrs:
                    if hasattr(self, attribute_name):
                        value = getattr(self, attribute_name)
                        filtered_attributes[attribute_name] = value
                return filtered_attributes

        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.
        """
        for key, value in json.items():
            setattr(self, key, value)

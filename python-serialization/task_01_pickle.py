#!/usr/bin/python3
import pickle
"""
CustomObject class capable of serializing instances.
"""


class CustomObject:
    """
    Class CustomObject.
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the attributes.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize instance.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Failed to serialize object: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Return an instance.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception as e:
            print(f"Failed to deserialize object: {e}")
            return None

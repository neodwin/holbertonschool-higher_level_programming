#!/usr/bin/python3
import xml.etree.ElementTree as ET
"""
Functions to serialize a Python dictionary into XML.
"""


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)
    print(f"Dictionary serialized to {filename}")


def deserialize_from_xml(filename):
    """
    Parse the XML file, navigate through the XML elements
    to reconstruct the dictionary.
    Return the constructed dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    result_dict = {}
    for child in root:
        result_dict[child.tag] = child.text

    return result_dict

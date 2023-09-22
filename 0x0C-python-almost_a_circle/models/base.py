#!/usr/bin/python3
"""
Base Class Module

This module defines the Base class for creating objects with unique IDs and
provides methods for JSON serialization and deserialization.
"""

import json

class Base:
    """
    Base Class

    Attributes:
        id (int): The unique identifier for the object.
    
    Class Attributes:
        __nb_objects (int): A class attribute to keep track of the number of objects created.

    Methods:
        __init__(self, id=None): Initializes a new Base instance.
        nb_objects (property): Gets the number of objects created.
        nb_objects (setter): Sets the number of objects created (read-only).
        to_json_string(list_dictionaries): Converts a list of dictionaries to a JSON string.
        save_to_file(cls, list_objs): Saves a list of objects to a JSON file.
        from_json_string(json_string): Loads a list of objects from a JSON string.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new Base instance.

        Args:
            id (int, optional): The unique identifier for the object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @property
    def nb_objects(self):
        """Gets the number of objects created."""
        return self.__nb_objects

    @nb_objects.setter
    def nb_objects(self, value):
        """Sets the number of objects created (read-only)."""
        pass

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: A JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of objects to a JSON file.

        Args:
            list_objs (list): A list of objects to be saved.
        """
        if list_objs is None:
            list_objs = []

        # Determine the filename based on the class name.
        filename = cls.__name__ + ".json"

        # Create a list of dictionaries from the list of objects.
        list_dicts = [obj.to_dictionary() for obj in list_objs]

        # Convert the list of dictionaries to a JSON string.
        json_str = cls.to_json_string(list_dicts)

        # Write the JSON string to the file, overwriting if it exists.
        with open(filename, mode='w', encoding='utf-8') as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        Loads a list of objects from a JSON string.

        Args:
            json_string (str): A JSON string representation of a list of dictionaries.

        Returns:
            list: A list of objects loaded from the JSON string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

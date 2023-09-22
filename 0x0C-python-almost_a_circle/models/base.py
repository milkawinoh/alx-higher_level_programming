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
        __nb_objects (int): A class attribute to keep
          track of the number of objects created.

    Methods:
        __init__(self, id=None): Initializes a new Base instance.
        nb_objects (property): Gets the number of objects created.
        nb_objects (setter): Sets the number of objects created
        (read-only).
        to_json_string(list_dictionaries): Converts a list of
        dictionaries to a JSON string.
        save_to_file(cls, list_objs): Saves a list of objects to a JSON file.
        from_json_string(json_string): Loads a list of objects from
          a JSON string.
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
            json_string (str): A JSON string representation of
            a list of dictionaries.

        Returns:
            list: A list of objects loaded from the JSON string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance with all attributes set based on a dictionary.

        Args:
            **dictionary: A dictionary containing attribute-value pairs.

        Returns:
            Base: An instance with attributes set based on the dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)

        # Use the update method to assign attributes based on the dictionary.
        dummy_instance.update(**dictionary)

        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances based on data from a JSON file.

        Returns:
            list: A list of instances loaded from the JSON file.
        """
        filename = cls.__name__ + ".json"

        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                json_data = file.read()

            # Deserialize the JSON data into a list of dictionaries.
            data_list = cls.from_json_string(json_data)

            # Create instances from the list of dictionaries.
            instances = [cls.create(**data) for data in data_list]

            return instances
        except FileNotFoundError:
            return []

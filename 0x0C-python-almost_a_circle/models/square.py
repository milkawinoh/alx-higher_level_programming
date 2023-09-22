#!/usr/bin/python3
"""
Square Module

A subclass of Rectangle that defines a square.
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Square class is a subclass of Rectangle.

    Attributes:
        size (int): The size of the square.
        x (int): The x-coordinate of the square's position.
        y (int): The y-coordinate of the square's position.
        id (int): The unique identifier for the square.

    Methods:
        __init__(self, size, x=0, y=0, id=None): Initializes a Square instance.
        size (property): Gets the size of the square.
        size (setter): Sets the size of the square.
        __str__(self): Returns a string representation of the square.
        update(self, *args, **kwargs): Updates the attributes of the square.
        to_dictionary(self): Returns a dictionary representation of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square's position.
            y (int, optional): The y-coordinate of the square's position.
            id (int, optional): The unique identifier for the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Gets the size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size to set. Must be a positive integer.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
    
    def update(self, *args, **kwargs):
        """
        Updates the attributes of the square.

        Args:
            *args: Positional arguments representing (id, size, x, y).
            **kwargs: Keyword arguments representing (id, size, x, y).
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the square.

        Returns:
            dict: A dictionary containing the square's attributes.
        """
        return {
            'id': self.id,
            'size': self.size,
            "x": self.x,
            'y': self.y
        }

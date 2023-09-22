#!/usr/bin/python3
"""Rectangle module"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle Class

    A subclass of Base that represents a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle's position.
        y (int): The y-coordinate of the rectangle's position.
        id (int): The unique identifier for the rectangle.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None): Initializes a new Rectangle instance.
        width (property): Gets the width of the rectangle.
        width (setter): Sets the width of the rectangle.
        height (property): Gets the height of the rectangle.
        height (setter): Sets the height of the rectangle.
        x (property): Gets the x-coordinate of the rectangle's position.
        x (setter): Sets the x-coordinate of the rectangle's position.
        y (property): Gets the y-coordinate of the rectangle's position.
        y (setter): Sets the y-coordinate of the rectangle's position.
        area(self): Calculates the area of the rectangle.
        display(self): Displays the rectangle using '#' characters.
        __str__(self): Returns a string representation of the rectangle.
        update(self, *args, **kwargs): Updates the attributes of the rectangle.
        to_dictionary(self): Returns a dictionary representation of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position.
            y (int, optional): The y-coordinate of the rectangle's position.
            id (int, optional): The unique identifier for the rectangle.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """Gets the x-coordinate of the rectangle's position."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x-coordinate of the rectangle's position."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the y-coordinate of the rectangle's position."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y-coordinate of the rectangle's position."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Displays the rectangle using '#' characters.
        """
        for _ in range((self.__y)):
            print()
        for _ in range(self.__height):
            print(self.__x * " " + self.__width * "#")

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: A string in the format "[Rectangle]
            (<id>) <x>/<y> - <width>/<height>"
        """
        return "[{}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__, self.id,
            self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the rectangle.

        Args:
            *args: Positional arguments in the order (id, width, height, x, y).
            **kwargs: Keyword arguments where each key represents an attribute.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the rectangle.

        Returns:
            dict: A dictionary containing the rectangle's attributes.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

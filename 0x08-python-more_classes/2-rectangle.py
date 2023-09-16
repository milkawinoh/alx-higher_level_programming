#!/usr/bin/python3
class Rectangle:
    """no imported module"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__heigth = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(self.__width, int):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__heigth

    @height.setter
    def height(self, value):
        if not isinstance(self.__heigth, int):
            raise TypeError("height must be an integer")
        if self.__heigth < 0:
            raise ValueError("height must be >= 0")
        self.__heigth = value

    def area(self):
        return self.__heigth * self.__width

    def perimeter(self):
        result = 2 * (self.__width + self.__heigth)
        return result
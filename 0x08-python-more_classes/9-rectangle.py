class Rectangle:
    """no imported module"""
    number_of_instances = 0
    print_symbol = "#"
    def __init__(self, width=0, height=0, ):
        self.__width = width
        self.__heigth = height
        Rectangle.number_of_instances += 1
        
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__heigth

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if self.__heigth < 0:
            raise ValueError("height must be >= 0")
        self.__heigth = value

    def area(self):
        return self.__heigth * self.__width

    def perimeter(self):
        result = 2 * (self.__width + self.__heigth)
        return result

    def __str__(self):
        v = ""
        for _ in range(self.__heigth):
            v+= self.print_symbol * self.__width
            v+= "\n"
        return v
    def __repr__(self):
        result= "Rectangle({}, {})".format(self.__width, self.__heigth)
        return result
         
    
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        # Check if rect_1 is an instance of Rectangle
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        # Check if rect_2 is an instance of Rectangle
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        # Compare the areas of rect_1 and rect_2
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
        
    @classmethod
    def square(cls, size=0):
        return cls(size, size)

   
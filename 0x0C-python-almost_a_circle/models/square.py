#!/usr/bin/python3
"""square module.a subclass of rectangle that defines square"""



from models.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        # The getter for size returns either width or height, as they are the same in a square.
        return self.width

    @size.setter
    def size(self, value):
        # The setter for size assigns value to both width and height
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        
        self.width = value
        self.height = value


    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
    
    def update(self, *args, **kwargs):
        if args:
            if len(args) >= 1:
                self.id= args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key,value in kwargs.items():
                setattr(self, key,value)

   
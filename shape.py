class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"Color: {self.color}, and {"Filled" if self.is_filled else 'Not Filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It's a circle with area of {3.14 * self.radius * self.radius} cm^2")
        super().describe()

class Rectangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"It's a rectangle with area of {2 * self.width + 2 * self.height} cm^2")
        super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height
    def describe(self):
        print(f"It's a triangle with area of {self.width * self.height/ 2} cm^2")
        super().describe()
    

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width
    
    def describe(self):
        print(f"It's a Square with area of {self.width * self.width} cm^2")
        super().describe()
        
    

circle = Circle("red", True, 5)
square = Square("blue", True, 10)
triangle = Triangle("green", True, 5, 10)

rectangle = Rectangle("yellow", True, 10, 5)

print(f"{square.color}")
print(f"{square.is_filled}")
print(f"{square.width}")

circle.describe()

triangle.describe()
rectangle.describe()
square.describe()

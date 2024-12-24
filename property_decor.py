# Property Decorators

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height



    # getter method to read
    @property
    def width(self):
        return f"{self._width:.1f}cm"
    
    @property
    def height(self):
        return f"{self._height:.1f}cm"

    # setter method to write
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be a greater than zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be a greater than zero")


    # deleter method to delete
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")


rectangle = Rectangle(5, 10)

print(rectangle._width)
print(rectangle._height)
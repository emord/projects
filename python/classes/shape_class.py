#!/usr/bin/python
"""
Create an abstract class called Shape and then inherit from it other shapes
like diamond, rectangle, circle, triangle etc. Then have each class override
the area and perimeter functionality to handle each shape type.
"""
import math

class Shape(object):
    """
    Generic Shape object
    """
    def area(self):
        """
        Area of shape
        """
        pass

    def perimeter(self):
        """
        Perimeter of shape
        """
        pass

class Square(Shape):
    """
    Basic square class
    """
    def __init__(self, side_length):
        self.side = side_length

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return self.side * 4

class Rectangle(Shape):
    """
    Basic rectangle class
    """
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Circle(Shape):
    """
    Basic circle class
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius

def main():
    """
    Displays inheritance methods
    """
    rect = Rectangle(5, 4)
    print("Rectangle(5, 4)")
    print("  Area: " + str(rect.area()))
    print("  Perimeter: " + str(rect.perimeter()))

    square = Square(5)
    print("Square(5)")
    print("  Area: " + str(square.area()))
    print("  Perimeter: " + str(square.perimeter()))

    circle = Circle(5)
    print("Circle(5)")
    print("  Area: " + str(circle.area()))
    print("  Perimeter: " + str(circle.perimeter()))

if __name__ == '__main__':
    main()

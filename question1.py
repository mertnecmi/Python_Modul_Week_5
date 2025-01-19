#Question1: Create a Python class called "Rectangle" that represents a rectangle. The Rectangle class must have the following 
# properties and methods:

# Features:
# width (an integer)
# height (an integer)
# Methods:
# area(self): A method that calculates and returns the area of ​​the rectangle.
# perimeter(self): A method that calculates and returns the perimeter of the rectangle.
# Create an instance of Rectangle class, set its width to 5 and height to 7, then print its area and perimeter.


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """berekent de oppervlakte van een vierhoek"""
        return self.width * self.height

    def perimeter(self):
        """berekent de omtrek van een vierhoek"""
        return 2 * (self.width + self.height)

vierkant = Rectangle(5,7)

print("Area:", vierkant.area(),"eenheid")
print("Perimeter:", vierkant.perimeter(),"eenheid")

#Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle



class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rect = Rectangle(10, 5)

print(f"Area of the rectangle: {rect.area()}") 
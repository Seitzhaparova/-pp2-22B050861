class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width
class Rectangle(Shape):
    def area(self):
        a = self.length * self.width
        print(a)
m = Rectangle(5,4)
m.area()